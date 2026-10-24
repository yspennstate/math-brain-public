"""ID-filtered prior records and a read-only, time-bounded math-store lookup."""
import json
from pathlib import Path
import re
import sqlite3
import time

ROOT = Path(__file__).resolve().parent
INTAKE = Path('~/<private-repo>/06_math_research/probability_1000_intake_claude_20260907')
receipt = {'candidate': 'C0017', 'intake_records': {}, 'export_nodes': [], 'store_read_only': True}
for filename in ('problems.jsonl', 'attempts.jsonl'):
    selected = []
    with (INTAKE / filename).open(encoding='utf-8') as stream:
        for number, line in enumerate(stream, 1):
            if 'C0017' not in line:
                continue
            row = json.loads(line)
            if row.get('problem_id') == 'C0017':
                selected.append({'line': number, 'record': row})
    receipt['intake_records'][filename] = selected
export_path = Path('~/math-brain-build/export/population/nodes.jsonl')
with export_path.open(encoding='utf-8') as stream:
    for number, line in enumerate(stream, 1):
        if 'C0017' not in line:
            continue
        row = json.loads(line)
        receipt['export_nodes'].append({'line': number, 'record': row})
        if len(receipt['export_nodes']) == 3:
            break

store_path = Path('~/math-brain-build/local/population/brain.sqlite3')
receipt['store_path'] = str(store_path)
if store_path.is_file():
    connection = sqlite3.connect('file:' + store_path.as_posix() + '?mode=ro', uri=True, timeout=2)
    started = time.monotonic()
    connection.set_progress_handler(lambda: int(time.monotonic() - started > 5), 10000)
    try:
        names = [row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table'")]
        receipt['store_schema'] = {}
        for name in names:
            if not re.fullmatch(r'[A-Za-z0-9_]+', name):
                continue
            if name not in ('nodes', 'cards', 'claims'):
                continue
            columns = [row[1] for row in connection.execute(f'PRAGMA table_info("{name}")')]
            receipt['store_schema'][name] = columns
            if name == 'nodes':
                search_columns = [c for c in ('logical_name', 'title') if c in columns]
                if search_columns:
                    where = ' OR '.join(f'"{column}" LIKE ?' for column in search_columns)
                    args = ['%c0017%' if column == 'logical_name' else '%Conformal invariance%critical bond%square%'
                            for column in search_columns]
                    selected = list(connection.execute(f'SELECT * FROM "{name}" WHERE {where} LIMIT 3', args))
                    receipt['store_matches'] = [dict(zip(columns, row)) for row in selected]
        receipt['store_lookup_status'] = 'read-only lookup completed'
    except sqlite3.Error as error:
        receipt['store_lookup_status'] = f'bounded lookup incomplete: {error}'
    finally:
        connection.close()
else:
    receipt['store_lookup_status'] = 'named store path absent'
(ROOT / 'LOCAL_SOURCE_RECEIPT.json').write_text(json.dumps(receipt, indent=2, ensure_ascii=False), encoding='utf-8')
print(json.dumps(receipt, indent=2, ensure_ascii=False)[:11000])
