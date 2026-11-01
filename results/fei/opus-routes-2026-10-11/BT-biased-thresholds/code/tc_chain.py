"""Chain-rule structure of TC(mu_A) for threshold events: per-coordinate terms I(Y_i; W_<i) in
heaviest-first and lightest-first orders, against c_i(1-q_i). Exact enumeration, float. Evidence."""
import numpy as np, math, sys, time
from scipy.optimize import minimize
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 2)
TLIM = float(sys.argv[2]) if len(sys.argv) > 2 else 200
def h(x):
    x = np.clip(x, 1e-300, 1 - 1e-16)
    return -(x * np.log(x) + (1 - x) * np.log(1 - x))
def analyze(w, theta, q):
    n = len(w); idx = np.arange(2 ** n)
    Y = ((idx[:, None] >> np.arange(n)) & 1).astype(float)
    W = Y @ w
    p = np.prod(np.where(Y == 1, q, 1 - q), axis=1)
    A = W >= theta - 1e-12
    a1 = p[A].sum()
    if a1 <= 1e-14 or a1 >= 1 - 1e-14: return None
    if a1 > 0.5:   # minority side: complement event in flipped coordinates
        A = ~A; q = 1 - q; Y = 1 - Y; w = w.copy(); a1 = p[A].sum()
        # complement {W < theta} = {sum w (1-y) > sum w - theta}: increasing in flipped coords
        W = Y @ w; theta = None
    alpha = a1
    pa = np.where(A, p, 0) / alpha
    b = pa @ Y
    TC = np.sum(h(b)) - (-np.sum(pa[pa > 0] * np.log(pa[pa > 0])))
    # criticality: y_i = 1 and y^{i->0} not in A
    c = np.zeros(n)
    Aset = A
    for i in range(n):
        flip = idx ^ (1 << i)
        crit = (Y[:, i] == 1) & Aset & (~Aset[flip])
        c[i] = pa[crit].sum()
    out = {}
    for name, order in (('heavy', np.argsort(-w, kind='stable')), ('light', np.argsort(w, kind='stable'))):
        terms = np.zeros(n)
        for pos, i in enumerate(order):
            pre = order[:pos]
            Wp = Y[:, pre] @ w[pre] if pos > 0 else np.zeros(len(idx))
            # I(Y_i; W_pre) under pa
            keys, inv = np.unique(np.round(Wp, 9), return_inverse=True)
            m = np.bincount(inv, weights=pa); m1 = np.bincount(inv, weights=pa * Y[:, i])
            with np.errstate(divide='ignore', invalid='ignore'):
                beta = np.where(m > 0, m1 / np.where(m > 0, m, 1), 0)
            terms[i] = h(np.array([b[i]]))[0] - np.sum(m * h(beta))
        out[name] = terms
    return dict(TC=TC, c=c, q=q, alpha=alpha, terms=out, chk=(out['heavy'].sum(), out['light'].sum()))
t0 = time.time(); worst = {'heavy': (0, None), 'light': (0, None), 'TCsum': (0, None)}; cnt = 0
while time.time() - t0 < TLIM:
    n = int(rng.integers(3, 11))
    kind = rng.integers(0, 3)
    w = (rng.integers(1, 6, n) if kind == 0 else np.exp(rng.normal(0, 1.2, n)) if kind == 1 else np.where(rng.random(n) < 0.3, 4, 1)).astype(float)
    theta = rng.random() * w.sum()
    q = 1 / (1 + np.exp(-rng.normal(0, 3, n)))
    r = analyze(w, theta, q)
    if r is None: continue
    cnt += 1
    base = r['c'] * (1 - r['q'])
    for name in ('heavy', 'light'):
        ratio = r['terms'][name].sum() / max(base.sum(), 1e-300)
        if ratio > worst[name][0]: worst[name] = (ratio, (n, w.round(3).tolist(), round(theta, 3)))
    rr = r['TC'] / max(base.sum(), 1e-300)
    if rr > worst['TCsum'][0]: worst['TCsum'] = (rr, (n, w.round(3).tolist(), round(theta, 3), r['alpha']))
    if abs(r['chk'][0] - r['TC']) > 1e-8 or abs(r['chk'][1] - r['TC']) > 1e-8:
        print('CHAIN RULE MISMATCH', r['chk'], r['TC']); break
print('configs', cnt)
for k, v in worst.items(): print(k, v)
