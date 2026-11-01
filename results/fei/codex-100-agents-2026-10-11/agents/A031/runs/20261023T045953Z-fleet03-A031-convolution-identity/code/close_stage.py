from pathlib import Path
import json,hashlib,subprocess,sys
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return p.read_text(encoding='utf-8')
def put(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
p=json.loads(Path('math-open-problems/reports/fei-2026-10-11/EXECUTION_PROTOCOL.json').read_text(encoding='utf-8'));f=p['required_per_run']
claims=json.loads(read(R/'CLAIMS.json'));progress=json.loads(read(R/'PROGRESS.json'));report=read(R/'REPORT.md')
assert all(set(c)==set(f['claim_fields']) for c in claims)
assert set(progress)=={s.split(' (')[0] for s in f['progress_fields']}
assert all('## '+s in report for s in f['report_fields'])
assert report.rstrip().split('\n\n')[-2]=='## Universal bridge'
assert len(read(A/'STATUS.md').splitlines())==2
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
for c in claims:
 assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
 assert sha(Path(c['proof_source']['path']))==c['proof_source']['sha256']
receipts=[]
for task,result in [('T-20261023-098','Stage18 saved and verified earlier: all-L nonfair third reset;7337+502 exact checks; full FEI open.'),('T-20261023-223','Stage19 saved and schema/hash verified: SAME original C2 spare>7/8; ALL adaptive private histories then retained-a/Fair_c leave>1/8;33385 checks; A035 scoped cycle review HOLDS; full FEI open.')]:
 try:
  done=subprocess.run([sys.executable,'-X','utf8','task_checklist_hook.py','done',task,result],capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=55,creationflags=0x08000000)
  receipts.append({'task':task,'exit_code':done.returncode,'stdout':done.stdout[-4000:],'stderr':done.stderr[-4000:]})
 except subprocess.TimeoutExpired:
  receipts.append({'task':task,'status':'TIMEOUT55S; no successful completion receipt claimed'})
put(R/'out/CHECKLIST_RECEIPTS.json',receipts)
notes=json.loads(read(R/'out/PERSISTENCE_NOTES.json'));notes['checklist_completion']='See exact exit/output receipts in out/CHECKLIST_RECEIPTS.json; no completion inferred on failure';put(R/'out/PERSISTENCE_NOTES.json',notes)
for file in R.rglob('*'):
 if file.is_file():
  assert file.stat().st_size<20*1024*1024
  if file.suffix=='.json':json.loads(read(file))
files=[x for x in R.rglob('*') if x.is_file() and x.name not in ['MANIFEST.json','FINAL_READBACK.json']]
manifest=[{'path':str(x.relative_to(R)),'sha256':sha(x),'bytes':x.stat().st_size} for x in files];put(R/'out/MANIFEST.json',manifest)
assert all(sha(R/x['path'])==x['sha256'] for x in manifest)
put(R/'out/FINAL_READBACK.json',{'status':'PASS','protocol_field_sets':'exact','report_sections':'all present; Universal bridge last paragraph','claim_statement_and_proof_hashes':'verified','manifest_entries':len(manifest),'all_manifest_hashes':'verified','packet_delta_identical':True,'status_lines':2,'research_jobs_running':False,'stopped_work':'none','full_fei':'OPEN','new_claim_peer_review':'PENDING'})
print(json.dumps({'readback':'PASS','files':len(manifest),'checklist_receipts':[{'task':x['task'],'exit_code':x.get('exit_code'),'status':x.get('status')} for x in receipts]}))
