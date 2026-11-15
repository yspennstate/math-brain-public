import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json,math
from audit import calc,truth,make_bank
from pathlib import Path
C=2/(math.e*math.log(2));out={}
for n in [4,6,7,8]:
    violation=0.;maxratio=0.;count=0
    for start in range(0,65536 if n==4 else 3000,1024):
        f=truth(np.arange(start,min(start+1024,65536),dtype=np.uint64),4) if n==4 else make_bank(n,min(1024,3000-start),17600+n+start)
        o=calc(f);c=o['c'];B,N=f.shape;maxcost=np.zeros(B);collision=np.zeros(B)
        for i in range(n):
            a=c.reshape(B,-1,2,1<<i)[:,:,0,:].reshape(B,-1);b=c.reshape(B,-1,2,1<<i)[:,:,1,:].reshape(B,-1);aa=a*a;bb=b*b;cost=bb*np.log2(np.maximum(aa+bb,1e-300)/np.maximum(bb,1e-300));maxcost+=cost.max(1);collision+=(aa*cost).sum(1)
        violation=max(violation,float((maxcost-C*o['I']).max()),float((collision-C*o['I']).max()));maxratio=max(maxratio,float((maxcost/np.maximum(o['I'],1e-300)).max()));count+=B
    out[str(n)]=dict(functions=count,violation=violation,max_sum_direction_max_over_I=maxratio)
Path('edge_budget.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
