"""Framing-independent check of the solver on the survey's nilpotent pair: exp(B0 h) = [[1,h],[0,1]],
exp(B1 h) = [[1,0],[-h,1]] exactly, so the switched flow is a plain product of shears."""
import numpy as np, math
rng = np.random.default_rng(5)
def mc(r, nseg=600000):
    x, y = 1.0, 0.3; logR = 0.0; T = 0.0; i = 0
    for h in rng.exponential(1.0/r, nseg):
        if i == 0: x = x + h*y
        else:      y = y - h*x
        n = math.hypot(x, y); logR += math.log(n); x /= n; y /= n; T += h; i = 1 - i
    return logR / T
for r in [0.1, 0.25, 0.5, 1.0, 4.6]:
    print(f"r={r:4.2f}: Monte Carlo growth rate {mc(r):+.4f}   (solver: 0.1674, ~0.20, 0.1665, 0.1082, 0.0269 at 0.1/0.25/0.5/1/4.6)")
