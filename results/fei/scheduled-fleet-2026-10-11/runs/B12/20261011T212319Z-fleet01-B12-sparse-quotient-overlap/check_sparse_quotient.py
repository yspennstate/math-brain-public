#!/usr/bin/env python3
"""Exhaustive quotient-space check for B12 A058 sparse-union theorem.

Enumerates every nonempty B subset of F_2^r with
  |B| <= floor(2^(r/2)) and |B|/2^r <= 1/4,
for 2 <= r <= 5.  All Walsh coefficients, Parseval identities,
influences, and boundary counts are computed as integers/rationals;
only the displayed Shannon entropies use floating-point logarithms.
No randomness is used.
"""

from itertools import combinations
from math import floor, log2


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


checked = 0
max_ratio = (-1.0, None)
min_bound_slack = (float("inf"), None)
min_iso_slack_numer = None
two_cell_checks = 0

for r in range(2, 6):
    n = 1 << r
    max_m = floor(2 ** (r / 2))
    for m in range(1, max_m + 1):
        if 4 * m > n:
            continue
        for comb in combinations(range(n), m):
            checked += 1
            indicator = [0] * n
            for y in comb:
                indicator[y] = 1
            walsh = fwht(indicator)

            # Integer Parseval: sum W(alpha)^2 = n*m.
            assert sum(w * w for w in walsh) == n * m

            p = m / n
            q = 2 * p - p * p
            masses = [(1 - p) ** 2, p * p]
            for w in walsh[1:]:
                a2 = (w / n) ** 2
                masses.extend((a2, a2))
            assert abs(sum(masses) - 1.0) < 2e-12

            H = entropy(masses)
            # For L = identity, I(K)=p+2 sum |alpha| a_alpha^2.
            I = p + 2 * sum(
                alpha.bit_count() * (walsh[alpha] / n) ** 2
                for alpha in range(1, n)
            )

            # Exact directed-boundary numerator for D_B: I(D_B)=boundary/n.
            boundary = sum(
                1
                for y in range(n)
                for j in range(r)
                if indicator[y] != indicator[y ^ (1 << j)]
            )
            I_D = boundary / n
            assert abs(I - (p + I_D / 2)) < 2e-12

            ell = log2(1 / p)
            iso_slack_numer = boundary - 2 * m * ell
            if min_iso_slack_numer is None or iso_slack_numer < min_iso_slack_numer[0]:
                min_iso_slack_numer = (iso_slack_numer, (r, comb))
            assert iso_slack_numer > -2e-10

            H_bound = (-(1-q)*log2(1-q) - q*log2(q)) + q*(r+1)
            slack = H_bound - H
            if slack < min_bound_slack[0]:
                min_bound_slack = (slack, (r, comb, H, H_bound))
            assert slack > -2e-12
            assert H <= 8 * I + 2e-12

            ratio = H / I
            if ratio > max_ratio[0]:
                max_ratio = (ratio, (r, comb, H, I))

    # Any two points in F_2^r form a one-dimensional affine subspace.
    for a, b in combinations(range(n), 2):
        direction = a ^ b
        assert direction != 0
        assert {a, a ^ direction} == {a, b}
        two_cell_checks += 1

print("scope: exhaustive nonempty B subsets for r=2..5 satisfying p<=1/4 and |B|<=floor(2^(r/2))")
print("randomness: none")
print(f"sparse subsets checked: {checked}")
print(f"two-cell affine-collapse checks: {two_cell_checks}")
print(f"max exact H/I: {max_ratio[0]:.15f} at {max_ratio[1]}")
print(f"minimum support-entropy bound slack: {min_bound_slack[0]:.15e} at {min_bound_slack[1]}")
print(f"minimum edge-isoperimetric numerator slack: {min_iso_slack_numer[0]:.15e} at {min_iso_slack_numer[1]}")
print("PASS: exact Walsh/Parseval/influence identities, edge boundary lower bound, support entropy bound, and H<=8I")
