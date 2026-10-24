"""Freeze file provenance and scoped peer receipts, with no integration or live-store mutation."""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def save(path, value):
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


state_path = ROOT / "SOURCE_STATUS.json"
state = json.loads(state_path.read_text(encoding="utf-8"))
source_base = Path("~/Downloads/Probability_1000_intake_claude_20260907/sources/chatterjee_chaos_2008")
expected = {"source.pdf": "17f13a871b84417a83514995c70d2ebf49f5464faeac9dd95e8c4d823b600658",
            "text.txt": "e58058138c0f797174c513fc8579af201360f9d093f241af8c24fe3503017956"}
source_checks = []
for name, target_hash in expected.items():
    path = source_base / name
    row = {"path": str(path).replace("\\", "/"), "catalog_sha256": target_hash}
    if path.is_file() and path.stat().st_size <= 2_000_000:
        raw = path.read_bytes()
        row.update({"available": True, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)})
        row["catalog_match"] = row["sha256"] == target_hash
    else:
        row.update({"available": False, "catalog_match": None, "note": "Local full source unavailable or over scoped byte bound; primary PDF was inspected through the public arXiv tool."})
    source_checks.append(row)
state["primary_source"]["local_hash_checks"] = source_checks
state["primary_source"]["source_hash_check"] = "complete local check recorded; mathematical correctness is a separate question"

peer_path = Path("~/brain_workers/w496/AUDIT_w495.jsonl")
peer_raw = peer_path.read_bytes()
peer_rows = [json.loads(line) for line in peer_raw.decode("utf-8").splitlines() if line.strip()]
peer_rows = [r for r in peer_rows if r.get("subject") in {"w495-L0", "w495-S1"}]
receipt = {"path": str(peer_path).replace("\\", "/"), "sha256": hashlib.sha256(peer_raw).hexdigest(), "rows": peer_rows,
           "gate_note": "Scoped peer KEEP receipts only; author/referee served-model and different-login evidence are not supplied; no parent solved or theorem promotion."}
proof_audit_path = Path("~/brain_workers/w496/AUDIT_W495_PROOF.md")
proof_audit_raw = proof_audit_path.read_bytes()
proof_audit_text = proof_audit_raw.decode("utf-8")
assert "Verdict: KEEP as a graph-family obstruction" in proof_audit_text
assert "not a certified different-model or different-login proof gate" in proof_audit_text
receipt["full_proof_audit"] = {"auditor": "w496", "path": str(proof_audit_path).replace("\\", "/"),
    "sha256": hashlib.sha256(proof_audit_raw).hexdigest(), "subjects": ["w495-L1", "w495-L2", "w495-L3", "w495-L4", "w495-L5"],
    "verdict": "KEEP", "scope": "binary-tree-plus-chains graph family; sufficiently large r; beta fixed strictly positive for L5",
    "different_model_or_login_gate": "UNATTESTED", "parent_problem_proof": False}
save(ROOT / "AUDIT_RECEIPTS.json", receipt)
state["peer_review_receipts"] = [{"auditor": r["auditor"], "subject": r["subject"], "verdict": r["verdict"], "scope": r["scope"], "path": receipt["path"]} for r in peer_rows]
state["main_proof_review"] = {"referee": "w497", "status": "pending", "request_message": "msg-051c033861"}
state["adversary_proof_review"] = receipt["full_proof_audit"]
state["brain_pipeline_reviewed_meaning"] = "Full inbox bundle/model-login gate is not certified; scoped adversary KEEP receipts are recorded separately."
state["resource_gate_receipt"] = "MEASUREMENTS.json; numerical controls skipped, 76 artifact checks passed"
save(state_path, state)

claims_path = ROOT / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claims_path.read_text(encoding="utf-8").splitlines() if line.strip()]
for claim in claims:
    claim["independent_reviewer"] = "w496 scoped KEEP received; named referee w497 pending"
    claim["review_status"] = "Scoped mathematical/source KEEP by w496; different-model/login gate unattested; named referee pending"
    claim["review_evidence"] = receipt["path"] if claim["id"] in {"w495-L0", "w495-S1"} else receipt["full_proof_audit"]["path"]
claims_path.write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in claims), encoding="utf-8")

names = ["APPROACH_PRECOMMIT.md", "STATEMENT.md", "SOURCE_STATUS.json", "ATTEMPT.md", "GAP.md", "CLAIMS.jsonl", "REVIEW_PACKET.md", "REPORT.md", "MEASUREMENTS.json", "AUDIT_RECEIPTS.json", "bundle_001.json", "patches/01_C0120_source_scope.diff", "hooks/math-w495.jsonl", "prepare_delivery.py", "validate_packet.py", "finalize_receipts.py"]
hashes = []
for name in names:
    path = ROOT / name
    raw = path.read_bytes()
    hashes.append({"path": str(path).replace("\\", "/"), "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})
save(ROOT / "HASHES.json", {"purpose": "Review packet byte identity; not an integrator source manifest or mathematical proof receipt", "files": hashes})
attempt_hash = next(h["sha256"] for h in hashes if h["path"].endswith("/ATTEMPT.md"))
bundle_hash = next(h["sha256"] for h in hashes if h["path"].endswith("/bundle_001.json"))
body = (
    "C0120 independent packet: ~/brain_workers/w495/REVIEW_PACKET.md; "
    "ATTEMPT.md sha256=" + attempt_hash + "; full paths/hashes in HASHES.json. "
    "DRAFT inbox ~/math-brain-inbox/w495/bundle_001.json sha256=" + bundle_hash + ". "
    "Seven claim rows, seven draft concepts, eight relations, one source-row correction; 76 artifact checks pass, numerical controls gated. "
    "Scoped KEEP: w496 on L0/S1 and all L1-L5 (AUDIT_RECEIPTS.json); graph-family/fixed-beta scope retained. Named referee w497 pending. "
    "Hardest gap: GAP.md's fixed-lattice R_n(n^-delta)<=C n^(1-delta); the graph obstruction does not solve C0120. "
    "Current openness UNKNOWN. Author/referee response-side served-model evidence unavailable; no parent solved or theorem promotion."
)
(ROOT / "INTEGRATION_MESSAGE.txt").write_text(body + "\n", encoding="utf-8")
print(json.dumps({"attempt_sha256": attempt_hash, "bundle_sha256": bundle_hash, "peer_keep_subjects": [r["subject"] for r in peer_rows], "source_hash_checks": source_checks, "hashes_file": str(ROOT / "HASHES.json")}))
