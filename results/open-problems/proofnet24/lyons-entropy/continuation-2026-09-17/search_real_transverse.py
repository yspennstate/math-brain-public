"""Search Fisher-blind imaginary directions at real DPP kernels."""
import json,time
from pathlib import Path
import numpy as np
from scipy.special import expit
from scipy.optimize import minimize
from search_hessian import basis,curvature

def main():
    rng=np.random.default_rng(9172026);out=[];start=time.time()
    for n,count in [(4,5000),(5,3000),(6,1000)]:
        E=basis(n);E=E[np.any(abs(E.imag)>0,axis=(1,2))]
        idx=np.triu_indices(n);seeds=[];best=1e100;rec=None
        def kernel(x):
            B=np.zeros((n,n));B[idx]=x;B=B+B.T-np.diag(np.diag(B))
            w,U=np.linalg.eigh(B);p=1e-5+(1-2e-5)*expit(w)
            return (U*p)@U.T
        def value(x,save=False):
            nonlocal best,rec
            K=kernel(x)
            try:Q,p=curvature(K,E);w,V=np.linalg.eigh(Q)
            except (ValueError,np.linalg.LinAlgError):return 1e10
            val=float(w[0])
            if val<best:
                best=val;A=np.einsum('a,aij->ij',V[:,0],E)
                rec=dict(n=n,min_curvature=best,K=K.tolist(),A_imag=A.imag.tolist(),kernel_eigenvalues=np.linalg.eigvalsh(K).tolist(),atom_min=float(p.min()))
            return val
        for k in range(count):
            x=rng.normal(size=len(idx[0]))*rng.choice([.3,1,3,6]);val=value(x)
            if n==4 and val>1e-7:seeds.append((val,x))
        optim=[]
        if n==4:
            for val,x in sorted(seeds,key=lambda z:z[0])[:10]:
                r=minimize(value,x,method='L-BFGS-B',bounds=[(-12,12)]*len(x),options={'maxiter':250,'ftol':1e-13,'gtol':1e-9,'maxls':30})
                optim.append(dict(initial=val,final=float(r.fun),success=bool(r.success),nfev=int(r.nfev),message=str(r.message)))
        rec['random_count']=count;rec['optimizations']=optim;out.append(rec)
        Path('real_transverse_search.json').write_text(json.dumps(dict(records=out,elapsed=time.time()-start),indent=2));print(json.dumps({k:v for k,v in rec.items() if k not in ['K','A_imag']}),flush=True)

if __name__=='__main__':main()
