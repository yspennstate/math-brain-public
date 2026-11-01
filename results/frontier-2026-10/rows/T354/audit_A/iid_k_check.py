# Independent check of K under iid sampling (agent A, 20 Oct).
# First order in dv: E[m dv] = (1-b1)(1-b2) sum_i b1^i b2^i C  ->  K_iid = (1-b1)/(1-b1 b2), not 1.
# Frozen x = 0, n = 10, b = (9,-1,...,-1), a = 1: V0 = 9, m3 = 72; D(0) = -V0^-1/2 (1-b2) K m3 / (2 V0).
import sys, numpy as np
from scipy.signal import lfilter
b1, b2 = float(sys.argv[1]), float(sys.argv[2]); T = int(float(sys.argv[3])); seeds = int(sys.argv[4])
b = np.array([9.0] + [-1.0]*9); V0 = np.mean(b**2); m3 = np.mean(b**3)
est = []
for s in range(seeds):
    rng = np.random.default_rng(s)
    g = b[rng.integers(0, 10, T)]
    m = lfilter([1-b1], [1, -b1], g); v = lfilter([1-b2], [1, -b2], g*g)
    burn = int(50/(1-min(b1, b2)) + 50/(1-max(b1, b2)))
    est.append(np.mean(m[burn:]/np.sqrt(v[burn:])))
est = np.array(est); D = est.mean(); se = est.std(ddof=1)/np.sqrt(seeds)
pred = lambda K: -V0**-0.5*(1-b2)*K*m3/(2*V0)
Kx = (1-b1)/(1-b1*b2)
print(f"iid b1 {b1} b2 {b2}: sim D(0) {D:.5f} +/- {se:.5f} | first order K=1 {pred(1):.5f}, K=(1-b1)/(1-b1 b2)={Kx:.4f} {pred(Kx):.5f} | sim K {D/pred(1):.4f}")
