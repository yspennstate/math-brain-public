import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import sys,time,json,resource
sys.path.insert(0,os.path.abspath('inputs'))
from tree_dnf import Tree
start=time.time();rows=[]
for w,D in [(10,8),(16,55),(16,181),(20,196)]:
    t=Tree(w,D);mean,se=t.mc(100000,2104)
    r=dict(w=w,D=D,samples=100000,seed=2104,E_ratio=float(mean[0]/t.inf),E_standard_error=float(se[0]/t.inf),influence_check=float(mean[1]/t.inf),influence_check_se=float(se[1]/t.inf),total_mass=float(mean[2]),mass_se=float(se[2]))
    print(json.dumps(r),flush=True);rows.append(r)
json.dump(dict(rows=rows,seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),open('tree_estimates.json','w'),indent=2)
