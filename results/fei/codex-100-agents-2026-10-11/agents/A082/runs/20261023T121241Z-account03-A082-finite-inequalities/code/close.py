from pathlib import Path
import json,hashlib,subprocess,sys
R=Path(__file__).resolve().parents[1];H=R.parents[1]
def write(p,x):p.write_text(json.dumps(x,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
p=R/'DERIVATION.md';s=p.read_text(encoding='utf-8')
old='The allowance is SUPPLIED for this fixture; no arbitrary-seed rate is inferred and no intrinsic necessity of this particular target is claimed.'
new=old+' The incoming A and booked W are specified account data; no preceding physical prefix realizing that old booking is constructed in this stage. The universal obligation to supply an eligible actual ancestor account is not discharged by this example.'
assert old in s;s=s.replace(old,new);p.write_text(s,encoding='utf-8')
receipt=dict(task_id='T-20261023-425',first_done_exit=1,first_error='stderr was not retained by initial finalizer; reason unverified')
try:
 r=subprocess.run([sys.executable,'-B','task_checklist_hook.py','done','T-20261023-425','Stage20 research saved and checked; sharp affinity/tree budget theorem pending independent review; FEI OPEN'],timeout=40,capture_output=True,text=True,encoding='utf-8')
 receipt.update(retry_exit=r.returncode,stdout=r.stdout,stderr=r.stderr)
except subprocess.TimeoutExpired:receipt.update(retry_status='TIMEOUT40SECONDS_NO_CLOSURE_CLAIM')
write(R/'out/CHECKLIST_RECEIPT.json',receipt)
p=R/'REPORT.md';report=p.read_text(encoding='utf-8')
report=report.replace('original A=3, old debit1/4, initialCE2','SUPPLIED incoming A=3 and booked old debit1/4 (no preceding physical prefix constructed), initialCE2')
report=report.replace('Checklist working/done infrastructure is the explicit developer-required exception to research output ownership.','Checklist infrastructure is the explicit developer-required exception to research output ownership; its actual exit/error receipt is out/CHECKLIST_RECEIPT.json. Shared closure is unverified unless that receipt reports exit0.')
p.write_text(report,encoding='utf-8')
progress=json.loads((R/'PROGRESS.json').read_text(encoding='utf-8'))
if receipt.get('retry_exit')!=0:progress['blockers'].append('Shared checklist closure failed/unverified; see actual error in out/CHECKLIST_RECEIPT.json. Research files saved.')
for name in ['PROGRESS.json','PACKET_DELTA.json']:write(R/name,progress)
with (H/'LEARNED.md').open('a',encoding='utf-8') as f:f.write('\nStage20 scope clarification: the9-bit payment fixture specifies incoming allowance A3 and old booked W1/4 as supplied account data. It does NOT construct a preceding physical prefix realizing those quantities, nor prove the selected targets necessary. The universal eligible-ancestor supplier remains open.\n')
claims=json.loads((R/'CLAIMS.json').read_text(encoding='utf-8'))
for c in claims:assert hashlib.sha256(c['exact_statement'].encode('utf-8')).hexdigest()==c['statement_sha256']
assert '## Universal bridge' in report and report.rfind('## Universal bridge')>report.rfind('## actual persistence')
assert (R/'PROGRESS.json').read_bytes()==(R/'PACKET_DELTA.json').read_bytes()
assert len((H/'STATUS.md').read_text(encoding='utf-8').splitlines())==2
files=[]
for p in sorted(R.rglob('*')):
 if p.is_file() and p.name!='PERSISTENCE_RECEIPTS.json':
  raw=p.read_bytes();assert len(raw)<20_000_000
  files.append(dict(path=str(p.relative_to(R)),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
write(R/'out/PERSISTENCE_RECEIPTS.json',dict(status='FINAL_READBACK_SCHEMA_STATEMENT_HASH_SIZE_COMPATIBILITY_PASS',files=files,claims=len(claims),mirror_status='UNVERIFIED',full_fei='OPEN'))
for row in files:assert hashlib.sha256((R/row['path']).read_bytes()).hexdigest()==row['sha256']
print('FINAL READBACK PASS',len(files),'files;',len(claims),'statement hashes; final bridge and two-line STATUS checked.')
print('CHECKLIST',json.dumps(receipt,ensure_ascii=False)[:1100])
print('REPORT END',report[-700:])
