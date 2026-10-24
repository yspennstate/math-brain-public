from pathlib import Path
import json
import sqlite3

db = Path('~/.agents/coordination/agent_mesh.sqlite3')
result = {'read_only': True, 'database': str(db)}
try:
    with sqlite3.connect(db.as_uri() + '?mode=ro', uri=True, timeout=3) as conn:
        conn.row_factory = sqlite3.Row
        result['agents'] = [dict(r) for r in conn.execute(
            'SELECT agent_id,campaign_id,status FROM agents WHERE agent_id IN (?,?,?,?)',
            ('w507', 'w508', 'w509', 'codex-01a12190'))]
        result['campaigns'] = [dict(r) for r in conn.execute(
            "SELECT campaign_id,name,status FROM campaigns WHERE name IN (?,?,?)",
            ('P0162-independent-bent-selector', 'P0162-review', 'probability300-integration'))]
except Exception as exc:
    result['error'] = str(exc)
root = Path(__file__).resolve().parent
(root / 'RESUME_ROUTES.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result))
