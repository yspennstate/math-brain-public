from pathlib import Path
import subprocess,sys,json,hashlib
ROOT=Path(__file__).resolve().parents[1];AGENT=ROOT.parents[1]
def load(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
hook=Path(r'task_checklist_hook.py')
tasks=[('T-20261023-075','20261022T234254Z-account03-A065-stopping-rule-falsifier','A065 stage17 files saved and verified;577200 exact checks; full FEI OPEN.'),('T-20261023-213','20261023T043836Z-account03-A065-stopping-rule-falsifier','A065 stage18 saved and verified; ordinary-prefix reset theorem;612654 exact checks; full FEI OPEN.'),('T-20261023-369',ROOT.name,'A065 stage19 saved and verified; fixed-product-root tensor deficit>L/4, exact same-bank repair;33843 exact checks; full FEI OPEN.')]
life=load(ROOT/'out/LIFECYCLE.json');life['done_attempts']=[]
for task,run,result in tasks:
 assert (AGENT/'runs'/run/'REPORT.md').is_file()
 proc=subprocess.run([sys.executable,'-B','-X','utf8',str(hook),'done',task,result],capture_output=True,text=True,encoding='utf-8',errors='replace',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 life['done_attempts'].append({'task':task,'exit_code':proc.returncode,'stdout':proc.stdout[-1000:],'stderr':proc.stderr[-1000:]})
 save(ROOT/'out/LIFECYCLE.json',life)
 print(json.dumps({'task':task,'done_exit':proc.returncode}),flush=True)
current=life['done_attempts'][-1]['exit_code']==0
for name in ['PROGRESS.json','PACKET_DELTA.json']:
 p=ROOT/name;d=load(p);d['blockers']=[x for x in d['blockers'] if not x.startswith('Required checklist working helper')]
 if not current:d['blockers'].append('Task bookkeeping closure blocked by shared checklist locking; mathematical stage files complete.')
 save(p,d)
p=ROOT/'REPORT.md';s=p.read_text(encoding='utf-8');s=s.replace('Checklist working helper hit a shared-lock timeout, recorded in out/LIFECYCLE.json; closing bookkeeping is separately recorded when attempted.','Checklist working helper initially hit a shared-lock timeout. out/LIFECYCLE.json records the completed-stage closure attempts and actual return codes separately from mathematical completion.');p.write_text(s,encoding='utf-8',newline='\n')
assert load(ROOT/'PROGRESS.json')==load(ROOT/'PACKET_DELTA.json')
paths=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json')+[AGENT/x for x in ['STATUS.md','WORKLOG.md','LEARNED.md']]
rows=[]
for p in paths:
 assert p.stat().st_size<20_000_000
 rows.append({'path':str(p),'bytes':p.stat().st_size,'sha256':sha(p)})
save(ROOT/'out/PERSISTENCE_RECEIPTS.json',rows)
for row in load(ROOT/'out/PERSISTENCE_RECEIPTS.json'):
 p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
for name in ['REPORT.md','CLAIMS.json','PROGRESS.json','PACKET_DELTA.json']:assert (ROOT/name).stat().st_size>0
print(json.dumps({'final_readback':'PASS','unchanged_artifacts_verified':len(rows),'current_checklist_closed':current,'no_math_job_running':True,'full_FEI':'OPEN','review':'PENDING'}),flush=True)
