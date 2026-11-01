"""Read-only exact-quote check for one Team O worker's proposed node edges."""

import json
import re
import sqlite3
import sys
from pathlib import Path

worker = sys.argv[1]
root = Path("~/brain_workers") / worker
name = "RESULT_ROWS.jsonl" if (root / "RESULT_ROWS.jsonl").exists() else "results.jsonl"
rows = [json.loads(x) for x in (root / name).read_text(encoding="utf-8-sig").splitlines() if x.strip()]
by_key = {x["entry_key"]: x for x in rows if "entry_key" in x}
store = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True)
cache = {}


def target(logical):
    if logical not in cache:
        matches = store.execute("SELECT id,body,metadata_json FROM nodes WHERE metadata_json LIKE ?", (f"%{logical}%",)).fetchall()
        cache[logical] = [(i, body) for i, body, meta in matches if json.loads(meta).get("logical_id") == logical]
    return cache[logical]


checked = 0
failures = []
for row in rows:
    row_id = row.get("row_id") or row.get("id")
    for relation in row.get("relations", []):
        match = re.search(r'FROM: "([^"]*)" TO: "([^"]*)"', relation.get("rationale", ""))
        if not match:
            failures.append((row_id, "quote pair missing"))
            continue
        frm, to = match.groups()
        if frm not in row.get("statement", ""):
            failures.append((row_id, "FROM quote mismatch"))
        if "to_key" in relation:
            other = by_key.get(relation["to_key"])
            if other is None or to not in other.get("statement", ""):
                failures.append((row_id, "internal TO quote mismatch"))
        elif "to_existing_logical" in relation:
            matches = target(relation["to_existing_logical"])
            if not matches or not any(to in body for _, body in matches):
                failures.append((row_id, "store TO quote mismatch"))
        checked += 1
    for relation in row.get("store_edges", []):
        matches = target(relation["logical_id"])
        if not any(i == relation["store_node_id"] and relation["source_quote"] in body for i, body in matches):
            failures.append((row_id, "store edge ID/logical ID/quote mismatch"))
        checked += 1

print(json.dumps({"worker": worker, "edges_checked": checked, "failures": failures}, ensure_ascii=False))
