# E T_n (bridge pattern, level lambda) for larger n by value iteration h = 1 + P h on the last n-1 letters
# (vectorised; the sparse direct solve ran out of time at n = 20), then a fit a + b n^{-1/2} + c n^{-1}.
import math, sys
import numpy as np

def ET(lam, n, tol=1e-11, maxit=200000):
    f = math.floor(lam * math.sqrt(n)); L = f if (f - n) % 2 == 0 else f + 1
    m = n - 1; S = 1 << m
    s = np.arange(S, dtype=np.int64)
    pop = np.zeros(S, dtype=np.int64); t = s.copy()
    while t.any():
        pop += t & 1; t >>= 1
    sums = 2 * pop - m
    nxt = [((s << 1) | x) & (S - 1) for x in (0, 1)]
    live = [(sums + (1 if x else -1)) != L for x in (0, 1)]
    h = np.zeros(S)
    for it in range(maxit):
        hn = 1.0 + 0.5 * (np.where(live[0], h[nxt[0]], 0.0) + np.where(live[1], h[nxt[1]], 0.0))
        d = np.abs(hn - h).max(); h = hn
        if d < tol:
            break
    # remaining error after a geometric tail: d * q / (1 - q) with q the last contraction; report it
    return m + h.mean(), it, d

lam = float(sys.argv[1]) if len(sys.argv) > 1 else 0.0
ns = [int(a) for a in sys.argv[2].split(",")] if len(sys.argv) > 2 else [10, 12, 14, 16, 18, 20]
out = []
for n in ns:
    v, it, d = ET(lam, n); out.append((n, v / n)); print(n, repr(v), v / n, it, d, flush=True)
N = np.array([a for a, _ in out], float); Y = np.array([b for _, b in out])
for k in (2, 3, 4):
    if len(N) >= k + 1:
        X = np.vstack([N ** (-j / 2) for j in range(k)]).T
        print("fit terms", k, np.linalg.lstsq(X, Y, rcond=None)[0], flush=True)
