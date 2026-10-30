#!/usr/bin/env python3
"""Deterministic audit for B12 A058 effective-support v2.

Scope:
  * every nonempty B subset F_2^r for r=1,...,4 with p<=1/2;
  * every B subset of F_2^5 with 1<=|B|<=5.
The theorem condition log2(2M-1)<=2 log2(1/p)+1 is then filtered,
where M is the exact nonzero Walsh-support size of 1_B.

Walsh coefficients, Parseval, support size, and edge boundaries use
integer arithmetic.  Floating point is used only for logarithms.
No randomness is used.
"""

from itertools import combinations
from math import log2


LOG2E = log2(2.7182818284590452353602874713527)


def fwht(values):
    out = list(values)
    h = 1
    while h < len(out):
        for i in range(0, len(out), 2 * h):
            for j in range(i, i + h):
                x, y = out[j], out[j + h]
                out[j], out[j + h] = x + y, x - y
        h *= 2
    return out


def entropy(weights):
    return sum(-w * log2(w) for w in weights if w)


def subsets_for_r(r):
    n = 1 << r
    if r <= 4:
        for mask in range(1, 1 << n):
            m = mask.bit_count()
            if 2 * m <= n:
                yield tuple(i for i in range(n) if (mask >> i) & 1)
    else:
        for m in range(1, 6):
            yield from combinations(range(n), m)


examined = 0
admissible = 0
new_beyond_v1 = 0
max_ratio = (-1.0, None)
min_six_slack = (float("inf"), None)
min_analytic_slack = (float("inf"), None)

for r in range(1, 6):
    n = 1 << r
    for comb in subsets_for_r(r):
        examined += 1
        m = len(comb)
        p = m / n
        indicator = [0] * n
        for y in comb:
            indicator[y] = 1
        walsh = fwht(indicator)
        assert sum(w * w for w in walsh) == n * m
        M = sum(w != 0 for w in walsh)
        d = log2(2 * M - 1)
        ell = log2(1 / p)
        if d > 2 * ell + 1 + 1e-14:
            continue
        admissible += 1
        if not (p <= 0.25 and ell >= r / 2):
            new_beyond_v1 += 1

        masses = [(1 - p) ** 2, p * p]
        for w in walsh[1:]:
            a2 = (w / n) ** 2
            masses.extend((a2, a2))
        assert abs(sum(masses) - 1) < 2e-12
        H = entropy(masses)

        boundary = sum(
            1
            for y in range(n)
            for j in range(r)
            if indicator[y] != indicator[y ^ (1 << j)]
        )
        I_D = boundary / n
        I = p + I_D / 2
        I_fourier = p + 2 * sum(
            alpha.bit_count() * (walsh[alpha] / n) ** 2
            for alpha in range(1, n)
        )
        assert abs(I - I_fourier) < 2e-12
        assert I_D + 2e-12 >= 2 * p * ell

        q = 2 * p - p * p
        support_bound = (-(1-q)*log2(1-q) if q < 1 else 0.0)
        if q:
            support_bound += -q * log2(q) + q * d
        analytic_bound = q * (ell + LOG2E + d)
        assert H <= support_bound + 2e-12
        assert support_bound <= analytic_bound + 2e-12
        assert analytic_bound < 6 * p * (ell + 1) + 2e-12
        assert H < 6 * I + 2e-12

        ratio = H / I
        if ratio > max_ratio[0]:
            max_ratio = (ratio, (r, comb, p, M, H, I))
        slack = 6 * I - H
        if slack < min_six_slack[0]:
            min_six_slack = (slack, (r, comb, p, M))
        analytic_slack = 6 * p * (ell + 1) - analytic_bound
        if analytic_slack < min_analytic_slack[0]:
            min_analytic_slack = (analytic_slack, (r, comb, p, M))

print("scope: all p<=1/2 subsets for r<=4; all 1<=|B|<=5 for r=5")
print("randomness: none")
print(f"sets examined: {examined}")
print(f"v2-admissible sets: {admissible}")
print(f"admissible sets outside v1 hypotheses: {new_beyond_v1}")
print(f"max exact H/I: {max_ratio[0]:.15f} at {max_ratio[1]}")
print(f"minimum exact 6I-H slack: {min_six_slack[0]:.15e} at {min_six_slack[1]}")
print(f"minimum analytic 6p(ell+1)-bound slack: {min_analytic_slack[0]:.15e} at {min_analytic_slack[1]}")
print("PASS: effective support ledger, physical influence identity, isoperimetry, and H<6I")
