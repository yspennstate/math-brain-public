# T115: how large can |E_h| / ||MH + HM||_HS^2 be?  Lemma 3 proves <= 2. Hill-climb over positive weights w
# and sign functions h on small cubes. Floating point; a search, not a proof.
import itertools, math
import numpy as np

def out(*a):
    print(*a, flush=True)

rng = np.random.default_rng(5)

def cube(n):
    X = np.array(list(itertools.product([-1, 1], repeat=n)), dtype=float)
    subsets = sorted(itertools.chain.from_iterable(itertools.combinations(range(n), k) for k in range(n + 1)), key=len)
    deg = np.array([len(S) for S in subsets])
    Chi = np.ones((2**n, len(subsets)))
    for j, S in enumerate(subsets):
        for i in S:
            Chi[:, j] *= X[:, i]
    return X, deg, Chi

def ratio(logw, h, Chi, deg, n, edge):
    Q, R = np.linalg.qr(np.exp(0.5*logw)[:, None]*Chi)
    M = (Q*(deg - n/2)) @ Q.T
    same = (h[:, None] == h[None, :])
    T2 = 4*(M[same]**2).sum()
    nE = (edge & same).sum()
    return nE/T2 if T2 > 1e-12 else 0.0

for n in (2, 3, 4, 5):
    X, deg, Chi = cube(n); N = 2**n
    edge = ((X[:, None, :] != X[None, :, :]).sum(axis=2) == 1)
    best = 0.0; bestinfo = None
    hs = [np.array(h, dtype=float) for h in itertools.product([-1, 1], repeat=N)] if n <= 3 else [rng.choice([-1.0, 1.0], size=N) for _ in range(300)]
    if n >= 4:      # add structured sign functions
        hs += [X[:, 0].copy(), X[:, 0]*X[:, 1], np.sign(X.sum(axis=1) + 0.5), np.ones(N), Chi[:, -1].copy(), np.where(np.arange(N) == 0, -1.0, 1.0)]
    for h in hs:
        if h[0] < 0 and n <= 3:
            continue
        for start in range(3 if n <= 3 else 2):
            lw = rng.normal(scale=[0.1, 1.0, 3.0][start], size=N)
            cur = ratio(lw, h, Chi, deg, n, edge)
            step = 1.0
            for it in range(300 if n <= 4 else 120):
                cand = lw + rng.normal(scale=step, size=N)*(rng.random(N) < 0.5)
                c = ratio(cand, h, Chi, deg, n, edge)
                if c > cur:
                    lw, cur = cand, c
                else:
                    step = max(step*0.97, 1e-3)
            if cur > best:
                best = cur; bestinfo = (h.copy(), lw.copy())
    h, lw = bestinfo
    out("n=%d  largest |E_h| / ||T||^2 found: %.6f   (Lemma 3 gives <= 2; h == 1 with w == 1 gives exactly 1)" % (n, best))
    out("      at h with %d plus signs, log-weight spread %.2f" % (int((h > 0).sum()), lw.max() - lw.min()))
out("done")
