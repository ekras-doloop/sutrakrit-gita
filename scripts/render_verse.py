"""Render a single Bhagavad Gītā verse through the Sūtrakṛt substrate
into a per-verse object conforming to schema/per-verse-object.schema.json.

Usage:
    python scripts/render_verse.py --verse 2.55 --output rendered/bg_2_55.json

This is the substantive renderer. It produces a per-verse object using:
  - the substrate's intertextual scoring (substrate/sutrakrit.py)
  - the panel data's school-attested cross-references
  - vidyut-lipi for IAST transliteration
  - substrate.prosody for meter detection
  - the lists graph for theme-list memberships

Refinements still on the build queue (each marked '(forthcoming)' in
output where applicable):
  - Per-lemma surface-form/grammar via vidyut.prakriya
  - Per-lemma school-conditioned sense extraction from panel commentary
  - Reading-summary extraction per school's commentary
  - Pragmatic-context vocative detection
  - Prev/next verse meter-shift signals
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from substrate import FROZEN_WEIGHTS, Substrate  # noqa: E402
from substrate.pragmatics import detect_vocatives, primary_vocative  # noqa: E402
from substrate.prosody import detect_meter, detect_meter_shift  # noqa: E402
from substrate.reading_summaries import summarize_school_reading  # noqa: E402
from substrate.sense_extraction import extract_panel_senses  # noqa: E402

# Set to True to call LLM for reading_summary generation. Default False
# to keep render_verse.py runnable without API keys; render_all.py
# enables when LLM credentials are available in the environment.
ENABLE_READING_SUMMARIES = os.environ.get("ENABLE_READING_SUMMARIES", "false").lower() == "true"

PANEL_COMMENTATORS = ["shankara", "anandgiri", "ramanuja", "vedantadeshika",
                      "madhva", "jayatirtha", "vallabha", "sridhara", "madhusudan"]


def _devanagari_surface_for_lemma(token_surface: str) -> str:
    """The token surface_form in the renderer is in IAST after our
    transliteration. To match against Devanāgarī commentary text, we
    need to convert back to Devanāgarī.
    """
    try:
        from vidyut.lipi import Scheme, transliterate

        return transliterate(token_surface, Scheme.Iast, Scheme.Devanagari)
    except Exception:
        return ""

DIALOGUE_MAP = {
    "1": ("Arjuna", "Krishna"),
    "2": ("Krishna", "Arjuna"),
    "3": ("Krishna", "Arjuna"),
    "4": ("Krishna", "Arjuna"),
    "5": ("Krishna", "Arjuna"),
    "6": ("Krishna", "Arjuna"),
    "7": ("Krishna", "Arjuna"),
    "8": ("Krishna", "Arjuna"),
    "9": ("Krishna", "Arjuna"),
    "10": ("Krishna", "Arjuna"),
    "11": ("Krishna", "Arjuna"),
    "12": ("Krishna", "Arjuna"),
    "13": ("Krishna", "Arjuna"),
    "14": ("Krishna", "Arjuna"),
    "15": ("Krishna", "Arjuna"),
    "16": ("Krishna", "Arjuna"),
    "17": ("Krishna", "Arjuna"),
    "18": ("Krishna", "Arjuna"),
}

CHAPTER_NAMES = {
    "1": "Arjuna-Viṣāda-Yoga (The Yoga of Arjuna's Despondency)",
    "2": "Sāṅkhya-Yoga (The Yoga of Knowledge)",
    "3": "Karma-Yoga (The Yoga of Action)",
    "4": "Jñāna-Karma-Sannyāsa-Yoga (The Yoga of Renunciation of Action in Knowledge)",
    "5": "Karma-Sannyāsa-Yoga (The Yoga of Renunciation)",
    "6": "Dhyāna-Yoga (The Yoga of Meditation)",
    "7": "Jñāna-Vijñāna-Yoga (The Yoga of Knowledge and Realization)",
    "8": "Akṣara-Brahma-Yoga (The Yoga of the Imperishable Brahman)",
    "9": "Rāja-Vidyā-Rāja-Guhya-Yoga (The Yoga of Royal Knowledge and Royal Mystery)",
    "10": "Vibhūti-Yoga (The Yoga of Divine Manifestations)",
    "11": "Viśvarūpa-Darśana-Yoga (The Yoga of the Vision of the Universal Form)",
    "12": "Bhakti-Yoga (The Yoga of Devotion)",
    "13": "Kṣetra-Kṣetrajña-Vibhāga-Yoga (The Yoga of Distinction Between Field and Field-Knower)",
    "14": "Guṇatraya-Vibhāga-Yoga (The Yoga of Distinction of the Three Qualities)",
    "15": "Puruṣottama-Yoga (The Yoga of the Supreme Person)",
    "16": "Daivāsura-Sampad-Vibhāga-Yoga (The Yoga of Distinction Between Divine and Demonic Endowments)",
    "17": "Śraddhātraya-Vibhāga-Yoga (The Yoga of Distinction of Threefold Faith)",
    "18": "Mokṣa-Sannyāsa-Yoga (The Yoga of Liberation by Renunciation)",
}

SCHOOLS = {
    "advaita": ["shankara", "anandgiri"],
    "viśiṣṭādvaita": ["ramanuja", "vedantadeshika"],
    "dvaita": ["madhva", "jayatirtha"],
    "śuddhādvaita": ["vallabha"],
    "bhakti": ["sridhara"],
    "advaita-bhakti": ["madhusudan"],
}


def _to_iast(devanagari: str) -> str:
    """Transliterate Devanāgarī to IAST via vidyut-lipi."""
    try:
        from vidyut.lipi import Scheme, transliterate

        return transliterate(devanagari, Scheme.Devanagari, Scheme.Iast)
    except Exception:
        return ""


def _adjacent_verse_id(verse_id: str, offset: int) -> str | None:
    """Return the verse_id offset positions away in the BG sequence (within chapter)."""
    chapter, verse_num = verse_id.split(".")
    new_verse = int(verse_num) + offset
    if new_verse < 1:
        return None
    return f"{chapter}.{new_verse}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render a single Bhagavad Gītā verse through the Sūtrakṛt substrate."
    )
    parser.add_argument(
        "--verse",
        required=True,
        help="Verse identifier in chapter.verse form (e.g., '2.55')",
    )
    parser.add_argument(
        "--output",
        required=True,
        type=Path,
        help="Output path for the rendered JSON object",
    )
    parser.add_argument("--top-k", type=int, default=8)
    parser.add_argument("--substrate-version", default="v2.6-frozen")
    return parser.parse_args()


def render_verse(verse_id: str, top_k: int, substrate_version: str) -> dict:
    """Render a verse to a per-verse object."""
    sub = Substrate()
    devanagari = sub.get_verse(verse_id)
    if not devanagari:
        raise ValueError(f"Verse {verse_id} not found in BG mūla corpus")

    chapter, verse_num = verse_id.split(".")
    speaker, addressed = DIALOGUE_MAP.get(chapter, ("Krishna", "Arjuna"))
    chapter_name = CHAPTER_NAMES.get(chapter, f"Chapter {chapter}")

    # --- mūla section -------------------------------------------------
    iast = _to_iast(devanagari)
    mula = {
        "devanāgarī": devanagari,
        "iast": iast,
        "chapter_position": f"Chapter {chapter} ({chapter_name}), verse {verse_num}",
        "speaker": speaker,
        "addressed_to": addressed,
    }

    # --- intertextual_panel section ----------------------------------
    candidates = sub.score_query(verse_id, devanagari, top_k=top_k)
    intertextual_panel = [
        {
            "verse": c.verse,
            "type": c.relationship_type,
            "score": round(c.score, 4),
            "feature_breakdown": c.feature_breakdown,
        }
        for c in candidates
    ]

    # --- doctrinal_projections section -------------------------------
    doctrinal_projections = {}
    for school, commentators in SCHOOLS.items():
        witness_passages = []
        primary_prose = None
        primary_commentator = None
        for c in commentators:
            prose = sub.panel_commentary_for(c, verse_id)
            if prose:
                witness_passages.append(f"{c}_{verse_id}")
                if primary_prose is None:
                    primary_prose = prose
                    primary_commentator = c
        if witness_passages:
            reading_summary = ""
            if ENABLE_READING_SUMMARIES and primary_prose and len(primary_prose) >= 50:
                try:
                    reading_summary = summarize_school_reading(
                        verse_id, school, devanagari, primary_prose
                    )
                except Exception as e:
                    reading_summary = f"(LLM summary failed: {e})"
            doctrinal_projections[school] = {
                "reading_summary": reading_summary
                or "(reading summary extraction pending; ENABLE_READING_SUMMARIES=true to generate)",
                "key_cross_references": [],
                "witness_passages": witness_passages,
                "score": 0.5,
            }

    # --- prosodic_information section --------------------------------
    meter, meter_diag = detect_meter(devanagari)

    prev_id = _adjacent_verse_id(verse_id, -1)
    next_id = _adjacent_verse_id(verse_id, +1)
    prev_text = sub.get_verse(prev_id) if prev_id else ""
    next_text = sub.get_verse(next_id) if next_id else ""
    prev_meter = detect_meter(prev_text)[0] if prev_text else meter
    next_meter = detect_meter(next_text)[0] if next_text else meter

    vocatives_detected = detect_vocatives(devanagari, speaker)
    primary_voc = primary_vocative(vocatives_detected)
    if primary_voc and len(vocatives_detected) > 1:
        vocative_str = f"{primary_voc} (also: {', '.join(vocatives_detected[1:])})"
    elif primary_voc:
        vocative_str = primary_voc
    else:
        vocative_str = ""

    prosodic_information = {
        "meter": meter,
        "meter_shift_from_previous": detect_meter_shift(prev_meter, meter) if prev_text else False,
        "meter_shift_to_next": detect_meter_shift(meter, next_meter) if next_text else False,
        "pragmatic_context": {
            "vocative": vocative_str,
            "preceding_question": "",
            "following_response": "",
        },
    }

    # --- theme_list_memberships section -------------------------------
    theme_lists = sub.theme_lists_for(verse_id)
    theme_list_memberships = [
        {
            "list": tl,
            "role": "supporting",
            "other_verses_in_list": sub.other_verses_in_list(tl, exclude_verse=verse_id),
        }
        for tl in sorted(theme_lists)
    ]

    # --- word_by_word section ----------------------------------------
    tokens = sub.tokenize_with_grammar(devanagari)
    # Build commentary lookup once for all lemmas in this verse
    commentary_lookups = {
        c: sub.panel_commentary_for(c, verse_id) for c in PANEL_COMMENTATORS
    }
    word_by_word = []
    for tok in tokens:
        if not tok["lemma"]:
            continue
        # Convert surface form back to Devanāgarī for commentary search
        dev_surface = _devanagari_surface_for_lemma(tok["surface_form"])
        senses = extract_panel_senses(dev_surface, commentary_lookups, verse_devanagari=devanagari) if dev_surface else []
        # Per-lemma theme-list membership: which of this verse's
        # theme-lists have a key-phrase that contains this lemma?
        per_lemma_lists = sub.lists_containing_lemma(dev_surface, verse_id) if dev_surface else []
        word_by_word.append(
            {
                "surface_form": tok["surface_form"],
                "lemma": tok["lemma"],
                "grammar": tok["grammar"],
                "senses_attested_in_panel": senses,
                "theme_lists": per_lemma_lists,
            }
        )

    # --- audit_trail section ------------------------------------------
    audit_trail = {
        "substrate_version": substrate_version,
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
        "score_methodology_documented_at": "Paper 1, Section II.B (substrate architecture and feature definitions)",
    }

    return {
        "verse_id": verse_id,
        "mūla": mula,
        "word_by_word": word_by_word,
        "intertextual_panel": intertextual_panel,
        "doctrinal_projections": doctrinal_projections,
        "prosodic_information": prosodic_information,
        "theme_list_memberships": theme_list_memberships,
        "audit_trail": audit_trail,
    }


def main() -> int:
    args = parse_args()
    obj = render_verse(args.verse, args.top_k, args.substrate_version)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(obj, ensure_ascii=False, indent=2))
    print(f"Wrote {args.output}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
