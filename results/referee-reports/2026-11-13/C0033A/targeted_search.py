"""Optimize circulant-symbol Hessians and test genuine rank-two midpoints."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit
from dpp import stats,basis,hessian,random_kernel,random_unitary,spectral

root=Path(__file__).resolve().parent;data=root/'data';rng=np.random.default_rng(330014)
rows=[];start=time.time()
for n in (3,4,6,8):
    u=np.fft.fft(np.eye(n))/np.sqrt(n)
    for cx in (False,True):
        groups=[[j] for j in range(n)] if cx else [[0]]+[[j,n-j] for j in range(1,(n+1)//2)]+([[n//2]] if n%2==0 else [])
        b=np.array([spectral(u,np.isin(np.arange(n),g).astype(float)/np.sqrt(len(g))) for g in groups])
        if not cx:b=b.real
        best=-np.inf;calls=0;values=[]
        def objective(x):
            global best,calls
            f=np.zeros(n)
            for j,g in enumerate(groups):f[g]=1e-5+(1-2e-5)*expit(x[j])
            q=spectral(u,f)
            if not cx:q=q.real
            hh=hessian(q,b);ev,vec=np.linalg.eigh(hh);v=ev[-1];calls+=1
            if v>best:
                best=v;a=np.einsum('b,bij->ij',vec[:,-1],b)
                np.savez(data/f'circulant_optimized_n{n}_{cx}.npz',Q=q,A=a,symbol=f,value=v)
            return -v
        for restart in range(3):
            result=minimize(objective,rng.normal(size=len(groups))*(1+2*restart),method='Nelder-Mead',options={'maxfev':1000,'xatol':1e-7,'fatol':1e-12})
            values.append(float(-result.fun))
        row={'family':'circulant_symbol_optimization','n':n,'field':'complex' if cx else 'real','starts':3,'evaluations':calls,'max_second':float(best),'final_values':values}
        rows.append(row);print(json.dumps(row),flush=True)
for n in (3,4,6,8,10):
    for cx in (False,True):
        for definite in (False,True):
            gaps=[];steps=[]
            for trial in range(100):
                q=random_kernel(rng,n,cx,'uniform');u=random_unitary(rng,n,cx)
                a=spectral(u,np.r_[1,1 if definite else -1,np.zeros(n-2)])/np.sqrt(2)
                lam=np.linalg.eigvalsh(q);step=.9*min(lam.min(),1-lam.max())/np.linalg.norm(a,2)
                gap=stats(q)[0]-(stats(q+step*a)[0]+stats(q-step*a)[0])/2
                gaps.append(float(gap));steps.append(float(step))
            row={'family':'rank2_midpoint_psd' if definite else 'rank2_midpoint_indefinite','n':n,'field':'complex' if cx else 'real','trials':100,'minimum_gap':min(gaps),'median_gap':float(np.median(gaps)),'minimum_step':min(steps)}
            rows.append(row);print(json.dumps(row),flush=True)
(data/'targeted.json').write_text(json.dumps({'seed':330014,'elapsed_seconds':time.time()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,'rows':rows},indent=2)+'\n')
