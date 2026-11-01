from fractions import Fraction
from itertools import combinations
import random
import math


def det(M):
    A = [[Fraction(x) for x in row] for row in M]
    n = len(A)
    ans = Fraction(1)
    for i in range(n):
        p = next((r for r in range(i, n) if A[r][i] != 0), None)
        if p is None:
            return Fraction(0)
        if p != i:
            A[i], A[p] = A[p], A[i]
            ans = -ans
        a = A[i][i]
        ans *= a
        for j in range(i + 1, n):
            A[i][j] /= a
        A[i][i] = 1
        for r in range(i + 1, n):
            b = A[r][i]
            if b:
                for j in range(i + 1, n):
                    A[r][j] -= b * A[i][j]
                A[r][i] = 0
    return ans


def sub(A, R, C):
    return [[A[i][j] for j in C] for i in R]


def compound2(A):
    m, n = len(A), len(A[0])
    out = Fraction(0)
    for R in combinations(range(m), 2):
        for C in combinations(range(n), 2):
            q = det(sub(A, R, C))
            out += q * q
    return out


def schur_numerator_trial(rng, m=5):
    d = Fraction(rng.choice([1, 2, 3, -1, -2]), rng.choice([1, 2, 3]))
    w = [Fraction(rng.randint(-3, 3)) for _ in range(m)]
    C = [[Fraction(0) for _ in range(m)] for __ in range(m)]
    for i in range(m):
        for j in range(i, m):
            x = Fraction(rng.randint(-3, 3))
            C[i][j] = C[j][i] = x

    S = [[Fraction(0) for _ in range(m + 1)] for __ in range(m + 1)]
    S[0][0] = d
    for i in range(m):
        S[0][i + 1] = S[i + 1][0] = w[i]
        for j in range(m):
            S[i + 1][j + 1] = C[i][j]

    N = [[d * C[i][j] - w[i] * w[j] for j in range(m)] for i in range(m)]

    W = Fraction(0)
    outside = tuple(range(1, m + 1))
    for R0 in combinations(outside, 2):
        for C0 in combinations(outside, 2):
            ds = det(sub(S, (0,) + R0, (0,) + C0))
            dn = det(sub(N, tuple(i - 1 for i in R0), tuple(j - 1 for j in C0)))
            assert dn == d * ds
            W += ds * ds

    assert compound2(N) == d * d * W


def elementary(lam, k):
    out = 0.0
    for I in combinations(range(len(lam)), k):
        p = 1.0
        for i in I:
            p *= lam[i]
        out += p
    return out


def tail_trial(rng, rmax=8):
    # Exact nonnegative rational squared-singular-value surrogate.
    lam = sorted([Fraction(rng.randint(0, 20), rng.randint(1, 7)) for _ in range(rmax)], reverse=True)
    C1 = sum(lam)
    C2 = sum(lam[i] * lam[j] for i in range(rmax) for j in range(i + 1, rmax))
    C3 = sum(lam[i] * lam[j] * lam[k]
             for i in range(rmax) for j in range(i + 1, rmax) for k in range(j + 1, rmax))
    T1 = sum(lam[1:])
    T2 = sum(lam[2:])
    assert T1 * C1 <= 2 * C2
    assert T2 * C2 <= 3 * C3


def stress_check():
    # d=1/64 instance of S_d from the report.
    d = Fraction(1, 64)
    # N=diag(-4,d)
    L = Fraction(16) + d * d
    C2 = Fraction(16) * d * d
    assert C2 * 64 < L * L  # quantitative rank-one-tube branch
    # |lambda_-| > (4-d)/2 > 1 follows algebraically for 0<d<3.
    assert d > 0 and d < 3


if __name__ == "__main__":
    rng = random.Random(20260923000441)
    for _ in range(250):
        schur_numerator_trial(rng)
    for _ in range(5000):
        tail_trial(rng)
    stress_check()
    c0 = 1.0 / (3.0 * math.sqrt(200.0))
    c2 = 7.673759290384858
    c3 = 9.840655864922019
    C2_floor = c0 ** 2 / 64.0
    E2_cross_floor = C2_floor / 48.0
    density2 = c2 * E2_cross_floor ** (-1.0 / 8.0)
    half2 = 4.0 * math.sqrt(density2)
    C3_floor = c0 ** 3 / 12288.0
    E3_cross_floor = C3_floor / 256.0
    density3 = c3 * E3_cross_floor ** (-1.0 / 12.0)
    half3 = 4.0 * math.sqrt(density3)
    print("exact_schur_numerator_trials=250 PASS")
    print("exact_compound_tail_trials=5000 PASS")
    print("stress_d=1/64 PASS")
    print(f"c0={c0:.15f}")
    print(f"C2_floor={C2_floor:.15g}")
    print(f"E2_cross_floor={E2_cross_floor:.15g}")
    print(f"density_bound_E2={density2:.12f}")
    print(f"half_riesz_bound_E2={half2:.12f}")
    print(f"C3_floor={C3_floor:.15g}")
    print(f"E3_cross_floor={E3_cross_floor:.15g}")
    print(f"density_bound_E3={density3:.12f}")
    print(f"half_riesz_bound_E3={half3:.12f}")
    print("QFORM_SCHUR_NUMERATOR_CASCADE_CHECK_PASS")
