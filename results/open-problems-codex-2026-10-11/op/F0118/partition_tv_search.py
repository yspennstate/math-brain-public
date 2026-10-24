"""Bounded follow-up: test the weaker TV comparison for arbitrary partitions."""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import numpy as np,json,time
ROOT=Path(__file__).resolve().parent
def parts(n):
    def rec(a):
        if len(a)==n:yield tuple(a);return
        for k in range(max(a)+2):yield from rec(a+[k])
    return list(rec([0]))
def mat(q,N,ps,root):
    rows=[]
    for word in product(range(1,q+1),repeat=N):
        labs=(root,)+word;row=[]
        for p in ps:
            valid=all(labs[i]==labs[j] for i in range(N+1) for j in range(i) if p[i]==p[j])
            row.append(q**(N-max(p)) if valid else 0)
        rows.append(row)
    return np.array(rows,dtype=np.int64)
start=time.monotonic();rng=np.random.default_rng(11803);count=0;found=False
for N,q,r in [(3,3,4),(4,3,4),(4,4,5),(5,3,4),(5,4,5)]:
    if time.monotonic()-start>20:break
    ps=parts(N+1);sq=mat(q,N,ps,1)-mat(q,N,ps,2);sr=mat(r,N,ps,1)-mat(r,N,ps,2)
    for trial in range(10000):
        if time.monotonic()-start>20:break
        ix=rng.choice(len(ps),size=int(rng.integers(2,9)),replace=False);ws=rng.integers(1,10,len(ix))
        numeratorq=int(np.abs(sq[:,ix]@ws).sum());numeratorr=int(np.abs(sr[:,ix]@ws).sum())
        count+=1
        # Denominator common factor 2*sum(ws) can be omitted in this sign comparison.
        if numeratorr*q**N < numeratorq*r**N:
            tvq=F(numeratorq,2*int(ws.sum())*q**N);tvr=F(numeratorr,2*int(ws.sum())*r**N)
            payload={'N':N,'q':q,'r':r,'prior':[[list(ps[i]),int(w)] for i,w in zip(ix,ws)],
                     'prior_denominator':int(ws.sum()),'TV_q':str(tvq),'TV_r':str(tvr),'difference':str(tvr-tvq)}
            (ROOT/'partition_tv_witness.json').write_text(json.dumps(payload,indent=2),encoding='utf8')
            print('EXACT AUXILIARY TV WITNESS',json.dumps(payload),flush=True);found=True;break
    print('searched',N,q,r,'total priors',count,flush=True)
    if found:break
result={'seed':11803,'tested_priors':count,'found_TV_reversal':found,'wall_seconds':time.monotonic()-start,'wall_limit_seconds':20}
(ROOT/'partition_tv_search_summary.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result),flush=True)
