#!/usr/bin/env python3
"""Finite falsification check for B14 proxy-gauge activation-drop lemmas.

Enumerates Boolean functions modulo global output sign through n=3, every
nonempty proper physical block, and every branch-dependent character map.
The analytic report is independent of this floating-point check.
"""
from itertools import product
import math

def fwht(vals):
    a=[float(x) for x in vals]
    n=len(a); h=1
    while h<n:
        for i in range(0,n,2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return [x/n for x in a]

def spectrum(vals):
    return [x*x for x in fwht(vals)]

def phi(z,k):
    return sum(z**r for r in range(k))

def P(probs,n,z,T):
    return sum(p*phi(z,(s^T).bit_count()) for s,p in enumerate(probs))

def activation(probs,n,z):
    return min(P(probs,n,z,T) for T in range(1<<n))

def folded_J(probs,n):
    return min(sum(p*(s^T).bit_count() for s,p in enumerate(probs))
               for T in range(1<<n))

def ordinary_I(probs):
    return sum(p*s.bit_count() for s,p in enumerate(probs))

def restrict(vals,n,B,assignment):
    qb=[i for i in range(n) if (B>>i)&1]
    rb=[i for i in range(n) if not ((B>>i)&1)]
    out=[]
    for y in range(1<<len(rb)):
        x=0
        for j,i in enumerate(qb):
            if (assignment>>j)&1: x |= 1<<i
        for j,i in enumerate(rb):
            if (y>>j)&1: x |= 1<<i
        out.append(vals[x])
    return out

def character_shift(vals,T):
    return [v*(-1 if ((x&T).bit_count()&1) else 1)
            for x,v in enumerate(vals)]

cases=0
min_coercivity=float("inf")
min_drop_slack=float("inf")

for n in range(1,4):
    z=0.0 if n==1 else 1.0-1.0/n
    a=1.0 if n==1 else z**(n-1)
    # fix f(0)=+1, quotienting the irrelevant global output sign
    for tail in product((1,-1), repeat=(1<<n)-1):
        vals=[1,*tail]
        probs=spectrum(vals)
        J=folded_J(probs,n)
        A=activation(probs,n,z)
        min_coercivity=min(min_coercivity,A-a*J)

        for B in range(1,(1<<n)-1):
            qb=[i for i in range(n) if (B>>i)&1]
            m=n-len(qb)
            zc=0.0 if m<=1 else 1.0-1.0/m
            nb=1<<len(qb)
            chars=range(1<<m)
            for Tmap in product(chars, repeat=nb):
                mean_A=0.0
                mean_I=0.0
                for b,T in enumerate(Tmap):
                    child=restrict(vals,n,B,b)
                    cp=spectrum(child)
                    mean_A += activation(cp,m,zc)/nb
                    shifted=spectrum(character_shift(child,T))
                    mean_I += ordinary_I(shifted)/nb
                Tdrop=A-mean_A
                min_drop_slack=min(
                    min_drop_slack,
                    Tdrop-(a*J-mean_I)
                )
                cases+=1

print("cases", cases)
print("min_coercivity_slack", format(min_coercivity, ".17g"))
print("min_proxy_gauge_drop_slack", format(min_drop_slack, ".17g"))
assert min_coercivity >= -1e-12
assert min_drop_slack >= -1e-12
