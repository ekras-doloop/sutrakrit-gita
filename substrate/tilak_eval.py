"""Frozen Sūtrakṛt-v2.6 eval on Tilak Gītā-Rahasya.

Tilak's text is English prose interleaving transliterated Sanskrit quotes
(IAST-ish Roman, OCR'd from djvu). Citation pattern: `(Gi. X.Y)` and
`(GT. X.Y)`. Quoted Sanskrit phrase precedes each citation, delimited by
double-quotes. We:
  1. Extract (quoted_iast, target_bg_verse) pairs
  2. IAST → Devanāgarī conversion of the quote
  3. Apply frozen substrate features (sub + h + th) — the b/e_v shared-
     sutra signals zero out (Tilak isn't verse-anchored)
  4. Report mE5 R@4, Sūtrakṛt R@4, Δ
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
TILAK_TXT = BASE / "data" / "tilak_gita_rahasya.djvu.txt"
LISTS_JSON = BASE / "verification" / "v2_0_lists_graph.json"
VIDYUT_DATA = "/tmp/vidyut-data"
OUT_JSON = BASE / "verification" / "tilak_findings.json"
OUT_MD = BASE / "verification" / "tilak_findings.md"

# Tilak citation patterns: (Gi. X.Y), (GT. X.Y), (Gita X.Y)
CITE_RE = re.compile(r"\(\s*(?:Gi|GT|G[īi]t[āa])\.?\s*(\d{1,2})\s*\.\s*(\d{1,3})\s*\)")
# Quoted phrase preceding the citation (IAST transliteration in double-quotes)
QUOTE_RE = re.compile(r'"([^"]{5,300}?)"')


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


def iast_to_dev(s):
    """Best-effort IAST → Devanāgarī. OCR is imperfect; map common drift."""
    # OCR drift fixes: 'fi' often = 'ñ', 'fia' = 'ña', 'ari' often clean
    s = s.replace("fi", "ñ")
    # Already-IAST diacritics survive; non-diacritic Roman gets cleaned
    try:
        return transliterate(s, Scheme.Iast, Scheme.Devanagari)
    except Exception:
        return ""


def lemmatize_dev(text):
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


def extract_triples(bg):
    """Find each (Gi./GT. X.Y) citation, walk back to nearest preceding
    double-quoted phrase (within 250 chars), convert quote IAST→Dev."""
    txt = TILAK_TXT.read_text(errors="ignore")
    triples = []
    skipped_no_quote = 0
    skipped_bad_target = 0
    skipped_bad_iast = 0
    for m in CITE_RE.finditer(txt):
        ch, vs = int(m.group(1)), int(m.group(2))
        target = f"{ch}.{vs}"
        if target not in bg:
            skipped_bad_target += 1
            continue
        # Look backward for nearest "..." quote
        lookback = txt[max(0, m.start()-300):m.start()]
        quotes = list(QUOTE_RE.finditer(lookback))
        if not quotes:
            skipped_no_quote += 1
            continue
        iast_quote = quotes[-1].group(1).strip()
        # Strip OCR junk: linebreak markers, [1] footnote markers
        iast_quote = re.sub(r"\[\d+\]", "", iast_quote)
        iast_quote = re.sub(r"\s+", " ", iast_quote).strip()
        if len(iast_quote) < 10:
            skipped_bad_iast += 1
            continue
        dev = iast_to_dev(iast_quote)
        # Devanāgarī sanity: must have ≥4 Dev letters
        if len(re.findall(r"[\u0900-\u097F]", dev)) < 4:
            skipped_bad_iast += 1
            continue
        triples.append({"target": target, "sutra_iast": iast_quote, "sutra": normalize(dev)})
    print(f"  Triples extracted: {len(triples)}")
    print(f"  Skipped (no preceding quote): {skipped_no_quote}")
    print(f"  Skipped (bad/unknown BG target): {skipped_bad_target}")
    print(f"  Skipped (IAST→Dev conversion failed): {skipped_bad_iast}")
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
    verse_lemmas = {v: lemmatize_dev(bg[v]) for v in milestones}
    verse_stems = {v: {stem_prefix(l) for l in lems if l} for v, lems in verse_lemmas.items()}
    n_v = len(milestones)
    lemma_df = Counter()
    for lems in verse_lemmas.values():
        for l in lems: lemma_df[l] += 1
    lemma_idf = {l: np.log(n_v / max(df, 1)) for l, df in lemma_df.items()}

    a, b, e_v, z, h, th = 1.0, 0.01, 0.005, 0.2, 0.0, 0.01

    print("\n=== Extracting Tilak triples ===")
    triples = extract_triples(bg)
    if len(triples) < 10:
        print("Insufficient triples — abort.")
        return

    unique_sutras = sorted({t["sutra"] for t in triples})
    print(f"  Unique sutras: {len(unique_sutras)}")
    S = model.encode([f"query: {s}" for s in unique_sutras],
                     normalize_embeddings=True, batch_size=32, convert_to_numpy=True)
    s_idx = {s: i for i, s in enumerate(unique_sutras)}
    sutra_lemmas = {s: lemmatize_dev(s) for s in unique_sutras}
    sutra_stems = {s: {stem_prefix(l) for l in lems if l} for s, lems in sutra_lemmas.items()}

    per_sutra = {}
    for sutra in unique_sutras:
        sub = np.array([substring_score(sutra, bg[v]) for v in milestones])
        s_lems = sutra_lemmas[sutra]; s_stems = sutra_stems[sutra]
        lem = np.array([sum(lemma_idf.get(l, 0) for l in (s_lems & verse_lemmas[v])) for v in milestones])
        stem = np.array([float(len(s_stems & verse_stems[v])) for v in milestones])
        per_sutra[sutra] = (sub, lem, stem)

    def run(use_vyak):
        ranks = []
        for t in triples:
            sims = a * (M @ S[s_idx[t["sutra"]]])
            if use_vyak:
                sub, lem, stem = per_sutra[t["sutra"]]
                # Tilak source isn't BG-anchored → b/e_v contribute 0
                sims = sims + z*sub + h*lem + th*stem
            order = np.argsort(-sims)
            ranks.append(int(np.where(order == ms_idx[t["target"]])[0][0]))
        r = np.array(ranks)
        return {"r1": float((r<1).mean()), "r4": float((r<4).mean()),
                "r10": float((r<10).mean()), "r25": float((r<25).mean()),
                "median": int(np.median(r))}

    me5 = run(False); skt = run(True)
    delta = skt["r4"] - me5["r4"]

    print("\n=== TILAK GĪTĀ-RAHASYA SŪTRAKṚT FINDINGS ===")
    print(f"  n triples:                {len(triples)}")
    print(f"  unique sutras:            {len(unique_sutras)}")
    print(f"  mE5 R@4:                  {me5['r4']*100:.1f}%")
    print(f"  Sūtrakṛt R@4:             {skt['r4']*100:.1f}%")
    print(f"  Δ:                        {delta*100:+.1f}pp")
    print(f"  mE5 median rank:          {me5['median']}")
    print(f"  Sūtrakṛt median rank:     {skt['median']}")
    print(f"  Verdict:                  {'PASSED' if skt['r4'] >= 0.40 else 'FAILED'} (gate ≥ 40%)")

    out = {"corpus": "tilak-gita-rahasya", "n": len(triples),
           "unique_sutras": len(unique_sutras),
           "me5": me5, "sutrakrit": skt,
           "delta_r4": delta,
           "verdict": "PASSED" if skt["r4"] >= 0.40 else "FAILED"}
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    md = [
        "# Tilak Gītā-Rahasya — frozen Sūtrakṛt-v2.6 eval",
        "",
        f"- n triples extracted: **{len(triples)}**",
        f"- unique sutras: {len(unique_sutras)}",
        f"- mE5 R@4: **{me5['r4']*100:.1f}%**",
        f"- Sūtrakṛt R@4: **{skt['r4']*100:.1f}%**",
        f"- Δ: **{delta*100:+.1f}pp**",
        f"- median rank (mE5 / Sūtrakṛt): {me5['median']} / {skt['median']}",
        f"- verdict: **{'PASSED' if skt['r4'] >= 0.40 else 'FAILED'}** (gate ≥ 40%)",
        "",
        "Source: archive.org `tilak-gita-rahasya-english_202010` djvu.txt.",
        "Citation pattern matched: `(Gi. X.Y)` + `(GT. X.Y)` + `(Gita X.Y)`.",
        "Quoted Sanskrit transliterated IAST→Devanāgarī before substrate matching.",
    ]
    OUT_MD.write_text("\n".join(md))
    print(f"\nWrote {OUT_JSON.name} + {OUT_MD.name}")


if __name__ == "__main__":
    main()
