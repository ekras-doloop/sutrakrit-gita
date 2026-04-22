#!/usr/bin/env python3
"""Merge ByT5-multitask word_by_word output into rendered/bg_X_Y.json.

For each verse:
  - Replace word_by_word with the ByT5 token list.
  - Clear senses_attested_in_panel for each token (the old senses were
    anchored to garbage vidyut lemmas; sense re-extraction is a follow-up
    project, not part of this swap).
  - Leave doctrinal_projections, intertextual_panel, theme_list_memberships,
    so_what_questions, everyday_applications untouched — they are correct
    or independently produced.

Usage: python scripts/merge_byt5_into_rendered.py
"""
from __future__ import annotations
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARSE_FILE = ROOT / "data" / "parser_eval" / "runs" / "byt5_full_700.json"
RENDERED = ROOT / "rendered"


def main() -> int:
    if not PARSE_FILE.exists():
        print(f"ERROR: {PARSE_FILE} not found", file=sys.stderr)
        return 1
    parses = json.loads(PARSE_FILE.read_text())
    n_updated = 0
    n_missing = 0
    for vid, toks in parses.items():
        path = RENDERED / f"bg_{vid.replace('.', '_')}.json"
        if not path.exists():
            n_missing += 1
            continue
        d = json.loads(path.read_text())
        # Ensure each token has the substrate-schema fields the page renderer expects
        new_wbw = []
        for t in toks:
            new_wbw.append({
                "surface_form": t.get("surface_form", ""),
                "lemma": t.get("lemma", ""),
                "grammar": t.get("grammar", ""),
                "senses_attested_in_panel": [],   # follow-up: re-extract on new lemmas
                "theme_lists": [],                # follow-up: re-bind theme-lists to new lemmas
            })
        d["word_by_word"] = new_wbw
        # Mark the substrate version
        if "audit_trail" in d:
            d["audit_trail"]["word_by_word_parser"] = "ByT5-Sanskrit-multitask (Nehrdich/Hellwig/Keutzer EMNLP 2024)"
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        n_updated += 1
    print(f"Updated {n_updated} rendered/ files; {n_missing} missing")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
