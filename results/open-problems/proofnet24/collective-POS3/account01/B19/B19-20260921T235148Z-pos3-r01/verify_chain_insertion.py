#!/usr/bin/env python3
"""Deterministic regression checks for the POS3 chain-insertion recurrence.

This script is evidence, not a substitute for the proof in REPORT.md.
It uses only the Python standard library.
"""
from itertools import permutations


def transitive_closure(n, rel):
    R = [[False] * n for _ in range(n)]
    for a, b in rel:
        R[a][b] = True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    R[i][j] = R[i][j] or R[k][j]
    return R


def linear_extensions(R, subset):
    subset = list(subset)
    out = []
    for p in permutations(subset):
        pos = {x: i for i, x in enumerate(p)}
        ok = True
        for a in subset:
            for b in subset:
                if R[a][b] and not (pos[a] < pos[b]):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(p)
    return out


def chain_data(R, C, Q, tau):
    n = len(Q)
    pos = {q: i + 1 for i, q in enumerate(tau)}
    a, b = [], []
    for c in C:
        a.append(max((pos[q] for q in Q if R[q][c]), default=0))
        b.append(min((pos[q] - 1 for q in Q if R[c][q]), default=n))

    m = len(C)
    F = [[0] * (n + 1) for _ in range(m)]
    for r in range(n + 1):
        F[0][r] = int(a[0] <= r <= b[0])
    for j in range(1, m):
        prefix = 0
        for r in range(n + 1):
            prefix += F[j - 1][r]
            F[j][r] = prefix if a[j] <= r <= b[j] else 0

    G = [[0] * (n + 1) for _ in range(m)]
    for r in range(n + 1):
        G[m - 1][r] = int(a[m - 1] <= r <= b[m - 1])
    for j in range(m - 2, -1, -1):
        suffix = 0
        for r in range(n, -1, -1):
            suffix += G[j + 1][r]
            G[j][r] = suffix if a[j] <= r <= b[j] else 0

    W = sum(F[m - 1])
    for t in range(m):
        assert W == sum(F[t][r] * G[t][r] for r in range(n + 1))
    return W, pos, a, b, F, G


def bias_example():
    # x=0, y=1, c=2 with x<c and y incomparable to both.
    R = transitive_closure(3, {(0, 2)})
    Q, C = [0, 1], [2]
    weights = {}
    for tau in linear_extensions(R, Q):
        W, *_ = chain_data(R, C, Q, tau)
        weights[tau] = W
    assert weights[(0, 1)] == 2
    assert weights[(1, 0)] == 1
    assert sum(weights.values()) == len(linear_extensions(R, [0, 1, 2])) == 3
    return weights


def unbounded_distortion_family(s=8):
    # Q is A={a} plus a chain B of length s.  Add c above a and
    # incomparable with all B.  W(tau) is 1 + number of B-elements after a.
    a = 0
    B = list(range(1, s + 1))
    c = s + 1
    rel = {(B[i], B[i + 1]) for i in range(s - 1)} | {(a, c)}
    R = transitive_closure(s + 2, rel)
    Q, C = [a] + B, [c]
    vals = []
    for tau in linear_extensions(R, Q):
        W, *_ = chain_data(R, C, Q, tau)
        expected = 1 + sum(1 for b in B if tau.index(b) > tau.index(a))
        assert W == expected
        vals.append(W)
    assert min(vals) == 1
    assert max(vals) == s + 1
    return min(vals), max(vals)


def exhaustive_five_point_regression():
    # 1024 generated five-point posets.  Labels 0<1<2<3<4 give an acyclic
    # ambient order; C=(1,3) is forced to be a chain and Q=(0,2,4).
    # We verify both the total-extension recurrence and the forward/backward
    # formula for every Q--C pair against direct enumeration.
    N = 5
    C = [1, 3]
    Q = [0, 2, 4]
    pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    checked = 0
    for mask in range(1 << len(pairs)):
        rel = {(1, 3)}
        for bit, edge in enumerate(pairs):
            if (mask >> bit) & 1:
                rel.add(edge)
        R = transitive_closure(N, rel)
        LQ = linear_extensions(R, Q)
        LP = linear_extensions(R, range(N))

        total = 0
        predicted = {(q, c): 0 for q in Q for c in C}
        for tau in LQ:
            W, pos, a, b, F, G = chain_data(R, C, Q, tau)
            assert W >= 1
            assert all(a[j] <= b[j] for j in range(len(C)))
            assert all(a[j] <= a[j + 1] for j in range(len(C) - 1))
            assert all(b[j] <= b[j + 1] for j in range(len(C) - 1))
            total += W
            for t, c in enumerate(C):
                for q in Q:
                    predicted[(q, c)] += sum(
                        F[t][r] * G[t][r]
                        for r in range(pos[q], len(Q) + 1)
                    )

        assert total == len(LP)
        for q, c in predicted:
            direct = sum(1 for L in LP if L.index(q) < L.index(c))
            assert predicted[(q, c)] == direct
        checked += 1
    return checked


if __name__ == "__main__":
    print("bias_weights=", bias_example())
    print("distortion_range=", unbounded_distortion_family())
    print("generated_posets_checked=", exhaustive_five_point_regression())
    print("PASS")
