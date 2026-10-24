"""Bounded read-only schema/card probe; no model or whole-store export."""
import json
import sqlite3
import time
from pathlib import Path

root = Path(__file__).resolve().parent
db = Path("~/math-brain-build/local/population/brain.sqlite3")
start = time.monotonic()
result = {"database": str(db), "mode": "read-only", "command": "python -X utf8 brain_probe.py"}
con = sqlite3.connect(db.as_uri() + "?mode=ro", uri=True, timeout=5)
con.row_factory = sqlite3.Row
con.execute("PRAGMA query_only=ON")
con.set_progress_handler(lambda: int(time.monotonic() - start > 10), 1000)
tables = [row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
result["table_names"] = tables
for table in ("nodes", "current_nodes", "node_revisions", "claims"):
    if table in tables:
        result[table + "_schema"] = [dict(row) for row in con.execute('PRAGMA table_info("' + table + '")')]
result["elapsed_seconds"] = time.monotonic() - start
con.close()
(root / "brain_schema.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
