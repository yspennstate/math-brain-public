"""Use the existing supported mesh API only for explicitly authorised peers."""
import json
from pathlib import Path
import sys

sys.path.insert(0, "~/<private-repo>/12_cognitive_architecture/agent_mesh")
import team_comm

root = Path(__file__).resolve().parent
recipient, kind, message = sys.argv[1:4]
if recipient not in {"w489", "w491", "codex-01a12190"}:
    raise SystemExit("Recipient outside this task's authorised peer list")
receipt = {"recipient": recipient, "kind": kind, "body": message, "delivered": False}
try:
    mesh = team_comm.Mesh(team_comm.DB, busy_timeout_ms=15000)
    team_comm.ensure(mesh, "w490")
    result = mesh.send("w490", recipient, "probability300-C0056/" + kind, message[:600], kind=team_comm.KINDS[kind])
    team_comm.ring(recipient)
    receipt.update(delivered=True, result=result)
except Exception as error:
    receipt["error"] = str(error)
with (root / "mesh_receipts.jsonl").open("a", encoding="utf-8") as handle:
    handle.write(json.dumps(receipt, ensure_ascii=False, default=str) + "\n")
print(json.dumps(receipt, ensure_ascii=False, default=str))
