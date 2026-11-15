import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import sys,json,math,time,resource
from tensor_windows import Moments,bounds
import numpy as np
sys.path.insert(0,os.path.abspath('inputs'))
from tree_dnf import Tree
start=time.time();rows=[]
for L in [7,9,11,15,23,39,79]:
    D=round(math.sqrt(2**L));m=Moments(L,D)
    x=m.evaluate(quadrature=0 if D<800 else 20,rmax=3)
    if D>=800:
        y=m.evaluate(quadrature=40,rmax=3)
        x['quadrature_change']=max(abs(x[k]-y[k]) for k in ['L1','L2','L3']);x.update(y)
    row=dict(L=L,w=L+1,D=D,c=D*D*2**-L,**bounds(L,D),**x)
    print(json.dumps(row),flush=True);rows.append(row)
json.dump(dict(rows=rows,seconds=time.time()-start,nice=os.getpriority(os.PRIO_PROCESS,0),maxrss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),open('unbalanced.json','w'),indent=2)
