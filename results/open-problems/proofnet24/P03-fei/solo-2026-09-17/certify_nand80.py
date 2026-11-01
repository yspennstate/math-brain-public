#!/usr/bin/env python3
"""Exact rational interval certificate: an 80-variable Boolean f has B(f)/I(f)>4.007.

No floating-point value is used in any assertion. Logarithms are enclosed by
an atanh series with an explicit rational remainder; each interval operation
rounds outwards to a binary rational grid. This is a self-check, not an audit.
"""
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
import json

BITS=160
GRID=1 << BITS
TERMS=64


def floor_grid(x):return F((x.numerator*GRID)//x.denominator,GRID)
def ceil_grid(x):return -floor_grid(-x)


class IV:
    def __init__(self,lo,hi=None):
        lo=F(lo); hi=lo if hi is None else F(hi)
        assert lo<=hi
        self.lo=floor_grid(lo); self.hi=ceil_grid(hi)
    def __add__(self,other):
        other=other if isinstance(other,IV) else IV(other)
        return IV(self.lo+other.lo,self.hi+other.hi)
    __radd__=__add__
    def __neg__(self):return IV(-self.hi,-self.lo)
    def __sub__(self,other):return self+-other if isinstance(other,IV) else self+IV(-other)
    def __mul__(self,c):
        c=F(c)
        return IV(self.lo*c,self.hi*c) if c>=0 else IV(self.hi*c,self.lo*c)
    __rmul__=__mul__


def log_series(y):
    assert 1<=y<=2
    t=(y-1)/(y+1); t2=t*t
    power=t; lo=F(0)
    for j in range(TERMS):
        lo+=2*power/(2*j+1)
        power*=t2
    remainder=2*power/((2*TERMS+1)*(1-t2))
    return lo,lo+remainder


LN2_LO,LN2_HI=log_series(F(2))


@lru_cache(None)
def h(x):
    x=F(x)
    assert x>=0
    if x==0:return IV(0)
    k=x.numerator.bit_length()-x.denominator.bit_length()
    scale=F(2**k) if k>=0 else F(1,2**(-k))
    y=x/scale
    if y<1:k-=1;y*=2
    if y>=2:k+=1;y/=2
    assert 1<=y<2
    lo,hi=log_series(y)
    loglo=k+lo/LN2_HI
    loghi=k+hi/LN2_LO
    return IV(-x*loghi,-x*loglo)


def edge(r,s):return h(r)+h(s)-h(r+s)


def wht(a):
    a=list(a); step=1
    while step<len(a):
        for j in range(0,len(a),2*step):
            for k in range(step):
                u,v=a[j+k],a[j+k+step]
                a[j+k],a[j+k+step]=u+v,u-v
        step*=2
    return a


def initial_state():
    n=5; N=1<<n; a=[int(x<21) for x in range(N)]
    w=wht(a); c=[F(x,N) for x in w]
    assert sum(x*x for x in w)==N*sum(a)
    B=IV(0)
    for i in range(n):
        B+=sum((edge(c[s]**2,c[s+(1<<i)]**2) for s in range(N) if not(s&(1<<i))),IV(0))
    return F(21,32),[c[1<<i] for i in range(n)],B,1,n


def nand(state):
    alpha,t,B,mult,n=state
    p=alpha*alpha; nt=[-alpha*x for x in t]
    correction=sum((edge((1-p)**2,x*x)-edge(p*p,x*x) for x in nt),IV(0))
    return 1-p,nt,2*alpha*B+2*mult*correction,2*mult,2*n


def metrics(state):
    alpha,t,B,mult,n=state
    out=4*B+mult*sum((edge((1-2*alpha)**2,4*x*x)-4*edge(alpha**2,x*x) for x in t),IV(0))
    influence=2*mult*sum(abs(x) for x in t)
    return out,influence,n


def rational_interval(iv):return {'lower':str(iv.lo),'upper':str(iv.hi)}


def main():
    state=initial_state()
    for _ in range(4):state=nand(state)
    B,I,n=metrics(state)
    assert n==80 and I>0
    ratio=B*F(1,I)
    gap=B-4*I
    assert ratio.lo>F(4007,1000)
    assert ratio.hi<F(4008,1000)
    assert gap.lo>0
    result={'status':'PASS','claim':'4.007 < B(f)/I(f) < 4.008; hence B <= 4 I is false',
            'function':'A0(x)=1{x<21} on five input bits; A_{d+1}=1-A_d(x)A_d(y) on disjoint inputs; f=1-2 A4',
            'dimension':n,'arithmetic':'rational outward intervals only; no floats in decisions',
            'logarithm':'atanh series, 64 terms, explicit rational remainder, 160-bit binary outward rounding',
            'ratio':rational_interval(ratio),'B_minus_4I':rational_interval(gap),
            'I_exact':str(I),'B':rational_interval(B),
            'limitation':'This refutes only the proposed constant 4 for the erasure bound. FEI remains open.'}
    Path('nand80_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
