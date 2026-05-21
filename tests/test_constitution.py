"""Tests for the shared editorial constitution."""

from __future__ import annotations

import unytt_editorial as ed


def test_constitution_includes_all_blocks_by_default():
    full = ed.constitution()
    for block in ed.ALL_BLOCKS:
        assert block in full


def test_constitution_selects_subset():
    text = ed.constitution([ed.SITAT_FORMAT, ed.ANFORSELSTEGN])
    assert ed.SITAT_FORMAT in text
    assert ed.KILDETROSKAP not in text


def test_blocks_are_norwegian_and_nonempty():
    for block in ed.ALL_BLOCKS:
        assert block.strip()
        assert block.startswith("### ")
