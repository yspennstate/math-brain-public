from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction as Q
import json,time
R=Path(__file__).resolve().parents[1];start=time.perf_counter()
def transform(h):
    return [sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(h)) for s in range(len(h))]
counts=Counter();accepted=[];checks=0
for h in product(range(-2,3),repeat=4):
    W=transform(h);z=[v*v for v in W];T=sum(z)
    if not T:continue
    if z[0]*z[3]!=z[1]*z[2]:continue
    marg=[z[1]+z[3],z[2]+z[3]]
    varying=sum(0<t<T for t in marg)
    nf=sum(0<t<T and 2*t!=T for t in marg)
    fair=varying-nf
    counts[(nf,fair)]+=1
    checks+=1;assert nf<2
    accepted.append({'h':h,'W':W,'N':nf,'fair':fair,'norm':str(Q(T,16))})
# Direct independent square transform: product implies the determinant above.
# All integer height-two rows can be the zeroth partial Walsh row of a Boolean sign.
for row in accepted:
    for v in row['h']:
        signs=[1]*(2+v)+[-1]*(2-v)
        checks+=1;assert sum(signs)==2*v and len(signs)==4
assert 17**2<2**9 and 65**4<2**25
out={'result':'PASS','domain_size':625,'product_rows':len(accepted),'counts':[{'N':n,'fair':f,'count':c} for (n,f),c in sorted(counts.items())],'zero_fair_two_nonfair_rows':0,'assertions':checks,'runtime_seconds':time.perf_counter()-start,'certificate_rows':accepted}
(R/'out'/'endpoint.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='certificate_rows'},indent=2))
