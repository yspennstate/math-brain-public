#!/usr/bin/env python3
"""Finite checks for QFORM-HEAVY-FRESH-TRANSVERSE-CROSS-LIFT-v1."""
import math
import random

def lhs(x,H,g,n,d):
    return g*(n*x+H)**2+d*x

def rhs(x,H,g,n,d):
    return (g*n*n*(x+H/n+d/(2*g*n*n))**2
            -d*H/n-d*d/(4*g*n*n))

for _ in range(10000):
    x,H,d=[random.uniform(-10,10) for _ in range(3)]
    g=random.choice([-1,1])*random.uniform(.01,10)
    n=random.choice([-1,1])*random.uniform(1/math.sqrt(2),1)
    err=abs(lhs(x,H,g,n,d)-rhs(x,H,g,n,d))
    assert err < 1e-8*(1+abs(lhs(x,H,g,n,d)))

worst_neg=1e9
for k in range(100001):
    delta=(1/16)*k/100000
    s2=1+(1/63)*k/100001
    s=math.sqrt(s2)
    neg=2*(math.sqrt(delta*delta*s2*s2+4*s2)-delta*s2)
    worst_neg=min(worst_neg,neg)
assert worst_neg>1
assert abs(32*math.sqrt(2)-45.254833995939045)<1e-12
print("square completion: passed")
print("minimum sampled negative eigenvalue magnitude:",worst_neg)
print("universal heavy-coordinate constant:",32*math.sqrt(2))
