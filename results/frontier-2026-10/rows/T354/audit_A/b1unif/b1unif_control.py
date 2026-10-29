"""Negative control for b1unif_enum.py: w = (decreasing beta1 weights) + t * (one-hot at a middle lag), t chosen so that the
signed S is exactly 0. Not comonotone. If |e2| <= C d S needed no comonotonicity, e2 would vanish here; it does not.
usage: python b1unif_control.py"""
import numpy as np
from b1unif_enum import run
for b in ([4, -1, -1, -1, -1], [3, 1, -1, -1, -1, -1]):
    n = len(b)
    for d, beta2, b1 in ((0.01, 0.8, 0.5), (0.01, 0.95, 0.9), (0.002, 0.8, 0.5)):
        w1 = lambda L: (1-b1)*b1**L
        a_ep = beta2**np.arange(n); q0 = int(np.argmin(abs(a_ep - a_ep.mean())))
        w2 = lambda L: (L == q0).astype(float)
        import io, contextlib
        with contextlib.redirect_stdout(io.StringIO()):
            _, S1 = run(b, d, beta2, w1, ""); _, S2 = run(b, d, beta2, w2, "")
        t = -S1/S2
        run(b, d, beta2, lambda L: w1(L) + t*w2(L), f"S=0 mix t {t:.3f} b1 {b1}")
