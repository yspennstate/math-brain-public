#!/usr/bin/env python3
"""Independent audit of B05-A023 singleton-potential propagation."""

from fractions import Fraction
from math import log, log2
import itertools
import random

LN2 = log(2.0)
M = 2.0 / LN2
RHO = (1.0 + LN2) / 4.0
LAM = 4.0 / (1.0 - LN2)
CSTAR = LAM * M
TOL = 3e-10


def fwht(vals):
    a = [Fraction(x) for x in vals]
    h = 1
    while h < len(a):
        for k in range(0, len(a), 2*h):
            for j in range(k, k+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return [x / len(a) for x in a]


def upper(p):
    q = list(p)
    n = len(q).bit_length()-1
    for j in range(n):
        bit = 1 << j
        for s in range(1 << n):
            if not s & bit:
                q[s] += q[s | bit]
    return q


def U(f):
    p = [x*x for x in fwht(f)]
    pi = upper(p)
    return sum(float(x)*log2(float(y/x)) for x, y in zip(p, pi) if x)


def restrict(f, j, b):
    n = len(f).bit_length()-1
    out = []
    for z in range(1 << (n-1)):
        lo = z & ((1 << j)-1)
        hi = z >> j
        out.append(f[lo | (b << j) | (hi << (j+1))])
    return tuple(out)


def I(f):
    n = len(f).bit_length()-1
    return sum(Fraction(sum(f[x] != f[x ^ (1 << j)] for x in range(len(f))), len(f)) for j in range(n))


def G(f):
    n = len(f).bit_length()-1
    u = U(f)
    return sum(u - (U(restrict(f,j,0))+U(restrict(f,j,1)))/2 for j in range(n))


def phi(h):
    h = abs(float(h))
    return 0.0 if h == 0 else 2*h*h*(log2(1/h)+1/LN2)


def Phi(f):
    a = fwht(f)
    n = len(f).bit_length()-1
    return sum(phi(a[1 << j]) for j in range(n))


def R(t):
    def ent(x): return 0.0 if x == 0 else x*log2(1/x)
    x = (1+t)**2/4
    y = (1-t)**2/4
    e = ent(x) + (0.0 if y == 0 else y*log2(2/(1-t)))
    u = 0.0 if t == 0 else t*t*log2(1/(t*t))
    return e-u/2+(1-t*t)/4


def activate(q):
    return tuple(q[x >> 1] if not (x & 1) else 1 for x in range(2*len(q)))


def product(f,g):
    return tuple(f[x]*g[y] for y in range(len(g)) for x in range(len(f)))


def defect(r, sign=1):
    q = [sign]*(1 << r)
    q[-1] = -sign
    return tuple(q)


rng = random.Random(0xB19A094)
scalar = 0
worst_mid = (-1e9, None)
for j in range(1, 200001):
    h = j/200001
    assert phi(h) <= M*h + TOL
    assert phi(h/2) <= RHO*phi(h) + TOL
    for t in (-1+2*h,):
        assert R(t) <= 5*(1-t)/2 + TOL
    scalar += 2
for _ in range(200000):
    x, y = rng.uniform(-1,1), rng.uniform(-1,1)
    m, h = (x+y)/2, abs(x-y)/2
    slack = R(m)-(R(x)+R(y))/2-phi(h)
    worst_mid = max(worst_mid, (slack,(x,y)))
    assert slack <= TOL
    scalar += 1

functions = []
for n in range(4):
    for mask in range(1 << (1 << n)):
        functions.append(tuple(1 if (mask >> x)&1 else -1 for x in range(1 << n)))

identities = invariants = restrictions = 0
max_err = 0.0

for r in range(1,257):
    q = defect(r) if r <= 18 else None
    p = 2.0**(-r)
    beta = 1-2*p
    Iq = 2*r*p
    Uq = 0.0 if r == 1 else beta*beta*log2(1/(beta*beta))+2*r*p*beta
    if r == 1:
        Gq = 0.0
    else:
        pp = 2.0**(-(r-1)); bp = 1-2*pp
        Up = 0.0 if r == 2 else bp*bp*log2(1/(bp*bp))+2*(r-1)*pp*bp
        Gq = r*(Uq-Up/2)
    assert Gq <= 5*Iq+TOL
    scalar += 1
for f in functions:
    If, Uf, Gf, Pf = float(I(f)), U(f), G(f), Phi(f)
    assert Pf <= M*If + TOL
    for b in (0.0, .41, .91):
        a = 0.0 if If == 0 else max(0.0,(Gf-b*Uf)/If)
        A = max(a,5.0)+CSTAR
        assert Gf+LAM*Pf <= A*If+b*Uf+TOL
        invariants += 1
    F = activate(f)
    J = (1-float(sum(f)/len(f)))/2
    max_err = max(max_err, abs(float(I(F))-(If/2+J)))
    assert Phi(F) <= RHO*Pf+M*J+TOL
    identities += 2
    for r, s in ((1,1),(1,-1),(2,1),(2,-1)):
        q = product(defect(r,s),f)
        assert Phi(q) <= Pf+M*float(I(defect(r,s)))+TOL
        assert abs(U(q)-U(f)-U(defect(r,s))) <= 2e-10
        assert abs(G(q)-G(f)-G(defect(r,s))) <= 2e-10
        identities += 3
    n = len(f).bit_length()-1
    for j in range(n):
        for bit in (0,1):
            r = restrict(f,j,bit)
            assert Phi(r) <= M*float(I(r))+TOL
            restrictions += 1

# Exact correction witness: I(F2)=3/4+(r+1/2)2^-r < 1 for r>=6.
correction = 0
for r in range(6,101):
    val = Fraction(3,4)+(Fraction(2*r+1,2)*(Fraction(1,2)**r))
    assert val < 1
    correction += 1

print(f"scalar_checks={scalar}")
print(f"boolean_functions={len(functions)}")
print(f"identity_checks={identities}")
print(f"invariant_checks={invariants}")
print(f"restriction_checks={restrictions}")
print(f"correction_checks={correction}")
print(f"rho={RHO:.15f}")
print(f"lambda={LAM:.15f}")
print(f"Cstar={CSTAR:.15f}")
print(f"worst_midpoint_slack={worst_mid[0]:.3e}")
print(f"max_identity_error={max_err:.3e}")
print("PASS")
