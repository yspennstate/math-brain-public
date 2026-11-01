"""Anneal over selector pairs f(y,x)=g(x) if y=+1 else h(x) to maximise Delta_y U / Inf_y (EVIDENCE)."""
import numpy as np, json, time, sys
from feilib import spectrum
from upward import Uprime

def Ufun(t, n): return float(Uprime(spectrum(t), n))

def run(n, steps, seed, T0=0.4):
    rng = np.random.default_rng(seed); M = 1 << (n - 1)
    g = rng.choice([-1, 1], size=M); h = g.copy(); h[rng.integers(M)] *= -1
    def val(g, h):
        f = np.empty(2 * M, dtype=np.int64); f[0::2] = g; f[1::2] = h  # bit0 = y
        inf = np.mean(g != h)
        if inf == 0: return None, None, None
        Ug, Uh = Ufun(g, n - 1), Ufun(h, n - 1)
        return (Ufun(f, n) - 0.5 * (Ug + Uh)) / inf, Ug, Uh
    cur, _, _ = val(g, h); best = (cur, g.copy(), h.copy())
    for s in range(steps):
        T = T0 * (1 - s / steps) + 1e-3
        k = rng.integers(M); which = rng.integers(3)
        if which == 0: g[k] *= -1
        elif which == 1: h[k] *= -1
        else: g[k] *= -1; h[k] *= -1
        new, _, _ = val(g, h)
        if new is None or (new < cur and rng.random() > np.exp((new - cur) / T)):
            if which == 0: g[k] *= -1
            elif which == 1: h[k] *= -1
            else: g[k] *= -1; h[k] *= -1
            continue
        cur = new
        if cur > best[0]: best = (cur, g.copy(), h.copy())
    return best

if __name__ == "__main__":
    out = {}; t0 = time.time()
    for n in [6, 7, 8, 9]:
        b = None
        for seed in range(4):
            c = run(n, 6000 if n < 9 else 4000, seed)
            if b is None or c[0] > b[0]: b = c
        out[n] = dict(val=b[0], g=b[1].tolist(), h=b[2].tolist())
        print(n, round(b[0], 4), 'Inf_y', np.mean(b[1] != b[2]), round(time.time() - t0, 1), flush=True)
    json.dump(out, open("../data/anneal_sel.json", "w"))
