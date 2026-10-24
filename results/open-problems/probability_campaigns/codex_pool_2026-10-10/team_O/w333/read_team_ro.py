import json,sqlite3
from pathlib import Path
ROOT=Path(__file__).resolve().parent
conn=sqlite3.connect('file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro',uri=True)
conn.execute('PRAGMA query_only=ON')
conn.row_factory=sqlite3.Row
rows=[dict(row) for row in conn.execute('SELECT message_id,sender_agent,topic,kind,body,created_at FROM messages WHERE recipient=? AND acked_at IS NULL ORDER BY created_at DESC LIMIT 8',('w333',))]
(ROOT/'reports/team_inbox_readonly.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
for row in rows:
    print(json.dumps(row,ensure_ascii=False))
if not rows: print('w333: no unread directed messages; read-only mesh connection, no acknowledgements written.')
