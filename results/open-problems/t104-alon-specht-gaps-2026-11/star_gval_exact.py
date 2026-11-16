"""Exact value of the gap-weighted state at the top eigenvector on K_{1,k} plus n-1-k isolated vertices (W = 1).

Uses the closed form of GAP_STATE_FORM.md (sections "Setting" and "The inequality"):

    N = lam Pi - L_G,  tau = tr N,  t = sum_i x_i^2 N_ii,  d_ij = x_i - x_j,
    Gval/(n-2) = a lam + b,
    a = (2(n-1)/n)(tau - (2n/(n-2)) t),
    b = - tr N^2 - tau^2/(n-2) + (2n/(n-2)^2) tau t + (2n/(n-2)) sum_{i,j} x_i x_j N_ij^2
        - 2 sum_{i<j} N_ij d_ij^2 (N_ii + N_jj - 2 N_ij),
    s(G, top x) = Gval / (tau - (2n/(n-2)) t)        (the denominator is the trace of the unnormalised state).

Rational arithmetic throughout: x = v / sqrt(k^2 + k) with v = (k, -1, ..., -1, 0, ..., 0), and x enters only
through products of two coordinates.

usage: star_gval_exact.py NMIN NMAX
"""
import sys
from fractions import Fraction as Fr


def value(n, k):
    v = [k] + [-1] * k + [0] * (n - 1 - k)
    c = Fr(1, k * k + k)                      # x_i x_j = c v_i v_j
    w = [[Fr(0)] * n for _ in range(n)]
    for j in range(1, k + 1):
        w[0][j] = w[j][0] = Fr(1, k)
    L = [[(sum(w[i]) if i == j else -w[i][j]) for j in range(n)] for i in range(n)]
    lam = Fr(k + 1, k)
    # check: L v = lam v
    assert all(sum(L[i][j] * v[j] for j in range(n)) == lam * v[i] for i in range(n))
    N = [[lam * ((1 if i == j else 0) - Fr(1, n)) - L[i][j] for j in range(n)] for i in range(n)]
    tau = sum(N[i][i] for i in range(n))
    assert tau == (n - 1) * lam - 2
    t = sum(c * v[i] * v[i] * N[i][i] for i in range(n))
    trN2 = sum(N[i][j] * N[i][j] for i in range(n) for j in range(n))
    sx = sum(c * v[i] * v[j] * N[i][j] * N[i][j] for i in range(n) for j in range(n))
    pr = sum(N[i][j] * c * (v[i] - v[j]) ** 2 * (N[i][i] + N[j][j] - 2 * N[i][j]) for i in range(n) for j in range(i + 1, n))
    norm = tau - Fr(2 * n, n - 2) * t
    a = Fr(2 * (n - 1), n) * norm
    b = -trN2 - tau * tau / (n - 2) + Fr(2 * n, (n - 2) ** 2) * tau * t + Fr(2 * n, n - 2) * sx - 2 * pr
    gval = (n - 2) * (a * lam + b)
    return gval / norm if norm != 0 else None, gval, norm


def main():
    nmin, nmax = int(sys.argv[1]), int(sys.argv[2])
    worst = None
    for n in range(nmin, nmax + 1):
        row = []
        for k in range(1, n):
            s, g, nm = value(n, k)
            row.append((k, s))
            if s is not None and 1 < k < n - 1 and (worst is None or s < worst[0]):
                worst = (s, n, k)
        neg = [k for k, s in row if s is not None and s < 0]
        if n <= 12:
            print("n = %2d: " % n + "  ".join("k=%d: %s" % (k, s) for k, s in row))
        mid = [(s, k) for k, s in row if s is not None and 1 < k < n - 1]
        print("n = %2d: negative at k = %s; smallest for 1 < k < n-1: %s = %.6f at k = %d"
              % (n, neg if neg else "none", min(mid)[0], float(min(mid)[0]), min(mid)[1]))
    print("smallest over the range for 1 < k < n-1: %s = %.6f at n = %d, k = %d" % (worst[0], float(worst[0]), worst[1], worst[2]))


if __name__ == "__main__":
    main()
