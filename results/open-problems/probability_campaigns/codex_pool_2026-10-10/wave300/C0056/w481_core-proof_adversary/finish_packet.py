"""Finish the authorized packet, with bounded foreground communication only."""
from pathlib import Path
import json
import runpy
import subprocess
import sys

root = Path(__file__).resolve().parent
runpy.run_path(str(root / "submit_draft.py"), run_name="__main__")
# Refresh local review hashes after the submission-state update.
runpy.run_path(str(root / "prepare_packet.py"), run_name="__main__")

hashes = json.loads((root / "REVIEW_HASHES.json").read_text(encoding="utf-8"))["files"]
verdict_sha = next(h["sha256"] for h in hashes if h["path"].endswith("VERDICT_W480.md"))
peer_sha = next(h["sha256"] for h in hashes if h["path"].replace("\\", "/").endswith("w480/ATTEMPT.md"))
mesh = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
body = (
    "C0056 w481 review-ready packet: ~/brain_workers/w481/REVIEW_PACKET.md; "
    "CLAIMS.jsonl (7 rows), VERDICT_W480.md sha256=" + verdict_sha + "; paired ATTEMPT.md sha256=" + peer_sha + ". "
    "Scoped KEEP L1/L2/L3 finite-volume theorem/L4/L5; FIX only L3 necessity of successive limits, explicit witness JOINT_LIMIT_COUNTEREXAMPLE.md. "
    "DRAFT ~/math-brain-inbox/w481/bundle_001.json has 4 concept/definition cards and 4 supported relations, including existing C0056. "
    "LG and GOE unproved; w482 review pending. Author/referee response-side served-model evidence unavailable; requested settings are not evidence. "
    "Submitted DRAFT, not reviewed/ingested/retrievable by this worker; no parent solved or theorem promotion. "
    "Local hook staged in HOOK_PROPOSAL.jsonl for coordinator routing."
)
commands = [
    ("integration_handoff", [sys.executable, "-X", "utf8", mesh, "send", "--agent", "w481", "--to", "codex-01a12190",
                             "--topic", "probability300-integration", "--kind", "message", "--body", body,
                             "--idempotency-key", "w481-C0056-final-20261010", "--fire-once"]),
    ("progress", [sys.executable, "-X", "utf8", "~/primary_directive/pd_progress.py", "--event",
                  "C0056 w481: adversarial KEEP/FIX packet, 7 claim rows and 4 DRAFT cards/4 supported relations saved; LG and GOE still unproved",
                  "--agent", "w481", "--row", "S1.C0056", "--evidence", str(root / "REVIEW_PACKET.md")]),
    ("team_read", [sys.executable, "-X", "utf8", "~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py",
                   "read", "--as", "w481"])
]
receipts = {}
for label, command in commands:
    result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", errors="replace")
    receipts[label] = {"returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    print(label + ": " + json.dumps(receipts[label], ensure_ascii=False), flush=True)
    (root / "HANDOFF_RECEIPTS.json").write_text(json.dumps(receipts, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")

status_path = root / "STATUS.md"
old_lines = status_path.read_text(encoding="utf-8-sig").splitlines()
new_status = ["STATE: NEEDS_REVIEW", "NEXT: w482 checks the joint-limit witness and independent reductions; w480 fixes the scope sentence and attacks fixed-lambda infinite-volume LG."]
new_status += [line for line in old_lines[2:] if line]
new_status += ["2026-10-10: Deliverables complete: 7 claim rows, 4 DRAFT cards and 4 supported relations validated by 11 structural/exact-witness checks; validator 0.012 s, read-only target query 0.061 s. DRAFT atomically staged in the authorized inbox; independent review, served-model provenance, ingestion and retrieval not confirmed. No parent solution."]
status_path.write_text("\n".join(new_status)+"\n", encoding="utf-8")
print("STATE: NEEDS_REVIEW", flush=True)
