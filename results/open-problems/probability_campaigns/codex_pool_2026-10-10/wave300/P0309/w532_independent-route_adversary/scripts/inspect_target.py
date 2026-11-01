"""Read only the target's index entry and store schema; never export a store."""
import json
import sqlite3
from pathlib import Path

root = Path('~/<private-repo>/06_math_research')
index = root / 'probability_1000_intake_F_20260908/raw/dedup_index.json'
matches = []

def walk(obj, pointer=''):
    if isinstance(obj, dict):
        if any(isinstance(v, str) and (v == 'P0309' or 'cryst' in v.lower() or 'riesz' in v.lower()) for v in obj.values()):
            matches.append({'pointer': pointer, 'record': obj})
        for k, v in obj.items():
            if k == 'P0309' or 'cryst' in k.lower() or 'riesz' in k.lower():
                matches.append({'pointer': pointer + '/' + k, 'record': v})
            walk(v, pointer + '/' + k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            walk(v, pointer + '/' + str(i))

with index.open(encoding='utf-8-sig') as handle:
    payload = json.load(handle)
    print(json.dumps({'index_type': type(payload).__name__, 'length': len(payload), 'sample_keys': list(payload)[:6] if isinstance(payload, dict) else []})[:1000])
    walk(payload)
Path('target_index_matches.json').write_text(json.dumps(matches, ensure_ascii=False, indent=2), encoding='utf-8')
for match in matches:
    print(json.dumps(match, ensure_ascii=False)[:10000])

intake_matches = []
for intake in sorted(root.glob('probability_1000_intake_*')):
    records = intake / 'problems.jsonl'
    if not records.is_file():
        continue
    with records.open(encoding='utf-8-sig') as handle:
        for line_no, line in enumerate(handle, 1):
            if not any(term in line.lower() for term in ('riesz', 'crystall', 'p0309')):
                continue
            row = json.loads(line)
            evidence = {'path': str(records), 'line': line_no, 'record': row}
            intake_matches.append(evidence)
            print(json.dumps(evidence, ensure_ascii=False)[:5000])
Path('target_intake_matches.json').write_text(json.dumps(intake_matches, ensure_ascii=False, indent=2), encoding='utf-8')

store = Path('~/math-brain-build/local/population/brain.sqlite3')
with sqlite3.connect('file:' + store.as_posix() + '?mode=ro', uri=True, timeout=5) as connection:
    connection.execute('PRAGMA query_only=ON')
    for name, schema in connection.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name IN ('nodes','cards','claims','sources','reflexes')"):
        print(json.dumps({'table': name, 'schema': schema}, ensure_ascii=False))
    for row in connection.execute("SELECT id, kind, title, body, metadata_json FROM nodes WHERE body LIKE '%P0309%' OR title LIKE '%crystall%Riesz%' LIMIT 8"):
        print(json.dumps({'store_match': row}, ensure_ascii=False)[:6500])
