"""Read-only, exact-term inventory of the local math-brain store."""
from pathlib import Path
import sqlite3

db = Path('~/math-brain-build/local/population/brain.sqlite3')
connection = sqlite3.connect(db.as_uri() + '?mode=ro', uri=True)
connection.execute('PRAGMA query_only=ON')
for (name,) in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"):
    columns = [row[1] for row in connection.execute(f'PRAGMA table_info("{name}")')]
    if name.lower().startswith(('node', 'card', 'entry', 'claim')):
        print(name, columns)
        text_columns = [c for c in columns if any(t in c.lower() for t in ('title', 'statement', 'logical_name', 'body'))]
        for term in ('Fourier entropy', 'bent selector', 'entropy influence'):
            for col in text_columns:
                sql = f'SELECT {", ".join(chr(34)+x+chr(34) for x in columns[:min(4,len(columns))])} FROM "{name}" WHERE lower("{col}") LIKE ? LIMIT 4'
                for row in connection.execute(sql, ('%' + term.lower() + '%',)):
                    print('MATCH', term, col, repr(row)[:800])
connection.close()
