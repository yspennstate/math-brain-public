"""Check the form of Gval in terms of N = lam Pi - L_G (GAP_STATE_FORM.md).

For a weighted graph with top eigenvector x (eigenvalue lam), N = lam Pi - L_G is positive semidefinite, kills 1 and
x, and w_ij = N_ij + lam/n for i != j.  With tau = tr N, t = sum_i x_i^2 N_ii:
    Gval/(n-2) = a lam + b,
    a = (2(n-1)/n) (tau - (2n/(n-2)) t),
    b = - tr N^2 - tau^2/(n-2) + (2n/(n-2)^2) tau t + (2n/(n-2)) sum_ij x_i x_j N_ij^2
        - 2 sum_{i<j} N_ij d_ij^2 (N_ii + N_jj - 2 N_ij).
Also checks a >= 0 and the identity  sum_{i<j} d_ij^2 (N_ii + N_jj - 2 N_ij) = n t + tau.
usage: gapN_check.py trials seed
"""
import sys
import numpy as np
from canon_spectral import build
from canon_gap import gval


def main():
    trials, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(seed)
    worst = worst_id = 0.0
    amin = float("inf")
    for _ in range(trials):
        n = int(rng.integers(4, 10))
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        w = rng.uniform(0, 1, len(pairs)) * (rng.uniform(0, 1, len(pairs)) < rng.uniform(0.3, 1))
        if w.sum() <= 0:
            continue
        w = w / w.sum()
        L, ev, U, x, M = build(w, n, pairs)
        lam = ev[-1]
        N = lam * (np.eye(n) - 1.0 / n) - L
        tau = np.trace(N)
        t = float((x * x * np.diag(N)).sum())
        a = (2 * (n - 1.0) / n) * (tau - (2 * n / (n - 2.0)) * t)
        s3 = 0.0
        ident = 0.0
        for (i, j) in pairs:
            d2 = (x[i] - x[j]) ** 2
            nf = N[i, i] + N[j, j] - 2 * N[i, j]
            s3 += N[i, j] * d2 * nf
            ident += d2 * nf
        b = -np.trace(N @ N) - tau ** 2 / (n - 2.0) + (2 * n / (n - 2.0) ** 2) * tau * t \
            + (2 * n / (n - 2.0)) * float((np.outer(x, x) * N * N).sum()) - 2 * s3
        worst = max(worst, abs((a * lam + b) - gval(w, n, pairs)[0] / (n - 2.0)))
        worst_id = max(worst_id, abs(ident - (n * t + tau)))
        amin = min(amin, a)
    print("Gval/(n-2) = a lam + b: largest deviation %.2e; identity: %.2e; smallest a: %.4f (%d graphs, n = 4..9, W = 1)"
          % (worst, worst_id, amin, trials))


if __name__ == "__main__":
    main()
