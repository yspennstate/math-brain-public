from fractions import Fraction
from itertools import combinations


def zeros(r, c):
    return [[Fraction(0) for _ in range(c)] for __ in range(r)]


def eye(n):
    M = zeros(n, n)
    for i in range(n):
        M[i][i] = Fraction(1)
    return M


def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def matsub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def matscale(a, A):
    return [[a*x for x in row] for row in A]


def matmul(A, B):
    r, k, c = len(A), len(B), len(B[0])
    assert len(A[0]) == k
    return [[sum((A[i][z]*B[z][j] for z in range(k)), Fraction(0))
             for j in range(c)] for i in range(r)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def graph_mats(n, edges):
    A = zeros(n, n)
    for u, v in edges:
        A[u][v] = A[v][u] = Fraction(1)
    m = len(edges)
    B = zeros(n, m)
    for j, (u, v) in enumerate(edges):
        B[u][j] = B[v][j] = Fraction(1)
    AL = zeros(m, m)
    for i, e in enumerate(edges):
        for j in range(i + 1, m):
            if set(e) & set(edges[j]):
                AL[i][j] = AL[j][i] = Fraction(1)
    return A, B, AL


def allzero(A):
    return all(x == 0 for row in A for x in row)


def check_complete(n):
    edges = list(combinations(range(n), 2))
    d = n - 1
    A, B, AL = graph_mats(n, edges)
    BT = transpose(B)
    P = matscale(Fraction(1, d), A)
    Q = matscale(Fraction(1, 2*(d-1)), AL)
    K = matscale(Fraction(1, 2), BT)  # edge -> uniformly chosen endpoint
    J = matscale(Fraction(1, d), B)   # vertex -> uniformly chosen incident edge
    b = Fraction(d, 2*(d-1))
    c = Fraction(d, d-1)

    assert matmul(B, BT) == matadd(matscale(Fraction(d), eye(n)), A)
    assert matmul(BT, B) == matadd(matscale(Fraction(2), eye(len(edges))), AL)

    generator_intertwining = matsub(
        matmul(matsub(Q, eye(len(edges))), K),
        matscale(b, matmul(K, matsub(P, eye(n))))
    )
    assert allzero(generator_intertwining)

    heatbath_factorization = matsub(
        matsub(Q, eye(len(edges))),
        matscale(c, matsub(matmul(K, J), eye(len(edges))))
    )
    assert allzero(heatbath_factorization)

    lazy_vertex_factorization = matsub(
        matmul(J, K),
        matscale(Fraction(1, 2), matadd(eye(n), P))
    )
    assert allzero(lazy_vertex_factorization)

    print(
        f"K_{n}: d={d}, m={len(edges)}, "
        f"BBt=PASS BtB=PASS generator=PASS heatbath=PASS lazy=PASS "
        f"b={b} c={c}"
    )


print("P26 T08 line-graph exact sanity check")
for n in (4, 5, 6):
    check_complete(n)

print("LRE branching-base obstruction ratios")
for d in range(3, 11):
    ratio = Fraction(d-1, 2*d-3)
    assert ratio < 1
    print(f"d={d}: (d-1)/(2d-3)={ratio} < 1 PASS")

print("P26_T08_LINE_GRAPH_TRANSFER_EXACT_PASS")
