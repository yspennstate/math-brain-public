"""Simulate the probability that the origin is still uncovered at time t in the
planar inertial Boolean model with unit speeds and uniform directions, and
compare it with exp(-lambda*(pi r^2 + 2 r t)) from Lemma 2.1."""
import math
import numpy as np

rng = np.random.default_rng(20261116)
lam, r, reps = 0.4, 0.5, 12000
print(" t   simulated   exp(-lam(pi r^2+2rt))   std.err")
for t in (0.0, 1.0, 2.0, 5.0):
    R = r + t
    miss = 0
    for _ in range(reps):
        n = rng.poisson(lam * (2 * R) ** 2)
        x = rng.uniform(-R, R, (n, 2))
        th = rng.uniform(0, 2 * math.pi, n)
        v = np.column_stack((np.cos(th), np.sin(th)))
        s = np.clip(-np.sum(x * v, axis=1), 0.0, t)
        p = x + s[:, None] * v
        miss += not np.any(np.sum(p * p, axis=1) <= r * r)
    q = math.exp(-lam * (math.pi * r * r + 2 * r * t))
    se = math.sqrt(q * (1 - q) / reps)
    print(f"{t:3.0f}   {miss / reps:.4f}      {q:.4f}                  {se:.4f}")
