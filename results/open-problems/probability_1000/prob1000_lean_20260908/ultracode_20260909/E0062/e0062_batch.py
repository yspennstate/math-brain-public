# E0062: many orbits at once for the 4-cycle-with-ties Volterra operator, log coordinates.
# Classifies each orbit at the end as (i) converged to the fixed edge {1,3} / {2,4},
# (ii) still cycling through vertex neighbourhoods, (iii) other.
import numpy as np, math, sys, time
np.seterr(all="ignore")
rng = np.random.default_rng(20260909)

def ratios(a, b, c, d):
    lp = lambda u: math.log1p(u); lm = lambda u: -math.log1p(-u)
    return lm(a) * lm(c) / (lp(d) * lp(b)), lm(b) * lm(d) / (lp(a) * lp(c))

def batch(a, b, c, d, X0, nsteps, tag):
    A = np.array([[0, a, 0, -d], [-a, 0, b, 0], [0, -b, 0, c], [d, 0, -c, 0]], float)
    L = np.log(X0)                         # (K,4)
    K = L.shape[0]
    S = np.zeros_like(L)
    means_hist = []
    checkpoints = [nsteps // 4, nsteps // 2, 3 * nsteps // 4, nsteps]
    lastvertex = -np.ones(K, int); nvisits = np.zeros(K, int); nvisits_late = np.zeros(K, int)
    t0 = time.time()
    for n in range(1, nsteps + 1):
        x = np.exp(L)
        S += x
        L = L + np.log1p(x @ A.T)
        L -= np.log(np.exp(L).sum(axis=1, keepdims=True))
        m = L.argmax(axis=1)
        near = L[np.arange(K), m] > math.log(0.999)
        changed = near & (m != lastvertex)
        nvisits += changed
        if n > 0.7 * nsteps: nvisits_late += changed
        lastvertex[changed] = m[changed]
        if n in checkpoints: means_hist.append(S / n)
    x = np.exp(L)
    edge13 = (x[:, 1] + x[:, 3] < 1e-8)
    edge24 = (x[:, 0] + x[:, 2] < 1e-8)
    cycling = nvisits_late >= 2
    print(f"--- {tag}: a,b,c,d=({a},{b},{c},{d}) ratios r1,r2 = {np.round(ratios(a,b,c,d),3)}; {K} orbits x {nsteps} steps, {time.time()-t0:.0f}s")
    print(f"  converged to edge13: {edge13.sum()}, to edge24: {edge24.sum()}, cycling (>=2 vertex visits in last 30%): {cycling.sum()}, other: {(~edge13 & ~edge24 & ~cycling).sum()}")
    # Cesaro drift between the last two checkpoints, per orbit
    drift = np.abs(means_hist[-1] - means_hist[-2]).max(axis=1)
    print(f"  max |Cesaro(n) - Cesaro(3n/4)| over coords: converged orbits median {np.median(drift[edge13|edge24]) if (edge13|edge24).any() else float('nan'):.2e}; cycling orbits median {np.median(drift[cycling]) if cycling.any() else float('nan'):.2e}, min {drift[cycling].min() if cycling.any() else float('nan'):.2e}")
    if edge13.any():
        r = x[edge13, 2] / x[edge13, 0]
        print(f"  edge13 limits: x3/x1 in [{r.min():.3f}, {r.max():.3f}]  (attracting segment is (d/c, a/b) = ({d/c:.3f}, {a/b:.3f}))")
    return edge13, edge24, cycling

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300_000
    K = 80
    # mixed population: Dirichlet(1) interior points, plus points near vertices, plus points near the edges
    X0 = np.vstack([rng.dirichlet(np.ones(4), K // 2),
                    rng.dirichlet(np.full(4, 0.2), K // 4),
                    rng.dirichlet(np.full(4, 5.0), K // 4)])
    X0 = np.maximum(X0, 1e-12); X0 /= X0.sum(axis=1, keepdims=True)
    for a, b, c, d, tag in [(0.5, 0.5, 0.5, 0.5, "symmetric"),
                            (0.5, 0.4, 0.5, 0.4, "ac>bd, r1,r2>1"),
                            (0.9, 0.1, 0.9, 0.1, "ac>bd, r2<1"),
                            (0.3, 0.3, 0.3, 0.3, "symmetric small")]:
        batch(a, b, c, d, X0, N, tag)
