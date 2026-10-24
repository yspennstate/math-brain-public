# E0062 batch, second classifier. Per orbit: vertex visits (all / last half), Cesaro drift between
# 3n/4 and n, stationarity of the log-coordinates over the last 2000 steps, and the measured growth
# factor of the visit durations over the last full turn of the cycle.
import numpy as np, math, sys, time
np.seterr(all="ignore")
rng = np.random.default_rng(20260909)

def ratios(a, b, c, d):
    lp = lambda u: math.log1p(u); lm = lambda u: -math.log1p(-u)
    return lm(a) * lm(c) / (lp(d) * lp(b)), lm(b) * lm(d) / (lp(a) * lp(c))

def batch(a, b, c, d, X0, nsteps, tag):
    A = np.array([[0, a, 0, -d], [-a, 0, b, 0], [0, -b, 0, c], [d, 0, -c, 0]], float)
    L = np.log(X0); K = L.shape[0]; S = np.zeros_like(L)
    mean_q = None; Lprev = None
    lastv = -np.ones(K, int); visits = [[] for _ in range(K)]
    t0 = time.time()
    for n in range(1, nsteps + 1):
        x = np.exp(L); S += x
        L = L + np.log1p(x @ A.T); L -= np.log(np.exp(L).sum(axis=1, keepdims=True))
        m = L.argmax(axis=1); near = L[np.arange(K), m] > math.log(0.999)
        ch = np.nonzero(near & (m != lastv))[0]
        for k in ch: visits[k].append(n)
        lastv[ch] = m[ch]
        if n == 3 * nsteps // 4: mean_q = S / n
        if n == nsteps - 2000: Lprev = L.copy()
    mean = S / nsteps
    drift = np.abs(mean - mean_q).max(axis=1)
    big = L > math.log(1e-6)                       # coordinates that are not tiny
    stat = np.array([np.abs((L[k] - Lprev[k])[big[k]]).max() if big[k].any() else np.inf for k in range(K)])
    small_dec = np.array([bool(((L[k] - Lprev[k])[~big[k]] < 0).all()) if (~big[k]).any() else True for k in range(K)])
    nv_all = np.array([len(v) for v in visits]); nv_late = np.array([sum(1 for t in v if t > nsteps // 2) for v in visits])
    conv = (drift < 1e-3) & (stat < 1e-6) & small_dec & (nv_late == 0)
    cyc = (nv_late >= 1) | (drift > 1e-2)
    growth = []
    for v in visits:
        if len(v) >= 9:
            dur = np.diff(v); growth.append(dur[-1] / dur[-5])
    x = np.exp(L)
    print(f"--- {tag}: (a,b,c,d)=({a},{b},{c},{d}); predicted r1,r2 = {np.round(ratios(a,b,c,d),3)}; {K} orbits x {nsteps} steps, {time.time()-t0:.0f}s")
    print(f"  converged (drift<1e-3, stationary, no late vertex visit): {conv.sum()};  cycling (late vertex visit or drift>1e-2): {cyc.sum()};  neither: {(~conv & ~cyc).sum()}")
    print(f"  Cesaro drift |mean(n)-mean(3n/4)|: min {drift.min():.1e}, median {np.median(drift):.1e}, max {drift.max():.1e}")
    if growth: print(f"  measured duration growth per full turn (orbits with >=9 visits, n={len(growth)}): min {min(growth):.3f}, median {np.median(growth):.3f}, max {max(growth):.3f}")
    if conv.any():
        e13 = conv & (x[:, 1] + x[:, 3] < 1e-6); e24 = conv & (x[:, 0] + x[:, 2] < 1e-6)
        print(f"  converged limits on edge13: {e13.sum()}, on edge24: {e24.sum()}, elsewhere: {(conv & ~e13 & ~e24).sum()}")
        if e13.any():
            r = x[e13, 2] / x[e13, 0]; print(f"  edge13 limit ratios x3/x1 in [{r.min():.3f}, {r.max():.3f}]; attracting segment (d/c, a/b) = ({d/c:.3f}, {a/b:.3f})")

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100_000
    K = 80
    X0 = np.vstack([rng.dirichlet(np.ones(4), K // 2), rng.dirichlet(np.full(4, 0.2), K // 4), rng.dirichlet(np.full(4, 5.0), K // 4)])
    X0 = np.maximum(X0, 1e-12); X0 /= X0.sum(axis=1, keepdims=True)
    for a, b, c, d, tag in [(0.5, 0.5, 0.5, 0.5, "symmetric 0.5"), (0.3, 0.3, 0.3, 0.3, "symmetric 0.3"),
                            (0.5, 0.4, 0.5, 0.4, "ac>bd, r1,r2>1"), (0.9, 0.1, 0.9, 0.1, "ac>bd, r2<1"),
                            (0.6, 0.2, 0.6, 0.2, "ac>bd, r2<1 (second)")]:
        batch(a, b, c, d, X0, N, tag)
