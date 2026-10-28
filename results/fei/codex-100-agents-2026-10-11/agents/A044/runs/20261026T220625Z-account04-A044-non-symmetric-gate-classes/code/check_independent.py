from pathlib import Path
from fractions import Fraction as Q
from itertools import product, combinations
import json,time
root=Path(__file__).resolve().parents[1]
t0=time.monotonic()
rows=[]
checks=0
for n in range(4):
    xs=list(product((-1,1),repeat=n))
    expected=set()
    for out in (-1,1):
        expected.add(tuple(out for _ in xs))
        for i in range(n):
            expected.add(tuple(out*x[i] for x in xs))
        for ij in combinations(range(n),2):
            for signs in product((-1,1),repeat=2):
                expected.add(tuple(out*(1 if all(x[i]==s for i,s in zip(ij,signs)) else -1) for x in xs))
        for ijk in combinations(range(n),3):
            for signs in product((-1,1),repeat=3):
                expected.add(tuple(out*(1 if sum(x[i]*s for i,s in zip(ijk,signs))>0 else -1) for x in xs))
    found=set()
    for f in product((-1,1),repeat=len(xs)):
        lookup=dict(zip(xs,f))
        valid=True
        for i in range(n):
            ds=[]
            for y in product((-1,1),repeat=n-1):
                lo=list(y);lo.insert(i,-1)
                hi=list(y);hi.insert(i,1)
                ds.append(Q(lookup[tuple(hi)]-lookup[tuple(lo)],2))
            d=sum(z*z for z in ds)/len(ds)
            t=abs(sum(ds)/len(ds))
            valid &= d==t and t in (0,Q(1,2),1)
        if valid: found.add(f)
    assert found==expected
    checks+=1
    rows.append(dict(n=n,templates=len(expected),actual=len(found)))

# Exact positive/zero scalar residuals using atanh log bounds and proved tail.
def ln_bounds(x):
    # only x in [1,2] here; z in [0,1/3]
    z=(x-1)/(x+1)
    terms=24
    lo=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(terms)),Q(0))
    tail=2*z**(2*terms+1)/(Q(2*terms+1)*(1-z*z))
    return lo,lo+tail
for den in (2,4,8,16):
    for num in range(1,den+1):
        t=Q(num,den);j=0;u=t
        while 2*u<=1:u*=2;j+=1
        lo,hi=ln_bounds(1/u)
        lower=t*(1-t)-t*t*(j+hi)
        if t in (1,Q(1,2)):
            assert lower==0
        else: assert lower>0
        checks+=1
out=dict(status='PASS',checks=checks,domain=rows,scalar_cases=30,
         arithmetic='Fraction direct physical cofactors; explicit signed gate templates; rigorous 24-term atanh interval with geometric tail',
         seconds=time.monotonic()-t0)
(root/'out/INDEPENDENT.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
