from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import reference_v1 as ref
import prime_poly as kernel
import json,time

OUT=Path(__file__).resolve().parents[1]/'out'; start=time.monotonic(); rows=[]
for t in [863,64672]:
    gates=ref.primes(t,4); a=ref.walsh(t,4); N=len(gates)
    assert N==3
    natural=[[j for j in range(4) if m>>j&1] for m,v in gates]
    for flips in product([0,1],repeat=N):
        assert time.monotonic()-start<60
        orders=[o[::-1] if f else o for o,f in zip(natural,flips)]
        poly={A:kernel.extract(A,gates,orders,4) for A in range(1,16) if a[A]}; best=None
        for lam in product([Q(j,8) for j in range(1,9)],repeat=N):
            if any(sum(lam[l] for l,(m,v) in enumerate(gates) if m>>j&1)>1 for j in range(4)): continue
            lo,hi=kernel.residual(poly,lam,a,4)
            if best is None or hi<best[1]: best=(lo,hi,lam)
        rows.append({'truth':t,'gates':gates,'orders':orders,'lo':str(best[0]),'hi':str(best[1]),'midpoint':float((best[0]+best[1])/2),'lambda':[str(x) for x in best[2]],'polynomials':{str(A):[[m,d,str(c)] for (m,d),c in sorted(p.items())] for A,p in poly.items()}})
rows.sort(key=lambda x:Q(x['hi']))
(OUT/'p4_candidates.json').write_text(json.dumps({'elapsed_seconds':time.monotonic()-start,'rows':rows},indent=2))
print(json.dumps({'elapsed_seconds':time.monotonic()-start,'best':{k:v for k,v in rows[0].items() if k!='polynomials'}},indent=2))
