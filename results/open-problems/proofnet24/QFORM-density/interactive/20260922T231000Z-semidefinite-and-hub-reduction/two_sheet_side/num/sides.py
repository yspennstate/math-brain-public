# Leaking hub Q = 2 L (X0 + eps P) + lam V^2. For each light sample the hub value putting Q at level s is
# x*(s) = (s - lam V^2)/(2L) - eps P, with weight 1/(2|L|). The density of Q at s for hub law f0 is E[f0(x*)/(2|L|)];
# the supremum over hub laws (density <= 1) is the top unit mass of G_s, the weighted law of x*(s).
# G_s is estimated by a weighted histogram (bin 1/64); reported: its top unit mass at s = +sigma and s = -sigma.
import numpy as np, sys
try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception: pass
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
rng = np.random.default_rng(seed)
m, N, lam = 32, 16, 1.0
A = rng.normal(size=(m, 3)); Qm, _ = np.linalg.qr(A); w, v, p = Qm[:, 0], Qm[:, 1], Qm[:, 2]
pos = np.stack([np.sort(rng.choice(2*N, N, replace=False)) for _ in range(m)]).astype(float)   # tooth positions per coordinate
def sample(law, size):
    if law == "unif": return rng.random((size, m))
    k = rng.integers(0, N, size=(size, m))
    return pos[np.arange(m)[None, :], k] + rng.random((size, m))/N
b = 1/64; edges = np.arange(-60, 60 + b, b); K = int(round(1/b))
epss, sigs = (0.3, 0.1, 0.03), (0.05, 0.3, 1.0)
for law in ("comb", "unif"):
    mean = sample(law, 200_000).mean(axis=0)
    H = {(e, s0, sg): np.zeros(len(edges) - 1) for e in epss for s0 in sigs for sg in (1, -1)}
    S = 0
    for chunk in range(8):
        X = sample(law, 250_000) - mean; S += len(X)
        L, V, P = X @ w, X @ v, X @ p; wt = 1/(2*np.abs(L))
        for e in epss:
            for s0 in sigs:
                for sg in (1, -1):
                    xs = (sg*s0 - lam*V*V)/(2*L) - e*P
                    H[(e, s0, sg)] += np.histogram(xs, bins=edges, weights=wt)[0]
    for e in epss:
        for s0 in sigs:
            r = [np.sort(H[(e, s0, sg)])[::-1][:K].sum()/S for sg in (1, -1)]
            print("%-5s eps=%-5g sigma=%-5g  one-sheet %.4f   two-sheet %.4f" % (law, e, s0, r[0], r[1]), flush=True)
