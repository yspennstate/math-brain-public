"""Independent rational, high precision, sparse-law, and cap checks."""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import mpmath as mp
import numpy as np
from independent_iteration import evolve, stats

ROOT=Path(__file__).resolve().parents[1]

def conv(x,y,limit=None):
    length=len(x)+len(y)-1
    if limit is not None: length=min(length,limit+1)
    out=[x[0]*0 for _ in range(length)]
    for i,u in enumerate(x):
        for j,v in enumerate(y[:max(0,length-i)]):
            out[i+j]+=u*v
    return out

def rational_checks():
    records=[]
    for m,b in ((2,2),(2,4),(3,1),(3,2)):
        p=[F(0)]*(b+1);p[b]=F(1,1+((m-1)*b-1)*m**b);p[0]=1-p[b]
        laws=[p]
        maxerr=0
        a=np.zeros(514);a[b]=float(p[b])*m**b;degree=b
        for n in range(4):
            assert sum(p)==1
            assert sum(((m-1)*k-1)*m**k*u for k,u in enumerate(p))==0
            errors=[abs(float(v)-a[k]*float(m)**(-k)) for k,v in enumerate(p) if k>0]
            maxerr=max(maxerr,max(errors))
            c=[F(1)]
            for _ in range(m):c=conv(c,p)
            nxt=[c[0]+c[1]]+c[2:]
            mu=sum(k*v for k,v in enumerate(p));mun=sum(k*v for k,v in enumerate(nxt))
            assert mun==m*mu-1+p[0]**m
            if n<3:
                a,degree,_=evolve(a,m,512,degree)
                p=nxt;laws.append(p)
        for n in range(4):
            for t in range(4-n):
                rhs=m**t*sum(laws[n][t+1:])
                for i in range(n,n+t):rhs*=laws[i][0]**(m-1)
                assert 1-laws[n+t][0]>=rhs
        records.append(dict(m=m,b=b,exact_generations=3,max_FFT_atom_absolute_error=maxerr))
    return records

def tree_check(m):
    # Enumerate all leaves for depth two with values 0 or 3. Test each path event.
    total_events=0
    for leaves in itertools.product((0,3),repeat=m*m):
        child=[max(sum(leaves[j*m:(j+1)*m])-1,0) for j in range(m)]
        root=max(sum(child)-1,0)
        hits=0
        for j in range(m):
            for k in range(m):
                event=(leaves[j*m+k]>=3 and all(leaves[j*m+l]==0 for l in range(m) if l!=k)
                       and all(child[l]==0 for l in range(m) if l!=j))
                if event: hits+=1;assert root>0
        assert hits<=1
        total_events+=hits
    return dict(m=m,depth=2,configurations=2**(m*m),path_event_hits=total_events)

def direct_mp_check(m,b):
    mp.mp.dps=75
    cap=96
    p=[mp.mpf(0)]*(cap+2)
    p[b]=mp.mpf(1)/(1+((m-1)*b-1)*m**b);p[0]=1-p[b]
    a=np.zeros(cap+2);a[b]=float(p[b])*m**b;degree=b
    for n in range(81):
        if n==80: break
        c=[mp.mpf(1)]
        for _ in range(m):c=conv(c,p,cap+1)
        p=[mp.mpf(0)]+c[2:cap+2]
        p[0]=1-sum(p[1:])
        a,degree,_=evolve(a,m,cap,degree)
    q=sum(p[1:]);mu=sum(k*v for k,v in enumerate(p))
    row=stats(a,m,80)
    return dict(m=m,b=b,steps=80,cap=cap,dps=75,
                q_mp=str(q),mean_mp=str(mu),
                relative_q_error=abs(row['n2q']/6400-float(q))/float(q),
                relative_mean_error=abs(row['n2moment_1']/6400-float(mu))/float(mu))

def sparse(m):
    mp.mp.dps=90
    zeta=mp.zeta(2);li=mp.polylog(2,mp.mpf(1)/2)
    epsilon=sum(mp.power(m,-2**j)/(mp.mpf(j)**2*2**j) for j in range(1,13))
    D=(m-1)*zeta-li+epsilon;C=1/D;pzero=C*((m-1)*zeta-li)
    rec=dict(m=m,D=str(D),C=str(C),p_zero=str(pzero),
             normalization=str(pzero+C*epsilon),tilted_mass=str(C*(m-1)*zeta),
             tilted_first_moment=str(C*zeta),subsequence=[])
    for j in (5,10,20,40):
        a=2**j;n=a-1
        pj=C*mp.power(m,-a)/(j*j*a)
        trials=mp.power(m,n)
        lam=trials*pj
        leaf=-mp.expm1(trials*mp.log1p(-pj))
        assert leaf>=lam/2
        rec['subsequence'].append(dict(j=j,n=n,lambda_=str(lam),
                                      n2_leaf_lower=str(n*n*leaf),
                                      n2_half_lambda=str(n*n*lam/2),
                                      log10_pj=str(mp.log10(pj))))
    return rec

if __name__=='__main__':
    output={'rational':rational_checks(),'tree_disjointness':[tree_check(m) for m in (2,3)],
            'sparse':[sparse(m) for m in (2,3)]}
    (ROOT/'data'/'validation.json').write_text(json.dumps(output,indent=2))
    print('Rational, tree, sparse checks passed',flush=True)
    output['high_precision']=[direct_mp_check(m,b) for m,b in ((2,2),(2,4),(3,1),(3,2))]
    (ROOT/'data'/'validation.json').write_text(json.dumps(output,indent=2))
    print('High precision checks passed',flush=True)
    summaries=[]
    for m,b in ((2,2),(2,4),(3,1),(3,2)):
        lo=json.loads((ROOT/'data'/f'm{m}_b{b}_K8192.json').read_text())
        hi=json.loads((ROOT/'data'/f'm{m}_b{b}_K16384.json').read_text())
        keys=[k for k in hi['final'] if k.startswith('n2')]
        summaries.append(dict(m=m,b=b,final=hi['final'],
            max_relative_cap_difference=max(abs(lo['final'][k]/hi['final'][k]-1) for k in keys)))
    (ROOT/'data'/'summary.json').write_text(json.dumps(summaries,indent=2))
    print(json.dumps(output,indent=2),flush=True)
