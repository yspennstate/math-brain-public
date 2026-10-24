#!/usr/bin/env python3
"""Exact checks for PROB20-07 improved interior product-TV bound."""
import sympy as sp
from fractions import Fraction
import random

a,d,m = sp.symbols("a d m", positive=True)
b = 1-m*a

# Invariant-diameter formula and endpoint specialization.
D_bound = sp.simplify(2 - 2*a - 1/b)
assert sp.simplify(D_bound.subs({m:3,a:sp.Rational(1,12)}) - sp.Rational(1,2)) == 0

# All-dimension threshold from b(2-2a)=1.
root = sp.simplify(((m+1)-sp.sqrt(m**2+1))/(2*m))
assert sp.simplify(2*(1-root)*(1-m*root)-1) == 0

# Sharp m=3 equality construction.
r3 = 1 - 2*a - d
x = sp.Matrix([a+d,a,r3])
y = sp.Matrix([a,a+d,r3])
diff = []
for i in range(3):
    for j in range(3):
        diff.append(sp.factor(x[i]*x[j]-y[i]*y[j]))

expected = [
    d*(2*a+d), 0, d*r3,
    0, -d*(2*a+d), -d*r3,
    d*r3, -d*r3, 0,
]
for got, exp in zip(diff, expected):
    assert sp.simplify(got-exp) == 0

# Under 0<d<=1-3a, r3>=a>0, so the absolute values have the signs above.
prod_tv_sharp = sp.expand(d*(2*a+d) + 2*d*r3)
assert sp.simplify(prod_tv_sharp - d*(2-2*a-d)) == 0

# Compare old and new invariant diameter bounds.
old = 2 - 1/b
new = 2 - 2*a - 1/b
assert sp.simplify(old-new-2*a) == 0

# Rational spot checks using exact Fraction arithmetic.
def tv(v,w):
    return sum(abs(vi-wi) for vi,wi in zip(v,w))/2

def kron(v):
    return [vi*vj for vi in v for vj in v]

tests = [
    (Fraction(1,12), Fraction(1,10)),
    (Fraction(1,12), Fraction(1,2)),
    (Fraction(1,10), Fraction(1,5)),
]
for aa,dd in tests:
    assert dd <= 1-3*aa
    rr = 1-2*aa-dd
    xx = [aa+dd, aa, rr]
    yy = [aa, aa+dd, rr]
    got = tv(kron(xx),kron(yy))
    want = dd*(2-2*aa-dd)
    assert got == want

# Seeded exact-rational diagnostics for the inequality in dimension 3.
rng = random.Random(20260916)
for _ in range(1000):
    # denominator 120, each coordinate at least 10/120=1/12
    A = 10
    remaining = 120-3*A
    cuts = sorted([rng.randrange(remaining+1), rng.randrange(remaining+1)])
    parts1 = [cuts[0], cuts[1]-cuts[0], remaining-cuts[1]]
    cuts = sorted([rng.randrange(remaining+1), rng.randrange(remaining+1)])
    parts2 = [cuts[0], cuts[1]-cuts[0], remaining-cuts[1]]
    xx = [Fraction(A+p,120) for p in parts1]
    yy = [Fraction(A+p,120) for p in parts2]
    dd = tv(xx,yy)
    got = tv(kron(xx),kron(yy))
    want = dd*(2-Fraction(2,12)-dd)
    assert got <= want

print("ALL EXACT INTERIOR PRODUCT-TV CHECKS PASSED")
