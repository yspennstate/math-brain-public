"""Exact arithmetic; reconstructed from prior A022/A021 finite helpers."""
from fractions import Fraction as Q
from functools import lru_cache
from collections import Counter
@lru_cache(None)
def factors(n):
    d={}; p=2
    while p*p<=n:
        while n%p==0: d[p]=d.get(p,0)+1; n//=p
        p+=1
    if n>1: d[n]=d.get(n,0)+1
    return d
def plus(*terms):
    out={}
    for a in terms:
        for p,c in a.items(): out[p]=out.get(p,Q(0))+c
    return {p:c for p,c in out.items() if c}
def mul(a,c): return {p:v*c for p,v in a.items() if v*c}
def const(c): return {2:Q(c)} if c else {}
@lru_cache(None)
def lg(x):
    x=Q(x); assert x>0
    return plus(factors(x.numerator),mul(factors(x.denominator),-1))
@lru_cache(None)
def phi(x): return mul(lg(x),-x) if x else {}
def entropy(ps):
    return plus(*(mul(phi(p),n) for p,n in Counter(ps).items() if p))
def ce(ps,qs):
    grouped={}
    for p,q in zip(ps,qs):
        if p:
            assert q>0
            grouped[q]=grouped.get(q,Q(0))+p
    return plus(*(mul(lg(q),-p) for q,p in grouped.items()))
@lru_cache(None)
def log_interval(p):
    k=p.bit_length()-1; y=Q(p,2**k)
    def ln(x):
        z=(x-1)/(x+1); term=z; ans=Q(0)
        for j in range(40): ans+=2*term/(2*j+1); term*=z*z
        return ans,ans+2*term/(81*(1-z*z))
    lo,hi=ln(y); a,b=ln(Q(2))
    return k+lo/b,k+hi/a
def bounds(a):
    lo=hi=Q(0)
    for p,c in a.items():
        a,b=log_interval(p)
        if c<0: a,b=b,a
        lo+=c*a; hi+=c*b
    return lo,hi
def fwht(f):
    a=list(f); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for i in range(j,j+h): u,v=a[i],a[i+h]; a[i],a[i+h]=u+v,u-v
        h*=2
    return a
def spectrum(f):
    n=len(f); return [Q(v*v,n*n) for v in fwht(f)]
def restrict(f,i,b): return [v for j,v in enumerate(f) if (j>>i)&1==b]
def inf(f,i): return Q(sum(f[x]!=f[x^(1<<i)] for x in range(len(f))),len(f))
def g(x): return -1 if x==0 else 1
