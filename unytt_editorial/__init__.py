"""Shared editorial constitution for unytt newsroom tools.

Universal newsroom rules that apply whether a tool *writes* copy (kladd) or
*reviews* it (kaia). Each tool composes these framing-neutral blocks with its
own role and task-specific instructions, so the shared standards stay in one
place instead of drifting between products.

The rule prose lives in ``constitution.md`` so it can be edited as one
document; this module parses it into named blocks by their comment markers.
Public names are unchanged.
"""

from __future__ import annotations

import re
from pathlib import Path

_SOURCE = Path(__file__).parent / "constitution.md"
# Each block is preceded by an HTML-comment marker holding its machine name.
_MARKER = re.compile(r"^<!--\s*(\w+)\s*-->$", re.MULTILINE)


def _load_blocks() -> dict[str, str]:
    """Parse constitution.md into {NAME: block} keyed by each block's marker."""
    parts = _MARKER.split(_SOURCE.read_text(encoding="utf-8"))
    # re.split with one capture group → [preamble, name, body, name, body, ...]
    return {parts[i]: parts[i + 1].strip() for i in range(1, len(parts), 2)}


_BLOCKS = _load_blocks()

KILDETROSKAP = _BLOCKS["KILDETROSKAP"]
SITAT_FORMAT = _BLOCKS["SITAT_FORMAT"]
ANFORSELSTEGN = _BLOCKS["ANFORSELSTEGN"]
BALANSE = _BLOCKS["BALANSE"]
MOTSTRIDENDE = _BLOCKS["MOTSTRIDENDE"]
SPRAK = _BLOCKS["SPRAK"]

# Order used when assembling the full constitution.
ALL_BLOCKS = [KILDETROSKAP, SITAT_FORMAT, ANFORSELSTEGN, BALANSE, MOTSTRIDENDE, SPRAK]


def constitution(blocks: list[str] | None = None) -> str:
    """Join the chosen rule blocks into one prompt section (all blocks by default)."""
    return "\n\n".join(blocks if blocks is not None else ALL_BLOCKS)


__all__ = [
    "KILDETROSKAP",
    "SITAT_FORMAT",
    "ANFORSELSTEGN",
    "BALANSE",
    "MOTSTRIDENDE",
    "SPRAK",
    "ALL_BLOCKS",
    "constitution",
]
