"""Recompute the four-state lumping family with exact arithmetic.

tmix (stopping-rule mixing time) = max_i max_j (E_i T_j - E_pi T_j)  (Lovasz-Winkler).
Discrete-time chain P(i,j) = w_ij / w_i with loops; lumped chain sums weights over blocks.
"""
from fractions import Fraction as F
import sys


def hitting(P, j):
    n = len(P)
    idx = [i for i in range(n) if i != j]
    m = len(idx)
    # (I - P restricted) h = 1
    A = [[(F(1) if a == b else F(0)) - P[idx[a]][idx[b]] for b in range(m)] + [F(1)] for a in range(m)]
    for c in range(m):
        p = next(r for r in range(c, m) if A[r][c] != 0)
        A[c], A[p] = A[p], A[c]
        piv = A[c][c]
        A[c] = [x / piv for x in A[c]]
        for r in range(m):
            if r != c and A[r][c] != 0:
                f = A[r][c]
                A[r] = [x - f * y for x, y in zip(A[r], A[c])]
    h = [F(0)] * n
    for a in range(m):
        h[idx[a]] = A[a][m]
    return h


def tmix(w):
    n = len(w)
    deg = [sum(r) for r in w]
    tot = sum(deg)
    pi = [d / tot for d in deg]
    P = [[w[i][j] / deg[i] for j in range(n)] for i in range(n)]
    best = F(0)
    for j in range(n):
        h = hitting(P, j)
        hp = sum(pi[i] * h[i] for i in range(n))
        best = max(best, max(h[i] - hp for i in range(n)))
    return best


def family(t):
    t = F(t)
    w = [[F(0)] * 4 for _ in range(4)]
    def s(i, j, v):
        w[i][j] = v; w[j][i] = v
    s(0, 2, F(1)); s(1, 2, F(1)); s(0, 3, t); s(1, 3, t)
    w[0][0] = t * t - 1; w[1][1] = t * t - 1; w[3][3] = t ** 6
    return w


def lump(w, blocks):
    k = len(blocks)
    return [[sum(w[i][j] for i in blocks[a] for j in blocks[b]) for b in range(k)] for a in range(k)]


for t in [2, 3, 10, 100, 10**6]:
    w = family(t)
    a = tmix(w)
    b = tmix(lump(w, [[0], [1], [2, 3]]))
    tt = F(t)
    W = tt**6 + 2 * tt**2 + 4 * tt + 2
    fa = (tt + 1) * (tt**6 + tt**5 + 4 * tt + 2) / W
    fb = 2 * tt * (tt**6 + tt**2 + 3 * tt + 2) / W
    print(t, "tmix X", float(a), a == fa, "tmix hX", float(b), b == fb, "ratio", float(b / a))
    sys.stdout.flush()
