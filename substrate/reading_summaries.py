"""Reading-summary extraction per school.

Given a school's commentary prose on a Bhagavad Gītā verse, produce a
2-3 sentence English summary of how that school reads the verse. The
summary populates doctrinal_projections.{school}.reading_summary.

Architectural commitment: the LLM is constrained to summarize what the
commentary text says — not to interpret beyond it. The prompt
explicitly forbids hallucination (claims the commentary does not
support) and explicitly forbids translator-vector collapse (recasting
the school's reading through a non-school lens). Failures of either
constraint should be flagged in audit; the output should be a faithful
distillation, not a re-interpretation.

All credentials are read from environment variables at request time;
no credentials are stored in this file. Two providers supported via
the LLM_PROVIDER env var: 'openrouter' (default; routes to Claude /
GPT / Gemini / Llama / etc.) or 'groq' (fast open-weights inference).
Model identifier is configurable via LLM_MODEL env var.

Resume-on-restart: writes summaries incrementally to a disk cache so
re-runs skip pairs already summarized.
"""

from __future__ import annotations

import json
import os
import time
import urllib.request
import urllib.error
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CACHE_PATH = REPO_ROOT / "data" / "reading_summaries.cache.json"

PROVIDER_URLS = {
    "openrouter": "https://openrouter.ai/api/v1/chat/completions",
    "groq": "https://api.groq.com/openai/v1/chat/completions",
}

PROVIDER_ENV_VARS = {
    "openrouter": "OPENROUTER_API_KEY",
    "groq": "GROQ_API_KEY",
}

# Default model per provider. Override with LLM_MODEL env var or `model` kwarg.
DEFAULT_MODELS = {
    "openrouter": "anthropic/claude-sonnet-4.5",
    "groq": "openai/gpt-oss-120b",
}

SYSTEM_PROMPT = """You are a careful translator of classical Sanskrit \
philosophical commentary. Your task is to summarize, in 2-3 plain \
English sentences, how a specific school's commentary on a specific \
Bhagavad Gītā verse reads that verse. Constraints (in order of \
priority):

1. FAITHFULNESS. Stay strictly within what the commentary text says. \
Do not introduce claims the commentary does not support. Do not \
generalize beyond the commentary's specific reading of this specific \
verse.

2. SCHOOL VOICE. The summary should reflect this school's actual \
metaphysical and interpretive commitments — not a generic ecumenical \
reading. If the school is Advaita, the reading should be Advaita. If \
Viśiṣṭādvaita, it should be Viśiṣṭādvaita. Do not collapse to a \
common-denominator reading.

3. PLAIN ENGLISH. The summary is for a global readership that may not \
have Sanskrit training. Use Sanskrit technical terms where needed but \
gloss them briefly. Do not use unexplained jargon.

4. BRIEF. 2-3 sentences. No more.

Output ONLY the summary text, no preamble, no markdown, no quotation \
marks around it."""


SCHOOL_LABELS = {
    "advaita": "Advaita Vedānta (non-dualist)",
    "viśiṣṭādvaita": "Viśiṣṭādvaita Vedānta (qualified non-dualist, devotional realism)",
    "dvaita": "Dvaita Vedānta (dualist, soul-Lord-distinction)",
    "śuddhādvaita": "Śuddhādvaita (pure non-dualism, devotional)",
    "bhakti": "Bhakti-philological (devotional with philosophical balance)",
    "advaita-bhakti": "Advaita-Bhakti synthesis (Madhusūdana's framework)",
}


def _load_cache() -> dict:
    if CACHE_PATH.exists():
        return json.loads(CACHE_PATH.read_text())
    return {}


def _save_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(
        json.dumps(cache, ensure_ascii=False, indent=2, sort_keys=True)
    )


def _cache_key(verse_id: str, school: str, model: str) -> str:
    return f"{verse_id}::{school}::{model}"


def _resolve_provider() -> str:
    return os.environ.get("LLM_PROVIDER", "openrouter").lower()


def _call_llm(prompt_user: str, model: str, max_retries: int = 3) -> str:
    """POST to the configured provider's chat-completions endpoint.

    Provider is selected via LLM_PROVIDER env var; credentials via the
    provider-specific env var (read at call time, never persisted).
    """
    provider = _resolve_provider()
    if provider not in PROVIDER_URLS:
        raise RuntimeError(f"Unknown LLM_PROVIDER: {provider}")
    url = PROVIDER_URLS[provider]
    api_key = os.environ.get(PROVIDER_ENV_VARS[provider])
    if not api_key:
        raise RuntimeError(
            f"{PROVIDER_ENV_VARS[provider]} env var not set for provider={provider}"
        )

    body = {
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt_user},
        ],
        "max_tokens": 220,
        "temperature": 0.2,
    }
    payload = json.dumps(body).encode("utf-8")

    last_error = None
    for attempt in range(max_retries):
        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "curl/8.0",  # avoid edge UA-block on Groq
        }
        if provider == "openrouter":
            # OpenRouter requires HTTP-Referer + X-Title for proper attribution
            headers["HTTP-Referer"] = "https://github.com/ekras-doloop/sutrakrit-gita"
            headers["X-Title"] = "Sutrakrit-Gita substrate-rendered edition"

        req = urllib.request.Request(url, data=payload, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=90) as resp:
                data = json.loads(resp.read())
            return data["choices"][0]["message"]["content"].strip()
        except urllib.error.HTTPError as e:
            err_body = e.read().decode()[:300]
            last_error = f"HTTP {e.code}: {err_body}"
            if e.code == 429:
                time.sleep(2 ** attempt)
                continue
            if e.code >= 500:
                time.sleep(1 + attempt)
                continue
            raise RuntimeError(last_error)
        except (urllib.error.URLError, TimeoutError) as e:
            last_error = str(e)
            time.sleep(1 + attempt)

    raise RuntimeError(
        f"LLM call failed after {max_retries} attempts: {last_error}"
    )


def summarize_school_reading(
    verse_id: str,
    school: str,
    verse_devanagari: str,
    commentary_prose: str,
    use_cache: bool = True,
    model: str | None = None,
) -> str:
    """Produce a 2-3 sentence English summary of how the school reads the verse.

    Returns the summary string. Cached on disk by (verse_id, school, model)
    so re-runs skip already-summarized pairs and so different model
    runs are kept separately for comparison.
    """
    if not commentary_prose:
        return ""

    provider = _resolve_provider()
    chosen_model = model or os.environ.get("LLM_MODEL", DEFAULT_MODELS[provider])

    cache = _load_cache()
    key = _cache_key(verse_id, school, chosen_model)
    if use_cache and key in cache:
        return cache[key]

    school_label = SCHOOL_LABELS.get(school, school)
    commentary_trimmed = commentary_prose[:3500]

    user_msg = f"""Bhagavad Gītā verse {verse_id}:
{verse_devanagari}

The {school_label} commentary on this verse (in Sanskrit Devanāgarī):
{commentary_trimmed}

Summarize in 2-3 plain English sentences how the {school_label} school \
reads this verse, faithful to the commentary above."""

    summary = _call_llm(user_msg, model=chosen_model)
    cache[key] = summary
    _save_cache(cache)
    return summary
