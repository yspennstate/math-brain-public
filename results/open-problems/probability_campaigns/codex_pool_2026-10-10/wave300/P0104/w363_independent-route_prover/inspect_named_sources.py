"""Targeted local P0104 records and read-only math-store lookup."""
import json
from pathlib import Path
import sqlite3

root = Path(__file__).parent
campaign = Path('~/.codex/worktrees/probability-1000-20h-20260906/06_math_research/probability_1000_20h_20260906')
result = {'target': 'P0104', 'files': {}, 'source_records': []}
source_ids = set()
for filename in ['problems.jsonl', 'attempts.jsonl']:
    path = campaign / filename
    matches = []
    if path.exists():
        with path.open(encoding='utf-8') as stream:
            for number, line in enumerate(stream, 1):
                if 'P0104' not in line:
                    continue
                row = json.loads(line)
                if row.get('problem_id') == 'P0104':
                    matches.append({'line': number, 'record': row})
                    if row.get('source_id'):
                        source_ids.add(row['source_id'])
    result['files'][str(path)] = matches
path = campaign / 'sources.jsonl'
if path.exists():
    with path.open(encoding='utf-8') as stream:
        for number, line in enumerate(stream, 1):
            if not any(s in line for s in source_ids):
                continue
            row = json.loads(line)
            if row.get('source_id') in source_ids:
                result['source_records'].append({'path': str(path), 'line': number, 'record': row})
(root/'PRIOR_RECORDS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))

path = Path('~/math-brain-build/local/population/brain.sqlite3')
lookup = {'uri': 'file:'+path.as_posix()+'?mode=ro', 'tables': [], 'matches': []}
if path.exists():
    connection = sqlite3.connect(lookup['uri'], uri=True)
    connection.execute('PRAGMA query_only=ON')
    tables = [r[0] for r in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('cards','nodes')")]
    lookup['tables'] = tables
    for table in tables:
        columns = [r[1] for r in connection.execute(f'PRAGMA table_info({table})')]
        lookup[table+'_columns'] = columns
        label = next((c for c in ['logical_name','logical_id','title','name'] if c in columns), None)
        if label:
            wanted = [c for c in ['id','logical_id','namespace','logical_name','title','statement','kind'] if c in columns]
            rows = connection.execute(f"SELECT {','.join(wanted)} FROM {table} WHERE {label} LIKE ? LIMIT 6", ('%p0104%',)).fetchall()
            lookup['matches'] += [dict(zip(wanted,row)) for row in rows]
    connection.close()
(root/'BRAIN_LOOKUP.json').write_text(json.dumps(lookup,indent=2)+'\n',encoding='utf-8')
print(json.dumps(lookup,indent=2))
