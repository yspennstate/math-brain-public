import json
import sqlite3

path = "~/math-brain-build/local/population/brain.sqlite3"
conn = sqlite3.connect(f"file:{path}?mode=ro", uri=True)
for (table,) in conn.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"):
    if "node" in table or "card" in table:
        cols = [row[1] for row in conn.execute(f"PRAGMA table_info('{table}')")]
        print(table, ",".join(cols))
print("targeted matches:")
for row in conn.execute(
    "SELECT id, kind, title, substr(body,1,180), substr(metadata_json,1,220) "
    "FROM nodes WHERE lower(title) LIKE '%bigeodesic%' "
    "OR lower(body) LIKE '%bigeodesic%' "
    "OR lower(body) LIKE '%bi-infinite geodesic%' LIMIT 25"
):
    print(repr(row))
for title, meta in conn.execute(
    "SELECT title, metadata_json FROM nodes WHERE title LIKE 'Open problem: Absence of bi-infinite geodesics%'"
):
    data = json.loads(meta)
    print("target card metadata:", title, {k: v for k, v in data.items() if "logical" in k or "namespace" in k or k == "source_id"})
