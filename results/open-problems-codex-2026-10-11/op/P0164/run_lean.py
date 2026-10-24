import subprocess,time
from pathlib import Path
p=Path(__file__).resolve().parent
t=time.time()
r=subprocess.run(['lake','env','lean',str(p/'FiniteChecks.lean')],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
p.joinpath('lean_check.log').write_text(r.stdout+r.stderr+f"\nexit_code={r.returncode} elapsed_seconds={time.time()-t:.2f}\n",encoding='utf8')
print(r.stdout+r.stderr); print('exit',r.returncode,'seconds',time.time()-t)
