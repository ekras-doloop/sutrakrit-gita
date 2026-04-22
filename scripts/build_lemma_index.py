"""Build a lemma → [verse_ids] index from the rendered per-verse JSONs.

The index powers the lemma-wire view at gita.ekrasworks.com:
clicking a word on any verse page shows every other verse where the
same lemma surfaces. "Same wire buzzing across the corpus."

Output: rendered/lemma_index.json
  {
    "lemma_iast": [{"verse": "X.Y", "surface": "...", "grammar": "..."}, ...],
    ...
  }
"""

from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RENDERED = REPO_ROOT / "rendered"
OUTPUT = RENDERED / "lemma_index.json"


def main() -> int:
    index: dict[str, list[dict]] = defaultdict(list)
    n = 0
    for f in sorted(RENDERED.glob("bg_*.json")):
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        vid = d.get("verse_id")
        if not vid:
            continue
        n += 1
        seen_in_verse: set[str] = set()
        for tok in d.get("word_by_word", []):
            lemma = tok.get("lemma", "").strip()
            if not lemma:
                continue
            key = lemma.lower()
            if key in seen_in_verse:
                continue
            seen_in_verse.add(key)
            index[key].append({
                "verse": vid,
                "surface": tok.get("surface_form", ""),
                "grammar": tok.get("grammar", ""),
            })

    OUTPUT.write_text(json.dumps(
        {k: index[k] for k in sorted(index)},
        ensure_ascii=False,
        indent=2,
    ))
    print(f"Indexed {len(index)} unique lemmas across {n} verses → {OUTPUT}")
    multi = sum(1 for v in index.values() if len(v) >= 2)
    print(f"  {multi} lemmas appear in ≥2 verses (the wire-of-ideas)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
