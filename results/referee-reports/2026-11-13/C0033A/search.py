"""Reproducible exhaustive-atom random and optimized concavity searches."""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource
from pathlib import Path
import numpy as np
from scipy.optimize import minimize
from scipy.special import expit
from dpp import stats,basis,hessian,random_kernel,random_unitary,spectral

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data';DATA.mkdir(exist_ok=True)
RNG=np.random.default_rng(330013)
rows=[];best={};start=time.time()

def save():
    (DATA/'search.json').write_text(json.dumps({'seed':330013,'elapsed_seconds':time.time()-start,
      'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'rows':rows},indent=2)+'\n')

def record(family,n,cx,values,failures=0,**extra):
    row=dict(family=family,n=n,field='complex' if cx else 'real',trials=len(values),
      minimum=float(np.min(values)),median=float(np.median(values)),maximum=float(np.max(values)),
      numerical_errors=failures,**extra)
    rows.append(row);save();print(json.dumps(row),flush=True)

def candidate(key,value,q,a=None,q2=None):
    if key not in best or value>best[key]:
        best[key]=float(value)
        args={'Q':q,'value':value}
        if a is not None:args['A']=a
        if q2 is not None:args['Q2']=q2
        np.savez(DATA/(key+'.npz'),**args)

def search_hessian():
    for n in range(2,7):
        for cx in (False,True):
            b=basis(n,cx)
            for kind in ('uniform','extreme','projection'):
                vals=[];fail=0
                for i in range(100):
                    q=random_kernel(RNG,n,cx,kind)
                    try:
                        hh=hessian(q,b);ev,u=np.linalg.eigh(hh);v=ev[-1]
                        a=np.einsum('b,bij->ij',u[:,-1],b)
                        vals.append(v);candidate(f'hessian_n{n}_{cx}_{kind}',v,q,a)
                    except (ArithmeticError,np.linalg.LinAlgError):fail+=1
                record('full_hessian_'+kind,n,cx,vals,fail)

def direction_search():
    for n,count in ((3,200),(4,200),(6,200),(8,120),(10,60),(12,20),(14,6)):
        for cx in (False,True):
            for kind in ('dense','rank2_psd','rank2_indefinite','commuting','circulant'):
                vals=[];gaps=[];fail=0
                for i in range(count):
                    q=random_kernel(RNG,n,cx,('uniform','extreme','projection')[i%3])
                    if kind=='circulant':
                        f=RNG.uniform(.001,.999,n);g=RNG.uniform(.001,.999,n)
                        if not cx:
                            for j in range(1,n):f[j]=f[n-j];g[j]=g[n-j]
                        u=np.fft.fft(np.eye(n))/np.sqrt(n);q=spectral(u,f);q2=spectral(u,g)
                        if not cx:q=q.real;q2=q2.real
                        a=q2-q
                    elif kind=='commuting':
                        _,u=np.linalg.eigh(q);d=RNG.normal(size=n);a=spectral(u,d)
                        q2=spectral(u,RNG.uniform(.001,.999,n))
                    else:
                        u=random_unitary(RNG,n,cx)
                        d=RNG.normal(size=n) if kind=='dense' else np.r_[1,1 if kind=='rank2_psd' else -1,np.zeros(n-2)]
                        a=spectral(u,d);q2=random_kernel(RNG,n,cx,'extreme' if i%2 else 'uniform')
                    a/=np.linalg.norm(a)
                    try:
                        v=stats(q,a)[1];gap=stats((q+q2)/2)[0]-(stats(q)[0]+stats(q2)[0])/2
                        vals.append(v);gaps.append(gap)
                        candidate(f'direction_n{n}_{cx}_{kind}',v,q,a)
                        candidate(f'midpoint_n{n}_{cx}_{kind}',-gap,q,q2=q2)
                    except ArithmeticError:fail+=1
                record(kind,n,cx,vals,fail,min_midpoint_gap=float(min(gaps)),median_midpoint_gap=float(np.median(gaps)))

def optimize():
    for n in (3,4,5):
        for cx in (False,True):
            b=basis(n,cx);results=[];counts=[];converged=[]
            for restart in range(3):
                calls=[0]
                def decode(x):
                    z=np.einsum('b,bij->ij',x,b);lam,u=np.linalg.eigh(z)
                    return spectral(u,1e-4+(1-2e-4)*expit(lam))
                def objective(x):
                    q=decode(x);hh=hessian(q,b);ev,u=np.linalg.eigh(hh);v=ev[-1]
                    a=np.einsum('b,bij->ij',u[:,-1],b)
                    candidate(f'optimized_n{n}_{cx}',v,q,a);calls[0]+=1
                    return -v
                x=RNG.normal(size=len(b))*(1 if restart==0 else 4)
                res=minimize(objective,x,method='Nelder-Mead',options={'maxfev':1000,'xatol':1e-7,'fatol':1e-10})
                results.append(-res.fun)
                counts.append(calls[0]);converged.append(bool(res.success))
                print('opt',n,cx,restart,-res.fun,calls[0],flush=True)
            record('Nelder_Mead_top_eigenvalue',n,cx,results,evaluations_limit_per_restart=1000,
                   evaluations=counts,optimizer_converged=converged)

if __name__=='__main__':
    import sys
    phase=sys.argv[1] if len(sys.argv)>1 else 'all'
    if phase in ('all','hessian'):search_hessian()
    if phase in ('all','directions'):direction_search()
    if phase in ('all','optimize'):optimize()
    save()
