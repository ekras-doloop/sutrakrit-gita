"""Merge subagent batch results into the main reading_summaries cache.

Reads every batch_NNNN.results.json in data/summary_batches/ and folds
the (cache_key → summary) entries into data/reading_summaries.cache.json,
which the renderer reads.

Idempotent: running it multiple times produces no change after the
first run if no new batch results have appeared.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
BATCH_DIR = REPO_ROOT / "data" / "summary_batches"
CACHE_PATH = REPO_ROOT / "data" / "reading_summaries.cache.json"


def main() -> int:
    cache: dict = {}
    if CACHE_PATH.exists():
        cache = json.loads(CACHE_PATH.read_text())

    initial_size = len(cache)
    added = 0
    skipped = 0
    files_processed = 0

    for results_file in sorted(BATCH_DIR.glob("batch_*.results.json")):
        files_processed += 1
        try:
            results = json.loads(results_file.read_text())
        except Exception as e:
            print(f"  WARN: failed to parse {results_file.name}: {e}", file=sys.stderr)
            continue
        for cache_key, summary in results.items():
            if cache_key in cache:
                skipped += 1
                continue
            cache[cache_key] = summary
            added += 1

    if added > 0:
        CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
        CACHE_PATH.write_text(
            json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True)
        )

    print(f"Processed: {files_processed} batch result files")
    print(f"Cache before: {initial_size} entries")
    print(f"Cache after: {len(cache)} entries (+{added} new, {skipped} dupes skipped)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
