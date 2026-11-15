"""Bounded single-process search for tau1/tau0. All exponentials use Q directly."""
import os
for key in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
    os.environ[key]='1'
import json, signal, time
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq, differential_evolution, minimize
signal.alarm(240)
START=time.monotonic(); DEADLINE=START+180
rng=np.random.default_rng(4482026)
TARGET=np.exp(-1)
counts={'birth_death':0,'general':0}
best={}; records=[]

class Budget(Exception): pass

def assess(q,pi,kind,meta):
    if time.monotonic()>DEADLINE: raise Budget()
    n=len(pi)
    q=q/np.max(-np.diag(q))
    proj=np.tile(pi,(n,1))
    try:
        z=np.linalg.solve(proj-q,np.eye(n))-proj
        t0=np.trace(z)
        if not np.isfinite(t0) or t0<=0: return 0.
        def distance(t):
            p=expm(t*q)
            return np.max(np.sum(np.abs(p[:,None,:]-p[None,:,:]),axis=2))/2
        hi=2*t0
        while distance(hi)>TARGET:
            hi*=2
            if hi>128*t0: return 0.
        # Root finding on dimensionless time avoids absolute tolerances at huge t0.
        root=brentq(lambda r:distance(r*t0)-TARGET,0,hi/t0,xtol=2e-11,rtol=1e-12)
    except (np.linalg.LinAlgError,ValueError,OverflowError): return 0.
    counts[kind]+=1
    record={'ratio':float(root),'tau0':float(t0),'tau1':float(root*t0),
            'n':n,'kind':kind,'Q':q.tolist(),'pi':pi.tolist(),'meta':meta}
    if kind not in best or root>best[kind]['ratio']:
        best[kind]=record
    if not records or root>max(r['ratio'] for r in records):
        records.append(record)
        with open('ratio_search_checkpoint.json','w') as f:
            json.dump({'counts':counts,'best':best,'records':records},f,indent=2)
    return root

def bd(params,n):
    # Fix the first down-rate to 1; all other directed rates vary independently.
    down=np.r_[1.,np.exp(params[:n-2])]
    up=np.exp(params[n-2:])
    q=np.zeros((n,n)); weights=np.ones(n)
    for j in range(n-1):
        q[j,j+1]=up[j];q[j+1,j]=down[j]
        weights[j+1]=weights[j]*up[j]/down[j]
    pi=weights/weights.sum()
    q[np.diag_indices(n)]=-q.sum(axis=1)
    return q,pi

def general(params,n):
    logpi=np.r_[0.,params[:n-1]]
    pi=np.exp(logpi-np.max(logpi));pi/=pi.sum()
    edges=np.triu_indices(n,1)
    c=np.zeros((n,n));c[edges]=np.exp(params[n-1:]);c+=c.T
    q=c/pi[:,None];q[np.diag_indices(n)]=-q.sum(axis=1)
    return q,pi

def bd_obj(x,n):
    q,pi=bd(x,n)
    return -assess(q,pi,'birth_death',{'parameters':list(x),'phase':'optimizer'})

def gen_obj(x,n):
    q,pi=general(x,n)
    return -assess(q,pi,'general',{'parameters':list(x),'phase':'optimizer'})

def main():
    completed=[]
    try:
        # Baselines for every size through eight, including a very strongly biased chain.
        for n in range(3,9):
            for eps in [1e-3,1e-5,1e-8,1e-10]:
                x=np.r_[np.zeros(n-2),np.full(n-1,np.log(eps))]
                q,pi=bd(x,n);assess(q,pi,'birth_death',{'phase':'uniform_baseline','eps':eps})
        # Independent, broad random samples: 2,400 birth-and-death and 2,400 complete graphs.
        for trial in range(2400):
            n=3+trial%6
            x=np.r_[rng.uniform(-2,2,n-2),rng.uniform(-16,2,n-1)]
            q,pi=bd(x,n);assess(q,pi,'birth_death',{'phase':'random','trial':trial})
            n=3+trial%6
            z=np.r_[rng.uniform(-5,5,n-1),rng.uniform(-7,4,n*(n-1)//2)]
            q,pi=general(z,n);assess(q,pi,'general',{'phase':'random','trial':trial})
        completed.append('4800 random candidates')
        for n in [5,4,6,3,7,8]:
            bounds=[(-2,2)]*(n-2)+[(-23,1)]*(n-1)
            initial=np.r_[np.zeros(n-2),np.full(n-1,-18.)]
            res=differential_evolution(bd_obj,bounds,args=(n,),rng=rng,popsize=6,maxiter=35,
                                       polish=False,workers=1,x0=initial,tol=1e-9)
            local=minimize(bd_obj,res.x,args=(n,),method='L-BFGS-B',bounds=bounds,
                           options={'maxiter':60,'ftol':1e-13,'maxfun':2500})
            completed.append('birth-death n='+str(n))
        for n in [3,4,5,6,7,8]:
            bounds=[(-7,7)]*(n-1)+[(-9,5)]*(n*(n-1)//2)
            res=differential_evolution(gen_obj,bounds,args=(n,),rng=rng,popsize=4,maxiter=22,
                                       polish=False,workers=1,tol=1e-7)
            minimize(gen_obj,res.x,args=(n,),method='L-BFGS-B',bounds=bounds,
                     options={'maxiter':20,'ftol':1e-10,'maxfun':500})
            completed.append('general n='+str(n))
    except Budget:
        completed.append('180-second wall budget reached; current optimizer interrupted')
    out={'seed':4482026,'counts':counts,'best':best,'record_improvements':records,
         'completed':completed,'seconds':time.monotonic()-START,
         'warning':'Floating-point search only; finalists require high-precision verification.'}
    with open('ratio_search_results.json','w') as f: json.dump(out,f,indent=2)
    print(json.dumps({'counts':counts,'best_ratios':{k:v['ratio'] for k,v in best.items()},
                      'completed':completed,'seconds':out['seconds']},indent=2))

if __name__=='__main__':main()
