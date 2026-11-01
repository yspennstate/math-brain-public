"""Read only the two named C0047 cards, never write any live store."""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ids = ["claim_0bfe0a8a0e527dd20457f2c0393cb560907546ec53a1204204de0fc82235d788",
       "claim_77d417df1817eac0893d67dcfcf0d7140581f4e26ce07c31919403d44d301960"]
path = Path("~/math-brain-build/local/population/brain.sqlite3")
con = sqlite3.connect(path.as_uri()+"?mode=ro", uri=True, timeout=10)
con.execute("PRAGMA query_only=ON")
con.execute("PRAGMA busy_timeout=10000")
con.row_factory = sqlite3.Row
rows = [dict(row) for cid in ids for row in con.execute("SELECT * FROM nodes WHERE id=?", (cid,))]
result = {"store": str(path), "connection_mode": "ro/query_only",
          "exact_ids": ids, "rows": rows, "row_count": len(rows)}
(ROOT / "STORE_SOURCE_REPORT.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
print(json.dumps({"row_count": len(rows), "rows": [
    {"id": row["id"], "title": row.get("title"), "digest": row.get("digest")} for row in rows]}, indent=2))
