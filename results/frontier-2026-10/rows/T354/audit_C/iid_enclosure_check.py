"""Exact iid x*/x0 by the cumulant route (eps_moment_route.D) against remainder_iid.py's eight enclosures (agent C, T354)."""
import numpy as np
from scipy.optimize import brentq
from eps_moment_route import D
b = np.array([9.0] + [-1.0] * 9)
enc = {(0.9999, 0): (0.9994, 1.0014), (0.999, 0): (0.9935, 1.0169), (0.995, 0): (0.9504, 1.1444), (0.99, 0): (0.7548, 1.6140),
       (0.999, 0.9): (0.9936, 1.0169), (0.99, 0.9): (0.7726, 1.5826), (0.999, 0.99): (0.9939, 1.0164), (0.99, 0.99): (0.8324, 1.4857)}
for (b2, b1), (lo, hi) in enc.items():
    d = 1 - b2
    x0 = d * (1 - b1) / (1 - b1 * b2) * 4
    r = [brentq(lambda t: D(t, b, d, b1, 0.0, J), 0.3 * x0, 2 * x0, xtol=1e-17, rtol=1e-15) / x0 for J in (14, 20)]
    print("beta2 %-6s beta1 %-4s exact x*/x0 %.6f (J 20: %.6f)  enclosure [%.4f, %.4f]  %s"
          % (b2, b1, r[0], r[1], lo, hi, "inside" if lo <= r[1] <= hi else "OUTSIDE"), flush=True)
