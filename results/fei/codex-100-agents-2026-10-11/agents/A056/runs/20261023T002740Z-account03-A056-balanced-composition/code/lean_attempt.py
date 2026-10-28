from pathlib import Path
import json,hashlib,subprocess,sys
r=Path(__file__).resolve().parents[1]
cmd=[sys.executable,'-B','-X','utf8',r'tools\memok.py']
result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=55)
f=r/'code/allocation.lean';sha=hashlib.sha256(f.read_bytes()).hexdigest()
out={'scope':'integer source/reset allocation ONLY; no certification of log or Fourier mathematics','source_sha256':sha,'memok_exit':result.returncode,'memok_output':result.stdout+result.stderr,'estimated_core_compile_MB':200,'Mathlib':'excluded: documented4GB route exceeds1.5GB cap','status':'COMPUTE_ADMISSION_HELD','formal_target_verified':False}
if result.returncode==0:
 command=[sys.executable,'-B','-X','utf8',r'lean_check.py','--file',str(f),'--core','--target','fresh_reset_allocation','--reviewed-sha256',sha,'--timeout','45','--json']
 try:
  p=subprocess.run(command,capture_output=True,text=True,encoding='utf-8',timeout=55)
  out.update(command=command,exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr,status='SEE_WRAPPER_RECEIPT')
  try:out['formal_target_verified']=json.loads(p.stdout).get('result',{}).get('formal_target_verified',False)
  except ValueError:pass
 except subprocess.TimeoutExpired:out.update(status='RUNTIME_UNVERIFIED',reason='55second outer guard; no theorem receipt')
(r/'out/LEAN_RECEIPT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ['stdout','stderr','command']},indent=2))
