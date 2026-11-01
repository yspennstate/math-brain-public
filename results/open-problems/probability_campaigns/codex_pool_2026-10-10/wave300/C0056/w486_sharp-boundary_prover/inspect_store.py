"""Scoped C0056 reads only. The live SQLite database is opened read-only."""
import json
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
export = Path('~/math-brain-build/export/population/nodes.jsonl')
selected = {310, 319, 1266}
receipt = {'export_matches': [], 'live_matches': [], 'live_database_mode': 'ro'}


def summarize(row):
    out = {k: row[k] for k in ('id', 'logical_name', 'namespace', 'kind', 'status', 'title') if k in row}
    for key in ('payload_json', 'node_json'):
        if key in row:
            payload = json.loads(row[key]) if isinstance(row[key], str) else row[key]
            for name in ('logical_name', 'namespace', 'kind', 'status', 'title', 'statement'):
                if name in payload:
                    out[name] = str(payload[name])[:1600]
    return out


with export.open(encoding='utf-8') as stream:
    for number, line in enumerate(stream, 1):
        if number in selected:
            receipt['export_matches'].append({'line': number, **summarize(json.loads(line))})
        if number == max(selected):
            break

database = Path('~/math-brain-build/local/population/brain.sqlite3')
try:
    started = time.monotonic()
    with sqlite3.connect('file:' + database.as_posix() + '?mode=ro', uri=True, timeout=3) as connection:
        connection.row_factory = sqlite3.Row
        connection.set_progress_handler(lambda: int(time.monotonic() - started > 5), 10000)
        tables = {row[0] for row in connection.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','claims')")}
        for table in sorted(tables):
            columns = {row[1] for row in connection.execute('PRAGMA table_info(' + table + ')')}
            if 'payload_json' not in columns:
                continue
            for row in connection.execute('SELECT * FROM ' + table + " WHERE payload_json LIKE '%C0056%' LIMIT 4"):
                receipt['live_matches'].append({'table': table, **summarize(dict(row))})
    receipt['live_check'] = 'Completed scoped read; these rows do not establish current mathematical openness.'
except (sqlite3.Error, OSError) as error:
    receipt['live_check'] = 'Unavailable within scoped read: ' + str(error)

(ROOT / 'STORE_SCOPE.json').write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
print(json.dumps(receipt))
