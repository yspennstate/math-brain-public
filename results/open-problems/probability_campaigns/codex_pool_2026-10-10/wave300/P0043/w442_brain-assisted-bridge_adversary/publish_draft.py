"""Submit only this worker's validated concept draft, never write the live store."""
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
receipt=json.loads((ROOT/'VALIDATION.json').read_text(encoding='utf-8'))
assert receipt['passed']==9 and not receipt['live_store_written']
bundle=json.loads((ROOT/'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
assert len(bundle['entries'])==8 and len(bundle['relations'])==5
assert all(row['kind'] in {'concept','definition'} and row['proof_text'] is None for row in bundle['entries'])
destination=Path('~/math-brain-inbox/w442').resolve()
assert destination.parent==Path('~/math-brain-inbox').resolve() and destination.name=='w442'
destination.mkdir(exist_ok=True)
for number in range(1,1000):
    final=destination/f'bundle_{number:03d}.json'
    part=destination/f'bundle_{number:03d}.part'
    if not final.exists() and not part.exists():
        break
else:
    raise RuntimeError('no unused bundle number')
with part.open('x',encoding='utf-8',newline='\n') as handle:
    handle.write(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n')
part.rename(final)
states={'target':'P0043','bundle_path':str(final),'prepared':True,'submitted':True,
        'reviewed':False,'ingested':False,'retrievable':False,
        'independent_referee':'w443 (request pending; direct mesh delivery failed because unregistered)',
        'integrator_run':False,'entries':8,'draft_relations':5,'live_store_written':False}
(ROOT/'BUNDLE_STATES.json').write_text(json.dumps(states,indent=2)+'\n',encoding='utf-8')
print(json.dumps(states))
