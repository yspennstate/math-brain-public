"""Targeted read-only check of the three C0023-related live logical names."""
import sqlite3

uri = "file:~/math-brain-build/local/population/brain.sqlite3?mode=ro"
connection = sqlite3.connect(uri, uri=True, timeout=5)
connection.execute("PRAGMA query_only=ON")
tables = [name for (name,) in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")]
print("candidate tables:", [name for name in tables if any(s in name.lower() for s in ("node", "card", "entry"))])
for table in tables:
    if not any(s in table.lower() for s in ("node", "card", "entry")):
        continue
    cols = [row[1] for row in connection.execute(f'PRAGMA table_info("{table}")')]
    print(table, "columns:", cols)
    if "logical_name" not in cols and "metadata_json" in cols:
        targets = (
            "open-problem-c0023-no-percolation-at-criticality-on-z-d-for-3-d-10",
            "open-problem-c0084-no-infinite-cluster-at-criticality-on-quasi-transitive-graphs-with-p-c",
            "open-problem-c0094-no-infinite-cluster-at-criticality-on-z-d-for-all-d-2-duplicate-record",
        )
        for target in targets:
            row = connection.execute(
                f'SELECT id,kind,title,substr(body,1,210),substr(metadata_json,1,260) FROM "{table}" WHERE metadata_json LIKE ? ORDER BY created_at DESC LIMIT 1',
                (f"%{target}%",),
            ).fetchone()
            print(target, row)
        continue
    if "logical_name" not in cols:
        continue
    projection = [x for x in ("logical_name", "namespace", "title", "statement", "revision") if x in cols]
    targets = (
        "open-problem-c0023-no-percolation-at-criticality-on-z-d-for-3-d-10",
        "open-problem-c0084-no-infinite-cluster-at-criticality-on-quasi-transitive-graphs-with-p-c",
        "open-problem-c0094-no-infinite-cluster-at-criticality-on-z-d-for-all-d-2-duplicate-record",
    )
    sql = f'SELECT {", ".join(projection)} FROM "{table}" WHERE logical_name IN (?,?,?) LIMIT 10'
    rows = connection.execute(sql, targets).fetchall()
    for row in rows:
        if any("c0023" in str(v) or "c0084" in str(v) or "c0094" in str(v) for v in row):
            print(table, dict(zip(projection, [str(v)[:240] for v in row])))
connection.close()
