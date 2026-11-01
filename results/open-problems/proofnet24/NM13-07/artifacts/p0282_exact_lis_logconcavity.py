#!/usr/bin/env python3
"""Exact finite certificate for P0282 (Chen LIS log-concavity).

For each n <= N, RSK gives
  ell[n,k] = sum_{lambda |- n, lambda_1 = k} (f^lambda)^2,
where f^lambda is the number of standard Young tableaux of shape lambda.
All arithmetic below is integer/rational exact.
"""

from fractions import Fraction
from math import factorial
import sys

N = int(sys.argv[1]) if len(sys.argv) > 1 else 50

def partitions(n, max_part=None):
    if n == 0:
        yield ()
        return
    if max_part is None or max_part > n:
        max_part = n
    for first in range(max_part, 0, -1):
        rem = n - first
        if rem == 0:
            yield (first,)
        else:
            for tail in partitions(rem, min(first, rem)):
                yield (first,) + tail

def f_shape(lam):
    # Weyl/hook dimension formula:
    # f^lambda = n! * prod_{i<j}(lambda_i-lambda_j+j-i)
    #            / prod_i (lambda_i + r-i-1)!
    n = sum(lam)
    r = len(lam)
    num = factorial(n)
    for i in range(r):
        for j in range(i + 1, r):
            num *= lam[i] - lam[j] + (j - i)
    den = 1
    for i in range(r):
        den *= factorial(lam[i] + r - i - 1)
    assert num % den == 0
    return num // den

global_checks = 0
mass_checks = 0
row_slice_positive_neighbor_checks = 0
worst = None
counts_4 = None
counts_7 = None

for n in range(1, N + 1):
    counts = [0] * (n + 1)
    by_rows = {}
    for lam in partitions(n):
        f = f_shape(lam)
        w = f * f
        counts[lam[0]] += w
        by_rows.setdefault(len(lam), [0] * (n + 1))[lam[0]] += w

    assert sum(counts) == factorial(n)
    mass_checks += 1

    for k in range(2, n):
        a, b, c = counts[k - 1], counts[k], counts[k + 1]
        assert b * b >= a * c, (n, k, a, b, c)
        global_checks += 1
        if a * c:
            ratio = Fraction(b * b, a * c)
            if worst is None or ratio < worst[0]:
                worst = (ratio, n, k, a, b, c, b * b - a * c)

    # Symmetry-breaking refinement: condition on exact number r of rows.
    # We verify every fixed-r slice is also log-concave on this finite range.
    for r, arr in by_rows.items():
        for k in range(2, n):
            a, b, c = arr[k - 1], arr[k], arr[k + 1]
            assert b * b >= a * c, ("row-slice", n, r, k, a, b, c)
            if a and c:
                row_slice_positive_neighbor_checks += 1

    if n == 4:
        counts_4 = counts[1:]
    if n == 7:
        counts_7 = counts[1:]

ratio, n0, k0, a0, b0, c0, diff0 = worst

print("P0282 exact finite certificate")
print(f"N={N}")
print(f"mass_checks={mass_checks} PASS")
print(f"global_logconcavity_checks={global_checks} PASS")
print(f"fixed_row_positive_neighbor_checks={row_slice_positive_neighbor_checks} PASS")
print(f"counts_n4={counts_4}")
print(f"counts_n7={counts_7}")
print(f"weakest_global_ratio_location=n={n0},k={k0}")
print(f"a=ell[n,k-1]={a0}")
print(f"b=ell[n,k]={b0}")
print(f"c=ell[n,k+1]={c0}")
print(f"b^2-a*c={diff0}")
print(f"b^2/(a*c)={ratio.numerator}/{ratio.denominator}")
print("ALL_EXACT_CHECKS_PASS")
