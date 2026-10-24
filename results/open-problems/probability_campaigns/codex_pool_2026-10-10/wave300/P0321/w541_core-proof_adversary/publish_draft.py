"""Publish only the complete concept draft to the task-authorized worker inbox."""
from pathlib import Path
from datetime import datetime,timezone
import json
import os

root=Path(__file__).resolve().parent
inbox=Path('~/math-brain-inbox/w541')
expected=Path('~/math-brain-inbox/w541').resolve()
assert inbox.resolve()==expected
validation=json.loads((root/'VALIDATION.json').read_text(encoding='utf-8'))
assert validation['status']=='pass' and validation['theorem_promotions']==0
payload=(root/'bundle_001.json').read_bytes()
inbox.mkdir(parents=True,exist_ok=True)
for number in range(1,1000):
    final=inbox/f'bundle_{number:03}.json'
    part=inbox/f'bundle_{number:03}.part'
    if not final.exists() and not part.exists(): break
else:
    raise RuntimeError('No unused draft slot; do not overwrite or remove other work')
assert final.parent.resolve()==expected and part.parent.resolve()==expected
with part.open('xb') as out:
    out.write(payload)
    out.flush()
    os.fsync(out.fileno())
part.rename(final)
assert final.read_bytes()==payload
state=json.loads((root/'SUBMISSION_STATE.json').read_text(encoding='utf-8'))
state.update({'submitted':True,'submitted_at':datetime.now(timezone.utc).isoformat(),'submitted_path':str(final),'reviewed':False,'ingested':False,'retrievable':'not checked; submitted as concept draft only'})
(root/'SUBMISSION_STATE.json').write_text(json.dumps(state,indent=2)+'\n',encoding='utf-8')
print(json.dumps(state))
