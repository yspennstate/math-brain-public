"""Read a maximum of four directly relevant percolation cards, read-only."""
from pathlib import Path
import json
import sqlite3
import sys
import time

ROOT = Path(__file__).resolve().parent
canonical = len(sys.argv)>1 and sys.argv[1] == "canonical"
store = "~/math-research-brain/local/population/brain.sqlite3" if canonical else "~/math-brain-build/local/population/brain.sqlite3"
con = sqlite3.connect("file:"+store+"?mode=ro", uri=True, timeout=5)
start = time.monotonic()
con.set_progress_handler(lambda: int(time.monotonic()-start > 5), 10000)
rows = con.execute("SELECT id,kind,title,body FROM nodes WHERE title LIKE '%critical%' AND (body LIKE '%quasi-transitive%' OR title LIKE '%quasi-transitive%') LIMIT 4").fetchall()
con.close()
result = []
for identifier, kind, title, body in rows:
    try:
        parsed = json.loads(body)
    except (json.JSONDecodeError, TypeError):
        parsed = body
    result.append({"id": identifier, "kind": kind, "title": title, "body": parsed})
(ROOT / ("CANONICAL_SOURCE_ROWS.json" if canonical else "STORE_SOURCE_ROWS.json")).write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
for row in result:
    print(json.dumps(row, ensure_ascii=False)[:2800])
print(json.dumps({"rows": len(result), "readonly": True, "store": store, "elapsed_seconds": time.monotonic()-start}))
