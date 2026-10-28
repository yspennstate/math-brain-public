from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import json,time
R=Path(__file__).resolve().parents[1]; start=time.perf_counter(); checks=0
def ck(b):
    global checks
    checks+=1
    assert b
def ln_bounds(q):
    w=(q-1)/(q+1); s=Q(0); t=w
    for j in range(60): s+=t/(2*j+1); t*=w*w
    return 2*s,2*s+2*t/(121*(1-w*w))
l2,u2=ln_bounds(Q(2))
def log2_bounds(q):
    e=0
    while q<1: q*=2;e-=1
    while q>=2:q/=2;e+=1
    l,u=ln_bounds(q)
    return e+l/u2,e+u/l2
rows=[]
for k in range(2,9):
    N=k+2; L=1<<N
    f=[(-1 if y&3==0 else 1)*(-1 if y.bit_count()<=1 else 1) for y in range(L)]
    a=list(f);h=1
    while h<L:
        for j in range(0,L,2*h):
            for i in range(j,j+h):u,v=a[i],a[i+h];a[i],a[i+h]=u+v,u-v
        h*=2
    ck(sum(v*v for v in a)==L*L)
    lo=hi=Q(0)
    for v,count in Counter(x*x for x in a if x).items():
        p=Q(v,L*L); l,u=log2_bounds(p);lo-=count*p*u;hi-=count*p*l
    ck(lo>1)
    I=Q(sum(f[y]!=f[y^(1<<i)] for y in range(L) for i in range(N)),L)
    ck(I==1+Q(k*k-k+2,2**(k+1)))
    rows.append(dict(k=k,I=str(I),H_lower_gt_one=True,H_interval_width=str(hi-lo),H_lower_floor_1e6=(lo*10**6).__floor__(),H_upper_ceil_1e6=(hi*10**6).__ceil__()))
# k=1 really can admit a one-output proper block; g is the same literal seed.
f=[(-1 if y&3==0 else 1)*(-1 if y.bit_count()<=1 else 1) for y in range(8)]
rr={tuple(f[x|z] for z in (0,4)) for x in range(4)}
ck(len(rr)==2)
ck(136**4<2**34);ck(35**4<2*34**4)
result=dict(status='PASS',exact_assertions=checks,entropy_rows=rows,missing_fresh_bit_rows=[list(r) for r in sorted(rr)],threshold_signs=['136^4<2^34','35^4<2*34^4'],seconds=time.perf_counter()-start)
(R/'out/AUDIT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='entropy_rows'}))
