# Batch E — Negative control (engineered-monosemous texts) — Grok response

Source: https://grok.com/c/76b6a297-5260-4fe7-be3a-5f4df18be0c0
Captured: 2026-04-22
Thought for: 47s
Mode: Expert, 293 sources

Test purpose: run the same seven-criterion rubric on three texts designed for monosemy to see whether the diagnostic correctly titrates downward.

---

## Domain 1: RFC 9110 — IETF HTTP Semantics specification

**Polysemy density: Medium-high**
Bounded multi-meaning is load-bearing in core semantics but held tightly by ABNF grammar, MUST/SHOULD/MAY distinctions, and IANA registries. Examples: §9.3.1 (GET method) states "content received in a GET request has no generally defined semantics, cannot alter the meaning or target of the request"; §9.3.4 (PUT) allows side effects on other resources while remaining idempotent; §5.6.1 list-based fields require ignoring "a reasonable number of empty list elements" to handle sender errors without DoS; §13.2.2 mandates strict precondition evaluation order (If-Match before If-Unmodified-Since) but extensions "ought to define" their own ordering. These create co-existing expert readings (strict vs. defensive parsing, private agreements vs. public semantics) without breaking interoperability.

**Witness tradition: Institutionalized**
IETF httpbis Working Group maintains live discussion; public errata process (e.g., Errata ID 7107 on Content-Length forwarding ambiguity clarified via GitHub issue #1113; Errata ID 7138 on media type qvalue precedence); RFC obsoletes 7230–7235 series with explicit change logs; mailing-list archives and GitHub issues serve as traceable commentary layer.

**Current ML treatment:**
OpenAPI-based LLM function-calling pipelines (OpenAI GPT-4o/5.x tool use, Anthropic Claude function calling, Google Gemini) convert OpenAPI 3.1 specs (which embed RFC 9110 semantics for methods, status codes, headers) into tool schemas; agents.json (wild-card-ai) and Speakeasy Gram translate OpenAPI → LLM-ready contracts; RAG systems in LangChain/LlamaIndex or Gravitee AI workflows ingest API docs derived from RFC 9110; research prototypes like RFCScope (LLM logical-ambiguity detector for RFCs) and PSMBench (LLM extraction of protocol state machines from RFC text) directly process the spec.

**Cooking test verdict: Yes** — dense embedding + summarization collapses the precise MAY/SHOULD distinctions and edge-case notes (e.g., GET body semantics, trailer merging rules in §6.5) into fluent but context-free prose that an implementer would immediately flag as incomplete or insecure.

**Concrete harm vector:**
LLM-generated HTTP client/server code or API documentation (via OpenAPI RAG) silently drops RFC 9110 §5.1.6 forwarding rules or §14.2 Range header rejection logic, producing parsers vulnerable to request smuggling that pass unit tests and "look correct" in normal traffic.

**Falsifiable prediction:**
By 2028–2030, CVE or bug-bounty data will show a statistically measurable increase (≥20% YoY) in HTTP request-smuggling or header-parsing vulnerabilities explicitly attributed to LLM-generated code or docs that reference "RFC 9110 compliance" but fail the exact edge cases listed in verified errata.

**Substrate-fit score: 9/10**
A polysemy-preserving substrate with witness pointers (errata IDs, WG issues) + per-tradition rendering (WG consensus view vs. individual implementer notes) would serve the domain extremely well; only minor deduction for the already-strong IETF tooling.

## Domain 2: IRS Form 1040 Instructions — federal tax-filing guidance for individual taxpayers

**Polysemy density: High / fractal**
Legal language is deliberately bounded by statute, regulations, and cross-references but recurs at every scale. Examples from 2025 i1040gi.pdf: "lived with you for more than half of 2025" (qualifying child, p. 17) with temporary-absence exceptions (school, military, medical, detention); "valid SSN… issued before the due date" for Child Tax Credit (p. 22) with ITIN/ATIN election timing; EITC qualifying-child rules (Step 3) layer age, relationship, residency, and joint-return exceptions; "qualified tips" deduction cap ($25k) with modified AGI phase-outs (Schedule 1-A). Fractal because the same interpretive discipline appears in Pub 501 (dependents), Pub 596 (EITC), revenue rulings, and court precedents.

**Witness tradition: Institutionalized**
IRS revenue rulings/procedures, Treasury regulations, Private Letter Rulings/TAMs, Tax Court memorandum/regular opinions, and post-Loper Bright judicial review create a traceable commentary layer; IRM 4.10.7 explicitly catalogs sources (Code, regs, bulletins, court decisions, PLRs).

**Current ML treatment:**
Perplexity Computer (drafts full Form 1040 + schedules from uploaded docs); H&R Block AI Tax Assist and TurboTax AI chat/Q&A features that ingest 1040 instructions; UiPath Document Understanding ML package for 1040 form extraction; general LLMs (ChatGPT, Claude, Gemini) prompted on i1040gi.pdf/Pub 17 for advice; CPA Pilot AI workflows for automated 1040 prep; academic work (e.g., "Technical Challenges in Maintaining Tax Prep Software" using LLMs to translate IRS publications into executable specs).

**Cooking test verdict: Yes** — averaging discards the layered exceptions and cross-references (e.g., "temporary absence" vs. permanent non-residency, SSN validity election timing) that a careful tax professional or IRS auditor would immediately spot as outcome-determinative.

**Concrete harm vector:**
AI tax-prep tools or LLM chatbots misapply the "lived with you" residency test or EITC SSN rules in edge cases (divorced parents, military families), generating returns that look compliant, pass initial IRS AI screening, but trigger amended-return notices or penalties upon manual review.

**Falsifiable prediction:**
In 2026–2028 tax seasons, IRS data or practitioner surveys will show a measurable rise (≥15% above trend) in amended 1040 returns or CP2000 notices explicitly citing misapplication of 2025 Form 1040 instructions sections on dependents, EITC, or Schedule 1 adjustments traceable to AI-generated filings/advice.

**Substrate-fit score: 8/10**
Excellent fit for witness pointers (rulings, PLRs, Tax Court citations) and per-tradition rendering (IRS view vs. judicial vs. practitioner); slight deduction because tax law changes annually, requiring rapid substrate updates.

## Domain 3: ISO 8601 — international standard for representations of dates and times

**Polysemy density: Low / medium**
Explicitly designed for syntactic unambiguity (YYYY-MM-DD, extended formats); polysemy is limited and mostly in extensions or edge cases: recurring intervals (R/…), durations (P1Y vs. calendar-month interpretation), time-zone handling (local time discouraged but permitted), midnight conventions (24:00 vs. 00:00), partial dates, and ordinal weeks. ISO 8601-2:2019 extensions and 2022 amendment explicitly tried to remove remaining ambiguities.

**Witness tradition: Curated / thin**
ISO TC 154 maintenance with published amendments (2019, 2022); community profiles (RFC 3339, W3C XML Schema, I-JSON) and implementation experience serve as de-facto commentary; no public errata database comparable to IETF.

**Current ML treatment:**
LLMs are routinely prompted/instructed to output strictly ISO 8601 strings for structured data (best-practice in agent/tool-calling pipelines); date-parsing libraries (Python dateutil, Rust chrono, JavaScript Temporal proposal tests) implement varying strictness levels; minimal direct RAG on the standard text itself—focus is on syntactic compliance rather than interpretive layers; no major vendor products treat the ISO document as a primary polysemic source.

**Cooking test verdict: No** — the core formats are purely syntactic and survive blending; subtle distinctions in interval/duration semantics or profile choices survive as long as output validation is used, so a careful standards expert would notice little loss in the primary payload.

**Concrete harm vector:**
LLM code generators produce datetime-handling routines that mishandle ISO 8601-2 recurring intervals or time-zone edge cases (e.g., assuming local time without offset), creating data-exchange bugs that format correctly but produce off-by-one or interoperability failures downstream.

**Falsifiable prediction:**
By 2028–2030, public test-suite runs (e.g., Temporal proposal or ISO 8601 compliance suites) on the top 100 most-starred LLM-generated datetime libraries on GitHub will show a statistically higher non-compliance rate for interval/precision edge cases than hand-written equivalents, measurable via automated validators.

**Substrate-fit score: 6/10**
Moderate fit — syntactic nature reduces need for multi-tradition rendering, but pointers to amendments, profiles (RFC 3339, W3C), and known implementation variances would still add value for audit trails in safety-critical systems.
