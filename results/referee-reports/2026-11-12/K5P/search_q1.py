"""Reproducible, single-thread search; each invocation capped at 210 s.

Save stdout to search_q1_output.txt.  Candidate weights are exact decimal
rationals on audit, with every merge checked by independent target solves.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS',
          'VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):
    os.environ[k]='1'
import time, json, resource
from itertools import combinations
from fractions import Fraction as Q
from pathlib import Path
from q1_core import numeric, scan, lump, blocks, exact_scan, serialize
import numpy as np
from scipy.optimize import differential_evolution, minimize

start = time.monotonic()
rng = np.random.default_rng(202611122117)
records = []; evaluations = 0

def matrix(z, n):
    w=np.zeros((n,n)); ix=np.triu_indices(n)
    w[ix] = np.exp(z)
    w[(ix[1],ix[0])] = w[ix]
    return w

for n in (3,4,5,6):
    best=(-1,None,None); pairs=list(combinations(range(n),2))
    for k in range(1200):
        z=rng.uniform(-10,10,n*(n+1)//2)
        w=matrix(z,n)
        if k%3==0:
            mask=rng.random((n,n))<.55
            mask=np.triu(mask,1); mask=mask|mask.T
            w[mask]=0
            for i in range(n-1): w[i,i+1]=w[i+1,i]=np.exp(rng.uniform(-5,5))
        try: ratio,pair=scan(w)
        except np.linalg.LinAlgError: continue
        evaluations+=len(pairs)+1
        if ratio>best[0]: best=(ratio,w.copy(),pair)
    print('random',n,best[0],best[2],flush=True)
    # Fixed last pair is equivalent by relabeling for optimization.
    pair=(n-2,n-1); bs=blocks(n,pair); calls=[0]
    def objective(z):
        calls[0]+=1
        w=matrix(z,n)
        try:
            t=numeric(w); th=numeric(np.array(lump(w,bs)))
            v=th/t
            return -v if np.isfinite(v) and 0<v<20 else 20
        except np.linalg.LinAlgError: return 20
    bounds=[(-12,12)]*(n*(n+1)//2)
    for run in range(3 if n>=4 else 1):
        if time.monotonic()-start>175: break
        result=differential_evolution(objective,bounds,popsize=5,maxiter=150,
                  tol=1e-8,seed=2000+100*n+run,polish=False,workers=1)
        result=minimize(objective,result.x,method='Nelder-Mead',bounds=bounds,
                        options={'maxfev':4500,'xatol':1e-7,'fatol':1e-10})
        w=matrix(result.x,n)
        ratio,p=scan(w)
        if ratio>best[0]: best=(ratio,w.copy(),p)
        print('optimized',n,run,ratio,p,flush=True)
    evaluations+=2*calls[0]
    wq=[[Q(format(x,'.9g')) for x in row] for row in best[1]]
    ex,allpairs=exact_scan(wq)
    best_exact=allpairs[0]
    rec={'n':n,'numeric_ratio':best[0],'weights':wq,'t':ex['t'],
         'maximizers':ex['pairs'],'all_exact_merges':allpairs}
    records.append(rec)
    Path('search_q1_results.json').write_text(json.dumps(serialize(records),indent=2))
    print('exact',n,float(best_exact[0]),best_exact[1],flush=True)
    if best_exact[0]>2:
        print('COUNTEREXAMPLE',flush=True); break
print('evaluations',evaluations,'seconds',time.monotonic()-start,
      'maxrss_bytes',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
