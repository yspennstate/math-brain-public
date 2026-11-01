"""Submit only the task-authorized own inbox draft and hook proposal."""
import hashlib
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TARGET = Path("~/math-brain-inbox/w555/bundle_001_c0047_independent_20261010.json")
HOOK_TARGET = Path("~/primary_directive/hooks1000/proposals/percolation-w555.jsonl")
claims = {"inbox":"clm-e54c5d9c2c", "hook":"clm-027728637f"}

draft = (ROOT / "bundle_001.json").read_bytes()
obj = json.loads(draft)
assert obj["author_agent"] == "w555"
assert obj["parent_problem_solved"] is False
assert all(entry["kind"] == "concept" and entry["proof_text"] is None for entry in obj["entries"])
TARGET.parent.mkdir(parents=True, exist_ok=True)
if TARGET.exists():
    if TARGET.read_bytes() != draft:
        raise RuntimeError("Existing external draft differs; refusing overwrite")
    inbox_state = "already-submitted-identical"
else:
    part = TARGET.with_suffix(".part")
    with part.open("xb") as out:
        out.write(draft)
        out.flush()
        os.fsync(out.fileno())
    part.rename(TARGET)
    inbox_state = "submitted-DRAFT"

hook_line = (ROOT / "HOOK_PROPOSAL.jsonl").read_text(encoding="utf-8")
hook = json.loads(hook_line)
assert hook["proposer"] == "w555" and len(hook["text"]) <= 300
HOOK_TARGET.parent.mkdir(parents=True, exist_ok=True)
exists = False
if HOOK_TARGET.exists():
    for line in HOOK_TARGET.read_text(encoding="utf-8").splitlines():
        previous = json.loads(line)
        if previous["id"] == hook["id"]:
            if previous != hook:
                raise RuntimeError("Existing hook with same id differs; refusing overwrite")
            exists = True
if not exists:
    with HOOK_TARGET.open("a", encoding="utf-8", newline="\n") as out:
        out.write(hook_line)
        out.flush()
        os.fsync(out.fileno())

receipt = {"inbox_path": str(TARGET), "inbox_state": inbox_state,
           "hook_path": str(HOOK_TARGET), "hook_state": "already-identical" if exists else "proposed",
           "narrow_claims": claims, "reviewed": False, "ingested": False, "retrievable": False,
           "live_store_mutations": 0}
(ROOT / "SUBMISSION_RECEIPT.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
status_path = ROOT / "SOURCE_STATUS.json"
status = json.loads(status_path.read_text(encoding="utf-8"))
status["submission_state"] = inbox_state
status["submission_receipt"] = str(ROOT / "SUBMISSION_RECEIPT.json")
status["review_state"] = "PENDING: w557 mathematical verdict; w556 adversarial check"
status["ingestion_state"] = "NOT_INGESTED"
status["retrieval_state"] = "NOT_TESTED"
status_path.write_text(json.dumps(status, indent=2)+"\n", encoding="utf-8")

# These are review-input byte hashes, not the integrator's release manifests or seals.
inputs = ["PROOFS.md", "ATTEMPT.md", "CLAIMS.jsonl", "SOURCE_STATUS.json", "REVIEW_PACKET.md", "REPORT.md",
          "STORE_SOURCE_REPORT.json", "PRIOR_ATTEMPT_SOURCE_REPORT.json", "STORE_CORRECTION.json",
          "RELATION_EVIDENCE.json", "bundle_001.json", "HOOK_PROPOSAL.jsonl", "PACKET_VALIDATION.json",
          "MEASUREMENTS.json", "MEASUREMENTS_001.json", "COMPUTE_GATE.json", "COMPUTE_GATE_001.json",
          "verify_finite.py", "inspect_scoped_sources.py", "patches/01_c0047_normalized_spectral_degree.diff",
          "SUBMISSION_RECEIPT.json"]
hashes = {"purpose":"review-input identity only; NOT a mathematical or formal certificate",
          "files": {name: hashlib.sha256((ROOT/name).read_bytes()).hexdigest() for name in inputs},
          "external_inbox_path": str(TARGET), "external_inbox_identical_to_local": TARGET.read_bytes()==draft}
(ROOT / "PACKET_HASHES.json").write_text(json.dumps(hashes, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"submission": receipt, "proof_sha256": hashes["files"]["PROOFS.md"],
                  "claims_sha256": hashes["files"]["CLAIMS.jsonl"], "bundle_sha256": hashes["files"]["bundle_001.json"]}, indent=2))
