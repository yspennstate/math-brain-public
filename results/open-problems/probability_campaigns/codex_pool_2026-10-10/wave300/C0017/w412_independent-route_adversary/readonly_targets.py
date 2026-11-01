"""Read only the two named C0017 cards from the live population store."""
import json
from pathlib import Path
import sqlite3

folder = Path("~/brain_workers/w412")
database = Path("~/math-brain-build/local/population/brain.sqlite3")
ids = ["claim_91f295e6d2a67634c0b90a5ee4130c1feed72dc0fe16086a679021c90c8917cb", "claim_07a861a72ebeb008dc23e9db32147327c062427adee7a530bab01f0de67bd002"]
receipt = {"database": str(database), "mode": "ro; PRAGMA query_only=ON", "query": "SELECT id,title,body,metadata_json FROM nodes WHERE id IN (?,?)", "requested_ids": ids, "rows": [], "error": None}
try:
    with sqlite3.connect(database.as_uri()+"?mode=ro", uri=True, timeout=2) as conn:
        conn.execute("PRAGMA query_only=ON")
        for identifier, title, body, metadata in conn.execute(receipt["query"], ids):
            receipt["rows"].append({"id": identifier, "title": title, "body": body, "metadata": json.loads(metadata)})
except sqlite3.Error as error:
    receipt["error"] = str(error)
(folder / "LIVE_TARGET_RECEIPT.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"database": str(database), "matched": [{"id": r["id"], "title": r["title"], "logical_id": r["metadata"].get("logical_id")} for r in receipt["rows"]], "error": receipt["error"]}), flush=True)
