import json
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = Path("~/math-brain-build/local/population/brain.sqlite3")
queries = {
    "finite_dependent_domination": "title LIKE '%Liggett%' OR title LIKE '%Schonmann%' OR title LIKE '%Stacey%' OR (title LIKE '%dependent%' AND title LIKE '%percolation%')",
    "percolation_uniqueness": "title LIKE '%Burton%' OR title LIKE '%Keane%' OR (title LIKE '%uniqueness%' AND title LIKE '%percolation%')",
    "critical_target": "title LIKE '%No percolation at criticality on Z%' OR title LIKE '%Critical percolation on Zd%' OR (title LIKE '%criticality%' AND body LIKE '%3%10%')",
}
start = time.monotonic()
db = sqlite3.connect(f"file:{DB.as_posix()}?mode=ro", uri=True, timeout=1)
db.execute("PRAGMA query_only=ON")
db.set_progress_handler(lambda: time.monotonic() - start > 20, 10000)
results = {}
for name, where in queries.items():
    t0 = time.monotonic()
    rows = db.execute(f"SELECT id,kind,title,body,metadata_json FROM nodes WHERE {where} LIMIT 3").fetchall()
    results[name] = {"elapsed_seconds": time.monotonic()-t0, "cards": [dict(zip(["id", "kind", "title", "body", "metadata_json"], row)) for row in rows]}
    print(name, "hits", len(rows))
    for row in rows:
        print(json.dumps(dict(zip(["id", "kind", "title", "body", "metadata_json"], row)), ensure_ascii=False)[:14000])
results["connection"] = {"store": str(DB), "mode": "read-only", "elapsed_seconds": time.monotonic()-start}
(ROOT / "brain_cards.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
db.close()
