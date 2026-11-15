"""Targeted three-point searches using the inherited analytic full Hessian."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import numpy as np, json, time,resource
from scipy.optimize import minimize
from scipy.special import expit
from pathlib import Path
from dpp import basis,hessian,spectral,random_unitary,random_kernel
rng=np.random.default_rng(330033); root=Path(__file__).resolve().parent
out=[];b=basis(3,True);br=basis(3,False);start=time.time()
def obj(q,bs):
    h=hessian(q,bs);e,v=np.linalg.eigh(h)
    return e[-1],np.einsum('k,kij->ij',v[:,-1],bs)
def save(family,vals,q,a,extra=None):
    v=float(max(vals));np.savez(root/'data'/f'{family}.npz',Q=q,A=a,value=v)
    row=dict(family=family,trials=len(vals),minimum=float(min(vals)),maximum=v,median=float(np.median(vals)),extra=extra)
    out.append(row);print(json.dumps(row),flush=True)
    (root/'data'/'explore3.json').write_text(json.dumps(dict(seed=330033,rows=out,elapsed_seconds=time.time()-start,peak_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss),indent=2)+'\n')
# Direct compact chart: Q = d I + r B normalized by the two extreme eigenvalues.
# Covers eigenvalue placement, off-diagonal phases, and dilute correlation scales.
for cx in (False,True):
    vals=[];best=-np.inf
    for j in range(6000):
        q=random_kernel(rng,3,cx,('uniform','extreme','projection')[j%3])
        if j%4==0:
            d=np.diag(q).real;eps=10**rng.uniform(-6,0)
            q=np.diag(d)+eps*(q-np.diag(d))
        v,a=obj(q,b if cx else br);vals.append(v)
        if v>best:best=v;qq=q;aa=a
    save('three_'+str(cx),vals,qq,aa)
# maximize normalized curvature in the off-diagonal small-correlation regime.
# Small curvature is divided by ||offdiag Q||^2 to avoid attraction to products.
for cx in (False,True):
    bs=b if cx else br;best=[-np.inf,None,None];calls=[0]
    def decode(x):
        d=.02+.96*expit(x[:3]);c=x[3:6].astype(complex)
        if cx:c=c+1j*x[6:9]
        r=np.zeros((3,3),complex);r[0,1],r[0,2],r[1,2]=c;r+=r.conj().T
        r/=max(1,np.linalg.norm(r,2))*2
        # congruence bounds both Q and I-Q away from zero.
        scale=np.sqrt(d*(1-d));q=np.diag(d)+np.einsum('i,ij,j->ij',scale,r,scale)
        return (q+q.conj().T)/2
    def objective(x):
        q=decode(x);v,a=obj(q,bs);scale=np.linalg.norm(q-np.diag(np.diag(q)))**2
        score=v/max(scale,1e-14);calls[0]+=1
        if score>best[0]:best[:]=[score,q,a]
        return -score
    vals=[]
    for j in range(8):
        res=minimize(objective,rng.normal(size=9 if cx else 6),method='Nelder-Mead',options=dict(maxfev=1800,xatol=1e-7,fatol=1e-8))
        vals.append(-res.fun)
    save('normalized_three_'+str(cx),vals,best[1],best[2],dict(evaluations=calls[0],score='lambda_max / squared Frobenius offdiagonal norm'))
