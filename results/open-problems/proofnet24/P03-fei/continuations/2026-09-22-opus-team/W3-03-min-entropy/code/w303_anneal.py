"""Simulated annealing for large Hinf/I at fixed n (single truth-table flips, incremental Walsh update).

usage: python w303_anneal.py n restarts steps seed
Prints the best ratio found per restart and overall, with the truth table (hex, bit x = f(x) true).
"""
import sys, json, math
import numpy as np
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
sys.path.insert(0, __file__.rsplit("/", 1)[0].rsplit("\\", 1)[0])
from fmei_lib import coeffs, popcounts

n, restarts, steps, seed = (int(a) for a in sys.argv[1:5])
N = 1 << n
rng = np.random.default_rng(seed)
pc = popcounts(n).astype(np.float64)
# character table chi[x, S] = (-1)^{|x & S|}
X = np.arange(N)
chi = np.where(popcounts(n)[(X[:, None] & X[None, :])] % 2 == 0, 1.0, -1.0)


def score(c):
    p = c * c
    I = p @ pc
    if I < 1e-12:
        return -1.0
    return -math.log2(p.max()) / I


best_all = (-1, None)
for r in range(restarts):
    kind = r % 3
    if kind == 0:
        f = np.where(rng.random(N) < 0.5, -1.0, 1.0)
    elif kind == 1:   # sparse-true start
        f = np.where(rng.random(N) < 0.2, -1.0, 1.0)
    else:             # dense-true start
        f = np.where(rng.random(N) < 0.8, -1.0, 1.0)
    c = coeffs(f)
    cur = score(c)
    best = (cur, f.copy())
    T0 = 0.2
    for t in range(steps):
        T = T0 * (1 - t / steps) + 1e-4
        x = int(rng.integers(N))
        dc = (-2.0 * f[x] / N) * chi[x]
        c2 = c + dc
        s2 = score(c2)
        if s2 >= cur or rng.random() < math.exp((s2 - cur) / T):
            f[x] = -f[x]
            c = c2
            cur = s2
            if cur > best[0]:
                best = (cur, f.copy())
    # exact recompute of best
    cb = coeffs(best[1])
    sb = score(cb)
    mask = int(sum(1 << i for i in range(N) if best[1][i] < 0))
    p = cb * cb
    print(json.dumps(dict(n=n, restart=r, ratio=sb, Hinf=float(-math.log2(p.max())), I=float(p @ pc),
                          mean=float(cb[0]), mask=hex(mask))), flush=True)
    if sb > best_all[0]:
        best_all = (sb, mask)
print(json.dumps(dict(n=n, best_ratio=best_all[0], mask=hex(best_all[1]))), flush=True)
