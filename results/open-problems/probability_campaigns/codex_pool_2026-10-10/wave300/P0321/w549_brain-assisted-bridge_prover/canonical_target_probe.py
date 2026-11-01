"""Target-only read of the named canonical repository's discovered audit snapshot."""
import json
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
db = Path("~/math-research-brain/local/audits/jmlr-two-paper-zip-audit-v1/mathbrain_v2.sqlite3")
start = time.monotonic()
result = {"command": "python -X utf8 canonical_target_probe.py", "database": str(db), "mode": "ro", "scope": "audit snapshot found in canonical repository, not certified current live store", "cards": []}
con = sqlite3.connect(db.as_uri()+"?mode=ro", uri=True, timeout=5)
con.row_factory = sqlite3.Row
con.execute("PRAGMA query_only=ON")
con.set_progress_handler(lambda: int(time.monotonic()-start > 10), 1000)
tables = [row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type='table'")]
result["table_names"] = tables
if "nodes" in tables:
    columns = {row[1] for row in con.execute("PRAGMA table_info(nodes)")}
    result["nodes_columns"] = sorted(columns)
    if {"id", "title", "body"} <= columns:
        result["cards"] = [dict(row) for row in con.execute("SELECT id,title,body FROM nodes WHERE lower(title) LIKE '%hexatic%' OR body LIKE '%P0321%' LIMIT 2")]
    else:
        result["note"] = "No supported id/title/body node schema; no broad scan or export performed."
con.close()
result["elapsed_seconds"] = time.monotonic()-start
(ROOT / "canonical_target_probe.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
