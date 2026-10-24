"""The p-substitution control, the sharpest available: same ratio, same lattice, only the bias differs.

Y_p = (1/3) sum_k B_k (2/3)^k with P(B=1) = p satisfies muhat_p(3k) = muhat_p(2k) for EVERY p, and for
p < 0.1153 the measure is singular (dim <= H(p)/log(3/2) < 1).  So any argument or estimator that
"works" identically at p = 1/2 and at p = 0.1 is proving too much and is wrong.

My closure of the window-shape lane rests on reading a LINEAR correlation integral, P(|D| <= r) ~ c r,
as the signature of an L^2 density.  Test that reading across p.  Expected: flat ratio at p = 1/2,
clearly growing ratio at p = 0.10 (singular, dim 0.8018), with p = 0.2113 -- the auxiliary bias that
appears in my exact second moment -- somewhere in between but still convergent.
"""
import numpy as np

def diff_ratio(p, K, radii):
    w0 = 1.0 - 2 * p * (1 - p)      # P(eta = 0)
    w1 = p * (1 - p)                # P(eta = +-1)
    steps = [(2 ** i) * (3 ** (K - i)) for i in range(K + 1)]
    half = int(sum(steps))
    size = 2 * half + 1
    q = np.zeros(size); q[half] = 1.0
    for s in steps:
        nq = w0 * q
        nq[s:] += w1 * q[:size - s]
        nq[:size - s] += w1 * q[s:]
        q = nq
    v = np.abs(np.arange(-half, half + 1))
    o = np.argsort(v, kind="stable")
    aS, qS = v[o], q[o]
    cum = np.cumsum(qS)
    P = 3.0 ** (K + 1)
    out = []
    for r in radii:
        j = np.searchsorted(aS, r * P, side="right")
        out.append(cum[j - 1] if j > 0 else 0.0)
    return out

K = 12
radii = [0.05, 0.02, 0.01, 0.005, 0.002]
print(f"exact lattice at depth K={K}; ratio P(|Y_p - Y'_p| <= r) / r")
print(f"{'p':>8} {'dim ratio':>10} " + " ".join(f"{'r='+str(r):>10}" for r in radii) + "   verdict")
from math import log
for p in (0.5, 0.2113, 0.15, 0.10, 0.05):
    H = -(p * log(p) + (1 - p) * log(1 - p))
    dim = H / log(1.5)
    vals = diff_ratio(p, K, radii)
    ratios = [v / r for v, r in zip(vals, radii)]
    trend = ratios[-1] / ratios[0]
    verdict = "flat (L^2 signature)" if trend < 1.15 else f"GROWING x{trend:.1f} (singular signature)"
    print(f"{p:>8.4f} {dim:>10.4f} " + " ".join(f"{x:>10.4f}" for x in ratios) + f"   {verdict}")
