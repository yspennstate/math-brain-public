# Adversarial search for monotone functions with large H/I or large R/I, where
#     R(f) = sum_{S: P(S)>0} P(S) sum_{v in S} log2+ (P(S - v)/P(S))      (paper Proposition 6.3: FEI <=> R <= K I).
# Simulated annealing over monotone Boolean functions on n variables; a move switches a maximal zero on or a minimal
# one off, so monotonicity is kept; the Fourier transform is updated in O(N) per move. The best function of every run
# is saved (truth table) with its H/I, R/I, sum_v B_v / I and rho_0 = min_v Delta_v/Inf_v.
import sys, math, random, time, numpy as np

def setup(n):
    N = 1 << n; idx = np.arange(N)
    par = np.zeros(N, dtype=np.int8)
    for k in range(n): par ^= ((idx >> k) & 1).astype(np.int8)
    sign = 1.0 - 2.0 * par                       # sign[t] = (-1)^{popcount t}
    pc = np.array([bin(t).count('1') for t in range(N)])
    low = [idx[((idx >> v) & 1) == 0] for v in range(n)]
    return N, idx, sign, pc, low

def fwht(a):
    a = a.copy(); N = a.shape[0]; h = 1
    while h < N:
        a = a.reshape(-1, 2, h); u = a[:, 0, :].copy(); w = a[:, 1, :]
        a[:, 0, :] = u + w; a[:, 1, :] = u - w; a = a.reshape(N); h *= 2
    return a

def phi(p):
    out = np.zeros_like(p); nz = p > 1e-300; out[nz] = -p[nz] * np.log2(p[nz]); return out

def stats(G, n, pc, low, full=False):
    P = G * G; I = float((P * pc).sum())
    if I < 1e-12: return None
    H = float(phi(P).sum())
    R = 0.0; B = 0.0
    for v in range(n):
        X = P[low[v]]; Y = P[low[v] | (1 << v)]
        ok = (X > 1e-300) & (Y > 1e-300)
        R += float((Y[ok] * np.maximum(np.log2(X[ok] / Y[ok]), 0.0)).sum())
        if full: B += float((phi(X) + phi(Y) - phi(X + Y)).sum())
    out = {'H': H, 'I': I, 'R': R}
    if full:
        out['B'] = B
        rho = math.inf
        for v in range(n):
            a = G[low[v]]; b = G[low[v] | (1 << v)]; inf = float((b * b).sum())
            if inf < 1e-12: continue
            d = H - 0.5 * float((phi((a + b) ** 2) + phi((a - b) ** 2)).sum())
            rho = min(rho, d / inf)
        out['rho0'] = rho
    return out

def anneal(n, obj, steps, seed, env):
    N, idx, sign, pc, low = env
    rng = random.Random(seed)
    kind = seed % 3
    if kind == 0:     # random threshold function
        w = np.array([rng.random() for _ in range(n)]); t = rng.uniform(0.2, 0.8) * w.sum()
        f = np.array([sum(w[v] for v in range(n) if (x >> v) & 1) >= t for x in range(N)])
    elif kind == 1:   # random monotone DNF of width 2-3
        f = np.zeros(N, dtype=bool)
        for _ in range(rng.randrange(2, 3 * n)):
            S = rng.sample(range(n), rng.choice((2, 2, 3))); m = sum(1 << v for v in S)
            f |= (idx & m) == m
    else:             # random tribes-like read-once DNF
        perm = list(range(n)); rng.shuffle(perm); f = np.zeros(N, dtype=bool); i = 0
        while i < n:
            k = rng.choice((2, 3, 4)); S = perm[i:i + k]; i += k; m = sum(1 << v for v in S)
            f |= (idx & m) == m
    if f.all() or not f.any(): f[N - 1] = True; f[0] = False
    G = fwht(np.where(f, -1.0, 1.0)) / N
    def val(G):
        s = stats(G, n, pc, low)
        if s is None: return -1.0
        return s['R'] / s['I'] if obj == 'R' else s['H'] / s['I']
    cur = val(G); best = (cur, f.copy())
    T0 = 0.05
    fl = f.tolist()
    ones = [[v for v in range(n) if (x >> v) & 1] for x in range(N)]
    zeros = [[v for v in range(n) if not (x >> v) & 1] for x in range(N)]
    for s in range(steps):
        x = rng.randrange(N)
        if fl[x]:
            if x == N - 1 or any(fl[x ^ (1 << v)] for v in ones[x]): continue
            delta = 2.0          # F(x) goes from -1 to +1
        else:
            if x == 0 or not all(fl[x | (1 << v)] for v in zeros[x]): continue
            delta = -2.0
        chi = sign[idx & x]
        G2 = G + (delta / N) * chi
        sc = val(G2)
        T = T0 * (1 - s / steps) + 1e-4
        if sc >= cur or rng.random() < math.exp((sc - cur) / T):
            f[x] = not f[x]; fl[x] = not fl[x]; G = G2; cur = sc
            if sc > best[0]: best = (sc, f.copy())
        if s % 50000 == 0 and s:     # re-anchor against rounding drift
            G = fwht(np.where(f, -1.0, 1.0)) / N; cur = val(G)
    return best

if __name__ == '__main__':
    try:
        import psutil; p = psutil.Process(); p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); p.cpu_affinity(list(range(2, 16)))
    except Exception: pass
    plan = [(10, 'R', 1000000, 4), (12, 'R', 600000, 4), (10, 'H', 1000000, 2), (12, 'H', 600000, 2),
            (14, 'R', 300000, 2)]
    keep = {}
    t0 = time.time()
    for n, obj, steps, seeds in plan:
        env = setup(n); top = (-1, None)
        for sd in range(seeds):
            sc, f = anneal(n, obj, steps, 7919 * n + sd, env)
            G = fwht(np.where(f, -1.0, 1.0)) / (1 << n)
            s = stats(G, n, env[3], env[4], full=True)
            print('n %2d obj %s seed %d start %s: best %.4f | H/I %.4f R/I %.4f sumB/I %.4f rho0 %.4f | ones %d | %.0f s'
                  % (n, obj, sd, ('thr', 'dnf', 'tribes')[(7919 * n + sd) % 3], sc, s['H'] / s['I'], s['R'] / s['I'],
                     s['B'] / s['I'], s['rho0'], int(f.sum()), time.time() - t0), flush=True)
            if sc > top[0]: top = (sc, f)
        keep['n%d_%s' % (n, obj)] = top[1]
        print('n %2d obj %s: overall best %.4f' % (n, obj, top[0]), flush=True)
        np.savez_compressed('adv_local_best.npz', **keep)
    print('done in %.0f s' % (time.time() - t0))
