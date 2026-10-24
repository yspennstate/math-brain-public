"""Fresh compute admission before the required scalar Lean attempt."""
from pathlib import Path
import sys,subprocess,json,hashlib
R=Path(__file__).resolve().parents[1]
flags=getattr(subprocess,'CREATE_NO_WINDOW',0)
def call(argv):
    p=subprocess.run(argv,capture_output=True,text=True,encoding='utf-8',errors='replace',creationflags=flags)
    return dict(exit_code=p.returncode,stdout=p.stdout,stderr=p.stderr)
mem=call([sys.executable,'-X','utf8','~/brain_workers/FEI100_20261011/tools/memok.py'])
(R/'out/LEAN_ADMISSION.json').write_text(json.dumps(mem,indent=2)+'\n',encoding='utf-8')
if mem['exit_code']:
    result={'status':'HELD_NO_COMPUTE_ADMISSION','formal_target_verified':False,'source':str(R/'code/Bank.lean'),'compiler_launched':False,'admission':mem}
else:
    p=R/'code/Bank.lean'
    raw=call([sys.executable,'-X','utf8','~/.claude/dreaming/lean_check.py','--file',str(p),'--target','A051.reset_bank','--reviewed-sha256',hashlib.sha256(p.read_bytes()).hexdigest(),'--timeout','45','--json'])
    try:result=json.loads(raw['stdout'])
    except json.JSONDecodeError:result={'status':'RUNTIME_UNVERIFIED','formal_target_verified':False,'raw':raw}
    result['wrapper_exit_code']=raw['exit_code']
(R/'out/LEAN.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2)[:4500])
