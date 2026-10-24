#!/usr/bin/env python3
"""Small exact sanity checker for the P05 one-sided run-cap ladder.

The proof in the companion report is analytic.  This script only checks the
pathwise deletion/increment inequalities on a finite exhaustive family and
the exact M=1 phase formula.  It is not Monte Carlo and is not used to infer
an asymptotic constant.
"""
from itertools import product
from fractions import Fraction


def lcs(a, b):
    dp = [0] * (len(b) + 1)
    for x in a:
        prev = 0
        for j, y in enumerate(b, 1):
            old = dp[j]
            dp[j] = prev + 1 if x == y else max(dp[j], dp[j - 1])
            prev = old
    return dp[-1]


def build_runs(v, phase):
    return ''.join(str(phase ^ (i & 1)) * g for i, g in enumerate(v))


def cap(v, M):
    return tuple(min(g, M) for g in v)


checks = 0
for r in range(1, 4):
    vecs = list(product(range(1, 5), repeat=r))
    for gx in vecs:
        for gy in vecs:
            for px in (0, 1):
                for py in (0, 1):
                    x = build_runs(gx, px)
                    y = build_runs(gy, py)
                    for M in range(1, 4):
                        xm = build_runs(cap(gx, M), px)
                        diff = lcs(x, y) - lcs(xm, y)
                        deleted = sum(max(g - M, 0) for g in gx)
                        assert 0 <= diff <= deleted

                        xmp = build_runs(cap(gx, M + 1), px)
                        inc = lcs(xmp, y) - lcs(xm, y)
                        added = sum(1 for g in gx if g >= M + 1)
                        assert 0 <= inc <= added
                        checks += 2

phase_checks = 0
for r in range(1, 6):
    x = build_runs((1,) * r, 0)
    for gy in product(range(1, 5), repeat=r):
        y_same = build_runs(gy, 0)
        y_opp = build_runs(gy, 1)
        assert lcs(x, y_same) == r
        assert lcs(x, y_opp) == r - 1
        phase_checks += 2

for M in range(1, 9):
    excess_mean = Fraction(1, 2 ** (M - 1))  # E[(G-M)_+]
    normalized_step_cap = Fraction(1, 2 ** (M + 1))
    print(M, excess_mean, normalized_step_cap)

print('pathwise_checks', checks)
print('phase_checks', phase_checks)
print('ONE_SIDED_CAP_LADDER_SMALL_CASE_PASS')
