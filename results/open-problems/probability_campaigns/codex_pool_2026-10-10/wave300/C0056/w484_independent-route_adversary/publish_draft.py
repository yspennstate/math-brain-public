from pathlib import Path
import json
import subprocess

root=Path(__file__).resolve().parent
inbox=Path('~/math-brain-inbox/w484').resolve()
assert inbox == Path('~/math-brain-inbox/w484').resolve()
command=['python','-X','utf8','~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py','assert','--agent','w484','--resource',str(inbox)]
lease=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=30)
print(lease.stdout)
if lease.returncode:
    print(lease.stderr)
    raise SystemExit('Lease assertion failed; local draft remains intact')

bundle=json.loads((root/'DRAFT_BUNDLE.json').read_text(encoding='utf-8'))
allowed={'depends_on','defines','proves','refutes','generalizes','specializes','analogous_to','cites','semantic_association'}
required={'key','namespace','logical_name','kind','title','statement','proof_text','assumptions','domain','source'}
keys={row['key'] for row in bundle['entries']}
assert len(keys)==len(bundle['entries'])<=200
for row in bundle['entries']:
    assert required <= set(row)
    assert row['kind']=='concept' and row['proof_text'] is None
    assert row['source']['license'].startswith('owner-own-work')
for relation in bundle['relations']:
    assert relation['from_key'] in keys and relation['to_key'] in keys
    assert relation['kind'] in allowed and relation['rationale']
inbox.mkdir(exist_ok=True)
serial=1
while (inbox/f'bundle_{serial:03d}.json').exists() or (inbox/f'bundle_{serial:03d}.part').exists():
    serial+=1
final=inbox/f'bundle_{serial:03d}.json'
part=inbox/f'bundle_{serial:03d}.part'
assert final.resolve().is_relative_to(inbox) and part.resolve().is_relative_to(inbox)
part.write_text(json.dumps(bundle,indent=2)+'\n',encoding='utf-8')
part.rename(final)
receipt={'draft_path':str(final),'entries':len(bundle['entries']),'relations':len(bundle['relations']),
 'submitted':True,'reviewed':False,'ingested':False,'retrievable':False,
 'gateway':'BUNDLE_SPEC.md v1; own folder path lease asserted; complete part renamed atomically',
 'integration':'Coordinator must validate; no integrate_drafts.py or store mutation performed'}
(root/'SUBMISSION_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
source_path=root/'SOURCE_STATUS.json'; status=json.loads(source_path.read_text(encoding='utf-8'))
status['submission_state']='submitted as DRAFT concepts; review pending'
status['draft_path']=str(final)
source_path.write_text(json.dumps(status,indent=2)+'\n',encoding='utf-8')
print(json.dumps(receipt,indent=2))
