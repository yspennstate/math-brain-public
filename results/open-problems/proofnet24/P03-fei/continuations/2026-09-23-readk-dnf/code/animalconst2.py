"""Simplified constants (|V(U)| <= V_tot <= beta k s + W):
FEI : C(k)  = 11.384 + beta + log2 k + log2(beta k + 1) + log2(beta k) + K2 M_beta(k)
FEI+: C'(k) = 13.771 + 7.055 + beta + log2 k + log2(beta k + 1) + log2(beta k) + K2 max(log2 k + 2, 2 M_beta(k))
K2 = 1 + log2e (1/(beta k + 1) + 1/(beta k)).  Checks A + B log2 k envelopes on a dense grid of k."""
import numpy as np
from scipy.stats import binom
L2E = 1 / np.log(2)
betas = [3, 3.5, 4, 5, 6, 7, 8, 9, 10, 12, 14, 16, 20, 24, 28, 32]
ks = sorted(set([int(round(x)) for x in np.logspace(0, 6, 400)]))
mmax = 40000
m = np.arange(1, mmax + 1)
Tt = {}
for b in betas:
    kk = np.ceil(m / b - 1) - 1
    t = np.where(kk >= 0, binom.cdf(kk, m - 1, 0.5), 0.0)
    mt = m * t
    assert mt[-500:].max() < 1e-9
    Tt[b] = np.maximum.accumulate(mt[::-1])[::-1]
def M(b, k): return float(np.max(np.minimum(m, k * Tt[b])))
def CF(k, b):
    K2 = 1 + L2E * (1 / (b * k + 1) + 1 / (b * k))
    return 11.384 + b + np.log2(k) + np.log2(b * k + 1) + np.log2(b * k) + K2 * M(b, k)
def CP(k, b):
    K2 = 1 + L2E * (1 / (b * k + 1) + 1 / (b * k))
    return 20.826 + b + np.log2(k) + np.log2(b * k + 1) + np.log2(b * k) + K2 * max(np.log2(k) + 2, 2 * M(b, k))
F = np.array([min(CF(k, b) for b in betas) for k in ks]); Pp = np.array([min(CP(k, b) for b in betas) for k in ks])
lk = np.log2(np.array(ks, dtype=float))
for A in (20, 21, 22, 24):
    B = max((F - A) / np.maximum(lk, 1e-9))
    print(f"FEI : C(k) <= {A} + {B:.3f} log2 k  (k=1 value {F[0]:.2f})")
for A in (31.5, 32, 33, 35):
    B = max((Pp - A) / np.maximum(lk, 1e-9))
    print(f"FEI+: C'(k) <= {A} + {B:.3f} log2 k  (k=1 value {Pp[0]:.2f})")
for k in (1, 2, 3, 4, 10, 100, 1000, 10**6):
    i = ks.index(k)
    print(k, round(F[i], 2), round(Pp[i], 2))
