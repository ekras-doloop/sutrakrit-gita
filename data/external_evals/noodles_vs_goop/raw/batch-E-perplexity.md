# Batch E — Negative control (engineered-monosemous texts) — Perplexity response

Source: https://www.perplexity.ai/search/the-framing-noodles-vs-goop-cr-5GTW7LKAQlSd6UY8YtHUFQ
Captured: 2026-04-22

Test purpose: run the same seven-criterion rubric on three texts designed for monosemy (or thought to be) to see whether the diagnostic correctly titrates downward on non-polysemic domains.

---

Perplexity's opening summary: "RFC 9110, 1040 instructions, and ISO 8601 all look 'structured and precise,' but they each lean on different kinds of engineered ambiguity; current ML tooling mostly treats them as tomato soup when at least two of them are bolognese."

## DOMAIN 1 — RFC 9110 (HTTP Semantics)

**1. Polysemy density: HIGH (nearly fractal once you include intermediaries and deployment idioms)**
Many core terms are deliberately multi-load-bearing: "representation," "resource," "message," "field," "safe," "idempotent," "cacheable" are defined once but have different operational consequences depending on method, status code, intermediaries, and HTTP version.
"Representation" in RFC 9110 §8 is a specific mapping of a resource at a point in time, but participates differently in conditional requests (§13), content negotiation (§12), and caching (§4–§6); the single word pins together multiple behavioral regimes.
"Safe" and "idempotent" in §9.2–§9.3 are prototypical bounded polysemy: safety is defined as no semantic state change on the "origin server" from the perspective of "intended semantics," yet in practice GET is routinely used for state-changing operations (tracking pixels, CSRF), with the spec relying on this tension to support caching and link prefetching.

**2. Witness tradition: CURATED / INSTITUTIONALIZED**
Formal errata and update chain: RFC 9110 (2022) consolidates and obsoletes the earlier RFC 7230–7235 series and references related specs (RFC 9111 Caching, 9112 HTTP/1.1, 9113/9114 HTTP/2 and HTTP/3).
Witnesses include IETF HTTP Working Group issues on GitHub and datatracker; security research like "HTTP Request Smuggling – RFC 9110 style" showing practical divergence between compliant interpretations around multiple Content-Length or Transfer-Encoding headers; tutorial and commentary sites (ARC-IT, "Build Your Own Web Server").

**3. Current ML treatment**
- API-spec RAG and doc assistants: LangChain, Meilisearch, FAISS-based RAG patterns ingest HTTP specs as dense embeddings and surface chunks for "explain this header" or "generate server code."
- Standards-aware code generation: LLM assistants asked to "implement RFC 9110-compliant parsing" or "fix request smuggling issues."
- General RAG frameworks (Qwak, lakeFS) promote treating technical standards as vector-store content and relying on similarity search plus summarization to answer protocol questions, without explicit handling of spec-layer polysemy.
- In practice: RFC 9110 is being chunked, embedded, and summarized as if it were monosemous reference prose.

**4. Cooking test verdict: YES**
A careful HTTP implementer will notice that summarization tends to collapse "MUST," "SHOULD," and "MAY" distinctions, weaken subtle cache invalidation rules, and miss adversarial interaction patterns (duplicate header semantics, ambiguous message length). Dense embeddings treat the spec as tomato soup, but HTTP semantics are closer to bolognese, where the spatial arrangement of conditions and cross-references is doing real work.

**5. Concrete harm vector**
LLM-driven "RFC 9110-compliant" server code that accepts multiple Content-Length headers and silently uses the last one, ignoring the spec's guidance on message framing; or treats all 3xx status codes as cacheable redirects by default, missing subtle distinctions (302 vs 307/308). In practice this yields HTTP request smuggling vulnerabilities or cache poisoning that pass naïve tests but fail under attacker-crafted edge cases.

**6. Falsifiable prediction (3–5 years)**
By 2029, at least one published security paper or major CVE will explicitly trace an exploitable HTTP vulnerability to LLM- or RAG-generated code that "followed" RFC 9110 but mis-handled message framing or header precedence due to misunderstanding ambiguous cases (multiple Content-Length, Transfer-Encoding + Content-Length, or downgrade/upgrade semantics).

**7. Substrate-fit score: 8/10**
The spec already lives in a linked, versioned ecosystem, so this architecture is natural. Gap is socio-technical: HTTP implementers are used to monolithic text; per-tradition multiplexing would be a big but plausible shift.

## DOMAIN 2 — IRS Form 1040 Instructions

**1. Polysemy density: FRACTAL**
Instructions sit atop a layered legal regime: Title 26 statutes, regulations, revenue rulings, court cases, and IRS Publication 17, each using overlapping but not identical terms ("dependent," "qualifying child," "earned income," "adjusted gross income"). "Main home was in the United States" in Pub 17 and 1040 instructions has different consequences depending on credits and provisions; it sounds plain but is load-bearing for EITC, new "no tax on tips" deductions in the 2025 updates. Same line on Form 1040 is interpreted differently across taxpayer profiles (self-employed vs W-2, nonresident vs resident, with/without dependents), producing a fractal polysemy.

**2. Witness tradition: INSTITUTIONALIZED**
Annual revisions of Form 1040 instructions and Publication 17; revenue rulings, notices, Chief Counsel Advice memoranda; Tax Court and appellate decisions acting as external witnesses on ambiguous wording; professional commentary (AICPA, large tax firms, EA/CPA guides) providing line-by-line interpretive glosses. Research on software maintenance highlights explicit "update-from-last-year" workflows, where developers compare prior-year code to current IRS publications.

**3. Current ML treatment**
- Column Tax's "Iris" — AI tax development agent that "understand[s] tax law, turn[s] it into software code, and test[s] itself."
- Academic work on "Maintaining Tax Prep Software with Large Language Models" using LLMs to ingest IRS publications and update software when law changes.
- Ikukuyeva's analysis of "magic" LLMs and IRS penalties on processing 2024 Form 1040's 140 user-fillable fields.
- Consumer tools like TaxGPT as AI assistants for tax professionals preparing Form 1040.
- Common pattern: Form instructions and Publication 17 ingested as embeddings, with RAG answering "What goes on line X?" as if the texts are expository, not a front-end to a doctrinal lattice.

**4. Cooking test verdict: YES**
Summarization tends to flatten edge-case eligibility conditions, drop non-obvious cross-references (e.g., "See Pub. 596" for EITC), and mis-handle terms like "household income" vs "modified adjusted gross income" defined across different pubs and sections. Dense embedding + summarization treats instructions as tomato soup how-to prose; they are bolognese where references to other publications, examples, and exceptions form the interpretive weave.

**5. Concrete harm vector**
LLM-based assistant that correctly extracts values from a scanned Form 1040 (field-level) but misinterprets whether the taxpayer qualifies for a new 2025 deduction ("no tax on tips," new Schedule 1-A) because it compresses multi-part conditions into a simple heuristic. Returns accepted by e-file schema but later adjusted by the IRS, or worse, audited.

**6. Falsifiable prediction (3–5 years)**
By 2029, at least one IRS or TIGTA report or prominent investigative article documenting systemic mis-reporting patterns tied to consumer-facing AI tax assistants or LLM-backed tax prep workflows, explicitly involving misinterpretation of Form 1040 instructions or related pubs (incorrect credits or deductions). Corresponding litigation indicating "reliance on AI tools" did not excuse penalties.

**7. Substrate-fit score: 9/10**
The field already works like a polysemous, witness-heavy system. Main challenge is encoding complex cross-document constraints and confidentiality concerns, not conceptual fit.

## DOMAIN 3 — ISO 8601 (Date and Time)

**1. Polysemy density: MEDIUM (with some engineered ambiguity)**
ISO 8601 looks monosemous (YYYY-MM-DD, hh:mm:ss) but intentionally leaves some interpretive questions open:
- NASA/FITS summary notes that ISO 8601 does not specify whether a time like "09:00" denotes an instant or a period (end of the ninth hour vs an interval), requiring separate agreement among users.
- Week dates, ordinal dates, and calendar dates can all represent "the same" time in different coordinate systems; mapping involves conventions about weeks starting on Monday and existence of week 53.
- Time zone offsets and "Z" UTC designators compress multiple concepts (local time representation vs absolute instant vs wall-clock conventions), producing operational polysemy when systems disagree about what "2023-02-11T01:12:31" should be converted to under local rules.

**2. Witness tradition: THIN / CURATED**
ISO 8601 periodically revised by ISO; commentary relatively sparse compared to law or HTTP. Explanatory sites (IONOS, NASA FITS documentation) as informal commentaries. Developer Q&A (Stack Overflow threads) as a de facto witness tradition documenting edge-case interpretations and library behaviors. No single institutional variant commentary tradition akin to IETF working groups or tax courts, but practical software ecosystems (POSIX, .NET, Java, PostgreSQL) encode conventions.

**3. Current ML treatment**
- DATETIME benchmark targets LLM capabilities in ISO 8601 translation and computation (iso8601.add.day.1.x, natural-language-to-ISO translation).
- Community discussions explicitly note LLMs "don't reliably parse or compare dates" and recommend doing ISO 8601 parsing/normalization in code and only feeding high-level outcomes back to the model.
- LLM-integrated systems rely on external date libraries (Python, JS) for ISO 8601 interpretation, treating the standard as a hard-coded schema rather than a text to be interpreted via embeddings.
- ISO 8601 is often not "RAG'd"; instead treated as a syntactic format with deterministic parsers around the LLM.

**4. Cooking test verdict: BORDERLINE / MOSTLY NO**
For mainstream use (serializing timestamps, basic parsing and arithmetic), breaking the text into embeddings and summarizing does not lose much — libraries embody the semantics, and the ambiguity about whether "09:00" is a point or period is usually irrelevant at that layer. In systems that rely on precise semantics (SLA windows, financial cut-offs, astronomy), the distinction between instant vs interval and issues like leap seconds and end-of-day definitions can matter.

**5. Concrete harm vector**
LLM agents asked to "compute" ISO 8601 date arithmetic in free text (e.g., "if payment is due 30 days after 2023-01-31T00:00:00Z") that occasionally mis-handle month lengths, year boundaries, or DST-like edge cases. Natural-language policy descriptions that gloss over ambiguous interpretations (whether "2026-06-30T24:00:00" is valid or how to interpret "24:00:00" as end of day). Usually caught by deterministic validation, but can mislead non-technical users who trust the natural language explanation.

**6. Falsifiable prediction (3–5 years)**
By 2029, DATETIME benchmark will show persistent, quantifiable error rates in LLM-only ISO 8601 computation tasks relative to rule-based baselines, leading best-practice guidance to strongly recommend external ISO 8601 parsers in high-stakes applications. At least one public incident report attributing a user-facing scheduling or deadline error in an AI assistant to LLM mishandling of ISO 8601 semantics.

**7. Substrate-fit score: 5/10**
For most ISO 8601 use, deterministic parsing already collapses polysemy satisfactorily; overhead of a richer substrate may not pay for itself. In specialized domains with time semantics debates (UTC vs TAI, leap seconds), a witness-aware system could prevent subtle mistakes.

— 45 sources cited by Perplexity
