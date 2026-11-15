"""Run the local numerical checks sequentially, with one numerical thread."""
import os,subprocess,sys
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[key]='1'
current=os.getpriority(os.PRIO_PROCESS,0)
if current<10:os.nice(10-current)
assert os.getpriority(os.PRIO_PROCESS,0)>=10
os.chdir(Path(__file__).resolve().parent)
runs=[(['tensor_windows.py','validate'],'tensor_validate.log'),(['window_search.py','validate'],'windows_validate.log'),(['linear_audit.py'],'linear_audit.log'),(['extra_checks.py'],'extra_checks.log')]
if '--quick' not in sys.argv:
 runs +=[(['inputs/tree_dnf.py','selftest'],'tree_selftest.log'),(['tensor_windows.py'],'tensor_asymptotics.log'),(['unbalanced.py'],'unbalanced.log'),(['window_search.py','scan'],'windows_scan.log'),(['tree_estimates.py'],'tree_estimates.log'),(['audit.py'],'audit.log')]
for args,log in runs:
 print('Running',' '.join(args),flush=True)
 with open(log,'w') as stream:subprocess.run([sys.executable,*args],stdout=stream,stderr=subprocess.STDOUT,check=True)
