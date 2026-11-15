"""Run local reproducibility commands at nice >=10 and one numerical thread."""
import os,sys,subprocess,json,time,resource
from pathlib import Path
os.environ.update(OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1',MKL_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
current=os.getpriority(os.PRIO_PROCESS,0)
if current<10:os.setpriority(os.PRIO_PROCESS,0,10)
start=time.time();r=subprocess.run(sys.argv[1:])
with Path('runs.jsonl').open('a') as f:f.write(json.dumps(dict(command=sys.argv[1:],nice=os.getpriority(os.PRIO_PROCESS,0),wall_seconds=time.time()-start,child_maxrss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,exit_code=r.returncode))+'\n')
sys.exit(r.returncode)
