"""Merge per-verse translation panels into the rendered per-verse JSONs.

For each verse where data/translation_results/bgN/verse_X_Y.results.json
exists, fold:
  - doctrinal_renderings[school].english       → doctrinal_projections[school].english_rendering
  - doctrinal_renderings[school].divergence_note → doctrinal_projections[school].divergence_note
  - everyday_applications                       → (new top-level field)
  - so_what_questions                           → (new top-level field)

Idempotent. Skips translation files with malformed JSON.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
RENDERED = REPO_ROOT / "rendered"
TRANSLATIONS_BASE = REPO_ROOT / "data" / "translation_results"


def _renderings_dict(result: dict) -> dict[str, dict]:
    """Normalize doctrinal_renderings to {school: {english, ...}}.
    Subagents emitted both dict-of-dicts and list-of-dicts shapes."""
    drs = result.get("doctrinal_renderings")
    if drs is None:
        return {}
    out: dict[str, dict] = {}
    if isinstance(drs, dict):
        for school, v in drs.items():
            if isinstance(v, dict):
                out[school] = v
    elif isinstance(drs, list):
        for entry in drs:
            if not isinstance(entry, dict):
                continue
            school = entry.get("school") or entry.get("name") or ""
            if school:
                out[school] = entry
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--chapter", required=True, help="Chapter to merge (e.g. '2').")
    args = parser.parse_args()

    trans_dir = TRANSLATIONS_BASE / f"bg{args.chapter}"
    if not trans_dir.is_dir():
        print(f"No translations directory for chapter {args.chapter}", file=sys.stderr)
        return 1

    merged = 0
    skipped = 0
    no_target = 0
    bad_json = 0

    for tf in sorted(trans_dir.glob("verse_*.results.json")):
        try:
            t = json.loads(tf.read_text())
        except Exception:
            bad_json += 1
            continue
        vid = t.get("verse_id", "")
        if not vid:
            skipped += 1
            continue
        target = RENDERED / f"bg_{vid.replace('.', '_')}.json"
        if not target.exists():
            no_target += 1
            continue
        verse = json.loads(target.read_text())
        renderings = _renderings_dict(t)

        proj = verse.setdefault("doctrinal_projections", {})
        for school, r in renderings.items():
            entry = proj.setdefault(school, {})
            eng = r.get("english", "") if isinstance(r, dict) else ""
            div = r.get("divergence_note", "") if isinstance(r, dict) else ""
            if eng:
                entry["english_rendering"] = eng
            if div:
                entry["divergence_note"] = div
            entry.setdefault("score", 0.5)

        if t.get("so_what_questions"):
            verse["so_what_questions"] = t["so_what_questions"]
        if t.get("everyday_applications"):
            verse["everyday_applications"] = t["everyday_applications"]

        target.write_text(json.dumps(verse, ensure_ascii=False, indent=2))
        merged += 1

    print(f"Merged: {merged}, no-target: {no_target}, bad-json: {bad_json}, skipped: {skipped}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
