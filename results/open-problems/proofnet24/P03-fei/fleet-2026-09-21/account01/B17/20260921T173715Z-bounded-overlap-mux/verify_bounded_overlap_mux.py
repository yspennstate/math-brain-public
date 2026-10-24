#!/usr/bin/env python3
"""Finite r=2 self-check for the bounded-overlap MUX toll theorem.

This is a stress test, not the proof. It enumerates all conditional-mean
vectors g,h in {-1,0,1}^4, evaluates the exact MUX entropy toll formula in
floating arithmetic, and checks the proved analytic constant C_2.
"""
from itertools import product
from math import e, log2

def phi(x):
    return 0.0 if x <= 0.0 else -x * log2(x)

def walsh4(v):
    pts = ((1,1),(1,-1),(-1,1),(-1,-1))
    out = []
    for mask in range(4):
        s = 0.0
        for a,(y1,y2) in zip(v,pts):
            chi = 1.0
            if mask & 1:
                chi *= y1
            if mask & 2:
                chi *= y2
            s += a * chi
        out.append(s / 4.0)
    return out

def psi(u,v):
    return (
        phi((u+v)**2 / 4.0)
        + phi((u-v)**2 / 4.0)
        - 0.5 * (phi(u*u) + phi(v*v))
    )

def toll(g,h):
    x = walsh4(g)
    w = walsh4(h)
    ra = 1.0 - sum(t*t for t in x)
    rb = 1.0 - sum(t*t for t in w)
    omega = ra + rb + sum(psi(u,v) for u,v in zip(x,w))
    q = (1.0 - sum(u*v for u,v in zip(x,w))) / 2.0
    return omega, q

C2 = max(2 + 5 + log2(e), 7 + 1 + 0.5*log2(e))
vals = list(product((-1.0,0.0,1.0), repeat=4))
best_ratio = -1.0
best = None
violations = 0
tested = 0

for g in vals:
    for h in vals:
        omega, q = toll(g,h)
        tested += 1
        if q > 1e-15:
            ratio = omega / q
            if ratio > best_ratio:
                best_ratio = ratio
                best = (g,h,omega,q)
            if omega > C2*q + 1e-12:
                violations += 1

assert tested == 6561
assert violations == 0

print("status=PASS")
print("tested_pairs=6561")
print("C2=%.15f" % C2)
print("violations=%d" % violations)
print("max_ratio=%.15f" % best_ratio)
print("argmax_g=%s" % (best[0],))
print("argmax_h=%s" % (best[1],))
print("argmax_omega=%.16f" % best[2])
print("argmax_q=%.16f" % best[3])
