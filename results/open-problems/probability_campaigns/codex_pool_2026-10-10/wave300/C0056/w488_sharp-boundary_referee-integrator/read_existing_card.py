"""Read one C0056 card from the local math store without changing it."""
import json
import sqlite3
from pathlib import Path

path = Path(r"~\math-brain-build\local\population\brain.sqlite3")
con = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=5)
con.execute("PRAGMA query_only=ON")
row = con.execute(
    "SELECT id, title, body, metadata_json, digest FROM nodes WHERE id=?",
    ("claim_09038093d9a000c99aeace01330a48caf661984fe5badf3cd03f77be5582e4db",),
).fetchone()
if row is None:
    raise SystemExit("C0056 card missing")
meta = json.loads(row[3])
print(json.dumps({"id": row[0], "title": row[1], "body": row[2],
                  "logical_id": meta.get("logical_id"), "truth_status": meta.get("truth_status"),
                  "source_id": meta.get("source_id"), "digest": row[4]}, ensure_ascii=False))
con.close()
