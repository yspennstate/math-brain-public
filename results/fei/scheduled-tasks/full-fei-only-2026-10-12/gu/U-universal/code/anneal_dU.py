"""Search for Boolean f and coordinate i with large Delta_i U / Inf_i (EVIDENCE)."""
import numpy as np, json, time, sys
from feilib import spectrum, influences, restrict, nbits
from upward import Uprime

def local_ratios(t, n):
    p = spectrum(t); inf = influences(p, n); U = float(Uprime(p, n))
    tp = np.stack([restrict(t, n, i, 0) for i in range(n)]); tm = np.stack([restrict(t, n, i, 1) for i in range(n)])
    Up = Uprime(spectrum(tp), n - 1); Um = Uprime(spectrum(tm), n - 1)
    D = U - 0.5 * (Up + Um)
    rel = inf > 1e-12
    if not rel.any(): return None
    r = np.where(rel, D / np.where(rel, inf, 1), -np.inf)
    return r

def anneal(n, mode, steps, seed, T0=0.5):
    rng = np.random.default_rng(seed); N = 1 << n
    t = rng.choice([-1, 1], size=N)
    def score(t):
        r = local_ratios(t, n)
        if r is None: return None
        return float(r.max()) if mode == 'max' else float(np.min(np.where(np.isfinite(r), r, np.inf)))
    cur = score(t)
    while cur is None: t = rng.choice([-1, 1], size=N); cur = score(t)
    best = (cur, t.copy())
    for s in range(steps):
        T = T0 * (1 - s / steps) + 1e-3
        k = rng.integers(N); t[k] *= -1
        new = score(t)
        if new is None or (new < cur and rng.random() > np.exp((new - cur) / T)):
            t[k] *= -1; continue
        cur = new
        if cur > best[0]: best = (cur, t.copy())
    return best

if __name__ == "__main__":
    out = {}; t0 = time.time()
    for n in [5, 6, 7]:
        for mode in ['max', 'min']:
            b = None
            for seed in range(3):
                c = anneal(n, mode, 3000 if n < 7 else 2000, seed)
                if b is None or c[0] > b[0]: b = c
            out[f"{n}_{mode}"] = dict(val=b[0], table=b[1].tolist())
            print(n, mode, round(b[0], 4), round(time.time() - t0, 1), flush=True)
    json.dump(out, open("../data/anneal_dU.json", "w"))
