"""Read only the exact historical C0017 target/attempt ids; never write SQLite."""
from pathlib import Path
import json
import sqlite3

ROOT = Path(__file__).resolve().parent
PATHS = [Path('~/math-brain-build/local/population/brain.sqlite3'),
         Path('~/math-research-brain/local/brain.sqlite3'),
         Path('~/math-research-brain/local/math_brain.sqlite3')]
TARGETS = ['claim_91f295e6d2a67634c0b90a5ee4130c1feed72dc0fe16086a679021c90c8917cb',
           'claim_07a861a72ebeb008dc23e9db32147327c062427adee7a530bab01f0de67bd002']
receipts = []
for path in PATHS:
    receipt = {'path': str(path), 'mode': 'ro', 'exists': path.exists(), 'rows': []}
    if path.exists():
        try:
            with sqlite3.connect('file:' + path.as_posix() + '?mode=ro', uri=True, timeout=2) as connection:
                connection.execute('PRAGMA query_only=ON')
                schema = {r[1] for r in connection.execute('PRAGMA table_info(nodes)')}
                if {'id', 'title', 'body', 'metadata_json'} <= schema:
                    for target in TARGETS:
                        row = connection.execute('SELECT id,title,body,metadata_json FROM nodes WHERE id=? LIMIT 1', (target,)).fetchone()
                        if row:
                            receipt['rows'].append(dict(zip(['id', 'title', 'body', 'metadata_json'], row)))
                else:
                    receipt['note'] = 'Exact expected population node schema absent; no broader query attempted.'
        except sqlite3.Error as exc:
            receipt['error'] = str(exc)
    receipts.append(receipt)
(ROOT / 'STORE_READ_RECEIPT.json').write_text(json.dumps(receipts, indent=2) + '\n', encoding='utf-8')
print(json.dumps([{'path': r['path'], 'exists': r['exists'], 'matched_target_rows': len(r['rows']),
                  'error': r.get('error'), 'note': r.get('note')} for r in receipts], indent=2))
