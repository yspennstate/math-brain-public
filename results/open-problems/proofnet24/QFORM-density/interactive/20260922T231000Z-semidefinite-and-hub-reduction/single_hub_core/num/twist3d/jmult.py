# J_mult(theta) = int_{|y| <= 2/theta} J(y, theta*y) dy, the integral the hub-conditioned route needs above |eta| = 1/|x|
# (twist strength proportional to the partner frequency, kappa = theta*y, theta = eps/|x|). Compared with J_2(0).
import sys, math, time
import numpy as np
from jperp import rot
from j1check import setup, J

N = int(sys.argv[1]); thetas = [float(x) for x in sys.argv[2].split(",")]
R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3)))
S = setup(N, R); t0 = time.time()
da = 1.0 / (3.0 * S["rngL"])
for th in thetas:
    ymax = 2.0 / th if th > 0 else 8.0 / S["s"]
    ymax = min(ymax, 8.0 / S["s"] + 2.0 * np.abs(S["P"]).max())
    y = np.arange(0.0, ymax, da)
    vals = np.array([J(S, a, th * a) for a in y])
    tot = 2 * (vals.sum() - 0.5 * vals[0]) * da
    print("N=%d theta=%.3f  J_mult = %.3f  (y up to %.1f, %d values, %.0fs)" % (N, th, tot, ymax, len(y), time.time() - t0), flush=True)
