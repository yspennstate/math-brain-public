"""Read only four exact card IDs and the schema needed to decode them."""
import json
import sqlite3
from pathlib import Path

root = Path(__file__).resolve().parent
ids = (
    "claim_25c5933eb4eeace1fc2a65fb1aba685df634054eba10e9f383b0eeb7c1ba32f7",
    "claim_3a7f53cc4f4c10093c8e4e07c223f18d52212a9c7d6f98c1196f104f16111a3d",
    "claim_1d9fd4ecb780476895cdc3e58580ccbe",
    "claim_1b864127f2bba872e9317da0f8bb92499ed6de1b5bd8779daf961da7ad1cb410",
)
with sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True) as con:
    con.row_factory = sqlite3.Row
    schema = con.execute("SELECT sql FROM sqlite_master WHERE name=?", ("nodes",)).fetchone()
    print("node schema:", schema[0] if schema else "missing")
    rows = [dict(r) for r in con.execute("SELECT * FROM nodes WHERE id IN (?,?,?,?) ORDER BY id", ids)]
    fts = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE name LIKE ?", ("%fts%",))]
record = {"source":"~/math-brain-build/local/population/brain.sqlite3",
          "mode":"ro", "requested_ids":list(ids), "returned_count":len(rows), "fts_tables":fts, "cards":rows}
(root / "BRAIN_CARDS.json").write_text(json.dumps(record, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
for row in rows:
    print(json.dumps({key:row[key] for key in ("id", "title", "body") if key in row}, ensure_ascii=False))
