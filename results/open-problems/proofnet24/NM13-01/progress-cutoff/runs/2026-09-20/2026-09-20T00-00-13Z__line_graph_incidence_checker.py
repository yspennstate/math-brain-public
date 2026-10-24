#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations


def matmul(A, B):
    n, m = len(A), len(A[0])
    assert m == len(B)
    p = len(B[0])
    return [[sum(A[i][k] * B[k][j] for k in range(m))
             for j in range(p)] for i in range(n)]


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def scale(c, A):
    return [[c * x for x in row] for row in A]


def transpose(A):
    return [list(row) for row in zip(*A)]


def graph_data(n, edges):
    edges = [tuple(sorted(e)) for e in edges]
    m = len(edges)
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for u, v in edges:
        A[u][v] = A[v][u] = 1
    degrees = [sum(row) for row in A]
    assert len(set(degrees)) == 1
    d = int(degrees[0])

    B = [[Fraction(0) for _ in range(m)] for _ in range(n)]
    for j, (u, v) in enumerate(edges):
        B[u][j] = B[v][j] = 1

    AL = [[Fraction(0) for _ in range(m)] for _ in range(m)]
    for i, e in enumerate(edges):
        for j, f in enumerate(edges):
            if i != j and (set(e) & set(f)):
                AL[i][j] = 1
    return d, A, B, AL


def verify(name, n, edges):
    d, A, B, AL = graph_data(n, edges)
    m = len(edges)
    BT = transpose(B)

    # Incidence identities.
    assert matmul(B, BT) == add(A, scale(Fraction(d), eye(n)))
    assert matmul(BT, B) == add(AL, scale(Fraction(2), eye(m)))

    # C: edge -> uniform endpoint. D: vertex -> uniform incident edge.
    C = scale(Fraction(1, 2), BT)          # m x n
    D = scale(Fraction(1, d), B)           # n x m
    P = scale(Fraction(1, d), A)           # base SRW
    Q = scale(Fraction(1, 2 * (d - 1)), AL)  # line-graph SRW

    beta = Fraction(d, d - 1)
    R = matmul(C, D)
    S = matmul(D, C)

    # Core identities used in the proof.
    assert add(Q, scale(Fraction(-1), eye(m))) == \
           scale(beta, add(R, scale(Fraction(-1), eye(m))))
    assert S == scale(Fraction(1, 2), add(eye(n), P))

    # R^k = C S^(k-1) D for k >= 1.
    Rpow = eye(m)
    Spow = eye(n)
    for k in range(1, 7):
        Rpow = matmul(Rpow, R)
        if k > 1:
            Spow = matmul(Spow, S)
        assert Rpow == matmul(matmul(C, Spow), D)

    # Rate arithmetic: a=beta/2 and a*T=tau when T=(2*tau)/beta.
    a = beta / 2
    tau = Fraction(17, 5)  # arbitrary exact test value
    T = 2 * tau / beta
    assert a * T == tau

    # Line-graph LRE branching benchmark exceeds inherited ball-growth base.
    assert (d - 1) < (2 * d - 3)

    print(
        f"{name}: n={n}, m={m}, d={d}, line_degree={2*(d-1)}, "
        f"beta={beta}, a={a}; ALL_EXACT_IDENTITIES_PASS"
    )


if __name__ == "__main__":
    verify("K4", 4, list(combinations(range(4), 2)))
    verify("K3,3", 6, [(i, j) for i in range(3) for j in range(3, 6)])
    print("ALL_EXACT_CHECKS_PASS")
