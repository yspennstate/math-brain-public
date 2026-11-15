#!/usr/bin/env python3
"""Independent double-precision substitution in Harangi (3), d=3."""
import itertools
import math
import os
import resource
import signal

os.environ["OMP_NUM_THREADS"] = "1"
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15
signal.alarm(120)

p = (0.2493, 0.2778, 0.2880, 0.1849)
q = (0.1184, 0.5947, 0.8876, 0.9827)
lam, m = 19.3, 0.557
assert math.isclose(sum(p), 1, rel_tol=0, abs_tol=1e-15)
v = math.fsum(
    p[i] * p[j] * p[k]
    * (1 + (lam - 1) * (1 - q[i]) * (1 - q[j]) * (1 - q[k])) ** m
    for i, j, k in itertools.product(range(4), repeat=3)
)
e = math.fsum(
    p[i] * p[j] * (1 - (1 - 1 / lam) * q[i] * q[j]) ** m
    for i, j in itertools.product(range(4), repeat=2)
)
b = (math.log(v) - 1.5 * math.log(e)) / (m * math.log(lam))
print("nice =", os.getpriority(os.PRIO_PROCESS, 0))
print("ordered star terms = 64; ordered edge terms = 16")
print(f"V = {v:.17g}")
print(f"E = {e:.17g}")
print(f"B = {b:.17g}")
print(f"0.450789952 - B = {0.450789952 - b:.12g}")
assert b < 0.450789952
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1024**3  # macOS reports bytes.
print("peak RSS bytes =", rss)
