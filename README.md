# unytt_editorial

Shared editorial constitution for unytt newsroom tools.

These are the universal newsroom rules that apply whether a tool **writes** copy
([kladd](https://github.com/geirmolnes/kladd)) or **reviews** it
([kaia](https://github.com/geirmolnes/kaia)): source fidelity, quote typography,
balance/tilsvar, contradictions, and language. Keeping them in one place stops
the rules from drifting between products.

## Usage

```python
import unytt_editorial as ed

# All blocks, joined:
ed.constitution()

# Just the quote rules:
ed.constitution([ed.SITAT_FORMAT, ed.ANFORSELSTEGN])
```

Each tool composes these framing-neutral blocks with its own role line and
task-specific instructions (kladd: drafting/sitatsak/manus; kaia: review/cut/
proofread).

## Blocks

`KILDETROSKAP` · `SITAT_FORMAT` · `ANFORSELSTEGN` · `BALANSE` · `MOTSTRIDENDE` · `SPRAK`

The rule prose lives in `unytt_editorial/constitution.md` — edit the text
there, not in `__init__.py`. Each block is delimited by an HTML-comment marker
(`<!-- KILDETROSKAP -->`) that maps it to the matching `ed.<NAME>` constant;
keep the markers and their names. The module just parses and assembles it.

## Tests

```bash
uv run pytest tests/ -v
```
