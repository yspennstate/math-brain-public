import json
import sqlite3
import time
from pathlib import Path

root = Path(__file__).resolve().parent
path = Path("~/math-brain-build/local/population/brain.sqlite3")
t0 = time.monotonic()
db = sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True, timeout=1)
db.execute("PRAGMA query_only=ON")
db.set_progress_handler(lambda: time.monotonic() - t0 > 15, 10000)
rows = db.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND (name LIKE '%node%' OR name LIKE '%card%' OR name LIKE '%statement%' OR name LIKE '%fts%')").fetchall()
result = {"store": str(path), "mode": "read-only", "schema": rows, "elapsed_seconds": time.monotonic()-t0}
(root / "store_schema.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps(result, indent=2)[:15000])
db.close()
