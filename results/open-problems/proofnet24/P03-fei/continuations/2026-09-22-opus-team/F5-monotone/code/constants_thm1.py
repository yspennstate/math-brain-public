"""Constants of Theorem 1 (FEI for linear threshold functions), computed with mpmath at 50 digits,
and the scalar facts the proof uses, each checked on its whole range where the check is finite.

  B    = (3/2) (2/sqrt(pi)) sqrt(3) = 3 sqrt(3/pi)       [Lemma 3, choice c = N/(3K)]
  L1   = 2 ln B + 2                                        [Lemma 3]
  C(a) = 3 + (1 + ln(a/(a-1)) + a L1) / ln 2,  a > 1     [Theorem 1]
  a*   = (1 + sqrt(1 + 4/L1))/2 minimises C(a).
"""
from mpmath import mp, mpf, sqrt, pi, log, e, binomial, nstr, exp
import math

mp.dps = 50
B = 3 * sqrt(3 / pi)
L1 = 2 * log(B) + 2
a = (1 + sqrt(1 + 4 / L1)) / 2
C = 3 + (1 + log(a / (a - 1)) + a * L1) / log(2)
print("B   =", nstr(B, 20))
print("L1  =", nstr(L1, 20))
print("a*  =", nstr(a, 20))
print("C   =", nstr(C, 20), " (Theorem 1 states C <= 14.22)")
assert C < mpf("14.22")

# Fact A: (1 - 1/(3K))^(-K) <= 3/2 for K >= 1.  -K ln(1-1/(3K)) = sum_{m>=1} 3^-m K^(1-m)/m is
# nonincreasing in K, so its maximum is at K = 1 where it equals ln(3/2).  Spot check:
for K in [1, 1.5, 2, 5, 10, 100, 10**6]:
    K = mpf(K)
    v = (1 - 1 / (3 * K)) ** (-K)
    assert v <= mpf(3) / 2 + mpf(10) ** -40, (K, v)
print("Fact A spot checks passed; limit e^(1/3) =", nstr(exp(mpf(1) / 3), 12))

# Fact B: min(1, sqrt(2/(pi m))) <= (2/sqrt(pi)) (m+1)^(-1/2) for all integers m >= 0
# (m = 0: 1 <= 2/sqrt(pi); m >= 1: equivalent to m >= 1).
assert 1 <= 2 / sqrt(pi)
print("Fact B: 2/sqrt(pi) =", nstr(2 / sqrt(pi), 12), ">= 1")

# Fact C: C(m, floor(m/2)) 2^-m <= sqrt(2/(pi m)), m >= 1.  Analytic: C(2r,r)4^-r <= (pi r)^(-1/2)
# (Wallis) and the odd case reduces to 4r^2 + 2r - 1 >= 0.  Exact check for m <= 4000:
worst = mpf(0)
for m in range(1, 4001):
    v = mpf(math.comb(m, m // 2)) / mpf(2) ** m / sqrt(2 / (pi * m))
    worst = max(worst, v)
assert worst <= 1
print("Fact C: max_{m<=4000} ratio =", nstr(worst, 15))

# Fact D (tail integral): int_0^inf min(1, B e^{-u/2}) du = 2 ln B + 2 for B >= 1.
assert B >= 1
print("Fact D: 2 ln B + 2 =", nstr(L1, 15))

# Corollary 2: k co-monotone threshold functions (or t sign changes): L1 -> L1 + 2 ln k.
for k in [1, 2, 3, 4, 8, 16, 100]:
    Lk = L1 + 2 * log(k)
    ak = (1 + sqrt(1 + 4 / Lk)) / 2
    Ck = 3 + (1 + log(ak / (ak - 1)) + ak * Lk) / log(2)
    print("C_%d = %s" % (k, nstr(Ck, 10)))
