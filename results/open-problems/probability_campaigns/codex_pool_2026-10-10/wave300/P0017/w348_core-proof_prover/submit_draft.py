from pathlib import Path
import datetime as dt
import json
import subprocess
import sys

base=Path(__file__).resolve().parent
target_dir=Path('~/math-brain-inbox/w348')
target=target_dir/'bundle_001.json'
tool='~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py'
check=subprocess.run([sys.executable,'-B','-X','utf8',tool,'assert','--agent','w348',
                      '--resource',str(target_dir)],capture_output=True,text=True,
                     encoding='utf-8',errors='replace',timeout=90)
receipt={'checked_at_utc':dt.datetime.now(dt.timezone.utc).isoformat(),
         'command':'agent_mesh.py assert --agent w348 --resource ~/math-brain-inbox/w348',
         'exit_code':check.returncode,'stdout':check.stdout,'stderr':check.stderr,
         'submitted':False,'reviewed':False,'ingested':False,'retrievable':False}
receipt_path=base/'checks'/'submission.json'
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
if check.returncode:
    print(json.dumps({'submitted':False,'reason':'narrow claim assertion failed','details':check.stderr.strip()}))
    raise SystemExit(check.returncode)
raw=(base/'drafts'/'bundle_001.json').read_bytes()
bundle=json.loads(raw)
assert all(e['kind']=='concept' and e['proof_text'] is None for e in bundle['entries'])
target_dir.mkdir(exist_ok=True)
if target.exists():
    if target.read_bytes()!=raw:
        raise SystemExit('Different existing bundle preserved; choose a new number before submission.')
else:
    part=target_dir/'bundle_001.part'
    part.write_bytes(raw)
    part.rename(target)
receipt.update({'submitted':True,'path':str(target),'entries':len(bundle['entries']),
                'relations':len(bundle['relations']),'entry_kind':'concept',
                'review_status':'PENDING; not a theorem promotion or ingestion receipt'})
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
for filename in ['SOURCE_STATUS.json','METRICS.json']:
    p=base/filename
    data=json.loads(p.read_text(encoding='utf-8'))
    if filename=='SOURCE_STATUS.json': data['brain_states']['submitted']=True
    else: data['submitted']=True
    p.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps({'submitted':True,'path':str(target),'entries':len(bundle['entries']),
                  'relations':len(bundle['relations']),'reviewed':False,'ingested':False,'retrievable':False}))
