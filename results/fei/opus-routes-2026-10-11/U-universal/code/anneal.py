"""Simulated annealing over truth tables to maximise a target functional (EVIDENCE only)."""
import numpy as np, sys, json, time
from feilib import spectrum, entropy, influences, erasure_terms, binh

def objectives(t, n):
    p = spectrum(t); H = float(entropy(p)); inf = influences(p, n); I = float(inf.sum())
    if I <= 1e-12: return None
    Bi = erasure_terms(p, n); B = float(Bi.sum())
    rel = inf > 1e-12
    loc = float((Bi[rel] / inf[rel]).min())
    return dict(HI=H / I, HDTC=H / (I + H - B), loc=loc, BI=B / I)

def anneal(n, key, steps, seed, T0=0.3):
    rng = np.random.default_rng(seed)
    N = 1 << n
    t = rng.choice([-1, 1], size=N)
    cur = objectives(t, n)
    while cur is None:
        t = rng.choice([-1, 1], size=N); cur = objectives(t, n)
    best = (cur[key], t.copy(), cur)
    for s in range(steps):
        T = T0 * (1 - s / steps) + 1e-3
        k = rng.integers(N); t[k] *= -1
        new = objectives(t, n)
        if new is None or (new[key] < cur[key] and rng.random() > np.exp((new[key] - cur[key]) / T)):
            t[k] *= -1; continue
        cur = new
        if cur[key] > best[0]: best = (cur[key], t.copy(), dict(cur))
    return best

if __name__ == "__main__":
    out = {}
    t0 = time.time()
    for n in [5, 6, 7]:
        for key in ["HI", "HDTC", "loc"]:
            bestall = None
            for seed in range(3):
                b = anneal(n, key, 4000 if n < 7 else 2500, seed)
                if bestall is None or b[0] > bestall[0]: bestall = b
            out[f"{n}_{key}"] = dict(val=bestall[0], obj=bestall[2], table=bestall[1].tolist())
            print(n, key, round(bestall[0], 4), {k: round(v, 3) for k, v in bestall[2].items()}, round(time.time() - t0, 1), flush=True)
    json.dump(out, open("../data/anneal_n5_7.json", "w"))
