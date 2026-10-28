from pathlib import Path
import subprocess,json,hashlib,os,time
R=Path(__file__).resolve().parents[1]
flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
source=R/'code/Residual.lean';raw=source.read_bytes();sha=hashlib.sha256(raw).hexdigest()
assert b'import Lean.Elab.Tactic.Omega' in raw and b'by\n  omega' in raw
audit=json.loads((R/'out/AUDIT.json').read_text(encoding='utf-8'));assert audit['lean_source_sha256']==sha
admit=subprocess.run(['python','-B','-X','utf8','tools/memok.py'],capture_output=True,text=True,encoding='utf-8',timeout=60,creationflags=flags)
result={'admission_exit':admit.returncode,'admission_output':admit.stdout+admit.stderr,'source_sha256':sha,'status':'NOT_RUN_ADMISSION_HELD','scope':'Only the residual two-bit integer inversion; not full KL theorem or FEI'}
if admit.returncode==0:
 env=dict(os.environ);env['LEAN_CHECK_DIR']=str(R/'out/lean');env['PYTHONDONTWRITEBYTECODE']='1'
 args=['python','-B','-X','utf8','lean_check.py','--core','--file',str(source),'--target','residual_two_bit_inversion','--reviewed-sha256',sha,'--timeout','45','--json']
 try:
  proc=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',timeout=65,creationflags=flags,env=env)
  result.update({'command':args,'exit_code':proc.returncode,'output':proc.stdout+proc.stderr,'status':'TARGET_ACCEPTED' if proc.returncode==0 else 'UNVERIFIED'})
 except subprocess.TimeoutExpired as e:
  result.update({'status':'TIMEOUT_UNVERIFIED','output':str(e)})
(R/'out/LEAN_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
