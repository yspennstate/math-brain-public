"""Diagnose exact source endpoint mismatches in selected w340 rows."""

import json
import sqlite3
from pathlib import Path

ids = {"w340.P0109.001", "w340.P0038.001", "w340.P0038.002"}
rows = [json.loads(x) for x in Path("~/brain_workers/w340/results.jsonl").read_text(encoding="utf-8-sig").splitlines() if x.strip()]
store = sqlite3.connect("file:~/math-brain-build/local/population/brain.sqlite3?mode=ro", uri=True)
for row in rows:
    if row.get("row_id") not in ids:
        continue
    for edge in row.get("store_edges", []):
        node = store.execute("SELECT body,metadata_json FROM nodes WHERE id=?", (edge["store_node_id"],)).fetchone()
        if node is None:
            print(row["row_id"], edge["kind"], "id_missing")
            continue
        body, metadata = node
        actual_logical = json.loads(metadata).get("logical_id")
        print(row["row_id"], edge["kind"],
              "id_exists=", True,
              "logical_match=", actual_logical == edge["logical_id"],
              "quote_match=", edge["source_quote"] in body,
              "actual_logical=", actual_logical,
              "body_start=", body[:180])
        if edge["source_quote"] not in body:
            print("quote=", repr(edge["source_quote"]))
            print("body_excerpt=", repr(body[:650]))

bundle = json.loads(Path("~/brain_workers/w340/bundle_002.json").read_text(encoding="utf-8-sig"))
for edge in bundle["relations"]:
    if edge.get("to_existing_logical", "").endswith("markov-inequality"):
        logical = edge["to_existing_logical"]
        rows = store.execute("SELECT body FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?", (logical,)).fetchall()
        print("markov_relation=", repr(edge["rationale"]))
        print("markov_body=", repr(rows[0][0][:750]) if rows else "MISSING")
