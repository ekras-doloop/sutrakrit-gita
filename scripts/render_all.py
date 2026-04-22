"""Render all 700 Bhagavad Gītā verses through the Sūtrakṛt substrate.

Usage:
    python scripts/render_all.py --output-dir rendered/

Notes:
  - Loads the Substrate once and reuses it across all verses (the
    embedding model and lemmatizer take ~30 seconds to initialize;
    sharing them across 700 verses saves roughly six hours of redundant
    initialization).
  - Skips already-rendered verses (resume-on-restart). Pass --force to
    re-render everything.
  - On a laptop with 8 GB RAM and no GPU, expect approximately 30–60
    minutes for the full 700-verse run; on a machine with a GPU, well
    under 10 minutes.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from substrate import FROZEN_WEIGHTS, Substrate  # noqa: E402
from substrate.pragmatics import detect_vocatives, primary_vocative  # noqa: E402
from substrate.prosody import detect_meter, detect_meter_shift  # noqa: E402

from scripts.render_verse import (  # noqa: E402
    CHAPTER_NAMES,
    DIALOGUE_MAP,
    SCHOOLS,
    _to_iast,
    _adjacent_verse_id,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render all 700 Bhagavad Gītā verses through the Sūtrakṛt substrate."
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=REPO_ROOT / "rendered",
        help="Directory to write per-verse JSON outputs (default: rendered/)",
    )
    parser.add_argument(
        "--top-k",
        type=int,
        default=8,
        help="Intertextual candidates per verse (default: 8)",
    )
    parser.add_argument(
        "--substrate-version",
        default="v2.6-frozen",
        help="Substrate version identifier (default: v2.6-frozen)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-render verses that already have output files",
    )
    parser.add_argument(
        "--verses",
        nargs="+",
        help="Optional explicit list of verse IDs to render (default: all)",
    )
    return parser.parse_args()


def render_one(sub: Substrate, verse_id: str, top_k: int, version: str) -> dict:
    """Render a single verse using a pre-loaded Substrate."""
    devanagari = sub.get_verse(verse_id)
    if not devanagari:
        return {}

    chapter, verse_num = verse_id.split(".")
    speaker, addressed = DIALOGUE_MAP.get(chapter, ("Krishna", "Arjuna"))
    chapter_name = CHAPTER_NAMES.get(chapter, f"Chapter {chapter}")

    candidates = sub.score_query(verse_id, devanagari, top_k=top_k)

    doctrinal_projections = {}
    for school, commentators in SCHOOLS.items():
        witnesses = []
        for c in commentators:
            if sub.panel_commentary_for(c, verse_id):
                witnesses.append(f"{c}_{verse_id}")
        if witnesses:
            doctrinal_projections[school] = {
                "reading_summary": "(reading summary extraction forthcoming in next-pass build)",
                "key_cross_references": [],
                "witness_passages": witnesses,
                "score": 0.5,
            }

    theme_lists = sub.theme_lists_for(verse_id)
    tokens = sub.tokenize_with_grammar(devanagari)

    # Prosody
    meter, _ = detect_meter(devanagari)
    prev_id = _adjacent_verse_id(verse_id, -1)
    next_id = _adjacent_verse_id(verse_id, +1)
    prev_text = sub.get_verse(prev_id) if prev_id else ""
    next_text = sub.get_verse(next_id) if next_id else ""
    prev_meter = detect_meter(prev_text)[0] if prev_text else meter
    next_meter = detect_meter(next_text)[0] if next_text else meter

    # Vocative
    vocs = detect_vocatives(devanagari, speaker)
    primary_voc = primary_vocative(vocs)
    if primary_voc and len(vocs) > 1:
        vocative_str = f"{primary_voc} (also: {', '.join(vocs[1:])})"
    elif primary_voc:
        vocative_str = primary_voc
    else:
        vocative_str = ""

    return {
        "verse_id": verse_id,
        "mūla": {
            "devanāgarī": devanagari,
            "iast": _to_iast(devanagari),
            "chapter_position": f"Chapter {chapter} ({chapter_name}), verse {verse_num}",
            "speaker": speaker,
            "addressed_to": addressed,
        },
        "word_by_word": [
            {
                "surface_form": tok["surface_form"],
                "lemma": tok["lemma"],
                "grammar": tok["grammar"],
                "senses_attested_in_panel": [],
                "theme_lists": [],
            }
            for tok in tokens
            if tok["lemma"]
        ],
        "intertextual_panel": [
            {
                "verse": c.verse,
                "type": c.relationship_type,
                "score": round(c.score, 4),
                "feature_breakdown": c.feature_breakdown,
            }
            for c in candidates
        ],
        "doctrinal_projections": doctrinal_projections,
        "prosodic_information": {
            "meter": meter,
            "meter_shift_from_previous": detect_meter_shift(prev_meter, meter) if prev_text else False,
            "meter_shift_to_next": detect_meter_shift(meter, next_meter) if next_text else False,
            "pragmatic_context": {
                "vocative": vocative_str,
                "preceding_question": "",
                "following_response": "",
            },
        },
        "theme_list_memberships": [
            {"list": tl, "role": "supporting", "other_verses_in_list": []}
            for tl in sorted(theme_lists)
        ],
        "audit_trail": {
            "substrate_version": version,
            "fitted_weights": FROZEN_WEIGHTS,
            "corpus_provenance": {
                "mūla": "Belvalkar critical edition (BORI 1947), via Ambuda multi-witness",
                "panel_witnesses": [
                    "bg-mula", "bg-shankara", "bg-ramanuja", "bg-madhva",
                    "bg-vedantadeshika", "bg-vallabha", "bg-jayatirtha",
                    "bg-anandgiri", "bg-sridhara", "bg-madhusudan",
                ],
            },
            "extraction_date": date.today().isoformat(),
            "score_methodology_documented_at": "Paper 1, Section II.B",
        },
    }


def verse_path(out_dir: Path, verse_id: str) -> Path:
    return out_dir / f"bg_{verse_id.replace('.', '_')}.json"


def main() -> int:
    args = parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)

    print("Loading substrate (this takes ~30 seconds)...", file=sys.stderr)
    sub = Substrate()
    sub._load_bg()  # noqa: SLF001
    sub._load_lists_graph()  # noqa: SLF001
    sub._load_embeddings()  # noqa: SLF001
    sub._load_lemma_index()  # noqa: SLF001

    verses_to_render = args.verses if args.verses else sub.all_verses()
    n = len(verses_to_render)
    print(f"Rendering {n} verses to {args.output_dir}/", file=sys.stderr)

    rendered_count = 0
    skipped_count = 0
    start = time.time()
    for i, vid in enumerate(verses_to_render, 1):
        out_path = verse_path(args.output_dir, vid)
        if out_path.exists() and not args.force:
            skipped_count += 1
            continue
        obj = render_one(sub, vid, args.top_k, args.substrate_version)
        if not obj:
            print(f"  WARN verse {vid} not found in BG mūla, skipping", file=sys.stderr)
            continue
        out_path.write_text(json.dumps(obj, ensure_ascii=False, indent=2))
        rendered_count += 1
        if rendered_count % 20 == 0:
            elapsed = time.time() - start
            rate = rendered_count / elapsed
            eta = (n - i) / rate if rate > 0 else 0
            print(
                f"  [{i}/{n}] rendered {rendered_count}, skipped {skipped_count}, "
                f"rate {rate:.1f}/s, ETA {eta/60:.1f} min",
                file=sys.stderr,
            )

    elapsed = time.time() - start
    print(
        f"Done. Rendered {rendered_count} new, skipped {skipped_count} existing, "
        f"in {elapsed/60:.1f} minutes.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
