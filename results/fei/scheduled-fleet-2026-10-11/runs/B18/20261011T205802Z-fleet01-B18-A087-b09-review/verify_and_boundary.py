#!/usr/bin/env python3
"""Exact rational checks and high-precision diagnostics for B09 AND boundary.

The proof of the asymptotic statement is analytic and appears in REPORT.md.
The symbolic checks here verify the exact probability identities.  Decimal
values are diagnostics only and are not used as interval certificates.
"""

from fractions import Fraction
from decimal import Decimal, getcontext

checks = 0
for dp in range(2, 18):
    for np in range(1, dp):
        p = Fraction(np, dp)
        for dq in range(2, 18):
            for nq in range(1, dq):
                q = Fraction(nq, dq)
                v = 4*q*(1-q)
                a = 4*q*q
                w0 = (1-2*p*q)**2
                wx = 4*q*q*p*(1-p)
                wy = 4*p*p*q*(1-q)
                wxy = 4*p*(1-p)*q*(1-q)
                assert w0+wx+wy+wxy == 1
                assert wy+wxy == p*v
                assert w0+wx == 1-p*v
                assert wx/(w0+wx) == a*p*(1-p)/(1-p*v)
                assert wxy/(wy+wxy) == 1-p
                assert v-a == 4*q*(1-2*q)
                checks += 6
assert (4*Fraction(1,4)*(1-2*Fraction(1,4))) == Fraction(1,2)

getcontext().prec = 80
LN2 = Decimal(2).ln()

def h2(x):
    if x == 0 or x == 1:
        return Decimal(0)
    return -(x*x.ln()+(1-x)*(1-x).ln())/LN2

def values(pp, qq=Decimal(1)/4):
    vv = 4*qq*(1-qq)
    aa = 4*qq*qq
    theta = aa*pp*(1-pp)/(1-pp*vv)
    J = h2(pp*vv)-pp*h2(vv)
    M = (1-pp*vv)*h2(theta)+pp*vv*h2(pp)
    Delta = pp*((1-pp)/pp).ln()/LN2
    return J, M, Delta, (J-M)/Delta

print(f"EXACT_RATIONAL_IDENTITIES PASS checks={checks}")
print("q=1/4 diagnostic ratios (J-M)/Delta; analytic limit = 1/2")
for k in (8, 16, 32, 64):
    pp = Decimal(2) ** (-k)
    J, M, Delta, ratio = values(pp)
    print(f"k={k:2d} p=2^-{k} ratio={ratio:.40f} "
          f"gap={J-M:.20E} Delta={Delta:.20E}")
