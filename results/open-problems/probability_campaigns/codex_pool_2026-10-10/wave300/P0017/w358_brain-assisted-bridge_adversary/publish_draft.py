"""Publish the complete worker-owned draft, never ingest it or overwrite another file."""
from pathlib import Path
import json

root=Path(__file__).parent
dest=Path('~/math-brain-inbox/w358/bundle_001.json')
part=dest.with_suffix('.part')
payload=(root/'bundle_001.json').read_text(encoding='utf-8')
data=json.loads(payload)
assert data['author_agent']=='w358' and data['spec']=='mathbrain-draft-v1'
assert all(e['kind']=='concept' and e['proof_text'] is None for e in data['entries'])
assert str(dest.resolve()).lower().startswith(str(Path('~/math-brain-inbox/w358').resolve()).lower()+'\\')
dest.parent.mkdir(parents=True,exist_ok=True)
if dest.exists():
    if dest.read_text(encoding='utf-8')!=payload:
        raise SystemExit('Destination exists with different content; preserved without overwrite')
else:
    part.write_text(payload,encoding='utf-8')
    # rename is atomic in this same directory and refuses an existing destination on Windows.
    part.rename(dest)
assert dest.read_text(encoding='utf-8')==payload
life=json.loads((root/'BUNDLE_LIFECYCLE.json').read_text(encoding='utf-8'))
life.update(submitted=True,submission_claim='clm-8545c6e623',submission_method='complete .part -> .json same-directory rename')
(root/'BUNDLE_LIFECYCLE.json').write_text(json.dumps(life,indent=2)+'\n',encoding='utf-8')
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['owner_prior_work_check']['canonical_repository']='No SQLite file found by targeted filename lookup; local has named subdirectories and no immediate files. Canonical store location unresolved; benchmark/evaluation subdirectories were not opened.'
(root/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
receipt={'draft_file':str(dest),'complete_and_equal_to_local':True,'submitted':True,
         'reviewed':False,'ingested':False,'retrievable':False,
         'store_write_by_worker':False,'integration_invoked':False}
(root/'SUBMISSION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt))
