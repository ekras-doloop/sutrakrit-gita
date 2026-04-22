#!/usr/bin/env python3
"""Build a meaning-first review sheet for the ByT5 substrate.

Each verse shows:
- Devanāgarī + IAST
- Śaṅkara's English rendering (so the labeler knows what the verse means)
- A flat list of "key words the parser found" with lemma + a 1-line MW gloss
- Labeler scans: do the glosses fit the verse meaning? Mark anything that doesn't.

This is the format Gaurav can actually evaluate.
"""
from __future__ import annotations
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RUNS = ROOT / "data" / "parser_eval" / "runs"
GOLD = ROOT / "data" / "parser_eval" / "gold_50" / "verses.json"
RENDERED = ROOT / "rendered"
GLOSS_CACHE = ROOT / "data" / "parser_eval" / "mw_gloss_cache.json"
OUT = ROOT / "data" / "parser_eval" / "REVIEW_SHEET_meanings.md"


def iast_to_slp1(s: str) -> str:
    """Cologne MW lookup expects SLP1-encoded keys."""
    table = [
        ("ā", "A"), ("ī", "I"), ("ū", "U"), ("ṛ", "f"), ("ṝ", "F"),
        ("ḷ", "x"), ("ai", "E"), ("au", "O"),
        ("ṃ", "M"), ("ḥ", "H"),
        ("kh", "K"), ("gh", "G"), ("ṅ", "N"),
        ("ch", "C"), ("jh", "J"), ("ñ", "Y"),
        ("ṭh", "Th"), ("ṭ", "w"), ("ḍh", "Dh"), ("ḍ", "q"), ("ṇ", "R"),
        ("th", "T"), ("dh", "D"),
        ("ph", "P"), ("bh", "B"),
        ("ś", "S"), ("ṣ", "z"),
    ]
    out = s
    # Apply digraphs first by sorting longest-first
    for a, b in sorted(table, key=lambda p: -len(p[0])):
        out = out.replace(a, b)
    # naive: th/Th/dh/Dh/etc. require special order — handled by length-sort above
    out = out.replace("w", "w").replace("q", "q")
    return out


def _direct_lookup(lemma_iast: str) -> str:
    """Single MW lookup, no recursion."""
    if not lemma_iast or len(lemma_iast) <= 1:
        return ""
    key_slp = iast_to_slp1(lemma_iast)
    url = (
        "https://www.sanskrit-lexicon.uni-koeln.de/scans/csl-apidev/getword.php?"
        + urllib.parse.urlencode({
            "key": key_slp, "filter": "glossless",
            "dict": "mw", "accent": "no",
        })
    )
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "curl"})
        raw = urllib.request.urlopen(req, timeout=10).read().decode("utf-8", "replace")
    except Exception:
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = unescape(re.sub(r"\s+", " ", text)).strip()
    # No body content → not in dictionary
    if "Printed book page" not in text:
        return ""
    # MW entry shape (after HTML strip):
    #   "<lemma> (H1) [Printed book page X,Y] <lemma> <pos> <gloss> [ ID=N ] ..."
    # Strategy: find each "[ID=...]"-delimited chunk, pick first one with real gloss.
    # Drop the leading "<lemma> (H1) [Printed book page X,Y]" header.
    chunks = re.split(r"\[\s*ID\s*=\s*\d+\s*\]", text)
    best = ""
    for chunk in chunks:
        # Strip "[Printed book page X,Y]"
        c = re.sub(r"\[\s*Printed book page[^\]]+\]", " ", chunk)
        # Strip "(H<n>)" headers
        c = re.sub(r"\(\s*H\s*\d+\s*\)", " ", c)
        # Drop initial lemma + part-of-speech tag (m./f./n./mfn./ind./cl. etc.)
        c = re.sub(r"^\s*\S+\s+(?:m|f|n|mfn|ind|cl|adv|num|ifc|iic)\.\s*", "", c)
        # Drop leading "<lemma> See col. 3 ." cross-reference stubs
        if re.match(r"^\s*\S+\s+See\s+col", c):
            continue
        # Drop pure parentheticals at the start
        c = re.sub(r"^\s*\([^)]*\)\s*", "", c).strip()
        # Take up to the first ; or , followed by source-abbreviation pattern
        m = re.search(r"^([^;]+?)(?:\s*,\s*(?:RV|MBh|Mn|R|L|Pāṇ|Pur|TS|ŚB|Hariv|Yājñ|Suśr|Kāv|MārkP|VP|BhP|VarBṛS|Ragh|Bhag|ChUp|TUp|MuṇḍUp|MaitrUp|Kaṭh|MahābhārayMBh|Vishn|Subh|Mn|Yājñ|Daś|Kum|Megh|Śak|Vikr|Mālav|Mudr|Vet)\.|\s*\[)", c)
        if m:
            best = m.group(1).strip(" ,.")
        else:
            # fallback: first ; or first 100 chars
            best = re.split(r"[;\[]", c)[0].strip(" ,.")[:100]
        if best and len(best) >= 5:
            break
    gloss = best
    gloss = re.sub(r"\b(RV|MBh|Mn|L|cf|i\.e|e\.g|esp|etc|&c)\.[\s,&c.]*", "", gloss).strip(" ,.")
    if len(gloss) > 100:
        gloss = gloss[:100].rsplit(" ", 1)[0] + "…"
    return gloss


def fetch_gloss(lemma_iast: str, cache: dict) -> str:
    """MW lookup with compound-split fallback.

    If the full lemma isn't in MW (common for samāsa not lexicalized as one entry),
    try splitting it at every position and look up both halves. Pick the split
    where both halves resolve and the second half is a known compound-final
    (adhipa, pati, īśa, etc.) or both halves are at least 3 chars and both
    return MW glosses.
    """
    if lemma_iast in cache:
        return cache[lemma_iast]
    if not lemma_iast or len(lemma_iast) <= 1:
        cache[lemma_iast] = ""
        return ""

    direct = _direct_lookup(lemma_iast)
    if direct:
        cache[lemma_iast] = direct
        return direct

    # Sandhi-aware compound split fallback: try every position 3+ from each end.
    # Common joints in samāsa: a+a → ā (so "janā" + "dhipa" came from jana + adhipa).
    # We try both raw splits and ā-split-becomes-a+a reconstructions.
    candidates = []
    L = lemma_iast
    n = len(L)
    for i in range(3, n - 2):
        left, right = L[:i], L[i:]
        # Try as-is
        candidates.append((left, right))
        # Try ā at boundary → a + a (jana + adhipa from janādhipa)
        if left.endswith("ā"):
            candidates.append((left[:-1] + "a", "a" + right))
        # Try ā at boundary → a + ī or ā + i (etc.) — a few more sandhi reversals
        if left.endswith("e"):
            candidates.append((left[:-1] + "a", "i" + right))
            candidates.append((left[:-1] + "a", "ī" + right))
        if left.endswith("o"):
            candidates.append((left[:-1] + "a", "u" + right))
            candidates.append((left[:-1] + "a", "ū" + right))

    best = None
    for left, right in candidates:
        if len(left) < 2 or len(right) < 2:
            continue
        lg = _lookup_with_cache(left, cache)
        rg = _lookup_with_cache(right, cache)
        if lg and rg:
            # Score: prefer roughly balanced splits with both glosses present
            score = abs(len(left) - len(right))
            if best is None or score < best[0]:
                best = (score, left, right, lg, rg)
                if score == 0:  # perfect balance, stop
                    break

    if best:
        _, left, right, lg, rg = best
        result = f"{left} ({lg.split(',')[0][:40]}) + {right} ({rg.split(',')[0][:40]})"
        cache[lemma_iast] = result
        return result

    cache[lemma_iast] = ""
    return ""


def _lookup_with_cache(lemma_iast: str, cache: dict) -> str:
    """Direct lookup but use cache to avoid duplicates during compound search."""
    if lemma_iast in cache:
        return cache[lemma_iast]
    g = _direct_lookup(lemma_iast)
    cache[lemma_iast] = g
    return g


def get_shankara_rendering(verse_id: str) -> str:
    p = RENDERED / f"bg_{verse_id.replace('.', '_')}.json"
    if not p.exists():
        return ""
    d = json.loads(p.read_text())
    proj = d.get("doctrinal_projections", {}).get("advaita", {})
    return proj.get("english_rendering", "")


def main() -> int:
    verses = json.loads(GOLD.read_text())
    verses_sorted = sorted(verses, key=lambda x: tuple(int(p) for p in x["verse_id"].split(".")))
    multitask = json.loads((RUNS / "byt5_multitask.json").read_text())

    # Use the curated gloss dict (hand-written, accurate). Cologne MW scraping
    # produced too many false negatives and homonym mis-pulls.
    curated_path = ROOT / "data" / "parser_eval" / "curated_glosses.json"
    cache = {}
    if curated_path.exists():
        curated = json.loads(curated_path.read_text())
        cache = {k: v for k, v in curated.items() if not k.startswith("_")}

    lines = []
    lines.append("# Substrate parser eval — meaning-first review sheet\n")
    lines.append("**Goal:** does the parser identify words that mean what the verse needs them to mean?\n")
    lines.append("**How to use:** For each verse, read Śaṅkara's English rendering at the top so you have the meaning. Then scan the **Words the parser found** list. Each row is: parser-lemma → 1-line MW gloss. Ask: *does this gloss make sense for this verse?* If a row is wrong (the lemma doesn't mean anything close to what this verse needs), mark it `→ ✗` with one word about what it should be. If everything fits, do nothing.\n")
    lines.append("**Skip when uncertain.** Easier to mark obvious failures than borderline calls. If 5 verses look totally clean, the substrate is in good shape.\n")
    lines.append(f"**{len(verses_sorted)} verses · {sum(len(multitask[v['verse_id']]) for v in verses_sorted)} words to scan total**\n")
    lines.append("---\n")

    for vd in verses_sorted:
        vid = vd["verse_id"]
        lines.append(f"\n## BG {vid}\n")
        lines.append(f"_{vd['iast']}_\n")
        rendering = get_shankara_rendering(vid)
        if rendering:
            lines.append(f"\n**Śaṅkara/advaita reading (so you know what the verse says):**\n> {rendering[:600]}{'…' if len(rendering) > 600 else ''}\n")
        lines.append("\n**Words the parser found:**\n")
        seen = set()
        for tok in multitask.get(vid, []):
            lem = tok.get("lemma", "")
            if not lem or lem in seen:
                continue
            seen.add(lem)
            gloss = cache.get(lem, "")
            surface = tok.get("surface_form", "")
            if gloss:
                lines.append(f"- **{lem}** _(seen as {surface})_ — {gloss}")
            else:
                lines.append(f"- **{lem}** _(seen as {surface})_ — _(no MW gloss; not in dictionary)_")
        lines.append("")

    lines.append("\n---\n## Scoring\n\nWhen done, count: how many lemmas you marked `✗` out of the total. Anything below ~5% means the substrate is publishable. Anything between 5–15% means we tune the rule layer. Above 15% means we need to revisit the parser or its inputs.\n")

    OUT.write_text("\n".join(lines))
    print(f"Wrote {OUT}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
