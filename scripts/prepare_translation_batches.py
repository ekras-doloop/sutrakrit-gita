"""Prepare per-verse translation payloads for subagent dispatch.

For each verse in --chapter (or all 700), build a JSON payload containing
the mūla and each school's primary commentator's prose. The subagent
dispatcher consumes these and produces:
  - 6 doctrinal renderings (school-anchored English)
  - 5–7 verse-level so-what questions
  - 6 everyday-applications (per school, modern-life landing)

Output: data/translation_batches/verse_<X_Y>.payload.json
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from substrate import Substrate  # noqa: E402

BATCH_DIR = REPO_ROOT / "data" / "translation_batches"

SCHOOL_TO_PRIMARY = {
    "advaita": ("shankara", "Śaṅkarācārya — strict Advaita Vedānta, jñāna-mārga, niṣkāma-karma as preparation for jñāna; terse, dialectical voice"),
    "viśiṣṭādvaita": ("ramanuja", "Rāmānujācārya — Viśiṣṭādvaita, karma as kainkarya (service) to Bhagavān, niṣkāma-karma as bhakti-yoga preparation; expansive, devotional voice"),
    "dvaita": ("madhva", "Madhvācārya — Dvaita, jīva eternally distinct from Brahman, action as dependent worship of Hari; precise, polemical voice"),
    "śuddhādvaita": ("vallabha", "Vallabhācārya — Śuddhādvaita / Puṣṭi-mārga, all action as Kṛṣṇa's līlā-prasāda; rapturous, imperative voice"),
    "bhakti": ("sridhara", "Śrīdhara Svāmī — bhakti-philological, traditional but devotionally inflected; balanced voice"),
    "advaita-bhakti": ("madhusudan", "Madhusūdana Sarasvatī — synthesizes Advaita-jñāna with Kṛṣṇa-bhakti; synthesizing voice"),
}


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser()
    p.add_argument("--chapter", type=str, default=None,
                   help="Restrict to one chapter (e.g. '2'). Default: all.")
    p.add_argument("--force", action="store_true",
                   help="Overwrite payloads that already exist.")
    return p.parse_args()


def main() -> int:
    args = parse_args()
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    sub = Substrate()

    written = 0
    skipped = 0
    for verse_id in sub.all_verses():
        if args.chapter and not verse_id.startswith(f"{args.chapter}."):
            continue
        out = BATCH_DIR / f"verse_{verse_id.replace('.','_')}.payload.json"
        if out.exists() and not args.force:
            skipped += 1
            continue
        mula = sub.get_verse(verse_id)
        payload: dict = {
            "verse_id": verse_id,
            "mula_devanagari": mula,
            "schools": {},
        }
        any_panel = False
        for school, (commentator, voice) in SCHOOL_TO_PRIMARY.items():
            prose = sub.panel_commentary_for(commentator, verse_id) or ""
            if prose:
                any_panel = True
            payload["schools"][school] = {
                "voice": voice,
                "primary_commentator": commentator,
                "panel_commentary_devanagari": prose[:3500],
            }
        if not any_panel:
            skipped += 1
            continue
        out.write_text(json.dumps(payload, ensure_ascii=False, indent=2))
        written += 1

    print(f"Wrote {written} payloads to {BATCH_DIR} (skipped {skipped})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
