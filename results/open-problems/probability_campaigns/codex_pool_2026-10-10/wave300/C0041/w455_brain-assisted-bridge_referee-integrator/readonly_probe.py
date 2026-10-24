import json
import sqlite3
import time
from pathlib import Path

root = Path(__file__).resolve().parent
db = Path("~/math-brain-build/local/population/brain.sqlite3")
started = time.monotonic()
conn = sqlite3.connect("file:" + db.as_posix() + "?mode=ro", uri=True, timeout=8)
conn.execute("PRAGMA query_only=ON")
conn.execute("PRAGMA busy_timeout=8000")
conn.set_progress_handler(lambda: int(time.monotonic() - started > 25), 2000)
rows = conn.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE lower(title) LIKE '%ballistic%' OR lower(title) LIKE '%random%environment%' OR lower(title) LIKE '%regeneration%' LIMIT 16").fetchall()
cards = [{"id": r[0], "kind": r[1], "title": r[2], "body": r[3], "metadata": json.loads(r[4])} for r in rows]
schema = [{"name": r[0], "sql": r[1]} for r in conn.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND (name LIKE '%fts%' OR name LIKE '%search%')")]
conn.close()
receipt = {"store": str(db), "mode": "read_only", "bounded_sql": "title matches ballistic/random-environment/regeneration, limit 16, 25-second deadline", "elapsed_seconds": round(time.monotonic()-started, 3), "count": len(cards), "cards": cards, "search_schema": schema}
(root / "math_recall_cards.json").write_text(json.dumps(receipt, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k:v for k,v in receipt.items() if k != "cards"}, ensure_ascii=False))
for card in cards:
    print(json.dumps({"id":card["id"], "title":card["title"], "body":card["body"]}, ensure_ascii=False))
