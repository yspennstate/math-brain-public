"""Read only the exact stored links among P0110 and its two conditional-theorem cards."""
import json
import sqlite3
from pathlib import Path

root = Path(__file__).resolve().parent
cards = json.loads((root / "TARGET_CARDS.json").read_text(encoding="utf-8"))["cards"]
ids = [x["id"] for x in cards]
db = Path("~/math-brain-build/local/population/brain.sqlite3")
with sqlite3.connect(db.resolve().as_uri() + "?mode=ro", uri=True) as con:
    con.execute("PRAGMA query_only=ON")
    placeholders = ",".join("?" for _ in ids)
    rows = con.execute(
        f"SELECT source_id,target_id,kind,rationale FROM edges WHERE source_id IN ({placeholders}) AND target_id IN ({placeholders}) LIMIT 30",
        ids + ids,
    ).fetchall()
    counts = {x: con.execute("SELECT count(*) FROM edges WHERE source_id=? OR target_id=?", (x, x)).fetchone()[0]
              for x in ids}
out = {"within_target_links": rows, "adjacent_edge_counts": counts, "access": "mode=ro; PRAGMA query_only=ON"}
(root / "TARGET_LINKS.json").write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out, indent=2))
