"""No import of main checker/helper. Direct characters and independent KL expansion."""
from fractions import Fraction as Q
from pathlib import Path
from functools import lru_cache
from collections import defaultdict
import json,time
ROOT=Path(__file__).resolve().parents[1]; START=time.monotonic(); checks=nodes=leaves=0

def ck(v):
    global checks
    assert v;checks+=1

def add(*terms):
    z=defaultdict(Q)
    for term in terms:
        for k,v in term.items(): z[k]+=v
    return {k:v for k,v in z.items() if v}

def mul(term,c): return {k:v*c for k,v in term.items() if v*c}
def difference(a,b): return add(a,mul(b,-1))
def mean(a,b): return mul(add(a,b),Q(1,2))

@lru_cache(None)
def log(q):
    result=defaultdict(Q)
    for N,sgn in [(q.numerator,1),(q.denominator,-1)]:
        d=2
        while d*d<=N:
            while N%d==0:result[d]+=sgn;N//=d
            d+=1
        if N>1:result[N]+=sgn
    return dict(result)

def D(p,r):
    ck(sum(p)==sum(r)==1)
    return add(*(mul(log(x/y),x) for x,y in zip(p,r) if x))

def H(p): return add(*(mul(log(x),-x) for x in p if x))

@lru_cache(None)
def coefficients(t):
    return tuple(sum(((-1)**((s&x).bit_count())*v for x,v in enumerate(t)),Q())/len(t) for s in range(len(t)))

def law(t):return tuple(x*x for x in coefficients(t))

def ids(n,i,b):
    return [x for x in range(n) if ((x>>i)&1)==b]

def child(t,i,b): return tuple(t[x] for x in ids(len(t),i,b))

def joint(t,r,i):
    aa=coefficients(t); js=[[],[]]
    lo=ids(len(t),i,0)
    for s in lo:
        u,v=aa[s],aa[s|(1<<i)]
        mass=r[s]+r[s|(1<<i)]
        for b in [0,1]:
            prob=(u+(-1)**b*v)**2/(2*(u*u+v*v)) if u or v else Q(1,2)
            js[b].append(mass*prob)
    branch=[sum(row) for row in js]
    ck(sum(branch)==1 and min(branch)>0)
    rr=[tuple(x/branch[b] for x in js[b]) for b in [0,1]]
    Er={}
    # Independent conditional decomposition of the erasure KL.
    pp=law(t)
    for s in lo:
        sp=pp[s]+pp[s|(1<<i)];sr=r[s]+r[s|(1<<i)]
        if sp:
            Er=add(Er,mul(D((pp[s]/sp,pp[s|(1<<i)]/sp),(r[s]/sr,r[s|(1<<i)]/sr)),sp))
    O=D((Q(1,2),Q(1,2)),tuple(branch))
    ck(not difference(D(pp,r),add(Er,O,mean(*(D(law(child(t,i,b)),rr[b]) for b in [0,1])))))
    return rr,Er,O
