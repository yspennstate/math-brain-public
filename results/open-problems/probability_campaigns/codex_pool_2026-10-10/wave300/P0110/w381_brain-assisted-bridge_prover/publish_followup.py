"""Publish only this additional complete draft after the matching-gap claim is asserted."""
import datetime
import json
import subprocess
import sys
from pathlib import Path

root=Path(__file__).resolve().parent
assert json.loads((root/'followup_validation_receipt.json').read_text(encoding='utf-8'))['failures']==0
mesh=r'~\<private-repo>\12_cognitive_architecture\agent_mesh\agent_mesh.py'
cmd=[sys.executable,'-B','-X','utf8',mesh,'assert','--agent','w381','--resource','topic:P0110:variance-scale-exponent-regularity']
checked=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=60)
(root/'followup_claim_assertion.txt').write_text(checked.stdout+'\n'+checked.stderr,encoding='utf-8')
assert checked.returncode==0,checked.stderr
folder=Path(r'~\math-brain-inbox\w381').resolve()
assert folder.parent==Path(r'~\math-brain-inbox').resolve()
number=2
while (folder/f'bundle_{number:03d}.json').exists() or (folder/f'bundle_{number:03d}.json.part').exists():number+=1
final=folder/f'bundle_{number:03d}.json'
part=folder/(final.name+'.part')
bundle=json.loads((root/'drafts'/'bundle_002.json').read_text(encoding='utf-8'))
bundle['bundle_slug']=f'p0110-variance-regularity-20261010-{number:03d}'
with part.open('x',encoding='utf-8',newline='\n') as stream:stream.write(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n')
part.rename(final)
receipt={'submitted_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'draft_path':str(final),'entries':3,'relations':2,'submitted':True,'reviewed':False,'ingested':False,'retrievable':False,'independent_audit':False,'integration_run':False}
(root/'followup_submission_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
