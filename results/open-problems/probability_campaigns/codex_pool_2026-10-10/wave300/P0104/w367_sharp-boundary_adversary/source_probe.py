"""Narrow, read-only source probe; never loads an entire store export."""
from pathlib import Path
import json
import sqlite3
import subprocess

ROOT = Path(__file__).resolve().parent
DB = Path('~/math-brain-build/local/population/brain.sqlite3')
report = {'sqlite': [], 'export_matches': [], 'errors': []}
try:
    con = sqlite3.connect(DB.as_uri() + '?mode=ro', uri=True, timeout=3)
    con.execute('PRAGMA query_only=ON')
    tables = con.execute('SELECT name, sql FROM sqlite_master WHERE type=?', ('table',)).fetchall()
    for name, schema in tables:
        if any(word in name.lower() for word in ('node', 'card', 'source', 'problem')):
            report['sqlite'].append({'table': name, 'schema': schema})
    con.close()
except Exception as exc:
    report['errors'].append(type(exc).__name__ + ': ' + str(exc))

export = Path('~/math-brain-build/export/population/nodes.jsonl')
if export.exists():
    try:
        match = subprocess.run(['rg', '-n', '-i', '-m', '6',
                                'P0104|Subdiffusive and KPZ passage', str(export)],
                               capture_output=True, text=True, encoding='utf-8', timeout=20)
        for line in match.stdout.splitlines():
            line_number, raw = line.split(':', 1)
            item = json.loads(raw)
            report['export_matches'].append({'line': int(line_number), 'record': item})
        report['export_rg_exit'] = match.returncode
    except Exception as exc:
        report['errors'].append(type(exc).__name__ + ': ' + str(exc))

(ROOT / 'SOURCE_PROBE.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
for item in report['sqlite']:
    print(item['table'], item['schema'][:1600])
for item in report['export_matches']:
    print('TARGET EXPORT ROW', json.dumps(item, ensure_ascii=False)[:5000])
for error in report['errors']:
    print('PROBE ERROR', error)
