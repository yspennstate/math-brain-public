"""Exact-id canonical math-store reads only. Never open a writable connection."""
from pathlib import Path
import sqlite3
import json

root = Path(__file__).resolve().parent
store = Path('~/math-brain-build/local/population/brain.sqlite3')
ids = [
    'claim_00e83dbdd81c6433d9909a1b375c4e0a688bea718951c1d68fe8ffcd72b1bcf1',
    'claim_428fe793773c1d59b046e229c47907b20780786ceaae651f93241d8680ca3996',
]
logicals = [
    'math:probability.core:open-problem-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp',
    'math:probability.core:attempt-p0117-absence-of-bi-infinite-geodesics-in-planar-iid-fpp',
]
def ident(value):
    return '"' + value.replace('"', '""') + '"'
found = []
with sqlite3.connect(f'file:{store.as_posix()}?mode=ro', uri=True) as db:
    db.row_factory = sqlite3.Row
    tables = [r[0] for r in db.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
    for table in tables:
        cols = [r[1] for r in db.execute(f'PRAGMA table_info({ident(table)})')]
        if 'logical_id' in cols:
            key, wanted = 'logical_id', logicals
        elif 'id' in cols:
            key, wanted = 'id', ids
        else:
            continue
        query = f'SELECT * FROM {ident(table)} WHERE {ident(key)} IN (?,?) LIMIT 2'
        for row in db.execute(query, wanted):
            record = {k: v if not isinstance(v, bytes) else f'<binary {len(v)} bytes>' for k,v in dict(row).items()}
            found.append({'table': table, 'exact_lookup_key': key, 'record': record})
(root / 'STORE_EXACT_ROWS.json').write_text(json.dumps(found, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(found, ensure_ascii=False, indent=2))
print('Exact matches:', len(found), '; read-only connection; no store write.')
