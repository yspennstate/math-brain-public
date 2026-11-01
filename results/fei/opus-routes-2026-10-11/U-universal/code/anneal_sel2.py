"""Continue selector annealing at n=9,10 seeded from the n-1 maximiser (dummy-variable extension)."""
import numpy as np, json, time
from feilib import spectrum
from upward import Uprime
def Ufun(t, n): return float(Uprime(spectrum(t), n))
def val(g, h, n):
    M = len(g); f = np.empty(2 * M, dtype=np.int64); f[0::2] = g; f[1::2] = h
    inf = np.mean(g != h)
    if inf == 0: return None
    return (Ufun(f, n) - 0.5 * (Ufun(g, n - 1) + Ufun(h, n - 1))) / inf
def run(n, g, h, steps, seed, T0=0.15):
    rng = np.random.default_rng(seed); M = len(g)
    cur = val(g, h, n); best = (cur, g.copy(), h.copy())
    for s in range(steps):
        T = T0 * (1 - s / steps) + 1e-3
        k = rng.integers(M); which = rng.integers(3)
        if which != 1: g[k] *= -1
        if which != 0: h[k] *= -1
        new = val(g, h, n)
        if new is None or (new < cur and rng.random() > np.exp((new - cur) / T)):
            if which != 1: g[k] *= -1
            if which != 0: h[k] *= -1
            continue
        cur = new
        if cur > best[0]: best = (cur, g.copy(), h.copy())
    return best
d = json.load(open("../data/anneal_sel.json")); out = {}
g = np.array(d["8"]["g"]); h = np.array(d["8"]["h"]); t0 = time.time()
for n in [9, 10]:
    g = np.concatenate([g, g]); h = np.concatenate([h, h])   # new top coordinate is dummy
    b = None
    for seed in range(3):
        c = run(n, g.copy(), h.copy(), 5000, seed)
        if b is None or c[0] > b[0]: b = c
    g, h = b[1], b[2]; out[n] = dict(val=b[0], g=g.tolist(), h=h.tolist())
    print(n, round(b[0], 4), 'Inf_y', np.mean(g != h), round(time.time() - t0, 1), flush=True)
json.dump(out, open("../data/anneal_sel2.json", "w"))
