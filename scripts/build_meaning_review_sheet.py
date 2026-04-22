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


def fetch_gloss(lemma_iast: str, cache: dict) -> str:
    if lemma_iast in cache:
        return cache[lemma_iast]
    if not lemma_iast or len(lemma_iast) <= 1:
        cache[lemma_iast] = ""
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
        cache[lemma_iast] = ""
        return ""
    text = re.sub(r"<[^>]+>", " ", raw)
    text = unescape(re.sub(r"\s+", " ", text)).strip()
    # Find first occurrence of ") " then take until first ";" or "[ID="
    # Pattern: "... part-of-speech-info ) <GLOSS> [ID= or ;"
    # Simpler: take everything between the first ")" after the lemma and the first ";" or "["
    m = re.search(r"\)\s+([^;\[]+?)(?:[;\[]|,$)", text)
    gloss = m.group(1).strip() if m else ""
    # Tidy: remove "RV. &c. &c." and similar abbrev tails
    gloss = re.sub(r"\b(RV|MBh|Mn|L|cf|i\.e|e\.g|esp|etc|&c)\.[\s,&c.]*", "", gloss).strip(" ,.")
    if len(gloss) > 100:
        gloss = gloss[:100].rsplit(" ", 1)[0] + "…"
    cache[lemma_iast] = gloss
    return gloss


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

    cache = {}
    if GLOSS_CACHE.exists():
        cache = json.loads(GLOSS_CACHE.read_text())

    # Collect unique lemmas
    unique_lemmas = sorted({
        t["lemma"] for vid, toks in multitask.items() for t in toks if t.get("lemma")
    })
    print(f"Looking up {len(unique_lemmas)} unique lemmas in MW...", file=sys.stderr)
    t0 = time.time()
    for i, lem in enumerate(unique_lemmas):
        if lem in cache:
            continue
        fetch_gloss(lem, cache)
        if (i + 1) % 25 == 0:
            print(f"  {i+1}/{len(unique_lemmas)} ({time.time()-t0:.1f}s)", file=sys.stderr)
            GLOSS_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2))
    GLOSS_CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2))
    print(f"  done in {time.time()-t0:.1f}s", file=sys.stderr)

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
