"""Read only the named target cards and this worker's mesh inbox."""
from datetime import datetime, timezone
from pathlib import Path
import json
import os
import sqlite3

ROOT = Path(__file__).resolve().parent
result = {'read_utc': datetime.now(timezone.utc).isoformat(), 'live_target_cards': [],
          'mesh_messages': [], 'errors': []}
probe = json.loads((ROOT / 'SOURCE_PROBE.json').read_text(encoding='utf-8'))
db = Path('~/math-brain-build/local/population/brain.sqlite3')
try:
    con = sqlite3.connect(db.as_uri() + '?mode=ro', uri=True, timeout=3)
    con.row_factory = sqlite3.Row
    for item in probe['export_matches']:
        node = con.execute('SELECT * FROM nodes WHERE id=?', (item['record']['id'],)).fetchone()
        if node:
            result['live_target_cards'].append(dict(node))
    con.close()
except Exception as exc:
    result['errors'].append('Target cards: ' + str(exc))

mesh_path = Path(os.environ.get('AGENT_MESH_DB') or
                 '~/.agents/coordination/agent_mesh.sqlite3')
try:
    con = sqlite3.connect(mesh_path.as_uri() + '?mode=ro', uri=True, timeout=3)
    con.row_factory = sqlite3.Row
    columns = [row[1] for row in con.execute('PRAGMA table_info(messages)')]
    result['mesh_columns'] = columns
    recipient = next((name for name in ('to_agent', 'recipient', 'recipient_agent', 'to_agent_id')
                      if name in columns), None)
    if recipient:
        order = next((name for name in ('created_at', 'message_id') if name in columns), recipient)
        sql = f'SELECT * FROM messages WHERE "{recipient}"=? ORDER BY "{order}" DESC LIMIT 8'
        result['mesh_messages'] = [dict(row) for row in con.execute(sql, ('w367',))]
    else:
        result['errors'].append('Mesh recipient column not identified; no unfiltered read performed.')
    con.close()
except Exception as exc:
    result['errors'].append('Mesh peek: ' + str(exc))

(ROOT / 'TARGET_CONTEXT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps({'live_target_cards': len(result['live_target_cards']),
                  'mesh_messages': result['mesh_messages'], 'errors': result['errors']}, ensure_ascii=False)[:5000])
