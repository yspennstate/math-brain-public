"""Named-peer handoff using team_comm's existing offline-recipient fallback."""
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

os.environ["PYTHONDONTWRITEBYTECODE"] = "1"
sys.dont_write_bytecode = True
sys.path.insert(0, "~/<private-repo>/12_cognitive_architecture/agent_mesh")
import team_comm

base = Path(__file__).resolve().parent
mesh = team_comm.Mesh(team_comm.DB, busy_timeout_ms=20000)
try:
    team_comm.ensure(mesh, "w354")
    # Exactly the recipient fallback already implemented by team_comm.cmd_say.
    # This registers a mailbox for an existing named peer; it starts no process.
    team_comm.ensure(mesh, "w356")
    body = "Full P0017 proof packet: ~/brain_workers/w354/SIMPLEX_PROOF.md and CLAIMS.jsonl (001-004). Exact isotropic simplex orthogonal fibers; optimal directional conditional constant; smooth triangle witness variance=1/2, directional energy=1/3, full energy=13/27. Independent raw monomial receipt POLYNOMIAL_CHECK.json. Adversary w355 received STATEMENT.md first. Please return claim-by-claim KEEP/FIX, especially conditioning, positive-mass fibers and full-gradient distinction. No full KLS or novelty claim."
    result = mesh.send("w354", "w356", "P0017-sharp-boundary/referee", body, kind="request")
    team_comm.ring("w356")
finally:
    mesh.close()
receipt = {"sent_at": datetime.now(timezone.utc).isoformat(), "recipient": "w356", "statement_first_recipient": "w355", "statement_first_message_id": "msg-d2d8a72760", "method": "existing team_comm.ensure and mesh.send; no team campaign existed", "recipient_registration": "mailbox metadata only; no process started", "result": result, "mathematical_review_received": False}
(base / "REVIEW_HANDOFF.json").write_text(json.dumps(receipt, indent=2, default=str), encoding="utf-8")
print(json.dumps(receipt, indent=2, default=str))
