"""Frozen A044-two-mean-v2. Fractions, formal logs and proved log intervals."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
from functools import lru_cache
from math import isqrt
import time,json
ROOT=Path(__file__).resolve().parents[1]
start=time.perf_counter(); checks=0
def check(x):
    global checks
    checks+=1
    assert x
def prod(xs):
    z=Q(1)
    for x in xs:z*=x
    return z
@lru_cache(None)
def factors(n):
    if n==1:return {}
    sq=isqrt(n)
    if sq*sq==n:return {p:2*k for p,k in factors(sq).items()}
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        sq=isqrt(n)
        if n>1 and sq*sq==n:
            for k,v in factors(sq).items():d[k]=d.get(k,0)+2*v
            return d
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return d
def addlog(d,c,x):
    check(x>0)
    for n,s in [(x.numerator,1),(x.denominator,-1)]:
        for p,k in factors(n).items():d[p]=d.get(p,Q(0))+c*s*k
def combine(*parts):
    d={}
    for c,x in parts:
        for p,k in x.items():d[p]=d.get(p,Q(0))+c*k
    return {p:c for p,c in d.items() if c}
def lnat(x):
    z=(x-1)/(x+1);N=32
    lo=2*sum((z**(2*k+1)/Q(2*k+1) for k in range(N)),Q(0))
    return lo,lo+2*z**(2*N+1)/(Q(2*N+1)*(1-z*z))
LN2=lnat(Q(2))
@lru_cache(None)
def lnprime(p):
    k=p.bit_length()-1; l,u=lnat(Q(p,2**k))
    return l+k*LN2[0],u+k*LN2[1]
def interval(d,c=Q(0)):
    lo=hi=c
    for p,a in d.items():
        l,u=lnprime(p);lo+=a*(l if a>=0 else u);hi+=a*(u if a>=0 else l)
    return lo,hi
def ent(P,biases):
    d={}
    for mask,p in enumerate(P):
        if mask and p:
            sigma=prod(4*q*(1-q) for i,q in enumerate(biases) if mask>>i&1)
            addlog(d,p,sigma/p)
    return combine((Q(1),d))
def spectrum(values,biases):
    n=len(biases);rows=[]
    for x,f in values.items():rows.append((x,f,prod(q if b else 1-q for q,b in zip(biases,x))))
    P=[]
    for mask in range(2**n):
        S=[i for i in range(n) if mask>>i&1]
        numerator=sum((w*f*prod(Q(x[i])-biases[i] for i in S) for x,f,w in rows),Q(0))
        P.append(numerator**2/prod(biases[i]*(1-biases[i]) for i in S))
    check(sum(P)==sum((w*f*f for x,f,w in rows),Q(0)))
    return P
def delta(P):return sum(((mask.bit_count()-1)*p for mask,p in enumerate(P) if mask),Q(0))
def pivotal_check(P,values,biases):
    for i,q in enumerate(biases):
        pivotal=sum((prod(b if xj else 1-b for xj,b in zip(x,biases)) for x,f in values.items() if f!=values[x[:i]+(1-x[i],)+x[i+1:]]),Q(0))
        check(sum((p for mask,p in enumerate(P) if mask>>i&1),Q(0))==4*q*(1-q)*pivotal)
def ell(d,c,r):
    addlog(d,2*c*(1-r),Q(2));addlog(d,-2*c*r,r)
