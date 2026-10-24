# Adversarial search against the open statement (C1): for monotone f, every coordinate v of largest influence has
# Delta_v <= K Inf_v with K about 6 (exhaustive n <= 6 and the families give 6.004). Simulated annealing over monotone
# functions on n variables maximises c1(f) = max over v of largest influence of Delta_v / Inf_v, with O(N) Fourier updates
# per move (a move switches a maximal zero on or a minimal one off). The best function of each run is saved.
import math, random, time, numpy as np

def fwht(a):
    a = a.copy(); N = a.shape[0]; h = 1
    while h < N:
        a = a.reshape(-1, 2, h); u = a[:, 0, :].copy(); w = a[:, 1, :]
        a[:, 0, :] = u + w; a[:, 1, :] = u - w; a = a.reshape(N); h *= 2
    return a

def phi(p):
    out = np.zeros_like(p); nz = p > 1e-300; out[nz] = -p[nz] * np.log2(p[nz]); return out

def setup(n):
    N = 1 << n; idx = np.arange(N)
    par = np.zeros(N, dtype=np.int8)
    for k in range(n): par ^= ((idx >> k) & 1).astype(np.int8)
    sign = 1.0 - 2.0 * par
    low = [idx[((idx >> v) & 1) == 0] for v in range(n)]
    ones = [[v for v in range(n) if (x >> v) & 1] for x in range(N)]
    zeros = [[v for v in range(n) if not (x >> v) & 1] for x in range(N)]
    return N, idx, sign, low, ones, zeros

def c1(G, n, low):
    P = G * G; H = float(phi(P).sum())
    infs = np.array([float((G[low[v] | (1 << v)] ** 2).sum()) for v in range(n)])
    mx = infs.max()
    if mx < 1e-12: return -1.0, None
    best = -1.0; arg = None
    for v in range(n):
        if infs[v] < mx - 1e-12: continue
        a = G[low[v]]; b = G[low[v] | (1 << v)]
        d = H - 0.5 * float((phi((a + b) ** 2) + phi((a - b) ** 2)).sum())
        r = d / infs[v]
        if r > best: best, arg = r, v
    return best, arg

def anneal(n, steps, seed, env):
    N, idx, sign, low, ones, zeros = env
    rng = random.Random(seed); kind = seed % 3
    if kind == 0:
        w = [rng.random() for _ in range(n)]; t = rng.uniform(0.2, 0.8) * sum(w)
        f = np.array([sum(w[v] for v in range(n) if (x >> v) & 1) >= t for x in range(N)])
    elif kind == 1:
        f = np.zeros(N, dtype=bool)
        for _ in range(rng.randrange(2, 3 * n)):
            S = rng.sample(range(n), rng.choice((2, 2, 3))); m = sum(1 << v for v in S); f |= (idx & m) == m
    else:
        perm = list(range(n)); rng.shuffle(perm); f = np.zeros(N, dtype=bool); i = 0
        while i < n:
            k = rng.choice((2, 2, 3)); S = perm[i:i + k]; i += k; m = sum(1 << v for v in S); f |= (idx & m) == m
    if f.all() or not f.any(): f[N - 1] = True; f[0] = False
    G = fwht(np.where(f, -1.0, 1.0)) / N; fl = f.tolist()
    cur, _ = c1(G, n, low); best = (cur, f.copy())
    for s in range(steps):
        x = rng.randrange(N)
        if fl[x]:
            if x == N - 1 or any(fl[x ^ (1 << v)] for v in ones[x]): continue
            delta = 2.0
        else:
            if x == 0 or not all(fl[x | (1 << v)] for v in zeros[x]): continue
            delta = -2.0
        G2 = G + (delta / N) * sign[idx & x]
        sc, _ = c1(G2, n, low)
        T = 0.05 * (1 - s / steps) + 1e-4
        if sc >= cur or rng.random() < math.exp((sc - cur) / T):
            fl[x] = not fl[x]; f[x] = not f[x]; G = G2; cur = sc
            if sc > best[0]: best = (sc, f.copy())
        if s % 50000 == 0 and s:
            G = fwht(np.where(f, -1.0, 1.0)) / N; cur, _ = c1(G, n, low)
    return best

if __name__ == '__main__':
    try:
        import psutil; p = psutil.Process(); p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); p.cpu_affinity(list(range(2, 16)))
    except Exception: pass
    t0 = time.time(); keep = {}
    for n, steps, seeds in ((8, 400000, 6), (10, 400000, 6), (12, 200000, 4)):
        env = setup(n); top = (-1, None)
        for sd in range(seeds):
            sc, f = anneal(n, steps, 7717 * n + sd, env)
            print('n %2d seed %d start %s: best max-influence step ratio %.4f | ones %d | %.0f s'
                  % (n, sd, ('thr', 'dnf', 'tribes')[(7717 * n + sd) % 3], sc, int(f.sum()), time.time() - t0), flush=True)
            if sc > top[0]: top = (sc, f)
        keep['n%d' % n] = top[1]
        print('n %2d: overall best %.4f' % (n, top[0]), flush=True)
        np.savez_compressed('adv_c1_best.npz', **keep)
    print('done in %.0f s' % (time.time() - t0))
