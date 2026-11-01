import json
import sqlite3
import time
from pathlib import Path

root = Path(__file__).resolve().parent
out = {}
mesh = sqlite3.connect("file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro", uri=True, timeout=3)
try:
    out["math_campaigns"] = mesh.execute("SELECT campaign_id,name FROM campaigns WHERE lower(name) LIKE '%probability%' OR lower(name) LIKE '%w0300%' OR lower(name) LIKE '%p0162%' LIMIT 12").fetchall()
except Exception as exc:
    out["mesh_error"] = str(exc)
finally:
    mesh.close()

c = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True, timeout=3)
try:
    ids = ["claim_d7e82bff88909352dff2f23bfcaf7a76446d6bfd14af38c5bda1d5efeb9d9c06",
           "claim_06b0c09db7e28efc6febd3962e234332a00c2ba45a17792cc4d83fdbc6752fba",
           "claim_d15d0160e58b4c9183707be9f49462d2"]
    out["cited_store_cards"] = []
    for claim_id in ids:
        row = c.execute("SELECT n.title,n.body,n.metadata_json,c.payload_json FROM nodes n JOIN claims c ON c.id=n.id WHERE n.id=?", (claim_id,)).fetchone()
        if row:
            payload = json.loads(row[3])
            out["cited_store_cards"].append({"id": claim_id, "title": row[0], "body": row[1],
                "metadata": json.loads(row[2]), "payload": payload})
except Exception as exc:
    out["store_error"] = str(exc)
finally:
    c.close()

out["core_lane_method_excerpts"] = {}
for worker in ("w504", "w505"):
    path = Path("~/brain_workers") / worker / "ATTEMPT.md"
    if path.exists():
        lines = path.read_text(encoding="utf-8-sig").splitlines()
        # Only the introduction/method boundary, after w507's method precommit.
        out["core_lane_method_excerpts"][worker] = "\n".join(lines[:70])

out["team_comm_selected_code"] = {}
path = Path("~/<private-repo>/12_cognitive_architecture/agent_mesh/team_comm.py")
lines = path.read_text(encoding="utf-8-sig").splitlines()
for start, end in ((81, 115), (241, 264)):
    out["team_comm_selected_code"][str(start)] = "\n".join(lines[start-1:end])
(root / "NARROW_SOURCE_READS.json").write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print("math_campaigns", json.dumps(out.get("math_campaigns", out.get("mesh_error"))))
for card in out.get("cited_store_cards", []):
    print("CARD", card["id"], card["title"])
    print("PAYLOAD", json.dumps(card["payload"], ensure_ascii=False)[:10000])
for worker, excerpt in out["core_lane_method_excerpts"].items():
    print("CORE_METHOD", worker, excerpt)
print("TEAM_CODE", json.dumps(out["team_comm_selected_code"]))
