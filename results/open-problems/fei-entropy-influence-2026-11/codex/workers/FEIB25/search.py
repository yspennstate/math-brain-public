"""Bounded-memory edge-profile hill search; incremental Walsh updates."""
import json, math, os, time
from pathlib import Path
import numpy as np
from levels import ROOT, wht, profile, profile_mu, plan, candidates, tribes, threshold

def main():
    started=time.monotonic();rng=np.random.default_rng(251110)
    results=[]
    objectives=['L1','L2','lower_all','tail_linear','global_I']
    for n in [6,8,10,12,14,16]:
        N=1<<n; idx=np.arange(N);wt=np.array([int(i).bit_count() for i in idx]); pp=plan(n)
        # Full truth-table arrays never exceed 2^16; no N by N neighbour array.
        for objective in objectives:
            best=-1.;bestf=None;accepted=0;evaluations=0
            for start_kind in ['random','selector','tribes']:
                if start_kind=='random':f=np.where(rng.random(N)<.5,-1.,1.)
                elif start_kind=='tribes':f=tribes(n,2)
                else:
                    # parity on bit n-1, selector on bit n-2; odd majority below.
                    m=n-3; lower=threshold(m,(m+1)//2)
                    lower=np.tile(lower,2) # one dummy bit, no change to profile
                    h=np.r_[lower,np.ones_like(lower)];f=np.r_[h,-h]
                coeff=wht(f)
                def score(c):
                    nonlocal evaluations
                    W,A,E=profile_mu(c*c,n,pp);den=candidates(W)[objective]
                    rat=np.divide(A[2:],den[2:],out=np.zeros(n-1),where=den[2:]>1e-15)
                    evaluations+=1
                    return float(rat.max()),int(rat.argmax()+2)
                cur,degree=score(coeff)
                budget=80 if n<=12 else 35
                for step in range(budget):
                    xs=rng.integers(0,N,size=1 if step%4 else 2)
                    xs=np.unique(xs)
                    prop=coeff.copy()
                    for x in xs:
                        # Parity of idx & x, using a byte lookup (no dense Walsh matrix).
                        z=(idx & int(x)).astype(np.uint32)
                        parity=np.zeros(N,dtype=np.int8)
                        while np.any(z):parity^=(z&1).astype(np.int8);z>>=1
                        prop-=2*f[x]/N*(1.-2.*parity)
                    new,deg=score(prop)
                    if new>cur+1e-12:
                        f[xs]*=-1;coeff=prop;cur=new;degree=deg;accepted+=1
                if cur>best:best=cur;bestf=f.copy();bestdegree=degree;beststart=start_kind
            row=profile(bestf)
            row.update(objective=objective,best_ratio=best,d=bestdegree,start=beststart,
                       evaluations=evaluations,accepted_moves=accepted,seed=251110)
            name=f'hill_n{n}_{objective}.npz';np.savez_compressed(ROOT/name,f=bestf.astype(np.int8))
            row['truth_table_file']=name;results.append(row)
            (ROOT/'hill.json').write_text(json.dumps(results,indent=2))
            print(n,objective,best,'evaluations',evaluations,flush=True)
    print('elapsed_seconds',time.monotonic()-started,flush=True)

if __name__=='__main__':main()
