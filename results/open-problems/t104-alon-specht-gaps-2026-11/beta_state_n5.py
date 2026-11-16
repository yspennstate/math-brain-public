"""n = 5: a state that does not single out one eigenvector.

For the Laplacian eigenpairs (lam_k, u_k) on the sum-zero space and a weight f_k >= 0 put

    D_f = sum over pairs k, l with lam_k > lam_l of  f_k (lam_k - lam_l) a_kl a_kl^t / trace,
    a_kl = the [3,2] component of (u_k u_l^t + u_l u_k^t)/sqrt 2.

With f the indicator of the top eigenvalue this is the gap-weighted state at the top eigenvector.  With
f_k = exp(beta (lam_k - lam)/lam) it is a function of L alone (no choice inside an eigenspace) and continuous in G.

    s_beta(G) = 3 tr(D_f L(G, [3,2])) - 4 lam + 2W   (W = 1),   slack(G) >= s_beta(G) for every beta.

usage: beta_state_n5.py NRANDOM SEED
"""
import sys
import numpy as np
import minmax_n5 as mm

n = mm.n
BETAS = [0.0, 1.0, 3.0, 10.0, 30.0, 100.0, 300.0, 1000.0, 1e4, 1e6]


def s_beta(w, betas=BETAS):
    w = w / w.sum()
    L = mm.lap(w)
    ev, U = np.linalg.eigh(L - np.ones((n, n)) / n)        # column 0 is the constant vector (eigenvalue -1)
    lam = ev[-1]
    M = mm.L32(w)
    need = (n - 1) * lam - 2.0
    slack = (n - 2) * np.linalg.eigvalsh(M)[-1] - need
    terms = []
    for k in range(1, n):
        for l in range(1, k):
            g = ev[k] - ev[l]
            if g > 1e-13:
                a = mm.B.T @ ((np.outer(U[:, k], U[:, l]) + np.outer(U[:, l], U[:, k])) / np.sqrt(2.0)).ravel()
                terms.append((k, g, float(a @ M @ a), float(a @ a)))
    out = []
    for beta in betas:
        num = den = 0.0
        for k, g, q, nn in terms:
            f = np.exp(beta * (ev[k] - lam) / lam)
            num += f * g * q; den += f * g * nn
        out.append((n - 2) * num / den - need if den > 1e-15 else -need)
    return slack, np.array(out), ev[-1] - ev[-2]


def show(label, w):
    slack, vals, gap = s_beta(w)
    print("%-26s gap %.2e slack %+.5f | " % (label, gap, slack) + " ".join("%+.5f" % v for v in vals), flush=True)
    return vals


def main():
    nr, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = np.random.default_rng(seed)
    print("beta:" + " " * 45 + " ".join("%8g" % b for b in BETAS))
    show("edge", mm.graph([((0, 1), 1.0)]))
    for k in range(2, 5):
        show("K_{1,%d}" % k, mm.graph([((0, j), 1.0) for j in range(1, k + 1)]))
    show("two edges 3:1", mm.graph([((0, 1), 3.0), ((2, 3), 1.0)]))
    show("triangle", mm.graph([((0, 1), 1.0), ((1, 2), 1.0), ((0, 2), 1.0)]))
    show("K_5", np.ones(mm.m))
    bad = {}
    for name in ("bad1", "bad2"):
        base = mm.start(name, np.random.default_rng(0)) * 0 + 0
    b1 = np.array([0.00007132, 0.02226662, 0.20735806, 0.20834156, 0.30343969, 0.00292157, 0.00121865,
                   0.02462748, 0.02321798, 0.20653708])
    b2 = np.array([0.21210057, 0.21352633, 0.01393605, 0.00089872, 0.21228140, 0.01567941, 0.00283654,
                   0.01366421, 0.00059663, 0.31448014])
    for name, b in (("bad1", b1), ("bad2", b2)):
        show(name, b)
        worst = None
        for trial in range(400):
            wp = np.abs(b + 10 ** rng.uniform(-6, -2.5) * rng.normal(0, 1, mm.m))
            slack, vals, gap = s_beta(wp)
            worst = vals if worst is None else np.minimum(worst, vals)
        print("%-26s %27s | " % (name + ", 400 perturbations", "smallest per beta") + " ".join("%+.5f" % v for v in worst), flush=True)
    # random graphs: smallest value per beta, and the smallest of (max over beta)
    worst = None; worstmax = None; wm = None
    for trial in range(nr):
        kind = mm.KINDS[trial % len(mm.KINDS)]
        w = mm.start(kind, rng)
        slack, vals, gap = s_beta(w)
        worst = vals if worst is None else np.minimum(worst, vals)
        if worstmax is None or vals.max() < worstmax:
            worstmax = vals.max(); wm = (kind, slack, gap, w / w.sum())
    print("%-26s %27s | " % ("%d graphs (ten families)" % nr, "smallest per beta") + " ".join("%+.5f" % v for v in worst))
    print("smallest of max over beta: %+.6e (family %s, slack %+.5f, gap %.2e)" % (worstmax, wm[0], wm[1], wm[2]))
    print("   weights " + " ".join("%d%d:%.6f" % (i + 1, j + 1, v) for (i, j), v in zip(mm.pairs, wm[3])))


if __name__ == "__main__":
    main()
