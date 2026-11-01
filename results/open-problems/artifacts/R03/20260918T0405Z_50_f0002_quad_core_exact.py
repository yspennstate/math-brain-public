from itertools import product
from fractions import Fraction
from collections import Counter


def invert_matrix(A):
    n = len(A)
    M = [
        [Fraction(A[i][j]) for j in range(n)]
        + [Fraction(int(i == j)) for j in range(n)]
        for i in range(n)
    ]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c]), None)
        if p is None:
            return None
        M[c], M[p] = M[p], M[c]
        z = M[c][c]
        M[c] = [v / z for v in M[c]]
        for r in range(n):
            if r == c:
                continue
            z = M[r][c]
            if z:
                M[r] = [M[r][j] - z * M[c][j] for j in range(2 * n)]
    return [row[n:] for row in M]


def qform(x, C):
    n = len(x)
    return sum(
        Fraction(x[i]) * C[i][j] * x[j]
        for i in range(n)
        for j in range(n)
    )


def N(A):
    C = invert_matrix(A)
    if C is None:
        return None
    n = len(A)
    return sum(qform(x, C) in (1, -1) for x in product((-1, 1), repeat=n))


def symmetric_sign_matrices(n):
    ij = [(i, j) for i in range(n) for j in range(i, n)]
    for z in product((-1, 1), repeat=len(ij)):
        A = [[0] * n for _ in range(n)]
        for (i, j), v in zip(ij, z):
            A[i][j] = A[j][i] = v
        yield A


witness = None
for m in range(1, 5):
    distribution = Counter()
    for A in symmetric_sign_matrices(m):
        c = N(A)
        if c is not None:
            distribution[c] += 1
            if m == 4 and c == 12 and witness is None:
                witness = A
    print(
        f"m={m} invertible={sum(distribution.values())} "
        f"distribution={dict(sorted(distribution.items()))}"
    )

print("witness_m4_N12=")
for row in witness:
    print(" ".join(map(str, row)))
