import numpy as np, sys
exec(open(r'~/AppData/Local/Temp/prob/h0020_search.py').read().split('best = (-np.inf, None)')[0])
def tenable(R):
    d = R.shape[0]
    for i in range(d):
        if R[i, i] < 0:
            di = -R[i, i]
            if any(R[i, j] % di != 0 for j in range(d)): return False
    return True
rng = np.random.default_rng(int(sys.argv[1]))
best_nn = (-np.inf, None); best_neg = (-np.inf, None)
for t in range(int(sys.argv[2])):
    d = rng.integers(3, 6); lam = int(rng.integers(1, 9))
    R = np.zeros((d, d), dtype=int)
    for i in range(d):
        off = rng.integers(0, lam + 4, size=d - 1) * (rng.random(d - 1) < rng.uniform(0.2, 1.0))
        R[i, [j for j in range(d) if j != i]] = off
        R[i, i] = lam - off.sum()
    if not irreducible(R) or not tenable(R): continue
    v = lam_max(R.astype(float), lam, d - 1)
    if np.all(np.diag(R) >= 0):
        if v > best_nn[0]: best_nn = (v, R.copy())
    else:
        if v > best_neg[0]: best_neg = (v, R.copy())
for name, b in [('nonneg-diagonal', best_nn), ('tenable negative-diagonal', best_neg)]:
    print(name, ': max lambda_max(p=d-1) =', b[0]); print(b[1])
