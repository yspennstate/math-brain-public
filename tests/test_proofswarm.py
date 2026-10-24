import hashlib
import json
from dataclasses import replace

import pytest

from math_brain.models import Claim, ClaimKind, EdgeKind, EvidenceKind, RecordStatus
from math_brain.proofswarm import (
    MAX_PROOFSWARM_TICKET_BYTES,
    import_proofswarm_ticket,
)

TREE_DIGEST = "sha256:" + "a" * 64


def ticket_bytes(statement: str, *, verdict: str = "lean_verified") -> bytes:
    content = "exact local verifier artifact"
    payload = {
        "ticket_id": "ticket-001",
        "problem_id": "problem-001",
        "statement_informal": statement,
        "statement_lean": "theorem sample : True := by trivial",
        "assumptions": [],
        "parents": [],
        "children": [],
        "verdict": verdict,
        "evidence": [
            {
                "kind": "lean_proof",
                "content": content,
                "sha256": hashlib.sha256(content.encode("utf-8")).hexdigest(),
                "produced_by": "prover",
                "produced_at": "2026-08-02T00:00:00+00:00",
                "cost_usd": 0.0,
                "metadata": {"reported_ok": True},
            }
        ],
        "history": [],
        "confidence": 1.0,
        "cost_usd": 0.0,
        "store_revision": 1,
        "created_at": "2026-08-02T00:00:00+00:00",
        "updated_at": "2026-08-02T00:00:01+00:00",
    }
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()


def import_ticket(raw: bytes, claim: Claim):
    return import_proofswarm_ticket(
        raw,
        claim=claim,
        observed_source_tree_digest=TREE_DIGEST,
        expected_source_tree_digest=TREE_DIGEST,
    )


def test_positive_ticket_verdict_remains_discovery_only() -> None:
    claim = Claim("For every n, n + 0 = n.", ClaimKind.THEOREM)
    candidate = import_ticket(ticket_bytes(claim.statement), claim)
    assert candidate.verdict == "lean_verified"
    assert not candidate.promotion_eligible
    assert candidate.discovery_evidence.kind is EvidenceKind.DISCOVERY_REPORT
    assert not candidate.discovery_evidence.passed
    assert candidate.discovery_evidence.artifact_hash == candidate.ticket_digest
    assert "not verification authority" in candidate.discovery_evidence.limitations[0]


def test_ticket_must_match_claim_and_pinned_source_tree() -> None:
    claim = Claim("For every n, n + 0 = n.", ClaimKind.THEOREM)
    with pytest.raises(ValueError, match="does not exactly match"):
        import_ticket(ticket_bytes("A different statement"), claim)
    with pytest.raises(ValueError, match="differs from the pinned"):
        import_proofswarm_ticket(
            ticket_bytes(claim.statement),
            claim=claim,
            observed_source_tree_digest="sha256:" + "b" * 64,
            expected_source_tree_digest=TREE_DIGEST,
        )


def test_ticket_rejects_nonzero_cost_and_unbound_evidence() -> None:
    claim = Claim("For every n, n + 0 = n.", ClaimKind.THEOREM)
    payload = json.loads(ticket_bytes(claim.statement))
    payload["cost_usd"] = 0.01
    with pytest.raises(ValueError, match="zero marginal API cost"):
        import_ticket(json.dumps(payload).encode(), claim)
    payload["cost_usd"] = 0.0
    payload["evidence"][0]["sha256"] = "0" * 64
    with pytest.raises(ValueError, match="does not bind"):
        import_ticket(json.dumps(payload).encode(), claim)


def test_ticket_rejects_duplicate_keys_and_oversized_input() -> None:
    claim = Claim("For every n, n + 0 = n.", ClaimKind.THEOREM)
    duplicated = ticket_bytes(claim.statement).replace(
        b'{"assumptions":',
        b'{"ticket_id":"shadow","assumptions":',
        1,
    )
    with pytest.raises(ValueError, match="duplicate JSON object key"):
        import_ticket(duplicated, claim)
    with pytest.raises(ValueError, match="fixed byte bound"):
        import_ticket(b"{" + b" " * MAX_PROOFSWARM_TICKET_BYTES + b"}", claim)


def test_ticket_rejects_deep_json_and_nontext_evidence_kind() -> None:
    claim = Claim("For every n, n + 0 = n.", ClaimKind.THEOREM)
    payload = json.loads(ticket_bytes(claim.statement))
    nested: object = "leaf"
    for _ in range(70):
        nested = [nested]
    payload["evidence"][0]["metadata"] = {"nested": nested}
    with pytest.raises(ValueError, match="JSON structure budget"):
        import_ticket(json.dumps(payload).encode(), claim)
    payload = json.loads(ticket_bytes(claim.statement))
    payload["evidence"][0]["kind"] = []
    with pytest.raises(ValueError, match="evidence kind"):
        import_ticket(json.dumps(payload).encode(), claim)


def test_flipped_discovery_evidence_changes_digest_but_gains_no_authority(
    tmp_path,
) -> None:
    claim = Claim("For every n, n + 0 = n.", ClaimKind.THEOREM)
    candidate = import_ticket(ticket_bytes(claim.statement), claim)
    forged = replace(candidate.discovery_evidence, passed=True)
    assert forged.digest() != candidate.discovery_evidence.digest()
    assert candidate.discovery_evidence.passed is False
    from math_brain.store import ResearchStore

    with ResearchStore(tmp_path / "brain.sqlite3") as store:
        store.add_claim(claim)
        store.add_evidence(forged)
        assert {edge.kind for edge in store.iter_edges()} == {
            EdgeKind.SEMANTIC_ASSOCIATION
        }
        assert store.evidence_attestations_for(claim.id) == {}
        assert store.evidence_receipts_for(claim.id) == {}
        assert store.current_status(claim.id) is RecordStatus.UNVERIFIED


def test_same_exact_ticket_produces_same_import_digest() -> None:
    claim = Claim("For every n, n + 0 = n.", ClaimKind.THEOREM)
    raw = ticket_bytes(claim.statement)
    first = import_ticket(raw, claim)
    second = import_ticket(raw, claim)
    assert first == second
    assert first.digest() == second.digest()
