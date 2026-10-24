"""Bounded targeted reads; never load the whole corpus or write a live store."""
import json
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
path = Path("~/math-brain-build/local/population/brain.sqlite3")
start = time.perf_counter()
db = sqlite3.connect(f"file:{path.as_posix()}?mode=ro", uri=True, timeout=5)
db.row_factory = sqlite3.Row
db.execute("PRAGMA query_only=ON")
db.set_progress_handler(lambda: int(time.perf_counter() - start > 45), 5000)
queries = [
    ("candidate_id", "SELECT id,title,body,metadata_json FROM nodes WHERE body LIKE ? OR metadata_json LIKE ? LIMIT 8", ("%C0041%", "%C0041%")),
    ("rwre_titles", "SELECT id,title,body,metadata_json FROM nodes WHERE lower(title) LIKE ? OR lower(title) LIKE ? LIMIT 8", ("%rwre%", "%random%environment%")),
    ("ballistic_titles", "SELECT id,title,body,metadata_json FROM nodes WHERE lower(title) LIKE ? LIMIT 8", ("%ballistic%",)),
    ("regeneration_titles", "SELECT id,title,body,metadata_json FROM nodes WHERE lower(title) LIKE ? LIMIT 8", ("%regeneration%",)),
]
out = []
for label, sql, parameters in queries:
    rows = [dict(row) for row in db.execute(sql, parameters)]
    for row in rows:
        row["metadata"] = json.loads(row.pop("metadata_json"))
    out.append({"query":label, "result_count":len(rows), "rows":rows})
db.close()
result = {"command":"python -B -X utf8 retrieve_cards.py", "store":str(path), "mode":"read-only bounded SQL lookup, not a ranking-engine benchmark", "elapsed_seconds":round(time.perf_counter()-start,6), "queries":out}
ROOT.joinpath("math_cards.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"elapsed_seconds":result["elapsed_seconds"],"queries":[{"query":r["query"],"count":r["result_count"],"titles":[x["title"] for x in r["rows"]]} for r in out]}))
