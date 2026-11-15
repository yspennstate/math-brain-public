"""Reproduce receipts, serially, with one numerical thread and niceness >=10."""
import os,sys,subprocess,time,resource,json,hashlib
from pathlib import Path
for k in ('OMP_NUM_THREADS','OPENBLAS_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[k]='1'
current=os.getpriority(os.PRIO_PROCESS,0)
if current<10:os.nice(10-current)
assert os.getpriority(os.PRIO_PROCESS,0)>=10
start=time.time();steps=[]
def run(args,out):
    t=time.time()
    with open(out,'w') as log:result=subprocess.run(args,stdout=log,stderr=subprocess.STDOUT)
    steps.append(dict(command=args,output=out,returncode=result.returncode,wall_seconds=time.time()-t))
    Path('run_receipt.json').write_text(json.dumps(dict(steps=steps,nice=os.getpriority(os.PRIO_PROCESS,0),wall_seconds=time.time()-start,max_child_rss_bytes=resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss),indent=2))
    if result.returncode:raise SystemExit(f'Failed: {args}; see {out}')
    print('finished',out,flush=True)
if '--regenerate-npn' in sys.argv:
    run(['clang','-O3','npn5.c','-o','npn5'],'compile_npn.log')
    run(['./npn5'],'npn_generation.txt')
run([sys.executable,'compute.py','small'],'small.log')
run([sys.executable,'compute.py','npn5'],'npn5.log')
run([sys.executable,'compute.py','samples'],'samples.log')
run([sys.executable,'compute.py','families'],'families.log')
run([sys.executable,'analytic_families.py'],'analytic.log')
run(['clang','-O3','verify_census.c','-o','verify_census'],'compile_verify.log')
run(['./verify_census'],'independent_census.json')
run([sys.executable,'audit.py'],'audit.log')
run([sys.executable,'check_restrictions.py'],'restriction_address.log')
