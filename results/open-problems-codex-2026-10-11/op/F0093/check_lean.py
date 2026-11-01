import subprocess,time
from pathlib import Path
root=Path('~/brain_workers/TRIO_1011/op/F0093')
t=time.time()
try:
 p=subprocess.run(['lake','env','lean',str(root/'FiniteCovariance.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
 out=f'exit_code={p.returncode}\nelapsed_seconds={time.time()-t:.3f}\n'+p.stdout+p.stderr
except Exception as e:out=repr(e)
(root/'lean_check.txt').write_text(out,encoding='utf8');print(out)
