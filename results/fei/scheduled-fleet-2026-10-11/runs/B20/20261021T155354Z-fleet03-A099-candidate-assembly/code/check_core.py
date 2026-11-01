from pathlib import Path
import subprocess,sys,json,hashlib,os,time
run=Path(__file__).resolve().parents[1]
# Core Std only; no Mathlib import/build. Integer bookkeeping is the only target.
source='''
import Std
theorem reset_account (A d b r Z T t : Int) (h : T = b + r + t) :
    A - (d + b) - (t + Z) = (A - d - T) + r - Z := by
  omega
'''.strip()
raw=('\n'+source+'\n').encode('utf-8')
(run/'code/ResetAccount.lean').write_bytes(raw)
env=os.environ.copy();env['LEAN_CHECK_DIR']=str(run/'out/lean')
cmd=[sys.executable,'-X','utf8','~/.claude/dreaming/lean_check.py',
 '--core','--stmt',source,'--target','reset_account',
 '--reviewed-sha256',hashlib.sha256(raw).hexdigest(),'--timeout','55','--json']
try:
 result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',env=env,timeout=75,
   creationflags=getattr(subprocess,'CREATE_NO_WINDOW',0))
 out={'exit_code':result.returncode,'stdout':result.stdout,'stderr':result.stderr,
      'scope':'Only integer reset_account bookkeeping, NOT entropy/KL/FEI. Core Std, no Mathlib.'}
except subprocess.TimeoutExpired as e:
 out={'status':'INCOMPLETE_TIMEOUT','scope':'No Lean mathematical certification claimed'}
(run/'out/LEAN_CORE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='stdout' and k!='stderr'}))
if 'stdout' in out:print(out['stdout'][:3500])
