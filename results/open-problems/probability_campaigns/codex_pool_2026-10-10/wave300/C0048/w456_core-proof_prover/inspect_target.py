"""Read-only, target-specific lookup; no store export or model load."""
from pathlib import Path
import json
import sqlite3

root = Path(__file__).resolve().parent
path = Path('~/math-brain-build/local/population/brain.sqlite3')
out = {"path": str(path), "mode": "ro", "target": "C0048", "rows": []}
with sqlite3.connect('file:' + path.as_posix() + '?mode=ro', uri=True, timeout=5) as conn:
    conn.execute('PRAGMA query_only=ON')
    tables = [row[0] for row in conn.execute("SELECT name FROM sqlite_master WHERE type='table' LIMIT 40")]
    out['tables'] = tables
    if 'claims' in tables:
        cols = [row[1] for row in conn.execute('PRAGMA table_info(claims)')]
        out['claim_columns'] = cols
        chosen = [name for name in ('id', 'title', 'statement', 'logical_name', 'namespace', 'metadata', 'status') if name in cols]
        if 'title' in cols:
            fields = ','.join('"' + name + '"' for name in chosen)
            cur = conn.execute('SELECT ' + fields + ' FROM claims WHERE title LIKE ? OR title LIKE ? LIMIT 8', ('%Discontinuity of the Potts phase transition%', '%C0048%'))
            for row in cur:
                out['rows'].append({name: value[:6500] if isinstance(value, str) else value for name, value in zip(chosen, row)})
        elif 'payload_json' in cols:
            query = "SELECT id,payload_json FROM claims WHERE json_extract(payload_json,'$.title') LIKE ? OR json_extract(payload_json,'$.title') LIKE ? LIMIT 8"
            for row_id, raw in conn.execute(query, ('%Discontinuity of the Potts phase transition%', '%C0048%')):
                payload = json.loads(raw)
                out['rows'].append({'id': row_id, 'payload': payload})
            if not out['rows']:
                target_ids = ('claim_38c945c83e6d9f9dc77b20f936b660e811e528c284f76bd513990e6ed06ecc6a', 'claim_9830d2b5c32b82afa88de780611e6b0fe5e81b7d425ff5fabff71dad19cc6930')
                for row_id, raw in conn.execute('SELECT id,payload_json FROM claims WHERE id IN (?,?)', target_ids):
                    out['rows'].append({'id': row_id, 'payload': json.loads(raw)})
            if not out['rows']:
                query = 'SELECT id,payload_json FROM claims WHERE payload_json LIKE ? OR payload_json LIKE ? LIMIT 8'
                for row_id, raw in conn.execute(query, ('%potts_discontinuity_d3_q3%', '%C0048%')):
                    out['rows'].append({'id': row_id, 'payload': json.loads(raw)})
(root / 'store_target_lookup.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, ensure_ascii=False))
