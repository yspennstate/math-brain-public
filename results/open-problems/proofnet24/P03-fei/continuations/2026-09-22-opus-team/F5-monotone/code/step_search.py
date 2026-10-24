"""Annealing search for LTFs maximising the heaviest-coordinate restriction ratio
Delta_1 H / Inf_1 (coordinate 1 = largest weight), and separately min_i Delta_i H / Inf_i.

Usage: python step_search.py n restarts steps seed mode   (mode = heavy | min | ratioHI)
"""
import sys, time
import numpy as np
from ltf_core import linform, ltf_table, spectrum, HI
from step_analysis import step_all


def evaluate(w, maxthr, mode):
    wf = w.astype(np.float64)
    v = np.unique(np.round(linform(wf), 9))
    mids = 0.5 * (v[:-1] + v[1:])
    if len(mids) > maxthr:
        k = maxthr // 4
        idx = np.unique(np.concatenate([np.arange(k), np.arange(len(mids) - k, len(mids)),
                                        np.linspace(0, len(mids) - 1, maxthr - 2 * k).astype(int)]))
        mids = mids[idx]
    n = len(w)
    hv = int(np.argmax(w))
    best = (-1.0, None)
    for th in mids:
        f = ltf_table(wf, th)
        c = spectrum(f)
        st = step_all(c, n)
        rel = st[:, 1] > 1e-13
        if not rel[hv]:
            continue
        r = st[:, 0] / np.maximum(st[:, 1], 1e-300)
        if mode == "heavy":
            val = r[hv]
        elif mode == "min":
            val = r[rel].min()
        else:
            H, I = HI(c)
            val = H / I
        if val > best[0]:
            H, I = HI(c)
            best = (val, (th, H, I, (1 - c[0]) / 2, r[hv], r[rel].min(), r[rel].max()))
    return best


def search(n, restarts, steps, seed, mode, wmax=12, maxthr=40):
    rng = np.random.default_rng(seed)
    glob = None
    for rs in range(restarts):
        w = rng.integers(1, wmax + 1, size=n)
        cur = evaluate(w, maxthr, mode)
        T = 0.1
        for s in range(steps):
            w2 = w.copy()
            i = rng.integers(n)
            w2[i] = max(0, w2[i] + rng.choice([-3, -1, 1, 3]))
            if rng.random() < 0.15:
                w2[rng.integers(n)] = rng.integers(0, 3 * wmax)
            if w2.max() == 0:
                continue
            cand = evaluate(w2, maxthr, mode)
            if cand[1] is None:
                continue
            if cand[0] > cur[0] or rng.random() < np.exp((cand[0] - cur[0]) / T):
                w, cur = w2, cand
            T *= 0.99
            if glob is None or cur[0] > glob[0][0]:
                glob = (cur, np.sort(w)[::-1].copy())
        th, H, I, p, rh, rmin, rmax = cur[1]
        print("restart %d: val %.5f | p=%.4g H/I=%.4f heavy=%.4f min=%.4f max=%.4f w=%s th=%.2f" % (
            rs, cur[0], p, H / I, rh, rmin, rmax, np.sort(w)[::-1].tolist(), th), flush=True)
    return glob


if __name__ == "__main__":
    n, restarts, steps, seed = map(int, sys.argv[1:5]); mode = sys.argv[5]
    t = time.time()
    g = search(n, restarts, steps, seed, mode)
    th, H, I, p, rh, rmin, rmax = g[0][1]
    print("BEST mode=%s n=%d val=%.6f p=%.5g H/I=%.5f heavy=%.5f min=%.5f max=%.5f w=%s (%.0fs)" % (
        mode, n, g[0][0], p, H / I, rh, rmin, rmax, g[1].tolist(), time.time() - t), flush=True)
