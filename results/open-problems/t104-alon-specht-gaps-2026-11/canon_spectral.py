"""Primal form of Reduction R with a test vector taken from the graph (HOOKS_AND_TWO_ROWS.md section 5).

For a weighted graph G (total weight W) with top Laplacian eigenvector x (eigenvalue lam), summing (*) over pairs
with the weights gives a quadratic form in y on {1, x}^perp:
    M = (2W - lam) I + (2n/(n-2)) ((n-1) lam - 2W) D^2 - 2n D L D - (n-2) (2 L2 - L),
D = diag(x), L2 the Laplacian with weights w_ij (x_i - x_j)^2.  If y^t M y >= 0 for one y in {1, x}^perp then
Conjecture F holds for G.  The script draws weights, compresses M to the other eigenvectors u_1..u_(n-2) of L
(ascending eigenvalues) and records the smallest value over the sample of
    top eigenvalue of the compression; its trace (the uniform state); y^t M y for y = u_1, y = u_(n-2), the best u_k;
    spectral traces sum_k f(lam_k) u_k^t M u_k for a few f.
All with W = 1.
usage: canon_spectral.py n samples seed
"""
import sys
import numpy as np


def build(w, n, pairs):
    L = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        L[i, i] += v; L[j, j] += v; L[i, j] -= v; L[j, i] -= v
    W = w.sum()
    # the constant vector is pushed to the bottom so that index 0 is always it, also for disconnected graphs
    ev, U = np.linalg.eigh(L - 10.0 * W * np.ones((n, n)) / n)
    x = U[:, -1]
    lam = ev[-1]
    D = np.diag(x)
    L2 = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        t = v * (x[i] - x[j]) ** 2
        L2[i, i] += t; L2[j, j] += t; L2[i, j] -= t; L2[j, i] -= t
    M = (2 * W - lam) * np.eye(n) + (2 * n / (n - 2.0)) * ((n - 1) * lam - 2 * W) * D @ D - 2 * n * D @ L @ D \
        - (n - 2) * (2 * L2 - L)
    return L, ev, U, x, M


def check_against_star(n, rng, pairs):
    """y^t M y against the weighted sum of (*) computed entry by entry."""
    w = rng.uniform(0, 1, len(pairs)); w /= w.sum()
    L, ev, U, x, M = build(w, n, pairs)
    y = U[:, 1 + rng.integers(0, n - 2)]
    C = np.outer(y, y)
    dg = np.diag(C); kappa = float((x * x * dg).sum())
    tot = 0.0
    for (i, j), v in zip(pairs, w):
        d2 = (x[i] - x[j]) ** 2
        cij = (y[i] - y[j]) ** 2
        gij = (x[i] * y[i] - x[j] * y[j]) ** 2
        tot += v * ((2 - d2) + (2 * n * kappa / (n - 2.0)) * ((n - 1) * d2 - 2) - 2 * n * gij - (n - 2) * (2 * d2 - 1) * cij)
    return abs(tot - y @ M @ y)


def main():
    n, samples, seed = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    rng = np.random.default_rng(seed)
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    m = len(pairs)
    print("n=%d formula check: largest deviation %.1e" % (n, max(check_against_star(n, rng, pairs) for _ in range(50))))
    names = ["top eigenvalue", "trace (uniform)", "y=u_1 (Fiedler)", "y=u_(n-2) (second top)", "best u_k",
             "f=lam_k", "f=lam-lam_k", "f=1/(lam-lam_k)", "f=1/lam_k"]
    worst = {k: (float("inf"), None) for k in names}
    used = 0
    for s in range(samples):
        kind = s % 5
        if kind == 0:
            w = rng.uniform(0, 1, m)
        elif kind == 1:
            w = np.exp(rng.normal(0, 2.5, m))
        elif kind == 2:
            w = rng.uniform(0, 1, m) * (rng.uniform(0, 1, m) < 0.4)
        elif kind == 3:
            w = np.array([1.0 if i == 0 else 0.0 for (i, j) in pairs]) + 0.2 * rng.uniform(0, 1, m) ** 3
        else:
            w = (rng.uniform(0, 1, m) < 0.35) * 1.0
        if w.sum() <= 0:
            continue
        w = w / w.sum()
        L, ev, U, x, M = build(w, n, pairs)
        if ev[-1] - ev[-2] < 1e-6:
            continue
        used += 1
        B = U[:, 1:n - 1]
        lk = ev[1:n - 1]
        Mc = B.T @ M @ B
        q = np.diag(Mc)
        gap = ev[-1] - lk
        vals = {
            "top eigenvalue": np.linalg.eigvalsh(Mc)[-1],
            "trace (uniform)": q.sum() / (n - 2),
            "y=u_1 (Fiedler)": q[0],
            "y=u_(n-2) (second top)": q[-1],
            "best u_k": q.max(),
            "f=lam_k": (q * lk).sum() / lk.sum() if lk.sum() > 1e-12 else 0.0,
            "f=lam-lam_k": (q * gap).sum() / gap.sum(),
            "f=1/(lam-lam_k)": (q / gap).sum() / (1 / gap).sum(),
            "f=1/lam_k": (q / np.maximum(lk, 1e-9)).sum() / (1 / np.maximum(lk, 1e-9)).sum(),
        }
        for k, v in vals.items():
            if v < worst[k][0]:
                worst[k] = (float(v), w.copy())
    print("n=%d, %d weightings with a simple top eigenvalue; smallest value of each quantity:" % (n, used))
    for k in names:
        v, w = worst[k]
        tag = " ".join("%d%d:%.3f" % (p[0] + 1, p[1] + 1, a) for p, a in zip(pairs, w) if a > 5e-3) if v < -1e-9 else ""
        print("  %-24s %+.6f  %s" % (k, v, tag[:110]))


if __name__ == "__main__":
    main()
