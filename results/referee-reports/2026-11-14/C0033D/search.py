"""Sequential seven-variable searches, saving every family best and checkpoint.

Floating point only. Saved near-extremizers must be independently certified.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[k]='1'
import json,time,resource,argparse
from pathlib import Path
import numpy as np
from scipy.optimize import minimize,differential_evolution
from scipy.special import expit
from reduced import kernel,parameters,criterion,jsonable,gauge
from dpp import spectral,random_unitary

SEED=33402
OUT=Path('data/search.json')

def decode(v,eps):
    # A Hermitian logarithm in a seven-entry gauge chart. Gauge the result too.
    a,b,c,x,y,z,t=v
    h=np.array([[a,x,y],[x,b,z+1j*t],[y,z-1j*t,c]])
    lam,u=np.linalg.eigh(h)
    return gauge(spectral(u,eps+(1-2*eps)*expit(lam)))

def encode(q,eps):
    lam,u=np.linalg.eigh(q)
    v=np.clip((lam-eps)/(1-2*eps),1e-14,1-1e-14)
    h=spectral(u,np.log(v/(1-v)))
    # Gauge the logarithm rather than Q.
    h=gauge(h)
    return np.r_[h.diagonal().real,h[0,1].real,h[0,2].real,h[1,2].real,h[1,2].imag]

def sample(rng,kind):
    if kind in ('uniform','spectral_extreme','rank1','rank2','all_zero','all_one'):
        u=random_unitary(rng,3,True)
        if kind=='uniform':lam=rng.uniform(.001,.999,3)
        elif kind=='spectral_extreme':
            e=10**rng.uniform(-9,-1,3);lam=np.where(rng.random(3)<.5,e,1-e)
        elif kind in ('all_zero','all_one'):
            lam=10**rng.uniform(-9,-1,3)
            if kind=='all_one':lam=1-lam
        else:
            e=10**rng.uniform(-9,-1,3);lam=e.copy();lam[:(1 if kind=='rank1' else 2)]=1-e[:(1 if kind=='rank1' else 2)]
        return gauge(spectral(u,lam))
    if kind in ('phase_zero','phase_pi','phase_endpoint'):
        u=random_unitary(rng,3,False)
        eps=10**rng.uniform(-9,-2,3)
        q=spectral(u,np.where(rng.random(3)<.5,eps,1-eps))
        # Mix with a complex kernel: convexity preserves strict feasibility.
        eta=10**rng.uniform(-10,-1) if kind=='phase_endpoint' else 0
        if eta:
            uu=random_unitary(rng,3,True);q=(1-eta)*q+eta*spectral(uu,rng.uniform(.05,.95,3))
        q=gauge(q)
        if kind=='phase_zero' and q[1,2].real<0:return None
        if kind=='phase_pi' and q[1,2].real>0:return None
        return q
    # Diagonally dominant graph, then move towards one spectral boundary.
    diag=rng.uniform(.05,.95,3)
    off=10**rng.uniform(-3,-.25,3)
    if kind=='small_edge':off[rng.integers(3)]*=10**rng.uniform(-10,-2)
    if kind=='disconnected_limit':off[rng.choice(3,2,replace=False)]*=10**rng.uniform(-9,-2)
    q=kernel(np.r_[diag,off,rng.uniform(0,np.pi)])
    # Shrink off diagonal to achieve strict feasibility; do not fill missing edges.
    D=np.diag(diag)
    for _ in range(24):
        ev=np.linalg.eigvalsh(q)
        if ev[0]>1e-9 and ev[-1]<1-1e-9:return q
        q=D+(q-D)*.6
    return None

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--samples',type=int,default=12000)
    ap.add_argument('--starts',type=int,default=36);ap.add_argument('--maxfev',type=int,default=6000)
    ap.add_argument('--de-iter',type=int,default=600);args=ap.parse_args()
    rng=np.random.default_rng(SEED);start=time.monotonic()
    out=dict(seed=SEED,arguments=vars(args),families=[],optimizations=[],de=[],numerical_threads=1,
             priority=os.getpriority(os.PRIO_PROCESS,0))
    best=(-np.inf,None);pool=[]
    def save():
        out['seconds']=time.monotonic()-start
        out['peak_rss_mib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/2**20
        if best[1] is not None:out['best']=jsonable(dict(Q=best[1],**criterion(best[1],True)))
        tmp=OUT.with_suffix('.tmp');tmp.write_text(json.dumps(out,indent=2)+'\n');tmp.replace(OUT)
    for kind in ('uniform','spectral_extreme','rank1','rank2','all_zero','all_one','small_edge','disconnected_limit','phase_zero','phase_pi','phase_endpoint'):
        top=(-np.inf,None);count=0;rejected=0
        for _ in range(args.samples):
            q=sample(rng,kind)
            if q is None:rejected+=1;continue
            try:r=criterion(q)
            except (ArithmeticError,np.linalg.LinAlgError):rejected+=1;continue
            # Guard against ill-conditioned solves in the extreme tails.
            if not 0<=r<=3.001:rejected+=1;continue
            count+=1
            if r>top[0]:top=(r,q)
        if top[1] is not None:
            pool.append(top)
            if top[0]>best[0]:best=top
            out['families'].append(jsonable(dict(family=kind,attempts=args.samples,accepted=count,rejected=rejected,**criterion(top[1],True),Q=top[1])))
        print(kind,count,top[0],flush=True);save()
    pool.sort(key=lambda t:-t[0])
    for eps in (1e-3,1e-5,1e-7):
        def objective(v):
            try:
                r=criterion(decode(v,eps))
                return -r if 0<=r<=3.001 else 10
            except (ArithmeticError,np.linalg.LinAlgError):return 10
        res=differential_evolution(objective,[(-14,14)]*7,popsize=12,maxiter=args.de_iter,
                                   seed=rng,workers=1,polish=False,tol=1e-9,atol=1e-10)
        q=decode(res.x,eps);r=criterion(q);pool.append((r,q))
        if r>best[0]:best=(r,q)
        out['de'].append(jsonable(dict(epsilon=eps,evaluations=res.nfev,converged=bool(res.success),Q=q,**criterion(q,True))))
        print('DE',eps,res.nfev,r,flush=True);save()
    pool.sort(key=lambda t:-t[0])
    for it in range(args.starts):
        eps=(1e-3,1e-5,1e-7)[it%3]
        q=pool[it%len(pool)][1] if it<2*len(pool) else sample(rng,'uniform')
        x0=encode(q,eps)
        if it>=len(pool):x0+=rng.normal(0,.25,7)
        def objective(v):
            try:
                r=criterion(decode(v,eps))
                return -r if 0<=r<=3.001 else 10
            except (ArithmeticError,np.linalg.LinAlgError):return 10
        res=minimize(objective,x0,method='Nelder-Mead',options=dict(maxfev=args.maxfev,xatol=1e-9,fatol=1e-11))
        q=decode(res.x,eps);r=criterion(q)
        if r>best[0]:best=(r,q)
        out['optimizations'].append(jsonable(dict(start=it,epsilon=eps,evaluations=res.nfev,converged=bool(res.success),Q=q,**criterion(q,True))))
        print('NM',it,eps,res.nfev,r,flush=True);save()
    np.savez('data/best.npz',Q=best[1],A=criterion(best[1],True)['A'])
    save()
if __name__=='__main__':main()
