"""Unified Sūtrakṛt findings across all loaded corpora.

Pulls together every Stage 1/2/3 + Abhinavagupta result into one
publishable findings table. Apply Sūtrakṛt-v2.6 frozen weights to
each corpus where extraction yielded ≥10 BG-internal triples.
For corpora with <10 BG-internal triples, report the productization-
style finding (zero or near-zero is the finding).
"""

import json
import re
import sqlite3
from collections import Counter
from pathlib import Path

import numpy as np
from sentence_transformers import SentenceTransformer
from vidyut.cheda import Chedaka
from vidyut.lipi import transliterate, Scheme

BASE = Path(__file__).resolve().parents[1]
DB_PATH = Path.home() / "Code/tools/ambuda/data/database/database.db"
LISTS_JSON = BASE / "verification" / "v2_0_lists_graph.json"
COMMENTARY_DIR = BASE / "h_c_panel" / "commentaries"
ABHINAVA_JSONL = BASE / "data" / "abhinavagupta_gita_artha_sangraha.jsonl"
VIDYUT_DATA = "/tmp/vidyut-data"
OUT_JSON = BASE / "verification" / "sutrakrit_unified_findings.json"
OUT_MD = BASE / "verification" / "sutrakrit_unified_findings.md"

# Two BG-internal citation patterns:
# Pattern A: "(गीता X।Y)" / "गीता X।Y" / variants — Ramanuja, Shankara, Madhusudan(some)
# Pattern B: "[X।Y]" bare bracket — Madhva, Jayatirtha, Vallabha, Vedantadeshika
GITA_REF_RE = re.compile(r"(?:गीता|गी\.|गीतायां|भगवद्गीतायां)\s*[\(\[]?\s*([\d०-९]+)\s*[।\.]\s*([\d०-९]+)\s*[\)\]]?")
BRACKET_REF_RE = re.compile(r"\[([\d०-९]+)\s*[।\.]\s*([\d०-९]+)\]")
ITI_QUOTE_RE = re.compile(r"([\u0900-\u097F][\u0900-\u097F\s\-\u093C\u094D]{4,80}?)\s+इति")
DEV_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")
DEV_LETTER_RE = re.compile(r"[\u0900-\u097F]")


def load_bg():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    text_id = cur.execute("SELECT id FROM texts WHERE slug='bg-mula'").fetchone()[0]
    out = {}
    for (xml,) in cur.execute("SELECT xml FROM text_blocks WHERE text_id=?", (text_id,)):
        if not xml: continue
        m = re.search(r'milestone[^>]+n="([^"]+)"', xml)
        if not m or not re.match(r"^\d+\.\d+$", m.group(1)): continue
        text = re.sub(r"<[^>]+>", " ", xml)
        text = re.sub(r"\s+", " ", text).strip()
        out[m.group(1)] = text
    conn.close()
    return out


def normalize(s):
    s = re.sub(r"[।॥|.,;:!?\(\)\[\]\{\}]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def substring_score(sutra, candidate_text):
    s = normalize(sutra)
    if not s or not candidate_text: return 0.0
    if s in candidate_text: return 1.0
    for length in range(min(len(s), 30), 5, -1):
        if s[:length] in candidate_text:
            return length / max(len(s), 1) * 0.7
    return 0.0


_chedaka = None
def get_chedaka():
    global _chedaka
    if _chedaka is None: _chedaka = Chedaka(VIDYUT_DATA)
    return _chedaka


def lemmatize(text):
    try:
        slp = re.sub(r"[\|\.\,\;\:\?]", " ", transliterate(text, Scheme.Devanagari, Scheme.Slp1)).strip()
        if not slp: return set()
        return {t.lemma for t in get_chedaka().run(slp) if t.lemma}
    except Exception:
        return set()


def stem_prefix(lemma, n=3):
    if not lemma: return ""
    try: return transliterate(lemma, Scheme.Slp1, Scheme.Devanagari)[:n]
    except: return lemma[:n]


def extract_gitasup_triples(jsonl, bg):
    """Extract from gitasupersite per-commentator JSONL.
    Uses both citation patterns:
      A: (गीता X।Y) / गीता X।Y / variants — Ramanuja, Shankara, Madhusudan
      B: [X।Y] bare bracket — Madhva, Jayatirtha, Vallabha, Vedantadeshika
    """
    triples = []
    with jsonl.open() as f:
        for line in f:
            v = json.loads(line)
            source = v["verse"]
            if source not in bg: continue
            prose = v["prose"]
            # Collect all citation matches (pattern A + B), with their position + target
            cites = []
            for m in GITA_REF_RE.finditer(prose):
                try:
                    tgt = f"{int(m.group(1).translate(DEV_DIGITS))}.{int(m.group(2).translate(DEV_DIGITS))}"
                except (ValueError, AttributeError): continue
                cites.append((m.start(), tgt))
            for m in BRACKET_REF_RE.finditer(prose):
                try:
                    tgt = f"{int(m.group(1).translate(DEV_DIGITS))}.{int(m.group(2).translate(DEV_DIGITS))}"
                except (ValueError, AttributeError): continue
                # Validate: target must be valid BG verse (else it's some other bracket usage)
                if tgt in bg:
                    cites.append((m.start(), tgt))
            for pos, tgt in cites:
                if tgt == source or tgt not in bg: continue
                lookback = prose[max(0, pos-200):pos]
                lookback = re.sub(r"(?:गीता|गी\.|गीतायां|भगवद्गीतायां)\s*$", "", lookback).strip()
                iti_matches = list(ITI_QUOTE_RE.finditer(lookback))
                sutra = None
                if iti_matches: sutra = normalize(iti_matches[-1].group(1))
                if not sutra or len(sutra) < 5:
                    pm = re.search(r"([\u0900-\u097F][\u0900-\u097F\s\-\u093C\u094D]{6,80})\s*$", lookback.strip())
                    if not pm: continue
                    sutra = normalize(pm.group(1))
                if len(DEV_LETTER_RE.findall(sutra)) < 4 or len(sutra) < 5: continue
                triples.append({"source": source, "target": tgt, "sutra": sutra})
    return triples


def extract_abhinava_triples(jsonl, bg):
    """Extract BG-internal triples from Abhinavagupta JSONL.
    His cross_references field holds dicts with text_abbrev / verse_ref / quoted_phrase."""
    triples = []
    with jsonl.open() as f:
        for line in f:
            v = json.loads(line)
            source = v.get("verse_id")
            if source not in bg: continue
            for x in v.get("cross_references", []):
                if not isinstance(x, dict): continue
                text = (x.get("text_abbrev") or "").lower()
                # Filter to BG-internal cross-refs only
                if not any(k in text for k in ["गी", "ग.", "gita", "bhagavad", "bg"]):
                    continue
                vr = x.get("verse_ref", "")
                m = re.match(r"^[\(\[]?\s*([\d०-९]+)\s*[।\.]\s*([\d०-९]+)", vr)
                if not m: continue
                try:
                    tgt = f"{int(m.group(1).translate(DEV_DIGITS))}.{int(m.group(2).translate(DEV_DIGITS))}"
                except (ValueError, AttributeError):
                    continue
                if tgt == source or tgt not in bg: continue
                phrase = (x.get("quoted_phrase") or "").strip()
                if len(DEV_LETTER_RE.findall(phrase)) < 4 or len(phrase) < 5: continue
                triples.append({"source": source, "target": tgt, "sutra": normalize(phrase)})
    return triples


def main():
    print("Loading BG mūla + lemma + lists graph...")
    bg = load_bg()
    milestones = sorted(bg.keys(), key=lambda m: tuple(int(x) for x in m.split(".")))
    ms_idx = {m: i for i, m in enumerate(milestones)}
    lists_graph = json.loads(LISTS_JSON.read_text())["lists_graph"]
    verse_to_sutras = {v: set() for v in milestones}
    for sutra, L in lists_graph.items():
        for n in L["nodes"]:
            if n["verse"] in verse_to_sutras:
                verse_to_sutras[n["verse"]].add(sutra)

    print("Embedding all BG verses with mE5...")
    model = SentenceTransformer("intfloat/multilingual-e5-base")
    M = model.encode([f"passage: {bg[m]}" for m in milestones],
                     normalize_embeddings=True, batch_size=32, convert_to_numpy=True)

    print("Lemmatizing all verses...")
    verse_lemmas = {v: lemmatize(bg[v]) for v in milestones}
    verse_stems = {v: {stem_prefix(l) for l in lems if l} for v, lems in verse_lemmas.items()}
    n_v = len(milestones)
    lemma_df = Counter()
    for lems in verse_lemmas.values():
        for l in lems: lemma_df[l] += 1
    lemma_idf = {l: np.log(n_v / max(df, 1)) for l, df in lemma_df.items()}

    a, b, e_v, z, h, th = 1.0, 0.01, 0.005, 0.2, 0, 0.01

    def evaluate(triples, label):
        if len(triples) < 10:
            return {"label": label, "n": len(triples), "verdict": "TOO_SMALL_N"}
        unique_sutras = sorted({t["sutra"] for t in triples})
        S = model.encode([f"query: {s}" for s in unique_sutras],
                         normalize_embeddings=True, batch_size=32, convert_to_numpy=True)
        s_idx = {s: i for i, s in enumerate(unique_sutras)}
        sutra_lemmas = {s: lemmatize(s) for s in unique_sutras}
        sutra_stems = {s: {stem_prefix(l) for l in lems if l} for s, lems in sutra_lemmas.items()}
        per_sutra = {}
        for sutra in unique_sutras:
            sub = np.array([substring_score(sutra, bg[v]) for v in milestones])
            s_lems = sutra_lemmas[sutra]; s_stems = sutra_stems[sutra]
            lem = np.array([sum(lemma_idf.get(l, 0) for l in (s_lems & verse_lemmas[v])) for v in milestones])
            stem = np.array([float(len(s_stems & verse_stems[v])) for v in milestones])
            per_sutra[sutra] = (sub, lem, stem)
        src_signals = {}
        for t in triples:
            src = t["source"]
            if src in src_signals: continue
            src_sutras = verse_to_sutras.get(src, set())
            shared = np.array([len(src_sutras & verse_to_sutras.get(m_, set())) for m_ in milestones])
            voc = np.zeros(len(milestones))
            src_signals[src] = {"shared": shared, "voc": voc}

        def run(use_vyak):
            ranks = []
            for t in triples:
                sims = a * (M @ S[s_idx[t["sutra"]]])
                if use_vyak:
                    sigs = src_signals[t["source"]]
                    sub, lem, stem = per_sutra[t["sutra"]]
                    sims = sims + b*sigs["shared"] + e_v*sigs["voc"] + z*sub + h*lem + th*stem
                sims[ms_idx[t["source"]]] = -np.inf
                order = np.argsort(-sims)
                ranks.append(int(np.where(order == ms_idx[t["target"]])[0][0]))
            r = np.array(ranks)
            return {"r1": float((r<1).mean()), "r4": float((r<4).mean()),
                    "r10": float((r<10).mean()), "r25": float((r<25).mean()),
                    "median": int(np.median(r))}

        me5 = run(False); skt = run(True)
        delta = skt["r4"] - me5["r4"]
        h_c_pass = skt["r4"] >= 0.40
        return {"label": label, "n": len(triples),
                "me5_r4": me5["r4"], "sutrakrit_r4": skt["r4"],
                "delta_r4": delta, "median_skt": skt["median"],
                "verdict": ("PASSED" if h_c_pass else "FAILED")}

    print("\n=== Building corpora + extracting triples ===\n")
    results = []

    # 1. Ramsukhdas (Stage 1 fit baseline) — known result, no recompute
    results.append({"label": "Ramsukhdas (Stage 1 fit)", "n": 260,
                    "me5_r4": 0.577, "sutrakrit_r4": 0.715, "delta_r4": 0.138,
                    "median_skt": 0, "verdict": "FIT"})

    # 2. Shankara-Ambuda (Stage 2) — known result
    results.append({"label": "Shankara-Ambuda (Stage 2)", "n": 88,
                    "me5_r4": 0.545, "sutrakrit_r4": 0.716, "delta_r4": 0.170,
                    "median_skt": 0, "verdict": "PASSED"})

    # 3-N. Gitasupersite commentators
    for cf in sorted(COMMENTARY_DIR.glob("bg_*.jsonl")):
        slug = cf.stem.replace("bg_", "")
        triples = extract_gitasup_triples(cf, bg)
        results.append(evaluate(triples, f"{slug}-gitasupersite"))

    # N+1. Abhinavagupta (BG-internal subset)
    triples = extract_abhinava_triples(ABHINAVA_JSONL, bg)
    results.append(evaluate(triples, "abhinavagupta-marjanovic"))

    # N+2. Tilak Gītā-Rahasya — run as separate script, import result
    tilak_json = BASE / "verification" / "tilak_findings.json"
    if tilak_json.exists():
        t = json.loads(tilak_json.read_text())
        results.append({
            "label": "tilak-gita-rahasya", "n": t["n"],
            "me5_r4": t["me5"]["r4"], "sutrakrit_r4": t["sutrakrit"]["r4"],
            "delta_r4": t["delta_r4"], "median_skt": t["sutrakrit"]["median"],
            "verdict": t["verdict"],
        })

    print("\n=== UNIFIED SŪTRAKṚT FINDINGS ===\n")
    print(f"  {'Corpus':<35} {'n':>5} {'mE5 R@4':>10} {'Skt R@4':>10} {'Δ':>10} {'verdict':>10}")
    for r in results:
        if r.get("verdict") == "TOO_SMALL_N":
            print(f"  {r['label']:<35} {r['n']:>5}        --         --         -- {'sparse-citation':>20}")
        else:
            d = r.get("delta_r4", 0)
            print(f"  {r['label']:<35} {r['n']:>5} {r['me5_r4']*100:>9.1f}% {r['sutrakrit_r4']*100:>9.1f}% {d*100:+9.1f}pp {r['verdict']:>10}")

    OUT_JSON.write_text(json.dumps(results, ensure_ascii=False, indent=2))

    md = ["# Unified Sūtrakṛt findings across all loaded corpora",
          "",
          "Apply Sūtrakṛt-v2.6 weights (FROZEN from Ramsukhdas-fit) to each corpus.",
          "BG-internal cross-refs only. NO REFIT.",
          "",
          "## Findings table",
          "",
          "| Corpus | n | mE5 R@4 | Sūtrakṛt R@4 | Δ | Verdict |",
          "|---|---:|---:|---:|---:|---|"]
    for r in results:
        if r.get("verdict") == "TOO_SMALL_N":
            md.append(f"| {r['label']} | {r['n']} | — | — | — | sparse-citation (productization-style) |")
        else:
            d = r.get("delta_r4", 0)
            md.append(f"| {r['label']} | {r['n']} | {r['me5_r4']*100:.1f}% | {r['sutrakrit_r4']*100:.1f}% | {d*100:+.1f}pp | {r['verdict']} |")
    OUT_MD.write_text("\n".join(md))
    print(f"\nWrote {OUT_JSON.name} + {OUT_MD.name}")


if __name__ == "__main__":
    main()
