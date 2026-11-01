#!/usr/bin/env python3
"""Stress test for B17 one-overlap MUX theorem.

Enumerates every ordered pair of Boolean branches a(y,u1,u2), b(y,v1,v2).
Walsh coefficients are exact Fractions; entropy is evaluated in binary float
only as a stress test. The theorem itself is analytic in REPORT.md.
"""
from fractions import Fraction
import hashlib
import math

def fwht_int(vals):
    a = list(vals)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x,y = a[j],a[j+h]
                a[j],a[j+h] = x+y,x-y
        h *= 2
    n = len(a)
    return [Fraction(x,n) for x in a]

def phi(q):
    x=float(q)
    return 0.0 if x <= 0.0 else -x*math.log2(x)

def psi(x,y):
    return (phi((x+y)*(x+y)/4) + phi((x-y)*(x-y)/4)
            - 0.5*phi(x*x) - 0.5*phi(y*y))

branches=[]
for mask in range(256):
    vals=[1 if (mask>>i)&1 else -1 for i in range(8)]
    A=fwht_int(vals)
    x=(A[0],A[1])
    R=Fraction(1)-x[0]*x[0]-x[1]*x[1]
    assert abs(x[0])+abs(x[1]) <= 1
    branches.append((mask,x,R))

count=0
min_slack=float("inf")
max_ratio=(-1.0,None)
for ma,x,Ra in branches:
    for mb,w,Rb in branches:
        d=x[0]*w[0]+x[1]*w[1]
        q=(Fraction(1)-d)/2
        Omega=float(Ra+Rb)+psi(x[0],w[0])+psi(x[1],w[1])
        slack=6.0*float(q)-Omega
        if slack < min_slack:
            min_slack=slack
        if slack < -2e-12:
            raise AssertionError((ma,mb,q,Omega,slack))
        if q:
            ratio=Omega/float(q)
            if ratio > max_ratio[0]:
                max_ratio=(ratio,(ma,mb,x,w,q,Omega))
        count += 1

r,arg=max_ratio
print("ordered_branch_pairs", count)
print("minimum_6q_minus_Omega", format(min_slack,".17g"))
print("maximum_Omega_over_q", format(r,".15f"))
ma,mb,x,w,q,Omega=arg
print("argmax_masks", ma, mb)
print("argmax_core_a", x)
print("argmax_core_b", w)
print("argmax_q", q)
print("argmax_Omega", format(Omega,".16f"))
print("PASS")
