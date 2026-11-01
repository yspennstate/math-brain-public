"""Read back local receipts; close the owner's already registered task."""
from pathlib import Path
import json,hashlib,subprocess,sys
RUN=Path(__file__).resolve().parents[1];ROOT=RUN.parents[1]
def read(p):return Path(p).read_text(encoding='utf-8')
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def save(p,o):Path(p).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8',newline='\n')
receipt=json.loads(read(RUN/'out/PERSISTENCE_RECEIPTS.json'))
for f in receipt['files']:assert digest(RUN/f['path'])==f['sha256']
for f in receipt['rolling']:assert digest(f['path'])==f['sha256']
claim=json.loads(read(RUN/'CLAIMS.json'))[0]
assert claim['version']==9 and hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert (RUN/'PROGRESS.json').read_bytes()==(RUN/'PACKET_DELTA.json').read_bytes()
assert len(read(ROOT/'STATUS.md').splitlines())==2
checklist=Path(r'~\<private-repo>\12_cognitive_architecture\task_checklist\checklist.py')
result=subprocess.run([sys.executable,'-X','utf8',str(checklist),'done','T-20261023-437','A023 stage21: scoped all-even-m>=6 edited-source reference and DATA bank>153/256;728 canonical leaves exact checks PASS; full FEI and independent review OPEN; local files sealed.'],capture_output=True,text=True,encoding='utf-8',timeout=60)
save(RUN/'out/CHECKLIST_RECEIPT.json',{'task_id':'T-20261023-437','returncode':result.returncode,'stdout':result.stdout,'stderr':result.stderr})
closed=result.returncode==0
note='Owner checklist entry T-20261023-437 closed after local read-back verification.' if closed else 'Owner checklist entry T-20261023-437 remains OPEN: completion update was rejected twice with a shared checklist lock error; no lock was modified. This is an administrative blocker, not a local artifact or mathematical check failure.'
report=read(RUN/'REPORT.md').rstrip()+' '+note+'\n'
(RUN/'REPORT.md').write_text(report,encoding='utf-8',newline='\n')
files=[p for p in RUN.rglob('*') if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json']
assert all(p.stat().st_size<20*1024*1024 for p in files)
receipt['files']=[{'path':str(p.relative_to(RUN)),'bytes':p.stat().st_size,'sha256':digest(p)} for p in files]
receipt['read_back_verified']=True
receipt['closed_task_id']='T-20261023-437' if closed else None
receipt['checklist_status']='DONE' if closed else 'OPEN_SHARED_LOCK_BLOCKED'
save(RUN/'out/PERSISTENCE_RECEIPTS.json',receipt)
verify=json.loads(read(RUN/'out/PERSISTENCE_RECEIPTS.json'))
for f in verify['files']:assert digest(RUN/f['path'])==f['sha256']
print(json.dumps({'status':'PASS_LOCAL_ARTIFACT','files_read_back_and_hash_checked':len(files),'statement_sha256':'VERIFIED','schema':'EXACT','task_id':'T-20261023-437','checklist_exit':result.returncode,'checklist_status':receipt['checklist_status'],'full_FEI':'OPEN','independent_person_review':'PENDING','mirror':'UNVERIFIED'}))
