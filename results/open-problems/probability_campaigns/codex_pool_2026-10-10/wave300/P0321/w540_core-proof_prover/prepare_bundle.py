"""Stage reviewed-in-part draft concepts; never writes a live mathematical store."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INBOX = Path("~/math-brain-inbox/w540")
claims_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8-sig").splitlines() if line.strip()]
measurements = json.loads((ROOT / "MEASUREMENTS.json").read_text(encoding="utf-8"))
assert measurements["passed"] and len(claims) == 6
for claim in claims:
    claim["peer_audit"] = {
        "auditor": "w541",
        "path": "~/brain_workers/w541/AUDIT.md",
        "verdict": "KEEP conditional reductions and counterexamples; M explicitly unproved",
        "required_fix": "Qualified the volume-only sentence; fixed-r vanishing errors suffice for an iterated limit.",
        "fix_applied": True,
        "designated_referee": "w542",
        "designated_referee_status": "pending"
    }
    if claim["id"].endswith("-L3"):
        claim["statement"] += (" Alternatively, retain L1 and the amplitude bounds, assume epsilon_{L,r}->0 "
                               "at every fixed r and existence of the fixed-r limit of C_{6,L}; taking L->infinity "
                               "before r->infinity yields A_- exp(-H)r^(-eta)<=|C_6(r)|<=A_+ exp(H)r^(-eta). "
                               "No joint distance/volume rate is asserted by this alternative.")
        claim["proof_or_counterexample"] += " For the alternative, pass the reverse/direct triangle inequalities to the fixed-r limit, then let r increase."
        claim["assumptions"].append("Either the original uniform scale-decaying error or the stated fixed-r vanishing-error alternative; limit order is explicit.")
claims_path.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")

entry_names = {
    "L1": ("absolute-cumulant-bounds-give-algebraic-vertex-order", "Conditional cumulant-to-vertex bounds"),
    "L2": ("anchored-mixed-cumulant-summation", "Connected scale cumulants without independence"),
    "L3": ("nonzero-bond-amplitude-correlation-transfer", "Transfer to a microscopic bond observable with explicit limit order"),
    "C1": ("logarithmic-variance-does-not-imply-algebraic-vertex-order", "Logarithmic variance can have zero vertex correlation"),
    "C2": ("wrapped-gaussian-vertex-cancellation-at-correlation-scale", "Positive wrapped-Gaussian perturbation cancels the leading vertex"),
    "M": ("p0321-microscopic-connected-defect-gap", "Unproved microscopic input for the Riesz hexatic route")
}
entries = []
for claim in claims:
    suffix = claim["id"].rsplit("-", 1)[1]
    logical_name, title = entry_names[suffix]
    entries.append({
        "key": suffix.lower(), "namespace": "probability.statisticalmechanics",
        "logical_name": logical_name, "kind": "concept", "title": "DRAFT: " + title,
        "statement": "DRAFT concept material, not a full P0321 proof. " + claim["statement"] + " Independent designated-referee review is pending.",
        "proof_text": None, "assumptions": claim["assumptions"], "domain": "probability theory and statistical mechanics",
        "source": {"source_id": "owner:w540:P0321-transfer-20261010:" + suffix.lower(), "url": None,
                   "revision": "author-proof-w541-audit-fix-2026-10-10-v1", "license": "owner-own-work",
                   "excerpt": None, "local_path": "~/brain_workers/w540/ATTEMPT.md"},
        "review_status": "w541 checked; designated referee w542 pending", "remaining_gap": claim["remaining_gap"]
    })
relations = [
    {"from_key": "l3", "to_key": "l1", "kind": "depends_on",
     "rationale": "L3 begins 'Assume L1 with q=6'; L1 supplies exp(-H)r^(-eta)<=|E exp(iqX)|<=exp(H)r^(-eta), the exact leading bounds used by the two triangle inequalities."},
    {"from_key": "l2", "to_key": "l1", "kind": "semantic_association",
     "rationale": "L2 supplies sum_{n>=3}q^n|kappa_n(X)|/n!<=Y sum q^n b_n. L1 requires this same higher-cumulant bound plus a separate logarithmic variance estimate; L2 does not prove the missing variance input."},
    {"from_key": "c1", "to_key": "l1", "kind": "semantic_association",
     "rationale": "C1 has exact logarithmic variance but E exp(iqX)=0. L1 has a positive lower bound only under absolute all-order cumulant summability, which C1 cannot satisfy at that q."},
    {"from_key": "c2", "to_key": "l3", "kind": "semantic_association",
     "rationale": "C2 cancels a wrapped-Gaussian correlation a=r^(-eta) at TV distance 2a/pi. L3 requires an insertion error below the leading correlation scale, or an error that disappears in the fixed-r limit; C2 has neither guarantee."},
    {"from_key": "m", "to_existing_logical": "math:probability.core:open-problem-p0321-existence-of-a-hexatic-phase-for-two-dimensional-riesz-gases", "kind": "cites",
     "rationale": "The existing card asks for an intermediate hexatic phase with orientational order and absent crystalline positional order. M is the explicitly unproved microscopic defect/insertion and positional-disorder input needed by this conditional angular route."}
]
bundle = {"spec": "mathbrain-draft-v1", "author_agent": "w540", "bundle_slug": "p0321-cumulant-transfer-001",
          "entries": entries, "relations": relations, "bundle_state": "DRAFT",
          "review_packet": "~/brain_workers/w540/REVIEW_PACKET.md"}

# A local schema/edge check only. The live integrator is intentionally not run:
# the worker is forbidden to write live stores and cannot self-ingest proofs.
keys = {entry["key"] for entry in entries}
assert len(keys) == len(entries) <= 200
allowed_relations = {"depends_on", "defines", "proves", "refutes", "generalizes", "specializes", "analogous_to", "cites", "semantic_association"}
for entry in entries:
    assert entry["kind"] == "concept" and entry["proof_text"] is None
    assert entry["source"]["license"].startswith("owner-own-work")
    assert entry["statement"] and entry["logical_name"] == entry["logical_name"].lower()
for relation in relations:
    assert relation["from_key"] in keys and relation["kind"] in allowed_relations
    assert relation.get("to_key") in keys or relation.get("to_existing_logical")
    assert relation["rationale"]
text = json.dumps(bundle, indent=2, ensure_ascii=False) + "\n"
(ROOT / "brain_bundle_001.json").write_text(text, encoding="utf-8")
INBOX.mkdir(parents=True, exist_ok=True)
final_path = INBOX / "bundle_001.json"
if final_path.exists():
    if final_path.read_text(encoding="utf-8") != text:
        raise RuntimeError("Preserve existing inbox bundle; a changed payload needs a new bundle number")
else:
    part_path = INBOX / "bundle_001.part"
    if part_path.exists():
        raise RuntimeError("Preserve any earlier incomplete artifact for inspection")
    part_path.write_text(text, encoding="utf-8")
    part_path.rename(final_path)

state = {"agent": "w540", "bundle_path": str(final_path), "entry_count": len(entries),
         "relation_count": len(relations), "submitted": True, "reviewed": False,
         "review_receipts": [{"auditor": "w541", "path": "~/brain_workers/w541/AUDIT.md", "status": "conditional keep; wording fix applied"}],
         "designated_referee": "w542", "ingested": False, "retrievable": False,
         "live_integrator_run": False, "scope": "All six entries remain labeled DRAFT concepts; full P0321 input M is unproved."}
(ROOT / "BUNDLE_STATE.json").write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"submitted": True, "entries": len(entries), "relations": len(relations),
                  "reviewed": False, "ingested": False, "retrievable": False}))
