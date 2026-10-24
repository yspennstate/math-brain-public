"""Read-only schema and narrow LQG title probe; never mutates the store."""
import json
import sqlite3

p = '~/math-brain-build/local/population/brain.sqlite3'
c = sqlite3.connect('file:' + p + '?mode=ro', uri=True)
tables = [r[0] for r in c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name")]
print('tables:', tables)
for table in tables:
    if table in ('cards', 'entries', 'nodes'):
        print(table, [r[1] for r in c.execute(f'PRAGMA table_info({table})')])
        if table == 'nodes':
            for pattern in ('%hausdorff dimension%liouville%', '%lfpp%', '%p0297%'):
                rows = c.execute('SELECT title,metadata_json FROM nodes WHERE lower(title) LIKE ? OR lower(body) LIKE ? LIMIT 12', (pattern, pattern)).fetchall()
                print('probe', pattern, 'count_shown', len(rows))
                for title, metadata in rows:
                    m = json.loads(metadata)
                    print(title[:100], '|', m.get('logical_id'), '|', m.get('claim_kind'), '|', m.get('draft'))
