"""Targeted read-only lookups; never emit serialized export or manifest lines."""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CANDIDATES = [
    Path(r"~/math-brain-build/local/population/brain.sqlite3"),
    Path(r"~/math-research-brain/brain.sqlite3"),
    Path(r"~/math-research-brain/store.sqlite3"),
]
output = []
for path in CANDIDATES:
    if not path.is_file():
        output.append({"path": str(path), "exists": False})
        continue
    connection = sqlite3.connect(path.as_uri() + "?mode=ro", uri=True, timeout=5)
    tables = [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    item = {"path": str(path), "exists": True}
    if "nodes" in tables:
        columns = [row[1] for row in connection.execute("PRAGMA table_info(nodes)")]
        item["node_columns"] = columns
        if "title" in columns:
            wanted = [column for column in ("id", "title", "kind", "body", "metadata_json") if column in columns]
            query = ("SELECT " + ",".join(wanted) + " FROM nodes WHERE "
                     "lower(title) LIKE '%bigeodesic%' OR title LIKE '%P0117%' OR "
                     "lower(title) LIKE '%bi-infinite geodesics in planar%' LIMIT 12")
            found = []
            for row in connection.execute(query):
                value = dict(zip(wanted, row))
                value["body"] = str(value.get("body", ""))[:2800]
                raw = value.pop("metadata_json", None)
                if raw:
                    metadata = json.loads(raw)
                    value["metadata"] = {key: metadata[key] for key in
                                         ("logical_id", "truth_status", "claim_kind", "source_id", "statement_fidelity_reviewed")
                                         if key in metadata}
                found.append(value)
            item["target_rows"] = found
    else:
        item["tables"] = tables
    connection.close()
    output.append(item)
(ROOT / "live_store_check.json").write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
for item in output:
    print(json.dumps({key: value for key, value in item.items() if key != "target_rows"}))
    for row in item.get("target_rows", []):
        print(json.dumps(row, ensure_ascii=False))
