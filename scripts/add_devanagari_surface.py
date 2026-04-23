#!/usr/bin/env python3
"""Add a precise Devanāgarī surface to each word_by_word token.

ByT5-multitask emits IAST surface forms. The page renderer's hover-
tooltip system needs Devanāgarī to display each token in the mūla
script. A JS-side longest-match fallback was approximate; this script
runs vidyut.lipi (the same library the substrate uses) over each token
and stores the result as `surface_devanagari` on every token in
rendered/bg_X_Y.json. The page can then read it directly without
re-transliterating client-side.

Run:
    python scripts/add_devanagari_surface.py
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

try:
    from vidyut.lipi import Scheme, transliterate
except Exception as e:
    print(f"ERROR: vidyut.lipi unavailable: {e}", file=sys.stderr)
    raise SystemExit(1)


def to_devanagari(iast: str) -> str:
    if not iast:
        return ""
    try:
        return transliterate(iast, Scheme.Iast, Scheme.Devanagari)
    except Exception:
        return ""


def main() -> int:
    rendered = ROOT / "rendered"
    files = sorted(rendered.glob("bg_*.json"))
    print(f"Adding surface_devanagari to {len(files)} verses...", flush=True)
    t0 = time.time()
    n_tokens = 0
    for i, p in enumerate(files):
        d = json.loads(p.read_text())
        for tok in d.get("word_by_word", []):
            iast = tok.get("surface_form", "")
            tok["surface_devanagari"] = to_devanagari(iast)
            n_tokens += 1
        p.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        if (i + 1) % 100 == 0:
            print(f"  {i+1}/{len(files)} ({time.time()-t0:.1f}s)", flush=True)
    print(f"DONE: {len(files)} verses, {n_tokens} tokens, {time.time()-t0:.1f}s", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
