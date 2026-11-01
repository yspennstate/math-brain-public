from pathlib import Path
import hashlib,json,subprocess,sys,time
R=Path(__file__).resolve().parents[1];p=R/'code/Cancellation.lean'
cmd=[sys.executable,'-B','-X','utf8','lean_check.py','--file',str(p),'--core','--target','A002_weighted_cancellation','--reviewed-sha256',hashlib.sha256(p.read_bytes()).hexdigest(),'--timeout','45','--json']
start=time.monotonic()
try:
 r=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',timeout=65,creationflags=0x08000000)
 out={'command':cmd,'exit_code':r.returncode,'seconds':time.monotonic()-start,'stdout':r.stdout,'stderr':r.stderr,'scope':'binary scalar cancellation after clearing dyadic reaches only; not entropy/Boolean premises','admission':'memok exited0 before invocation; core Lean only, no Mathlib build'}
except subprocess.TimeoutExpired as e:
 out={'command':cmd,'status':'WRAPPER_TIMEOUT_UNVERIFIED','seconds':time.monotonic()-start,'scope':'No Lean theorem acceptance claimed'}
(R/'out/LEAN.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k not in ('command','stdout','stderr')}));print(out.get('stdout','')[:1800])
