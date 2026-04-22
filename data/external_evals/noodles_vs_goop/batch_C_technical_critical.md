# Batch C — Technical & Critical — External LLM Evaluations

**Date:** 2026-04-22
**Domains tested:** Medical specialty diagnostic reasoning · Critical-edition philology · Security threat-modeling
**Engines:** Perplexity (long-form, citation-dense) + Grok (concise, named-tool-rich)
**Raw files:** `raw/batch-C-perplexity.md`, `raw/batch-C-grok.md`

---

## CROSS-ENGINE SCORE TABLE

| Domain | Polysemy density | Witness tradition | Substrate-fit (Perplexity) | Substrate-fit (Grok) | Convergent? |
|---|---|---|---:|---:|:---:|
| Medical specialty diagnostic reasoning | fractal (both) | institutionalized (both) | 9/10 | 9/10 | ✓ |
| Critical-edition philology | fractal (both) | institutionalized (both) | 10/10 | 9/10 | ✓ |
| Security threat-modeling | high→borderline-fractal (Perplexity), fractal (Grok) | curated (Perplexity), institutionalized (Grok) | 8/10 | 8/10 | ✓ |

All three domains: both engines converge on substrate-fit ranking and reach within 1 point of each other on every domain. Convergent rate so far across Batches A+B+C = 9 of 9 domains.

---

## DOMAIN 1 — Medical specialty diagnostic reasoning

**Convergent finding:** Same symptom cluster (chronic fatigue, weight loss, neuropathic pain) is interpreted differently by ER, internal medicine, psychiatry, and oncology, with each specialty's "canonical" differential diagnosis bounded by training, setting, and risk tolerance. Both engines call this fractal. Both call the witness tradition institutionalized (CPGs, GRADE evidence grading, specialty journals, Tax Court-equivalent evolving standards).

**Specific tools both engines named:**
- Google DeepMind AMIE (Articulate Medical Intelligence Explorer) — diagnostic dialogue LLM
- LLM clinical decision support (CDS) projects integrating CPGs via Binary Decision Trees + Chain-of-Thought
- 2025 Nature npj Digital Medicine eval on MIMIC-IV-ED (2000 real ED cases, RAG-assisted Claude 3.5 Sonnet)
- Editorials in iMedical promoting LLM-as-CDS layer
- Epic / Microsoft / Truveta clinical-AI products (Grok)

**Concrete harm vector (both engines, same insight):** A CDS LLM tuned on emergency or internal-medicine datasets overweights acute organic causes and systematically under-represents psychiatric, functional, or palliative framings. The output is fluent and guideline-sounding, drives "evidence-based" over-testing or missed psychiatric referrals, but the divergent specialty framings — which would have surfaced the right workup — are erased from the synthesis layer.

**Falsifiable prediction (Perplexity):** By 2030, hospitals deploying LLM-CDS primarily tuned on general internal-medicine/ED data will show statistically detectable shift in workup patterns for "multi-specialty" complaints toward more homogeneous testing/treatment profiles — without corresponding improvement in 30–90 day mortality. Measurable in post-deployment audits.

**Substrate-fit (both 9/10):** A polysemy-preserving substrate that stores per-specialty guideline graphs, points to lineage (guideline version, dissenting editorials, local protocol overrides), and renders per-tradition diagnostic workflows side-by-side would directly serve the specialty disagreement that LLM-CDS currently flattens.

---

## DOMAIN 2 — Critical-edition philology (NT, classical, Sanskrit)

**Convergent finding (both engines, both fractal):** Critical editions of NT, Greek/Latin classics, and Sanskrit texts are built on layered bounded ambiguity. Each lemma carries variant readings + competing conjectures. The critical apparatus (NA28, UBS for NT; sigla and stemmata for classical and Sanskrit) IS the institutionalized witness tradition.

**Specific tools both named:**
- AI Critical New Testament (AICNT) — markets itself as preserving 7000+ documented variants while producing "neutral English" — the engines call this out as flattening the polyphony
- 2025 PLOS ONE Duke/Reichman/Tel Aviv stylometric AI for biblical authorship segmentation — produces reproducible-but-flattening attributions
- Hal-Inria / ACM "Critical Edition of Sanskrit Texts" — algorithmic distance metrics + alignment for collation, introducing algorithmic preferences into contested editorial judgment
- Sanskrit NLP IR collections optimized for retrieval, normalize away morphological/orthographic richness underwriting traditional ambiguity

**Substrate-fit (Perplexity 10/10, Grok 9/10):** Critical-edition philology is the highest-rated substrate-fit domain in the entire eval set. Reason both engines give: the apparatus IS the substrate already; the field has institutionalized the polysemy-preservation move for two centuries; AI is the disruption, not the foundation.

**The Sūtrakṛt v1.0 paper claim this validates:** Sūtrakṛt is the operationalization of what critical-edition philology has been doing in print for 200 years. We're not inventing the methodology — we're computing it.

---

## DOMAIN 3 — Security threat-modeling (code patterns vs threat models)

**Convergent finding:** The same code pattern (e.g., string concatenation in SQL query construction, prototype pollution, deserialization of untrusted input) means radically different things depending on threat model: web-app vs embedded firmware vs supply-chain vs nation-state. Both engines call this fractal/borderline.

**Witness tradition split (interesting divergence):**
- Perplexity calls it **curated** — CWE/CVE database, OWASP, MITRE ATT&CK, but no formal adjudication of which threat model "wins" for a given pattern
- Grok calls it **institutionalized** — same artifacts but treats CVE/MITRE as institutional witness layer

**Specific tools both named:**
- GitHub Copilot security suggestions
- Snyk DeepCode AI
- Veracode AI-assisted SAST
- Google's OSS-Fuzz with LLM mutation scheduling
- Microsoft Security Copilot
- SemGrep AI rules

**Concrete harm vector (both engines):** AI vulnerability scanner trained on web-app threat models flags string-concat-in-SQL as critical SQLi, missing that in the embedded-firmware context the same pattern carries a memory-safety concern (buffer-underrun) that the web-app trained model has no signal for. Or: misses chain-attacks where each step is benign in its own threat model but the composition is the actual exploit (the supply-chain threat model is *defined* by emergent multi-component composition).

**Substrate-fit (both 8/10):** A polysemy-preserving substrate that tags each code pattern with its threat-model-specific reading + audit trail back to which CVE class it has historically participated in across each threat-model tradition would address the cross-model misclassification harm vector. One point deducted by both engines because the threat-model traditions are less formally codified than legal jurisdictions or religious schools.

---

## HEADLINE TAKEAWAYS FOR v1.0 PAPER §6

1. **Critical-edition philology = highest substrate-fit of any domain in the entire eval (10/10 + 9/10).** Use as the paper's "this isn't new methodology, it's old methodology computed" anchor.

2. **Medical CDS is the active-harm domain in this batch.** Both engines independently built the same harm vector (specialty-flattening) and the same falsifiable prediction (workup-pattern homogenization without mortality improvement). This is publishable evidence on its own.

3. **Security threat-modeling reveals a witness-tradition typology gap.** Perplexity sees the threat-model traditions as curated (no formal cross-model adjudication body); Grok sees them as institutionalized via CVE/MITRE. Both right; the disagreement is itself a signal that "witness tradition" is multi-dimensional. Bank as a §3 methodology subtlety: the framework needs to distinguish *normative-jurisdictional* witness traditions (law, religion) from *empirical-evidentiary* ones (security CVEs, medical CPGs).

4. **9-of-9 cross-engine convergence after Batches A+B+C.** The framework is recoverable from independent engines on independent domains. This is the recoverability-evidence claim for the paper.
