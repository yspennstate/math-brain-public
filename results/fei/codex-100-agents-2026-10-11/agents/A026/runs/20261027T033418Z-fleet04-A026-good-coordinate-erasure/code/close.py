"""Record actual formal/lifecycle outcomes and refresh final local receipts."""
from pathlib import Path
import json,hashlib,subprocess,sys,datetime
R=Path(__file__).resolve().parents[1];A=R.parents[1]
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def write(p,v):p.write_text(json.dumps(v,indent=2,ensure_ascii=False)+'\n',encoding='utf-8',newline='\n')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
lean=read(R/'out/LEAN_RECEIPT.json');assert lean['status']=='UNCERTIFIED'
assert 'RUNTIME_UNVERIFIED' in lean['lean_stdout']
p=R/'REPORT.md';s=p.read_text(encoding='utf-8')
s=s.replace('Lean receipt is separate and certifies at most its real-algebra statement.',
 'Fresh memok passed (10.6GB physical and22.0GB commit free). The correctly quoted real-algebra Lean attempt returned RUNTIME_UNVERIFIED after120.4s; translation fidelity is UNVERIFIED and no formal certification is claimed. An earlier cmd argument-quoting failure is preserved separately in LEAN_STDOUT.txt; code/formal.py corrected invocation with an argument list. Full receipt: out/LEAN_RECEIPT.json.')
s=s.replace('code/intake.py; code/finalize.py, each with python -X utf8.',
 'code/intake.py; code/finalize.py; code/formal.py; code/close.py, each with python -X utf8.')
p.write_text(s,encoding='utf-8',newline='\n')
p=R/'DERIVATION.md';s=p.read_text(encoding='utf-8')
s=s.replace('This is a scope audit, not a new refutation of A026@6.', 'The A026@6 endpoint bound retains this refund explicitly.')
s=s.replace("This extends, rather than repeats, A029's calibrated-carrier reduction by following the actual erasures and arbitrary physical interleavings.","The following identities refine A029's calibrated-carrier reduction by following the actual erasures and arbitrary physical interleavings.")
s=s.replace('not just the examples below.', 'including the examples below.')
p.write_text(s,encoding='utf-8',newline='\n')
result=subprocess.run([sys.executable,'-X','utf8',r'task_checklist_hook.py','done','T-20261027-027',
 'A026 stage22 saved:89325 exact checks, calibrated-floor review and root-versus-hereditary carrier ledger; FEI OPEN.'],
 capture_output=True,text=True,encoding='utf-8',errors='replace',creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
write(R/'out/CHECKLIST_RECEIPT.json',{'task_id':'T-20261027-027','exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr,'scope':'Stage artifact complete; full FEI remains OPEN; seen flag untouched.'})
progress=read(R/'PROGRESS.json')
progress['blockers']=[x for x in progress['blockers'] if not x.startswith('Lean and administrative')]
progress['blockers'].append('Lean real-algebra check RUNTIME_UNVERIFIED after120.4s; no formal certification')
if result.returncode:
 progress['blockers'].append('Administrative done call failed; exact output in out/CHECKLIST_RECEIPT.json')
 before='Administrative/Lean receipts state actual outcomes; no automatic green status is inferred.'
 after='Lean check is UNVERIFIED. Administrative done call also failed; exact output is retained in out/CHECKLIST_RECEIPT.json. No shared lock, task ledger or seen flag was manually altered.'
 p=R/'REPORT.md';s=p.read_text(encoding='utf-8').replace(before,after);p.write_text(s,encoding='utf-8',newline='\n')
write(R/'PROGRESS.json',progress);write(R/'PACKET_DELTA.json',progress)
now=datetime.datetime.now(datetime.timezone.utc).isoformat()
with (A/'WORKLOG.md').open('a',encoding='utf-8',newline='\n') as f:f.write(f'\n{now} stage22 closure: fresh memok0; correctly quoted Lean algebra attempt RUNTIME_UNVERIFIED after120.4s, no formal certificate. Administrative done exit{result.returncode}; receipt retained. Mathematical final total remains89325, no jobs intentionally left running.\n')
protocol=read(Path(r'math-open-problems/reports\fei-2026-10-11\EXECUTION_PROTOCOL.json'))['required_per_run']
claims=read(R/'CLAIMS.json')
for c in claims:
 assert set(c)==set(protocol['claim_fields'])
 assert c['statement_sha256']==hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()
assert set(progress)=={x.split(' (')[0] for x in protocol['progress_fields']}
assert (R/'PACKET_DELTA.json').read_bytes()==(R/'PROGRESS.json').read_bytes()
assert all('## '+k in (R/'REPORT.md').read_text(encoding='utf-8') for k in protocol['report_fields'])
assert len((A/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[]
for p in R.rglob('*'):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPT.json':
  assert p.stat().st_size<20*1024*1024
  files.append({'path':str(p.relative_to(R)),'sha256':sha(p),'bytes':p.stat().st_size})
write(R/'out/PERSISTENCE_RECEIPT.json',{'status':'PASS_LOCAL_ONLY','at_utc':now,'final_exact_assertions':89325,'files':files,
 'rolling':[{'path':str(A/f),'sha256':sha(A/f)} for f in ['STATUS.md','WORKLOG.md','LEARNED.md']],
 'formal_status':'RUNTIME_UNVERIFIED','checklist_exit':result.returncode,'mirror':'UNVERIFIED'})
print(json.dumps({'status':'PASS_LOCAL_ONLY','exact_checks':89325,'formal_status':'RUNTIME_UNVERIFIED','checklist_exit':result.returncode,'files':len(files)}))
