import json
import sqlite3
from pathlib import Path

path = Path("~/math-brain-build/local/population/brain.sqlite3")
con = sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True, timeout=5)
con.execute("PRAGMA query_only=ON")
rows = con.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND (name LIKE '%node%' OR name LIKE '%card%' OR name LIKE '%entry%' OR name LIKE '%edge%' OR name LIKE '%fts%')").fetchall()
for name, sql in rows:
    print(json.dumps({"table": name, "schema": sql}, ensure_ascii=False))
con.close()
