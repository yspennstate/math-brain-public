"""Record final progress and the exact continuation, without changing proof files."""
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
from datetime import datetime, timezone

root = Path(__file__).resolve().parent
environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
delivery = json.loads((root / "INTEGRATION_DELIVERY.json").read_text(encoding="utf-8"))
if delivery.get("exit_code") != 0:
    raise SystemExit("Integration routing failed: do not record successful routing.")

commands = [
    [sys.executable, "-X", "utf8", "~/primary_directive/pd_progress.py", "--event", "P0162 w510: w511/w512 KEEP four scoped boundary proofs; reviewed bundle hash matches; routed to codex-01a12190. Served-model/account gates and ingestion unverified; corrected-gate rerun denied.", "--agent", "w510", "--row", "S1.P0162.w510", "--evidence", str(root / "HANDOFF.json")],
    [sys.executable, "-X", "utf8", "~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py", "read", "--as", "w510", "--max", "5"]
]
receipts = []
for command in commands:
    completed = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace", env=environment)
    receipt = {"command": command, "exit_code": completed.returncode, "stdout": completed.stdout, "stderr": completed.stderr}
    receipts.append(receipt)
    print(json.dumps({"tool": Path(command[3]).name, "exit_code": completed.returncode, "stdout": completed.stdout[:1300], "stderr": completed.stderr[:400]}), flush=True)

now = datetime.now(timezone.utc).isoformat()
original = [json.loads(line) for line in (root / "REVIEWED_CLAIMS_SNAPSHOT.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
current = [json.loads(line) for line in (root / "CLAIMS.jsonl").read_text(encoding="utf-8-sig").splitlines() if line.strip()]
original_by_id = {row["claim_id"]: row for row in original}
proof_fields = ["claim_id", "statement", "assumptions", "source", "proof", "scope", "novelty"]
unchanged = len(original) == len(current) and all(all(row.get(key) == original_by_id[row["claim_id"]].get(key) for key in proof_fields) for row in current)
if not unchanged:
    raise SystemExit("Review metadata update changed proof fields: preserve checkpoint and flag integration.")

checkpoint = {
    "saved_at_utc": now, "state": "NEEDS_REVIEW",
    "next": "codex-01a12190 verifies response-side served models/account separation and records audited integration; next proof step is a variance-weighted block entropy budget.",
    "mathematical_status": "w511 and w512 KEEP C001-C004 at their narrow scopes",
    "reviewed_proof_fields_unchanged": unchanged,
    "promotion_provenance": "unverified", "general_fei_proved": False,
    "corrected_gate_rerun": "pending; denied previously; no new experiment on resumption",
    "ingested": "unverified", "retrievable": "not tested",
    "integration_delivery": str(root / "INTEGRATION_DELIVERY.json"),
    "integration_message_id": json.loads(delivery["stdout"]).get("message_id"),
    "referee_notification_message_id": "msg-b0c2727c5e",
    "progress_logged": receipts[0]["exit_code"] == 0,
    "team_read_exit_code": receipts[1]["exit_code"],
    "handoff_sha256": hashlib.sha256((root / "HANDOFF.json").read_bytes()).hexdigest(),
    "receipts": receipts
}
(root / "CHECKPOINT_RECEIPT.json").write_text(json.dumps(checkpoint, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
status_path = root / "STATUS.md"
status = status_path.read_text(encoding="utf-8-sig")
status = status.replace("2.082 GB physical headroom", "2.082 GB physical memory available")
status = status.replace("w512 mathematical review remains pending.", "At the previous checkpoint, w512 mathematical review was pending; its KEEP is recorded below.")
status += f"\n{now}: Final checkpoint: reviewed proof fields unchanged; integration msg-541f477b71 and referee notification msg-b0c2727c5e saved. Progress logged={checkpoint['progress_logged']}; team read exit={checkpoint['team_read_exit_code']}. See CHECKPOINT_RECEIPT.json. No new experiment; ingestion/retrieval unverified.\n"
status_path.write_text(status, encoding="utf-8")
print(json.dumps({"checkpoint": str(root / "CHECKPOINT_RECEIPT.json"), "state": "NEEDS_REVIEW", "proof_fields_unchanged": unchanged, "progress_logged": checkpoint["progress_logged"]}), flush=True)
