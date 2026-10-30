import json, time
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
from functools import lru_cache

ROOT = Path(__file__).resolve().parents[1]
START = time.perf_counter()
ASSERTIONS = 0
CASES = Counter()

def check(ok):
    global ASSERTIONS
    ASSERTIONS += 1
    assert ok, ASSERTIONS
    if time.perf_counter()-START > 60:
        raise RuntimeError('Frozen runtime limit exceeded')

def walsh(values):
    a = list(values)
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2*h):
            for i in range(j, j+h):
                u,v = a[i],a[i+h]
                a[i],a[i+h] = u+v,u-v
        h *= 2
    return a

def parity(v):
    return -1 if v.bit_count()%2 else 1

@lru_cache(None)
def factors(n):
    ans = {}
    d=2
    while d*d <= n:
        while n%d == 0:
            ans[d]=ans.get(d,0)+1
            n//=d
        d+=1
    if n>1: ans[n]=ans.get(n,0)+1
    return ans

def add(a,b,weight=Q(1)):
    out=Counter(a)
    for p,v in b.items(): out[p]+=weight*v
    return {p:v for p,v in out.items() if v}

def entropy(ps):
    ans={}
    for p in ps:
        if not p: continue
        for prime,v in factors(p.denominator).items(): ans[prime]=ans.get(prime,Q(0))+p*v
        for prime,v in factors(p.numerator).items(): ans[prime]=ans.get(prime,Q(0))-p*v
    return {p:v for p,v in ans.items() if v}

def influence(w):
    return Q(sum(v*v*i.bit_count() for i,v in enumerate(w)),len(w)**2)

def verify(k,m,rows,group,seed=None):
    # rows[b][x]; physical indexing x + 2^k*a + 2^(k+m)*b.
    nx,nb=1<<k,1<<m
    rw=[walsh(row) for row in rows]
    values=[rows[b][x]*parity(a&b) for b in range(nb) for a in range(nb) for x in range(nx)]
    fw=walsh(values); den=len(values)**2
    px=[Q(0)]*nx; py=[Q(0)]*(nb*nb)
    ix=iy=Q(0)
    for t in range(nb):
        for s in range(nb):
            for v in range(nx):
                index=v+nx*s+nx*nb*t
                check(fw[index]==nb*parity(s&t)*rw[s][v])
                p=Q(fw[index]**2,den)
                px[v]+=p;py[s+nb*t]+=p
                ix+=p*v.bit_count();iy+=p*(s.bit_count()+t.bit_count())
    check(sum(px)==1)
    check(all(p==Q(1,nb*nb) for p in py))
    check(iy==m)
    check(ix==sum((influence(w) for w in rw),Q(0))/nb)
    bcost={}
    for w in rw:
        bcost=add(bcost,entropy([Q(v*v,nx*nx) for v in w]),Q(1,nb))
    hj=entropy([Q(w*w,den) for w in fw])
    check(hj==add({2:Q(2*m)},bcost))
    cond=add(hj,entropy(px),Q(-1))
    # Exact formal logarithm identity, retaining mutual information.
    mutual=add(entropy(px),bcost,Q(-1))
    check(cond==add({2:Q(2*m)},mutual,Q(-1)))
    for u in range(nx):
        branch=[parity(a&b)*rows[b][u] for b in range(nb) for a in range(nb)]
        bw=walsh(branch)
        check(all(abs(w)==nb for w in bw))
    if group=='linear':
        check(entropy(px)=={2:Q(k)})
        check(cond=={2:Q(2*m-k)})
        check(ix==Q(k,2))
    if seed is not None:
        sw=walsh(seed);eps=Q(4,nb)
        check(px==[(1-eps)*Q(w*w,nx*nx)+eps/Q(nx) for w in sw])
        check(ix==influence(sw)+Q(2,nb)*(k-2*influence(sw)))
        branch_signatures=[tuple(rows[b][u] for b in range(nb)) for u in range(nx)]
        check(len(set(branch_signatures))==nx)
        expected=add(entropy([Q(w*w,nx*nx) for w in sw]),{},Q(1))
        expected={p:(1-Q(nx,nb))*v for p,v in expected.items()}
        for u in range(nx):
            flipped=seed.copy();flipped[u]*=-1
            expected=add(expected,entropy([Q(w*w,nx*nx) for w in walsh(flipped)]),Q(1,nb))
        check(bcost=={p:v for p,v in expected.items() if v})
        # Independent physical edge calculation, no Fourier influence formula.
        edge_ix=sum(values[z]!=values[z^(1<<i)] for z in range(len(values)) for i in range(k))
        check(ix==Q(edge_ix,len(values)))
    CASES[group]+=1

def receipt():
    out={'status':'PASS','cases':dict(CASES),'total_cases':sum(CASES.values()),'assertions':ASSERTIONS,'runtime_seconds':time.perf_counter()-START,'arithmetic':'integer signed Walsh; Fraction; exact prime-log entropy expressions','independent_review':False}
    (ROOT/'out'/'validation.json').write_text(json.dumps(out,indent=2)+'\n')
    return out

for k,m in [(1,1),(2,1)]:
    for mask in range(1<<(k and ((1<<k)*(1<<m)))):
        rows=[[parity((mask>>(x+(1<<k)*b))&1) for x in range(1<<k)] for b in range(1<<m)]
        verify(k,m,rows,'exhaustive_phase')
receipt()
for j in range(16):
    rows=[[parity((j*x + (j+1)*b + x*b + (x^b)).bit_count()) for x in range(4)] for b in range(4)]
    verify(2,2,rows,'deterministic_phase')
receipt()
for k in range(1,4):
    nx=1<<k
    masks=list(range(1<<nx)) if k<3 else [0,1,3,15,85,105,127,255]
    for m in [k+1,k+2]:
        for mask in masks:
            seed=[parity((mask>>x)&1) for x in range(nx)]
            rows=[[seed[x]*(-1 if b==x else 1) for x in range(nx)] for b in range(1<<m)]
            verify(k,m,rows,'rare_tag',seed)
    receipt()
for k in range(1,4):
    for m in [k,k+1]:
        rows=[[parity(x&b) for x in range(1<<k)] for b in range(1<<m)]
        verify(k,m,rows,'linear')
print(json.dumps(receipt(),indent=2))
