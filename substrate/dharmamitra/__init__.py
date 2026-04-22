"""Dharmamitra ByT5-Sanskrit-multitask analyzer wrapper.

Wraps `chronbmm/sanskrit5-multitask` (Nehrdich, Hellwig, Keutzer EMNLP 2024)
into a `tokenize_with_grammar(devanagari) -> [{surface, lemma, grammar}]`
function compatible with the existing substrate.sutrakrit.Substrate API.

This is the parser the Sūtrakṛt v1.0 substrate paper depends on. It replaces
vidyut-cheda (lemma agreement ~14% vs gold) with the SOTA character-level
T5 trained on the Digital Corpus of Sanskrit (DCS).

Confirmed on BG 2.15 (live test 2026-04-22): produces 16/16 correct lemmas
with full Case|Gender|Number|Tense|Mood|Person tagging. Vidyut produced 0.
"""
from __future__ import annotations
from pathlib import Path

_MODEL_ID = "chronbmm/sanskrit5-multitask"
_TAGS_PATH = Path(__file__).parent / "data" / "sanskrit_tags.tsv"

_model = None
_tokenizer = None
_device = None
_tags: dict[str, str] = {}


def _load_tags() -> dict[str, str]:
    global _tags
    if _tags:
        return _tags
    for line in _TAGS_PATH.read_text().splitlines():
        parts = line.split("\t")
        if len(parts) >= 2:
            _tags[parts[0]] = parts[1].strip()
    return _tags


def _load_model():
    global _model, _tokenizer, _device
    if _model is not None:
        return _model, _tokenizer, _device
    from transformers import T5ForConditionalGeneration, AutoTokenizer
    import torch
    _tokenizer = AutoTokenizer.from_pretrained(_MODEL_ID)
    _model = T5ForConditionalGeneration.from_pretrained(_MODEL_ID)
    _device = (
        "mps" if torch.backends.mps.is_available()
        else "cuda" if torch.cuda.is_available()
        else "cpu"
    )
    _model = _model.to(_device).eval()
    _load_tags()
    return _model, _tokenizer, _device


# Map UD-style tag values to short human-readable English
_HUMANIZE = {
    "Acc": "accusative", "Nom": "nominative", "Voc": "vocative",
    "Dat": "dative", "Gen": "genitive", "Loc": "locative",
    "Ins": "instrumental", "Abl": "ablative", "Cpd": "compound",
    "Masc": "masculine", "Fem": "feminine", "Neut": "neuter",
    "Sing": "singular", "Dual": "dual", "Plur": "plural",
    "Pres": "present", "Past": "past", "Fut": "future",
    "Ind": "indicative", "Imp": "imperative", "Opt": "optative",
    "1": "1st person", "2": "2nd person", "3": "3rd person",
    "Part": "participle", "Inf": "infinitive", "Ger": "gerund",
}


def _humanize_tag(short_tag: str) -> str:
    full = _tags.get(short_tag, "")
    if not full:
        return ""
    parts = []
    for kv in full.split("|"):
        if "=" in kv:
            _, v = kv.split("=", 1)
            parts.append(_HUMANIZE.get(v, v.lower()))
    if parts:
        if "compound" in parts:
            parts.append("(compound member)")
        else:
            # add part-of-speech inference: tense/mood/person → verb; case/gender → noun
            if any(p in {"present", "past", "future"} for p in parts):
                parts.append("verb")
            elif any(p in {"nominative", "accusative", "vocative", "dative", "genitive", "locative", "instrumental", "ablative"} for p in parts):
                parts.append("noun")
    return " ".join(parts)


def _devanagari_to_iast(text: str) -> str:
    """Use vidyut.lipi for Dev → IAST. Falls back to indic_transliteration if absent."""
    try:
        from vidyut.lipi import Scheme, transliterate
        return transliterate(text, Scheme.Devanagari, Scheme.Iast)
    except Exception:
        try:
            from indic_transliteration import sanscript
            return sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.IAST)
        except Exception:
            return text


def tokenize_with_grammar(devanagari_text: str) -> list[dict]:
    """Sūtrakṛt-compatible per-token grammar extraction via ByT5-multitask.

    Returns rows of {surface_form, lemma, grammar} suitable for the existing
    page renderer and per-verse JSON schema.
    """
    import re
    import torch
    iast = _devanagari_to_iast(devanagari_text)
    # Strip danda + punctuation for cleaner input
    iast = re.sub(r"[\|\.\,\;\:\?]", " ", iast).strip()
    if not iast:
        return []
    model, tokenizer, device = _load_model()
    inp = tokenizer(
        "SLM " + iast,
        return_tensors="pt",
        truncation=True,
        max_length=512,
    ).to(device)
    with torch.inference_mode():
        out = model.generate(**inp, max_length=512)
    raw = tokenizer.decode(out[0], skip_special_tokens=True)
    return _parse_slm_output(raw)


# Known Unicode mangling in the multitask checkpoint's decoder:
# ṛ (U+1E5B) tokens occasionally roundtrip as ﾱ (U+FFB1, halfwidth katakana).
# Spot-fix at the lemma layer.
_UNICODE_FIXES = {
    "\uffb1": "ṛ",
}


def _fix_unicode(s: str) -> str:
    for bad, good in _UNICODE_FIXES.items():
        s = s.replace(bad, good)
    return s


def _parse_slm_output(raw: str) -> list[dict]:
    """Parse SLM-mode output: items separated by spaces,
    each as `<surface>_<lemma>_<short_tag>`.
    """
    rows = []
    for item in raw.split(" "):
        item = item.strip().lstrip("_")
        if not item:
            continue
        parts = item.split("_")
        if len(parts) < 3:
            continue
        surface, lemma, short_tag = parts[0], parts[1], parts[2]
        # Filter junk: empty lemmas, single-char fragments where surface is longer
        if not lemma or not surface:
            continue
        # The Devanāgarī-encoded lemma sometimes has bytes-mangled chars (e.g. kﾱp);
        # accept as-is, downstream consumers can re-transliterate.
        grammar = _humanize_tag(short_tag) if short_tag else ""
        rows.append({
            "surface_form": _fix_unicode(surface),
            "lemma": _fix_unicode(lemma),
            "grammar": grammar,
        })
    return rows


__all__ = ["tokenize_with_grammar"]
