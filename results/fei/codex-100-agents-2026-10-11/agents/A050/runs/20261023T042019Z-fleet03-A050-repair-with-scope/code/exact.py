"""A050 active-label v1. Log-vector primitives independently copied from own stage2.
Every joint is rebuilt from exact coherent kernels, not from reported MI formulas.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
from collections import defaultdict
import time,json,sys
ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter(); COUNT=0; CASES=0
PILOT='--pilot' in sys.argv
LIMIT=60 if PILOT else 300
def ck(ok):
    global COUNT
    assert ok
    COUNT+=1
    if time.perf_counter()-START>LIMIT:raise RuntimeError('frozen watchdog')
@lru_cache(None)
def factor(n):
    d={};i=2
    # A residual integer is a valid logarithm atom; primality is unnecessary.
    # Do not spend shared-machine time factoring large marginal numerators.
    while i*i<=n and i<=97:
        while n%i==0:d[i]=d.get(i,0)+1;n//=i
        i+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def ent(ps):
    out={}
    for p in ps:
        if not p:continue
        for n,s in [(p.numerator,-1),(p.denominator,1)]:
            for prime,k in factor(n).items():out[prime]=out.get(prime,F(0))+s*p*k
    return {p:v for p,v in out.items() if v}
def add(*vs):
    d={}
    for v in vs:
        for p,x in v.items():d[p]=d.get(p,F(0))+x
    return {p:x for p,x in d.items() if x}
def scale(v,a):return {p:a*x for p,x in v.items() if a*x}
@lru_cache(None)
def ln(x):
    z=(x-1)/(x+1)
    lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(32)),F(0))
    return lo,lo+2*z**65/(65*(1-z*z))
LN2=ln(F(2))
@lru_cache(None)
def log(x):
    x=F(x);k=0
    while x<1:x*=2;k-=1
    while x>=2:x/=2;k+=1
    lo,hi=ln(x);v=[a/b for a in (lo,hi) for b in LN2]
    grid=1<<256
    lo=(min(v)+k)*grid;hi=(max(v)+k)*grid
    return F(lo.numerator//lo.denominator,grid),F(-((-hi).numerator//(-hi).denominator),grid)
def bounds(v):
    lo=hi=F(0)
    for p,x in v.items():
        a,b=log(p)
        if x<0:a,b=b,a
        lo+=x*a;hi+=x*b
    return lo,hi
def nonneg(v):ck(not v or bounds(v)[0]>=0)
def serial(v):return {str(p):str(x) for p,x in v.items()}

LIMIT=60 if PILOT else 120

def logvec(x):
    out={}
    for n,sgn in [(x.numerator,1),(x.denominator,-1)]:
        for p,k in factor(n).items():out[p]=out.get(p,F(0))+sgn*k
    return {p:v for p,v in out.items() if v}
def kl(p,q):
    out={}
    for s,w in p.items():
        if w:
            ck(q.get(s,F(0))>0)
            out=add(out,scale(logvec(w/q[s]),w))
    return out
def marginal(p,mask):
    out={}
    for s,w in p.items():out[s&mask]=out.get(s&mask,F(0))+w
    return out
def spec(t,coords):
    a=list(t);step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(j,j+step):x,y=a[k],a[k+step];a[k],a[k+step]=x+y,x-y
        step*=2
    p={sum(1<<i for j,i in enumerate(coords) if s>>j&1):F(v*v,len(a)**2) for s,v in enumerate(a) if v}
    ck(sum(p.values())==1)
    inf={i:sum((w for s,w in p.items() if s>>i&1),F(0)) for i in coords}
    for j,i in enumerate(coords):
        flips=sum(t[x]!=t[x|(1<<j)] for x in range(len(t)) if not(x>>j&1))
        ck(inf[i]==F(flips,len(t)//2))
    return p,inf
def restrict(t,j,b):
    return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(b<<j)] for x in range(len(t)//2))

