"""Versioned, hashable records used by the trusted core."""

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from typing import Any
from uuid import uuid4


SCHEMA_VERSION = 1


class RecordStatus(StrEnum):
    UNVERIFIED = "unverified"
    PROVISIONAL = "provisional"
    VERIFIED = "verified"
    REFUTED = "refuted"
    UNKNOWN = "unknown"


class ClaimKind(StrEnum):
    DEFINITION = "definition"
    LEMMA = "lemma"
    THEOREM = "theorem"
    CONJECTURE = "conjecture"
    COMPUTATION = "computation"
    HEURISTIC = "heuristic"
    EXAMPLE = "example"
    COUNTEREXAMPLE = "counterexample"


class EvidenceKind(StrEnum):
    NUMERIC = "numeric"
    SYMBOLIC = "symbolic"
    EXHAUSTIVE_FINITE = "exhaustive_finite"
    HUMAN_PROOF_REVIEW = "human_proof_review"
    LEAN_KERNEL = "lean_kernel"
    FORMALIZATION_FIDELITY = "formalization_fidelity"
    CITATION = "citation"
    INDEPENDENT_REPRODUCTION = "independent_reproduction"
    COUNTEREXAMPLE = "counterexample"


class NodeKind(StrEnum):
    CLAIM = "claim"
    EVIDENCE = "evidence"
    SOURCE = "source"
    ERROR_PATTERN = "error_pattern"
    MISTAKE = "mistake"
    REFLEX = "reflex"
    OPEN_QUESTION = "open_question"


class EdgeKind(StrEnum):
    DEPENDS_ON = "depends_on"
    DEFINES = "defines"
    PROVES = "proves"
    REFUTES = "refutes"
    GENERALIZES = "generalizes"
    SPECIALIZES = "specializes"
    ANALOGOUS_TO = "analogous_to"
    CITES = "cites"
    VERIFIED_BY = "verified_by"
    FAILS_UNDER = "fails_under"
    TRIGGERS = "triggers"


class EdgePolarity(StrEnum):
    """The epistemic sign of an edge, separate from its typed meaning."""

    POSITIVE = "positive"
    NEGATIVE = "negative"


NEGATIVE_EDGE_KINDS = frozenset(
    {
        EdgeKind.REFUTES,
        EdgeKind.FAILS_UNDER,
        EdgeKind.TRIGGERS,
    }
)


def utc_now() -> str:
    return datetime.now(UTC).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid4().hex}"


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def content_hash(value: Any) -> str:
    return "sha256:" + hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


@dataclass(frozen=True, slots=True)
class Claim:
    statement: str
    kind: ClaimKind
    assumptions: tuple[str, ...] = ()
    domain: str = ""
    status: RecordStatus = RecordStatus.UNVERIFIED
    id: str = field(default_factory=lambda: new_id("claim"))
    schema_version: int = SCHEMA_VERSION
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if not self.statement.strip():
            raise ValueError("claim statement must not be empty")
        if self.schema_version != SCHEMA_VERSION:
            raise ValueError(f"unsupported claim schema version: {self.schema_version}")

    def digest(self) -> str:
        return content_hash(asdict(self))


@dataclass(frozen=True, slots=True)
class Evidence:
    claim_id: str
    kind: EvidenceKind
    summary: str
    scope: str
    verifier: str
    passed: bool
    artifact_hash: str | None = None
    limitations: tuple[str, ...] = ()
    id: str = field(default_factory=lambda: new_id("evidence"))
    schema_version: int = SCHEMA_VERSION
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        for name, value in (
            ("claim_id", self.claim_id),
            ("summary", self.summary),
            ("scope", self.scope),
            ("verifier", self.verifier),
        ):
            if not value.strip():
                raise ValueError(f"{name} must not be empty")

    def digest(self) -> str:
        return content_hash(asdict(self))


@dataclass(frozen=True, slots=True)
class VerificationEvent:
    claim_id: str
    from_status: RecordStatus
    to_status: RecordStatus
    evidence_ids: tuple[str, ...]
    rationale: str
    reviewer: str
    id: str = field(default_factory=lambda: new_id("verification"))
    schema_version: int = SCHEMA_VERSION
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if not self.rationale.strip() or not self.reviewer.strip():
            raise ValueError("rationale and reviewer are required")
        if self.to_status is RecordStatus.VERIFIED and not self.evidence_ids:
            raise ValueError("verified promotion requires evidence")

    def digest(self) -> str:
        return content_hash(asdict(self))


@dataclass(frozen=True, slots=True)
class GraphNode:
    id: str
    kind: NodeKind
    title: str
    body: str = ""
    metadata: dict[str, Any] = field(default_factory=dict)
    schema_version: int = SCHEMA_VERSION
    created_at: str = field(default_factory=utc_now)

    def __post_init__(self) -> None:
        if not self.id.strip() or not self.title.strip():
            raise ValueError("graph node id and title are required")

    def digest(self) -> str:
        return content_hash(asdict(self))


@dataclass(frozen=True, slots=True)
class GraphEdge:
    source_id: str
    target_id: str
    kind: EdgeKind
    rationale: str
    weight: float = 1.0
    metadata: dict[str, Any] = field(default_factory=dict)
    id: str = field(default_factory=lambda: new_id("edge"))
    schema_version: int = SCHEMA_VERSION
    created_at: str = field(default_factory=utc_now)
    polarity: EdgePolarity | None = None

    def __post_init__(self) -> None:
        if not self.source_id.strip() or not self.target_id.strip():
            raise ValueError("edge endpoints are required")
        if self.source_id == self.target_id:
            raise ValueError("self edges are not allowed")
        if not self.rationale.strip():
            raise ValueError("edge rationale is required")
        if not 0 < self.weight <= 1:
            raise ValueError("edge weight must be in (0, 1]")
        expected_polarity = (
            EdgePolarity.NEGATIVE
            if self.kind in NEGATIVE_EDGE_KINDS
            else EdgePolarity.POSITIVE
        )
        if self.polarity is None:
            object.__setattr__(self, "polarity", expected_polarity)
        elif self.polarity is not expected_polarity:
            raise ValueError(
                f"{self.kind.value} edges must have {expected_polarity.value} polarity"
            )

    @property
    def signed_weight(self) -> float:
        """Return a negative weight for warning/refutation edges."""

        sign = -1.0 if self.polarity is EdgePolarity.NEGATIVE else 1.0
        return sign * self.weight

    @property
    def is_warning(self) -> bool:
        return self.polarity is EdgePolarity.NEGATIVE

    def digest(self) -> str:
        payload = asdict(self)
        # Polarity is a validated projection of ``kind``. Excluding the redundant
        # field preserves hashes written by schema-version-1 stores.
        payload.pop("polarity")
        return content_hash(payload)
