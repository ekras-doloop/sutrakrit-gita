#!/usr/bin/env python3
"""Rebuild the BG chapter-13 translator payloads with each commentary aligned
to the verse it actually discusses.

The edition counts chapter 13 as 34 verses (13.1 = "idaṃ śarīraṃ"). Most of
the commentary files count 35 (13.1 = Arjuna's question), so their 13.N+1 is
the edition's 13.N. The original payloads paired edition mūla N with every
commentary's 13.N, i.e. the previous verse's bhāṣya for those schools.
Measured on 2026-10-22 by matching each bhāṣya's pratīka words against the
mūla (see OFFSET); Rāmānuja and Ānandagiri count 34 except Rāmānuja's last
two (his 13.32 is duplicated as 13.33).

Writes data/translation_batches/ch13_realigned/verse_13_N.payload.json and
WITNESS (school -> [source ids]) used by the merge step.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COMM = ROOT / "panel-data" / "commentaries"
OUT = ROOT / "data" / "translation_batches" / "ch13_realigned"
MAX_CHARS = 3500   # prompt v1.0 input spec

SCHOOLS = {   # school -> (primary commentator, voice) — as in the original payloads
    "advaita": "shankara", "viśiṣṭādvaita": "ramanuja", "dvaita": "madhva",
    "śuddhādvaita": "vallabha", "bhakti": "sridhara", "advaita-bhakti": "madhusudan",
}
WITNESS = {   # school -> commentators cited, as in rendered/ witness_passages
    "advaita": ["shankara", "anandgiri"], "viśiṣṭādvaita": ["ramanuja", "vedantadeshika"],
    "dvaita": ["madhva", "jayatirtha"], "śuddhādvaita": ["vallabha"],
    "bhakti": ["sridhara"], "advaita-bhakti": ["madhusudan"],
}


def source_verse(commentator: str, n: int) -> int:
    """The commentator's own number for edition verse 13.n."""
    if commentator == "anandgiri":
        return n
    if commentator == "ramanuja":
        return n if n <= 32 else n + 1
    return n + 1


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    prose = {}
    for c in {c for cs in WITNESS.values() for c in cs}:
        rows = (json.loads(l) for l in (COMM / f"bg_{c}.jsonl").open(encoding="utf-8"))
        prose[c] = {r["verse"]: r["prose"] for r in rows}
    voices = json.loads((ROOT / "data/translation_batches/verse_13_5.payload.json").read_text())["schools"]
    for n in range(1, 35):
        verse = json.loads((ROOT / "rendered" / f"bg_13_{n}.json").read_text())
        schools = {}
        for school, c in SCHOOLS.items():
            src = f"13.{source_verse(c, n)}"
            schools[school] = {
                "voice": voices[school]["voice"],
                "primary_commentator": c,
                "source_verse": src,
                "panel_commentary_devanagari": prose[c].get(src, "")[:MAX_CHARS],
            }
        payload = {"verse_id": f"13.{n}", "mula_devanagari": verse["mūla"]["devanāgarī"],
                   "mula_iast": verse["mūla"]["iast"], "schools": schools,
                   "witness_passages": {s: [f"{c}_13.{source_verse(c, n)}" for c in cs
                                            if f"13.{source_verse(c, n)}" in prose[c]]
                                        for s, cs in WITNESS.items()}}
        (OUT / f"verse_13_{n}.payload.json").write_text(json.dumps(payload, ensure_ascii=False, indent=1))
    print(f"wrote 34 payloads to {OUT}")


if __name__ == "__main__":
    main()
