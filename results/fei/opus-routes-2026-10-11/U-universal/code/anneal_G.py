"""Anneal to maximise G(f)/I(f), G = sum_i Delta_i U.  Counterexample hunt for the global inequality (GU). EVIDENCE."""
import numpy as np, json, time
from feilib import spectrum, influences, restrict
from upward import Uprime

def GI(t, n):
    p = spectrum(t); inf = influences(p, n); I = float(inf.sum())
    if I < 1e-12: return None
    U = float(Uprime(p, n))
    tp = np.stack([restrict(t, n, i, 0) for i in range(n)]); tm = np.stack([restrict(t, n, i, 1) for i in range(n)])
    D = U - 0.5 * (Uprime(spectrum(tp), n - 1) + Uprime(spectrum(tm), n - 1))
    return float(D.sum()) / I

def run(n, t, steps, seed, T0=0.3):
    rng = np.random.default_rng(seed); N = len(t)
    cur = GI(t, n)
    while cur is None: t = rng.choice([-1, 1], size=N); cur = GI(t, n)
    best = (cur, t.copy())
    for s in range(steps):
        T = T0 * (1 - s / steps) + 1e-3
        k = rng.integers(N); t[k] *= -1
        new = GI(t, n)
        if new is None or (new < cur and rng.random() > np.exp((new - cur) / T)):
            t[k] *= -1; continue
        cur = new
        if cur > best[0]: best = (cur, t.copy())
    return best

if __name__ == "__main__":
    out = {}; t0 = time.time(); prev = None
    for n in [5, 6, 7, 8]:
        b = None
        seeds = [np.random.default_rng(100 + s).choice([-1, 1], size=1 << n) for s in range(3)]
        if prev is not None: seeds.append(np.concatenate([prev, prev]))
        for si, t in enumerate(seeds):
            c = run(n, t.copy(), 3000 if n < 8 else 2000, si)
            if b is None or c[0] > b[0]: b = c
        prev = b[1]; out[n] = dict(val=b[0], table=b[1].tolist())
        print(n, round(b[0], 4), round(time.time() - t0, 1), flush=True)
    json.dump(out, open("../data/anneal_G.json", "w"))
