from fractions import Fraction as F
def inv2(a):
    d = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return [[a[1][1] / d, -a[0][1] / d], [-a[1][0] / d, a[0][0] / d]], d

def invariant(G, P):
    n = 5
    tau = sum(G[i][i] for i in range(n))
    M = sum(P[i][i] * G[i][i] for i in range(n))
    diag2 = sum(G[i][i] ** 2 for i in range(n))
    tr2 = sum(G[i][j] ** 2 for i in range(n) for j in range(n))
    QS = sum(P[i][i] * sum(G[i][j] ** 2 for j in range(n)) for i in range(n))
    Rr = sum(P[i][j] * G[i][j] ** 2 for i in range(n) for j in range(n))
    Rr += 2 * sum(P[i][i] * G[i][j] * G[j][j] for i in range(n) for j in range(n))
    return F(9, 80) + (11 * M - 2 * tau) / 8 + (100 * tau * M - 320 * diag2 - 1280 * QS
                                               + 448 * tr2 - 33 * tau * tau) / 320 + Rr

