"""Prepare summary-batches for subagent dispatch.

Walks the BG corpus, identifies all (verse_id, school) pairs that have
panel commentary and that are NOT yet in the reading_summaries cache,
and writes them to batch files in data/summary_batches/.

Each batch file is a JSON array of:
  {
    "verse_id": "X.Y",
    "school": "advaita",
    "verse_devanagari": "...",
    "commentary": "...",
    "school_label": "Advaita Vedānta (non-dualist)",
  }

The renderer's subagent dispatch loop reads each batch, summarizes
each item, and writes back to data/reading_summaries.cache.json.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

from substrate import Substrate  # noqa: E402
from substrate.reading_summaries import (  # noqa: E402
    CACHE_PATH,
    DEFAULT_MODELS,
    SCHOOL_LABELS,
)

BATCH_DIR = REPO_ROOT / "data" / "summary_batches"
BATCH_SIZE = 12

SCHOOL_TO_COMMENTATORS = {
    "advaita": ["shankara", "anandgiri"],
    "viśiṣṭādvaita": ["ramanuja", "vedantadeshika"],
    "dvaita": ["madhva", "jayatirtha"],
    "śuddhādvaita": ["vallabha"],
    "bhakti": ["sridhara"],
    "advaita-bhakti": ["madhusudan"],
}


def main() -> int:
    BATCH_DIR.mkdir(parents=True, exist_ok=True)
    # Clear any prior batches
    for f in BATCH_DIR.glob("batch_*.json"):
        f.unlink()

    # Load the cache to know what's already done
    cache = {}
    if CACHE_PATH.exists():
        cache = json.loads(CACHE_PATH.read_text())

    # We use claude-sonnet-4.5 as the canonical model identifier so
    # subagent-generated summaries cache under the same key as the
    # OpenRouter Claude Sonnet 4.5 entries (the 27 already cached).
    model_key = "anthropic/claude-sonnet-4.5"

    sub = Substrate()
    pending: list[dict] = []
    for verse_id in sub.all_verses():
        verse_text = sub.get_verse(verse_id)
        for school, commentators in SCHOOL_TO_COMMENTATORS.items():
            cache_key = f"{verse_id}::{school}::{model_key}"
            if cache_key in cache:
                continue
            primary_prose = None
            for c in commentators:
                prose = sub.panel_commentary_for(c, verse_id)
                if prose and len(prose) >= 50:
                    primary_prose = prose
                    break
            if not primary_prose:
                continue
            # Trim very long commentary to keep subagent context tractable
            primary_prose = primary_prose[:3500]
            pending.append({
                "verse_id": verse_id,
                "school": school,
                "verse_devanagari": verse_text,
                "commentary": primary_prose,
                "school_label": SCHOOL_LABELS[school],
                "cache_key": cache_key,
            })

    # Batch them
    n_batches = (len(pending) + BATCH_SIZE - 1) // BATCH_SIZE
    for i in range(n_batches):
        batch = pending[i * BATCH_SIZE : (i + 1) * BATCH_SIZE]
        batch_path = BATCH_DIR / f"batch_{i:04d}.json"
        batch_path.write_text(json.dumps(batch, ensure_ascii=False, indent=2))

    cache_size = len(cache)
    print(f"Cached: {cache_size} summaries")
    print(f"Pending: {len(pending)} summaries to generate")
    print(f"Batched into: {n_batches} batches of up to {BATCH_SIZE} each")
    print(f"Batch files written to: {BATCH_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
