"""The single hub in the spread regime: does the density of Q = 2 X_h L + lambda V^2 + 2 eps L P grow with the number m
of light coordinates? Same exact-in-hub window estimator as small_eps.py (delta = 0.002, maximum over a grid of y), comb
light laws (8 teeth of width 1/8 at the integers, centred), one random orthonormal frame per m (redrawn until
w_i^2 + v_i^2 <= 1/2), and the rough hub (a random half of the cells of length eps in [0, 2]) or the uniform hub.
Proposition 3.17 allows growth like log m; the conjecture says there is none. small_eps is reloaded before every entry
so that each entry starts from the same seed; the frame is fixed per m."""
import sys, importlib
import numpy as np
import small_eps as se

def entry(m, hubkind, eps, nsamp):
    importlib.reload(se)
    while True:
        w, v, p = se.frames("random", m)
        if np.max(w ** 2 + v ** 2) <= 0.5:
            break
    se.frames = lambda kind, mm: (w, v, p)
    d, y = se.peak(eps, hubkind, "comb", "random", m, nsamp=nsamp, B=100_000)
    return d, float(np.max(np.abs(w)))

if __name__ == "__main__":
    ms = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [8, 32, 128]
    nsamp = int(sys.argv[2]) if len(sys.argv) > 2 else 1_000_000
    for m in ms:
        for hubkind in ("rough", "unif"):
            row = []
            for eps in (0.01, 0.001):
                d, wmax = entry(m, hubkind, eps, nsamp)
                row.append("eps=%g: %.3f" % (eps, d))
            print("m=%4d  max|w_i| %.2f  %-5s hub  %s" % (m, wmax, hubkind, "   ".join(row)), flush=True)
