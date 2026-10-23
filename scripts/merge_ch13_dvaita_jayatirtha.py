#!/usr/bin/env python3
"""BG 13 dvaita slots: credit Jayatīrtha where he fills out a terse Madhva, and
say so where both are silent.

Madhva's Gītā-bhāṣya passes over many verses of chapter 13 or glosses a word
or two; Jayatīrtha's Prameyadīpikā comments on Madhva, so it speaks only where
Madhva does. For the seven thin verses, the reading is rewritten from both
(data/translation_results/bg13_dvaita_jayatirtha/). For verses where Madhva is
absent, the note now records Jayatīrtha's silence too, verified from
panel-data rather than assumed.

Updates the bg13_realigned results files and every target rendered directory.

    python3 scripts/merge_ch13_dvaita_jayatirtha.py rendered ~/Code/project-awaaz/summon-web/public/gita-data
"""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "data" / "translation_results" / "bg13_realigned"
JAYA = ROOT / "data" / "translation_results" / "bg13_dvaita_jayatirtha"
COMM = ROOT / "panel-data" / "commentaries"
THIN = (1, 4, 6, 11, 14, 18, 19)
PREFIX = "Read with Jayatīrtha's Prameyadīpikā on Madhva's bhāṣya"


def prose(name: str) -> dict:
    return {json.loads(l)["verse"]: json.loads(l)["prose"]
            for l in (COMM / f"bg_{name}.jsonl").open(encoding="utf-8")}


def silence_note(text: str) -> str | None:
    body = text.split("।।", 2)[-1].strip() if text else ""
    if not body or "did not comment" in body:
        return "Jayatīrtha's Prameyadīpikā is also silent on this verse."
    if len(body) < 40:
        return f"Jayatīrtha's Prameyadīpikā gives only the opening words ({body})."
    return None


def main(targets: list[Path]) -> None:
    madhva, jaya = prose("madhva"), prose("jayatirtha")
    updates = {}   # n -> (dvaita rendering dict, everyday application or None)
    for n in range(1, 35):
        res = json.loads((RESULTS / f"verse_13_{n}.results.json").read_text(encoding="utf-8"))
        dv = res["doctrinal_renderings"]["dvaita"]
        src = f"13.{n + 1}"
        if n in THIN:
            j = json.loads((JAYA / f"verse_13_{n}.dvaita.json").read_text(encoding="utf-8"))
            assert j["verse_id"] == f"13.{n}" and j["divergence_note"].startswith(PREFIX), n
            assert j["english"].strip() and j["everyday_application"].strip(), n
            dv = {"english": j["english"].strip(), "key_terms_preserved": j["key_terms_preserved"],
                  "divergence_note": j["divergence_note"].strip(), "commentator": j["commentator"]}
            updates[n] = (dv, j["everyday_application"].strip())
        else:
            m = madhva.get(src, "")
            body = m.split("।।", 2)[-1].strip()
            madhva_absent = len(body) < 40 or "did not comment" in body   # < 40: the pratīka alone
            note = silence_note(jaya.get(src, "")) if madhva_absent else None
            if not note:
                continue
            if note not in dv["divergence_note"]:
                dv = {**dv, "divergence_note": f"{dv['divergence_note'].rstrip()} {note}"}
            updates[n] = (dv, None)
        res["doctrinal_renderings"]["dvaita"] = dv
        if updates[n][1]:
            res["everyday_applications"]["dvaita"] = updates[n][1]
        (RESULTS / f"verse_13_{n}.results.json").write_text(
            json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")

    stamp = datetime.now(timezone.utc).isoformat()
    for target in targets:
        for n, (dv, everyday) in updates.items():
            f = target / f"bg_13_{n}.json"
            raw = f.read_text(encoding="utf-8")
            verse = json.loads(raw)
            indent, tail = (1, "") if raw.startswith('{\n "') else (2, "\n")
            proj = verse["doctrinal_projections"]["dvaita"]
            proj["english_rendering"] = dv["english"]
            proj["divergence_note"] = dv["divergence_note"]
            proj["commentator"] = dv["commentator"]
            if everyday:
                verse["everyday_applications"]["dvaita"] = everyday
            repairs = verse["audit_trail"].setdefault("post_generation_repairs", [])
            repairs[:] = [r for r in repairs if r.get("kind") != "ch13_dvaita_jayatirtha"]
            repairs.append({"kind": "ch13_dvaita_jayatirtha", "applied_at": stamp,
                            "applied_by": "sutrakrit-gita/scripts/merge_ch13_dvaita_jayatirtha.py",
                            "change": "reading rewritten with Jayatirtha's Prameyadipika" if everyday
                                      else "note records that Jayatirtha is also silent"})
            f.write_text(json.dumps(verse, ensure_ascii=False, indent=indent) + tail, encoding="utf-8")
        print(f"{target}: {len(updates)} verses ({sum(1 for u in updates.values() if u[1])} rewritten)")


if __name__ == "__main__":
    main([Path(a).expanduser() for a in sys.argv[1:]])
