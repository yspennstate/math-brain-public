"""Submit only to the expressly authorized draft inbox; no live-store operation."""
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
local = ROOT / "bundle_001.json"
bundle = json.loads(local.read_text(encoding="utf-8"))
assert bundle["spec"] == "mathbrain-draft-v1"
assert all(e["kind"] == "concept" and e["proof_text"] is None for e in bundle["entries"])
destination_dir = Path("~/math-brain-inbox/w427")
destination_dir.mkdir(exist_ok=True)
destination = destination_dir / "bundle_001.json"
temporary = destination_dir / "bundle_001.json.part"
payload = local.read_bytes()
if destination.exists():
    assert destination.read_bytes() == payload, "existing inbox artifact differs; do not overwrite"
    outcome = "identical draft already present"
else:
    with temporary.open("xb") as stream:
        stream.write(payload)
    temporary.rename(destination)
    outcome = "complete draft renamed from .part to .json"
receipt = {
    "submitted_at": datetime.now(timezone.utc).isoformat(),
    "artifact": str(destination), "bytes": len(payload), "entries": len(bundle["entries"]),
    "kind": "concept-only DRAFT", "outcome": outcome,
    "integrator_invoked": False, "live_store_written_by_worker": False,
    "mathematical_review": "pending w428 independent check",
    "different_model_gate": "not established; served-model receipts unavailable",
    "ingestion": "unconfirmed", "retrieval": "unconfirmed",
}
(ROOT / "SUBMISSION_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")

claims_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
claims[0]["source"] = {"type": "owner-own-work", "artifact": "INDEPENDENT.md", "license": "owner-own-work",
                       "primary_source_status": "self-contained elementary derivation; accepted source tag confirmed against BUNDLE_SPEC"}
cycle_claim = {
    "claim_id": "w427-C0023-004", "target": "C0023",
    "statement": "In the four-cycle o--a--b--c--o with relays A={a,c}, no deterministic vertex v and relay a_star satisfy both separator assumptions of w426 L1. This obstructs that finite-forest proof extension, not the product gluing inequality.",
    "assumptions": ["Undirected four-cycle with four distinct vertices", "A={a,c}, target b, origin o"],
    "source": {"type": "owner-own-work", "license": "owner-own-work", "artifact": "PAIRED_AUDIT.md"},
    "counterexample": "The direct o-to-a and o-to-c paths share only o, so their common separator must be o. The direct edge from either relay to b avoids o. At p=1/2 exact enumeration still gives terminal probability 7/16 above product bound 27/64.",
    "independent_reviewer": "w428 (pending)", "remaining_gap": "Independent referee check pending; no general gluing refutation.",
    "status": "proved special case", "review_state": "pending", "recorded_at": "2026-10-10",
}
if not any(row.get("claim_id") == cycle_claim["claim_id"] for row in claims):
    claims.append(cycle_claim)
claims_path.write_text("".join(json.dumps(row, separators=(",", ":")) + "\n" for row in claims), encoding="utf-8")

source_path = ROOT / "SOURCE_STATUS.json"
source = json.loads(source_path.read_text(encoding="utf-8"))
source["states"] = {
    "submitted": {"state": "submitted", "artifact": str(destination), "receipt": "SUBMISSION_RECEIPT.json"},
    "reviewed": {"state": "pending", "referee": "w428", "different_model_gate": "not established"},
    "ingested": {"state": "unconfirmed", "worker_ingestion_attempted": False},
    "retrievable": {"state": "unconfirmed", "post_ingestion_recall_run": False},
}
canonical_path = ROOT / "CANONICAL_RECEIPT.json"
if canonical_path.exists():
    source["canonical_store_read"] = json.loads(canonical_path.read_text(encoding="utf-8"))
source["paired_audit"] = {"artifact": "PAIRED_AUDIT.jsonl", "scoped_keeps": ["w426-C0023-L1", "w426-C0023-L2", "w426-C0023-B1"],
                          "limits": "These are w427 verdicts on mathematical statements, not review of another verdict or a parent-problem proof."}
source["pair_measurements"] = json.loads((ROOT / "PAIR_MEASUREMENTS.json").read_text(encoding="utf-8"))
source_path.write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8")

artifact_names = ["ATTEMPT.md", "CLAIMS.jsonl", "PAIRED_AUDIT.jsonl", "MEASUREMENTS.json",
                  "PAIR_MEASUREMENTS.json", "bundle_001.json", "REVIEW_PACKET.md", "REPORT.md"]
hashes = {name: {"path": str(ROOT / name), "sha256": hashlib.sha256((ROOT / name).read_bytes()).hexdigest()}
          for name in artifact_names}
(ROOT / "ARTIFACT_HASHES.json").write_text(json.dumps({
    "purpose": "Byte identity for the review handoff only; not a source manifest, proof certificate, store seal or release MAC.",
    "artifacts": hashes}, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
print("REVIEW_PACKET_SHA256", hashes["REVIEW_PACKET.md"]["sha256"])
print("BUNDLE_SHA256", hashes["bundle_001.json"]["sha256"])
