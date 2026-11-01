"""Direct character sums on every partial assignment of the seven-bit fixture."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from functools import lru_cache
import time,json
RUN=Path(__file__).resolve().parent.parent
START=time.monotonic(); checks=0
def ck(v):
    global checks
    checks+=1; assert v; assert time.monotonic()-START<55
def add(*terms):
    r={}
    for t in terms:
        for k,v in t.items(): r[k]=r.get(k,Q(0))+v
    return {k:v for k,v in r.items() if v}
def scale(t,a): return {k:v*a for k,v in t.items() if v*a}
def log(q):
    r={}
    for n,sgn in [(q.numerator,1),(q.denominator,-1)]:
        d=2
        while n>1:
            while n%d==0: r[d]=r.get(d,0)+sgn; n//=d
            d+=1
    return {k:Q(v) for k,v in r.items() if v}
def eta(q): return scale(log(q),-q) if q else {}
def ent(xs): return add(*(eta(x) for x in xs))
@lru_cache(None)
def coeff(t):
    return tuple(Q(sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(t)),len(t)) for s in range(len(t)))
def subtable(t,assignment):
    free=[i for i,z in enumerate(assignment) if z==-1]
    fixed=sum(z<<i for i,z in enumerate(assignment) if z!=-1)
    return tuple(t[fixed+sum(((x>>j)&1)<<i for j,i in enumerate(free))] for x in range(1<<len(free)))
a0=tuple(-1 if x in (0,1,2) else 1 for x in range(8))
g0=tuple((-1 if (x&7)==0 else 1)*(-1 if x&8 else 1) for x in range(16))
h0=tuple((-1 if (x&7).bit_count()<=1 else 1)*(-1 if x&8 else 1) for x in range(16))
states=0
for ass in product((-1,0,1),repeat=7):
    a=subtable(a0,ass[:3]); g=subtable(g0,ass[3:]); h=subtable(h0,ass[3:])
    f=tuple(g[x] if z==1 else h[x] for z in a for x in range(len(g)))
    aa,gg,hh,ff=map(coeff,(a,g,h,f))
    p=Q(a.count(-1),len(a)); V=4*p*(1-p)
    gamma=Q(sum(x!=y for x,y in zip(g,h)),len(g))
    q=tuple((1-p)*x*x+p*y*y for x,y in zip(gg,hh))
    w=tuple(V*(x-y)**2/4 for x,y in zip(gg,hh))
    ck(sum(q)==1);ck(sum(w)==V*gamma)
    for i,(qi,wi) in enumerate(zip(q,w)):
        ck(sum(ff[s*len(g)+i]**2 for s in range(len(a)))==qi)
        ck(sum(ff[s*len(g)+i]**2 for s in range(1,len(a)))==wi)
    B=add(*(add(eta(wi),eta(qi-wi),scale(eta(qi),-1)) for qi,wi in zip(q,w)))
    HA=ent(tuple(z*z/V for z in aa[1:])) if V else {}
    sector=add(ent(q),B,scale(HA,V*gamma))
    ck(add(ent(tuple(z*z for z in ff)),scale(sector,-1))=={})
    # Product and direct physical edge influence normalization are checked separately.
    n=len(f).bit_length()-1
    edge=sum(Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f)) for i in range(n))
    fourier=sum(Q(s.bit_count())*z*z for s,z in enumerate(ff))
    ck(edge==fourier)
    states+=1
out={'status':'PASS','partial_assignments':states,'exact_assertions':checks,'seconds':time.monotonic()-START,
     'method':'direct character sums; rational spectra; independent prime-log equality; all ternary partial assignments, no quotient'}
(RUN/'out/independent.json').write_text(json.dumps(out,indent=2),encoding='utf-8',newline='\n')
print(json.dumps(out))
