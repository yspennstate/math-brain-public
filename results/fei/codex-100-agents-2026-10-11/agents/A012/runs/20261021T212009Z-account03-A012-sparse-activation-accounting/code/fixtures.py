from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from itertools import permutations,combinations
from collections import defaultdict
import json,time
R=Path(__file__).resolve().parents[1];t0=time.perf_counter();checks=0
def ck(x):
    global checks
    assert x;checks+=1
def walsh(a):
    return [Q(sum(v*(-1)**((s&t).bit_count()%2) for s,v in enumerate(a)),len(a)) for t in range(len(a))]
def influence(a):
    return sum((Q(sum(a[x]!=a[x^(1<<j)] for x in range(len(a))),len(a)) for j in range((len(a)-1).bit_length())),Q(0))
@lru_cache(None)
def fac(n):
    out={};p=2
    while p*p<=n:
        while n%p==0:out[p]=out.get(p,0)+1;n//=p
        p+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(*vectors):
    out=defaultdict(Q)
    for scale,vec in vectors:
        for p,x in vec.items():out[p]+=scale*x
    return {p:x for p,x in out.items() if x}
def log(q):return add((1,fac(q.numerator)),(-1,fac(q.denominator)))
def L(q):return add((-q,log(q))) if q else {}
def entropy(p):return add(*[(1,L(x)) for x in p])
def ce(p,r):
    ck(all(not x or y>0 for x,y in zip(p,r)))
    return add(*[(-x,log(y)) for x,y in zip(p,r) if x])
classification=json.loads((R/'out'/'CLASSIFICATION.json').read_text(encoding='utf-8'))
for mask in range(256):
    c=[(-1)**((mask>>s)&1) for s in range(8)];images=[]
    for t in range(8):
        for sign in (-1,1):images.append(sum((c[s]*sign*(-1)**((s&t).bit_count()%2)<0)<<s for s in range(8)))
    ck(int(classification['mapping'][str(mask)])==min(images))
    ck(sum(x*x for x in walsh(c))==1)
# Every ordered triple has an explicit affine permutation of ALL eight points.
triples=0
for w0,w1,w2 in permutations(range(8),3):
    u=w0^w1;v=w0^w2
    third=next(t for t in range(1,8) if t not in (u,v,u^v))
    image=[w0^ (u if x&1 else 0)^ (v if x&2 else 0)^ (third if x&4 else 0) for x in range(8)]
    ck(len(set(image))==8);ck(image[:3]==[w0,w1,w2]);triples+=1
patterns=[(0,0,0),(15,15,15),(1,1,1),(1,2,4),(1,3,7),(5,10,3),(1,15,6),(7,8,12)]
cases=0
for mask in range(256):
    c=[(-1)**((mask>>s)&1) for s in range(8)];gh=walsh(c);pg=[x*x for x in gh];ig=influence(c)
    for events in patterns:
        h=[c[s]*(1-2*((events[s]>>v)&1)) if s<3 else c[s] for v in range(4) for s in range(8)]
        f=h+[c[s] for v in range(4) for s in range(8)]
        hh=walsh(h);fh=walsh(f);ph=[x*x for x in hh];pf=[x*x for x in fh]
        q=[Q(e.bit_count(),4) for e in events];d=sum(q)/8;delta=sum(x*x for x in q)/8
        b=[sum(Q(c[s]*(-1)**((s&t).bit_count()%2),8)*q[s] for s in range(3)) for t in range(8)]
        ck(sum(x*x for x in b)==delta);ck(influence(f)==(ig+influence(h))/2+d)
        ck(Q(sum(f[x]!=f[x+32] for x in range(32)),32)==d)
        for t in range(8):ck(fh[t]==gh[t]-b[t]);ck(fh[t+32]==-b[t])
        private=sum(ph[8:]);ck(private==4*(d-delta))
        directB={}
        for t in range(32):directB=add((1,directB),(1,L(pf[t])),(1,L(pf[t+32])),(-1,L(pf[t]+pf[t+32])))
        formula={2:2*(d-delta)} if d!=delta else {}
        for t in range(8):
            A=(gh[t]-b[t])**2;B=b[t]**2
            formula=add((1,formula),(1,L(A)),(1,L(B)),(-1,L(A+B)))
        ck(directB==formula)
        # Deliberately non-optimal full private reference, including all off-target atoms.
        rh=ph[:8]+[(ph[t]+private/24)/2 for t in range(8,32)]
        rg=pg;rf=pf[:]
        for t in range(8,32):rf[t]=rf[t+32]=rh[t]/4
        ck(sum(rh)==1);ck(sum(rf)==1)
        HF=entropy(pf);HH=entropy(ph);HG=entropy(pg);CH=ce(ph,rh);CF=ce(pf,rf)
        ck(add((1,CF),(-1,HF))==add((Q(1,2),CH),(-Q(1,2),HH)))
        ck(add((1,CF),(-Q(1,2),CH),(-Q(1,2),HG))==add((1,HF),(-Q(1,2),HH),(-Q(1,2),HG)))
        cases+=1
        if time.perf_counter()-t0>52:raise RuntimeError('52-second cap: incomplete, no PASS')
# Recheck the retained proper-grammar witness directly.
a=[1 if x.bit_count()>=2 else -1 for x in range(32)]
for i in range(5):
    for value in (0,1):
        c=[a[x] for x in range(32) if (x>>i)&1==value]
        ck(all(any(c[x]!=c[x^(1<<j)] for x in range(16)) for j in range(4)))
minors=[]
for bits in range(1,16):
    U=[i for i in range(5) if bits>>i&1];V=[i for i in range(5) if not bits>>i&1]
    def value(x,y):return a[sum(((x>>j)&1)<<i for j,i in enumerate(U))+sum(((y>>j)&1)<<i for j,i in enumerate(V))]
    found=None
    for x,x1 in combinations(range(1<<len(U)),2):
        for y,y1 in combinations(range(1<<len(V)),2):
            det=value(x,y)*value(x1,y1)-value(x,y1)*value(x1,y)
            if det:found=[bits,x,x1,y,y1,det];break
        if found:break
    ck(found is not None);minors.append(found)
out={'status':'PASS','exact_assertions':checks,'Boolean_cases':cases,'ordered_affine_triples':triples,'nonproduct_minors':minors,'seconds':time.perf_counter()-t0,'domain':'all256 phases x8 event triples on2 private bits;6 physical input bits; all ordered shared triples; all10 threshold5 cofactors/15 bipartitions','arithmetic':'Fraction, direct character sums, direct physical edges, exact prime-log coefficient vectors'}
(R/'out'/'FIXTURES.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='nonproduct_minors'}))
