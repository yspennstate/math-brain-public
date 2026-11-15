"""Reproduce the numeric experiment in this directory, using one worker at nice 10."""
import os
from pathlib import Path
import subprocess
import time

root = Path(__file__).resolve().parents[1]
os.chdir(root)
if os.getpriority(os.PRIO_PROCESS, 0) < 10:
    os.setpriority(os.PRIO_PROCESS, 0, 10)
os.environ.update(OMP_NUM_THREADS="1", OPENBLAS_NUM_THREADS="1", MKL_NUM_THREADS="1",
                  VECLIB_MAXIMUM_THREADS="1", XDG_CACHE_HOME=str(root/'data'/'cache'),
                  MPLCONFIGDIR=str(root/'data'/'mplconfig'))
(root/'data').mkdir(exist_ok=True)
subprocess.run(['clang++','-std=c++17','-O2','-Wall','-Wextra','-pedantic',
                'code/simulate.cpp','-o','code/simulate'],check=True)
start=time.monotonic()
with (root/'data'/'simulation_console.txt').open('w') as log:
    subprocess.run(['code/simulate','24','2000000','1000000','data'],stdout=log,check=True)
    log.write(f'Wall seconds: {time.monotonic()-start:.6f}\n')
subprocess.run(['python3','code/analyze.py'],check=True)
subprocess.run(['python3','code/audit_artifacts.py'],check=True)
