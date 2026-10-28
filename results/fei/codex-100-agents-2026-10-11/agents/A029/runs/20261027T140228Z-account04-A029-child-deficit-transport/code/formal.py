from pathlib import Path
import subprocess,json,hashlib,time,sys
r=Path(__file__).resolve().parents[1];now=time.monotonic()
def run(args,timeout):
 try:
  p=subprocess.run(args,capture_output=True,encoding='utf-8',errors='replace',timeout=timeout,creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
  return {'exit_code':p.returncode,'stdout':p.stdout,'stderr':p.stderr}
 except subprocess.TimeoutExpired as e:return {'status':'RUNTIME_UNVERIFIED_TIMEOUT','stdout':str(e.stdout),'stderr':str(e.stderr)}
admit=run([sys.executable,'-X','utf8',r'tools\memok.py'],55)
out={'memory_admission':admit,'scope':'integer child ledger only; not full theorem','memory_estimate_MB':180,'Mathlib':False}
if admit.get('exit_code')==0:
 p=r/'code/Accounting.lean';sha=hashlib.sha256(p.read_bytes()).hexdigest();out['reviewed_source_sha256']=sha
 out['lean']=run([sys.executable,'-B','-X','utf8',r'lean_check.py','--core','--file',str(p),'--target','child_payment','--reviewed-sha256',sha,'--timeout','45','--json'],65)
else:out['lean']={'status':'NOT_RUN_ADMISSION_HELD'}
out['seconds']=time.monotonic()-now
(r/'out/LEAN_RECEIPT.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({'admission_exit':admit.get('exit_code'),'lean_exit':out['lean'].get('exit_code'),'status':out['lean'].get('status'),'seconds':out['seconds']}))
