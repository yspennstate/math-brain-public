from fractions import Fraction
from itertools import combinations


def matmul(A, B):
    n, m, k = len(A), len(B), len(B[0])
    return [
        [sum(A[i][r] * B[r][j] for r in range(m)) for j in range(k)]
        for i in range(n)
    ]


def trace(A):
    return sum(A[i][i] for i in range(len(A)))


def qform(y, Q):
    n = len(y)
    return sum(y[i] * Q[i][j] * y[j] for i in range(n) for j in range(n))


def falling(a, r):
    out = 1
    for i in range(r):
        out *= a - i
    return out


def build_q(n):
    # Deterministic rational symmetric matrix projected to 1^perp on both sides.
    B = [
        [Fraction((i + 1) * (j + 2) + (j + 1) * (i + 3), n + 3) for j in range(n)]
        for i in range(n)
    ]
    B = [[Fraction(B[i][j] + B[j][i], 2) for j in range(n)] for i in range(n)]
    H = [[Fraction(int(i == j), 1) - Fraction(1, n) for j in range(n)] for i in range(n)]
    Q = matmul(matmul(H, B), H)
    assert all(sum(row) == 0 for row in Q)
    return Q


def exact_case(n, d):
    Q = build_q(n)
    vals = []
    for S in combinations(range(n), d):
        y = [Fraction(0) for _ in range(n)]
        for i in S:
            y[i] = Fraction(1)
        vals.append(qform(y, Q))

    EZ = sum(vals, Fraction(0)) / len(vals)
    EZ2 = sum(v * v for v in vals) / len(vals)

    p = [Fraction(1)]
    for r in range(1, 5):
        p.append(Fraction(falling(d, r), falling(n, r)) if d >= r else Fraction(0))
    p1, p2, p3, p4 = p[1:]

    tau = trace(Q)
    tr2 = sum(Q[i][j] * Q[j][i] for i in range(n) for j in range(n))
    diag2 = sum(Q[i][i] * Q[i][i] for i in range(n))

    a = p1 - p2
    formula_E = a * tau
    formula_E2 = (
        (p2 - 2 * p3 + p4) * tau * tau
        + (2 * p2 - 4 * p3 + 2 * p4) * tr2
        + (p1 - 7 * p2 + 12 * p3 - 6 * p4) * diag2
    )

    assert EZ == formula_E
    assert EZ2 == formula_E2
    return EZ, EZ2


if __name__ == "__main__":
    cases = [(5, 1), (5, 2), (6, 2), (6, 3), (7, 2), (7, 3)]
    for n, d in cases:
        EZ, EZ2 = exact_case(n, d)
        print(f"n={n} d={d} E={EZ} E2={EZ2} PASS")
    print("ALL_EXACT_CHECKS_PASS = True")
