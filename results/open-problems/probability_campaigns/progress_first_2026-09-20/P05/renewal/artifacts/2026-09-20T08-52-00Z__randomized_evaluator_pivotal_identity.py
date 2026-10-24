#!/usr/bin/env python3
"""
P05 binary LCS: exact randomized-evaluator / pivotal-density identity self-check.

For deterministic strings x,y, let V(i,j) be the suffix LCS value. At a mismatch,
V(i,j)=max(A,B)=(A+B)/2 + |A-B|/2, where
A=V(i+1,j), B=V(i,j+1), and |A-B| in {0,1}.

The randomized evaluator chooses the two deletion branches with probability 1/2
at each mismatch, awards the local bonus |A-B|/2, and moves diagonally with
reward 1 at a match. Dynamic programming proves its expected reward equals the
exact LCS for every deterministic pair.

For iid uniform binary strings, average path statistics satisfy
E[M_n]=E[Q_n]=E[T_n]/2=(2n-E[H_n])/3
and
E[L_n]=E[M_n]+E[P_n]/2,
where M_n=#match steps, Q_n=#mismatch steps, P_n=#pivotal mismatches
(|A-B|=1), T_n=M_n+Q_n, and H_n is the terminal coordinate deficit.

This program exhaustively verifies the deterministic identity for every binary
pair up to length 8 and the exact averaged identities at each n.
"""

from fractions import Fraction
from itertools import product

MAX_N = 8

def suffix_lcs_table(x, y):
    n = len(x)
    m = len(y)
    V = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if x[i] == y[j]:
                V[i][j] = 1 + V[i + 1][j + 1]
            else:
                V[i][j] = max(V[i + 1][j], V[i][j + 1])
    return V

def evaluator_stats(x, y, V):
    n = len(x)
    m = len(y)
    memo = {}

    # Returns exact expectations (T, M, Q, P, H) from suffix state (i,j).
    def rec(i, j):
        if i == n or j == m:
            return (
                Fraction(0), Fraction(0), Fraction(0), Fraction(0),
                Fraction(abs(i - j))
            )
        key = (i, j)
        if key in memo:
            return memo[key]

        if x[i] == y[j]:
            T, M, Q, P, H = rec(i + 1, j + 1)
            ans = (T + 1, M + 1, Q, P, H)
        else:
            left = rec(i + 1, j)
            right = rec(i, j + 1)
            delta = abs(V[i + 1][j] - V[i][j + 1])
            assert delta in (0, 1)

            avg = tuple((left[k] + right[k]) / 2 for k in range(5))
            ans = (
                avg[0] + 1,
                avg[1],
                avg[2] + 1,
                avg[3] + delta,
                avg[4],
            )

        memo[key] = ans
        return ans

    return rec(0, 0)

print("P05 exact randomized-evaluator / pivotal-density check")
print("MAX_N =", MAX_N)

for n in range(1, MAX_N + 1):
    pair_count = 2 ** (2 * n)
    sums = [Fraction(0) for _ in range(6)]  # L,T,M,Q,P,H

    for x in product((0, 1), repeat=n):
        for y in product((0, 1), repeat=n):
            V = suffix_lcs_table(x, y)
            T, M, Q, P, H = evaluator_stats(x, y, V)
            L = Fraction(V[0][0])

            # Exact deterministic evaluator identity.
            assert L == M + P / 2

            vals = (L, T, M, Q, P, H)
            for k, val in enumerate(vals):
                sums[k] += val

    L, T, M, Q, P, H = [s / pair_count for s in sums]

    # Exact source-averaged path identities.
    assert M == Q
    assert 2 * M == T
    assert Fraction(3, 2) * T == 2 * n - H
    assert L == M + P / 2

    pivotal_density = P / Q
    assert pivotal_density == 2 * (L / M - 1)

    print(
        "n =", n,
        "pairs =", pair_count,
        "E_LCS =", L,
        "E_LCS_over_n =", float(L / n),
        "E_T =", T,
        "E_M =", M,
        "E_Q =", Q,
        "E_P =", P,
        "E_H =", H,
        "p_n =", pivotal_density,
        "p_n_decimal =", format(float(pivotal_density), ".15f"),
    )

print("EXACT_RANDOMIZED_EVALUATOR_PIVOTAL_IDENTITY_PASS")
