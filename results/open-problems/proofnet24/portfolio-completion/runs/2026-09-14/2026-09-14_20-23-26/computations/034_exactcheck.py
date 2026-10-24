#!/usr/bin/env python3
"""Independent exact checks for the worker 034 subcritical proof audit.

No simulation or asymptotic claim is inferred from these finite calculations.
Infinite-tail enclosures use the analytic bounds proved in agents/034.md.
"""
from fractions import Fraction as F
from math import gcd, isqrt
from functools import reduce

q = F(1, 4)
d = F(3, 4)
n = 256
rare_support = []
first_moment = q
second_moment = q
records = []
for stage in range(1, 4):
    h = d * n
    assert h.denominator == 1
    root_n = isqrt(n)
    assert root_n * root_n == n
    lo, hi = int(h) - root_n, int(h) + root_n
    assert F(5, 8) * n < lo < hi <= F(13, 16) * n
    assert lo % 16 == hi % 16 == 0
    if rare_support:
        assert max(rare_support) < lo
    assert 2 * lo > n - 1
    p = F(1, n**4)
    first_moment += p * (lo + hi)
    second_moment += p * (lo * lo + hi * hi)
    d *= 1 - F(2, n**3)
    assert first_moment == 1 - d
    rare_support += [lo, hi]
    records.append((stage, n, lo, hi))
    n = n**4

# The next n is n_4. The errors bound all later stages, not a numerical truncation.
mean_lo = first_moment
mean_hi = first_moment + F(4, n**3)
var_lo = second_moment - mean_hi**2
var_hi = second_moment + F(4, n**2) - mean_lo**2
gamma_lo = q * (1 - mean_hi)
gamma_hi = q * (1 - mean_lo)
a_lo = gamma_lo / var_hi
a_hi = gamma_hi / var_lo
v_lo = q * (1 - q) - gamma_hi**2 / var_lo
v_hi = q * (1 - q) - gamma_lo**2 / var_hi
assert F(1, 4) < mean_lo <= mean_hi < F(5, 16)
assert F(1, 8) < var_lo <= var_hi < F(1, 2)
assert 0 < a_lo <= a_hi
assert 0 < v_lo <= v_hi

claimed = {
    "nu": (
        "0.25000008940696716308593750001893",
        "0.25000008940696716308593750001894",
        mean_lo, mean_hi,
    ),
    "sigma2": (
        "0.18751724064349328819349030655071",
        "0.18751724064349328819349030655072",
        var_lo, var_hi,
    ),
    "a_star": (
        "0.99990793915708316509750109871089",
        "0.99990793915708316509750109871090",
        a_lo, a_hi,
    ),
    "v_star": (
        "0.000017283757730977125785051309865713",
        "0.000017283757730977125785051309865714",
        v_lo, v_hi,
    ),
}
for name, (outer_lo, outer_hi, inner_lo, inner_hi) in claimed.items():
    assert F(outer_lo) <= inner_lo <= inner_hi <= F(outer_hi), name

# These give an exact check on the endpoint arithmetic of the Bernstein constant.
# The general inequalities are proved symbolically in the report.
assert F(7, 12) * 256 - 1 > F(256, 3)
assert F(1, 9) / F(8, 3) == F(1, 24)
assert reduce(gcd, rare_support) == 16

print("PASS: three exact recursive support stages and telescoping mean identity")
for stage, size, lo, hi in records:
    print(f"stage={stage} n={size} Lminus={lo} Lplus={hi}")
print("PASS: all four printed decimal intervals enclose exact infinite-tail bounds")
print("PASS: positive conditional residual variance, Bernstein arithmetic, rare gcd=16")
print("LIMITATION: no numerical conditional-probability or asymptotic-convergence test")
