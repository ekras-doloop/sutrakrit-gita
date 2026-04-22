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

# Devanāgarī characters that should NEVER appear at the start of a
# valid gloss snippet — mātrā (vowel marks), virāma, anusvāra, visarga.
# Their presence at gloss-start means the lemma match was mid-akṣara of
# a longer word.
DEV_DEPENDENT_MARKS = set("\u093C\u093E\u093F\u0940\u0941\u0942\u0943\u0944\u0945\u0946\u0947\u0948\u0949\u094A\u094B\u094C\u094D\u0902\u0903")
# Word-break characters: a valid gloss should begin AFTER one of these
# in the commentary, otherwise the lemma match was mid-word.
DEV_WORD_BREAK = set(" \t\n।॥|.,;:!?()[]{}-\u00a0&")

# Minimum surface-form length (in Devanāgarī characters) for a token to
# be eligible for sense extraction. Below this, the surface form is too
# short to safely substring-match — single-character surface forms like
# च (and), ख, स, etc. occur inside hundreds of unrelated Sanskrit words.
MIN_SURFACE_LEN = 4

# Sanskrit particles, conjunctions, and auxiliary words that should
# NEVER be sent to sense extraction. These are real Sanskrit words but
# they (a) appear constantly in commentary as discourse particles
# rather than as content words being glossed, and (b) substring-match
# inside many longer words. The substrate's word_by_word section will
# still surface them with their grammar, but skip sense_attested_in_panel.
SANSKRIT_STOPLIST = {
    "च", "वा", "तु", "हि", "एव", "अपि", "इव", "इति", "किं", "किम्",
    "न", "नो", "मा", "अथ", "अहो", "तत्", "तत", "तदा", "यदा", "यथा", "तथा",
    "यद्", "यत्", "यः", "सः", "स", "अयम्", "अयं", "इदम्", "इदं",
    "एतत्", "एतद्", "एवम्", "एवं", "तस्मात्", "तस्मात", "अतः", "अत",
    "वै", "खलु", "नूनम्", "अत्र", "तत्र", "यत्र", "किल",
    # Common single-akṣara morphemes from over-segmentation
    "अ", "आ", "उ", "इ", "ए", "ओ", "ख", "स", "त", "य", "अहम्",
    # vidyut quirks that produce these as standalone "tokens"
    "ad", "as", "kha", "at",
}

# Devanāgarī letter range for is-letter test
def _is_dev_letter(ch: str) -> bool:
    return "\u0900" <= ch <= "\u097F" and ch not in DEV_WORD_BREAK


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
    """Return the index of the lemma's first WORD-BOUNDED occurrence in
    commentary, or -1.

    Word-boundary requirement: the lemma must appear with a word-break
    character immediately before it (or at string start) AND a word-break
    or compound-junction character immediately after it. This rejects
    substring matches inside larger compounds (e.g., 'bhūta' matching
    inside 'sarva-bhūta-hita' when we want only standalone 'bhūta').

    Compound boundaries are tricky because Sanskrit sandhi joins words.
    Our heuristic: the next character after the lemma should NOT be a
    Devanāgarī dependent vowel-mark or virāma — those would mean the
    lemma is mid-akṣara of a longer word.
    """
    if not lemma_devanagari:
        return -1
    start = 0
    while True:
        idx = commentary.find(lemma_devanagari, start)
        if idx < 0:
            return -1
        # Check char-before
        if idx > 0:
            prev_ch = commentary[idx - 1]
            # Reject if previous char is a Devanāgarī letter (lemma is mid-word)
            # Allow if previous char is a word-break, hyphen (compound junction),
            # or punctuation
            if prev_ch not in DEV_WORD_BREAK and not (
                prev_ch == "\u094D"  # virāma at end of prev syllable is OK
            ):
                # Check if previous char is itself a Devanāgarī letter
                if "\u0900" <= prev_ch <= "\u097F" and prev_ch not in DEV_WORD_BREAK:
                    start = idx + 1
                    continue
        # Check char-after: should not be a stranded mātrā
        after_idx = idx + len(lemma_devanagari)
        if after_idx < len(commentary):
            next_ch = commentary[after_idx]
            if next_ch in DEV_DEPENDENT_MARKS:
                # The character after is a vowel-mark or virāma — means our
                # lemma is mid-akṣara of a longer Sanskrit word. Reject.
                start = idx + 1
                continue
        return idx


def _extract_gloss_snippet(commentary: str, after_idx: int) -> str:
    """Extract the gloss snippet starting after the lemma occurrence.
    Trims at the first natural Sanskrit boundary (verse-end markers,
    common conjunction markers introducing new clauses).

    Also defensively skips any leading mātrā/virāma/whitespace residue
    in case the lemma-match cut left mid-akṣara fragments at the start.
    """
    window_end = min(len(commentary), after_idx + GLOSS_WINDOW)
    snippet = commentary[after_idx:window_end]
    # Defensively strip leading dependent vowel marks (mātrā), virāma,
    # anusvāra, visarga — none of these can validly start a gloss.
    while snippet and (snippet[0] in DEV_DEPENDENT_MARKS or snippet[0].isspace()):
        snippet = snippet[1:]
    # Trim at the first natural boundary
    end_match = GLOSS_END_MARKERS.search(snippet)
    if end_match and end_match.start() > 5:
        snippet = snippet[: end_match.start()]
    return snippet.strip()


def is_eligible_for_sense_extraction(
    lemma_devanagari: str,
    verse_devanagari: str = "",
) -> tuple[bool, str]:
    """Check whether a lemma surface-form is safe to send to sense extraction.

    Returns (is_eligible, reason). Filters out:
      - Empty / too-short surface forms (< MIN_SURFACE_LEN characters)
      - Surface forms in the Sanskrit stoplist (particles, conjunctions, etc.)
      - Surface forms that don't actually appear in the verse text (artifacts
        of vidyut over-segmentation of compound words)
    """
    if not lemma_devanagari:
        return False, "empty surface form"
    if lemma_devanagari in SANSKRIT_STOPLIST:
        return False, f"in Sanskrit stoplist (particle/conjunction)"
    # Strip trailing virāma (्) for length comparison since it doesn't add a syllable
    effective_len = len(lemma_devanagari.rstrip("\u094D"))
    if effective_len < MIN_SURFACE_LEN:
        return False, f"too short ({effective_len} chars; threshold {MIN_SURFACE_LEN})"
    if verse_devanagari and lemma_devanagari not in verse_devanagari:
        # Try without trailing virāma — vidyut's surface forms sometimes have
        # virāma added that the verse text doesn't have at the same position
        if lemma_devanagari.rstrip("\u094D") not in verse_devanagari:
            return False, "surface form not present in verse text (likely vidyut over-segmentation artifact)"
    return True, "eligible"


def extract_sense_for_lemma(
    lemma_devanagari: str,
    commentary: str,
) -> tuple[str, float]:
    """Extract one school's attested gloss for a lemma from its commentary
    on a specific verse.

    Returns (gloss_snippet, confidence_score). The snippet is in Devanāgarī.
    Empty string + 0.0 if not found or contamination-risk too high.

    Confidence score is in [0, 1]:
      0.0 = no extraction or rejected
      0.5 = matched but with weak word-boundary
      0.8 = matched with strong word-boundary on both sides
      1.0 = matched with strong word-boundary AND lemma is verse-specific
    """
    if not commentary:
        return "", 0.0
    cleaned = _clean_html_entities(commentary)
    idx = _find_lemma_in_commentary(lemma_devanagari, cleaned)
    if idx < 0:
        return "", 0.0
    after_idx = idx + len(lemma_devanagari)
    snippet = _extract_gloss_snippet(cleaned, after_idx)
    if len(snippet) < 5:
        return "", 0.0
    # Confidence assessment
    confidence = 0.5  # baseline if we got here at all
    # Strong-boundary check on both sides
    prev_ok = idx == 0 or cleaned[idx - 1] in DEV_WORD_BREAK
    if after_idx < len(cleaned):
        next_ch = cleaned[after_idx]
        next_ok = (next_ch in DEV_WORD_BREAK) or (next_ch == "\u094D")
    else:
        next_ok = True
    if prev_ok and next_ok:
        confidence = 0.8
    return snippet, confidence


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
    verse_devanagari: str = "",
    min_confidence: float = 0.8,
) -> list[dict]:
    """Given a lemma and a dict of {commentator_name: commentary_prose_or_None},
    extract per-school attested senses for the lemma.

    Filters out lemmas that are not eligible for sense extraction (too short,
    in Sanskrit stoplist, or not actually present in the verse text — the
    last is a vidyut over-segmentation safeguard).

    Each extracted sense carries a confidence score; senses below
    min_confidence are filtered out to prevent contamination from
    appearing in the per-verse object.

    Returns a list of sense dicts:
        [{
          "sense": "<gloss in Devanāgarī from the school commentary>",
          "school": "<school name>",
          "weight": <float, currently confidence-derived>,
          "witnesses": ["<commentator>_<verse>", ...]
        }, ...]
    """
    eligible, _ = is_eligible_for_sense_extraction(lemma_devanagari, verse_devanagari)
    if not eligible:
        return []

    senses = []
    for school, commentators in PANEL_COMMENTATORS.items():
        per_school_gloss = None
        per_school_witnesses = []
        per_school_confidence = 0.0
        for c in commentators:
            commentary = commentary_lookups.get(c)
            if not commentary:
                continue
            gloss, confidence = extract_sense_for_lemma(lemma_devanagari, commentary)
            if gloss and confidence >= min_confidence:
                if per_school_gloss is None:
                    per_school_gloss = gloss
                    per_school_confidence = confidence
                per_school_witnesses.append(c)
        if per_school_gloss:
            senses.append(
                {
                    "sense": per_school_gloss,
                    "school": school,
                    "weight": round(per_school_confidence, 2),
                    "witnesses": per_school_witnesses,
                }
            )
    return senses
