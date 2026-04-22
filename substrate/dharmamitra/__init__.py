"""Dharmamitra ByT5-Sanskrit-multitask analyzer wrapper.

Wraps `chronbmm/sanskrit5-multitask` (Nehrdich, Hellwig, Keutzer EMNLP 2024)
into a `tokenize_with_grammar(devanagari) -> [{surface, lemma, grammar}]`
function compatible with the existing substrate.sutrakrit.Substrate API.

This is the parser the Sūtrakṛt v1.0 substrate paper depends on. It replaces
vidyut-cheda (lemma agreement ~14% vs gold) with the SOTA character-level
T5 trained on the Digital Corpus of Sanskrit (DCS).
"""
from __future__ import annotations
from pathlib import Path
from typing import Optional

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
    _device = "mps" if torch.backends.mps.is_available() else "cuda" if torch.cuda.is_available() else "cpu"
    _model = _model.to(_device).eval()
    _load_tags()
    return _model, _tokenizer, _device


def _humanize(short_tag: str) -> str:
    """Convert SLM-style short tag to human-readable English grammar."""
    full = _tags.get(short_tag, short_tag)
    parts = full.split("|")
    out = []
    for p in parts:
        if "=" in p:
            k, v = p.split("=", 1)
            out.append(v.lower())
    return " ".join(out)


def tokenize_with_grammar(devanagari_text: str) -> list[dict]:
    """Sūtrakṛt-compatible per-token grammar extraction.

    Returns rows of {surface_form, lemma, grammar} suitable for the existing
    page renderer and per-verse JSON schema.
    """
    import torch
    model, tokenizer, device = _load_model()
    inp = tokenizer(
        "SLM " + devanagari_text,
        return_tensors="pt",
        truncation=True,
        max_length=512,
    ).to(device)
    with torch.inference_mode():
        out = model.generate(**inp, max_length=512)
    raw = tokenizer.decode(out[0], skip_special_tokens=True)
    return _parse_slm_output(raw)


def _parse_slm_output(raw: str) -> list[dict]:
    """Parse model SLM output: items separated by spaces, each as
    `<surface>_<lemma>_<short_tag>` (or with leading `__` markers).
    """
    rows = []
    for item in raw.split(" "):
        item = item.strip().lstrip("_")
        if not item or "_" not in item:
            continue
        parts = item.split("_")
        if len(parts) >= 3:
            surface, lemma, short_tag = parts[0], parts[1], parts[2]
            grammar = _humanize(short_tag)
            rows.append({
                "surface_form": surface,
                "lemma": lemma,
                "grammar": grammar,
            })
        elif len(parts) == 2:
            lemma, short_tag = parts
            rows.append({
                "surface_form": "",
                "lemma": lemma,
                "grammar": _humanize(short_tag),
            })
    return rows


__all__ = ["tokenize_with_grammar"]
