"""Check the expanded inequality of HOOKS_AND_TWO_ROWS.md section 5 (d) against Gval of canon_gap.py.

    lhs = (n-2)(n-5) lam^2 + 2 lam^2 - (n-2) tr L^2 + 2(n-2) P + 4(n-2) S - 2n lam A + 2n tr(D L D L)
    rhs = tau^2 - (2n/(n-2)) tau (lam (n-1)/n - A)
    Gval = lhs - rhs
with tau = (n-1) lam - 2W, A = sum_i deg_i x_i^2, P = sum_{i<j} w_ij d_ij^2 (deg_i + deg_j), S = sum w_ij^2 d_ij^2.
usage: gap_form_check.py trials seed
"""
import sys
import numpy as np
from canon_spectral import build
from canon_gap import gval


def main():
    trials, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(seed)
    worst = 0.0
    for t in range(trials):
        n = int(rng.integers(4, 10))
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        w = rng.uniform(0, 1, len(pairs)) * (rng.uniform(0, 1, len(pairs)) < rng.uniform(0.3, 1))
        if w.sum() <= 0:
            continue
        w = w / w.sum()
        L, ev, U, x, M = build(w, n, pairs)
        lam, W = ev[-1], 1.0
        deg = np.diag(L).copy()
        D = np.diag(x)
        A = float((deg * x * x).sum())
        P = sum(v * (x[i] - x[j]) ** 2 * (deg[i] + deg[j]) for (i, j), v in zip(pairs, w))
        S = sum(v * v * (x[i] - x[j]) ** 2 for (i, j), v in zip(pairs, w))
        tau = (n - 1) * lam - 2 * W
        lhs = (n - 2) * (n - 5) * lam ** 2 + 2 * lam ** 2 - (n - 2) * np.trace(L @ L) + 2 * (n - 2) * P \
            + 4 * (n - 2) * S - 2 * n * lam * A + 2 * n * np.trace(D @ L @ D @ L)
        rhs = tau ** 2 - (2 * n / (n - 2.0)) * tau * (lam * (n - 1.0) / n - A)
        worst = max(worst, abs((lhs - rhs) - gval(w, n, pairs)[0]))
    # the unit star, both sides
    for n in (5, 6, 9):
        pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
        w = np.array([1.0 if i == 0 else 0.0 for (i, j) in pairs])
        L, ev, U, x, M = build(w, n, pairs)
        lam, W = ev[-1], w.sum()
        deg = np.diag(L).copy()
        A = float((deg * x * x).sum())
        tau = (n - 1) * lam - 2 * W
        rhs = tau ** 2 - (2 * n / (n - 2.0)) * tau * (lam * (n - 1.0) / n - A)
        print("unit star n=%d: rhs %.6f, n(n-1)(n-2)(n-3) = %d" % (n, rhs, n * (n - 1) * (n - 2) * (n - 3)))
    print("expanded inequality against Gval: largest deviation %.2e over %d random weighted graphs, n = 4..9" % (worst, trials))


if __name__ == "__main__":
    main()
