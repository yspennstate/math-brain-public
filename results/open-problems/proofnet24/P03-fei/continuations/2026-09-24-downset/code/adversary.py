# Adversarial search against Lemma 2 / Theorem 2 of the down-set note: simulated annealing over monotone Boolean
# functions on n variables (moves keep monotonicity: switch a maximal zero on or a minimal one off), maximizing
#     R(f) = max_v Delta_v / (Inf_v (2/ln2 + c0 + Psi(4m/Inf_v - 2)))      (Theorem 2; must stay < 1)
# and separately the erasure form  max_v B_v / (Inf_v (c0 + Psi(4m/Inf_v - 2)))  (Lemma 2; must stay < 1).
import sys, math, random, numpy as np

C0 = 2 * math.exp(-0.5) / math.log(2); JSC = 2 / math.log(2)

def fwht(a):
    a = a.copy(); N = a.shape[0]; h = 1
    while h < N:
        a = a.reshape(-1, 2, h); u = a[:, 0, :].copy(); w = a[:, 1, :]
        a[:, 0, :] = u + w; a[:, 1, :] = u - w; a = a.reshape(N); h *= 2
    return a

def phi(p):
    out = np.zeros_like(p); nz = p > 1e-300; out[nz] = -p[nz] * np.log2(p[nz]); return out

def Psi(r):
    r = np.maximum(r, 0.0); return np.log2(np.e * (r + 2 * np.sqrt(r) + 2))

def score(f, n, idx0s, mode):
    N = 1 << n
    G = fwht(np.where(f, -1.0, 1.0)) / N
    q = (1 + G[0]) / 2; m = min(q, 1 - q)
    if m <= 1e-12: return 0.0, None
    P = G * G; H = phi(P).sum()
    best = (0.0, None)
    for v in range(n):
        i0 = idx0s[v]; a = G[i0]; b = G[i0 | (1 << v)]
        inf = (b * b).sum()
        if inf < 1e-12: continue
        if mode == 'delta':
            val = H - 0.5 * (phi((a + b) ** 2) + phi((a - b) ** 2)).sum()
            bound = inf * (JSC + C0 + Psi(4 * m / inf - 2))
        else:
            val = H - phi(a * a + b * b).sum()
            bound = inf * (C0 + Psi(4 * m / inf - 2))
        r = val / bound
        if r > best[0]: best = (float(r), v)
    return best

def anneal(n, mode, steps, seed):
    rng = random.Random(seed); N = 1 << n
    idx = np.arange(N)
    idx0s = [idx[((idx >> v) & 1) == 0] for v in range(n)]
    up = [[x | (1 << v) for v in range(n) if not (x >> v) & 1] for x in range(N)]
    dn = [[x & ~(1 << v) for v in range(n) if (x >> v) & 1] for x in range(N)]
    # random start: threshold of random weights
    w = np.array([rng.random() for _ in range(n)]); t = rng.uniform(0.2, 0.8) * w.sum()
    f = np.array([sum(w[v] for v in range(n) if (x >> v) & 1) >= t for x in range(N)])
    cur, _ = score(f, n, idx0s, mode); best = (cur, f.copy())
    T0 = 0.05
    for s in range(steps):
        x = rng.randrange(N)
        if f[x] and all(not f[y] for y in dn[x]) and x != N - 1: newval = False
        elif (not f[x]) and all(f[y] for y in up[x]) and x != 0: newval = True
        else: continue
        f[x] = newval
        sc, _ = score(f, n, idx0s, mode)
        T = T0 * (1 - s / steps) + 1e-4
        if sc >= cur or rng.random() < math.exp((sc - cur) / T):
            cur = sc
            if sc > best[0]: best = (sc, f.copy())
        else:
            f[x] = not newval
    return best

if __name__ == '__main__':
    try:
        import psutil; p = psutil.Process(); p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); p.cpu_affinity(list(range(2, 16)))
    except Exception: pass
    n = int(sys.argv[1]); mode = sys.argv[2]; steps = int(sys.argv[3]); seeds = int(sys.argv[4])
    overall = 0.0
    for sd in range(seeds):
        sc, f = anneal(n, mode, steps, 1000 * n + sd)
        overall = max(overall, sc)
        print('n %d mode %s seed %d: best ratio %.6f  (|f^-1(1)| = %d)' % (n, mode, sd, sc, int(f.sum())), flush=True)
    print('n %d mode %s: overall best ratio %.6f' % (n, mode, overall))
