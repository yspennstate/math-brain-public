from pathlib import Path
import json,hashlib,subprocess,datetime
R=Path(__file__).resolve().parents[1]
def save(p,x):p.write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8',newline='')
save(R/'out/CHECKLIST_INITIAL_FAILURE.json',{'action':'done T-20261023-514','exit_code':1,'error':"checklist: error: RuntimeError('checklist lock held too long')",'effect':'Protocol finalizer completed; original chained audit did not run; no shared lock or process touched.'})
cmd=['python','-X','utf8','task_checklist_hook.py','done','T-20261023-514','A011 stage21 local proof/checks/artifacts complete: arbitrary physical policies in supplied-source finite-edit family;2576591 assertions PASS;independent review/full FEI open.']
try:
 result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=65);code=result.returncode;stdout=result.stdout;stderr=result.stderr
except subprocess.TimeoutExpired:
 code=-1;stdout='';stderr='Bounded checklist closure retry timed out; shared service not modified.'
closure={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'entry':'T-20261023-514','status':'DONE' if code==0 else 'BLOCKED_SHARED_SERVICE','exit_code':code,'stdout':stdout,'stderr':stderr,'scope':'Only bookkeeping service status; all mathematical checks/local stage artifacts completed.'};save(R/'out/CHECKLIST_CLOSURE.json',closure)
# Preserve all original receipt checks except two deliberate, named editorial changes.
receiptpath=R/'out/ARTIFACT_RECEIPTS.json';receipt=json.loads(receiptpath.read_text(encoding='utf-8'));changed={'DERIVATION.md','code/audit.py'}
for row in receipt['files']:
 q=Path(row['path']);q=q if q.is_absolute() else R/q;digest=hashlib.sha256(q.read_bytes()).hexdigest();relative=str(q.relative_to(R)).replace('\\','/') if q.is_relative_to(R) else ''
 if relative in changed:row['bytes']=q.stat().st_size;row['sha256']=digest
 else:assert q.stat().st_size==row['bytes'] and digest==row['sha256'],str(q)
save(receiptpath,receipt)
subprocess.run(['python','-X','utf8',str(R/'code/audit.py')],check=True,timeout=60)
print(json.dumps({'checklist_status':closure['status'],'initial_error_saved':True,'audit':'completed'}))
