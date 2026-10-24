"""Place the explicitly requested draft file in w332's inbox, never ingest."""
import json
from pathlib import Path

root=Path(__file__).resolve().parent
validation=json.loads((root/'validation_receipt.json').read_text(encoding='utf-8'))
assert validation['passed']
draft=root/'drafts/bundle_001.json'
raw=draft.read_text(encoding='utf-8')
obj=json.loads(raw)
assert validation['entries']==len(obj['entries']) and validation['relations']==len(obj['relations'])
assert obj['author_agent']=='w332'
inbox=Path('~/math-brain-inbox/w332')
inbox.mkdir(parents=True,exist_ok=True)
for number in range(1,1000):
    target=inbox/f'bundle_{number:03d}.json'
    part=inbox/f'bundle_{number:03d}.part'
    if not target.exists() and not part.exists():
        break
else:
    raise RuntimeError('No free draft number; no existing file was changed')
with part.open('x',encoding='utf-8',newline='\n') as stream:
    stream.write(raw)
part.rename(target)
receipt={'draft_path':str(target),'entries':len(obj['entries']),'relations':len(obj['relations']),
    'placement':'complete .part renamed atomically to .json','ingested_by_worker':False,'independent_audit':'pending_w346',
    'authorized_destination':'named explicitly in the w332 brief, step 4'}
(root/'publish_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
