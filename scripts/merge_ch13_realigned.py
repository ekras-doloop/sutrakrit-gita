#!/usr/bin/env python3
"""Fold the realigned chapter-13 panels into rendered verse JSONs.

Reads data/translation_results/bg13_realigned/verse_13_N.results.json (made
from data/translation_batches/ch13_realigned, see
build_ch13_realigned_payloads.py) and, for each target directory, replaces
per school: english_rendering, divergence_note, commentator and
witness_passages (now in each commentator's own verse numbering), plus the
verse's so_what_questions and everyday_applications. Appends an audit_trail
entry. Refuses to write anything if any of the 34 results is incomplete.

    python3 scripts/merge_ch13_realigned.py rendered ~/Code/project-awaaz/summon-web/public/gita-data
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "data" / "translation_results" / "bg13_realigned"
PAYLOADS = ROOT / "data" / "translation_batches" / "ch13_realigned"
SCHOOLS = ["advaita", "viśiṣṭādvaita", "dvaita", "śuddhādvaita", "bhakti", "advaita-bhakti"]


def load_checked(n: int) -> tuple[dict, dict]:
    res = json.loads((RESULTS / f"verse_13_{n}.results.json").read_text(encoding="utf-8"))
    pay = json.loads((PAYLOADS / f"verse_13_{n}.payload.json").read_text(encoding="utf-8"))
    assert res["verse_id"] == f"13.{n}", (n, res["verse_id"])
    dr, ea = res["doctrinal_renderings"], res["everyday_applications"]
    for s in SCHOOLS:
        assert dr[s]["english"].strip(), (n, s, "empty rendering")
        assert ea[s].strip(), (n, s, "empty application")
    assert 5 <= len(res["so_what_questions"]) <= 7, (n, len(res["so_what_questions"]))
    text = json.dumps(res, ensure_ascii=False)
    assert not any(q in text for q in "‘’“”"), (n, "smart quotes")
    return res, pay


def main(targets: list[Path]) -> None:
    panels = {n: load_checked(n) for n in range(1, 35)}
    stamp = datetime.now(timezone.utc).isoformat()
    for target in targets:
        for n, (res, pay) in panels.items():
            f = target / f"bg_13_{n}.json"
            raw = f.read_text(encoding="utf-8")
            verse = json.loads(raw)
            # keep each copy's own layout: the site writes indent=1, no newline
            indent, tail = (1, "") if raw.startswith('{\n "') else (2, "\n")
            for s in SCHOOLS:
                proj = verse["doctrinal_projections"].setdefault(s, {})
                r = res["doctrinal_renderings"][s]
                proj["english_rendering"] = r["english"].strip()
                proj["divergence_note"] = (r.get("divergence_note") or "").strip()
                proj["commentator"] = r["commentator"]
                proj["witness_passages"] = pay["witness_passages"][s]
            verse["so_what_questions"] = res["so_what_questions"]
            verse["everyday_applications"] = {s: res["everyday_applications"][s] for s in SCHOOLS}
            verse["audit_trail"].setdefault("post_generation_repairs", []).append({
                "kind": "ch13_commentary_realignment",
                "applied_at": stamp,
                "applied_by": "sutrakrit-gita/scripts/merge_ch13_realigned.py",
                "root_cause": "Chapter 13 commentaries count 35 verses (13.1 = Arjuna's question) "
                              "but the edition counts 34; payloads paired mūla 13.N with each "
                              "commentary's 13.N, i.e. the previous verse's bhāṣya for most schools.",
                "source_verses": {s: pay["schools"][s]["source_verse"] for s in SCHOOLS},
            })
            f.write_text(json.dumps(verse, ensure_ascii=False, indent=indent) + tail, encoding="utf-8")
        print(f"merged 34 verses into {target}")


if __name__ == "__main__":
    main([Path(a).expanduser() for a in sys.argv[1:]])
