"""Fresh admission and bounded CORE Lean check; full entropy theorem stays prose."""
from pathlib import Path
import subprocess,sys,hashlib,json,time
R=Path(__file__).resolve().parents[1]
flags=subprocess.CREATE_NO_WINDOW if sys.platform=='win32' else 0
def run(args):return subprocess.run(args,capture_output=True,text=True,encoding='utf-8',errors='replace',creationflags=flags)
admit=run([sys.executable,'-X','utf8',r'tools\memok.py'])
out={'admission_exit':admit.returncode,'admission':admit.stdout.strip(),'rung':'NOT_LEAN_CHECKED','target':'reserve_max_sum','scope':'Nat max-sum algebra only; not entropy, real logs, probability or the full reset theorem'}
if admit.returncode==0:
    src=R/'code'/'ReserveMax.lean';sh=hashlib.sha256(src.read_bytes()).hexdigest()
    command=[sys.executable,'-X','utf8',r'lean_check.py','--file',str(src),'--core','--target','reserve_max_sum','--reviewed-sha256',sh,'--timeout','35','--json']
    start=time.perf_counter();p=run(command)
    (R/'out'/'FORMAL_RAW.txt').write_text(p.stdout+p.stderr,encoding='utf-8')
    out.update(exit_code=p.returncode,source_sha256=sh,seconds=time.perf_counter()-start,raw_output='out/FORMAL_RAW.txt')
    # Only the receipt, never exit0 alone, can establish target/axiom acceptance.
    try:out['receipt']=json.loads(p.stdout)
    except json.JSONDecodeError:out['receipt_parse']='not a single JSON receipt; inspect raw'
else:out['formal_status']='ADMISSION_HELD'
(R/'out'/'FORMAL.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='receipt'}))
