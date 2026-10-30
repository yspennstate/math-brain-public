from pathlib import Path
import subprocess,json,sys,hashlib,time
R=Path(__file__).resolve().parents[1]
source=R/'code/Budget.lean';digest=hashlib.sha256(source.read_bytes()).hexdigest()
gate=subprocess.run([sys.executable,'-X','utf8',r'tools\memok.py'],capture_output=True,text=True,encoding='utf-8')
out={'gate_exit':gate.returncode,'gate_output':gate.stdout+gate.stderr,'source_sha256':digest,'targets':[]}
if gate.returncode==0:
 for target in ['a051_shifted_budget','a051_occupied_budget']:
  cmd=[sys.executable,'-X','utf8',r'lean_check.py','--file',str(source),'--target',target,'--reviewed-sha256',digest,'--timeout','55','--json']
  start=time.monotonic()
  try:
   p=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=90)
   rec={'target':target,'exit':p.returncode,'output':p.stdout+p.stderr,'seconds':time.monotonic()-start}
  except subprocess.TimeoutExpired as err:
   rec={'target':target,'status':'WRAPPER_TIMEOUT_UNVERIFIED','seconds':time.monotonic()-start}
  out['targets'].append(rec)
  (R/'out/LEAN_STATUS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
else:out['status']='HELD_NO_CERTIFICATE'
(R/'out/LEAN_STATUS.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out))
