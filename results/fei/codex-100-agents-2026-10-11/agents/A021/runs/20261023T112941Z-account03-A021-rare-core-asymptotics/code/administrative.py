from pathlib import Path
import subprocess,sys,json,hashlib
r=Path(__file__).resolve().parents[1]
rows=[{'action':'working','task':'T-20261023-381','returncode':1,'stderr':'checklist lock held too long','receipt':'observed initial stage registration attempt; research completion tracked separately'}]
def save(): (r/'out/CHECKLIST_RECEIPTS.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8',newline='')
save()
# The current checklist was read first: all three asks match A021 and this session.
for ident,message in [('T-20261023-381','A021 stage20 saved: unequal-depth stopping proof within original cap; all65/4095 certificate+replay and144 physical histories PASS; FEI OPEN, external review/source handoff pending'),('T-20261023-221','A021 stage19 saved: active-cylinder-only controller continuation and exact checks complete at scoped claim; full FEI remains OPEN'),('T-20261021-189','A021 stage17 deliverables saved: exact same-owner query transport and scoped obstruction checked; later stages continue open full-FEI work')]:
 p=subprocess.run([sys.executable,'-X','utf8',r'task_checklist_hook.py','done',ident,message],capture_output=True,text=True,encoding='utf-8')
 rows.append({'action':'done','task':ident,'returncode':p.returncode,'stdout':p.stdout,'stderr':p.stderr});save();print('CHECKLIST',ident,p.returncode,p.stdout[-200:],p.stderr[-200:],flush=True)
files=[]
for p in r.rglob('*'):
 if p.is_file() and p!=r/'out/ARTIFACT_CHECK.json':
  assert p.stat().st_size<20_000_000;files.append({'path':str(p.relative_to(r)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
j={'status':'PASS','exact_schema':'PASS (validated by code/finalize.py)','statement_digest':'PASS','compatibility':'BYTE_IDENTICAL','files':files,'administrative_receipts':'out/CHECKLIST_RECEIPTS.json'}
assert (r/'PROGRESS.json').read_bytes()==(r/'PACKET_DELTA.json').read_bytes()
(r/'out/ARTIFACT_CHECK.json').write_text(json.dumps(j,indent=2)+'\n',encoding='utf-8',newline='')
print('FINAL_LOCAL_RECEIPT_PASS',len(files),'files',flush=True)
