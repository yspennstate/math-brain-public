"""Bounded read-only lookup of precisely C0052 logical IDs."""
import json
import sqlite3
import time
from pathlib import Path

started = time.perf_counter()
path = "~/math-brain-build/local/population/brain.sqlite3"
with sqlite3.connect(f"file:{path}?mode=ro", uri=True, timeout=5) as con:
    con.execute("PRAGMA query_only=ON")
    con.set_progress_handler(lambda: int(time.perf_counter() - started > 10), 1000)
    rows = con.execute(
        "SELECT id,title,body,metadata_json FROM nodes "
        "WHERE lower(json_extract(metadata_json,'$.logical_id')) LIKE ? LIMIT 5",
        ("math:probability.statmech:%c0052-%",),
    ).fetchall()
result = {"source": path, "read_only": True, "seconds": time.perf_counter() - started,
          "exact_problem_hits": len(rows),
          "rows": [{"id": r[0], "title": r[1], "body": r[2], "metadata": json.loads(r[3])} for r in rows]}
Path(__file__).with_name("STORE_LOOKUP.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2))
