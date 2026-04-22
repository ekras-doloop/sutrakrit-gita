"""Build a theme-list → [verse_ids] index from the rendered per-verse JSONs.

Powers the theme-list walks at gita.ekrasworks.com: pick a theme-list
(a Pāṇinian-style anuvṛtti chain like ज्ञान or क्षमी) and walk every
verse where it threads through the corpus.

Output: rendered/theme_list_index.json
  {
    "list_name": [{"verse": "X.Y", "role": "..."}, ...],
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
OUTPUT = RENDERED / "theme_list_index.json"


def main() -> int:
    index: dict[str, list[dict]] = defaultdict(list)
    n = 0
    for f in sorted(RENDERED.glob("bg_*.json")):
        if f.name in {"lemma_index.json", "theme_list_index.json"}:
            continue
        try:
            d = json.loads(f.read_text())
        except Exception:
            continue
        vid = d.get("verse_id")
        if not vid:
            continue
        n += 1
        for tl in d.get("theme_list_memberships", []):
            name = tl.get("list", "").strip()
            if not name:
                continue
            index[name].append({
                "verse": vid,
                "role": tl.get("role", "supporting"),
            })

    OUTPUT.write_text(json.dumps(
        {k: index[k] for k in sorted(index)},
        ensure_ascii=False,
        indent=2,
    ))
    print(f"Indexed {len(index)} theme-lists across {n} verses → {OUTPUT}")
    multi = sum(1 for v in index.values() if len(v) >= 2)
    print(f"  {multi} lists thread across ≥2 verses")
    return 0


if __name__ == "__main__":
    sys.exit(main())
