"""Read only the named mesh/resource records and one matched math card."""
import itertools
import json
import os
import sqlite3
import time
from pathlib import Path

root = Path(__file__).resolve().parent
mesh_path = Path(os.environ.get('AGENT_MESH_DB') or '~/.agents/coordination/agent_mesh.sqlite3')
con = sqlite3.connect(mesh_path.resolve().as_uri() + '?mode=ro', uri=True)
rows = con.execute("SELECT campaign_id,name,status FROM campaigns WHERE name LIKE '%prob%' ORDER BY rowid DESC LIMIT 8").fetchall()
peers = con.execute("SELECT a.agent_id,c.name,c.status FROM agents a LEFT JOIN campaigns c ON c.campaign_id=a.campaign_id WHERE a.agent_id IN ('w594','w595','w596','w588','w591','codex-01a12190')").fetchall()
con.close()
print('MESH', json.dumps({'campaigns': rows, 'peers': peers}, ensure_ascii=False))

state_path = Path('~/.claude/compute/compute_state.json')
state = json.loads(state_path.read_text(encoding='utf-8-sig'))
print('COMPUTE_KEYS', list(state))
for key in ('ts','timestamp','status','local','pc','laptop'):
    if key in state:
        value = state[key]
        if isinstance(value, dict):
            value = {k:v for k,v in value.items() if not any(w in k.lower() for w in ('process','azure','trading','remote','job'))}
        print('COMPUTE', key, json.dumps(value, ensure_ascii=False)[:5500])
print('COMPUTE_MTIME_AGE', time.time()-state_path.stat().st_mtime)

nodes = Path('~/math-brain-build/export/population/nodes.jsonl')
with nodes.open(encoding='utf-8-sig') as handle:
    line = next(itertools.islice(handle, 273, 274))
card = json.loads(line)
(root/'MATCHED_CARD.json').write_text(json.dumps(card, ensure_ascii=False, indent=2), encoding='utf-8')
print('MATCHED_CARD_KEYS', list(card))
print('MATCHED_CARD', json.dumps({k:v for k,v in card.items() if k != 'body'}, ensure_ascii=False)[:1800])
body = card.get('body','')
start = body.find('q=1')
print('MATCHED_CARD_QUOTE', body[max(0,start-80):start+350])

identity = {k:os.environ.get(k) for k in ('CODEX_THREAD_ID','CODEX_SESSION_ID','AGENT_MESH_ID') if os.environ.get(k)}
(root/'NATIVE_IDENTITY.json').write_text(json.dumps(identity, indent=2), encoding='utf-8')
print('IDENTITY', json.dumps(identity))
