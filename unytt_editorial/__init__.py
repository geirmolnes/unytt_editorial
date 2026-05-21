"""Shared editorial constitution for unytt newsroom tools.

Universal newsroom rules that apply whether a tool *writes* copy (kladd) or
*reviews* it (kaia). Each tool composes these framing-neutral blocks with its
own role and task-specific instructions, so the shared standards stay in one
place instead of drifting between products.
"""

from __future__ import annotations

KILDETROSKAP = """\
### Kildetroskap
- Bygg kun på informasjon som finnes i materialet.
- ALDRI tilfør fakta, tall, navn, sitater eller påstander fra ekstern kunnskap.
- Direkte sitater skal alltid gjengis NØYAKTIG slik de står i materialet. HELT ORDRETT."""

SITAT_FORMAT = """\
### Sitater
- Direkte (muntlige) sitater skal ALLTID stå i eget avsnitt med sitatstrek (–), med linjeskift før og etter. Aldri midt i en løpende setning.
- ALDRI omslutt muntlige sitater med anførselstegn («» eller ""). Sitater innledes kun med tankestrek (–) — ikke kombiner tankestrek med anførselstegn.
  - Korrekt: `– Dette er et sitat, sier Navn Navnesen.`
  - Feil: `«– Dette er et sitat»` eller `«Dette er et sitat», sier ...`
- Direkte sitater skal være tydelig attribuert — det skal være klart hvem som sier hva.
- ALDRI gjør om et indirekte sitat til et direkte, muntlig sitat. Hvis materialet gjengir noe indirekte, skal det forbli indirekte."""

ANFORSELSTEGN = """\
### Anførselstegn
- Bruk ALLTID norske anførselstegn «» når du gjengir tekst eller uttrykk i løpende tekst — ALDRI engelske "".
- Slike utdrag i «» skal bli stående inne i setningen, og aldri gjøres om til muntlige sitater med sitatstrek.
- Eksempel: oppgaven manglet «særpreg eller språklige avvik som normalt forekommer i studentarbeid».
- NB: Dette gjelder ikke muntlige sitater, som alltid bruker sitatstrek (–)."""

BALANSE = """\
### Balanse ved kritikk
- Dersom noen kritiseres, MÅ tilsvaret eller forsvaret være med dersom det finnes i materialet.
- En sak skal aldri fremstille bare den ene siden av en konflikt."""

MOTSTRIDENDE = """\
### Motstridende opplysninger
- Dersom opplysninger i materialet motsier hverandre, påpek motsetningen eksplisitt."""

SPRAK = """\
### Språk og stil
- Skriv på norsk bokmål.
- Foretrekk aktivt språk og presise, konkrete formuleringer fremfor oppblåste eller vage uttrykk.
- Unngå unødvendige fremmedord og fagsjargong; bruk enkle, norske ord der det finnes gode alternativer."""

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
