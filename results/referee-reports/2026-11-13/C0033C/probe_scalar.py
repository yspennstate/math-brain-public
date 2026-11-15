"""Search the exact three-point scalar criterion from C0033B (17)."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'): os.environ[k]='1'
import json,time,resource
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from dpp import basis, probabilities, hessian, random_kernel, spectral, stats
B=basis(3,True)

def certificate(q, details=False):
    p,m=probabilities(q)
    ell=np.log([p[2]*p[4]/(p[0]*p[6]),p[1]*p[4]/(p[0]*p[5]),p[1]*p[2]/(p[0]*p[3])])
    gamma=np.log(p[7]*p[1]*p[2]*p[4]/(p[0]*p[3]*p[5]*p[6]))
    r=np.diag(ell)-gamma*q
    vals,u=np.linalg.eigh(r)
    if vals[0]<=1e-14: raise ArithmeticError('R numerically singular')
    root=spectral(u,np.sqrt(vals))
    dirs=np.einsum('ij,bjk,kl->bil',root,B,root,optimize=False)
    inv=np.linalg.inv(m)
    dp=p[:,None]*np.einsum('sij,bji->sb',inv,dirs,optimize=False).real
    f=np.einsum('sb,sc,s->bc',dp,dp,1/p,optimize=False)/np.prod(vals)
    z=np.trace(B,axis1=1,axis2=2).real
    v=np.linalg.solve(np.eye(9)+f,z)
    ratio=float(z@v)
    if not details:return ratio
    a=np.einsum('b,bij->ij',v,dirs)
    a=(a+a.conj().T)/2
    a/=np.linalg.norm(a)
    return ratio,r,a,float(np.linalg.eigvalsh(hessian(q,B))[-1])

def decode(v):
    # A bounded entry parametrization via spectral logistic; all 9 variables used.
    x=np.einsum('b,bij->ij',v,B)
    lam,u=np.linalg.eigh(x)
    lam=1e-5+(1-2e-5)/(1+np.exp(-np.clip(lam,-30,30)))
    return spectral(u,lam)

def main():
    rng=np.random.default_rng(33361);t=time.monotonic();rows=[];best=(-1,None)
    for kind in ('uniform','extreme','projection'):
        ratios=[]
        for it in range(1500):
            q=random_kernel(rng,3,True,kind)
            try:r=certificate(q)
            except (ArithmeticError,np.linalg.LinAlgError):continue
            ratios.append(r)
            if r>best[0]:best=r,q
        rows.append(dict(family=kind,accepted=len(ratios),max_ratio=max(ratios),min_ratio=min(ratios)))
        print(rows[-1],flush=True)
    def objective(v):
        try:return -certificate(decode(v))
        except (ArithmeticError,np.linalg.LinAlgError):return 100
    opt=[]
    for it in range(8):
        q=best[1] if it==0 else random_kernel(rng,3,True,'uniform')
        lam,u=np.linalg.eigh(q)
        x=spectral(u,np.log(lam/(1-lam)))
        v=np.einsum('bij,ji->b',B,x).real
        res=minimize(objective,v,method='Nelder-Mead',options=dict(maxfev=1600,xatol=1e-8,fatol=1e-10))
        r=-res.fun;opt.append(dict(start=it,ratio=r,evaluations=res.nfev,converged=bool(res.success)))
        if r>best[0]:best=r,decode(res.x)
        print(opt[-1],flush=True)
    r,rr,a,ev=certificate(best[1],True)
    np.savez('data/scalar_witness.npz',Q=best[1],R=rr,A=a)
    out=dict(seed=33361,rows=rows,optimizations=opt,best_ratio=r,full_hessian_largest=ev,curvature=float(stats(best[1],a)[1]),seconds=time.monotonic()-t,peak_rss_mib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20)
    Path('data/scalar_search.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out,flush=True)
if __name__=='__main__':main()
