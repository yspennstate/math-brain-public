"""Only inspect the schemas of named mathematical card/source tables, read-only."""
import json
from pathlib import Path
import sqlite3

store = Path("~/math-brain-build/local/population/brain.sqlite3")
with sqlite3.connect("file:" + store.as_posix() + "?mode=ro", uri=True, timeout=3) as connection:
    tables = connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name IN ('cards','nodes','entries','statements','sources')"
    ).fetchall()
    for (name,) in tables:
        print(json.dumps({"table": name, "columns": connection.execute(f'PRAGMA table_info("{name}")').fetchall()}))
    if ("nodes",) in tables:
        rows = connection.execute(
            "SELECT id,kind,title,body,metadata_json FROM nodes "
            "WHERE kind NOT IN ('test','test_item','question','benchmark') "
            "AND title LIKE '%critical%' AND title LIKE '%percolation%' LIMIT 6"
        ).fetchall()
        for identifier, kind, title, body, metadata in rows:
            print(json.dumps({"id": identifier, "kind": kind, "title": title,
                              "body_excerpt": body[:1600], "metadata_excerpt": metadata[:1700]}, ensure_ascii=False))
