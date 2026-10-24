#!/usr/bin/env python3
# C28 / I0103 exact baseline rerun for the 2026-09-16 stuck-recovery report.
# Mathematical assertions use exact integer/radical arithmetic via SymPy.

import sympy as sp

p = 73
S = (0, 1, 2, 3, 5, 32, 38, 41, 45, 46, 52, 54, 58, 61)
m = len(S)
x = sp.symbols("x")

assert sp.isprime(p) and p % 4 == 1
assert 13**5 < p**3 < 14**5 and m == 14

def legendre(a, p):
    a %= p
    if a == 0:
        return 0
    e = pow(a, (p - 1)//2, p)
    assert e in (1, p - 1)
    return 1 if e == 1 else -1

A = sp.Matrix(m, m, lambda i, j: 0 if i == j else legendre(S[i] - S[j], p))
assert A == A.T
charpoly = sp.expand(A.charpoly(x).as_expr())
expected = sp.expand(
    (x - 5) * (x - 3)**2 * (x - 1)**3 * (x + 1)**3 * (x + 3)**3 * (x**2 + 2*x - 51)
)
assert sp.expand(charpoly - expected) == 0

sqrt13 = sp.sqrt(13)
lam_min = -1 - 2*sqrt13
lam_max = -1 + 2*sqrt13
other_roots = [-3, -1, 1, 3, 5]
assert all(sp.simplify(r - lam_min) > 0 for r in other_roots)
assert all(sp.simplify(lam_max - r) > 0 for r in other_roots)
assert sp.simplify(sp.sqrt(73) - (1 + 2*sqrt13)) > 0

kappa_sq = sp.simplify((sp.sqrt(73) + lam_max) / (sp.sqrt(73) + lam_min))
kappa = sp.sqrt(kappa_sq)

scale = 10**6
lo73, hi73, lo13 = 8544003, 8544004, 3605551
assert lo73**2 < 73*scale**2 < hi73**2
assert lo13**2 < 13*scale**2
lb_sq = sp.Rational(lo73 - scale + 2*lo13, hi73 - scale - 2*lo13)
assert sp.simplify(kappa_sq - lb_sq) > 0

print("C28_PALEY_ETF_EXACT_CERTIFICATE_RERUN")
print(f"p={p}")
print(f"m={m}")
print("epsilon=1/10; regime m(p)=ceil(p^(3/5))")
print("subset=" + repr(S))
print("charpoly_factor=" + str(sp.factor(charpoly)))
print("lambda_min=" + str(lam_min))
print("lambda_max=" + str(lam_max))
print("kappa_squared_exact=" + str(kappa_sq))
print("kappa_exact=" + str(kappa))
print("kappa_decimal_15=" + str(sp.N(kappa, 16)))
print("certified_rational_lower_bound_for_kappa_squared=" + str(lb_sq))
print("certified_rational_lower_bound_for_kappa=" + str(sp.N(sp.sqrt(lb_sq), 16)))
print("ALL_EXACT_CHECKS_PASS")
