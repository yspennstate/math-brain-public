#!/usr/bin/env python3
"""Exact rational self-check for the D0030 lower-psi obstruction family.

For M >= 3, define a binary pair (U,V) by
  P(U=1,V=1)=0,
  P(U=1,V=0)=1/2,
  P(U=0,V=1)=1/M,
  P(U=0,V=0)=1/2-1/M.
The report proves parametrically that phi(sigma(U),sigma(V))=1/M,
psi'(sigma(U),sigma(V))=0, and rho(U,V)^2=1/(M-1).
This checker exhausts all nonempty binary events for several exact rational M.
It is a finite self-check, not an independent proof or audit.
"""

from fractions import Fraction
from itertools import combinations


def events():
    base = {0, 1}
    return [frozenset(s) for r in (1, 2) for s in combinations(base, r)]


def metrics(M):
    d = Fraction(1, M)
    p = {
        (0, 0): Fraction(1, 2) - d,
        (0, 1): d,
        (1, 0): Fraction(1, 2),
        (1, 1): Fraction(0),
    }
    assert all(x >= 0 for x in p.values())
    assert sum(p.values()) == 1

    ev = events()

    def pu(A):
        return sum(q for (u, v), q in p.items() if u in A)

    def pv(B):
        return sum(q for (u, v), q in p.items() if v in B)

    def pab(A, B):
        return sum(q for (u, v), q in p.items() if u in A and v in B)

    phi = Fraction(0)
    psi_prime = None
    for A in ev:
        pa = pu(A)
        if pa == 0:
            continue
        for B in ev:
            pb = pv(B)
            if pb == 0:
                continue
            phi = max(phi, abs(pab(A, B) / pa - pb))
            ratio = pab(A, B) / (pa * pb)
            psi_prime = ratio if psi_prime is None else min(psi_prime, ratio)

    # For two binary variables, HGR maximal correlation squared equals the
    # squared 2x2 determinant divided by the product of the four marginals.
    det = p[(0, 0)] * p[(1, 1)] - p[(0, 1)] * p[(1, 0)]
    rho2 = det * det / (pu({0}) * pu({1}) * pv({0}) * pv({1}))
    return phi, psi_prime, rho2


print("D0030 exact binary lower-psi obstruction checker")
print("Joint law: P11=0, P10=1/2, P01=1/M, P00=1/2-1/M")
for M in [3, 4, 5, 10, 100, 1000]:
    phi, psi_prime, rho2 = metrics(M)
    assert phi == Fraction(1, M)
    assert psi_prime == 0
    assert rho2 == Fraction(1, M - 1)
    print(f"M={M}: phi={phi}, psi'={psi_prime}, rho^2={rho2}")
print("ALL_EXACT_CHECKS_PASS")
