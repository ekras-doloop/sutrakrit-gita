"""Validate every per-verse object in `rendered/` against the schema.

Usage:
    python scripts/validate_rendered.py
    python scripts/validate_rendered.py --rendered-dir rendered/

Reports per-file pass/fail and a summary count. Exit code is non-zero
if any object fails validation; suitable for CI use.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import jsonschema

REPO_ROOT = Path(__file__).resolve().parents[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate rendered per-verse objects against the schema."
    )
    parser.add_argument(
        "--rendered-dir",
        type=Path,
        default=REPO_ROOT / "rendered",
        help="Directory of per-verse JSON outputs to validate (default: rendered/)",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=REPO_ROOT / "schema" / "per-verse-object.schema.json",
        help="Path to the JSON Schema (default: schema/per-verse-object.schema.json)",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Print only failures (default: print pass/fail per file)",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.rendered_dir.exists():
        print(f"ERROR: {args.rendered_dir} does not exist", file=sys.stderr)
        return 2

    schema = json.loads(args.schema.read_text())
    validator = jsonschema.Draft202012Validator(schema)

    files = sorted(args.rendered_dir.glob("bg_*.json"))
    if not files:
        print(f"No bg_*.json files in {args.rendered_dir}", file=sys.stderr)
        return 0

    passed = 0
    failed = 0
    for f in files:
        try:
            obj = json.loads(f.read_text())
            errors = list(validator.iter_errors(obj))
            if errors:
                failed += 1
                print(f"FAIL {f.name}:")
                for err in errors:
                    print(f"  {err.message} at {list(err.absolute_path)}")
            else:
                passed += 1
                if not args.quiet:
                    print(f"OK   {f.name}")
        except Exception as e:
            failed += 1
            print(f"ERROR {f.name}: {e}")

    print(f"\nSummary: {passed} passed, {failed} failed (total {len(files)})")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
