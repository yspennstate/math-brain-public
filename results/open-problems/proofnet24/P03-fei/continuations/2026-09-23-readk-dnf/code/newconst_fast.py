"""Same as newconst.py with scipy (float64 cdf; tau values only enter as k*sup m*tau(m)).
Cross-checked against exact integer sums for m <= 300."""
import numpy as np
from scipy.stats import binom
from math import comb
LOG2E = 1 / np.log(2)

def tau_table(beta, mmax=6000):
    m = np.arange(1, mmax + 1)
    thr = m / beta - 1
    # Pr[Bin(m-1,1/2) < thr] = cdf(ceil(thr)-1)
    kk = np.ceil(thr) - 1
    t = np.where(kk >= 0, binom.cdf(kk, m - 1, 0.5), 0.0)
    return np.concatenate([[0.0], t])

def exact_tau(beta, m):
    thr = m / beta - 1
    s = sum(comb(m - 1, j) for j in range(0, m) if j < thr)
    return s / 2 ** (m - 1)

for b in (2.1, 3.0):
    t = tau_table(b)
    err = max(abs(t[m] - exact_tau(b, m)) for m in range(1, 301))
    print(f"check beta={b}: max |float - exact| over m<=300 = {err:.2e}")

def M_of(beta, ks, mmax=6000):
    t = tau_table(beta, mmax)
    mt = np.arange(mmax + 1) * t
    T = np.maximum.accumulate(mt[::-1])[::-1]
    w = np.arange(1, mmax + 1)
    return {k: float(np.max(np.minimum(w, k * T[1:]))) for k in ks}, float(mt[-100:].max())

ks = [1, 2, 3, 4, 5, 8, 10, 16, 32, 64, 100, 1000, 10000]
betas = [2.05, 2.1, 2.15, 2.2, 2.3, 2.4, 2.5, 2.75, 3.0, 3.5, 4.0, 5.0, 6.0, 8.0]
Ms = {}
for b in betas:
    Ms[b], tail = M_of(b, ks)
    print(f"beta={b}: tail {tail:.1e}; M: " + ", ".join(f"{k}:{Ms[b][k]:.1f}" for k in ks))
cs = np.linspace(0.05, 4, 400)
print()
for k in ks:
    bestF = min((2.886 + 2 + (np.exp(c) - 1) * LOG2E + np.log2(k / c) + 2 * (b - 1) * k + 2 * Ms[b][k], b, c) for b in betas for c in cs)
    bestP = min((2 * LOG2E + 8 + 2 + 2 * (np.exp(c) - 1) * LOG2E + np.log2(k / c) + 2 * (b - 1) * k + 2 * max(np.log2(k) + 2, 2 * Ms[b][k]), b, c) for b in betas for c in cs)
    print(f"k={k:6d}: FEI new {bestF[0]:10.2f} (beta {bestF[1]}, c {bestF[2]:.2f}) old {2.886 + 9.898 * k:10.2f} | FEI+ new {bestP[0]:10.2f} (beta {bestP[1]}, c {bestP[2]:.2f}) old {10.9 + 14 * k:10.2f}")
