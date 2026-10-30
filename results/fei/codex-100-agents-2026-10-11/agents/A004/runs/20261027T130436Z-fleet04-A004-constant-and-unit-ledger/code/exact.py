"""A004 independent finite-law projections and actual Boolean certificates."""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, sys, hashlib

RUN=Path(__file__).resolve().parents[1]
COUNT=0
def ck(x):
    global COUNT
    COUNT+=1
    assert x
@lru_cache(None)
def factors(n):
    out={};d=2
    while d*d<=n:
        while n%d==0:out[d]=out.get(d,0)+1;n//=d
        d+=1
    if n>1:out[n]=out.get(n,0)+1
    return out
def add(*terms):
    out={}
    for a,v in terms:
        for p,b in v.items():out[p]=out.get(p,F(0))+a*b
    return {p:a for p,a in out.items() if a}
def logq(q):
    q=F(q);assert q>0
    return add((1,factors(q.numerator)),(-1,factors(q.denominator)))
def CE(p,q):
    return add(*[(-a,logq(b)) for a,b in zip(p,q) if a])
def KL(p,q):return add((1,CE(p,q)),(-1,CE(p,p)))
def lnunit(x):
    z=(x-1)/(x+1);v=sum((2*z**(2*j+1)/F(2*j+1) for j in range(36)),F(0))
    return v,v+2*z**73/(73*(1-z*z))
LN2=lnunit(F(2))
@lru_cache(None)
def lb(p):
    k=p.bit_length()-1;a,b=lnunit(F(p,1<<k))
    return k+a/LN2[1],k+b/LN2[0]
def bounds(v):
    lo=hi=F(0)
    for p,a in v.items():
        l,h=lb(p);lo+=a*(l if a>=0 else h);hi+=a*(h if a>=0 else l)
    return lo,hi
def record(v):
    lo,hi=bounds(v)
    return {'prime_logs':{str(p):str(a) for p,a in sorted(v.items())},'lower':str(lo),'upper':str(hi),'display_only':float((lo+hi)/2)}
