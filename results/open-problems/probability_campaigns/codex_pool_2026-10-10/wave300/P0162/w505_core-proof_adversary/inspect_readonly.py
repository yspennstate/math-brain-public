"""Narrow read-only checks of peer coordination and FEI cards; no table exports."""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
def connect(path):
    db = sqlite3.connect("file:" + path.as_posix() + "?mode=ro", uri=True, timeout=3)
    db.row_factory = sqlite3.Row
    db.execute("PRAGMA query_only=ON")
    return db

out = {}
mesh_path = Path("~/.agents/coordination/agent_mesh.sqlite3")
if mesh_path.exists():
    with connect(mesh_path) as db:
        names = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' AND (name LIKE '%claim%' OR name LIKE '%message%' OR name='agents')")]
        mesh = {"path": str(mesh_path), "mode": "ro", "tables": names}
        for table in names:
            cols = [r[1] for r in db.execute('PRAGMA table_info("'+table+'")')]
            mesh[table+"_columns"] = cols
            if "claim" in table:
                agent_col = next((c for c in ["agent_id", "owner_agent", "owner_agent_id"] if c in cols), None)
                if agent_col:
                    rows = [dict(r) for r in db.execute('SELECT * FROM "'+table+'" WHERE "'+agent_col+'" IN (?,?,?) LIMIT 12', ("w504", "w505", "w506"))]
                    mesh[table+"_peer_rows"] = rows
            if "message" in table:
                to_col = next((c for c in ["recipient", "recipient_agent", "recipient_agent_id", "to_agent", "to_agent_id"] if c in cols), None)
                order_col = next((c for c in ["created_at", "message_id", "id"] if c in cols), None)
                if to_col:
                    order = ' ORDER BY "'+order_col+'" DESC' if order_col else ''
                    rows = [dict(r) for r in db.execute('SELECT * FROM "'+table+'" WHERE "'+to_col+'"=?'+order+' LIMIT 6', ("w505",))]
                    mesh[table+"_worker_rows"] = rows
        out["mesh"] = mesh

brain_path = Path("~/math-brain-build/local/population/brain.sqlite3")
if brain_path.exists():
    with connect(brain_path) as db:
        names = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('cards','nodes','math_nodes')")]
        brain = {"path": str(brain_path), "mode": "ro", "tables": names}
        for table in names:
            cols = [r[1] for r in db.execute('PRAGMA table_info("'+table+'")')]
            brain[table+"_columns"] = cols
            title_col = next((c for c in ["title", "name", "logical_name"] if c in cols), None)
            if title_col:
                wanted = [c for c in ["id", "card_id", "namespace", "logical_name", "title", "kind", "statement", "source_id"] if c in cols]
                query = 'SELECT '+','.join('"'+c+'"' for c in wanted)+' FROM "'+table+'" WHERE lower("'+title_col+'") LIKE ? AND lower("'+title_col+'") LIKE ? LIMIT 6'
                rows = [dict(r) for r in db.execute(query, ("%entropy%", "%influence%"))]
                for row in rows:
                    for k, v in list(row.items()):
                        if isinstance(v, str) and len(v)>1600:
                            row[k] = v[:1600]+" [bounded excerpt]"
                brain[table+"_fei_rows"] = rows
        out["brain"] = brain
        if "nodes" in names:
            wanted_ids = ["claim_d7e82bff88909352dff2f23bfcaf7a76446d6bfd14af38c5bda1d5efeb9d9c06",
                          "claim_06b0c09db7e28efc6febd3962e234332a00c2ba45a17792cc4d83fdbc6752fba",
                          "claim_d15d0160e58b4c9183707be9f49462d2"]
            brain["named_target_nodes"] = [dict(r) for r in db.execute(
                "SELECT id,kind,title,substr(body,1,6000) AS body_excerpt,substr(metadata_json,1,2000) AS metadata_excerpt FROM nodes WHERE id IN (?,?,?)", wanted_ids)]
(ROOT/"READONLY_CONTEXT.json").write_text(json.dumps(out, indent=2)+"\n", encoding="utf-8")
print(json.dumps(out, indent=2))
