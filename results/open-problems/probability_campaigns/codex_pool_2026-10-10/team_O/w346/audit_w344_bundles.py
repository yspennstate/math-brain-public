"""Independently verify w344's proposed edge endpoints against draft/store text."""
import json
import re
import sqlite3
from pathlib import Path

root = Path('~/brain_workers/w344')
db = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro', uri=True)
results = []
for i in range(1, 11):
    path = root / 'drafts' / f'bundle_{i:03}.json'
    bundle = json.loads(path.read_text(encoding='utf-8'))
    entries = {e['key']: e for e in bundle['entries']}
    errors = []
    for rel in bundle['relations']:
        key = rel['from_key']
        quotes = re.findall(r'"([^\"]*)"', rel['rationale'])
        if key not in entries or len(quotes) < 2:
            errors.append([key, 'missing from entry or pair of quotes'])
            continue
        first, second = quotes[:2]
        if first not in entries[key]['statement']:
            errors.append([key, 'new-end quote mismatch', first])
        if 'to_key' in rel:
            target = entries.get(rel['to_key'])
            if target is None or second not in target['statement']:
                errors.append([key, 'draft target quote mismatch', rel['to_key'], second])
        else:
            logical = rel['to_existing_logical']
            bodies = db.execute("SELECT body FROM nodes WHERE json_extract(metadata_json,'$.logical_id')=?", (logical,)).fetchall()
            if not bodies:
                errors.append([key, 'store target absent', logical])
            elif not any(second in body for (body,) in bodies):
                errors.append([key, 'store target quote mismatch', logical, second])
    results.append({'bundle': i, 'entries': len(entries), 'relations': len(bundle['relations']), 'endpoint_quotes': 2*len(bundle['relations']), 'errors': errors})
out = Path(__file__).with_name('w344_bundle_validation.json')
out.write_text(json.dumps(results, indent=2), encoding='utf-8')
print(json.dumps(results))
