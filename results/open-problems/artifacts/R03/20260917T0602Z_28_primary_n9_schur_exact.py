#!/usr/bin/env python3
"""
R03 run28 exact arithmetic checker.

Scope:
1. Recompute the collision-free binary count G_9 from the signed-Stirling formula.
2. Take the externally sourced exact total singular 9x9 binary count S_9
   (OEIS A046747, a(9), credited to Dominik Beck 2026-07-02; the later
   Beck-Lv-Potechin arXiv:2607.26857 documents the exhaustive n=9
   canonical-representative/Bareiss enumeration that obtains the full c_9 data).
3. Derive the exact residual count R_9 and exact normalized R03 value r(10).
4. Verify that this strictly improves the previous replay-certified bound.
5. Exhaustively verify, for n<=4, the standard sign-to-binary singular-count
   multiplicity S_sign(n)=2^(2n-1) S_binary(n-1).
6. Exhaustively verify, at binary order m=4, the Schur-complement/minor-incidence
   identity used in C277.

This checker does NOT re-run the external 9x9 canonical enumeration.
"""

from fractions import Fraction
from itertools import product
from decimal import Decimal, getcontext

getcontext().prec = 60

def det_bareiss(M):
    A = [list(map(int, row)) for row in M]
    n = len(A)
    if n == 0:
        return 1
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            pivot = next((i for i in range(k + 1, n) if A[i][k] != 0), None)
            if pivot is None:
                return 0
            A[k], A[pivot] = A[pivot], A[k]
            sign = -sign
        piv = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * piv - A[i][k] * A[k][j]) // prev
        for i in range(k + 1, n):
            A[i][k] = 0
        prev = piv
    return sign * A[n - 1][n - 1]

def rank_q(M):
    if not M:
        return 0
    A = [[Fraction(x) for x in row] for row in M]
    r = 0
    rows, cols = len(A), len(A[0])
    for c in range(cols):
        piv = next((i for i in range(r, rows) if A[i][c]), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        q = A[r][c]
        A[r] = [x / q for x in A[r]]
        for i in range(rows):
            if i != r and A[i][c]:
                q = A[i][c]
                A[i] = [A[i][j] - q * A[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r

def s1_table(n):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            dp[i][k] = dp[i-1][k-1] - (i-1) * dp[i-1][k]
    return dp

def falling(x, m):
    z = 1
    for j in range(m):
        z *= x - j
    return z

def collision_free_binary_count(m):
    s = s1_table(m + 1)
    return sum(s[m+1][b+1] * falling(2**b - 1, m) for b in range(m + 1))

def all_matrices(vals, n):
    for flat in product(vals, repeat=n*n):
        yield [list(flat[i*n:(i+1)*n]) for i in range(n)]

def count_singular(vals, n):
    return sum(det_bareiss(M) == 0 for M in all_matrices(vals, n))

def no_binary_collisions(B):
    n = len(B)
    for X in (B, [list(c) for c in zip(*B)]):
        for i in range(n):
            if all(v == 0 for v in X[i]):
                return False
        for i in range(n):
            for j in range(i+1, n):
                if X[i] == X[j]:
                    return False
    return True

def minor(B, di, dj):
    n = len(B)
    return [[B[i][j] for j in range(n) if j != dj]
            for i in range(n) if i != di]

def binary_schur_identity_check(m):
    """
    For fixed deleted last row/column, Xi(A) counts collision-free singular
    border completions of an invertible (m-1)x(m-1) binary A.
    Summing over all m^2 deleted positions must equal the sum, over residual
    rank-(m-1) collision-free matrices B, of their number of nonzero cofactors.
    """
    k = m - 1
    bits = list(product((0, 1), repeat=k))
    xi_sum = 0
    invertible_A = 0

    for flat in product((0, 1), repeat=k*k):
        A = [list(flat[i*k:(i+1)*k]) for i in range(k)]
        if det_bareiss(A) == 0:
            continue
        invertible_A += 1
        cols = {tuple(A[i][j] for i in range(k)) for j in range(k)}
        rows = {tuple(r) for r in A}

        for b in bits:
            if b == (0,)*k or b in cols:
                continue
            for c in bits:
                if c == (0,)*k or c in rows:
                    continue
                hits = 0
                for d in (0, 1):
                    B = [A[i] + [b[i]] for i in range(k)] + [list(c) + [d]]
                    if det_bareiss(B) == 0 and no_binary_collisions(B):
                        hits += 1
                assert hits <= 1
                xi_sum += hits

    residual_rank_m1 = 0
    weighted_nonzero_cofactors = 0
    for B in all_matrices((0, 1), m):
        if det_bareiss(B) == 0 and rank_q(B) == m-1 and no_binary_collisions(B):
            residual_rank_m1 += 1
            nonzero_cofactors = sum(
                det_bareiss(minor(B, i, j)) != 0
                for i in range(m) for j in range(m)
            )
            assert nonzero_cofactors >= 9
            weighted_nonzero_cofactors += nonzero_cofactors

    assert m*m*xi_sum == weighted_nonzero_cofactors
    return invertible_A, xi_sum, residual_rank_m1, weighted_nonzero_cofactors

m = 9
G9 = collision_free_binary_count(m)
expected_G9 = 2040859528996474439366400
assert G9 == expected_G9

S9_SOURCE = 902616230040448613437952
collision_singular9 = 2**81 - G9
R9 = S9_SOURCE - collision_singular9
assert collision_singular9 == 376992110232783910045952
assert R9 == 525624119807664703392000

r10 = Fraction(R9, 2**71)
expected_r10 = Fraction(2053219217998690247625, 9223372036854775808)
assert r10 == expected_r10

old_r10 = Fraction(81207138539551628924901, 295147905179352825856)
assert r10 < old_r10
gain = old_r10 - r10

r11 = Fraction(
    4080135425100039167106240490725,
    7787900129957441143457185792,
)

transform_checks = []
for n in range(2, 5):
    sign_sing = count_singular((-1, 1), n)
    bin_sing = count_singular((0, 1), n-1)
    assert sign_sing == (2**(2*n-1)) * bin_sing
    transform_checks.append((n, sign_sing, bin_sing))

schur4 = binary_schur_identity_check(4)
assert schur4 == (174, 1152, 1800, 18432)

def dec(fr):
    return Decimal(fr.numerator) / Decimal(fr.denominator)

print("R03 RUN28 EXACT ARITHMETIC CHECK")
print("EXTERNAL_ENUMERATION_INPUT: S9 =", S9_SOURCE)
print("EXTERNAL_ENUMERATION_NOT_REEXECUTED_HERE")
print("G9 =", G9)
print("collision_singular9 =", collision_singular9)
print("R9 =", R9)
print("r10 =", r10.numerator, "/", r10.denominator)
print("r10_decimal =", dec(r10))
print("old_r10_decimal =", dec(old_r10))
print("strict_gain =", gain.numerator, "/", gain.denominator)
print("strict_gain_decimal =", dec(gain))
print("r11_retained_decimal =", dec(r11))
for n, ss, bs in transform_checks:
    print(f"sign_binary_check n={n}: sign_singular={ss}, binary_singular={bs}, multiplier={2**(2*n-1)}")
print("binary_schur_identity m=4:",
      "invertible_A3=", schur4[0],
      "Xi_sum=", schur4[1],
      "residual_rank3=", schur4[2],
      "weighted_nonzero_cofactors=", schur4[3])
print("SELF-CHECK PASS")
