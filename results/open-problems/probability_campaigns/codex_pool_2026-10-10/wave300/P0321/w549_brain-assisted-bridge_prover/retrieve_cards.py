"""Read only a handful of named mathematical cards with bounded SQL."""
import json
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
database = Path("~/math-brain-build/local/population/brain.sqlite3")
start = time.monotonic()
con = sqlite3.connect(database.as_uri()+"?mode=ro", uri=True, timeout=5)
con.row_factory = sqlite3.Row
con.execute("PRAGMA query_only=ON")
con.set_progress_handler(lambda: int(time.monotonic()-start > 10), 1000)
queries = [("strong mixing", 2), ("Delaunay", 1), ("Mermin", 1), ("hexatic", 2)]
groups = []
for term, limit in queries:
    rows = con.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE lower(title) LIKE ? ORDER BY created_at DESC LIMIT ?", ("%"+term.lower()+"%", limit)).fetchall()
    cards = []
    for row in rows:
        card = dict(row)
        card["metadata"] = json.loads(card.pop("metadata_json"))
        cards.append(card)
    groups.append({"query": term, "limit": limit, "cards": cards})
con.close()
result = {"command": "python -X utf8 retrieve_cards.py", "database": str(database), "mode": "ro", "groups": groups, "elapsed_seconds": time.monotonic()-start}
(ROOT / "brain_cards.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(result, ensure_ascii=False, indent=2))
