"""n = 5, Conjecture F near a double top Laplacian eigenvalue: states built from the top two-plane.

Conjecture F for a weighted graph G on n vertices (W = total weight, lam = lambda_max(L_G)):

    slack(G) = (n-2) lambda_max(G, [n-2,2]) - (n-1) lam + 2W >= 0.

Any density matrix D on V_[n-2,2] gives lambda_max(G, [n-2,2]) >= tr(D L(G, [n-2,2])).  For a unit vector x with
sum zero let N_x be the positive part of Q (x^t L x Pi - L_G) Q, Q the projection onto {1, x}^perp, with eigenpairs
(g_k, y_k), and

    D_x = sum_k g_k a_k a_k^t / trace,   a_k = the [n-2,2] component of (x y_k^t + y_k x^t)/sqrt 2.

For x the top eigenvector this is the gap-weighted state of GAP_STATE_FORM.md, and (n-2) tr(D_x L) - (n-1) lam + 2W
has the sign of Gval.  gval_n5_check2.out found Gval < 0 next to two graphs with a double top eigenvalue.  This script
recomputes that with an explicit model of V_[3,2] (no formula for Gval is used) and asks whether some x in the plane
of the top two eigenvectors, or some state supported on the vectors a(x, y) with x in that plane, restores the bound.

Model of V_[n-2,2]: symmetric n x n matrices with zero diagonal and zero row sums, S_n acting by conjugation.
"""
import sys
import numpy as np

n = 5
pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
idx = {p: k for k, p in enumerate(pairs)}
CASES = [
    "12:0.00007132 13:0.02226662 14:0.20735806 15:0.20834156 23:0.30343969 24:0.00292157 25:0.00121865 "
    "34:0.02462748 35:0.02321798 45:0.20653708",
    "12:0.21210057 13:0.21352633 14:0.01393605 15:0.00089872 23:0.21228140 24:0.01567941 25:0.00283654 "
    "34:0.01366421 35:0.00059663 45:0.31448014",
]


def from_text(s):
    w = np.zeros(len(pairs))
    for tok in s.split():
        a, v = tok.split(":")
        w[idx[(int(a[0]) - 1, int(a[1]) - 1)]] = float(v)
    return w


def lap(w):
    L = np.zeros((n, n))
    for (i, j), v in zip(pairs, w):
        L[i, i] += v; L[j, j] += v; L[i, j] -= v; L[j, i] -= v
    return L


def basis32():
    rows = []
    for i in range(n):
        for j in range(n):
            if i < j:
                r = np.zeros((n, n)); r[i, j] = 1; r[j, i] = -1; rows.append(r.ravel())   # symmetry
        r = np.zeros((n, n)); r[i, i] = 1; rows.append(r.ravel())                         # zero diagonal
        r = np.zeros((n, n)); r[i, :] = 1; rows.append(r.ravel())                         # zero row sums
    A = np.array(rows)
    u, s, vt = np.linalg.svd(A)
    rank = int((s > 1e-10).sum())
    B = vt[rank:].T                                                                       # n^2 x dim, orthonormal
    assert B.shape[1] == n * (n - 3) // 2, B.shape
    return B


B = basis32()
SWAP = {}
for (i, j) in pairs:
    P = np.eye(n); P[[i, j]] = P[[j, i]]
    R = np.kron(P, P)                               # vec(P T P^t) = (P kron P) vec(T), row-major, P symmetric
    SWAP[(i, j)] = B.T @ R @ B
    assert np.allclose(SWAP[(i, j)] @ SWAP[(i, j)], np.eye(B.shape[1]), atol=1e-10)


def L32(w):
    d = B.shape[1]
    out = np.zeros((d, d))
    for p, v in zip(pairs, w):
        out += v * (np.eye(d) - SWAP[p])
    return out


def comp32(x, y):
    return B.T @ ((np.outer(x, y) + np.outer(y, x)) / np.sqrt(2.0)).ravel()


def state(L, x):
    """D_x and its vectors; x a unit vector with sum zero."""
    Pi = np.eye(n) - 1.0 / n
    Q = Pi - np.outer(x, x)
    Nx = Q @ (float(x @ L @ x) * Pi - L) @ Q
    g, Y = np.linalg.eigh((Nx + Nx.T) / 2)
    vecs = [np.sqrt(gk) * comp32(x, Y[:, k]) for k, gk in enumerate(g) if gk > 1e-13]
    D = sum(np.outer(a, a) for a in vecs)
    return D / np.trace(D)


def report(w, label):
    w = w / w.sum()
    L = lap(w)
    ev, U = np.linalg.eigh(L)
    lam, gap = ev[-1], ev[-1] - ev[-2]
    u1, u2 = U[:, -1], U[:, -2]
    M = L32(w)
    need = (n - 1) * lam - 2.0
    direct = (n - 2) * np.linalg.eigvalsh(M)[-1] - need
    top = (n - 2) * float(np.trace(state(L, u1) @ M)) - need
    ts = np.linspace(0, np.pi, 1441)
    vals = np.array([(n - 2) * float(np.trace(state(L, np.cos(t) * u1 + np.sin(t) * u2) @ M)) - need for t in ts])
    k = int(vals.argmax())
    # every state supported on the vectors a(x, y), x in the top two-plane, y in V
    Pi = np.eye(n) - 1.0 / n
    span = np.array([comp32(u, Pi[:, c]) for u in (u1, u2) for c in range(n)]).T
    q, s, _ = np.linalg.svd(span, full_matrices=False)
    q = q[:, s > 1e-10]
    sub = (n - 2) * np.linalg.eigvalsh(q.T @ M @ q)[-1] - need
    print("%-12s gap %.3e  direct %+.6e  top-x state %+.6e  best x in plane %+.6e (angle %.3f)  plane-supported %+.6e (dim %d)"
          % (label, gap, direct, top, vals[k], ts[k], sub, q.shape[1]))
    return vals, ts, u1, u2


def main():
    for c, s in enumerate(CASES, 1):
        w = from_text(s); w = w / w.sum()
        print("graph %d" % c)
        vals, ts, u1, u2 = report(w, "base")
        k = int(vals.argmin())
        xw = np.cos(ts[k]) * u1 + np.sin(ts[k]) * u2
        print("   on the circle of the top two-plane: min %+.6e, max %+.6e, fraction below 0: %.3f"
              % (vals.min(), vals.max(), float((vals < 0).mean())))
        H = np.array([max(0.0, -xw[i] * xw[j]) for (i, j) in pairs])
        for delta in (1e-6, 1e-5, 1e-4, 3e-4, 1e-3, 1e-2):
            report(w + delta * H, "w+%.0eH" % delta)
        rng = np.random.default_rng(5 + c)
        worst = None
        for trial in range(400):
            wp = np.abs(w + 10 ** rng.uniform(-6, -2.5) * rng.normal(0, 1, len(pairs)))
            wp = wp / wp.sum()
            L = lap(wp); ev, U = np.linalg.eigh(L); M = L32(wp); need = (n - 1) * ev[-1] - 2.0
            ts2 = np.linspace(0, np.pi, 181)
            best = max((n - 2) * float(np.trace(state(L, np.cos(t) * U[:, -1] + np.sin(t) * U[:, -2]) @ M)) - need for t in ts2)
            top = (n - 2) * float(np.trace(state(L, U[:, -1]) @ M)) - need
            if worst is None or best < worst[0]:
                worst = (best, top, ev[-1] - ev[-2])
        print("   400 random perturbations (size 1e-6..3e-3): smallest 'best x in plane' %+.6e (its top-x value %+.6e, gap %.3e)" % worst)


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
