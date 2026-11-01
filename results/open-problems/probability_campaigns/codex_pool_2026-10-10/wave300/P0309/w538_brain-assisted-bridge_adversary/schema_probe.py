import sqlite3,json,pathlib
p=pathlib.Path('~/math-brain-build/local/population/brain.sqlite3')
c=sqlite3.connect(p.as_uri()+'?mode=ro',uri=True,timeout=5)
c.execute('PRAGMA query_only=ON')
rows=c.execute("SELECT name,sql FROM sqlite_master WHERE type='table' AND (name LIKE '%node%' OR name LIKE '%card%' OR name LIKE '%fts%')").fetchall()
print(json.dumps(rows,ensure_ascii=False)[:18000])
c.close()
