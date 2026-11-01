"""Targeted read-only receipts. Never use the mesh constructor: it writes."""
import json
from pathlib import Path
import sqlite3
import time

root = Path(__file__).resolve().parent
db = Path("~/.agents/coordination/agent_mesh.sqlite3")
receipt = {"started": time.strftime("%Y-%m-%d %H:%M:%S"), "database_mode": "ro", "messages": []}
if db.is_file():
    with sqlite3.connect(db.as_uri() + "?mode=ro", uri=True, timeout=3) as conn:
        conn.execute("PRAGMA query_only=ON")
        conn.row_factory = sqlite3.Row
        receipt["messages"] = [dict(r) for r in conn.execute(
            "SELECT sender_agent,recipient,topic,kind,body,created_at FROM messages WHERE recipient=? AND (delivered_at IS NULL OR (requires_ack=1 AND acked_at IS NULL)) ORDER BY rowid LIMIT 8", ("w373",))]
        receipt["peer_claims"] = [dict(r) for r in conn.execute(
            "SELECT sender_agent,recipient,topic,kind,body,created_at FROM messages WHERE sender_agent IN (?,?,?) AND kind IN ('claim','done','found') ORDER BY rowid DESC LIMIT 9", ("w372", "w374", "w377"))]
else:
    receipt["mesh_status"] = "not found"
(root / "team_read_receipt.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False, indent=2))

research = Path("~/<private-repo>/06_math_research")
intake = research / "probability_1000_intake_claude_20260907"
bundle = json.loads((intake / "brain_bundle_C006p01.json").read_text(encoding="utf-8"))
entries = bundle["entries"]
target = [row for row in entries if row.get("key") == "op-p0110"]
(root / "intake_target_receipt.json").write_text(json.dumps(target, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(target, ensure_ascii=False, indent=2))
