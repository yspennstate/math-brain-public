from pathlib import Path
from itertools import product
from fractions import Fraction
from math import prod
import json,time
root=Path(__file__).resolve().parents[1];start=time.perf_counter();counts=[];screened=odd=accepted=0
for m in range(3):
    P=1<<m;num=0
    for h in product((-2,-1,0,1,2),repeat=P):
        screened+=1;M=[y for y,x in enumerate(h) if abs(x)==1]
        if len(M)%2==0:continue
        odd+=1
        W=[sum(h[y]*(-1)**((s&y).bit_count()) for y in range(P)) for s in range(P)]
        z=sum(x*x for x in W);marg=[sum(x*x for s,x in enumerate(W) if s>>i&1) for i in range(m)]
        if m and not all(W[s]**2*z**(m-1)==prod(marg[i] if s>>i&1 else z-marg[i] for i in range(m)) for s in range(P)):continue
        accepted+=1;num+=1
        if not m:continue
        ratios=[Fraction(abs(W[1<<i]),abs(W[0])) for i in range(m)]
        a=[x.denominator for x in ratios];b=[x.numerator for x in ratios]
        assert abs(W[0])==prod(a)
        D=prod(x*y for x,y in zip(a,b));E=[y for y,x in enumerate(h) if abs(x)==2]
        t=sum((-1)**y.bit_count() for y in M);te=sum((-1)**y.bit_count() for y in E)
        assert (t+4*te)%D==0
        assert prod((x*x+y*y)//2 for x,y in zip(a,b))==len(M)+4*len(E)
        assert len(M)%4==1
        assert sum(W[s]*W[s^(P-1)] for s in range(P))==P*(t+4*te)
    counts.append({'m':m,'admitted_odd_rows':num})
assert screened==655 and odd==326
out={'status':'PASS','screened':screened,'odd_mask_rows':odd,'product_rows':accepted,'counts':counts,'runtime_seconds':time.perf_counter()-start}
(root/'out'/'shared_validation.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out,indent=2))
