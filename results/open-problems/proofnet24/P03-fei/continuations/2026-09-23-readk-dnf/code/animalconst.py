"""Explicit constants for the rooted-animal proof (read-k DNF formulas).
FEI : C(k)  = 11.384 + beta + log2 k + log2(beta k+1) + log2(1+(beta-1)k) + K2 * M_beta(k)
FEI+: C'(k) = 13.771 + beta + 7.055 + log2 k + log2(beta k+1) + log2(1+(beta-1)k) + K2 * max(log2 k + 2, 2 M_beta(k))
K2 = 1 + log2e/(beta k+1) + log2e/(1+(beta-1)k);  M_beta(k) = sup_w min(w, k T_beta(w)),
T_beta(w) = sup_{m>=w} m tau(m), tau(m) = Pr[Bin(m-1,1/2) < m/beta - 1]."""
import numpy as np
from scipy.stats import binom
L2E = 1 / np.log(2)

def Mtab(beta, ks, mmax=20000):
    m = np.arange(1, mmax + 1)
    kk = np.ceil(m / beta - 1) - 1
    t = np.where(kk >= 0, binom.cdf(kk, m - 1, 0.5), 0.0)
    mt = m * t
    T = np.maximum.accumulate(mt[::-1])[::-1]
    return {k: float(np.max(np.minimum(m, k * T))) for k in ks}, float(mt[-200:].max())

ks = [1, 2, 3, 4, 5, 6, 8, 10, 16, 32, 64, 100, 256, 1000, 10**4, 10**5, 10**6]
betas = [2.5, 3, 4, 5, 6, 7, 8, 10, 12, 16, 20, 24, 32]
M = {}
for b in betas:
    M[b], tail = Mtab(b, ks)
    assert tail < 1e-6, (b, tail)
def CF(k, b):
    K2 = 1 + L2E / (b * k + 1) + L2E / (1 + (b - 1) * k)
    return 11.384 + b + np.log2(k) + np.log2(b * k + 1) + np.log2(1 + (b - 1) * k) + K2 * M[b][k]
def CP(k, b):
    K2 = 1 + L2E / (b * k + 1) + L2E / (1 + (b - 1) * k)
    return 13.771 + 7.055 + b + np.log2(k) + np.log2(b * k + 1) + np.log2(1 + (b - 1) * k) + K2 * max(np.log2(k) + 2, 2 * M[b][k])
print(" k      FEI new (beta)   old      |  FEI+ new (beta)   old    | new FEI / log2(2k)")
for k in ks:
    f = min((CF(k, b), b) for b in betas); p = min((CP(k, b), b) for b in betas)
    print(f"{k:7d}  {f[0]:8.2f} ({f[1]:>2})  {2.886 + 9.898 * k:10.1f} | {p[0]:8.2f} ({p[1]:>2}) {10.9 + 14 * k:10.1f} | {f[0] / np.log2(2 * k):6.2f}")
# a clean uniform statement: find A,B with C(k) <= A + B log2 k for all k (fixed beta per range)
for b in (8, 12, 16):
    vals = [(k, CF(k, b)) for k in ks]
    print(f"beta={b}: " + ", ".join(f"{k}:{v:.1f}" for k, v in vals))
