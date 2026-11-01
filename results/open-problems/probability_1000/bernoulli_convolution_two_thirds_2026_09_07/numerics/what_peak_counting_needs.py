"""What would the peak-counting route have to prove? A Chernoff bound is not enough, by 1.29^K.

The route: cover [1,2], bound P_K on each piece, sum height x measure. A peak where a fraction alpha of
the K constraints ||t lam_m|| < delta are met has height about 2^(alpha K). If the constraints behaved
INDEPENDENTLY, the measure of the set meeting at least alpha K of them would be about exp(-K D(alpha||p0))
with p0 = 2 delta, by Chernoff. The contribution of that level is then (2^alpha exp(-D))^K, and the route
succeeds only if that is <= 1 for every alpha.
Compute the worst alpha. Then compare with the TRUE carrier measure, 0.7119^K, derived earlier from the
measured height and width exponents.
"""
import numpy as np
from math import log, exp

def D(a, p):
    a = min(max(a, 1e-12), 1-1e-12)
    return a*log(a/p) + (1-a)*log((1-a)/(1-p))

for delta in (0.10, 0.15, 0.20):
    p0 = 2*delta
    best_a, best_f = None, -9
    for a in np.linspace(p0+1e-6, 0.999, 4000):
        f = a*log(2) - D(a, p0)
        if f > best_f: best_f, best_a = f, a
    print(f"delta={delta:.2f} (p0={p0:.2f}): worst alpha={best_a:.3f}, growth exp({best_f:+.4f})^K = {exp(best_f):.4f}^K")
print()
print("Every choice gives growth > 1, so an independence/Chernoff measure bound does NOT close the route.")
print()
h, meas = 1.4046, 0.7119
print(f"The TRUE numbers: height {h}^K on a carrier of measure {meas}^K, product {h*meas:.5f}^K")
print("  (that product is 1 by construction - it is the flatness of I_K, not an independent fact).")
print()
print("So the route needs the carrier measure to be as small as 0.7119^K, while independence gives only")
for delta in (0.10,0.15,0.20):
    p0=2*delta; a=0.5
    print(f"   delta={delta:.2f}: exp(-D(0.5||{p0:.2f})) = {exp(-D(0.5,p0)):.4f}^K at alpha=1/2")
print("The gap between those and 0.7119 is the correlation the proof would have to supply - the")
print("constraints must be shown POSITIVELY correlated at a precise rate, not merely counted.")
