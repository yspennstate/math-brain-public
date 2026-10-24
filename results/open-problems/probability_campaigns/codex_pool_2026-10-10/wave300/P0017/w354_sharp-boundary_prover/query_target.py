import json
import sqlite3
from pathlib import Path

base = Path(__file__).resolve().parent
path = Path("~/math-brain-build/local/population/brain.sqlite3")
connection = sqlite3.connect("file:" + path.as_posix() + "?mode=ro", uri=True, timeout=3)
rows = connection.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE ? LIMIT 4", ("%Dimension-free log-concave Poincare%",)).fetchall()
connection.close()
receipt = [{"id": row[0], "kind": row[1], "title": row[2], "body": row[3], "metadata": json.loads(row[4])} for row in rows]
(base / "LIVE_TARGET_RECEIPT.json").write_text(json.dumps({"store": str(path), "mode": "ro", "query": "title LIKE '%Dimension-free log-concave Poincare%' LIMIT 4", "rows": receipt}, indent=2, ensure_ascii=False), encoding="utf-8")
print(json.dumps(receipt, ensure_ascii=False))
