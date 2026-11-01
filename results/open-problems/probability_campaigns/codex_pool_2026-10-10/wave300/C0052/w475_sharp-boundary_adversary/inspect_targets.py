"""Bounded read-only lookups for the assigned target and its peer-routing metadata."""
from pathlib import Path
import sqlite3
import json

root = Path(__file__).resolve().parent
mesh_code = Path('~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py')
lines = mesh_code.read_text(encoding='utf-8').splitlines()
print('Mesh default-path definitions:')
for line in lines[:65]:
    if 'DEFAULT_HOME' in line or 'DEFAULT_DB' in line or 'AGENT_MESH' in line:
        print(line)

store_path = Path('~/math-brain-build/local/population/brain.sqlite3')
store = sqlite3.connect(store_path.as_uri()+'?mode=ro', uri=True, timeout=3)
store.execute('PRAGMA query_only=ON')
targets = ['claim_93dc043f691fa62549866c90e84e26aa836d69164fd798c69ba9c0dc431b1fc0']
found = []
for target in targets:
    row = store.execute('SELECT id,title,body,metadata_json FROM nodes WHERE id=?',(target,)).fetchone()
    if row:
        metadata = json.loads(row[3])
        found.append({'id':row[0],'title':row[1],'body':row[2],
                      'logical_id':metadata.get('logical_id'),
                      'truth_status':metadata.get('truth_status')})
store.close()
(root/'live_target_receipt.json').write_text(json.dumps({'store_mode':'read-only','targets':found},indent=2)+'\n',encoding='utf-8')
print(json.dumps({'live_target_rows':len(found),'logical_ids':[r['logical_id'] for r in found]}))
