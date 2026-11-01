from fractions import Fraction


def zeros(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def eye(n):
    M = zeros(n)
    for i in range(n):
        M[i][i] = Fraction(1)
    return M


def add(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A))] for i in range(len(A))]


def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]


def scale(c, A):
    return [[c * x for x in row] for row in A]


def mm(A, B):
    n, m, k = len(A), len(B[0]), len(B)
    C = [[Fraction(0) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for t in range(k):
            if A[i][t]:
                for j in range(m):
                    C[i][j] += A[i][t] * B[t][j]
    return C


def kron(A, B):
    na, ma = len(A), len(A[0])
    nb, mb = len(B), len(B[0])
    C = [[Fraction(0) for _ in range(ma * mb)] for _ in range(na * nb)]
    for i in range(na):
        for j in range(ma):
            for u in range(nb):
                for v in range(mb):
                    C[i * nb + u][j * mb + v] = A[i][j] * B[u][v]
    return C


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def k4():
    n = 4
    A = zeros(n)
    for i in range(n):
        for j in range(n):
            if i != j:
                A[i][j] = 1
    return A


def k33():
    n = 6
    A = zeros(n)
    for i in range(3):
        for j in range(3, 6):
            A[i][j] = A[j][i] = 1
    return A


def degree(A):
    return int(sum(A[0]))


def nbrw_kernels(A, R=6):
    n = len(A)
    d = degree(A)
    M = {0: eye(n), 1: A}
    M[2] = sub(mm(A, A), scale(Fraction(d), eye(n)))
    for r in range(3, R + 1):
        M[r] = sub(mm(A, M[r - 1]), scale(Fraction(d - 1), M[r - 2]))
    K = {}
    for r in range(1, R + 1):
        K[r] = scale(Fraction(1, d * (d - 1) ** (r - 1)), M[r])
    return d, K


def verify_collision(A, name):
    n = len(A)
    d, K = nbrw_kernels(A, 6)
    vals = []
    for r in range(1, 7):
        chi = Fraction(n) * sum(x * x for x in K[r][0]) - 1
        spec = trace(mm(K[r], K[r])) - 1
        assert chi == spec, (name, r, chi, spec)
        vals.append(str(chi))
    print(f"NBRW_TRACE_PASS {name} d={d} chi2_r1_to_r6={','.join(vals)}")


def verify_strong_product(A):
    n = len(A)
    d = degree(A)
    I = eye(n)
    AS = add(add(kron(A, I), kron(I, A)), kron(A, A))
    D = degree(AS)
    assert D == d * d + 2 * d
    P = scale(Fraction(1, d), A)
    Q = scale(Fraction(1, D), AS)
    alpha = Fraction(1, d + 2)
    beta = Fraction(d, d + 2)
    Qmix = add(add(scale(alpha, kron(P, I)), scale(alpha, kron(I, P))), scale(beta, kron(P, P)))
    assert Q == Qmix
    a = Fraction(d + 1, d + 2)
    R = zeros(n)
    y0 = 0
    for x in range(n):
        st = x * n + y0
        for xp in range(n):
            R[x][xp] = sum(Q[st][xp * n + yp] for yp in range(n))
    assert R == add(scale(1 - a, I), scale(a, P))
    q = d - 1
    assert q * q < D - 1
    print(f"STRONG_PRODUCT_PASS d={d} D={D} alpha={alpha} beta={beta} coordinate_rate={a} growth_base={q*q} lre_base={D-1}")


A = k4()
verify_strong_product(A)
verify_collision(A, "K4")
verify_collision(k33(), "K33")
print("ALL_EXACT_CHECKS_PASS")
