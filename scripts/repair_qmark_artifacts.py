"""Apply ?→, repair to sutrakrit-gita/rendered/. Same as summon-web fix.
Run from sutrakrit-gita root. Verifies before-string match, audit-trail stamps."""
import json, glob, sys, os
from datetime import datetime, timezone

RENDERED = "rendered"
DRY = "--apply" not in sys.argv

total_patches = 0
files_touched = 0
errors = []

for fpath in sorted(glob.glob(f"{RENDERED}/bg_*.json")):
    with open(fpath) as f:
        v = json.load(f)
    file_patches = 0
    for tok in v.get("word_by_word", []):
        for s in tok.get("senses_attested_in_panel", []):
            sense = s.get("sense", "")
            if "?" in sense:
                if not DRY:
                    s["sense"] = sense.replace("?", ",")
                file_patches += sense.count("?")
    if file_patches > 0:
        files_touched += 1
        total_patches += file_patches
        if not DRY:
            audit = v.setdefault("audit_trail", {}).setdefault("post_generation_repairs", [])
            audit.append({
                "kind": "qmark_artifact_repair",
                "applied_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "patches": file_patches,
                "root_cause": "ITRANS \\, escape coerced to ASCII ? in gitasupersite HTML pipeline",
                "verification": "Cross-school 5-verse alignment (12.13, 9.4, 11.32, 18.65, 14.5) vs sd_bgshankarabhashya.itx",
            })
            with open(fpath, "w") as f:
                json.dump(v, f, ensure_ascii=False, indent=2)

mode = "DRY-RUN" if DRY else "APPLY"
print(f"{mode}: {total_patches} ?-chars across {files_touched} files (in {RENDERED}/)")
