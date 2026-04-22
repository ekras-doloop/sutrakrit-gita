# Sūtrakṛt-Gītā Architecture

This document describes how the substrate-rendered Bhagavad Gītā edition is built — what the components are, how they fit together, and how a new researcher can navigate the codebase.

## High-level pipeline

```
Source corpora (panel-data/) ──┐
                                │
                                ▼
                       Substrate (substrate/)
                       fitted on Ramsukhdas
                       frozen weights v2.6
                                │
                                ▼
                       Per-verse renderer
                       (scripts/render_verse.py)
                                │
                                ▼
                       Rendered objects (rendered/)
                       conforming to schema/per-verse-object.schema.json
                                │
                                ▼
                       Web frontend (web/)
                       deployed to gita.ekrasworks.com
```

The pipeline operates on a per-verse basis. For each of the 700 BG verses, the renderer:

1. Loads the verse's mūla text from the BORI critical edition
2. Lemmatizes the verse via vidyut-cheda
3. Looks up panel cross-references where this verse is the source or target
4. Computes the substrate's full feature scores against all 699 other BG verses
5. Selects top-K intertextual candidates with feature breakdown
6. Surfaces per-school doctrinal projections from the panel evidence
7. Computes prosodic and theme-list metadata
8. Assembles the per-verse object conforming to `schema/per-verse-object.schema.json`
9. Writes the object to `rendered/bg_X_Y.json`

## Component responsibilities

### `substrate/`

The Sūtrakṛt computational substrate. The core scoring function and feature implementations described in Paper 1 Section II.B.

Key files:
- `sutrakrit_unified_findings.py` — the full substrate runner that produces panel results across all commentators
- `tilak_eval.py` — substrate evaluation against Tilak (Category 3 faithfulness control)
- `sutrakrit_unified_findings.json` — committed panel results for reproducibility checking

The substrate uses six features (cosine, theme-graph, vocative, substring, lemma-IDF, stem-prefix) with frozen weights `(a=1.0, b=0.01, e_v=0.005, z=0.2, h=0, th=0.01)` fitted on Ramsukhdas's marked cross-references. See Paper 1 Section II.B for full architecture.

### `panel-data/`

Extracted cross-reference triples per commentator, in JSONL format. Each line is a triple `{verse: source, prose: commentary_text}`.

Per-commentator files:
- `commentaries/bg_shankara.jsonl` — Śaṅkara (Advaita)
- `commentaries/bg_ramanuja.jsonl` — Rāmānuja (Viśiṣṭādvaita)
- `commentaries/bg_madhva.jsonl` — Madhva (Dvaita)
- `commentaries/bg_vedantadeshika.jsonl` — Vedantadeshika (Viśiṣṭādvaita-amplification)
- `commentaries/bg_vallabha.jsonl` — Vallabha (Śuddhādvaita-bhakti)
- `commentaries/bg_jayatirtha.jsonl` — Jayatīrtha (Dvaita ṭīkā)
- `commentaries/bg_madhusudan.jsonl` — Madhusūdana Sarasvatī (Advaita-Bhakti synthesis)
- `commentaries/bg_sridhara.jsonl` — Śrīdhara Svāmī (Bhakti-philological)
- `commentaries/bg_anandgiri.jsonl` — Anandagiri (Advaita ṭīkā)

(Ramsukhdas is loaded from the project-awaaz repository's samvad_db ramsukhdas corpus during fitting; the fit produces the frozen weights here.)

### `schema/`

JSON Schema specification for the per-verse object format.

- `per-verse-object.schema.json` — the formal schema definition
- `example-bg-2-55.json` — a complete worked example for BG 2.55 conforming to the schema

The schema is normative: every rendered object in `rendered/` must validate against the schema. Schema-validation is run as part of the test suite (`tests/`).

### `rendered/`

The output of the build pipeline. Per-verse objects, one JSON file per verse, named `bg_X_Y.json` where X is chapter and Y is verse.

Status: build in progress. Approximately 100 of 700 verses currently rendered through the full pipeline. Remaining 600 to follow.

### `web/`

Frontend code for the public-facing site at `gita.ekrasworks.com`. Reads the per-verse objects from `rendered/` and provides the user-facing navigation interface.

Status: not yet started. Planned.

### `scripts/`

Build-pipeline scripts:

- `render_verse.py` — render a single verse's per-verse object
- `render_all.py` — render all 700 verses (orchestrates `render_verse.py`)
- `validate_rendered.py` — schema-validate all objects in `rendered/`
- `build_panel.py` — re-extract panel cross-references from source corpora (used when adding a new commentator)
- `refit_substrate.py` — re-run the substrate's grid-search fit on a chosen anchor corpus

Status: rendering scripts in progress. Validation and panel-build scripts forthcoming.

### `tests/`

Validation tests:

- `test_schema_compliance.py` — every `rendered/*.json` validates against the schema
- `test_substrate_recall.py` — substrate's recall@4 on the panel matches committed expected values (regression test)
- `test_audit_trail_completeness.py` — every claim in every per-verse object has a corpus-provenance entry

### `docs/`

Architecture documentation (this file plus others).

## How to reproduce panel results

```bash
# Install dependencies
pip install -e .

# Re-run panel evaluation
python substrate/sutrakrit_unified_findings.py

# Re-run Tilak faithfulness control
python substrate/tilak_eval.py

# Compare against committed results
diff substrate/sutrakrit_unified_findings.json <(python substrate/sutrakrit_unified_findings.py --output-stdout)
```

The panel re-run takes approximately one hour on a laptop with 8 GB RAM. The Tilak eval takes approximately ten minutes. No proprietary dependencies; no paid API calls.

## How to render a verse

```bash
# Render a single verse
python scripts/render_verse.py --verse 2.55 --output rendered/bg_2_55.json

# Render all 700 verses
python scripts/render_all.py --output-dir rendered/

# Validate all rendered objects against the schema
python scripts/validate_rendered.py rendered/
```

## How to add a new commentator to the panel

```bash
# Extract cross-reference triples from the new commentator's corpus
python scripts/build_panel.py --source path/to/new_commentator.html --output panel-data/commentaries/bg_NEWCOMMENTATOR.jsonl

# Re-run the substrate against the expanded panel
python substrate/sutrakrit_unified_findings.py
```

## How to refit the substrate on a different anchor

```bash
# Refit weights on a different commentator's cross-references
python scripts/refit_substrate.py --anchor panel-data/commentaries/bg_OTHER_ANCHOR.jsonl --output substrate/refitted_weights.json

# Re-run the panel with the refitted weights
python substrate/sutrakrit_unified_findings.py --weights substrate/refitted_weights.json
```

The methodology welcomes alternative anchoring choices; this is one of the open empirical questions Paper 3 names (Falsification 4).

## License and reproducibility

Code is MIT-licensed (`LICENSE`). Per-verse rendered objects and panel data are CC-BY 4.0 (`LICENSE-DATA`). Anyone with this repository can reproduce every panel result, refit the substrate, render their own variant edition, and publish the variant under appropriate attribution.

## Citations

If using this work, cite the three companion research papers (forthcoming). Citation format will be finalized when papers are formally published; canonical citation strings will appear here.
