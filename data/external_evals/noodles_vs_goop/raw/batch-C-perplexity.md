# Batch C — Technical & Critical — Perplexity response

Source: https://www.perplexity.ai/search/the-framing-noodles-vs-goop-cr-pjyuGrDdSdKZr3V7Gnr2EA
Captured: 2026-04-22

---

## Domain 1 — Medical specialty diagnostic reasoning

**Polysemy density: fractal**
The same symptom cluster (e.g., chronic fatigue, weight loss, neuropathic pain) is interpreted differently by ER, internal medicine, psychiatry, and oncology, with each specialty's "canonical" differential diagnosis shaped by training, setting, and risk tolerance; LLM-CDS work explicitly notes that performance and reasoning paths vary strongly by clinical task and context. [nature+1]
Guidelines and pathways (e.g., UpToDate-style CPGs, COVID-19 outpatient CPGs) encode bounded ambiguity: multiple acceptable workups and treatments keyed to comorbidities, resource setting, and patient preferences, rather than a single monosemous "correct" decision tree. [hypersense-software+1]

**Witness tradition: institutionalized**
Modern medicine has layered witnesses: primary literature, systematic reviews, clinical practice guidelines (CPGs), consensus statements, and local protocols, each with explicit grading (e.g., GRADE) and documented dissent; recent LLM-CDS papers explicitly talk about "grounding" in trusted guidelines as a distinct layer. [pmc.ncbi.nlm.nih+2]
Specialty disagreements are archived in practice guideline updates, editorial debates, and evolving standards of care (e.g., oncology vs palliative care framing of treatment-resistant pain), creating a traceable commentary tradition akin to juristic or scholastic glosses. [pmc.ncbi.nlm.nih+1]

**Current ML treatment (concrete tools / what they do)**
- Google DeepMind's AMIE (Articulate Medical Intelligence Explorer) is positioned as a diagnostic dialogue LLM that takes patient symptoms/history and proposes diagnoses and management plans, evaluated against clinicians on complex cases. [makebot]
- Multiple groups are building LLM-powered clinical decision support (CDS); a 2024 study integrates CPGs into LLMs via Binary Decision Trees, Program-Aided Graph Construction, and Chain-of-Thought Few-Shot Prompting, essentially compiling guidelines into graph/tree substrates that the LLM traverses. [pmc.ncbi.nlm.nih]
- A 2025 Nature npj Digital Medicine paper evaluates LLM workflows (including RAG-assisted models like Claude 3.5 Sonnet) on 2000 real ED cases (MIMIC-IV-ED), using real-world triage and diagnostic tasks; the LLM is treated as a single summarizing reasoner over notes plus literature, not as a polyphony of specialty voices. [nature]
- Editorials in iMedical and other journals explicitly promote LLMs as CDS layers that combine patient data with "the latest medical literature," emphasizing synthesis and efficiency over preserving competing but legitimate interpretive frames. [sciencedirect+2]

**Cooking test verdict: yes**
Dense-embedding plus summarization workflows that ingest multi-specialty notes, guidelines, and literature to output a single "best practice" plan will erase visible traces of oncology vs psychiatry vs internal medicine framings of the same symptom cluster, even though those framings are clinically load-bearing. [nature+1]

**Concrete harm vector**
Mis-triage of ambiguous chronic symptoms: a CDS LLM trained/evaluated on emergency or internal-medicine datasets (MIMIC-IV-ED, general hospital notes) overweights acute organic causes and systematically under-represents psychiatric, functional, or palliative framings, yet still outputs fluent, guideline-sounding advice; this can drive seemingly "evidence-based" over-testing, missed psychiatric referrals, or delayed cancer workups that only a specialist's divergent framing would have surfaced. [med.stanford+2]

**Falsifiable 3–5 year prediction**
Hospitals that deploy LLM-based CDS primarily tuned on general internal-medicine/ED data will show a statistically detectable shift in workup patterns for "multi-specialty" complaints (chronic fatigue, medically unexplained pain, weight loss) toward more homogeneous testing/treatment profiles and reduced involvement of psychiatry and palliative care, without a corresponding improvement in 30–90 day mortality or readmission; this pattern should appear in post-deployment quality/safety studies or health-system audits. [mednexus+3]

**Substrate-fit score: 9/10**
A polysemy-preserving substrate that: (a) stores per-specialty guideline graphs, (b) points to lineage (guideline version, dissenting editorials, local protocol overrides), and (c) renders per-tradition diagnostic workflows side-by-side would serve this domain extremely well, because the legitimate disagreement and risk-framing between specialties is exactly what current "one best answer" LLM-CDS workflows collapse. [hypersense-software+2]

## Domain 2 — Critical-edition philology (NT, classical, Sanskrit)

**Polysemy density: fractal**
Critical editions of the New Testament, Greek/Latin classics, and Sanskrit texts are built on layered bounded ambiguity: each lemma carries variant readings, orthographic variants, and competing conjectures, with apparatus symbols encoding degrees and kinds of disagreement. [aicnt+3]
Polysemy is load-bearing both in the base language (e.g., Sanskrit words with several context-dependent meanings) and in the scholarly reasoning (different stemmata, local vs Alexandrian text families, competing editorial principles), making the "texture" itself the argument. [fid4sa-repository.ub.uni-heidelberg+2]

**Witness tradition: institutionalized**
The critical apparatus IS the witness tradition: manuscripts, versions, and patristic citations are encoded as sigla, with variant readings and editorial decisions recorded line by line; NT editions (NA28, UBS), Sanskrit and classical Greek/Latin critical editions all institutionalize this. [inria.hal+2]
AI-driven projects like the AI Critical New Testament (AICNT) explicitly market themselves as leveraging AI while preserving a critical apparatus of over 7000 documented variants and aligning with early Greek manuscripts, thus formalizing the witness tradition in a digital/AI-aware way. [aicnt+1]

**Current ML treatment (concrete tools / what they do)**
- The AI Critical New Testament (AICNT) uses AI to produce a "neutral English rendering" from Greek while documenting textual variants, claiming to minimize human interpretive bias; AI is part of the translation and collation pipeline, but the output is a smoothed English text plus apparatus, not a polyphony of possible theological or philological readings. [aicnt+1]
- A 2025 PLOS ONE-reported project by teams at Duke, Reichman, Tel Aviv, Collège de France, and others uses AI (stylometric word-frequency analysis and clustering) to identify "linguistic fingerprints" and segment biblical texts by probable authorship, providing reproducible but flattening attributions that can override nuanced traditional debates about strata and redaction. [bigdata.duke]
- Work on computer-assisted critical editions of Sanskrit (e.g., Hal-Inria / ACM-published "Critical Edition of Sanskrit Texts") uses computational distance metrics between manuscript versions and alignment algorithms to support collation and stemmatic reasoning, introducing algorithmic preferences into what had been explicitly contested editorial judgment. [acm+1]
- In a broader Sanskrit NLP space, projects build IR collections and stemmers optimized for retrieval performance, which tend to normalize or strip morphological/orthographic richness that often underwrites traditional semantic ambiguity. [sciencedirect]

**Cooking test verdict: yes**
Treating a corpus of variant-laden texts as chunks to be embedded, clustered, and summarized into a single "best" reading or author-segmentation will erase precisely the bounded interpretive tension that makes a critical edition valuable to expert readers; it turns a bolognese of witnesses and conjectures into a tomato-soup synopsis. [bigdata.duke+3]

**Concrete harm vector**
False manuscript filiation / misleading authority weighting: AI-based collation and authorship tools that rely on distance metrics and stylometry can produce confident-looking stemmata or author attributions that underweight codicological constraints, localized scribal habits, and genre-driven variation; such outputs can be taken up by non-specialists or even publishers as "objective" and feed into Bible translations, classical text editions, or Sanskrit commentarial work that silently privileges one line of reconstruction while appearing rigorously scientific. [inria.hal+2]

**Falsifiable 3–5 year prediction**
Within 3–5 years, at least one AI-assisted critical edition or major translation project (biblical, classical, or Sanskrit) that leans heavily on automated collation/attribution will face formal scholarly correction: a significant portion of its stemma or key textual decisions will be revised in peer-reviewed responses or second editions on grounds that the underlying AI metrics misrepresented witness relationships or suppressed viable alternative readings; this will be visible in journal reviews, published rebuttals, or documented errata. [acm+3]

**Substrate-fit score: 10/10**
This domain is almost a perfect match for a substrate that treats each witness, variant, and editorial principle as first-class, with pointers to manuscript sigla, parallel traditions, and per-school renderings (e.g., Byzantine-leaning vs Alexandrian-leaning base text, different Sanskrit sampradāya readings), and allows readers or downstream tools to navigate the bounded polysemy rather than averaging it away. [aicnt+3]

## Domain 3 — Security threat-modeling (code patterns vs threat models)

**Polysemy density: high (borderline fractal)**
A single code pattern (say, dynamic string concatenation in SQL, debug backdoor in firmware, or lenient deserialization) carries different security semantics under different threat models: in an internal tool, it might be low risk; in a public web app with untrusted inputs, it's critical; in firmware or supply chain, the same pattern could signify a planted backdoor. [openssf+2]
Supply-chain security guidance from OpenSSF and others treats the same artifact (e.g., a dependency choice, build script, or signing configuration) differently depending on whether the adversary is a casual attacker, a criminal group, or a nation-state, formalizing multiple overlapping but bounded threat framings. [best.openssf+2]

**Witness tradition: curated**
The "witnesses" in security are CVEs, advisories, threat models, incident postmortems, and framework docs (OWASP, SLSA, OpenSSF), which record how specific patterns were exploited under particular conditions; these create a curated but incomplete commentary tradition. [finitestate+2]
Security incident reports and vendor blogs (e.g., Finite State on firmware backdoors, Codacy on supply chain vulnerabilities) explicitly document how the same code or configuration behaved differently under different deployment contexts, adding to the interpretive record. [codacy+1]

**Current ML treatment (concrete tools / what they do)**
- GitHub's CodeQL + Copilot "code scanning autofix" pipes SAST findings into Copilot, which generates "contextualized" vulnerability explanations and fixes based on the code snippet and a generic vulnerability description, effectively summarizing a large code+rules corpus into a single recommendation. [github]
- Open-source projects like SunWeb3Sec/llm-sast-scanner expose "LLM SAST" skills that let LLM-based coding agents analyze code for vulnerabilities, typically by summarizing patterns in local snippets against generic vulnerability taxonomies, not by reasoning through full deployment and threat models. [github]
- Security blogs report that AI-assisted SASTs and AI "security engineers" (e.g., ZeroPath) combine LLM queries with regex/grep, SAST, and dependency checks to find bugs and answer "is my code affected by CVE-XYZ?", again synthesizing highly context-specific vulnerability semantics into a single yes/no or patch recommendation. [appsecsanta+1]
- In firmware and supply-chain security, platforms like Finite State emphasize combining source code scanning with binary analysis to catch issues like build-time backdoors and third-party library risks, but much of the marketing and analytics layer still converges on single severity ratings per finding that mask underlying conditionality. [finitestate+1]

**Cooking test verdict: yes**
Dense embeddings and summarization that aim to map "similar vulnerability patterns" or produce unified advice ("fix this like that CVE") will actively crush the fact that the same code pattern could be benign, exploitable, or indicative of a nation-state backdoor depending on asset criticality, exposure, and supply-chain posture; an expert threat modeler would absolutely notice the loss. [github+3]

**Concrete harm vector**
Missed or misclassified CVE class under different threat models: an LLM-augmented SAST or "AI security engineer" trained on web-app centric patterns flags SQL injection and XSS but downplays or normalizes firmware backdoor patterns or build-pipeline manipulations, because in its averaged training data such patterns often belong to low-risk internal tooling; the generated report is coherent, references OWASP-like categories, and looks professional, so teams ship firmware or supply-chain configurations that a specialized analyst would treat as high-risk. [joshua+3]

**Falsifiable 3–5 year prediction**
Within 3–5 years, at least one major publicly analyzed incident will show that an organization using AI-augmented SAST or AI "security engineer" tooling passed code or build configs as "low risk," while a subsequent compromise (likely supply-chain or firmware) exploited patterns that those tools systematically underweighted; post-mortem reports or vendor retrospectives will explicitly mention AI/SAST advice as a contributing blind spot, analogous to how today's reports call out "accepted risk" based on earlier tool outputs. [appsecsanta+4]

**Substrate-fit score: 8/10**
A substrate that keeps each code pattern tied to multiple threat models, deployment contexts, and real-world incident witnesses (CVE, CSIRT report, vendor advisory), and renders per-threat-model interpretations side-by-side ("web app public," "internal service," "firmware in field," "nation-state adversary"), would significantly reduce harmful averaging; it would still need careful curation to avoid overwhelming practitioners, but it aligns well with how mature threat modeling already works. [openssf+3]

— 45 sources cited by Perplexity
