"""Check exact cited card IDs and quotes in the math store, read only."""

import json
import sqlite3
from pathlib import Path

store = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
connection = sqlite3.connect(store, uri=True)
rows = Path("~/brain_workers/w340/results.jsonl").read_text(encoding="utf-8-sig").splitlines()
for line in rows:
    row = json.loads(line)
    for edge in row.get("store_edges", []):
        result = connection.execute("SELECT payload_json FROM claims WHERE id=?", (edge["store_node_id"],)).fetchone()
        if result is None:
            print(row["row_id"], edge["kind"], "source_claim_missing")
            continue
        payload = json.loads(result[0])
        full = json.dumps(payload, ensure_ascii=False)
        print(row["row_id"], edge["kind"],
              "quote_exact=", edge["source_quote"] in full,
              "logical_id_exact=", edge["logical_id"] in full)

quote = "nu=(delta_(1/10)+delta_10)/2 yields failure of log-unimodality for every t>=5*pi."
for title, body, metadata in connection.execute(
    "SELECT title,body,metadata_json FROM nodes WHERE title LIKE ?", ("%P0193%",)
):
    print("P0193", "title=", title[:90], "witness_quote_exact=", quote in body,
          "logical_id_in_metadata=", "attempt-p0193" in metadata)
print("P0193", "exact_quote_claim_ids=", [r[0] for r in connection.execute(
    "SELECT id FROM claims WHERE payload_json LIKE ? LIMIT 5", (f"%{quote}%",)
)])

for title, body in connection.execute(
    "SELECT title,body FROM nodes WHERE title LIKE ?", ("%P0208%",)
):
    print("P0208", "title=", title[:90],
          "tau_star_discussed=", "tau*" in body or "tau_star" in body,
          "Aldous_Fill_problem_7_27=", "Problem 7.27" in body)
