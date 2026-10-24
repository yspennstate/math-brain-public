import subprocess,time
from pathlib import Path
start=time.time()
r=subprocess.run(['lake','env','lean','~/brain_workers/TRIO_1011/op/G0008/CriticalFirstStep.lean'],cwd='~/lean_verify',capture_output=True,text=True,encoding='utf8',timeout=3600)
Path('lean_check.log').write_text(r.stdout+r.stderr+f'\nEXIT_CODE={r.returncode}\nELAPSED_SECONDS={time.time()-start:.3f}\n',encoding='utf8');print(r.stdout,r.stderr,'EXIT',r.returncode)
