"""Independent numerical search using visited-set first-step equations.

One process; BLAS threads fixed before importing numpy. Numerical searches do
not prove uniqueness; the exact cone audit supplies that proof.
"""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
os.environ['VECLIB_MAXIMUM_THREADS']='1'
os.environ['MKL_NUM_THREADS']='1'
import itertools as it
import json
import resource
import signal
import time
from pathlib import Path
import numpy as np
from scipy.optimize import minimize

signal.signal(signal.SIGALRM, lambda *_: (_ for _ in ()).throw(TimeoutError()))
signal.alarm(280)
EDGES=list(it.combinations(range(4),2))
BLOCKS=[]
for size in (3,2,1):
    for S in it.combinations(range(4),size):
        mask=sum(1<<i for i in S)
        BLOCKS.append((mask,list(S),[j for j in range(4) if j not in S]))

def expected(w,h):
    A=np.zeros((4,4))
    for (i,j),v in zip(EDGES,w):
        A[i,j]=A[j,i]=v
    m=A.sum(axis=1)+h
    P=(A+np.diag(h))/m[:,None]
    T=np.zeros((16,4))
    for mask,S,out in BLOCKS:
        rhs=np.ones(len(S))
        for j in out:
            rhs+=P[S,j]*T[mask|1<<j,j]
        T[mask,S]=np.linalg.solve(np.eye(len(S))-P[np.ix_(S,S)],rhs)
    return np.dot(m,[T[1<<i,i] for i in range(4)])/m.sum()

def unpack(v,support,holding):
    logits=np.r_[v[:len(support)-1],0.0]
    z=np.exp(logits-logits.max())
    w=np.zeros(6)
    w[support]=z/z.sum()
    h=v[len(support)-1:] if holding else np.zeros(4)
    return w,h

def run(support,holding,rng,count):
    rows=[]
    for k in range(count):
        v=np.r_[np.clip(rng.normal(0,2.0,len(support)-1),-6,6),
                rng.uniform(0,2,4) if holding else []]
        def objective(x):
            return expected(*unpack(x,support,holding))
        initial=objective(v)
        r=minimize(objective,v,method='L-BFGS-B',
                   bounds=[(-9,9)]*(len(support)-1)+([(0,10)]*4 if holding else []),
                   options=dict(maxiter=350,ftol=1e-13,gtol=2e-7,maxls=35))
        w,h=unpack(r.x,support,holding)
        rows.append(dict(initial=float(initial),value=float(expected(w,h)),success=bool(r.success),
                         iterations=int(r.nit),weights=w.tolist(),holding=h.tolist(),message=str(r.message)))
    return rows

def main():
    start=time.monotonic()
    rng=np.random.default_rng(6302026)
    groups={}
    for holding in (False,True):
        name='K4_support_with_holding' if holding else 'K4_support_no_holding'
        rows=run(list(range(6)),holding,rng,40)
        vals=[r['value'] for r in rows]
        deviations=[max(abs(v-1/6) for v in r['weights']) for r in rows]
        hs=[max(r['holding']) for r in rows]
        summary=dict(restarts=len(rows),minimum=min(vals),maximum_endpoint=max(vals),
                     successful=sum(r['success'] for r in rows),max_weight_error=max(deviations),
                     max_holding=max(hs))
        print(name,json.dumps(summary),flush=True)
        assert min(vals)>=5.5-1e-8 and max(vals)<5.5+1e-8
        assert max(deviations)<2e-5 and max(hs)<1e-7
        groups[name]=dict(summary=summary,runs=rows)
    for name,support in [('path',[0,3,5]),('star',[0,1,2]),('cycle',[0,2,3,5]),('K4_minus_edge',[1,2,3,4,5])]:
        rows=run(support,False,rng,6)
        assert all(r['value']>5.5+1e-5 for r in rows)
        summary=dict(restarts=6,minimum=min(r['value'] for r in rows),maximum_endpoint=max(r['value'] for r in rows))
        print(name,json.dumps(summary),flush=True)
        groups[name]=dict(summary=summary,runs=rows)
    # Ordinary local curvature in the five independent conductance directions.
    eps=1e-3
    f=lambda v:expected(*unpack(v,list(range(6)),False))
    z=np.zeros(5)
    H=np.zeros((5,5))
    for i in range(5):
        ei=np.eye(5)[i]*eps
        H[i,i]=(f(ei)-2*f(z)+f(-ei))/eps**2
        for j in range(i):
            ej=np.eye(5)[j]*eps
            H[i,j]=H[j,i]=(f(ei+ej)-f(ei-ej)-f(-ei+ej)+f(-ei-ej))/(4*eps**2)
    eigenvalues=np.linalg.eigvalsh(H).tolist()
    assert min(eigenvalues)>0
    out=dict(passed=True,groups=groups,finite_difference_hessian_eigenvalues=eigenvalues,
             seconds=time.monotonic()-start,max_rss_bytes=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    Path('referee_numeric_results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Hessian eigenvalues',eigenvalues)
    print('seconds',out['seconds'],'max_rss_bytes',out['max_rss_bytes'])

if __name__=='__main__':
    main()
