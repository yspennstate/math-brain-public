import json
import sqlite3
from pathlib import Path

store = Path('~/math-brain-build/local/population/brain.sqlite3')
with sqlite3.connect(store.as_uri() + '?mode=ro', uri=True) as connection:
    connection.execute('PRAGMA query_only=ON')
    rows = connection.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE '%fts%'").fetchall()
    output = [{'name': name, 'sql': sql} for name, sql in rows]
    Path('store_schema.json').write_text(json.dumps(output, indent=2), encoding='utf-8')
    print(json.dumps(output, indent=2)[:16000])
