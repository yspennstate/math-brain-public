import json
from pathlib import Path
import sqlite3
import time

root = Path(__file__).resolve().parent
db = '~/math-brain-build/local/population/brain.sqlite3'
con = sqlite3.connect('file:' + db + '?mode=ro', uri=True, timeout=5)
con.row_factory = sqlite3.Row
started = time.perf_counter()
rows = [dict(r) for r in con.execute("SELECT n.id,n.kind,n.title,n.body,n.metadata_json,c.payload_json FROM nodes n LEFT JOIN claims c ON c.id=n.id WHERE n.title LIKE '%sublinear%' OR n.title LIKE '%P0104%' OR n.title LIKE '%passage%fluctuation%' OR (n.title LIKE '%KPZ%' AND n.body LIKE '%passage%') ORDER BY n.title LIMIT 18")]
(root / 'target_nodes.json').write_text(json.dumps(rows, indent=2), encoding='utf-8')
print(json.dumps({'elapsed_seconds':round(time.perf_counter()-started,3), 'nodes':[{'id':r['id'],'kind':r['kind'],'title':r['title'],'body_preview':r['body'][:220]} for r in rows]}, ensure_ascii=False))
con.close()
mesh = sqlite3.connect('file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro', uri=True, timeout=5)
mesh.row_factory = sqlite3.Row
messages = [dict(r) for r in mesh.execute("SELECT created_at,sender_agent,recipient,topic,kind,body FROM messages WHERE recipient='w370' OR (sender_agent IN ('w369','w371') AND (topic LIKE '%P0104%' OR body LIKE '%P0104%')) ORDER BY created_at DESC LIMIT 8")]
(root / 'peer_messages.json').write_text(json.dumps(messages, indent=2), encoding='utf-8')
print('PEER_MESSAGES', json.dumps(messages, ensure_ascii=False))
mesh.close()
research = Path('~/<private-repo>/06_math_research')
print('PROBABILITY_DIRS', [p.name for p in research.iterdir() if p.is_dir() and ('prob' in p.name.lower() or 'kesten' in p.name.lower())])
