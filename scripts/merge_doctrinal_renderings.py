#!/usr/bin/env python3
"""Merge data/translation_results/*/verse_X_Y.results.json doctrinal_renderings
into rendered/bg_X_Y.json doctrinal_projections[<school>].english_rendering /
divergence_note.

Read-only on translation_results; rewrites rendered/.
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "data" / "translation_results"
DST = ROOT / "rendered"

# Map commentator-tradition labels in translation_results.school to the
# doctrinal_projections school keys actually used in rendered/.
def normalize_school(raw: str) -> str | None:
    """Tolerant matcher — subagents misspelled śuddhādvaita 14 different ways."""
    s = (raw or "").strip().lower().replace("_", "-")
    if not s:
        return None
    # advaita-bhakti synthesis must be checked BEFORE bare advaita
    if "advaita" in s and "bhakti" in s:
        return "advaita-bhakti"
    if s.startswith(("suddh", "shuddh", "śuddh", "shudh", "śuddhā")):
        return "śuddhādvaita"
    if s.startswith(("vishish", "visist", "viśiṣ", "viśiṣṭā")):
        return "viśiṣṭādvaita"
    if s.startswith("dvaita"):
        return "dvaita"
    if s.startswith("advaita"):
        return "advaita"
    if s.startswith("bhakti"):
        return "bhakti"
    return None


def merge_one(results_path: Path) -> tuple[str, int]:
    data = json.loads(results_path.read_text())
    verse_id = data.get("verse_id")
    if not verse_id:
        return ("", 0)
    rendered_path = DST / f"bg_{verse_id.replace('.', '_')}.json"
    if not rendered_path.exists():
        return (verse_id, 0)
    rendered = json.loads(rendered_path.read_text())
    projections = rendered.setdefault("doctrinal_projections", {})
    n = 0
    dr = data.get("doctrinal_renderings")
    entries = []
    if isinstance(dr, list):
        for e in dr:
            if not isinstance(e, dict):
                continue
            entries.append({
                "school": e.get("school"),
                "rendering": e.get("rendering") or e.get("english"),
                "divergence_note": e.get("divergence_note") or e.get("bhashya_anchor"),
                "commentator": e.get("commentator"),
            })
    elif isinstance(dr, dict):
        for school_key, val in dr.items():
            if isinstance(val, str):
                entries.append({
                    "school": school_key,
                    "rendering": val,
                    "divergence_note": None,
                    "commentator": None,
                })
            elif isinstance(val, dict):
                entries.append({
                    "school": school_key,
                    "rendering": val.get("english") or val.get("rendering"),
                    "divergence_note": val.get("divergence_note") or val.get("bhashya_anchor"),
                    "commentator": val.get("commentator"),
                })
    for entry in entries:
        school = normalize_school(entry.get("school") or "")
        if not school or school not in projections:
            continue
        proj = projections[school]
        rendering = (entry.get("rendering") or "").strip()
        anchor = (entry.get("divergence_note") or "").strip()
        if rendering:
            proj["english_rendering"] = rendering
            n += 1
        if anchor:
            proj["divergence_note"] = anchor
        commentator = (entry.get("commentator") or "").strip()
        if commentator:
            proj["commentator"] = commentator
    rendered_path.write_text(
        json.dumps(rendered, ensure_ascii=False, indent=2) + "\n"
    )
    return (verse_id, n)


def main() -> int:
    if not SRC.exists():
        print(f"ERROR: {SRC} not found", file=sys.stderr)
        return 1
    paths = sorted(SRC.glob("bg*/verse_*.results.json"))
    if not paths:
        print("No translation_results found", file=sys.stderr)
        return 1
    total_verses = 0
    total_renderings = 0
    missing_rendered = []
    for p in paths:
        verse_id, n = merge_one(p)
        if not verse_id:
            continue
        if n == 0:
            missing_rendered.append(verse_id)
            continue
        total_verses += 1
        total_renderings += n
    print(f"merged {total_renderings} renderings across {total_verses} verses")
    if missing_rendered:
        print(f"skipped {len(missing_rendered)} (no rendered/ file or empty): "
              f"{missing_rendered[:5]}...")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
