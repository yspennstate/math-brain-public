"""Proposed bounded research-ID fallback. Uses only exact node metadata and a read-only connection."""
import argparse
import json
from pathlib import Path
import re
import sqlite3
import time

parser = argparse.ArgumentParser()
parser.add_argument("query")
args = parser.parse_args()
matches = set(re.findall(r"(?<![A-Za-z0-9])P[0-9]{4}(?![A-Za-z0-9])", args.query, re.IGNORECASE))
if len(matches) != 1:
    raise SystemExit("No exact P#### research target ID; fallback remains silent.")
target = matches.pop().lower()
routes = {"p0309": ["Open problem: Positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases", "Attempt on Positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases"]}
if target not in routes:
    raise SystemExit("No validated title route for this research target; fallback remains silent.")
path = Path("~/math-brain-build/local/population/brain.sqlite3")
start = time.monotonic()
con = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=2)
con.execute("PRAGMA query_only=ON")
con.row_factory = sqlite3.Row
con.set_progress_handler(lambda: int(time.monotonic()-start>3), 1000)
rows = [dict(row) for row in con.execute(
    "SELECT id,title,body,metadata_json FROM nodes WHERE kind='claim' AND title IN (?,?) LIMIT 4",
    routes[target])]
con.close()
for row in rows:
    row["metadata"] = json.loads(row.pop("metadata_json"))
expected = {"op-" + target, "at-" + target}
rows = [row for row in rows if row["metadata"].get("bundle_entry_key") in expected]
keys = {row["metadata"].get("bundle_entry_key") for row in rows}
record = {"query": args.query, "target": target.upper(), "command": "python -X utf8 tools/exact_target_lookup.py \"P0309 Riesz gas mistakes\"", "store": str(path), "read_only": True, "row_limit": 4, "elapsed_s": time.monotonic()-start, "expected_exact_keys": sorted(expected), "returned_exact_keys": sorted(keys), "exact_hits": len(expected & keys), "expected_count": len(expected), "rows": rows}
out = Path(__file__).resolve().parents[1] / "evidence" / "title_target_lookup.json"
out.write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({key: value for key, value in record.items() if key != "rows"}, indent=2))
for row in rows:
    print(row["metadata"].get("bundle_entry_key"), row["title"])
