"""Record a read of a claim as evidence the store can show.

The store's evidence tables were empty for a month while agents read claims by hand and filed the
verdicts in ledgers the hook never sees. This records such a read where the hook looks.

Two roles, kept honest by the store's own rules:

  --role agent   (default) an agent's read. Recorded as a DISCOVERY_REPORT through
                 ResearchStore.add_evidence - unauthenticated, linked to the claim by a
                 semantic-association edge, and by design never an authority: decide_promotion()
                 ignores discovery evidence, so the claim's status does not move. The hook can
                 still say "read on <date> by <who>: sound" beside its hint, which is the truth.
  --role human   a human's read. HUMAN_PROOF_REVIEW under the human-reviewer key
                 (local/human_review.key, 32+ bytes, never committed). One human review makes a
                 theorem PROVISIONAL, never VERIFIED: the store requires a second, independent
                 route for that (see decide_promotion). The key is not minted here - a missing key
                 is a refusal, because inventing a human authority for an agent would be a lie.

    python tools/record_review.py --claim claim_<id> --reviewer <who> --verdict sound \
        --summary "statement and proof sketch read against the standard sources" \
        [--scope "statement + proof sketch"] [--limitation "..."]... [--role agent|human] [--store PATH]

Exit 0 on success. Idempotent per (claim, reviewer, summary, verdict): a repeat is skipped.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from dataclasses import replace
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUILD = Path(os.environ.get("MATHBRAIN_BUILD", HERE.parent))
sys.path.insert(0, str(BUILD / "src"))

from math_brain.models import (  # noqa: E402
    Evidence,
    EvidenceAttestation,
    EvidenceAuthorityMode,
    EvidenceAuthorityRole,
    EvidenceKind,
    EvidenceReceipt,
    content_hash,
)
from math_brain.store import ResearchStore  # noqa: E402

DEFAULT_STORE = Path(os.environ.get("MATHBRAIN_STORE", BUILD / "local" / "population" / "brain.sqlite3"))
HUMAN_KEY = BUILD / "local" / "human_review.key"
HUMAN_KEY_ID = "human-read-v1"

VERDICTS = ("sound", "corrected", "gap", "unsound")


def _existing_summaries(store: ResearchStore, claim_id: str) -> set[str]:
    return {item.summary for item in store.evidence_for(claim_id)}


def record_agent_read(store: ResearchStore, claim_id: str, reviewer: str, verdict: str,
                      summary: str, scope: str, limitations: tuple[str, ...]) -> str | None:
    text = f"read by {reviewer}: {verdict} - {summary}"
    if text in _existing_summaries(store, claim_id):
        return None
    lims = ("an agent's read, recorded as a discovery report; not a verification authority and no status change",) + limitations
    item = Evidence(
        claim_id,
        EvidenceKind.DISCOVERY_REPORT,
        text,
        scope,
        reviewer,
        verdict in ("sound", "corrected"),
        artifact_hash=content_hash({"claim": claim_id, "reviewer": reviewer, "verdict": verdict, "summary": summary}),
        limitations=lims,
    )
    store.add_evidence(item, link=True)
    return item.id


def record_human_read(store: ResearchStore, claim_id: str, reviewer: str, verdict: str,
                      summary: str, scope: str, limitations: tuple[str, ...]) -> str | None:
    from math_brain.verification import (
        EvidenceKeyPolicy,
        EvidenceVerifier,
        evidence_authorization_mac,
        register_authenticated_evidence,
    )

    if not HUMAN_KEY.exists():
        raise SystemExit(f"no human-reviewer key at {HUMAN_KEY}; a human creates it (32+ random bytes) - it is not minted here")
    key = HUMAN_KEY.read_bytes()
    if len(key) < 32:
        raise SystemExit("human-reviewer key must hold at least 32 bytes")
    policy = EvidenceKeyPolicy(key, EvidenceAuthorityRole.HUMAN_REVIEWER,
                               frozenset({EvidenceKind.HUMAN_PROOF_REVIEW, EvidenceKind.CITATION}))
    verifier = EvidenceVerifier({HUMAN_KEY_ID: policy})
    claim = store.get_claim(claim_id)
    if claim is None:
        raise SystemExit(f"unknown claim {claim_id}")
    text = f"human read by {reviewer}: {verdict} - {summary}"
    if text in _existing_summaries(store, claim_id):
        return None
    passed = verdict in ("sound", "corrected")
    nonce = hashlib.sha256(f"{claim_id}|{reviewer}|{summary}|{verdict}".encode("utf-8")).hexdigest()[:40]
    artifact_hash = content_hash({"claim": claim_id, "reviewer": reviewer, "verdict": verdict, "summary": summary})
    item = Evidence(claim_id, EvidenceKind.HUMAN_PROOF_REVIEW, text, scope, reviewer, passed,
                    artifact_hash=artifact_hash, limitations=limitations)
    verifier_digest = content_hash({"verifier": HUMAN_KEY_ID})
    toolchain_digest = content_hash({"toolchain": "human read"})
    source_digest = content_hash({"source": summary})
    attestation = EvidenceAttestation(
        evidence_id=item.id, claim_id=claim.id, claim_digest=claim.digest(), evidence_digest=item.digest(),
        evidence_kind=item.kind, authority_key_id=HUMAN_KEY_ID, authority_role=policy.role,
        authority_mode=EvidenceAuthorityMode.LOCAL_HUMAN_REVIEW, nonce=nonce, artifact_hash=artifact_hash,
        request_digest=content_hash({"request": nonce}), result_digest=content_hash({"result": nonce, "passed": passed}),
        verifier_digest=verifier_digest, toolchain_digest=toolchain_digest, source_digest=source_digest,
        environment_digest=content_hash({"environment": HUMAN_KEY_ID}), passed=passed,
    )
    unsigned = EvidenceReceipt(
        evidence_id=item.id, claim_id=claim.id, claim_digest=claim.digest(), evidence_digest=item.digest(),
        attestation_digest=attestation.digest(), evidence_kind=item.kind, authority_key_id=HUMAN_KEY_ID,
        authority_role=policy.role, nonce=nonce, artifact_hash=artifact_hash, verifier_digest=verifier_digest,
        toolchain_digest=toolchain_digest, source_digest=source_digest, mac="hmac-sha256:" + "0" * 64,
    )
    receipt = replace(unsigned, mac=evidence_authorization_mac(unsigned, policy.key))
    register_authenticated_evidence(store, item, attestation, receipt, verifier, link=True)
    return item.id


def resolve_claim(store: ResearchStore, ref: str) -> str:
    if store.get_claim(ref) is not None:
        return ref
    # allow a title
    matches = [n for n in store.iter_nodes() if (n.title or "").strip().casefold() == ref.strip().casefold()]
    if len(matches) == 1:
        return matches[0].id
    raise SystemExit(f"claim not found or ambiguous: {ref} ({len(matches)} title matches)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--claim", required=True, help="claim id, or an exact title")
    ap.add_argument("--reviewer", required=True)
    ap.add_argument("--verdict", choices=VERDICTS, required=True)
    ap.add_argument("--summary", required=True)
    ap.add_argument("--scope", default="statement and proof sketch")
    ap.add_argument("--limitation", action="append", default=[])
    ap.add_argument("--role", choices=("agent", "human"), default="agent")
    ap.add_argument("--store", default=str(DEFAULT_STORE))
    a = ap.parse_args()
    with ResearchStore(a.store) as store:
        claim_id = resolve_claim(store, a.claim)
        fn = record_human_read if a.role == "human" else record_agent_read
        eid = fn(store, claim_id, a.reviewer, a.verdict, a.summary, a.scope, tuple(a.limitation))
    print(json.dumps({"claim": claim_id, "evidence": eid, "role": a.role, "verdict": a.verdict,
                      "skipped": eid is None}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
