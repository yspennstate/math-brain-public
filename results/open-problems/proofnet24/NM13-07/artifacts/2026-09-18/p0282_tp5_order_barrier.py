#!/usr/bin/env python3
"""Exact order-of-total-positivity falsifier for P0282 coefficient array.

Defines A[k,j] = ell_{k+j,k}/((k+j)!)^2, where ell_{n,k} counts
permutations of [n] with LIS length k.  Counts are reconstructed by RSK:
ell_{n,k} = sum_{lambda |- n, lambda_1=k} (f^lambda)^2,
with f^lambda from the hook-length formula.

The checker independently verifies:
  * partition enumeration count p(n) for every 1<=n<=20;
  * Plancherel mass sum_k ell_{n,k}=n!;
  * signs of every contiguous square minor of orders 2..5 whose
    bottom-right A entry has total index k+j<=20.

All verdicts use Python arbitrary-precision integers and Fraction.
"""

from fractions import Fraction
from math import factorial

NMAX = 20

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
            for rest in partitions(rem, min(first, rem)):
                yield (first,) + rest

def partition_number_dp(n):
    dp = [0] * (n + 1)
    dp[0] = 1
    for part in range(1, n + 1):
        for s in range(part, n + 1):
            dp[s] += dp[s - part]
    return dp[n]

def f_standard_tableaux(lam):
    n = sum(lam)
    hooks = 1
    rows = len(lam)
    for i, rowlen in enumerate(lam):
        for j in range(rowlen):
            below = sum(1 for r in range(i + 1, rows) if lam[r] > j)
            hooks *= (rowlen - j) + below
    return factorial(n) // hooks

L = {}
partition_total = 0
for n in range(1, NMAX + 1):
    counts = [0] * (n + 1)
    pc = 0
    for lam in partitions(n):
        pc += 1
        f = f_standard_tableaux(lam)
        counts[lam[0]] += f * f
    expected_pc = partition_number_dp(n)
    assert pc == expected_pc, (n, pc, expected_pc)
    assert sum(counts) == factorial(n), (n, sum(counts), factorial(n))
    partition_total += pc
    L[n] = counts

def A(k, j):
    n = k + j
    return Fraction(L[n][k], factorial(n) ** 2)

def det_exact(mat):
    a = [row[:] for row in mat]
    n = len(a)
    det = Fraction(1)
    sign = 1
    for c in range(n):
        pivot = None
        for r in range(c, n):
            if a[r][c] != 0:
                pivot = r
                break
        if pivot is None:
            return Fraction(0)
        if pivot != c:
            a[c], a[pivot] = a[pivot], a[c]
            sign *= -1
        p = a[c][c]
        det *= p
        for j in range(c, n):
            a[c][j] /= p
        for r in range(c + 1, n):
            q = a[r][c]
            if q:
                for j in range(c, n):
                    a[r][j] -= q * a[c][j]
    return sign * det

stats = {}
negatives = {}
for order in range(2, 6):
    pos = zero = neg = 0
    negs = []
    for k0 in range(1, NMAX + 1):
        for j0 in range(0, NMAX + 1):
            if (k0 + order - 1) + (j0 + order - 1) > NMAX:
                continue
            mat = [[A(k0 + i, j0 + j) for j in range(order)]
                   for i in range(order)]
            d = det_exact(mat)
            if d > 0:
                pos += 1
            elif d == 0:
                zero += 1
            else:
                neg += 1
                negs.append((k0, j0, d))
    stats[order] = (pos, zero, neg)
    negatives[order] = negs

W = [[A(k, j) for j in range(5)] for k in range(2, 7)]
Wd = det_exact(W)
EXPECTED = Fraction(
    -2295333698673749,
    447542484623979239893855371264000000000000,
)
assert Wd == EXPECTED
assert stats[2][2] == 0
assert stats[3][2] == 0
assert stats[4][2] == 0
assert stats[5][2] > 0

print("P0282 exact contiguous-minor order scan")
print(f"NMAX={NMAX}")
print(f"partition_total_rows_1_to_20={partition_total}")
print("all_partition_counts_match_independent_dp=True")
print("all_plancherel_factorial_mass_checks=True")
for order in range(2, 6):
    pos, zero, neg = stats[order]
    print(f"order={order} positive={pos} zero={zero} negative={neg}")
for order in range(2, 5):
    assert negatives[order] == []
print("first_focal_negative_order5_top_left=(k=2,j=0)")
print(f"witness_det_num={Wd.numerator}")
print(f"witness_det_den={Wd.denominator}")
print("witness_matrix_A_rows_k2_to_k6_cols_j0_to_j4=")
for row in W:
    print("  " + " ".join(f"{x.numerator}/{x.denominator}" for x in row))
print("all_negative_order5_witnesses_in_scan=")
for k0, j0, d in negatives[5]:
    print(f"  k0={k0} j0={j0} det={d.numerator}/{d.denominator}")
print("CONCLUSION=A_is_not_TP5")
print("ALL_EXACT_CHECKS_PASS")
