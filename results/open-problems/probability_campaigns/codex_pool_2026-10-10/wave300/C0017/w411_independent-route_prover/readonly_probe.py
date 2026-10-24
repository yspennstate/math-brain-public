"""Narrow schema and team lookup; always read-only, no exports."""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
paths = {
    "mesh": Path("~/.agents/coordination/agent_mesh.sqlite3"),
    "population": Path("~/math-brain-build/local/population/brain.sqlite3"),
}
result = {}
for name, path in paths.items():
    if not path.is_file():
        result[name] = {"exists": False}
        continue
    with sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=2) as conn:
        conn.execute("PRAGMA query_only=ON")
        if name == "mesh":
            result[name] = {
                "agents": conn.execute(
                    "SELECT a.agent_id,a.campaign_id,c.name FROM agents a "
                    "LEFT JOIN campaigns c ON c.campaign_id=a.campaign_id "
                    "WHERE a.agent_id IN ('w411','w412','w413')"
                ).fetchall()
            }
        else:
            result[name] = {
                "schema": conn.execute(
                    "SELECT name,sql FROM sqlite_master WHERE type='table' "
                    "AND name IN ('nodes','claims','claim_provenance')"
                ).fetchall()
            }
(ROOT / "READONLY_SCHEMA.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
