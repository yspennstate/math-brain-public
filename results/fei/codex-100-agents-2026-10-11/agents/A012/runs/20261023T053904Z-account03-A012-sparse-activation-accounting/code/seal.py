from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[1];O=R/'out'
def read(p):return json.loads(p.read_bytes().decode('utf-8-sig'))
def save(p,x):p.write_bytes((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode('utf-8'))
receipt={'current_task':'T-20261023-237','working':'exit0','done':'exit1: checklist lock held too long','earlier_task':'T-20261023-121','earlier_done':'exit0','mathematical_artifacts':'complete locally','running_own_jobs':0,'retry':'supervisor/checklist owner can reconcile from REPORT; no mathematical dependency'}
save(O/'CHECKLIST_RECEIPT.json',receipt)
p=read(R/'PROGRESS.json');blocker='Checklist completion T-20261023-237 failed: shared lock held too long; working succeeded and earlier T-20261023-121 completion exited0; local artifacts complete.'
if blocker not in p['blockers']:p['blockers'].append(blocker)
save(R/'PROGRESS.json',p);save(R/'PACKET_DELTA.json',p)
rp=R/'REPORT.md';text=rp.read_bytes().decode('utf-8');old='Checklist marker results are recorded separately when available.'
new='Checklist working T-20261023-237 exited0; completion exited1 because the shared checklist lock was held too long. Earlier T-20261023-121 completion exited0. CHECKLIST_RECEIPT.json records the precise operational blocker; no checklist process remains running.'
if old in text:text=text.replace(old,new);rp.write_bytes(text.encode('utf-8'))
receipts=read(O/'SOURCE_RECEIPTS.json');external=[x for x in receipts if '20261023T053904Z-account03-A012-sparse-activation-accounting' not in x['path']]
local=[]
for f in sorted(R.rglob('*')):
 if f.is_file() and f.name not in ('SOURCE_RECEIPTS.json','FINAL_VALIDATION.json') and '__pycache__' not in f.parts:
  data=f.read_bytes();assert len(data)<20*1024*1024;local.append({'path':str(f),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
save(O/'SOURCE_RECEIPTS.json',external+local)
assert all(hashlib.sha256(Path(x['path']).read_bytes()).hexdigest()==x['sha256'] for x in local)
claim=read(R/'CLAIMS.json')[0];assert hashlib.sha256(claim['exact_statement'].encode('utf-8')).hexdigest()==claim['statement_sha256']
assert read(R/'PROGRESS.json')==read(R/'PACKET_DELTA.json')
v=read(O/'FINAL_VALIDATION.json');v.update(local_hashes_rechecked=len(local),receipt_count=len(external+local),checklist='completion blocked by shared lock, receipt saved',all_new_jobs_finished=True)
save(O/'FINAL_VALIDATION.json',v)
print(json.dumps({'status':'SEALED_LOCALLY','local_hashes':len(local),'claim_statement_hash':'PASS','progress_delta':'identical','checklist':'shared-lock blocker recorded','new_running_jobs':0,'FEI':'OPEN'}))
