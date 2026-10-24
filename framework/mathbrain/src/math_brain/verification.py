"""Scope-aware status promotion for mathematical claims."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .models import Claim, ClaimKind, Evidence, EvidenceKind, RecordStatus


@dataclass(frozen=True, slots=True)
class PromotionDecision:
    allowed: bool
    target: RecordStatus
    rationale: str
    supporting_evidence_ids: tuple[str, ...] = ()
    missing: tuple[str, ...] = ()


def _passed_kinds(evidence: Iterable[Evidence]) -> dict[EvidenceKind, list[Evidence]]:
    result: dict[EvidenceKind, list[Evidence]] = {}
    for item in evidence:
        if item.passed:
            result.setdefault(item.kind, []).append(item)
    return result


def decide_promotion(
    claim: Claim,
    evidence: Iterable[Evidence],
    *,
    target: RecordStatus,
) -> PromotionDecision:
    relevant = [item for item in evidence if item.claim_id == claim.id]
    kinds = _passed_kinds(relevant)

    counterexamples = kinds.get(EvidenceKind.COUNTEREXAMPLE, [])
    if target is RecordStatus.REFUTED:
        if counterexamples:
            return PromotionDecision(
                True,
                target,
                "a verified counterexample refutes the claim",
                tuple(item.id for item in counterexamples),
            )
        return PromotionDecision(False, target, "refutation requires a verified counterexample", missing=("counterexample",))

    if counterexamples:
        return PromotionDecision(
            False,
            target,
            "claim has a verified counterexample and cannot be promoted",
            tuple(item.id for item in counterexamples),
        )

    passed = [item for item in relevant if item.passed]
    if target is RecordStatus.PROVISIONAL:
        if passed:
            return PromotionDecision(
                True,
                target,
                "at least one scoped check passed; claim remains provisional",
                tuple(item.id for item in passed),
            )
        return PromotionDecision(False, target, "provisional status requires scoped evidence", missing=("passed evidence",))

    if target is not RecordStatus.VERIFIED:
        return PromotionDecision(False, target, f"unsupported promotion target: {target.value}")

    if claim.kind is ClaimKind.CONJECTURE:
        return PromotionDecision(False, target, "a proved conjecture must be restated as a theorem before verification")
    if claim.kind is ClaimKind.HEURISTIC:
        return PromotionDecision(False, target, "heuristics may be supported but not promoted to verified theorems")

    required_alternatives: list[tuple[EvidenceKind, ...]]
    if claim.kind in {ClaimKind.THEOREM, ClaimKind.LEMMA}:
        required_alternatives = [
            (EvidenceKind.LEAN_KERNEL, EvidenceKind.FORMALIZATION_FIDELITY),
            (EvidenceKind.HUMAN_PROOF_REVIEW, EvidenceKind.INDEPENDENT_REPRODUCTION),
        ]
    elif claim.kind is ClaimKind.COMPUTATION:
        required_alternatives = [
            (EvidenceKind.NUMERIC, EvidenceKind.INDEPENDENT_REPRODUCTION),
            (EvidenceKind.SYMBOLIC, EvidenceKind.INDEPENDENT_REPRODUCTION),
        ]
    elif claim.kind is ClaimKind.DEFINITION:
        required_alternatives = [(EvidenceKind.FORMALIZATION_FIDELITY,)]
    else:
        required_alternatives = [
            (EvidenceKind.SYMBOLIC, EvidenceKind.INDEPENDENT_REPRODUCTION),
            (EvidenceKind.EXHAUSTIVE_FINITE, EvidenceKind.INDEPENDENT_REPRODUCTION),
        ]

    for alternative in required_alternatives:
        if all(kind in kinds for kind in alternative):
            supporters = tuple(kinds[kind][0].id for kind in alternative)
            return PromotionDecision(
                True,
                target,
                "evidence satisfies one complete verification route",
                supporters,
            )

    missing_options = tuple(
        " + ".join(kind.value for kind in alternative if kind not in kinds)
        for alternative in required_alternatives
    )
    return PromotionDecision(
        False,
        target,
        "no complete verification route covers the claim",
        missing=missing_options,
    )
