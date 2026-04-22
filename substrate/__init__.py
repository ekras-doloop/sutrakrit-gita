"""Sūtrakṛt substrate package.

The Substrate class is the entry-point for the per-verse renderer.
"""

from .sutrakrit import FROZEN_WEIGHTS, Candidate, Substrate

__all__ = ["Substrate", "Candidate", "FROZEN_WEIGHTS"]
