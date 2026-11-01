"""Read-only, narrowly targeted status lookup; no store export."""
import json
import sqlite3
from pathlib import Path

root = Path(__file__).resolve().parent
store = Path("~/math-brain-build/local/population/brain.sqlite3")
result = {"store": str(store), "connection_mode": "ro", "lookups": []}
with sqlite3.connect(store.as_uri() + "?mode=ro", uri=True, timeout=3) as conn:
    tables = [row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    result["named_tables"] = [t for t in tables if t in {"cards", "nodes", "sources", "theorems", "entities"}]
    for table in result["named_tables"]:
        columns = [r[1] for r in conn.execute('PRAGMA table_info("' + table + '")')]
        fields = [c for c in ("id", "key", "logical_name", "title", "statement", "status", "source_id") if c in columns]
        search_fields = [c for c in ("title", "statement", "logical_name", "key") if c in columns]
        if not fields or not search_fields:
            continue
        conditions, params = [], []
        for column in search_fields:
            conditions.append('(lower(COALESCE("' + column + '",\'\')) LIKE ? OR lower(COALESCE("' + column + '",\'\')) LIKE ?)')
            params.extend(("%transien%ballistic%", "%c0041%"))
        sql = 'SELECT ' + ','.join('"' + c + '"' for c in fields) + ' FROM "' + table + '" WHERE ' + ' OR '.join(conditions) + ' LIMIT 8'
        matches = [dict(zip(fields, row)) for row in conn.execute(sql, params)]
        result["lookups"].append({"table": table, "fields": fields, "matches": matches})
root.joinpath("STORE_LOOKUP.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2, ensure_ascii=False))
