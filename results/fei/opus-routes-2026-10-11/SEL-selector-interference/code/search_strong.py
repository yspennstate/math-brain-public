"""Balanced g with large H/(I-1): iterated composition g^{o k} has H/I = rho (1 - I^{-k}), rho = H/(I-1).
Exhaustive over balanced functions on 4 bits; random + symmetric search on 5 and 6 bits."""
import itertools, numpy as np
from fei_lib import fwht_int, entropy_from_W, influence_from_W
best = []
n = 4
for ones in itertools.combinations(range(16), 8):
    t = np.ones(16, dtype=np.int64); t[list(ones)] = -1
    W = fwht_int(t); I = influence_from_W(W, n); H = entropy_from_W(W, n)
    if I > 1:
        best.append((H / (float(I) - 1), H, I, ones))
best.sort(reverse=True)
print('n=4 balanced best H/(I-1):', best[0][:3], best[0][3])
rng = np.random.default_rng(5)
for n in (5, 6):
    bb = (0,)
    for trial in range(200000 if n == 5 else 60000):
        t = np.ones(1 << n, dtype=np.int64)
        t[rng.choice(1 << n, size=1 << (n - 1), replace=False)] = -1
        W = fwht_int(t); I = influence_from_W(W, n)
        if I <= 1: continue
        H = entropy_from_W(W, n); r = H / (float(I) - 1)
        if r > bb[0]: bb = (r, H, I, t.copy())
    print('n=%d random balanced best H/(I-1):' % n, bb[:3])
    # hill climb by swapping a -1 and a +1
    t = bb[3]; r = bb[0]
    for it in range(20000):
        i = rng.choice(np.where(t == -1)[0]); j = rng.choice(np.where(t == 1)[0])
        t2 = t.copy(); t2[i], t2[j] = 1, -1
        W = fwht_int(t2); I = influence_from_W(W, n)
        if I <= 1: continue
        H = entropy_from_W(W, n); r2 = H / (float(I) - 1)
        if r2 >= r: t, r = t2, r2
    W = fwht_int(t)
    print('  hill-climbed:', r, entropy_from_W(W, n), influence_from_W(W, n), ''.join('1' if v == -1 else '0' for v in t))
