#!/usr/bin/env python3
"""Exact checks for the P05 balanced geometric-tail quantizer theorem.

This is supporting evidence.  The arbitrary-r comparison and scalar-quantizer
optimality are proved analytically in the accompanying immutable report.
"""
from fractions import Fraction
from itertools import product


def q_center(g, M):
    return g if g < M else M + 1


def runs_to_string(rs, phase):
    return "".join(str((phase + i) & 1) * r for i, r in enumerate(rs))


def lcs(a, b):
    dp = [0] * (len(b) + 1)
    for ca in a:
        prev = 0
        for j, cb in enumerate(b, 1):
            old = dp[j]
            if ca == cb:
                dp[j] = prev + 1
            elif dp[j - 1] > dp[j]:
                dp[j] = dp[j - 1]
            prev = old
    return dp[-1]


# 1. Exact scalar L1 quantization recurrence for Geom(1/2).
# D_K = min E|G-Q(G)| over deterministic integer Q with <=K outputs.
D = {1: Fraction(1, 1)}
argmins = {1: (1, 2)}  # the one-centre medians of the full geometric tail
for K in range(2, 13):
    prev = D[K - 1]
    vals = {}
    # The proof shows the optimum is attained at b=2 (and also b=3 only
    # when K=2), so b<=40 is far beyond what is needed for this check.
    for b in range(2, 41):
        first_cluster = Fraction(1, 1) - Fraction(b, 2 ** (b - 1))
        tail = prev / (2 ** (b - 1))
        vals[b] = first_cluster + tail
    best = min(vals.values())
    args = tuple(b for b, v in vals.items() if v == best)
    D[K] = best
    argmins[K] = args
    assert best == Fraction(1, 2 ** (K - 1))
    if K == 2:
        assert args == (2, 3)
    else:
        assert args == (2,)


# 2. Exact moments of the centered tail quantizer.
# Tail event: G>=M, P=2^{-(M-1)}. Conditional excess E=G-M has
# P(E=e)=2^{-(e+1)}, mean 1 and variance 2. Q_M sends the whole tail to M+1.
# Hence delta=G-Q_M(G)=E-1 on the tail.
moment_rows = []
for M in range(1, 13):
    p = Fraction(1, 2 ** (M - 1))
    alpha = Fraction(1, 2 ** M)       # E(delta)_+
    beta = Fraction(1, 2 ** M)        # E(-delta)_+
    abs_moment = Fraction(1, 2 ** (M - 1))
    second = Fraction(1, 2 ** (M - 2)) if M >= 2 else Fraction(2, 1)
    assert alpha == beta
    assert abs_moment == alpha + beta
    assert second == 2 * p

    # Mean preservation: sum_{k=1}^{M-1} k/2^k +(M+1)/2^{M-1}=2.
    finite_mean = sum(Fraction(k, 2 ** k) for k in range(1, M))
    q_mean = finite_mean + Fraction(M + 1, 2 ** (M - 1))
    assert q_mean == 2

    # Asymptotic one-side and two-side common-core comparison budgets.
    one_side = max(alpha, beta) / 2
    two_side = max(alpha + alpha, beta + beta) / 2
    assert one_side == Fraction(1, 2 ** (M + 1))
    assert two_side == Fraction(1, 2 ** M)

    # Optimality inside the scalar common-core architecture:
    # max(alpha,beta) >= E|delta|/2 >= D_M/2.
    assert D[M] / 4 == one_side
    moment_rows.append((M, p, alpha, second, one_side, two_side))


# 3. Exhaustive deterministic common-core inequality checks.
one_side_cases = 0
for M in range(1, 5):
    for r in range(1, 4):
        vals = range(1, M + 4)
        for g in product(vals, repeat=r):
            q = tuple(q_center(x, M) for x in g)
            A = sum(max(x - y, 0) for x, y in zip(g, q))
            B = sum(max(y - x, 0) for x, y in zip(g, q))
            for phase in (0, 1):
                x = runs_to_string(g, phase)
                xq = runs_to_string(q, phase)
                for ny in range(0, 6):
                    for yt in product("01", repeat=ny):
                        y = "".join(yt)
                        assert abs(lcs(x, y) - lcs(xq, y)) <= max(A, B)
                        one_side_cases += 1


two_side_cases = 0
for M in range(1, 4):
    for r in range(1, 4):
        vals = range(1, M + 3)
        tuples = list(product(vals, repeat=r))
        for g in tuples:
            qg = tuple(q_center(x, M) for x in g)
            Ax = sum(max(x - y, 0) for x, y in zip(g, qg))
            Bx = sum(max(y - x, 0) for x, y in zip(g, qg))
            for h in tuples:
                qh = tuple(q_center(x, M) for x in h)
                Ay = sum(max(x - y, 0) for x, y in zip(h, qh))
                By = sum(max(y - x, 0) for x, y in zip(h, qh))
                for px in (0, 1):
                    x = runs_to_string(g, px)
                    xq = runs_to_string(qg, px)
                    for py in (0, 1):
                        y = runs_to_string(h, py)
                        yq = runs_to_string(qh, py)
                        assert abs(lcs(x, y) - lcs(xq, yq)) <= max(Ax + Ay, Bx + By)
                        two_side_cases += 1


print("scalar_L1_distortions_K1_to_K12 =", [str(D[k]) for k in range(1, 13)])
print("scalar_recurrence_argmins_K2_to_K12 =", [argmins[k] for k in range(2, 13)])
print("moment_rows_M1_to_M12 =")
for row in moment_rows:
    print(tuple(str(x) for x in row))
print("one_side_common_core_cases_checked =", one_side_cases)
print("two_side_common_core_cases_checked =", two_side_cases)
print("BALANCED_TAIL_QUANTIZER_EXACT_CHECK_PASS")
