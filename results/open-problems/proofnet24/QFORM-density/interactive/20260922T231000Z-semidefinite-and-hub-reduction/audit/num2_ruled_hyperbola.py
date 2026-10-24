try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
import numpy as np
np.random.seed(7)

print("=== N6: Theorem C ruling formula vs Monte Carlo (n = 3, product of unions of intervals) ===", flush=True)
# Y = R^T X, X_i indicator of union of intervals (total length 1). Q = l1 Y1^2 + l2 Y2^2 - mu Y3^2.
def t_interval_length(p0, d, R, sets):
    # length of {t : (R (p0 + t d))_i in E_i for all i}; R maps y -> x = R y
    x0 = R @ p0; dx = R @ d
    ivs = [(-np.inf, np.inf)]
    for i in range(3):
        # allowed t for coordinate i: union over intervals (a,b) of {t: a <= x0_i + t dx_i <= b}
        allowed = []
        for (a, b) in sets[i]:
            if abs(dx[i]) < 1e-15:
                if a <= x0[i] <= b: allowed.append((-np.inf, np.inf))
            else:
                t1 = (a - x0[i]) / dx[i]; t2 = (b - x0[i]) / dx[i]
                allowed.append((min(t1, t2), max(t1, t2)))
        new = []
        for (u1, u2) in ivs:
            for (v1, v2) in allowed:
                lo, hi = max(u1, v1), min(u2, v2)
                if lo < hi: new.append((lo, hi))
        ivs = new
        if not ivs: return 0.0
    return sum(hi - lo for lo, hi in ivs)
def ruling_density(s, lam, R, sets, nth=4000):
    l1, l2, mu = lam
    Dinv = np.diag([1/np.sqrt(l1), 1/np.sqrt(l2), 1/np.sqrt(mu)])
    tot = 0.0
    ths = (np.arange(nth) + 0.5) * 2 * np.pi / nth
    for th in ths:
        e = np.array([np.cos(th), np.sin(th), 0.0]); w = np.array([-np.sin(th), np.cos(th), 1.0])
        tot += t_interval_length(Dinv @ (np.sqrt(s) * e), Dinv @ w, R, sets)
    return 0.5 * (l1 * l2 * mu) ** -0.5 * tot * (2 * np.pi / nth)
def sample(sets, N):
    out = np.empty((N, 3))
    for i in range(3):
        iv = sets[i]; L = np.array([b - a for a, b in iv]); k = np.random.choice(len(iv), N, p=L / L.sum())
        a = np.array([iv[j][0] for j in k]); out[:, i] = a + np.random.rand(N) * L[k]
    return out
configs = [
    ("R=I, uniform, (1,1,1)", np.eye(3), [[(-0.5, 0.5)]] * 3, (1.0, 1.0, 1.0)),
    ("R=I, uniform, (2,3,1.5)", np.eye(3), [[(-0.5, 0.5)]] * 3, (2.0, 3.0, 1.5)),
    ("R random, spread sets, (1,1.7,1.2)", np.linalg.qr(np.random.randn(3, 3))[0],
        [[(0.0, 0.4), (1.1, 1.7)], [(-0.3, 0.2), (2.0, 2.5)], [(0.1, 0.6), (-1.5, -1.0)]], (1.0, 1.7, 1.2)),
]
N = 6_000_000
for name, R, sets, lam in configs:
    X = sample(sets, N)
    Y = X @ R   # Y = R^T X  (row form)
    Q = lam[0] * Y[:, 0]**2 + lam[1] * Y[:, 1]**2 - lam[2] * Y[:, 2]**2
    best = 0
    for s in [0.02, 0.1, 0.3, 0.7]:
        h = 0.004
        mc = np.mean(np.abs(Q - s) < h) / (2 * h)
        fr = ruling_density(s, lam, R, sets)
        best = max(best, fr)
        print(f"  {name:36s} s={s:4.2f}: MC {mc:.4f}   ruling formula {fr:.4f}", flush=True)
    print(f"     (bound pi sqrt 2 = {np.pi*np.sqrt(2):.4f}; general-eigenvalue bound "
          f"{(lam[0]*lam[1]*lam[2])**-0.5 * np.mean([2*np.pi/np.sqrt(np.sin(t)**2/lam[0]+np.cos(t)**2/lam[1]+1/lam[2]) for t in np.linspace(0,2*np.pi,2001)]):.4f})", flush=True)

print("=== N7: Lemma 1.4 adversarial (alternating bathtub over f1, f2) ===", flush=True)
def adversary(B, delta, T=40.0, nt=400001, dy=2e-3, iters=12):
    mu, E = np.linalg.eigh(B)          # mu[0] < 0 < mu[1]
    mum, mup = mu[0], mu[1]; em, ep = E[:, 0], E[:, 1]
    D = -mum * mup; Lam = 1/mup + 1/(-mum)
    t = np.linspace(-T, T, nt); dt = t[1] - t[0]
    br = []
    for epsn in (1, -1):
        w = epsn * np.sqrt(delta/mup) * np.cosh(t)[:, None] * ep + np.sqrt(delta/(-mum)) * np.sinh(t)[:, None] * em
        br.append(w)
    W = np.vstack(br)                    # points along both branches, each carries weight dt
    lo = W.min(0) - 1; hi = W.max(0) + 1
    # restrict to a window where anything can happen: |w_i| <= 60 (outside, a unit-mass set cannot matter much)
    keep = np.all(np.abs(W) <= 60, axis=1); W = W[keep]
    idx = [np.floor((W[:, i] + 60) / dy).astype(np.int64) for i in range(2)]
    nb = int(np.ceil(120 / dy)) + 1
    f = [np.zeros(nb), np.zeros(nb)]
    # start: f_i = indicator of [-1/2,1/2]
    for i in range(2):
        c = np.arange(nb) * dy - 60
        f[i] = ((c >= -0.5) & (c < 0.5)).astype(float)
    val = 0
    for it in range(iters):
        for i in range(2):
            j = 1 - i
            wts = f[j][idx[j]] * dt
            K = np.bincount(idx[i], weights=wts, minlength=nb) / dy   # kernel density in coordinate i
            order = np.argsort(-K); m = int(round(1.0 / dy))
            f[i] = np.zeros(nb); f[i][order[:m]] = 1.0
        val = np.sum(f[0][idx[0]] * f[1][idx[1]]) * dt
    return val / (2 * np.sqrt(D)), D, Lam
for trial in range(8):
    th = np.random.rand() * np.pi
    Rt = np.array([[np.cos(th), -np.sin(th)], [np.sin(th), np.cos(th)]])
    mup = np.exp(np.random.uniform(-2, 2)); mum = -np.exp(np.random.uniform(-2, 2))
    B = Rt @ np.diag([mup, mum]) @ Rt.T
    for delta in [1e-1, 1e-3, 1e-5]:
        p, D, Lam = adversary(B, delta)
        bound = D**-0.5 * (5.2 + max(np.log(32 / (Lam * delta)), 0))
        print(f"  mu=({mup:.3f},{mum:.3f}) delta={delta:.0e}: adversarial density {p:.4f}  bound {bound:.4f}  ratio {p/bound:.3f}", flush=True)
