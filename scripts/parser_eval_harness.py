#!/usr/bin/env python3
"""Parser-eval harness — runs every available Sanskrit parser against the
50-verse gold subset and emits side-by-side per-token tables for hand
labeling and quality measurement.

Outputs:
  data/parser_eval/runs/vidyut_cheda.json        (current substrate)
  data/parser_eval/runs/byt5_sanskrit.json       (target swap)
  data/parser_eval/runs/translist.json           (when wired)
  data/parser_eval/labeling/<verse_id>.csv       (hand-labeling sheet)

Per-token row schema (for labeling sheet):
  position | surface | parser_lemma | parser_morph | gold_lemma | gold_morph | gold_gloss | notes
"""
from __future__ import annotations
import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
GOLD = ROOT / "data" / "parser_eval" / "gold_50" / "verses.json"
RUNS = ROOT / "data" / "parser_eval" / "runs"
LABELS = ROOT / "data" / "parser_eval" / "labeling"
sys.path.insert(0, str(ROOT))


def run_vidyut() -> dict:
    """Current substrate baseline — for measuring delta only."""
    from substrate.sutrakrit import Substrate
    sub = Substrate()
    out = {}
    verses = json.loads(GOLD.read_text())
    for v in verses:
        toks = sub.tokenize_with_grammar(v["devanagari"])
        out[v["verse_id"]] = [
            {
                "surface_form": t["surface_form"],
                "lemma": t["lemma"],
                "grammar": t["grammar"],
            }
            for t in toks
        ]
    RUNS.mkdir(parents=True, exist_ok=True)
    (RUNS / "vidyut_cheda.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)
    )
    print(f"vidyut: {len(out)} verses, {sum(len(v) for v in out.values())} tokens")
    return out


def run_byt5_sanskrit_analyzer() -> dict:
    """ByT5-Sanskrit-analyzer (Hellwig / buddhist-nlp).

    Input: Devanāgarī verse string. Output: structured per-token analysis
    (format inferred from model behavior on first call — model card is empty).
    """
    from transformers import T5ForConditionalGeneration, AutoTokenizer
    import torch

    model_id = "buddhist-nlp/byt5-sanskrit-analyzer-hackathon"
    print(f"Loading {model_id} (this is the first call — may take a minute)...")
    tok = AutoTokenizer.from_pretrained(model_id)
    model = T5ForConditionalGeneration.from_pretrained(model_id)
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    print(f"Using device: {device}")
    model = model.to(device).eval()

    out = {}
    verses = json.loads(GOLD.read_text())
    for v in verses:
        text = v["devanagari"]
        # ByT5 is character-level; no special tokenization needed.
        # The Hellwig analyzer was trained to emit JSON-ish per-token analysis.
        # Try unprefixed; if outputs are empty, retry with task prefixes.
        inp = tok(text, return_tensors="pt", truncation=True, max_length=256).to(device)
        with torch.inference_mode():
            gen = model.generate(
                **inp,
                max_new_tokens=512,
                num_beams=1,
                do_sample=False,
            )
        decoded = tok.decode(gen[0], skip_special_tokens=True)
        out[v["verse_id"]] = {"raw": decoded, "input": text}
        print(f"  {v['verse_id']}: {decoded[:200]!r}")
    RUNS.mkdir(parents=True, exist_ok=True)
    (RUNS / "byt5_sanskrit_raw.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2)
    )
    return out


def emit_labeling_sheets() -> None:
    """One CSV per verse for hand labeling.

    Each row = one parser-emitted token. Annotator can mark CORRECT / WRONG
    in the gold_lemma + gold_morph fields, or add missing tokens at the bottom.
    """
    LABELS.mkdir(parents=True, exist_ok=True)
    vidyut = json.loads((RUNS / "vidyut_cheda.json").read_text())
    verses = json.loads(GOLD.read_text())
    for v in verses:
        vid = v["verse_id"]
        rows = vidyut.get(vid, [])
        out_path = LABELS / f"{vid}.csv"
        with open(out_path, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow([
                "position", "surface", "vidyut_lemma", "vidyut_morph",
                "gold_lemma", "gold_morph", "gold_gloss", "notes",
            ])
            w.writerow([
                "# verse:", v["devanagari"], "", "", "", "", "", v["iast"],
            ])
            for i, r in enumerate(rows):
                w.writerow([
                    i, r["surface_form"], r["lemma"], r["grammar"],
                    "", "", "", "",
                ])
        print(f"  wrote {out_path}")


def main() -> int:
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument("--parser", choices=["vidyut", "byt5", "label", "all"], default="all")
    args = p.parse_args()
    if args.parser in ("vidyut", "all"):
        run_vidyut()
    if args.parser in ("label", "all"):
        emit_labeling_sheets()
    if args.parser in ("byt5", "all"):
        run_byt5_sanskrit_analyzer()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
