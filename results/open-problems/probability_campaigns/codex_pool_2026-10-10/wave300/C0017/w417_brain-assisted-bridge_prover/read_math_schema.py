import json
import sqlite3
from pathlib import Path

db = Path('~/math-brain-build/local/population/brain.sqlite3')
with sqlite3.connect(db.as_uri()+'?mode=ro', uri=True) as conn:
    conn.execute('PRAGMA query_only=ON')
    rows=conn.execute("SELECT name,sql FROM sqlite_schema WHERE type='table' AND (name NOT LIKE '%fts_%' OR name LIKE '%fts') LIMIT 25").fetchall()
    print(json.dumps({'database':str(db), 'read_only':True, 'schema':rows},ensure_ascii=False,indent=2))
