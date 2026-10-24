"""Bounded read-only probe of P0117 prerequisites and current-status coverage."""
import json
import sqlite3
from pathlib import Path

db = Path('~/math-brain-build/local/population/brain.sqlite3')
uri = db.resolve().as_uri() + '?mode=ro'
with sqlite3.connect(uri, uri=True, timeout=5) as con:
    con.execute('PRAGMA query_only=ON')
    rows = {}
    for key, pattern in [
        ('ahlberg_hoffman_title', '%Ahlberg%Hoffman%'),
        ('bigeodesic_title', '%bigeodesic%'),
        ('backward_finite_body', '%backward%finit%'),
        ('fixed_direction_body', '%fixed%direction%bigeodesic%'),
    ]:
        field = 'title' if key.endswith('_title') else 'body'
        data = con.execute(
            f'SELECT id,title FROM nodes WHERE lower({field}) LIKE lower(?) LIMIT 20',
            (pattern,),
        ).fetchall()
        rows[key] = [{'id': node_id, 'title': title} for node_id, title in data]
print(json.dumps(rows, ensure_ascii=False, indent=2))
