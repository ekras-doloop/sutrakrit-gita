"""Sūtrakṛt substrate — the core scoring functions and feature
implementations described in Paper 1 Section II.B.

This module exposes a `Substrate` class that loads the BG mūla, the
panel data, and the lists graph; lemmatizes via vidyut-cheda; and
exposes a `score_query(source, query_phrase) -> ranked_candidates`
method that the per-verse renderer calls.

The frozen weights are v2.6 fitted on Ramsukhdas's marked cross-references:
  (a=1.0, b=0.01, e_v=0.005, z=0.2, h=0.0, th=0.01)

These weights MUST NOT be modified for any cross-validation result reported
under the substrate's "frozen weights" claim. Refitting on alternative
anchors is permitted and welcomed (see Paper 3 Section V Falsification 4),
but produces a different substrate variant and must be labeled as such.
"""

from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import numpy as np

REPO_ROOT = Path(__file__).resolve().parents[1]
BG_MULA_PATH = REPO_ROOT / "data" / "bg_mula.json"
LISTS_GRAPH_PATH = REPO_ROOT / "data" / "lists_graph.json"
PANEL_DIR = REPO_ROOT / "panel-data" / "commentaries"
VIDYUT_DATA = "/tmp/vidyut-data"

FROZEN_WEIGHTS = {
    "a": 1.0,    # cosine
    "b": 0.01,   # theme-graph co-membership
    "e_v": 0.005,  # vocative cue
    "z": 0.2,    # substring
    "h": 0.0,    # lemma-IDF overlap
    "th": 0.01,  # stem-prefix overlap
}

DEV_DIGITS = str.maketrans("०१२३४५६७८९", "0123456789")
DEV_LETTER_RE = re.compile(r"[\u0900-\u097F]")


@dataclass
class Candidate:
    """A ranked intertextual candidate for a query phrase."""

    verse: str
    score: float
    feature_breakdown: dict = field(default_factory=dict)
    relationship_type: str = "thematic-similarity"


def _normalize(s: str) -> str:
    s = re.sub(r"[।॥|.,;:!?\(\)\[\]\{\}]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _slp_to_iast(text: str) -> str:
    """Convert SLP1-romanized Sanskrit to IAST."""
    try:
        from vidyut.lipi import Scheme, transliterate

        return transliterate(text, Scheme.Slp1, Scheme.Iast)
    except Exception:
        return text


def _extract_field(text: str, prefix: str) -> str:
    """Extract a field's value from a vidyut PadaEntry repr string."""
    idx = text.find(prefix)
    if idx < 0:
        return ""
    after = text[idx + len(prefix):]
    # Field value typically ends at a comma, paren, or close-bracket
    for end_idx, ch in enumerate(after):
        if ch in (",", ")", "]", " "):
            return after[:end_idx]
    return after.strip()


_PURUSHA_MAP = {
    "Purusha.Prathama": "3rd person",
    "Purusha.Madhyama": "2nd person",
    "Purusha.Uttama": "1st person",
}
_VACANA_MAP = {
    "Vacana.Eka": "singular",
    "Vacana.Dvi": "dual",
    "Vacana.Bahu": "plural",
}
_LAKARA_MAP = {
    "Lakara.Lat": "present indicative",
    "Lakara.Lit": "perfect",
    "Lakara.Lut": "periphrastic future",
    "Lakara.Lrt": "simple future",
    "Lakara.Lot": "imperative",
    "Lakara.Lan": "imperfect",
    "Lakara.VidhiLin": "optative",
    "Lakara.AshirLin": "benedictive",
    "Lakara.Lun": "aorist",
    "Lakara.Lrn": "conditional",
}
_PRAYOGA_MAP = {
    "Prayoga.Kartari": "active",
    "Prayoga.Karmani": "passive",
    "Prayoga.Bhave": "impersonal",
}
_LINGA_MAP = {
    "Linga.Pum": "masculine",
    "Linga.Stri": "feminine",
    "Linga.Napumsaka": "neuter",
}
_VIBHAKTI_MAP = {
    "Vibhakti.Prathama": "nominative",
    "Vibhakti.Dvitiya": "accusative",
    "Vibhakti.Tritiya": "instrumental",
    "Vibhakti.Trtiya": "instrumental",  # vidyut spells without i
    "Vibhakti.Caturthi": "dative",
    "Vibhakti.Panchami": "ablative",
    "Vibhakti.Pancami": "ablative",
    "Vibhakti.Shashthi": "genitive",
    "Vibhakti.Sashthi": "genitive",
    "Vibhakti.Saptami": "locative",
    "Vibhakti.Sambodhana": "vocative",
}


def _humanize_purusha(v: str) -> str:
    return _PURUSHA_MAP.get(v, v)


def _humanize_vacana(v: str) -> str:
    return _VACANA_MAP.get(v, v)


def _humanize_lakara(v: str) -> str:
    return _LAKARA_MAP.get(v, v)


def _humanize_prayoga(v: str) -> str:
    return _PRAYOGA_MAP.get(v, v)


def _humanize_linga(v: str) -> str:
    return _LINGA_MAP.get(v, v)


def _humanize_vibhakti(v: str) -> str:
    return _VIBHAKTI_MAP.get(v, v)


def _substring_score(query: str, candidate: str) -> float:
    q = _normalize(query)
    if not q or not candidate:
        return 0.0
    if q in candidate:
        return 1.0
    for length in range(min(len(q), 30), 5, -1):
        if q[:length] in candidate:
            return length / max(len(q), 1) * 0.7
    return 0.0


class Substrate:
    """The Sūtrakṛt substrate. Lazy-loaded; first instantiation is
    expensive (loads embedding model + lemmatizer + lists graph) but
    subsequent queries are fast.
    """

    def __init__(self, weights: Optional[dict] = None) -> None:
        self.weights = dict(weights or FROZEN_WEIGHTS)
        self._bg: Optional[dict[str, str]] = None
        self._milestones: Optional[list[str]] = None
        self._ms_idx: Optional[dict[str, int]] = None
        self._verse_to_lists: Optional[dict[str, set[str]]] = None
        self._embedding_matrix: Optional[np.ndarray] = None
        self._embedding_model = None
        self._lemma_cache: dict[str, set[str]] = {}
        self._verse_lemmas: Optional[dict[str, set[str]]] = None
        self._lemma_idf: Optional[dict[str, float]] = None
        self._chedaka = None

    # ------------------------------------------------------------------
    # Lazy loaders

    def _load_bg(self) -> None:
        if self._bg is not None:
            return
        self._bg = json.loads(BG_MULA_PATH.read_text())
        self._milestones = sorted(
            self._bg.keys(), key=lambda m: tuple(int(x) for x in m.split("."))
        )
        self._ms_idx = {m: i for i, m in enumerate(self._milestones)}

    def _load_lists_graph(self) -> None:
        if self._verse_to_lists is not None:
            return
        self._load_bg()
        graph_data = json.loads(LISTS_GRAPH_PATH.read_text())
        graph = graph_data.get("lists_graph", graph_data)
        self._verse_to_lists = {v: set() for v in self._milestones}  # type: ignore[union-attr]
        for sutra, list_obj in graph.items():
            for node in list_obj.get("nodes", []):
                v = node.get("verse")
                if v in self._verse_to_lists:
                    self._verse_to_lists[v].add(sutra)

    def _load_embeddings(self) -> None:
        if self._embedding_matrix is not None:
            return
        self._load_bg()
        from sentence_transformers import SentenceTransformer

        self._embedding_model = SentenceTransformer("intfloat/multilingual-e5-base")
        passages = [f"passage: {self._bg[m]}" for m in self._milestones]  # type: ignore[union-attr,index]
        self._embedding_matrix = self._embedding_model.encode(
            passages,
            normalize_embeddings=True,
            batch_size=32,
            convert_to_numpy=True,
        )

    def _get_chedaka(self):
        if self._chedaka is not None:
            return self._chedaka
        from vidyut.cheda import Chedaka

        self._chedaka = Chedaka(VIDYUT_DATA)
        return self._chedaka

    def _lemmatize(self, text: str) -> set[str]:
        if text in self._lemma_cache:
            return self._lemma_cache[text]
        try:
            from vidyut.lipi import Scheme, transliterate

            slp = re.sub(
                r"[\|\.\,\;\:\?]",
                " ",
                transliterate(text, Scheme.Devanagari, Scheme.Slp1),
            ).strip()
            if not slp:
                lemmas: set[str] = set()
            else:
                lemmas = {t.lemma for t in self._get_chedaka().run(slp) if t.lemma}
        except Exception:
            lemmas = set()
        self._lemma_cache[text] = lemmas
        return lemmas

    def tokenize_with_grammar(self, devanagari_text: str) -> list[dict]:
        """Tokenize a verse and return full grammatical info per token.

        Returns a list of dicts:
            [{
              "surface_form": "<surface form in IAST>",
              "lemma": "<lemma in IAST>",
              "grammar": "<human-readable grammatical analysis>",
              "raw_info": "<vidyut PadaEntry repr for audit>",
            }, ...]

        Uses vidyut-cheda to lemmatize and extract per-token grammatical
        metadata (verb tense/person/number, noun case/gender/number, etc.).
        """
        try:
            from vidyut.lipi import Scheme, transliterate
        except Exception:
            return []

        slp = re.sub(
            r"[\|\.\,\;\:\?]",
            " ",
            transliterate(devanagari_text, Scheme.Devanagari, Scheme.Slp1),
        ).strip()
        if not slp:
            return []

        try:
            tokens = self._get_chedaka().run(slp)
        except Exception:
            return []

        out = []
        for tok in tokens:
            grammar = self._format_grammar(tok)
            out.append(
                {
                    "surface_form": _slp_to_iast(tok.text),
                    "lemma": _slp_to_iast(tok.lemma) if tok.lemma else "",
                    "grammar": grammar,
                    "raw_info": str(tok.data) if hasattr(tok, "data") else "",
                }
            )
        return out

    @staticmethod
    def _format_grammar(token) -> str:
        """Produce a human-readable grammar string from a vidyut Token's PadaEntry."""
        try:
            data = token.data
            data_str = str(data)
            # PadaEntry types: Tinanta (verb), Subanta (noun), Avyaya (indeclinable)
            if "Tinanta" in data_str:
                # Extract lakara, purusha, vacana from the repr
                lakara = _extract_field(data_str, "lakara=")
                purusha = _extract_field(data_str, "purusha=")
                vacana = _extract_field(data_str, "vacana=")
                prayoga = _extract_field(data_str, "prayoga=")
                parts = []
                if purusha:
                    parts.append(_humanize_purusha(purusha))
                if vacana:
                    parts.append(_humanize_vacana(vacana))
                if lakara:
                    parts.append(_humanize_lakara(lakara))
                if prayoga:
                    parts.append(_humanize_prayoga(prayoga))
                parts.append("verb")
                return " ".join(parts)
            elif "Subanta" in data_str:
                linga = _extract_field(data_str, "linga=")
                vibhakti = _extract_field(data_str, "vibhakti=")
                vacana = _extract_field(data_str, "vacana=")
                parts = []
                if vibhakti:
                    parts.append(_humanize_vibhakti(vibhakti))
                if vacana:
                    parts.append(_humanize_vacana(vacana))
                if linga:
                    parts.append(_humanize_linga(linga))
                parts.append("noun")
                return " ".join(parts)
            elif "Avyaya" in data_str:
                return "indeclinable"
            else:
                return "(unparsed)"
        except Exception:
            return "(unparsed)"

    def _stem_prefix(self, lemma: str, n: int = 3) -> str:
        if not lemma:
            return ""
        try:
            from vidyut.lipi import Scheme, transliterate

            return transliterate(lemma, Scheme.Slp1, Scheme.Devanagari)[:n]
        except Exception:
            return lemma[:n]

    def _load_lemma_index(self) -> None:
        if self._verse_lemmas is not None:
            return
        self._load_bg()
        self._verse_lemmas = {v: self._lemmatize(self._bg[v]) for v in self._milestones}  # type: ignore[union-attr,index]
        df: Counter = Counter()
        for lems in self._verse_lemmas.values():
            for l in lems:
                df[l] += 1
        n_v = len(self._milestones)  # type: ignore[arg-type]
        self._lemma_idf = {l: float(np.log(n_v / max(df_count, 1))) for l, df_count in df.items()}

    # ------------------------------------------------------------------
    # Public scoring API

    def get_verse(self, verse_id: str) -> str:
        """Return the Devanāgarī text of a BG verse."""
        self._load_bg()
        return self._bg.get(verse_id, "")  # type: ignore[union-attr]

    def all_verses(self) -> list[str]:
        """Return the sorted list of all BG verse identifiers."""
        self._load_bg()
        return list(self._milestones)  # type: ignore[arg-type]

    def theme_lists_for(self, verse_id: str) -> set[str]:
        """Return the set of theme-list memberships for a verse."""
        self._load_lists_graph()
        return self._verse_to_lists.get(verse_id, set())  # type: ignore[union-attr]

    def lists_containing_lemma(
        self, lemma_devanagari: str, verse_id: str
    ) -> list[str]:
        """Return the theme-lists associated with a verse whose phrase-key
        contains the lemma. Used for per-lemma theme-list membership in
        the per-verse object's word_by_word.theme_lists field.
        """
        self._load_lists_graph()
        verse_lists = self._verse_to_lists.get(verse_id, set())  # type: ignore[union-attr]
        if not verse_lists or not lemma_devanagari:
            return []
        return [
            lst for lst in sorted(verse_lists) if lemma_devanagari in lst
        ]

    def other_verses_in_list(self, list_key: str, exclude_verse: str = "") -> list[str]:
        """Return the verses participating in a given theme-list,
        optionally excluding the queried verse itself.
        """
        self._load_lists_graph()
        graph_data = json.loads(LISTS_GRAPH_PATH.read_text())
        graph = graph_data.get("lists_graph", graph_data)
        lst = graph.get(list_key)
        if not lst:
            return []
        return [
            n["verse"]
            for n in lst.get("nodes", [])
            if n.get("verse") and n["verse"] != exclude_verse
        ]

    def score_query(
        self,
        source_verse: str,
        query_phrase: str,
        top_k: int = 8,
    ) -> list[Candidate]:
        """Score a query phrase against all BG verses (excluding the source).

        Returns top_k candidates ranked by composite substrate score, with
        per-feature breakdown for each candidate.
        """
        self._load_bg()
        self._load_lists_graph()
        self._load_embeddings()
        self._load_lemma_index()

        w = self.weights
        query_norm = _normalize(query_phrase)
        source_lists = self.theme_lists_for(source_verse)

        # Compute per-candidate feature contributions
        from sentence_transformers import util  # noqa: F401

        query_emb = self._embedding_model.encode(  # type: ignore[union-attr]
            f"query: {query_phrase}", normalize_embeddings=True, convert_to_numpy=True
        )
        cosine_scores = self._embedding_matrix @ query_emb  # type: ignore[operator]

        query_lemmas = self._lemmatize(query_phrase)
        query_stems = {self._stem_prefix(l) for l in query_lemmas if l}

        scored: list[Candidate] = []
        for i, vid in enumerate(self._milestones):  # type: ignore[arg-type]
            if vid == source_verse:
                continue
            verse_text = self._bg[vid]  # type: ignore[index]
            verse_lists = self._verse_to_lists.get(vid, set())  # type: ignore[union-attr]
            verse_lemmas = self._verse_lemmas[vid]  # type: ignore[index]
            verse_stems = {self._stem_prefix(l) for l in verse_lemmas if l}

            cosine = float(cosine_scores[i])
            theme_overlap = float(len(source_lists & verse_lists))
            substring = _substring_score(query_norm, verse_text)
            lemma_overlap = float(
                sum(
                    self._lemma_idf.get(l, 0.0)  # type: ignore[union-attr]
                    for l in (query_lemmas & verse_lemmas)
                )
            )
            stem_overlap = float(len(query_stems & verse_stems))
            vocative = 0.0  # placeholder; full vocative-pattern detector would expand here

            composite = (
                w["a"] * cosine
                + w["b"] * theme_overlap
                + w["e_v"] * vocative
                + w["z"] * substring
                + w["h"] * lemma_overlap
                + w["th"] * stem_overlap
            )

            scored.append(
                Candidate(
                    verse=vid,
                    score=composite,
                    feature_breakdown={
                        "cosine": round(cosine, 4),
                        "theme_graph": theme_overlap,
                        "vocative": vocative,
                        "substring": round(substring, 4),
                        "lemma_overlap": round(lemma_overlap, 4),
                        "stem_prefix": stem_overlap,
                    },
                )
            )

        scored.sort(key=lambda c: c.score, reverse=True)
        return scored[:top_k]

    # ------------------------------------------------------------------
    # Panel-data accessors

    def panel_files(self) -> dict[str, Path]:
        """Return a dict of commentator-name → JSONL path for the panel."""
        return {
            f.stem.replace("bg_", ""): f for f in sorted(PANEL_DIR.glob("bg_*.jsonl"))
        }

    def panel_commentary_for(self, commentator: str, verse_id: str) -> Optional[str]:
        """Return the commentary prose a given commentator wrote on a given verse,
        or None if the commentator has no entry for that verse.
        """
        path = PANEL_DIR / f"bg_{commentator}.jsonl"
        if not path.exists():
            return None
        with path.open() as f:
            for line in f:
                row = json.loads(line)
                if row.get("verse") == verse_id:
                    return row.get("prose")
        return None
