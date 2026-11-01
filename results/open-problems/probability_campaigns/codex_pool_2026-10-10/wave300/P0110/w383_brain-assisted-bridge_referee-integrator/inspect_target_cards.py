"""Read only the P0110 and conditional-KPZ cards relevant to the referee task."""
import json
import sqlite3
from pathlib import Path

root = Path(__file__).resolve().parent
db = Path("~/math-brain-build/local/population/brain.sqlite3")
with sqlite3.connect(db.resolve().as_uri() + "?mode=ro", uri=True) as con:
    con.execute("PRAGMA query_only=ON")
    cards = con.execute(
        "SELECT id,title,body,metadata_json FROM nodes WHERE title LIKE ? OR title LIKE ? OR title LIKE ? ORDER BY title LIMIT 8",
        ("%An iid FPP law with proved KPZ exponent relation%", "Chatterjee (2013)%", "Auffinger-Damron (2014)%"),
    ).fetchall()
    columns = [row[1] for row in con.execute("PRAGMA table_info(edges)")]
data = {"cards": [{"id": row[0], "title": row[1], "body": row[2],
                   "metadata": json.loads(row[3])} for row in cards],
        "edge_columns": columns, "access": "mode=ro; PRAGMA query_only=ON"}
(root / "TARGET_CARDS.json").write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps({"cards": [{"id": x["id"], "title": x["title"], "body": x["body"][:1200]}
                             for x in data["cards"]], "edge_columns": columns}, indent=2, ensure_ascii=False))
