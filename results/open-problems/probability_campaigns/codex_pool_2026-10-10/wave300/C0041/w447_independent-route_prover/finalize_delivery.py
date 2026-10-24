"""Record scoped peer review, freeze the packet, and finish the worker checkpoint."""
import hashlib
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parent
stamp = datetime.now(timezone.utc).isoformat()
state_file = root / "SUBMISSION_STATE.json"
state = json.loads(state_file.read_text(encoding="utf-8"))
assert state["submitted"] and state["referee_handoff_sent"] and state["integration_contact_handoff_sent"]
hash_file = root / "REVIEW_FILE_HASHES.json"
hashes = json.loads(hash_file.read_text(encoding="utf-8"))
for name, expected in hashes.items():
    assert hashlib.sha256((root / name).read_bytes()).hexdigest() == expected, name
assert (root / "drafts/bundle_001.json").read_bytes() == Path(state["bundle_submission_path"]).read_bytes()
assert json.loads((root / "PATCH_CHECK.json").read_text(encoding="utf-8"))["passed"]

audit_path = Path("~/brain_workers/w448/AUDIT.jsonl")
audit_rows = [json.loads(line) for line in audit_path.read_text(encoding="utf-8").splitlines() if line.strip()]
receipt_rows = [row for row in audit_rows if row.get("id", "").startswith("w448-audit-w447-")]
assert {row["id"].rsplit("-", 1)[-1] for row in receipt_rows} == {"ER", "FV", "CC", "GO"}
assert all(row["verdict"] == "KEEP" and row["parent_problem_keep"] is False for row in receipt_rows)
receipt = {"received_on": stamp, "reviewer": "w448", "source": str(audit_path),
           "source_sha256": hashlib.sha256(audit_path.read_bytes()).hexdigest(), "scoped_keeps": receipt_rows,
           "required_referee": "w449 (pending)", "reviewer_served_model_evidence": "unavailable",
           "different_model_gate_satisfied": False, "parent_problem_keep": False,
           "scope_note": "Record only the displayed scopes. No byte-frozen proof/audit hash binding or served-model receipt was supplied."}
(root / "PEER_KEEP_RECEIPT.json").write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
claim_file = root / "CLAIMS.jsonl"
claims = [json.loads(line) for line in claim_file.read_text(encoding="utf-8").splitlines() if line.strip()]
for claim in claims:
    label = claim["claim_id"].rsplit("-", 1)[-1]
    if label in {"ER", "FV", "CC", "GO"}:
        verdict = next(row for row in receipt_rows if row["id"].endswith("-" + label))
        claim["independent_reviewer"] = "w448 scoped KEEP; assigned referee w449 pending"
        claim["scoped_review_receipt"] = {"path": str(audit_path), "id": verdict["id"], "scope": verdict["scope"]}
        claim["status"] = "proved special case"  # required review/model gate still pending
claim_file.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in claims), encoding="utf-8")
source_status_file = root / "SOURCE_STATUS.json"
source_status = json.loads(source_status_file.read_text(encoding="utf-8"))
source_status["review_state"] = "w448 scoped KEEP of ER/FV/CC/GO received; assigned w449 and source-status reviews pending"
source_status["peer_keep_receipt"] = str(root / "PEER_KEEP_RECEIPT.json")
source_status_file.write_text(json.dumps(source_status, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

report_file = root / "REPORT.md"
report = report_file.read_text(encoding="utf-8").replace("After: 4, independently kept: 0.",
    "After: 4 author proofs. One peer, w448, returned scoped KEEP on ER/FV/CC/GO; the required w449 and served-model gates remain pending.")
report_file.write_text(report + "\nPeer review receipt: PEER_KEEP_RECEIPT.json quotes the exact four kept scopes from w448/AUDIT.jsonl. No parent keep, source-status keep, fixed-byte audit binding, or different-model receipt was supplied. Claim statuses remain author proved special case pending the assigned review.\n", encoding="utf-8")
packet_file = root / "REVIEW_PACKET.md"
packet = packet_file.read_text(encoding="utf-8").replace(
    "No independent keep, ingestion or retrieval receipt exists.",
    "The required-referee, ingestion and retrieval receipts remain pending.")
packet += "\nScoped peer review received: w448 KEEP of ER/FV/CC/GO, recorded with each exact scope in PEER_KEEP_RECEIPT.json. No parent keep or source-status keep. Required w449 review, byte-frozen audit binding and actual served-model evidence remain pending; do not treat this as a satisfied integration gate. The mathematical proof texts and published bundle remain unchanged.\n"
packet_file.write_text(packet, encoding="utf-8")
checks_file = root / "ARTIFACT_CHECK.json"
checks = json.loads(checks_file.read_text(encoding="utf-8"))
checks.update({"independent_keeps": 4, "scoped_peer_reviewer": "w448", "required_referee_keeps": 0,
               "served_model_gate_satisfied": False})
checks_file.write_text(json.dumps(checks, indent=2) + "\n", encoding="utf-8")
hashes["PEER_KEEP_RECEIPT.json"] = ""
hashes["ARTIFACT_CHECK.json"] = ""
hashes = {name: hashlib.sha256((root / name).read_bytes()).hexdigest() for name in hashes}
hash_file.write_text(json.dumps(hashes, indent=2) + "\n", encoding="utf-8")
sha = hashes["REVIEW_PACKET.md"]

mesh = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
confirmations = []
for recipient in ("w449", "codex-01a12190"):
    body = (f"Frozen final w447 packet: ~/brain_workers/w447/REVIEW_PACKET.md SHA256 {sha}; "
            "REVIEW_FILE_HASHES.json records current file hashes, including isolated patch check. "
            "Peer w448 scoped KEEP ER/FV/CC/GO received; exact scopes in PEER_KEEP_RECEIPT.json. "
            "Assigned w449/source-status reviews and served-model/byte-binding gates pending. "
            "Six-entry DRAFT already submitted, ingestion/retrieval unconfirmed. Parent not proved; "
            "single gap E[K_tau|no-backtracking]<infinity. Four scoped keeps are not a parent or integration keep.")
    sent = subprocess.run(["python", "-X", "utf8", mesh, "send", "--agent", "w447", "--to", recipient,
                           "--topic", "C0041-final-packet", "--kind", "message", "--body", body],
                          capture_output=True, text=True, encoding="utf-8", timeout=60)
    record = {"to": recipient, "packet_sha256": sha, "returncode": sent.returncode, "stdout": sent.stdout,
              "stderr": sent.stderr, "at_utc": datetime.now(timezone.utc).isoformat()}
    with (root / "FINAL_HANDOFF_RECEIPTS.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(record) + "\n")
    if sent.returncode:
        raise RuntimeError(json.dumps(record))
    confirmations.append({"to": recipient, "message_id": json.loads(sent.stdout)["message_id"], "packet_sha256": sha})
    print(json.dumps(confirmations[-1]), flush=True)

state.update({"reviewed": True, "review_scope": "w448 peer scopes only; required w449 review pending",
              "independent_keeps": receipt_rows, "required_referee_reviewed": False,
              "ingested": False, "retrievable": False, "ingestion_receipt": None, "retrieval_receipt": None,
              "served_model_gate_satisfied": False, "byte_frozen_audit_binding_received": False,
              "parent_problem_solved_claim": False, "final_packet_sha256": sha, "final_handoffs": confirmations})
state_file.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
result = {"passed": True, "at_utc": datetime.now(timezone.utc).isoformat(), "file_hashes_checked": len(hashes),
          "draft_mirror_matches": True, "scoped_peer_keeps": 4, "required_referee_keeps": 0,
          "target_proved": False, "current_openness": "UNKNOWN", "final_packet_sha256": sha,
          "submitted": True, "reviewed": "scoped peer only", "ingested_confirmed": False, "retrievable_confirmed": False}
(root / "FINAL_CHECK.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
status = """STATE: NEEDS_REVIEW
NEXT: w449 audits CC's precise clock/count estimate and ER/FV/GO scopes plus source-status corrections; the next proof step is fixed-law E[K_tau|no-backtracking]<infinity, including repeated returns.

2026-10-10: Exact C0041 target/source recovered; current openness UNKNOWN after finding a new primary solution claim. No parent proof or novelty claim. Independent escape-geometry/count route committed before peer proofs.
2026-10-10: ER/FV/CC/GO complete author proofs saved; single remaining conditional exit-count moment explicit. Exact checks passed: 15 kernels, 300 statewise tails, 60 returns, 32 moment constants, 64 anticipative outcomes, 0.074186 seconds with a fresh gate.
2026-10-10: Source correction checked/applied to an isolated fixture: 1 changed row, 0 live edits. Six-entry/five-relation DRAFT published under clm-f47ca6b0d8 at ~/math-brain-inbox/w447/bundle_001.json. Two canonical-node status annotations and two local hook proposals prepared.
2026-10-10: Statement sent first to w448; complete and frozen packets sent to w449 and codex-01a12190. w448 scoped KEEP ER/FV/CC/GO recorded in PEER_KEEP_RECEIPT.json; required referee/source-status reviews, served-model evidence and byte-frozen audit binding remain pending. Ingestion/retrieval unconfirmed. No live store or recall controls changed by w447.
"""
(root / "STATUS.md").write_text(status, encoding="utf-8")
progress = subprocess.run(["python", "-X", "utf8", "~/primary_directive/pd_progress.py",
                          "--event", "C0041 w447 NEEDS_REVIEW: 4 scoped peer keeps from w448; exact checks and one-row isolated patch pass; frozen packet with w449/integration contact; parent unproved, exit-count moment gap.",
                          "--agent", "w447", "--row", "S1.C0041", "--evidence", str(root / "REVIEW_PACKET.md")],
                         capture_output=True, text=True, encoding="utf-8", timeout=60)
(root / "FINAL_PROGRESS_RECEIPT.json").write_text(json.dumps({"returncode": progress.returncode,
    "stdout": progress.stdout, "stderr": progress.stderr}, indent=2) + "\n", encoding="utf-8")
assert progress.returncode == 0
print(json.dumps(result, indent=2), flush=True)
