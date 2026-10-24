"""Bounded read-only peer routing and Ising-card lookup. No live-store writes."""
import json
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
mesh = sqlite3.connect('file:~/.agents/coordination/agent_mesh.sqlite3?mode=ro', uri=True, timeout=3)
schema = mesh.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND (name LIKE '%campaign%' OR name LIKE '%member%')").fetchall()
print('MESH_SCHEMA', json.dumps(schema)[:5000])
if any(name == 'campaigns' for name, _ in schema):
    cols = {r[1] for r in mesh.execute('PRAGMA table_info(campaigns)')}
    if {'campaign_id', 'name', 'status'} <= cols:
        names = mesh.execute("SELECT campaign_id,name,status FROM campaigns WHERE status='active' AND (name LIKE '%prob%' OR name LIKE '%brain%' OR name LIKE '%C0052%' OR name LIKE '%proof%') ORDER BY name LIMIT 12").fetchall()
        if not names:
            names = mesh.execute("SELECT campaign_id,name,status FROM campaigns WHERE status='active' LIMIT 3").fetchall()
        (ROOT / 'PEER_ROUTE.json').write_text(json.dumps(names, indent=2), encoding='utf-8')
        print('EXISTING_TEAMS', json.dumps(names))
mesh.close()
if '--routing-only' in sys.argv:
    raise SystemExit(0)

store = sqlite3.connect('file:~/math-brain-build/local/population/brain.sqlite3?mode=ro', uri=True, timeout=3)
rows = store.execute("SELECT id,kind,title,body,metadata_json FROM nodes WHERE title LIKE '%Ising%' AND (title LIKE '%3D%' OR title LIKE '%three%' OR title LIKE '%trivial%') LIMIT 5").fetchall()
evidence = [dict(zip(('id','kind','title','body','metadata_json'), row)) for row in rows if re.search(r'\bIsing\b',row[2],re.I)]
(ROOT / 'STORE_EVIDENCE.json').write_text(json.dumps(evidence, indent=2, ensure_ascii=False), encoding='utf-8')
print('ISING_CARDS', json.dumps([{'id':r['id'],'kind':r['kind'],'title':r['title'],'body_quote':r['body'][:700]} for r in evidence], ensure_ascii=False))
store.close()
