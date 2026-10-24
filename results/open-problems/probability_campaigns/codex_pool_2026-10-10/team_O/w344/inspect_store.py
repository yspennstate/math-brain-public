import json
import sqlite3

STORE = 'file:~/math-brain-build/local/population/brain.sqlite3?mode=ro'
with sqlite3.connect(STORE, uri=True) as conn:
    conn.execute('PRAGMA query_only=ON')
    names = [r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'")]
    print(json.dumps(names))
    for name in names:
        if name.lower() in {'nodes', 'cards', 'entries', 'edges'}:
            print(name, conn.execute('PRAGMA table_info(' + name + ')').fetchall())
