"""Inspect only relevant metadata using a read-only connection and a finite query cap."""
import json
import sqlite3
import time
from pathlib import Path

root = Path(__file__).resolve().parent
path = Path("~/math-brain-build/local/population/brain.sqlite3")
started = time.perf_counter()
with sqlite3.connect(path.as_uri()+"?mode=ro", uri=True, timeout=5) as conn:
    conn.execute("PRAGMA query_only=ON")
    conn.execute("PRAGMA busy_timeout=5000")
    conn.set_progress_handler(lambda: int(time.perf_counter()-started > 25), 2000)
    tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    schema = {}
    for (name,) in tables:
        if any(s in name.lower() for s in ("node", "card", "source", "edge")) and "fts" not in name:
            schema[name] = conn.execute('PRAGMA table_info("'+name.replace('"','""')+'")').fetchall()
    receipt = {"store": str(path), "access": "mode=ro; query_only=ON", "tables": tables,
               "selected_schema": schema, "elapsed_seconds": time.perf_counter()-started}
(root/"store_schema.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
