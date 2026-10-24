import sqlite3

db = 'file:~/math-brain-build/local/population/brain.sqlite3?mode=ro'
conn = sqlite3.connect(db, uri=True)
tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
print('TABLES', tables)
for (name,) in tables:
    if name.startswith('sqlite_'):
        continue
    cols = [row[1] for row in conn.execute(f'PRAGMA table_info("{name}")')]
    if any(k in cols for k in ('title', 'statement', 'logical_name')):
        print('CANDIDATE_TABLE', name, cols)
        fields = [k for k in ('id', 'namespace', 'logical_name', 'title', 'statement') if k in cols]
        checks = [k for k in ('title', 'statement', 'logical_name') if k in cols]
        where = ' OR '.join(f'"{k}" LIKE ?' for k in checks)
        rows = conn.execute(f'SELECT {", ".join(fields)} FROM "{name}" WHERE {where} LIMIT 15', ('%Liouville%',) * len(checks)).fetchall()
        for row in rows:
            print('ROW', tuple(str(v)[:300] for v in row))
if 'nodes' in [x[0] for x in tables]:
    for row in conn.execute("SELECT id, kind, title, body, metadata_json FROM nodes WHERE title LIKE '%Exact Hausdorff dimension of Liouville quantum gravity%' LIMIT 4"):
        print('P0297_NODE', tuple(str(v)[:2500] for v in row))
