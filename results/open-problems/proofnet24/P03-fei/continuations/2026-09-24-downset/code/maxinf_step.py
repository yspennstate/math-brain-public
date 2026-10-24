# Does the MOST INFLUENTIAL coordinate always satisfy the restriction-step bound? For monotone f let v* = argmax Inf_v
# (ties: the smallest step) and compare Delta_{v*}/Inf_{v*} with rho_0 = min_v Delta_v/Inf_v, over all monotone
# functions of n <= 5 variables (and n = 6 in chunks), and over the hard families (tribes, majority, thresholds,
# matchings, the Remark 6.1 functions, triangle containment).
import itertools, numpy as np
from mono_enum import monotone_masks
from gdnf import truth_table

def fwht(G):
    N = G.shape[1]; h = 1
    while h < N:
        G = G.reshape(G.shape[0], N // (2 * h), 2, h)
        a = G[:, :, 0, :].copy(); b = G[:, :, 1, :]
        G[:, :, 0, :] = a + b; G[:, :, 1, :] = a - b
        G = G.reshape(G.shape[0], N); h *= 2
    return G / N
def phi(p): return np.where(p > 1e-300, -p * np.log2(np.where(p > 1e-300, p, 1)), 0.0)
def steps(tt, n):
    N = 1 << n; Fh = fwht(np.where(tt, -1.0, 1.0)); P = Fh * Fh; H = phi(P).sum(1)
    x = np.arange(N); D = []; INF = []
    for v in range(n):
        lo = x[((x >> v) & 1) == 0]; a = Fh[:, lo]; b = Fh[:, lo | (1 << v)]
        D.append(H - 0.5 * (phi((a + b) ** 2) + phi((a - b) ** 2)).sum(1)); INF.append((b * b).sum(1))
    return np.stack(D, 1), np.stack(INF, 1)
def report(tt, n, label):
    D, INF = steps(tt, n)
    ok = INF.max(1) > 1e-12
    D, INF = D[ok], INF[ok]
    with np.errstate(divide='ignore', invalid='ignore'):
        R = np.where(INF > 1e-12, D / INF, np.inf)
    rho0 = R.min(1)
    mx = INF.max(1, keepdims=True)
    cand = np.where(INF >= mx - 1e-12, R, np.inf)       # among the most influential coordinates
    rstar = cand.min(1)
    print('%-26s %8d fns | max rho0 %.3f | max Delta/Inf at the most influential coordinate %.3f'
          % (label, len(D), rho0.max(), rstar.max()), flush=True)
    return rstar.max()
worst = 0.0
for n in range(2, 7):
    masks = monotone_masks(n); N = 1 << n; best = 0.0
    for c in range(0, len(masks), 200000):
        tt = ((masks[c:c + 200000, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(bool)
        best = max(best, report(tt, n, 'all monotone n=%d [%d]' % (n, c // 200000)) if n < 6 else report(tt, n, 'n=6 chunk %d' % (c // 200000)))
    worst = max(worst, best)
def maj(n):
    x = np.arange(1 << n); return np.array([bin(t).count('1') for t in x]) > n // 2
fam = [('matching8', 16, truth_table(16, [(2 * i, 2 * i + 1) for i in range(8)])),
       ('tribes 4x4', 16, truth_table(16, [tuple(range(4 * i, 4 * i + 4)) for i in range(4)])),
       ('tribes 3x5', 15, truth_table(15, [tuple(range(5 * i, 5 * i + 5)) for i in range(3)])),
       ('majority15', 15, maj(15))]
E6 = list(itertools.combinations(range(6), 2))
fam.append(('K6 triangle', 15, truth_table(15, [tuple(E6.index(e) for e in itertools.combinations(T, 2)) for T in itertools.combinations(range(6), 3)])))
for name, n, f in fam: worst = max(worst, report(f[None, :], n, name))
print('largest Delta/Inf at a most influential coordinate: %.3f' % worst)
