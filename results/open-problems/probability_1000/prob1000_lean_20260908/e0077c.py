"""E0077 / MMPP c^2>=1.  Route under test: is t -> log f(t) convex, where
f(t) = pi e^{(Q-D)t} 1 = P(no arrival in [0,t]) started stationary?
If yes then log f(t) >= f'(0)/f(0) * t = -(pi.lam) t, so int f >= 1/(pi.lam),
which is exactly the conjecture.  Also test the conclusion f(t) >= exp(-(pi.lam)t)
directly, since that is weaker than log-convexity and is what we actually need."""
import numpy as np
from scipy.linalg import expm, null_space

rng = np.random.default_rng(20260908)

def gen(m, kind):
    if kind == 'dense':
        Q = rng.exponential(1.0, (m, m)) * rng.choice([0.05,1.0,20.0])
    elif kind == 'cyclic':          # one-directional: maximally non-reversible
        Q = np.zeros((m, m))
        for i in range(m):
            Q[i, (i+1) % m] = rng.exponential(1.0)
        Q += 1e-3 * rng.exponential(1.0, (m, m))
    else:                            # skewed cycle
        Q = np.zeros((m, m))
        s = rng.uniform(0, 1)
        for i in range(m):
            Q[i, (i+1) % m] = rng.exponential(1.0)
            Q[i, (i-1) % m] += s * rng.exponential(1.0)
        Q += 1e-2 * rng.exponential(1.0, (m, m))
    np.fill_diagonal(Q, 0.0)
    np.fill_diagonal(Q, -Q.sum(1))
    return Q

def stat(Q):
    v = null_space(Q.T)
    if v.shape[1] != 1: return None
    p = v[:, 0].real
    if p.min() < 0: p = -p
    if p.min() <= 0: return None
    return p / p.sum()

ts = np.concatenate([np.linspace(0.0, 2.0, 161)[1:], np.linspace(2.0, 40.0, 121)[1:]])
worst_conv = 0.0; worst_ineq = 0.0; nconv = 0; nineq = 0; ntot = 0
wc_rec = None; wi_rec = None
for trial in range(4000):
    m = int(rng.choice([2,3,4,5,6,8]))
    kind = rng.choice(['dense','cyclic','skew'])
    Q = gen(m, kind); pi = stat(Q)
    if pi is None: continue
    scale = rng.choice([0.02, 1.0, 50.0])
    lam = rng.exponential(1.0, m) * scale
    if rng.random() < 0.3:           # near-degenerate: one hot state
        lam = np.full(m, 1e-3); lam[rng.integers(m)] = rng.exponential(1.0)*100
    M = Q - np.diag(lam)
    f = np.array([pi @ expm(M*t) @ np.ones(m) for t in ts])
    if f.min() <= 0: continue
    ntot += 1
    lf = np.log(f)
    # convexity of log f on the (non-uniform) grid: divided second difference
    for i in range(1, len(ts)-1):
        h1 = ts[i]-ts[i-1]; h2 = ts[i+1]-ts[i]
        d2 = ((lf[i+1]-lf[i])/h2 - (lf[i]-lf[i-1])/h1) / (0.5*(h1+h2))
        if d2 < worst_conv:
            worst_conv = d2; wc_rec = (m, kind, float(ts[i]), float(d2))
    # the weaker conclusion we actually need
    r = (lf + (pi@lam)*ts).min()
    if r < worst_ineq:
        worst_ineq = r; wi_rec = (m, kind, float(ts[int(np.argmin(lf + (pi@lam)*ts))]), float(r))
    if worst_conv < -1e-9 and nconv == 0: nconv = 1
    if r < -1e-9: nineq += 1

print("instances:", ntot)
print("worst log-f second difference :", worst_conv, wc_rec)
print("worst log f(t) + (pi.lam) t   :", worst_ineq, wi_rec)
print("instances violating f>=e^-rt  :", nineq)
