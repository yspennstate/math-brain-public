"""Constrained multistart search with top multiplicity built in, never penalized."""
import os,sys,time,json
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
import numpy as np
from scipy.optimize import minimize
from stratum import *

def frame(theta):
    A=np.zeros((4,4))
    for t,(i,j) in zip(theta,[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]):
        A[i,j]=t; A[j,i]=-t
    R=np.linalg.solve(np.eye(4)-A,np.eye(4)+A)
    return BASIS@R[:,:2]

seed=int(sys.argv[1]) if len(sys.argv)>1 else 41713
starts=int(sys.argv[2]) if len(sys.argv)>2 else 400
rng=np.random.default_rng(seed)

def decode(x):
    U=frame(x[:6]); a=x[6]; b=a*x[7]
    return a,b,U

def fun(x):
    a,b,U=decode(x)
    terms=closed(a,b,U)
    den=sum(terms[:3])
    return 1-terms[3]/max(den,1e-20)

def cons(x):
    a,b,U=decode(x)
    lam,G,Pi,L,z=matrices(a,b,U)
    return np.r_[z,lam-a, sum(closed(a,b,U)[:3])-1e-9]

bounds=[(-100.,100.)]*6+[(1e-7,1),(1e-7,1)]
records=[]; best=None; tic=time.monotonic()
for k in range(starts):
    th=rng.normal(size=6)
    r=10**rng.uniform(-5,0) if k%3==0 else rng.uniform(.01,1)
    U=frame(th); a=tmax(r,U)*rng.uniform(.15,.999)
    x=np.r_[th,a,r]
    if k%8==0 and best is not None:
        x=best['x']+rng.normal(size=8)*rng.choice([.02,.1,.3,1.])
        x[6]=np.clip(x[6],.001,.99); x[7]=np.clip(x[7],.0001,1)
        x[6]=min(x[6],.99*tmax(x[7],frame(x[:6])))
    res=minimize(fun,x,method='SLSQP',bounds=bounds,constraints={'type':'ineq','fun':cons},options={'maxiter':500,'ftol':3e-13})
    feas=float(min(cons(res.x)))
    a,b,U=decode(res.x)
    terms=closed(a,b,U)
    val=ratio(terms)
    rec={'k':k,'success':bool(res.success),'value':float(val),'feasibility':feas,'nit':int(res.nit),'denominator':float(sum(terms[:3])),'a':float(a),'b':float(b)}
    records.append(rec)
    if feas>=-2e-10 and np.isfinite(val) and sum(terms[:3])>1e-8 and (best is None or val<best['value']):
        best=dict(rec,x=res.x.copy())
        print('BEST',k,'ratio',format(val,'.17g'),'feas',feas,'gaps',a,b,flush=True)
        np.savez(f'cayley_best_{seed}.npz',x=res.x,U=U,a=a,b=b,terms=terms)
    if (k+1)%25==0:
        print('PROGRESS',k+1,'seconds',round(time.monotonic()-tic,2),'best',best['value'] if best else None,flush=True)
        with open(f'cayley_search_{seed}.json','w') as f: json.dump(records,f,indent=2)
with open(f'cayley_search_{seed}.json','w') as f: json.dump(records,f,indent=2)
print('FINAL',json.dumps({**best,'x':best['x'].tolist(),'seconds':time.monotonic()-tic}),flush=True)
