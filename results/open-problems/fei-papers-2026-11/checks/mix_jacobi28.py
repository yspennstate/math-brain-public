"""Mixing moment s_14 and Jacobi increments b_k^2 with m_28 (Chebyshev algorithm, exact)."""
from fractions import Fraction as F
from math import comb
T = {0: F(1), 2: F(1), 4: F(8, 3), 6: F(11), 8: F(908, 15), 10: F(415),
     12: F(23840, 7), 14: F(325719, 10), 16: F(112135066, 315), 18: F(3065263961, 700),
     20: F(69174280444, 1155), 22: F(5680684105259, 6300),
     24: F(1112571762134554, 75075), 26: F(2032842751996209, 7700),
     28: F(1141293103886559392, 225225)}
cat = lambda k: comb(2 * k, k) // (k + 1)
print("s_13 =", T[26] / cat(13), " s_14 =", T[28] / cat(14))
# symmetric law: Hankel determinants D_n of (m_{i+j}); b_n^2 = D_{n+1} D_{n-1} / D_n^2
m = [T.get(n, F(0)) for n in range(29)]

def det(M):
    M = [r[:] for r in M]; n = len(M); d = F(1)
    for i in range(n):
        p = next(r for r in range(i, n) if M[r][i] != 0)
        if p != i:
            M[i], M[p] = M[p], M[i]; d = -d
        d *= M[i][i]
        for r in range(i + 1, n):
            f = M[r][i] / M[i][i]
            for c in range(i, n):
                M[r][c] -= f * M[i][c]
    return d

D = [F(1)] + [det([[m[i + j] for j in range(n)] for i in range(n)]) for n in range(1, 16)]
b2 = [D[n + 1] * D[n - 1] / D[n] ** 2 for n in range(1, 15)]
print("b^2:", [float(x) for x in b2])
print("increments:", [f"{float(b2[i+1]-b2[i]):.5f}" for i in range(len(b2) - 1)])
