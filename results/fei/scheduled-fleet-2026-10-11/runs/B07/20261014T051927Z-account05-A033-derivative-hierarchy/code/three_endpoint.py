from pathlib import Path
from itertools import product
from collections import Counter
import json,time,math
R=Path(__file__).resolve().parents[1];start=time.perf_counter();counts=Counter();hits=[];cases=0
def walsh(h):
    a=list(h)
    for step in (1,2,4):
        for j in range(0,8,step*2):
            for k in range(j,j+step):u,v=a[k],a[k+step];a[k],a[k+step]=u+v,u-v
    return a
for h in product(range(-2,3),repeat=8):
    cases+=1;a=walsh(h);z=[v*v for v in a];T=sum(z)
    if not T:continue
    m=[z[1]+z[3]+z[5]+z[7],z[2]+z[3]+z[6]+z[7],z[4]+z[5]+z[6]+z[7]]
    if any(z[s]*T*T != math.prod(m[i] if s>>i&1 else T-m[i] for i in range(3)) for s in range(8)):continue
    N=sum(0<v<T and 2*v!=T for v in m);f=sum(2*v==T for v in m)
    counts[(N,f)]+=1
    if N>=2:hits.append({'h':h,'W':a,'N':N,'fair':f})
out={'result':'PASS' if not hits else 'ENDPOINT_EXISTS','case_count':cases,'counts':[{'N':n,'fair':f,'count':v} for (n,f),v in sorted(counts.items())],'rows_with_two_or_more_nonfair':hits,'runtime_seconds':time.perf_counter()-start}
(R/'out'/'three_endpoint.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
