"""Quote both ends of w527's proposed relations from draft and read-only store."""

import json
import sqlite3
from pathlib import Path

root = Path(__file__).resolve().parent
bundle = json.loads((root / "bundle_001.json").read_text(encoding="utf-8"))
entries = {entry["key"]: entry for entry in bundle["entries"]}
uri = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
conn = sqlite3.connect(uri, uri=True)
target_id = "claim_75af14e7ac074f83e6e184d7d70cc4ec4d65e92c7b55d0e037bd1065492535b1"
title, body, metadata_json = conn.execute(
    "SELECT title, body, metadata_json FROM nodes WHERE id=?", (target_id,)
).fetchone()
logical_id = json.loads(metadata_json)["logical_id"]
rows = []
for relation in bundle["relations"]:
    assert relation["to_existing_logical"] == logical_id
    source = entries[relation["from_key"]]
    rows.append(
        {
            "from_key": relation["from_key"],
            "from_title": source["title"],
            "from_statement_quote": source["statement"],
            "to_existing_logical": logical_id,
            "to_store_id": target_id,
            "to_title": title,
            "to_body_quote": body,
            "kind": relation["kind"],
            "rationale": relation["rationale"],
        }
    )
out = root / "EDGE_EVIDENCE.jsonl"
out.write_text("\n".join(json.dumps(row, ensure_ascii=False) for row in rows) + "\n", encoding="utf-8")
print(f"wrote {len(rows)} evidence-backed edge rows to {out}")
