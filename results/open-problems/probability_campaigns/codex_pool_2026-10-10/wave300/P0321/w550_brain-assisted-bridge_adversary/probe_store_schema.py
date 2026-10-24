"""A bounded metadata query; never construct or modify a database."""
import json
import pathlib
import sqlite3
import time

root = pathlib.Path(__file__).resolve().parent
database = pathlib.Path("~/math-brain-build/local/population/brain.sqlite3")
t0 = time.perf_counter()
out = {"database": str(database), "read_only": True, "gate": "compute_gate.json"}
if not database.is_file():
    out["error"] = "database does not exist"
else:
    try:
        with sqlite3.connect(database.as_uri()+"?mode=ro", uri=True, timeout=1) as con:
            con.execute("PRAGMA query_only=ON")
            con.set_progress_handler(lambda: int(time.perf_counter()-t0>3), 500)
            out["tables"] = [dict(zip(["name", "sql"], r)) for r in con.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name LIMIT 18")]
    except sqlite3.Error as e:
        out["error"] = str(e)
out["seconds"] = time.perf_counter()-t0
(root/"store_schema_receipt.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out))
