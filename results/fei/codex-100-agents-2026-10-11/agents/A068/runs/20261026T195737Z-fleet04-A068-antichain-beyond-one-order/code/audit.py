from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json,time
R=Path(__file__).resolve().parents[1]; t=time.perf_counter(); count=0
def ck(x):
    global count
    count+=1; assert x,count
    assert time.perf_counter()-t<45
def par(x): return x.bit_count()%2
def spectrum(a):
    n=len(a)
    return [F(sum(v*(-1 if par(s&x) else 1) for x,v in enumerate(a)),n)**2 for s in range(n)]
def lin(cols,x):
    v=0
    for i,c in enumerate(cols):
        if x>>i&1:v^=c
    return v
maps=[c for c in product(range(1,8),repeat=3) if len({lin(c,x) for x in range(8)})==8]
ck(len(maps)==168)
V={0,3}; group=[c for c in maps if lin(c,3)==3]; ck(len(group)==24)
ck({lin(c,1) for c in group}==set(range(8))-V)
q=[F(i+1,36) for i in range(8)]
qb=[sum((q[lin(c,x)] for c in group),F(0))/len(group) for x in range(8)]
ck(all(qb[x]==q[x] for x in V)); ck(len({qb[x] for x in range(8) if x not in V})==1)
for mask in range(4):
    base=[1 if mask>>par(3&x)&1 else -1 for x in range(8)]
    for e in range(8):
        f=list(base);f[e]*=-1
        p=spectrum(f)
        for c in group:ck(all(p[lin(c,x)]==p[x] for x in range(8)))
        for ass in product((-1,0,1),repeat=3):
            keep=[i for i,b in enumerate(ass) if b<0]
            addr=[sum(((x>>j)&1)<<i for j,i in enumerate(keep))+sum(b<<i for i,b in enumerate(ass) if b>=0) for x in range(1<<len(keep))]
            child=spectrum([f[x] for x in addr])
            image={sum(((s>>i)&1)<<j for j,i in enumerate(keep)) for s in V}
            outside=[child[x] for x in range(len(child)) if x not in image]
            ck(len(set(outside))<=1)
# Two-point edit of x0: partial return is NOT free. Exact cost is H+3/4.
f=[-1 if x&1 else 1 for x in range(8)]
for e in (0,1):f[e]*=-1
p=spectrum(f); V2={0,1}; outside=[s for s in range(8) if s not in V2]
ck(sorted(v for v in p if v)==[F(1,4)]*4)
ck(sum((p[s] for s in outside),F(0))==F(3,4))
qstar=sum((p[s] for s in outside),F(0))/len(outside)
ck(qstar==F(1,8)); ck(all(p[s]/qstar==2 for s in outside if p[s]))
# Each occupied outside atom has log2 ratio exactly one, hence debit 3/4.
result=dict(status='PASS',assertions=count,seconds=time.perf_counter()-t,GL3_maps=len(maps),stabilizer_maps=len(group),two_point_debit='3/4',representation='direct character sums and explicit GL enumeration; no primary imports')
(R/'out/AUDIT.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result))
