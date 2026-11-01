from fractions import Fraction
from math import comb, factorial


def laplace_sstar(lam: int) -> Fraction:
    # P_i are iid Gamma(2,1), S_* = sum P_i - max P_i.
    # For integer lambda, c=1+lambda and
    # L_lambda = 4/c^6 * sum_{r=0}^3 (-1)^r C(3,r)
    #            * sum_{j=0}^r C(r,j)c^j (j+1)!/(1+rc)^(j+2).
    c = 1 + lam
    total = Fraction(0, 1)
    for r in range(4):
        inner = Fraction(0, 1)
        for j in range(r + 1):
            inner += Fraction(
                comb(r, j) * (c ** j) * factorial(j + 1),
                (1 + r * c) ** (j + 2),
            )
        total += ((-1) ** r) * comb(3, r) * inner
    return Fraction(4, c ** 6) * total


L2 = laplace_sstar(2)
L3 = laplace_sstar(3)
q = Fraction(3, 2) * L2 - L3

assert L2 == Fraction(235233, 60025000)
assert L3 == Fraction(26555608, 33834074625)
assert q == Fraction(165509375107103, 32494245269850000)
assert q > 0

print("L2 =", L2, float(L2))
print("L3 =", L3, float(L3))
print("q_corner =", q, float(q))
print("q_gate = 4*exp(-4) (symbolic exact form)")
print("P20-FPP-CORNER-CREDIT-EXACT: ALL_CHECKS_PASS")
