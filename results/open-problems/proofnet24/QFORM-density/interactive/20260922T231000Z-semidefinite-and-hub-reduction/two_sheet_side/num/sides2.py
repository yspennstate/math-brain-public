# As sides.py, comb laws only, eps down to 0, with a control in which P is shuffled across samples
# (a hub that sees an independent P gains nothing; the gap to the control measures the estimator's selection bias).
import numpy as np, sys
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
rng = np.random.default_rng(seed)
m, N, lam = 32, 16, 1.0
A = rng.normal(size=(m, 3)); Qm, _ = np.linalg.qr(A); w, v, p = Qm[:, 0], Qm[:, 1], Qm[:, 2]
pos = np.stack([np.sort(rng.choice(2*N, N, replace=False)) for _ in range(m)]).astype(float)
def sample(size):
    k = rng.integers(0, N, size=(size, m)); return pos[np.arange(m)[None, :], k] + rng.random((size, m))/N
b = 1/64; edges = np.arange(-60, 60 + b, b); K = int(round(1/b))
epss, sigs = (0.03, 0.01, 0.003, 0.001, 0.0), (0.05, 0.3)
mean = sample(200_000).mean(axis=0)
H = {(e, s0, sg, sh): np.zeros(len(edges) - 1) for e in epss for s0 in sigs for sg in (1, -1) for sh in (0, 1)}
S = 0
for chunk in range(8):
    X = sample(250_000) - mean; S += len(X)
    L, V, P = X @ w, X @ v, X @ p; wt = 1/(2*np.abs(L)); Ps = rng.permutation(P)
    for e in epss:
        for s0 in sigs:
            for sg in (1, -1):
                for sh, PP in ((0, P), (1, Ps)):
                    xs = (sg*s0 - lam*V*V)/(2*L) - e*PP
                    H[(e, s0, sg, sh)] += np.histogram(xs, bins=edges, weights=wt)[0]
for e in epss:
    for s0 in sigs:
        r = {(sg, sh): np.sort(H[(e, s0, sg, sh)])[::-1][:K].sum()/S for sg in (1, -1) for sh in (0, 1)}
        print("seed %d eps=%-6g sigma=%-5g one-sheet %.4f (shuffled %.4f)  two-sheet %.4f (shuffled %.4f)"
              % (seed, e, s0, r[(1,0)], r[(1,1)], r[(-1,0)], r[(-1,1)]), flush=True)
