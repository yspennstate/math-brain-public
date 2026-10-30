from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json, time, sys, hashlib

ROOT=Path(__file__).resolve().parents[1]
checks=0
def ck(b):
    global checks
    checks+=1
    assert b, checks

# For m in [1,2], z=(m-1)/(m+1) lies in [0,1/3].
# ln(m)=2 sum z^(2i+1)/(2i+1); tail <=9/[4(2N+1)3^(2N+1)].
# Each truncated summand is rounded DOWN at scale 2^112.
SCALE=1<<112
N=44
def ln_unit(m):
    z=(m-1)/(m+1);a,b=z.numerator,z.denominator
    total=sum((2*pow(a,2*i+1)*SCALE)//(pow(b,2*i+1)*(2*i+1)) for i in range(N))
    tail=F(9,4*(2*N+1)*3**(2*N+1))
    return F(total,SCALE),F(total+N,SCALE)+tail
L2=ln_unit(F(2))
@lru_cache(None)
def lg(x):
    x=F(x);assert x>0
    k=x.numerator.bit_length()-x.denominator.bit_length()
    power=F(2)**k
    if x<power:k-=1;power/=2
    m=x/power
    assert 1<=m<2
    # First enclose the mantissa by dyadics; do not run a long series
    # on an exponentially long reset denominator.
    D=1<<100
    v=(m.numerator*D)//m.denominator
    lo=ln_unit(F(v,D))[0]; hi=ln_unit(F(v+1,D))[1]
    return lo/L2[1]+k,hi/L2[0]+k
def add(a,b):return a[0]+b[0],a[1]+b[1]
def sub(a,b):return a[0]-b[1],a[1]-b[0]
def mul(c,a):
    return (c*a[0],c*a[1]) if c>=0 else (c*a[1],c*a[0])
def ce(p,q):
    ans=(F(0),F(0))
    for x,y in zip(p,q):
        if x:ans=add(ans,mul(-x,lg(y)))
    return ans
def ent(p):return ce(p,p)
def pretty(a):return [str(a[0]),str(a[1])]

def spectrum(vals):
    # Direct character sums, deliberately not the peer's FWHT path.
    size=len(vals)
    w=[sum(v*(-1 if (s&x).bit_count()%2 else 1) for x,v in enumerate(vals)) for s in range(size)]
    return [F(x,size) for x in w]
def edges(vals):
    dim=len(vals).bit_length()-1
    return [F(sum(vals[x]!=vals[x^(1<<j)] for x in range(len(vals))),len(vals)) for j in range(dim)]
def ib(p):return sum(F(s.bit_count())*v for s,v in enumerate(p))
def h2(x):return ent([x,1-x])

