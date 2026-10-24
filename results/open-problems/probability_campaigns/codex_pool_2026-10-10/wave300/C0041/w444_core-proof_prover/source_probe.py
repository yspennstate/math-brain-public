"""Extract only C0041's top-level intake records; never load a store export."""
import json
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE = Path('~/<private-repo>/06_math_research')
intake = BASE / 'probability_1000_intake_claude_20260907'
record = {'candidate': 'C0041', 'top_level_intake_files': [], 'exact_records': [], 'prior_directory_files': {}}
for path in sorted(intake.iterdir()):
    if path.is_file():
        record['top_level_intake_files'].append({'name': path.name, 'bytes': path.stat().st_size})
    if path.is_file() and path.suffix == '.jsonl':
        with path.open(encoding='utf-8-sig', errors='replace') as handle:
            for lineno, line in enumerate(handle, 1):
                if '"C0041"' not in line:
                    continue
                value = json.loads(line)
                if any(value.get(k) == 'C0041' for k in ['problem_id', 'candidate_id', 'id']):
                    record['exact_records'].append({'path': str(path), 'line': lineno, 'record': value})
for name in ['probability_1000_attempts_H_20260912', 'probability_1000_attempts_I_20260914', 'prob1000_lean_20260908']:
    directory = BASE / name
    record['prior_directory_files'][name] = [str(p.relative_to(directory)) for p in directory.iterdir()][:35]
bundle = intake / 'brain_bundle_C007.json'
if bundle.is_file() and bundle.stat().st_size < 300000:
    value = json.loads(bundle.read_text(encoding='utf-8-sig'))
    record['prior_bundle_matching_entries'] = [e for e in value.get('entries', []) if 'C0041' in json.dumps(e)]
dbpath = Path('~/math-brain-build/local/population/brain.sqlite3')
if dbpath.is_file():
    with sqlite3.connect(dbpath.as_uri() + '?mode=ro', uri=True, timeout=3) as conn:
        names = [row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")]
        record['read_only_store_tables'] = names
        record['candidate_tables'] = {}
        for name in names:
            if name in ['cards', 'nodes', 'entries']:
                record['candidate_tables'][name] = [row[1] for row in conn.execute('PRAGMA table_info("' + name + '")')]
(ROOT / 'REPORT_SOURCE_RECORDS.json').write_text(json.dumps(record, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(record, ensure_ascii=False, indent=2)[:22000])
