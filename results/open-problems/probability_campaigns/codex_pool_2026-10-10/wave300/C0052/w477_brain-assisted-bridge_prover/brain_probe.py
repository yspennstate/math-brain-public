"""Read only named mathematical store metadata; no corpus export or writes."""
import json
import sqlite3
import time

path = "~/math-brain-build/local/population/brain.sqlite3"
started = time.perf_counter()
with sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=5) as con:
    con.execute("PRAGMA query_only=ON")
    tables = con.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE '%fts%'"
    ).fetchall()
    print(json.dumps({"tables": [row[0] for row in tables], "seconds": time.perf_counter() - started}))
    for name in ("nodes", "claims", "edges"):
        if (name,) in tables:
            print(json.dumps({"table": name, "columns": con.execute(f"PRAGMA table_info({name})").fetchall()}))
