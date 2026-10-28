from pathlib import Path
import json,hashlib,subprocess
R=Path(__file__).resolve().parents[1]
prefix='research_pushes/2026-10-11-full-fei-campaign/handoffs/account04/B17/'+R.name
resource='topic:repo/yspennstate/math-research-brain/'+prefix
mesh=subprocess.run(['python','-X','utf8',r'~/<private-repo>/12_cognitive_architecture/agent_mesh/agent_mesh.py','assert','--agent','codex-01a17a7a','--resource',resource],capture_output=True,text=True,encoding='utf-8',timeout=60)
if mesh.returncode:print(mesh.stdout+mesh.stderr);raise SystemExit(mesh.returncode)
files=[p for p in sorted(R.rglob('*')) if p.is_file() and '__pycache__' not in str(p) and p.suffix in ['.py','.json','.md','.lean','.txt'] and p.name not in ['PUBLICATION.json','API_PAYLOAD.json']]
scan=subprocess.run(['python','-X','utf8',r'scan_secrets.py',*[str(p) for p in files]],capture_output=True,text=True,encoding='utf-8',timeout=60)
scanresult={'exit_code':scan.returncode,'stdout':scan.stdout,'stderr':scan.stderr,'mode':'FILE: complete new single-commit API payload; no local git command; no intermediate commits','file_count':len(files)}
(R/'out/SECRET_SCAN.json').write_text(json.dumps(scanresult,indent=2),encoding='utf-8')
if scan.returncode:print(json.dumps(scanresult));raise SystemExit(scan.returncode)
files=[p for p in files if p.name!='RECEIPTS.json']
receipts=[{'path':str(p.relative_to(R)).replace('\\','/'),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size} for p in files]
(R/'out/RECEIPTS.json').write_text(json.dumps({'field_checks':'PASS','artifacts':receipts,'publication':'out/PUBLICATION.json records subsequent immutable commit readback'},indent=2),encoding='utf-8')
files.append(R/'out/RECEIPTS.json')
elements=[]
for p in files:
 b=p.read_bytes();path=prefix+'/'+str(p.relative_to(R)).replace('\\','/')
 elements.append({'path':path,'mode':'100644','type':'blob','content':b.decode('utf-8'),'expected_blob_sha':hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()})
payload={'prefix':prefix,'resource':resource,'elements':elements,'secret_scan':scanresult,'claim_assert':'PASS','expected_prior_receipt':json.loads((R/'out/PRIOR_RECEIPT_RESTORED.json').read_text(encoding='utf-8'))}
print(json.dumps(payload))
