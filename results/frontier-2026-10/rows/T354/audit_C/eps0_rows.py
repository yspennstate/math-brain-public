"""eps = 0 rows of the next-order section, by the cumulant route of eps_moment_route.py (agent C, T354 audit)."""
import numpy as np
from scipy.optimize import brentq
from eps_moment_route import D, pred
models = {"test": np.array([9.0] + [-1.0] * 9), "three": np.array([6.0, 2.0] + [-1.0] * 8)}
for mname, fam in (("test", "b1_0"), ("test", "r0.1"), ("test", "r1"), ("three", "b1_0"), ("three", "r0.1")):
    b, row = models[mname], []
    for d in (0.002, 0.001, 0.0005):
        b1 = 0.0 if fam == "b1_0" else 1 - d / (0.1 if fam == "r0.1" else 1.0)
        x0, br = pred(b, d, b1, 0.0)
        xs = brentq(lambda t: D(t, b, d, b1, 0.0), 0.3 * x0, 2 * x0, xtol=1e-17, rtol=1e-15)
        row.append((d, (xs / x0 - 1) / d, br))
    print("%-5s eps 0  %-4s " % (mname, fam) + "  ".join("d %g exact %.4f pred %.4f" % t for t in row)
          + "  Richardson %.4f" % (2 * row[2][1] - row[1][1]), flush=True)
