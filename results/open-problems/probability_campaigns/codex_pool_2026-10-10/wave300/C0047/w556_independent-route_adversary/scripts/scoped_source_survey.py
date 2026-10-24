"""Read only C0047 rows and their cited sources; write evidence inside w556."""
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = Path('~/<private-repo>/06_math_research')
FOLDERS = sorted(ROOT.glob('probability_1000_intake_*')) + [
    ROOT / 'probability_1000_attempts_H_20260912',
    ROOT / 'probability_1000_attempts_I_20260914',
    ROOT / 'prob1000_lean_20260908',
]
records = []
coverage = []

def target(row):
    if not isinstance(row, dict):
        return False
    return any(row.get(k) == 'C0047' for k in ('problem_id', 'dedup_key', 'candidate_id', 'id'))

for folder in FOLDERS:
    files = sorted(folder.glob('*.jsonl')) if folder.is_dir() else []
    source_ids = set()
    matched = 0
    for path in files:
        if 'retrieval' in path.name or 'source_failures' in path.name:
            continue
        for number, line in enumerate(path.open(encoding='utf-8-sig'), 1):
            if 'C0047' not in line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            if target(row):
                records.append({'path': str(path), 'line': number, 'row': row,
                                'row_sha256': hashlib.sha256(line.encode()).hexdigest()})
                source_ids.add(row.get('source_id'))
                matched += 1
    sources = folder / 'sources.jsonl'
    if sources.is_file() and source_ids:
        for number, line in enumerate(sources.open(encoding='utf-8-sig'), 1):
            row = json.loads(line)
            if row.get('source_id') in source_ids:
                records.append({'path': str(sources), 'line': number, 'row': row,
                                'row_sha256': hashlib.sha256(line.encode()).hexdigest()})
    coverage.append({'folder': str(folder), 'exact_C0047_rows': matched,
                     'scope': 'top-level jsonl target-id rows only',
                     'absence_is_not_retired_status': True})

out = {'target': 'C0047', 'records': records, 'coverage': coverage}
(HERE / 'SCOPED_PRIOR_RECORDS.json').write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding='utf-8')
for item in records:
    row = item['row']
    keep = {k: row[k] for k in ('problem_id', 'attempt_id', 'source_id', 'title',
                              'statement', 'locator', 'url', 'method', 'obstruction',
                              'current_status', 'historical_status', 'result_status') if k in row}
    print(json.dumps({'path': item['path'], 'line': item['line'], 'fields': keep}, ensure_ascii=False))
print(json.dumps({'coverage': coverage}, ensure_ascii=False))
