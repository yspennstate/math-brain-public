import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np,json
from dpp import random_kernel,probabilities,basis,hessian
rng=np.random.default_rng(33309)
rows=[]
for n in (3,4,5):
    best=1e9;besth=-1e9
    for j in range(800):
        q=random_kernel(rng,n,True,'uniform');c=q[1:,1:];v=q[1:,0];a=q[0,0].real
        pi,m=probabilities(c);iv=np.linalg.inv(m)
        r=np.einsum('i,sij,j->s',v.conj(),iv,v).real;qt=a-r
        g=np.einsum('s,sij->ij',pi*np.log((1-qt)/qt),iv)
        ee,u=np.linalg.eigh(g)
        if ee[0]<best:
            best=ee[0];np.savez('data/star_gradient_n%d.npz'%n,Q=q,G=g,w=u[:,0])
        bs=[e for e in basis(n,True) if np.max(np.abs(e[1:,1:]))==0]
        h=hessian(q,np.array(bs));eh,uh=np.linalg.eigh(h)
        if eh[-1]>besth:besth=eh[-1]
    row=dict(n=n,trials=800,min_loewner_gradient=best,max_star_hessian=besth)
    print(json.dumps(row),flush=True);rows.append(row)
open('data/star_probe.json','w').write(json.dumps(rows,indent=2)+'\n')
