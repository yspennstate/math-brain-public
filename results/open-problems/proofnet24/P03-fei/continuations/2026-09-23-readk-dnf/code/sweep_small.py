import time, numpy as np, numba as nb
from feicore import *
polite()

@nb.njit(cache=True)
def wht_nb(a):
    a = a.copy(); N = a.size; h = 1
    while h < N:
        for i in range(0, N, 2*h):
            for j in range(i, i+h):
                x = a[j]; y = a[j+h]; a[j] = x+y; a[j+h] = x-y
        h *= 2
    return a

@nb.njit(cache=True)
def all_stats(tt, n):
    N = 1 << n
    c = wht_nb(tt.astype(np.float64)) / N
    P = c*c
    H = 0.0; I = 0.0
    for S in range(N):
        p = P[S]
        if p > 1e-300:
            H -= p*np.log2(p)
        k = 0; s = S
        while s:
            k += s & 1; s >>= 1
        I += k*p
    # zeta
    g = P.copy()
    for i in range(n):
        for A in range(N):
            if A >> i & 1:
                g[A] += g[A ^ (1 << i)]
    beta = np.empty(N)
    for B in range(N):
        beta[B] = 1.0 - g[(N-1) ^ B]
    cost = np.full(N, np.inf); cost[0] = 0.0
    for B in range(1, N):
        if B & (B-1) == 0:
            cost[B] = 0.0; continue
        low = B & (-B); rest = B ^ low; best = np.inf; sub = rest
        while True:
            sub = (sub - 1) & rest
            B1 = low | sub
            cc = cost[B1] + cost[B ^ B1]
            if cc < best: best = cc
            if sub == 0: break
        cost[B] = beta[B] + best
    return H, I, cost[N-1]

def run_exhaustive4():
    n = 4; best = (0, None); bestH = (0, None)
    ratios = []
    for code in range(1, 1 << 16):
        tt = np.array([1 - 2*((code >> x) & 1) for x in range(16)], dtype=np.int8)
        H, I, C = all_stats(tt, n)
        if I < 1e-12: continue
        r = C / I
        if r > best[0]: best = (r, code, H/I)
        if H/I > bestH[0]: bestH = (H/I, code, r)
    print('n=4 exhaustive: max HC/I =', best, ' max H/I =', bestH, flush=True)

def run_random(n, count, rng):
    best = (0, None)
    for t in range(count):
        tt = np.where(rng.random(1 << n) < rng.random(), -1, 1).astype(np.int8)
        H, I, C = all_stats(tt, n)
        if I < 1e-12: continue
        r = C / I
        if r > best[0]: best = (r, H/I, tt.copy())
    print(f'n={n} random {count}: max HC/I = {best[0]:.4f} (H/I there {best[1]:.4f})', flush=True)
    return best

t = time.time(); run_exhaustive4(); print('time', time.time()-t)
rng = np.random.default_rng(1)
for n, c in [(5, 100000), (6, 50000), (7, 20000), (8, 5000)]:
    t = time.time(); run_random(n, c, rng); print('time', time.time()-t, flush=True)
