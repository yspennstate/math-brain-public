"""Exact optimal level-wise product reference cost for Maj3^{o d}: H(|S|) + E log2 C(3^d, |S|)
(optimal by transitivity + convexity, Theorem 1), versus H = 4(I-1), I = (3/2)^d.
|S| = Z_d, Galton-Watson with offspring 1 (prob 3/4) or 3 (prob 1/4). Also the proved lower bound (d-1) I."""
import math
import numpy as np
from scipy.special import gammaln
print(" d      n        I          H/I     LWopt/I   (d-1)   E[W log2 W]")
law = np.array([0.0, 1.0])           # Z_0 = 1
for d in range(1, 11):
    # Z_d = sum of Z_{d-1} iid offspring counts  <=>  law_d(k) via pgf: G_d(s) = G_{d-1}(3/4 s + 1/4 s^3) applied at root...
    # use Z_d = sum_{j=1}^{Z_1} Z_{d-1}^{(j)}: Z_1 in {1,3}
    L1 = law
    L3 = np.convolve(np.convolve(law, law), law)
    new = np.zeros(len(L3))
    new[:len(L1)] += 0.75 * L1
    new += 0.25 * L3
    law = new
    k = np.arange(len(law)); n = 3 ** d; I = 1.5 ** d
    m = law > 0
    Hs = -(law[m] * np.log2(law[m])).sum()
    lC = (gammaln(n + 1) - gammaln(k[m] + 1) - gammaln(n - k[m] + 1)) / math.log(2)
    LW = Hs + (law[m] * lC).sum()
    W = k[m] / I
    EWlogW = (law[m] * W * np.log2(np.where(W > 0, W, 1))).sum()
    H = 4 * (I - 1)
    print(f"{d:2d} {n:7d} {I:10.4f} {H/I:9.4f} {LW/I:9.4f} {d-1:6d} {EWlogW:9.4f}  (E|S|={float((law*k).sum()):.4f})")
