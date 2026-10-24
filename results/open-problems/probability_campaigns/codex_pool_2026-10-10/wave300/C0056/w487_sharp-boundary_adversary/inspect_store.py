"""Read only schema for named tables, then bounded exact Anderson matches."""
import json
import sqlite3
from pathlib import Path

path = Path(r"~\math-brain-build\local\population\brain.sqlite3")
con = sqlite3.connect(path.as_uri()+"?mode=ro", uri=True, timeout=2)
con.execute("PRAGMA query_only=ON")
for table in ("nodes", "claims"):
    fields = con.execute(f"PRAGMA table_info({table})").fetchall()
    print(table, json.dumps(fields))
con.close()
