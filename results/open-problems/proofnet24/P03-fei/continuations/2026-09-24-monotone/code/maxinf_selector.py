# Does restricting on the coordinate of MAXIMAL influence give Delta <= K Inf for monotone functions?
# Construction (the monotone analogue of F4's Proposition 6.2): F_n(y,z) = Maj_n(y) OR (z AND [y = y*]), y* with (n-1)/2
# ones, is monotone and its coordinate z has Inf_z = 2^-n and B_z/Inf_z >= (n - 3 log2 n)/2 (F4, Proposition 6.1).
# Replace each y_j by Maj_k of fresh variables.  The composition is monotone, B_z and Inf_z do not change (F4,
# Theorem 3.1: the inner functions are balanced and odd), and every y-leaf has influence Inf_{y_j}(F_n) * iota_k with
# iota_k = C(k-1,(k-1)/2) 2^(1-k).  Once iota_k < 2^-n / max_j Inf_{y_j}(F_n), z is the unique coordinate of maximal
# influence.  This script (a) computes B_z/Inf_z and Delta_z/Inf_z exactly for F_n, (b) checks by brute force, for n = 3
# and k = 3, that the composition leaves Delta_z and Inf_z of the coordinate z unchanged, and (c) reports the k at
# which z becomes the maximal-influence coordinate.
import itertools, math, numpy as np
from mono_enum import phi

def wht(v):
    G = v.astype(np.float64).copy(); N = len(G); h = 1
    while h < N:
        G = G.reshape(N // (2 * h), 2, h); a = G[:, 0, :].copy(); b = G[:, 1, :]
        G[:, 0, :] = a + b; G[:, 1, :] = a - b; G = G.reshape(N); h *= 2
    return G / N

def coord(c, nvar, i):
    S = np.arange(1 << nvar); lo = S[((S >> i) & 1) == 0]; hi = lo | (1 << i)
    u, v = c[lo], c[hi]
    inf = float((v * v).sum())
    B = float((phi(u * u) + phi(v * v) - phi(u * u + v * v)).sum())
    H = float(phi(c * c).sum())
    delta = H - 0.5 * float((phi((u + v) ** 2) + phi((u - v) ** 2)).sum())
    return inf, B, delta

def F_table(n):
    ystar = [1] * ((n - 1) // 2) + [0] * ((n + 1) // 2)
    tt = np.zeros(1 << (n + 1))
    for x in range(1 << (n + 1)):
        y = [(x >> t) & 1 for t in range(n)]; z = (x >> n) & 1
        val = (sum(y) > n // 2) or (z == 1 and y == ystar)
        tt[x] = 1.0 - 2.0 * val
    return tt

print('(a) the flip coordinate z of F_n: Inf_z, B_z/Inf_z, Delta_z/Inf_z, and the largest influence of a y-coordinate')
for n in [3, 5, 7, 9, 11, 13, 15]:
    c = wht(F_table(n))
    inf, B, d = coord(c, n + 1, n)
    maxy = max(coord(c, n + 1, j)[0] for j in range(n))
    print('  n %2d: Inf_z = %.3e  B_z/Inf_z = %.4f  Delta_z/Inf_z = %.4f  max_j Inf_yj = %.4f' % (n, inf, B / inf, d / inf, maxy), flush=True)

print('(b) brute-force composition check, n = 3, each y_j replaced by Maj_3 of fresh variables (10 variables)')
n, k = 3, 3
ystar = [1] * ((n - 1) // 2) + [0] * ((n + 1) // 2)
nv = n * k + 1
tt = np.zeros(1 << nv)
for x in range(1 << nv):
    w = [(x >> t) & 1 for t in range(nv)]
    y = [int(sum(w[j * k:(j + 1) * k]) > k // 2) for j in range(n)]; z = w[n * k]
    tt[x] = 1.0 - 2.0 * ((sum(y) > n // 2) or (z == 1 and y == ystar))
c2 = wht(tt)
infz2, Bz2, dz2 = coord(c2, nv, n * k)
c1 = wht(F_table(n)); infz1, Bz1, dz1 = coord(c1, n + 1, n)
print('  F_3:        Inf_z %.6f  B_z %.6f  Delta_z %.6f' % (infz1, Bz1, dz1))
print('  composed:   Inf_z %.6f  B_z %.6f  Delta_z %.6f' % (infz2, Bz2, dz2))
leaf = max(coord(c2, nv, t)[0] for t in range(n * k))
print('  largest leaf influence in the composition %.6f (= Inf_yj(F_3) * iota_3 = %.6f)' % (leaf, max(coord(c1, n + 1, j)[0] for j in range(n)) * 0.5))

print('(c) Maj_k size at which z becomes the unique maximal-influence coordinate')
for n in [11, 15, 21, 31]:
    maxy = math.comb(n - 1, (n - 1) // 2) * 2.0 ** (1 - n) + 2.0 ** -n   # a y-coordinate's influence in F_n is at most Maj_n's plus the flip
    kmin = (2 / math.pi) * maxy ** 2 * 4.0 ** n                           # iota_k <= sqrt(2/(pi k)) for odd k >= 3
    lower = (n - 3 * math.log2(n)) / 2
    print('  n %2d: any odd k > %.3g suffices; then Delta_z/Inf_z >= B_z/Inf_z >= %.2f at the maximal-influence coordinate' % (n, kmin, lower))
