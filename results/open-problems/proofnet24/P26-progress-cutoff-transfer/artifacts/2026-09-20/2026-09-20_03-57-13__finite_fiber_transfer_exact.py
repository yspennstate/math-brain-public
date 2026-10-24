from fractions import Fraction

def complete_graph_adj(n):
    return [[Fraction(0) if i == j else Fraction(1) for j in range(n)] for i in range(n)]

def cycle_adj(n):
    A = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        A[i][(i - 1) % n] = Fraction(1)
        A[i][(i + 1) % n] = Fraction(1)
    return A

def matmul(A, B):
    m, k, n = len(A), len(B), len(B[0])
    assert len(A[0]) == k
    return [[sum(A[i][h] * B[h][j] for h in range(k)) for j in range(n)] for i in range(m)]

def matlin(A, B, a=Fraction(1), b=Fraction(1)):
    return [[a * A[i][j] + b * B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def scale(A, c):
    return [[c * x for x in row] for row in A]

def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]

def row_kernel(A, degree):
    return [[x / Fraction(degree) for x in row] for row in A]

def check_case(base_name, fiber_name, A, F):
    n, r = len(A), len(F)
    d, s = int(sum(A[0])), int(sum(F[0]))
    assert all(sum(row) == d for row in A)
    assert all(sum(row) == s for row in F)

    N = n * r
    D = r * d + s
    P = row_kernel(A, d)
    W = row_kernel(F, s)

    # C projects (x,i) to x. U lifts x to a uniform point of its r-point fiber.
    C = [[Fraction(0) for _ in range(n)] for _ in range(N)]
    U = [[Fraction(0) for _ in range(N)] for _ in range(n)]
    for x in range(n):
        for i in range(r):
            z = x * r + i
            C[z][x] = Fraction(1)
            U[x][z] = Fraction(1, r)

    # Fiber walk W_hat.
    W_hat = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for x in range(n):
        for i in range(r):
            for j in range(r):
                W_hat[x * r + i][x * r + j] = W[i][j]

    T = matmul(matmul(C, P), U)
    a = Fraction(r * d, D)
    b = Fraction(s, D)
    Q = matlin(T, W_hat, a, b)

    # Direct SRW kernel on the lexicographic product G o F.
    Q_direct = [[Fraction(0) for _ in range(N)] for _ in range(N)]
    for x in range(n):
        for i in range(r):
            z = x * r + i
            for y in range(n):
                if A[x][y]:
                    for j in range(r):
                        Q_direct[z][y * r + j] = Fraction(1, D)
            for j in range(r):
                if F[i][j]:
                    Q_direct[z][x * r + j] = Fraction(1, D)

    assert Q == Q_direct
    assert matmul(U, C) == eye(n)
    assert matmul(W_hat, C) == C
    assert matmul(U, W_hat) == U
    assert matmul(T, W_hat) == T
    assert matmul(W_hat, T) == T

    # Exact projected generator identity: (Q-I) C = a C (P-I).
    lhs = matmul(matlin(Q, eye(N), Fraction(1), Fraction(-1)), C)
    rhs = scale(matmul(C, matlin(P, eye(n), Fraction(1), Fraction(-1))), a)
    assert lhs == rhs

    # The nominal tree branching base of the output is strictly larger
    # than the largest possible base-graph ball-growth base.
    assert D - 1 > d - 1

    print(
        f"{base_name} o {fiber_name}: n={n}, r={r}, d={d}, s={s}, "
        f"D={D}, a={a}, b={b}: EXACT_IDENTITIES_PASS"
    )

for case in [
    ("K4", "K2", complete_graph_adj(4), complete_graph_adj(2)),
    ("K5", "K3", complete_graph_adj(5), complete_graph_adj(3)),
    ("K4", "C4", complete_graph_adj(4), cycle_adj(4)),
]:
    check_case(*case)

print(
    "Checked: Q=aT+bW_hat; UC=I; W_hat C=C; U W_hat=U; "
    "T W_hat=W_hat T=T; (Q-I)C=a C(P-I); D-1>d-1."
)
print("P26_T08_FINITE_FIBER_TRANSFER_EXACT_PASS")
