from pathlib import Path
from fractions import Fraction as F
from itertools import product
import time,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
exec(compile((ROOT/'code/arithmetic.py').read_text(encoding='utf-8'),str(ROOT/'code/arithmetic.py'),'exec'))
start=time.perf_counter()
def shift(u,a,v):return plus((Phi((u+v)**2,a*a),F(1,4)),(Phi((u-v)**2,a*a),F(1,4)),(Phi(u*u,a*a),F(-1,2)))
fixtures=[]
for k in [2,4,6]:
    N=1<<k;a=F(1,N);b=F(1,1<<(k//2))
    g=tuple(-1 if z==0 else 1 for z in range(2*N))
    h=tuple((-1)**sum(((z>>j)&1)*((z>>(j+1))&1) for j in range(0,k,2)) for z in range(2*N))
    f=tuple(v for gg,hh in zip(g,h) for v in [gg,hh])
    alpha=inf(f,k+1);eq(alpha,a/2)
    actual=plus((B(f,k+1),F(1)),(B(g,k),F(-1,2)))
    compressed=plus((shift(-a,a,b),F(N-1)),(shift(1-a,a,b),F(1)))
    equal_expr(plus((actual,F(1)),(compressed,F(-1))))
    if k>=4:leq(plus((actual,F(-1))),-alpha*(k-4))
    lo,hi=bounds(actual)
    if k==4:assert lo>2*alpha
    fixtures.append(dict(k=k,influence=str(alpha),D_lower=str(lo),D_upper=str(hi),ratio_lower=str(lo/alpha),ratio_upper=str(hi/alpha)))
monomials=[s for s in range(8) if s.bit_count()<=2];cases=0
for mask in range(128):
    tt=tuple((-1)**sum(1 for j,s in enumerate(monomials) if mask>>j&1 and (z&s)==s) for z in range(8))
    for state in product([-1,0,1],repeat=3):
        if time.perf_counter()-start>55:raise RuntimeError('frozen review deadline')
        free=[i for i in range(3) if state[i]==-1]
        fixed=sum(state[i]<<i for i in range(3) if state[i]!=-1)
        restricted=tuple(tt[fixed+sum(((z>>j)&1)<<i for j,i in enumerate(free))] for z in range(1<<len(free)))
        for i in range(len(free)):
            d=inf(restricted,i)
            eq(d,F(sum(restricted[z]!=restricted[z^(1<<i)] for z in range(len(restricted))),len(restricted)))
            eq(d==0 or d>=F(1,2),True)
        cases+=1
result=dict(status='PASS',exact_assertions=checks,elapsed_seconds=time.perf_counter()-start,
            polynomial_restrictions=cases,A078_fixtures=fixtures)
(ROOT/'out/REVIEW_VALIDATION.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))
