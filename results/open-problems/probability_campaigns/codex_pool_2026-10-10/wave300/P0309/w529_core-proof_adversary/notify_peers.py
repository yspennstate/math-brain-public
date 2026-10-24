"""Task-authorized direct messages to the assigned prover and referee only."""
import json
import subprocess
import sys
from pathlib import Path

folder = Path(__file__).resolve().parent
mesh = "~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py"
sys.path.insert(0, str(Path(mesh).parent))
import team_comm

# This is the installed team_comm recovery for an unregistered named worker;
# it registers metadata and does not start an agent or process.
team_comm.ensure(team_comm.mesh(), "w530")
messages = [
    ("w528", "claim", "P0309 actual L1-L6 proof audited: KEEP scoped auxiliaries; G remains open. C7 is a smooth-map sufficient case of your L6; C6 refutes only dropping its entropy premise. C1-C3 preceded your statement, C6-C8 preceded your actual proof. ~/brain_workers/w529/CORE_AUDIT.md and PEER_VERDICT.jsonl. The DRAFT keeps the unrestricted repair/phase/DLR gaps explicit."),
    ("w530", "review", "P0309 review packet ready at ~/brain_workers/w529/CORE_AUDIT.md, ATTEMPT.md, ADDITIONAL_LEMMAS.md and CLAIMS.jsonl. Your C1 KEEP recorded. Please check new C2-C8, prioritizing C6 entropy counterexample, C7 repair Jacobian bound, C8 null rigid repair image. 2665 finite checks passed; full G and target remain unproved. Pending results stay DRAFT concepts."),
]
receipt_path = folder / "COORDINATION_RECEIPTS.json"
receipts = json.loads(receipt_path.read_text(encoding="utf-8")) if receipt_path.exists() else []
for peer, kind, body in messages:
    args = ["python", "-X", "utf8", mesh, "send", "--agent", "w529", "--to", peer, "--topic", "P0309/" + kind, "--kind", "message", "--body", body, "--idempotency-key", "p0309-w529-core-audit-" + peer + "-v2"]
    try:
        result = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=60)
        receipt = {"peer": peer, "kind": kind, "returncode": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
    except subprocess.TimeoutExpired:
        receipt = {"peer": peer, "kind": kind, "status": "timeout; delivery unknown; idempotency key retained"}
    receipts.append(receipt)
    (folder / "COORDINATION_RECEIPTS.json").write_text(json.dumps(receipts, indent=2), encoding="utf-8")
    print(json.dumps(receipt), flush=True)
