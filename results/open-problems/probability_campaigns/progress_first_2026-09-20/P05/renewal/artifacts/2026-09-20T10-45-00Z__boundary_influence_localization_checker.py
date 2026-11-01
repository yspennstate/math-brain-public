#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
from functools import lru_cache
import math


def lcs(x, y):
    dp = [0] * (len(y) + 1)
    for a in x:
        prev = 0
        for j, b in enumerate(y, 1):
            old = dp[j]
            if a == b:
                dp[j] = prev + 1
            elif dp[j - 1] > dp[j]:
                dp[j] = dp[j - 1]
            prev = old
    return dp[-1]


@lru_cache(None)
def F(m, n):
    if m == 0 or n == 0:
        return Fraction(0)
    total = 0
    for x in product((0, 1), repeat=m):
        for y in product((0, 1), repeat=n):
            total += lcs(x, y)
    return Fraction(total, 2 ** (m + n))


def joint_direct(m, n):
    # Condition on mismatch orientation X_1=0, Y_1=1.
    # The common core has lengths m-1 and n-1.
    counts = {(0, 0): 0, (1, 0): 0, (0, 1): 0, (1, 1): 0}
    for U in product((0, 1), repeat=m - 1):
        for V in product((0, 1), repeat=n - 1):
            c = lcs(U, V)
            alpha = lcs(U, (1,) + V) - c
            beta = lcs((0,) + U, V) - c
            assert alpha in (0, 1) and beta in (0, 1)
            counts[(alpha, beta)] += 1
    den = 2 ** (m + n - 2)
    return {k: Fraction(v, den) for k, v in counts.items()}


checked = 0
for m in range(1, 7):
    for n in range(1, 7):
        f = F(m, n)
        fl = F(m - 1, n)
        fd = F(m, n - 1)
        f0 = F(m - 1, n - 1)
        predicted = {
            (0, 0): 2 * (1 + f0 - f),
            (1, 0): 2 * f - fd - f0 - 1,
            (0, 1): 2 * f - fl - f0 - 1,
            (1, 1): 1 + fl + fd - 2 * f,
        }
        direct = joint_direct(m, n)
        assert direct == predicted, (m, n, direct, predicted)
        assert sum(predicted.values(), Fraction(0)) == 1
        assert all(v >= 0 for v in predicted.values())
        q = direct[(1, 0)] + direct[(0, 1)]
        q_poisson = 4 * f - 2 - 2 * f0 - fl - fd
        assert q == q_poisson
        checked += 1

# Numerical sanity checks for the explicit width chosen from the analytic
# exponential Green-strip estimate in the report.  This is not the proof of
# the mgf inequality; it checks the stated inversion formula.
for n in (10, 100, 1000, 10000):
    for eps in (Fraction(1, 10), Fraction(1, 100), Fraction(1, 1000)):
        e = float(eps)
        w = math.ceil(
            math.sqrt(2 * (n - 1) * math.log(4 * (n - 1) / (n * e)))
        )
        bound = 4 * (n - 1) / n * math.exp(-(w * w) / (2 * n - 2))
        assert bound <= e * (1 + 1e-12), (n, e, w, bound)

print("rectangles_checked =", checked)
print("max_rectangle = 6x6")
print("joint_boundary_influence_law = PASS")
print("poisson_xor_consistency = PASS")
print("exponential_strip_width_formula = PASS")
print("EXACT_BOUNDARY_INFLUENCE_IDENTITY_PASS")
