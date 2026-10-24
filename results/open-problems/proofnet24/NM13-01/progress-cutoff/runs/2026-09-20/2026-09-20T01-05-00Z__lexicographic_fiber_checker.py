from fractions import Fraction


def complete_graph(n):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                A[i][j] = 1
    return A


def complete_bipartite(a, b):
    n = a + b
    A = [[0] * n for _ in range(n)]
    for i in range(a):
        for j in range(a, a + b):
            A[i][j] = A[j][i] = 1
    return A


def cycle_graph(n):
    A = [[0] * n for _ in range(n)]
    for i in range(n):
        A[i][(i - 1) % n] = 1
        A[i][(i + 1) % n] = 1
    return A


def degree(A):
    return sum(A[0])


def Fmat(A, den=1):
    return [[Fraction(x, den) for x in row] for row in A]


def I(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def kron(A, B):
    return [
        [A[i][j] * B[a][b] for j in range(len(A[0])) for b in range(len(B[0]))]
        for i in range(len(A))
        for a in range(len(B))
    ]


def mm(A, B):
    C = [[Fraction(0) for _ in range(len(B[0]))] for __ in range(len(A))]
    for i in range(len(A)):
        for k in range(len(B)):
            if A[i][k]:
                for j in range(len(B[0])):
                    C[i][j] += A[i][k] * B[k][j]
    return C


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def scale(c, A):
    return [[c * x for x in row] for row in A]


def maxabs(A):
    return max(abs(x) for row in A for x in row)


def verify(G, F, name):
    n, r = len(G), len(F)
    d, k = degree(G), degree(F)
    D = r * d + k
    alpha = Fraction(r * d, D)
    P = Fmat(G, d)
    PF = Fmat(F, k)
    Jr = [[Fraction(1) for _ in range(r)] for __ in range(r)]
    Pir = [[Fraction(1, r) for _ in range(r)] for __ in range(r)]
    Pi = kron(I(n), Pir)

    # Lexicographic-product adjacency and SRW kernel.
    AH = add(kron(Fmat(G), Jr), kron(I(n), Fmat(F)))
    Q = scale(Fraction(1, D), AH)

    # Exact lumped/base dynamics.
    base_eff = add(scale(alpha, P), scale(1 - alpha, I(n)))
    lifted_base = kron(base_eff, Pir)
    assert maxabs(sub(mm(Q, Pi), lifted_base)) == 0
    assert maxabs(sub(mm(Pi, Q), lifted_base)) == 0

    # Exact fiber generator on ker Pi:
    # (Q-I)|kerPi = -alpha I + (k/D)(PF-I).
    NN = n * r
    ker = sub(I(NN), Pi)
    QmI = sub(Q, I(NN))
    fiber_gen = add(
        scale(-alpha, I(NN)),
        scale(Fraction(k, D), kron(I(n), sub(PF, I(r)))),
    )
    assert maxabs(sub(mm(QmI, ker), mm(fiber_gen, ker))) == 0

    assert all(sum(row) == 1 for row in Q)
    assert D - 1 > d - 1

    print(f"{name}: PASS")
    print(f"  d={d}, r={r}, k={k}, D={D}, alpha={alpha}")
    print("  QPi=PiQ=lift[(1-alpha)I+alpha P]: PASS")
    print("  fiber-generator identity on ker(Pi): PASS")
    print(f"  fiber damping floor alpha={alpha}")
    print(f"  branching separation D-1={D-1} > d-1={d-1}")


verify(complete_graph(4), cycle_graph(4), "K4 o C4")
verify(complete_bipartite(3, 3), complete_graph(2), "K3,3 o K2")
print("ALL_EXACT_CHECKS_PASS")
