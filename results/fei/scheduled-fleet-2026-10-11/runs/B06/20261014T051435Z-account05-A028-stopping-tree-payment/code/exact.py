"""Frozen arbitrary-controller certificate; all entropy signs use rational intervals."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from math import prod
import json, time, sys

ROOT=Path(__file__).resolve().parents[1]
MODE=sys.argv[1] if len(sys.argv)>1 else 'pilot'
assert MODE in ('pilot','full')
START=time.monotonic()
checks=0

def check(condition):
    global checks
    assert condition
    checks+=1

@lru_cache(None)
def factors(n):
    out={}
    q=2
    while q*q<=n:
        while n%q==0:
            out[q]=out.get(q,0)+1
            n//=q
        q+=1
    if n>1: out[n]=out.get(n,0)+1
    return tuple(out.items())

def add(*terms):
    out={}
    for term in terms:
        for k,v in term.items(): out[k]=out.get(k,F(0))+v
    return {k:v for k,v in out.items() if v}

def scale(term,q):
    return {k:v*q for k,v in term.items() if v*q}

def lg(q):
    q=F(q)
    assert q>0
    return add(dict((k,F(v)) for k,v in factors(q.numerator)),
               dict((k,F(-v)) for k,v in factors(q.denominator)))

def eta(q): return scale(lg(q),-q) if q else {}
def phi(t): return eta((1-2*t)**2)
def entropy(ps): return add(*(eta(q) for q in ps))

def ln_unit(q):
    # q in [1,2]; z<=1/3. Positive atanh series, rigorous tail.
    z=(q-1)/(q+1)
    total=F(0)
    power=z
    for j in range(24):
        total+=2*power/(2*j+1)
        power*=z*z
    tail=2*power/(49*(1-z*z))
    return total,total+tail

L2=ln_unit(F(2))
@lru_cache(None)
def log_prime(k):
    if k==2: return F(1),F(1)
    exponent=k.bit_length()-1
    lo,hi=ln_unit(F(k,1<<exponent))
    lower,upper=F(exponent)+lo/L2[1], F(exponent)+hi/L2[0]
    denominator=1<<48
    lower_scaled,upper_scaled=lower*denominator,upper*denominator
    low=lower_scaled.numerator//lower_scaled.denominator
    high=-((-upper_scaled.numerator)//upper_scaled.denominator)
    return F(low,denominator),F(high,denominator)

@lru_cache(None)
def cached_enclosure(items):
    lo=hi=F(0)
    for k,c in items:
        a,b=log_prime(k)
        lo+=c*(a if c>=0 else b)
        hi+=c*(b if c>=0 else a)
    return lo,hi

def enclosure(term): return cached_enclosure(tuple(sorted(term.items())))

@lru_cache(None)
def walsh(table):
    a=list(table)
    step=1
    while step<len(a):
        for base in range(0,len(a),2*step):
            for j in range(base,base+step):
                x,y=a[j],a[j+step]
                a[j],a[j+step]=x+y,x-y
        step*=2
    return tuple(a)

@lru_cache(None)
def stats(table):
    N=len(table)
    ps=tuple(F(a*a,N*N) for a in walsh(table))
    Hp=entropy(ps[1:])
    return ps,Hp,add(Hp,eta(ps[0])),sum((s.bit_count()*q for s,q in enumerate(ps)),F(0))

def edges(table,indices):
    return sum((F(sum(table[x]!=table[x^(1<<i)] for x in range(len(table))),len(table))
                for i in indices),F(0))

def tables(maxdim):
    for n in range(maxdim+1):
        for code in range(1<<(1<<n)):
            yield n,code,tuple(-1 if code>>x&1 else 1 for x in range(1<<n))

@lru_cache(None)
def tree(table,controls):
    if controls==0: return {},F(0)
    half=len(table)//2
    left,right=table[:half],table[half:]
    H=stats(table)[2]
    D=add(H,scale(add(stats(left)[2],stats(right)[2]),F(-1,2)))
    d=F(sum(x!=y for x,y in zip(left,right)),half)
    A,ai=tree(left,controls-1)
    B,bi=tree(right,controls-1)
    return add(D,scale(add(A,B),F(1,2))),d+(ai+bi)/2

