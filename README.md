# Sūtrakṛt-Gītā

**The first substrate-rendered edition of the Bhagavad Gītā — airgapped from any single school, doctrine-neutral but doctrine-queryable, preserving bounded polysemy at the mathematical maximum the corpus union supports.**

This repository hosts the build of Distribution 1 of the Open Source Wisdom Operating System (OSWOS): a per-verse navigation instrument over the Bhagavad Gītā that surfaces the work's own internal cross-reference network without imposing any single commentator's reading.

## What this is

Every English translation of the Bhagavad Gītā you have ever read was made by one person committing to one reading. Bhaktivedanta committed to Gauḍīya-Vaiṣṇavism. Easwaran committed to a universal-spiritualist humanism. Sargeant committed to academic philological exposition. They had to commit — that is how books work. The reader picks up an edition and inherits the editor's collapse before the first page is turned.

This edition does not commit. For each of the 700 verses it produces a per-verse object containing:

- **Mūla**: the Sanskrit verse in Devanāgarī and IAST, with chant audio reference, speaker, vocative, chapter position
- **Word-by-word**: each lemma identified, with all senses attested across the panel ranked by panel evidence
- **Intertextual panel**: the top-K BG verses ranked by the Sūtrakṛt substrate, with score decomposed by feature
- **Doctrinal projections**: the Advaita reading, the Viśiṣṭādvaita reading, the Dvaita reading, the Bhakti reading — each surfaced from the panel data, ranked, queryable
- **Prosodic information**: meter, meter-shift signals, pragmatic context
- **Theme-list memberships**: the verse's role in each theme-cluster the substrate identifies
- **Audit trail**: every claim above carries its substrate score and corpus provenance

The reader queries the lens they want. The substrate provides the lens-conditional projection. Or the reader queries no lens and walks the full network.

## Project structure

```
sutrakrit-gita/
├── substrate/        # The Sūtrakṛt substrate code (mE5 + 5 Sanskrit-aware features)
├── panel-data/       # Extracted cross-reference triples per commentator
├── schema/           # Per-verse object JSON Schema specification
├── rendered/         # Per-verse object outputs (the artifact itself)
├── web/              # Frontend code for gita.ekrasworks.com
├── scripts/          # Build pipeline scripts
├── tests/            # Validation tests against the panel
└── docs/             # Architecture documentation
```

## The intellectual foundation

This work rests on three companion research papers (forthcoming):

1. **Sūtrakṛt: A Computational Substrate for Cross-Reference Retrieval Across the Bhagavad Gītā Commentary Tradition** — the empirical substrate validation across an eight-commentator panel
2. **Bounded Polysemy as the Architecture of Long-Lived Texts** — the architectural framework with the four-metric faithfulness evaluation
3. **Convergent Validation in Computational Hermeneutics** — the methodology that escapes authority-based validation's self-reference trap

The papers articulate the methodological commitments under which this edition is built; the edition is the operational instantiation that the methodology licenses. Citations and links will be added to this README upon formal publication of the papers.

## Build status

**As of April 22 2026 (v1.0 substrate-swap complete):**

- [x] Substrate validated on the eight-commentator panel (companion paper Section III) — Ramsukhdas R@4 71.5%, Śaṅkara 71.6% with frozen weights, Vedantadeshika 40.2% at n=629, Tilak (negative control) 38.4%
- [x] Per-verse object schema designed (companion paper Section VI)
- [x] **All 700 verses rendered through the full pipeline** (10,578 tokens), all 6 doctrinal schools × 2 registers (Vyāsa-discipline + Tulsīdās-discipline), intertextual panels, theme-list memberships, audit trail
- [x] **Public-facing web frontend live at [gita.ekrasworks.com](https://gita.ekrasworks.com)** — chapter-by-chapter browse, verse-level six-school panel rendering, so-what questions, everyday applications, compare-mode, click-trails, theme-list walks, lemma-wire view
- [x] **Word-by-word substrate: ByT5-Sanskrit-multitask** (Nehrdich, Hellwig & Keutzer, EMNLP 2024) with full audit-trail provenance. Every verse renders per-token lemma + case/gender/number/tense/mood/person.
- [x] **15-domain × 2-engine cross-framework eval** completed April 22 — Perplexity + Grok converge on substrate-fit rank ordering across Indic / legal / religious / literary / technical / critical domains with ISO 8601 negative control correctly discriminating.
- [ ] Hand-labeled 50-verse gold subset for ≥95% lemma-agreement validation gate (next-session queued)
- [ ] Per-school sense re-extraction on ByT5-quality lemmas (current `senses_attested_in_panel` empty pending re-extraction)
- [ ] Independent reviewer audit by participating Sanskritists (invited)

**Companion papers:** the Sūtrakṛt triptych (Papers 1–3) + Sūtrakṛt-for-Code (Paper 4) + Sūtrakṛt-for-Context-Engineering (Paper 5) are drafted and pending arXiv submission. See the related Pneumae 16-paper research program on the voice-conversation substrate (Rastogi, February–April 2026, Project Respire).

## Reproducibility commitment

Everything in this repo is open source under permissive license. The substrate runs on a laptop with 8 GB RAM in approximately one hour for a full panel re-run. No proprietary dependencies. No paid API calls. Any researcher can byte-for-byte reproduce every panel result, refit the substrate weights on alternative anchors, add new commentator corpora, and produce their own substrate-rendered edition variants.

## License

Code: MIT License (see `LICENSE`). Per-verse rendered objects: CC-BY 4.0 (see `LICENSE-DATA`). Sanskrit primary sources are public domain or critical-edition licensed; provenance documented per source.

## Citation

If you use this work, please cite the three companion research papers (publication forthcoming; citation details will be added here when available).

## Contact

Project lead: Gaurav Rastogi (ekras-doloop on GitHub)
Project repository: https://github.com/ekras-doloop/sutrakrit-gita

जय माँ काली
