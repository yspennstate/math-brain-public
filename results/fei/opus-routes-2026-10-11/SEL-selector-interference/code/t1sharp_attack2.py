"""Boolean-leaf attack on T1-sharp at larger n, unbalanced two-cell partitions, starting near disjoint-support
pairs (G1 a function of y_1..y_k, G2 = y_{k+1} * (function of the rest)) and from random pairs; moves keep
E[G1 G2] = 0.  Objective: gap = H(F) - [H(p) + sum p_k (H(q_k) + H(G_k))]."""
import sys, numpy as np
from t1sharp_attack import gap
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def start(n, kind):
    N = 1 << n; idx = np.arange(N)
    if kind == 0:
        while True:
            g1 = rng.choice([-1, 1], size=N); g2 = rng.choice([-1, 1], size=N)
            if int(np.dot(g1, g2)) == 0: return g1, g2
    # disjoint-support start: g1 depends on low bits only, g2 = y_top * random function of others
    k = n // 2
    f1 = rng.choice([-1, 1], size=1 << k); g1 = f1[idx & ((1 << k) - 1)]
    f2 = rng.choice([-1, 1], size=N); top = 1 - 2 * ((idx >> (n - 1)) & 1)
    g2 = top * f2[idx & ((1 << (n - 1)) - 1)]
    if int(np.dot(g1, g2)) != 0: return start(n, 0)
    return g1, g2
best_all = (-1, None)
for (a, cell1) in [(2, [0]), (3, [0]), (3, [0, 1, 2])]:
    lab = np.ones(1 << a, dtype=np.int64); lab[cell1] = 0
    for n in (5, 6):
        for rep in range(2):
            g1, g2 = start(n, rep)
            cur = gap(lab, [g1, g2], a, n)
            for it in range(2500):
                h1, h2 = g1.copy(), g2.copy()
                prod = h1 * h2
                mv = rng.integers(3)
                if mv < 2:
                    pos = np.where(prod == 1)[0]; neg = np.where(prod == -1)[0]
                    if len(pos) == 0 or len(neg) == 0: continue
                    i, j = rng.choice(pos), rng.choice(neg)
                    tgt = h1 if mv == 0 else h2
                    tgt[i] *= -1; tgt[j] *= -1
                else:
                    i = rng.integers(len(h1)); h1[i] *= -1; h2[i] *= -1
                v = gap(lab, [h1, h2], a, n)
                if v >= cur - 1e-12: cur, g1, g2 = v, h1, h2
            print(a, cell1, n, rep, 'best gap %.3e' % cur, flush=True)
            if cur > best_all[0]: best_all = (cur, a, cell1, n)
print('overall', best_all)
