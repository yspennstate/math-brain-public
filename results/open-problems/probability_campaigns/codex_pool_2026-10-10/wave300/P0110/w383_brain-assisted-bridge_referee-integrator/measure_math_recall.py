"""Bounded read-only retrieval probe for the task's exact cards."""
import contextlib
import io
import json
import sqlite3
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = Path("~/math-brain-build/local/population/brain.sqlite3")
sys.path.insert(0, "~/math-brain-build/src")
from math_brain.cli import main  # noqa: E402

with sqlite3.connect(DB.resolve().as_uri() + "?mode=ro", uri=True) as con:
    con.execute("PRAGMA query_only=ON")
    named = con.execute(
        "SELECT id,title FROM nodes WHERE title LIKE ? OR title LIKE ? ORDER BY title LIMIT 5",
        ("%An iid FPP law with proved KPZ exponent relation%", "Chatterjee (2013)%"),
    ).fetchall()

queries = [
    "P0110 iid FPP law proved KPZ exponent relation",
    "Chatterjee 2013 KPZ relation hypotheses iid FPP chi xi exponent existence",
]
rows = []
for query in queries:
    out = io.StringIO()
    start = time.perf_counter()
    with contextlib.redirect_stdout(out):
        code = main(["recall", str(DB), query, "--limit", "10", "--skip-unknown-edges"])
    result = json.loads(out.getvalue())
    hits = result["hits"] if isinstance(result, dict) else result
    rows.append({
        "query": query,
        "exit_code": code,
        "elapsed_seconds": round(time.perf_counter() - start, 3),
        "top_titles": [h["title"] for h in hits[:5]],
        "target_ranks": {title: next((i + 1 for i, h in enumerate(hits) if h["id"] == ident), None)
                         for ident, title in named},
    })

receipt = {"database_access": "mode=ro; PRAGMA query_only=ON; CLI recall opens read-only",
           "named_cards": named, "limit": 10, "probes": rows}
(ROOT / "RETRIEVAL_MEASURE.json").write_text(json.dumps(receipt, indent=2), encoding="utf-8")
print(json.dumps(receipt, indent=2))
