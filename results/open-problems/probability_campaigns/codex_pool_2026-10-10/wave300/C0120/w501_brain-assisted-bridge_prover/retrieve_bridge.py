"""Targeted, bounded read-only card lookup. No whole-store materialization."""
import json
from pathlib import Path
import sqlite3
import time

ROOT = Path(__file__).resolve().parent
STORE = "~/math-brain-build/local/population/brain.sqlite3"
started = time.monotonic()
con = sqlite3.connect("file:"+STORE+"?mode=ro", uri=True, timeout=2)
con.execute("PRAGMA query_only=ON")
con.set_progress_handler(lambda: int(time.monotonic()-started > 15), 10000)
queries = ["%ornstein%", "%hypercontract%", "%superconcentr%", "%directed polymer%", "%C0120%"]
receipt = {"store": STORE, "mode": "ro", "deadline_seconds": 15, "queries": []}
for query in queries:
    rows = con.execute("SELECT id,kind,title FROM nodes WHERE lower(title) LIKE lower(?) LIMIT 12", (query,)).fetchall()
    receipt["queries"].append({"query": query, "returned": len(rows), "rows": rows})
receipt["elapsed_seconds"] = time.monotonic()-started
(ROOT / "retrieval_candidates.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
con.close()
print(json.dumps(receipt, ensure_ascii=False))
