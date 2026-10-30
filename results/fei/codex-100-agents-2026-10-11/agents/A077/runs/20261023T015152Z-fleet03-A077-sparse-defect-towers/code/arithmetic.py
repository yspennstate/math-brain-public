"""A076 shifted-row v1: independently enumerated spectra and adaptive trees."""
from fractions import Fraction as F
from collections import defaultdict
from functools import lru_cache
from pathlib import Path
import json, time
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def eq(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1
def plus(*pairs):
    out=defaultdict(F)
    for expr,w in pairs:
        for x,c in expr.items(): out[x]+=w*c
    return {x:c for x,c in out.items() if c and x!=1}
def phi(p): return {} if not p else {1/p:p}
def Phi(p,q): return plus((phi(p),F(1)),(phi(q),F(1)),(phi(p+q),F(-1)))
@lru_cache(None)
def coeff(t):
    v=list(t); h=1
    while h<len(v):
        for k in range(0,len(v),2*h):
            for j in range(k,k+h): v[j],v[j+h]=v[j]+v[j+h],v[j]-v[j+h]
        h*=2
    return tuple(F(a,len(v)) for a in v)
def H(t): return plus(*[(phi(a*a),F(1)) for a in coeff(t)])
def I(t): return sum((s.bit_count()*a*a for s,a in enumerate(coeff(t))),F(0))
def inf(t,i): return sum((a*a for s,a in enumerate(coeff(t)) if s>>i&1),F(0))
def B(t,i):
    c=coeff(t)
    return plus(*[(Phi(c[s]**2,c[s|(1<<i)]**2),F(1)) for s in range(len(c)) if not s>>i&1])
def child(t,i,bit):
    return tuple(t[(z&((1<<i)-1))+((z>>i)<<(i+1))+(bit<<i)] for z in range(len(t)//2))
def wrap(t,orientation):
    return tuple((1 if x==0 else t[z]) if orientation=='OR' else (t[z] if x==0 else -1)
                 for z in range(len(t)) for x in range(2))
def D(mu,a):
    return plus((Phi((1+mu)**2,a*a),F(1,4)),(Phi((1-mu)**2,a*a),F(1,4)),(Phi(mu*mu,a*a),F(-1,2)))
def R(mu):
    # constant represented as log2(2)
    return plus(({F(2):1-mu*mu},F(1)),(phi((1+mu)**2/4),F(1)),
                (phi((1-mu)**2/4),F(1)),(phi(mu*mu),F(-1,2)))
TERMS=24; SCALE=1<<70
def lnseries(x):
    z=(x-1)/(x+1)
    low=sum((2*z**(2*k+1)/F(2*k+1) for k in range(TERMS)),F(0))
    return low,low+2*z**(2*TERMS+1)/((2*TERMS+1)*(1-z*z))
LN2=lnseries(F(2))
@lru_cache(None)
def logbounds(x):
    if x==1:return F(0),F(0)
    k=x.numerator.bit_length()-x.denominator.bit_length();y=x/F(2)**k
    while y<1:k-=1;y*=2
    while y>2:k+=1;y/=2
    lo,hi=lnseries(y)
    lo+=k*LN2[0 if k>=0 else 1];hi+=k*LN2[1 if k>=0 else 0]
    corners=[a/b for a in (lo,hi) for b in LN2];lo=min(corners);hi=max(corners)
    return F((lo.numerator*SCALE)//lo.denominator,SCALE),F(-((-hi.numerator*SCALE)//hi.denominator),SCALE)
def bounds(e):
    lo=hi=F(0)
    for x,c in e.items():
        a,b=logbounds(x);lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return lo,hi
def equal_expr(e):
    # Exact rational prime-exponent identity, avoiding huge rational powers.
    total=defaultdict(F)
    for x,c in e.items():
        for p,k in factors(x.numerator):total[p]+=k*c
        for p,k in factors(x.denominator):total[p]-=k*c
    eq(all(v==0 for v in total.values()),True)
@lru_cache(None)
def factors(n):
    out=[];p=2
    while p*p<=n:
        k=0
        while n%p==0:n//=p;k+=1
        if k:out.append((p,k))
        p=3 if p==2 else p+2
    if n>1:out.append((n,1))
    return tuple(out)
def leq(e,rhs):
    global checks
    if not e:eq(F(0)<=rhs,True);return
    lo,hi=bounds(e)
    if hi<=rhs:checks+=1;return
    if lo<=rhs<=hi:
        equal_expr(plus((e,F(1)),({F(2):rhs},F(-1))))
        return
    raise AssertionError(('inequality',e,rhs,lo,hi))

# Exact enclosure memoization for the many repeated node ledgers.
_uncached_bounds=bounds
@lru_cache(maxsize=8192)
def _cached_bounds(items):return _uncached_bounds(dict(items))
def bounds(e):return _cached_bounds(tuple(sorted(e.items())))
