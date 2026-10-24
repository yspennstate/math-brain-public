"""Submit this worker's complete DRAFT after asserting its narrow mesh claim."""
import datetime
import json
import subprocess
import sys
from pathlib import Path

root=Path(__file__).resolve().parent
validation=json.loads((root/'bundle_validation_receipt.json').read_text(encoding='utf-8'))
assert validation['failures']==0 and not validation['independent_audit']
cmd=[sys.executable,'-B','-X','utf8',r'~\<private-repo>\12_cognitive_architecture\agent_mesh\agent_mesh.py','assert','--agent','w381','--resource','topic:P0110:terminal-bias-supporting-sphere']
claim=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=60)
(root/'narrow_claim_assertion.txt').write_text(claim.stdout+'\n'+claim.stderr,encoding='utf-8')
if claim.returncode:
    raise SystemExit('Narrow claim not asserted; DRAFT remains in worker folder.')
folder=Path(r'~\math-brain-inbox\w381').resolve()
assert folder.parent==Path(r'~\math-brain-inbox').resolve() and folder.name=='w381'
folder.mkdir(exist_ok=True)
bundle=json.loads((root/'drafts'/'bundle_001.json').read_text(encoding='utf-8'))
number=1
while (folder/f'bundle_{number:03d}.json').exists() or (folder/f'bundle_{number:03d}.json.part').exists():
    number+=1
final=folder/f'bundle_{number:03d}.json'
part=folder/(final.name+'.part')
bundle['bundle_slug']=f'p0110-terminal-bias-sphere-20261010-{number:03d}'
with part.open('x',encoding='utf-8',newline='\n') as stream:
    stream.write(json.dumps(bundle,indent=2,ensure_ascii=False)+'\n')
# Windows rename refuses to replace an existing target; no other artifact is overwritten.
part.rename(final)
receipt={'submitted_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'draft_path':str(final),'entries':len(bundle['entries']),'relations':len(bundle['relations']),
 'submitted':True,'reviewed':False,'ingested':False,'retrievable':False,
 'independent_audit':False,'integration_run':False,'source_manifests_or_digests_generated':False}
(root/'submission_receipt.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
source=json.loads((root/'SOURCE_STATUS.json').read_text(encoding='utf-8'))
source['brain_states']={k:receipt[k] for k in ('submitted','reviewed','ingested','retrievable')}
source['draft_path']=str(final)
(root/'SOURCE_STATUS.json').write_text(json.dumps(source,indent=2),encoding='utf-8')
print(json.dumps(receipt,indent=2))
