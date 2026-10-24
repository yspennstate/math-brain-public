"""Citation-entailment records without redistributing source text."""

from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum


class CitationVerdict(StrEnum):
    SUPPORTS = "supports"
    PARTIAL = "partial"
    CONTRADICTS = "contradicts"
    NOT_FOUND = "not_found"
    INACCESSIBLE = "inaccessible"


@dataclass(frozen=True, slots=True)
class CitationCheck:
    source_id: str
    source_hash: str
    locator: str
    attributed_claim: str
    verdict: CitationVerdict
    assumptions_match: bool
    statement_match: bool
    authorship_match: bool
    checked_by: str
    notes: str = ""

    def __post_init__(self) -> None:
        required = {
            "source_id": self.source_id,
            "source_hash": self.source_hash,
            "locator": self.locator,
            "attributed_claim": self.attributed_claim,
            "checked_by": self.checked_by,
        }
        missing = [name for name, value in required.items() if not value.strip()]
        if missing:
            raise ValueError(f"citation check is missing: {', '.join(missing)}")

    @property
    def fully_verified(self) -> bool:
        return (
            self.verdict is CitationVerdict.SUPPORTS
            and self.assumptions_match
            and self.statement_match
            and self.authorship_match
        )
