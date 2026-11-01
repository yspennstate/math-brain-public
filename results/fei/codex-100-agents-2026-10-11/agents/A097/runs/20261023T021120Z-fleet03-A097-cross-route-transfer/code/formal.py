from pathlib import Path
import subprocess,sys,json,hashlib,os,time
RUN=Path(__file__).resolve().parents[1];OUT=RUN/'out'
flags=subprocess.CREATE_NO_WINDOW if os.name=='nt' else 0
def run(cmd,timeout):
 try:
  r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace',timeout=timeout,creationflags=flags)
  return {'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
 except subprocess.TimeoutExpired as e:return {'status':'TIMEOUT_NOT_A_CERTIFICATE','stdout':str(e.stdout),'stderr':str(e.stderr)}
gate=run([sys.executable,'-X','utf8','tools/memok.py'],30)
obj={'memory_admission':gate,'memory_estimate_mb':900,'formal_scope':'Only canonical_nonempty_cancel scalar normalization; not the Boolean support or tree theorem','maximum_compiler_seconds':45,'proof_status':'NOT_RUN'}
if gate.get('exit_code')==0:
 path=RUN/'KEY_STEP.lean';sha=hashlib.sha256(path.read_bytes()).hexdigest()
 cmd=[sys.executable,'-B','-X','utf8','lean_check.py','--file',str(path),'--target','canonical_nonempty_cancel','--reviewed-sha256',sha,'--timeout','45','--json']
 obj['command']=cmd;obj['reviewed_source_sha256']=sha;obj['result']=run(cmd,75)
 obj['proof_status']='SEE_EXACT_RECEIPT_NOT_AUTOMATIC_ACCEPTANCE'
(OUT/'LEAN_RESULT.json').write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
print(json.dumps(obj))
