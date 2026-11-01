"""Bounded read-only recovery of the named P0043 records and store cards."""
import json
import os
import sqlite3
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent


def ro(path):
    conn = sqlite3.connect('file:' + Path(path).as_posix() + '?mode=ro', uri=True, timeout=2)
    deadline = time.monotonic() + 4
    conn.set_progress_handler(lambda: int(time.monotonic() > deadline), 1000)
    conn.row_factory = sqlite3.Row
    return conn


out = {'records': [], 'stores': [], 'teams': []}
base = Path('~/Downloads/Probability_1000_20h_20260906')
for filename in ('problems.jsonl', 'attempts.jsonl'):
    path = base / filename
    if path.exists():
        with path.open(encoding='utf-8') as stream:
            for line_number, line in enumerate(stream, 1):
                if 'P0043' not in line:
                    continue
                row = json.loads(line)
                if row.get('problem_id') == 'P0043':
                    out['records'].append({'path': str(path), 'line': line_number, 'record': row})

mesh_path = Path(os.environ.get('AGENT_MESH_DB') or '~/.agents/coordination/agent_mesh.sqlite3')
try:
    with ro(mesh_path) as conn:
        out['teams'] = [dict(r) for r in conn.execute("SELECT campaign_id, name FROM campaigns WHERE status='active' AND (name LIKE '%prob%' OR name LIKE '%W0300%' OR campaign_id IN (SELECT campaign_id FROM agents WHERE agent_id IN ('w433','w434','w344'))) LIMIT 12")]
except (OSError, sqlite3.Error) as exc:
    out['mesh_error'] = str(exc)

for path in (Path('~/math-brain-build/local/population/brain.sqlite3'),):
    record = {'path': str(path)}
    try:
        with ro(path) as conn:
            record['schema'] = {r[0]: [c['name'] for c in conn.execute('PRAGMA table_info(' + r[0] + ')')] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('nodes','edges','sources')")}
            if 'nodes' in record['schema']:
                fields = [f for f in ('id', 'namespace', 'logical_name', 'kind', 'title', 'body') if f in record['schema']['nodes']]
                record['cards'] = [dict(r) for r in conn.execute('SELECT ' + ','.join(fields) + " FROM nodes WHERE title LIKE '%critical percolation%' OR title LIKE '%criticality on quasi%' OR title LIKE '%quasi-transitive%' LIMIT 12")]
    except (OSError, sqlite3.Error) as exc:
        record['error'] = str(exc)
    out['stores'].append(record)

for name in ('math-research-brain', 'math_research_brain'):
    path = Path('~') / name
    out.setdefault('canonical_path_checks', []).append({'path': str(path), 'exists': path.exists()})

(ROOT / 'INPUT_RECEIPT.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False))
