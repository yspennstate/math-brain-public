"""Hill climbing / annealing over integer weight vectors and thresholds to maximise H/I of an LTF.

Usage: python local_search.py n restarts steps seed [wmax]
An LTF is f = +1 iff w.x > theta; theta is placed halfway between consecutive distinct values of
w.x, so every candidate is a genuine threshold function without ties.
"""
import sys, time
import numpy as np
from ltf_core import linform, spectrum, HI, ltf_table


def eval_all_thresholds(w, maxthr=None, rng=None):
    """Return list of (ratio, theta, H, I, p) for thresholds between distinct values of w.x."""
    v = np.unique(np.round(linform(w.astype(np.float64)), 9))
    mids = 0.5 * (v[:-1] + v[1:])
    if maxthr is not None and len(mids) > maxthr:
        # keep extremes (rare events) and a spread of interior thresholds
        k = maxthr // 4
        idx = np.unique(np.concatenate([np.arange(k), np.arange(len(mids) - k, len(mids)),
                                        np.linspace(0, len(mids) - 1, maxthr - 2 * k).astype(int)]))
        mids = mids[idx]
    out = []
    for th in mids:
        f = ltf_table(w.astype(np.float64), th)
        c = spectrum(f)
        H, I = HI(c)
        if I > 0:
            p = (1 - c[0]) / 2
            out.append((H / I, th, H, I, p))
    return out


def best_threshold(w, maxthr):
    r = eval_all_thresholds(w, maxthr)
    if not r:
        return (0.0, 0.0, 0.0, 0.0, 0.0)
    return max(r, key=lambda t: t[0])


def search(n, restarts, steps, seed, wmax=12, maxthr=48):
    rng = np.random.default_rng(seed)
    best_overall = None
    for r in range(restarts):
        w = rng.integers(1, wmax + 1, size=n)
        cur = best_threshold(w, maxthr)
        T = 0.05
        for s in range(steps):
            w2 = w.copy()
            i = rng.integers(n)
            w2[i] = max(0, w2[i] + rng.choice([-2, -1, 1, 2]))
            if rng.random() < 0.2:
                j = rng.integers(n)
                w2[j] = rng.integers(0, wmax + 1)
            if w2.sum() == 0:
                continue
            cand = best_threshold(w2, maxthr)
            if cand[0] > cur[0] or rng.random() < np.exp((cand[0] - cur[0]) / T):
                w, cur = w2, cand
            T *= 0.995
            if best_overall is None or cur[0] > best_overall[0][0]:
                best_overall = (cur, np.sort(w)[::-1].copy())
        print("restart %d: ratio %.6f p=%.4g H=%.5g I=%.5g w=%s" % (
            r, cur[0], cur[4], cur[2], cur[3], np.sort(w)[::-1].tolist()), flush=True)
    return best_overall


if __name__ == "__main__":
    n = int(sys.argv[1]); restarts = int(sys.argv[2]); steps = int(sys.argv[3]); seed = int(sys.argv[4])
    wmax = int(sys.argv[5]) if len(sys.argv) > 5 else 12
    t = time.time()
    b = search(n, restarts, steps, seed, wmax)
    print("BEST n=%d ratio=%.8f p=%.5g H=%.6g I=%.6g theta=%.4f w=%s  (%.1fs)" % (
        n, b[0][0], b[0][4], b[0][2], b[0][3], b[0][1], b[1].tolist(), time.time() - t))
