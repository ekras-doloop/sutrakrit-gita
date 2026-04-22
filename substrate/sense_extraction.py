"""Per-lemma sense extraction from school commentary.

Given a verse's lemmas and the panel commentaries on that verse,
extract each school's attested sense for each lemma.

Approach: the Sanskrit-bhāṣya tradition follows a canonical gloss
pattern in commentaries — each verse-lemma appears in the commentary
prose followed within a short window by the commentator's gloss
(typically a synonym, a synonym-list, or a brief explanation in
Sanskrit prose). For example, Śaṅkara on BG 2.55:

    प्रजहाति → प्रकर्षेण जहाति परित्यजति
    सर्वान्  → समस्तान्
    कामान्  → इच्छाभेदान्
    सthitaprajña → स्थिता प्रतिष्ठिता आत्मानात्मविवेकजा प्रज्ञा यस्य सः

The extractor:
  1. Searches each school's commentary text for each lemma's surface form
  2. Extracts the following ~120 chars as the candidate gloss
  3. Cleans HTML entities (&nbsp; etc.) and punctuation residue
  4. Trims at the next sandhi-boundary or punctuation marker
  5. Returns per-school gloss-snippets in Devanāgarī

This is bhāṣya-internal sense surfacing — it does not translate the
gloss into English (translation is an additional collapse layer that
adds the translator's commitment to the substrate's output, which
the airgap principle prohibits). Readers who want English glosses
must apply their own translation to the surfaced Devanāgarī gloss-snippet,
or query a different reading-system for translation. The substrate
surfaces the school's actual gloss in the school's own register.
"""

from __future__ import annotations

import re

NBSP = "\u00a0"
GLOSS_WINDOW = 120  # characters after the lemma to scan for gloss
GLOSS_END_MARKERS = re.compile(r"[।॥|]|(?:\s+(?:हे|यः|यत्|च\s|एव\s|अपि\s|तत्\s|तस्य\s))")


def _clean_html_entities(text: str) -> str:
    """Strip HTML entities and normalize whitespace."""
    text = text.replace("&nbsp;", " ")
    text = text.replace(NBSP, " ")
    text = re.sub(r"&[a-zA-Z]+;", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _find_lemma_in_commentary(
    lemma_devanagari: str, commentary: str
) -> int:
    """Return the index of the lemma's first occurrence in commentary, or -1."""
    return commentary.find(lemma_devanagari)


def _extract_gloss_snippet(commentary: str, after_idx: int) -> str:
    """Extract the gloss snippet starting after the lemma occurrence.
    Trims at the first natural Sanskrit boundary (verse-end markers,
    common conjunction markers introducing new clauses).
    """
    window_end = min(len(commentary), after_idx + GLOSS_WINDOW)
    snippet = commentary[after_idx:window_end]
    # Trim at the first natural boundary
    end_match = GLOSS_END_MARKERS.search(snippet)
    if end_match and end_match.start() > 5:  # require at least 5 chars of gloss
        snippet = snippet[: end_match.start()]
    return snippet.strip()


def extract_sense_for_lemma(
    lemma_devanagari: str,
    commentary: str,
) -> str:
    """Extract one school's attested gloss for a lemma from its commentary
    on a specific verse.

    Returns the gloss-snippet in Devanāgarī, or empty string if not found.
    """
    cleaned = _clean_html_entities(commentary)
    idx = _find_lemma_in_commentary(lemma_devanagari, cleaned)
    if idx < 0:
        return ""
    after_idx = idx + len(lemma_devanagari)
    snippet = _extract_gloss_snippet(cleaned, after_idx)
    if len(snippet) < 5:
        return ""
    return snippet


# School identifiers used in the panel-data filenames
PANEL_COMMENTATORS = {
    "advaita": ["shankara", "anandgiri"],
    "viśiṣṭādvaita": ["ramanuja", "vedantadeshika"],
    "dvaita": ["madhva", "jayatirtha"],
    "śuddhādvaita": ["vallabha"],
    "bhakti": ["sridhara"],
    "advaita-bhakti": ["madhusudan"],
}


def extract_panel_senses(
    lemma_devanagari: str,
    commentary_lookups: dict[str, str | None],
) -> list[dict]:
    """Given a lemma and a dict of {commentator_name: commentary_prose_or_None},
    extract per-school attested senses for the lemma.

    Returns a list of sense dicts conforming to the per-verse schema's
    senses_attested_in_panel field:

        [{
          "sense": "<gloss in Devanāgarī from the school commentary>",
          "school": "<school name>",
          "weight": <float, currently uniform>,
          "witnesses": ["<commentator>_<verse>", ...]
        }, ...]
    """
    senses = []
    for school, commentators in PANEL_COMMENTATORS.items():
        per_school_glosses = []
        per_school_witnesses = []
        for c in commentators:
            commentary = commentary_lookups.get(c)
            if not commentary:
                continue
            gloss = extract_sense_for_lemma(lemma_devanagari, commentary)
            if gloss:
                per_school_glosses.append(gloss)
                per_school_witnesses.append(c)
        if per_school_glosses:
            # Use the first commentator's gloss as the canonical school-gloss;
            # additional commentators' glosses can be folded into witnesses.
            senses.append(
                {
                    "sense": per_school_glosses[0],
                    "school": school,
                    "weight": round(1.0 / len(per_school_glosses), 2),
                    "witnesses": per_school_witnesses,
                }
            )
    return senses
