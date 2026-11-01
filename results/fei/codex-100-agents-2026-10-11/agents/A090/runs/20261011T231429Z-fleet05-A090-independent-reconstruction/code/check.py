from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json, time

start=time.perf_counter()
checks=packets=0
def check(x):
    global checks
    assert x
    checks+=1
def spectrum(v):
    n=len(v)
    return [F(sum(v[x]*(-1)**((x&t).bit_count()) for x in range(n)),n) for t in range(n)]
def add(d,x,c):
    if c and x!=1:
        d[x]=d.get(x,F(0))+c
        if not d[x]: del d[x]

cores=[spectrum(v) for v in product([-1,1],repeat=4)]
for a,b in product(cores,repeat=2):
    for p in [F(1,16),F(1,4),F(1,2),F(3,4),F(15,16)]:
        r=min(p,1-p)
        for aa,bb in zip(a,b):
            Q=p*aa*aa+(1-p)*bb*bb
            if not Q: continue
            packets+=1
            z=p*aa*aa/Q
            w=p*(1-p)*(aa-bb)**2/Q
            check(0<=w<=1)
            check(((p*aa+(1-p)*bb)**2+p*(1-p)*(aa-bb)**2)==Q)
            minor=min(z,1-z)+min(w,1-w)
            check((1-minor)**2<=1-r)  # minor >= 1-sqrt(1-r)

balanced=[v for v in product([-1,1],repeat=8) if sum(v)==0]
for v in balanced:
    g=spectrum(v)
    check(g[0]==0)
    check(sum(x*x for x in g)==1)
    for k in [1,2,3]:
        q=F(1,2**k)
        weighted={}; expected={}; queried=F(0)
        for s in range(1,k+1):
            u=F(1,2**s)
            # Actual truth table: last control queried; active iff all controls are zero.
            vals=[v[x>>s] if x%2**s==0 else 1 for x in range(2**s*8)]
            coeff=spectrum(vals)
            query=1<<(s-1)
            lam={}; mismatch={}; d=F(0)
            for t in range(len(coeff)):
                if t&query: continue
                a,b=coeff[t],coeff[t|query]
                Q=a*a+b*b; e=b*b
                d+=e
                check((abs(a+b)-abs(a-b))**2/4==e)
                if e:
                    add(lam,Q/e,e)
                    em=(abs(a+b)-abs(a-b))**2/4
                    add(mismatch,Q/em,em)
            check(lam==mismatch)
            check(d==u)
            direct={}; add(direct,F(2),u-u*u)
            add(direct,(1-2*u+2*u*u)/(u*u),u*u)
            check(lam==direct)
            reach=q/u
            queried+=reach*d
            for x,c in lam.items():add(weighted,x,reach*c)
            add(expected,F(2),q*(1-u))
            add(expected,(1-2*u+2*u*u)/(u*u),q*u)
        check(weighted==expected)
        check(queried==k*q)
        # Expected symbolic formula q[k + sum u(2s-1+log2 Q_s)].
        split={}; add(split,F(2),q*k)
        for s in range(1,k+1):
            u=F(1,2**s); Q=1-2*u+2*u*u
            check(F(1,2)<=Q<=1)
            add(split,F(2),q*u*(2*s-1))
            # Keep Q_s/u^2 as a single logarithm to compare without factorization.
            add(split,F(2),-q*u*2*s)
            add(split,Q/(u*u),q*u)
        check(weighted==split)

result={'status':'PASS','assertions':checks,'singleton_pairs_bias':1280,'nonzero_singleton_packets':packets,'balanced_core_control_cases':len(balanced)*3,'arithmetic':'exact Fraction; formal log argument/coefficient dictionaries','elapsed_seconds':time.perf_counter()-start,'scope':'finite identity validation; analytic proofs in REPORT.md establish universal claims'}
(Path(__file__).resolve().parents[1]/'out'/'CHECK.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result))
