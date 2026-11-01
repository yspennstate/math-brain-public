#!/usr/bin/env python3
"""Exact finite checks for R7-07 / F0012 nilpotent-fiber recovery.

All asserted matrix identities/counts use Python integers and Fraction Gaussian
elimination. No floating point arithmetic is used.
"""
from itertools import product
from fractions import Fraction
from collections import Counter
from math import comb

SIGNS = (-1, 1)

def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def is_zero(A):
    return all(x == 0 for row in A for x in row)

def rank_q(A):
    M = [[Fraction(x) for x in row] for row in A]
    m = len(M)
    n = len(M[0]) if m else 0
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if M[i][c] != 0), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        q = M[r][c]
        M[r] = [x / q for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                q = M[i][c]
                M[i] = [M[i][j] - q * M[r][j] for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def nilpotent(A):
    n = len(A)
    P = [row[:] for row in A]
    for _ in range(1, n):
        P = matmul(P, A)
    return is_zero(P)

def kernel_increment_profile(A):
    n = len(A)
    P = [row[:] for row in A]
    prev_nullity = 0
    inc = []
    for _ in range(1, n + 1):
        nullity = n - rank_q(P)
        inc.append(nullity - prev_nullity)
        prev_nullity = nullity
        if is_zero(P):
            break
        P = matmul(P, A)
    return tuple(inc)

def census(n):
    total = 0
    square_zero = 0
    profiles = Counter()
    for bits in product(SIGNS, repeat=n*n):
        A = [list(bits[i*n:(i+1)*n]) for i in range(n)]
        if nilpotent(A):
            total += 1
            profiles[kernel_increment_profile(A)] += 1
            if is_zero(matmul(A, A)):
                square_zero += 1
    return total, square_zero, profiles

expected = {
    1: (0, 0, {}),
    2: (4, 4, {(1, 1): 4}),
    3: (0, 0, {}),
    4: (2064, 144, {
        (1, 1, 1, 1): 1152,
        (2, 1, 1): 768,
        (2, 2): 96,
        (3, 1): 48,
    }),
}

for n in range(1, 5):
    total, sq, profiles = census(n)
    exp_total, exp_sq, exp_profiles = expected[n]
    assert total == exp_total
    assert sq == exp_sq
    assert dict(profiles) == exp_profiles
    print(f"n={n}: nilpotent={total}; square_zero={sq}; profiles={dict(sorted(profiles.items()))}")

# Local count for the nilpotent subfamily of the fixed shear construction.
# One off-diagonal orientation has a+b=0 and c+d=a+b: four choices.
# On the diagonal, requiring both triangular diagonal entries to vanish gives
# a+b=0, d-b=0, c+d=a+b: exactly two choices.
offdiag = 0
diag_nil = 0
for a,b,c,d in product(SIGNS, repeat=4):
    if a+b == 0 and c+d == a+b:
        offdiag += 1
    if a+b == 0 and d-b == 0 and c+d == a+b:
        diag_nil += 1
assert offdiag == 4
assert diag_nil == 2
print(f"fixed-shear local counts: offdiag={offdiag}, nilpotent_diag={diag_nil}")

for m in range(1, 6):
    n = 2*m
    count = (4 ** (m*(m-1))) * (2 ** m)
    expected_count = 2 ** (n*n//2 - n//2)
    assert count == expected_count
    print(f"shear_nilpotent_family n={n}: count={count}=2^({n*n//2 - n//2})")

# Numerical sanity check of the proved square-zero rank-r upper bound
# |Z_{n,r}| <= C(n,r)^2 2^{2r(n-r)} and its coarse all-r corollary.
for n in (2, 4, 6, 8):
    rhs = sum(comb(n,r)**2 * (2 ** (2*r*(n-r)))
              for r in range(1, n//2 + 1))
    coarse = (n+1) * (2 ** (2*n)) * (2 ** (n*n//2))
    assert rhs <= coarse
    print(f"square_zero_bound n={n}: rank_sum_rhs={rhs}; coarse_rhs={coarse}")

print("F0012_NILPOTENT_RECOVERY_EXACT_CHECK_PASS")
