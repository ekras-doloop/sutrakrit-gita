#!/usr/bin/env python3
"""Re-extract per-school senses for every BG verse against the new
ByT5-multitask lemmas and merge them into rendered/bg_X_Y.json.

After the substrate-swap (Apr 22), word_by_word lemmas were replaced
by ByT5 output but senses_attested_in_panel was cleared (the prior
senses were anchored to broken vidyut lemmas). This script restores
that layer using the existing substrate.sense_extraction code, which
reads each school's commentary text and surfaces the gloss-snippet
each commentator gives for each lemma's Devanāgarī surface form.

Run:
    python scripts/merge_senses_into_rendered.py
"""
from __future__ import annotations
import json
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from substrate.sutrakrit import Substrate
from substrate.sense_extraction import extract_panel_senses
from scripts.render_verse import (
    PANEL_COMMENTATORS,
    _devanagari_surface_for_lemma,
)


def main() -> int:
    rendered_dir = ROOT / "rendered"
    files = sorted(rendered_dir.glob("bg_*.json"))
    print(f"Loading substrate (one-time, ~30s)...", flush=True)
    sub = Substrate()
    print(f"Loaded. Processing {len(files)} verses...", flush=True)

    n_done = 0
    n_senses = 0
    t0 = time.time()
    for i, path in enumerate(files):
        d = json.loads(path.read_text())
        verse_id = d["verse_id"]
        devanagari = d["mūla"]["devanāgarī"]
        # Build commentary lookups for this verse
        commentary_lookups = {
            c: sub.panel_commentary_for(c, verse_id) for c in PANEL_COMMENTATORS
        }
        # For each token, look up senses
        verse_sense_count = 0
        for tok in d.get("word_by_word", []):
            surface = tok.get("surface_form", "")
            dev_surface = _devanagari_surface_for_lemma(surface) if surface else ""
            if dev_surface:
                senses = extract_panel_senses(
                    dev_surface, commentary_lookups, verse_devanagari=devanagari
                )
                tok["senses_attested_in_panel"] = senses
                verse_sense_count += len(senses)
            else:
                tok["senses_attested_in_panel"] = []
        path.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n")
        n_done += 1
        n_senses += verse_sense_count
        if (i + 1) % 50 == 0:
            elapsed = time.time() - t0
            eta = (elapsed / (i + 1)) * (len(files) - i - 1)
            print(
                f"  {i+1}/{len(files)} ({elapsed:.0f}s, ETA {eta:.0f}s) — "
                f"{n_senses} total senses extracted so far",
                flush=True,
            )
    print(
        f"DONE: {n_done} verses, {n_senses} senses across panel, "
        f"{time.time()-t0:.0f}s total",
        flush=True,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
