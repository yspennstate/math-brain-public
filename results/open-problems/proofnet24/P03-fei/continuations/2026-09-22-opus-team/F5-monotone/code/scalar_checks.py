"""Scalar inequalities used in the proof of Theorem A (numerical confirmation; each also has a short
analytic proof in REPORT.md)."""
import math
import numpy as np
from mpmath import mp, mpf, binomial, sqrt, pi, log
mp.dps = 30
# (1) Erdos-Littlewood-Offord constant: C(m, floor(m/2))/2^m <= sqrt(2/(pi m)), m = 1..20000 (exact big ints)
worst = 0.0
for m in range(1, 20001):
    v = mpf(math.comb(m, m // 2)) / mpf(2) ** m
    r = v / sqrt(2 / (pi * m))
    worst = max(worst, float(r))
print("(1) max_m<=20000 C(m,m/2)2^-m / sqrt(2/(pi m)) =", worst)
# (2) (1 - 1/(2K))^(-K) <= 2 for real K >= 1
K = np.concatenate([np.linspace(1, 10, 200001), np.logspace(1, 8, 20001)])
F = (1 - 1 / (2 * K)) ** (-K)
print("(2) max (1-1/(2K))^-K on K>=1:", F.max(), "at K=", K[np.argmax(F)])
# (3) OWZ Prop 2 elementary inequality on eps in (0,1]
e = np.concatenate([np.logspace(-12, -1, 20001), np.linspace(0.1, 1, 200001)])
t = 1 - np.sqrt(1 - e)
lhs = t * np.log2(2 / t)
rhs = 0.5 * e * np.log2(1 / e) + e
print("(3) min lhs-rhs on (0,1]:", (lhs - rhs).min(), " at eps=", e[np.argmin(lhs - rhs)])
# (4) (1-eps) log2(1/(1-eps)) <= 2 eps
print("(4) max (1-e)log2(1/(1-e)) - 2e:", ((1 - e) * np.log2(1 / (1 - e + 1e-300)) - 2 * e).max())
# (5) min(1, kappa sqrt(2/(pi m))) <= kappa (2/sqrt(pi)) (m+1)^(-1/2) for m>=0, kappa>=1
ok = all(min(1.0, k * math.sqrt(2 / (math.pi * m))) <= k * 2 / math.sqrt(math.pi) / math.sqrt(m + 1) + 1e-15
         for k in (1, 2) for m in range(1, 100000)) and all(1 <= k * 2 / math.sqrt(math.pi) for k in (1, 2))
print("(5) holds:", ok)
# (6) constants
for kap in (1, 2):
    B = 4 * math.sqrt(2) * kap / math.sqrt(math.pi)
    L = 2 * math.log(B) + 2
    print("(6) kappa=%d B=%.6f  2lnB+2=%.6f  per-class const (1+L)/ln2=%.6f  C0=3+that=%.6f" % (kap, B, L, (1 + L) / math.log(2), 3 + (1 + L) / math.log(2)))
