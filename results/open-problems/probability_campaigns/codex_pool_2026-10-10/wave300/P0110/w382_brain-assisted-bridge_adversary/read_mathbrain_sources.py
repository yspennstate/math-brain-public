"""Read only the exact P0110 cards already identified; save a source report."""
from pathlib import Path
import json
import sqlite3
import time

ROOT = Path(__file__).resolve().parent
DB = Path('~/math-brain-build/local/population/brain.sqlite3')
TARGETS = [
    'claim_081071dcf812e1c0843a53fe1da486f97876afe30678a091de36c26017e679f0',
    'claim_a60b9dcbea1c3b4133831211a8107b42fbce24f2c59d8b4b21ede96b3cab07f1',
    'claim_8a17e4ab36fa0ae9d777f6fbb2a993eb6ea86c1cf88c8d574bba5a789944a958',
]
started = time.perf_counter()
rows = []
with sqlite3.connect(DB.as_uri()+'?mode=ro', uri=True, timeout=10) as con:
    for node_id in TARGETS:
        row = con.execute('SELECT id,title,body,metadata_json FROM nodes WHERE id=?', (node_id,)).fetchone()
        if row is None:
            rows.append({'id': node_id, 'found': False})
            continue
        metadata = json.loads(row[3])
        rows.append({'id': row[0], 'title': row[1], 'body': row[2], 'found': True,
            'metadata': {key: metadata.get(key) for key in (
                'logical_id', 'claim_kind', 'proof_text', 'source_id', 'source_revision',
                'truth_status', 'supersedes', 'statement_fidelity_reviewed')}})
report = {'command': 'python -X utf8 read_mathbrain_sources.py', 'database': str(DB),
    'connection': 'mode=ro', 'query_scope': 'three exact public-math campaign source cards',
    'elapsed_seconds': round(time.perf_counter()-started,6), 'rows': rows,
    'status': 'Retrieved source cards, not a proof or independent audit.'}
(ROOT/'BRAIN_SOURCE_REPORT.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
for row in rows:
    title = row.get('title','')
    print(json.dumps({'id':row['id'], 'title':title[:180], 'body':row.get('body'), 'metadata':row.get('metadata')}))
