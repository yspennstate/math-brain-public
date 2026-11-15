import os
os.environ['OPENBLAS_NUM_THREADS']='1'
import numpy as np,json
from audit import calc
from pathlib import Path
out=[]
for m in [4,6,8,10,12]:
    s=2**(m//2);N=1<<m;ids=np.arange(N);ip=np.zeros(N,dtype=int)
    for j in range(0,m,2):ip^=((ids>>j)&1)*((ids>>(j+1))&1)
    orig=1-2*ip;positive=np.flatnonzero(orig==1);B=positive[:2]
    for mode in ['a_zero','u_zero']:
        u=orig.astype(float).copy();cnt=(s-2)//2 if mode=='a_zero' else s//2;u[positive[2:2+cnt]]=-1;v=u.copy();v[B]=-1;f=np.r_[u,v];o=calc(f[None,:]);c=o['c'][0];a=c[:N];b=c[N:];uh=a+b;delta=o['Inf'][0,m]
        out.append(dict(m=m,mode=mode,delta=float(delta),E_over_delta=float(o['E'][0,m]/delta),a_empty=float(a[0]),b_empty=float(b[0]),u_empty=float(uh[0]),a_reference_singular=bool(np.any((a==0)&(b!=0))),u_reference_singular=bool(np.any((uh==0)&(b!=0)))))
Path('singular_examples.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
