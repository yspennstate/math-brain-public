#!/usr/bin/env python3
"""
Outward-interval certificate for a three-support 1RSB hard-field trial for
classical iid random 3-SAT.

Outer survey law:
  R = s, 1/2, 1-s
with probabilities
  w, 1-2w, w.

For one root orientation, warnings arrive as a compound Poisson process with
lambda = 3 alpha / 2 and activation P = R1 R2. Put
  Z = prod_j (1-P_j), Q = 1-Z.
Then
  E Z^j = exp(lambda*(E(1-R1 R2)^j - 1)),
  mu_k = E Q^k = sum_{j=0}^k (-1)^j C(k,j) E Z^j,
and
  E log(1-Q_+Q_-) = -sum_{k>=1} mu_k^2/k.

The hard-field m->0 coefficient of the rigorous 1RSB interpolation trial is
  A = -sum_{k>=1} mu_k^2/k - 2 alpha E log(1-R1 R2 R3).
Hence A <= A_K for every finite K, because omitted series terms are
nonnegative before the leading minus sign. Thus A_K < 0 is a rigorous
one-sided certificate.

All arithmetic below uses outward mpmath interval arithmetic.
"""
import math
import mpmath as mp

DPS = 280
KMAX = 300
mp.iv.dps = DPS

zero = mp.iv.mpf([0, 0])
one = mp.iv.mpf([1, 1])

alpha = mp.iv.mpf([439539, 439539]) / 100000   # 4.39539
s = mp.iv.mpf([47, 47]) / 800                  # 0.05875
w = mp.iv.mpf([4179, 4179]) / 20000            # 0.20895
mid = one - 2*w                                 # 0.58210

vals = [s, one/2, one-s]
probs = [w, mid, w]
lam = 3*alpha/2

EZ = [one]
for j in range(1, KMAX + 1):
    moment = zero
    for a, ra in enumerate(vals):
        for b, rb in enumerate(vals):
            moment += probs[a]*probs[b]*(one-ra*rb)**j
    EZ.append(mp.iv.exp(lam*(moment-one)))

series = zero
all_mu_positive = True
mu1 = None
muK = None
for k in range(1, KMAX + 1):
    mu = zero
    for j in range(k + 1):
        mu += ((-1)**j) * math.comb(k, j) * EZ[j]
    if k == 1:
        mu1 = mu
    if k == KMAX:
        muK = mu
    all_mu_positive = all_mu_positive and bool(mu.a > 0)
    series += mu*mu/k

L = zero
for a, ra in enumerate(vals):
    for b, rb in enumerate(vals):
        for c, rc in enumerate(vals):
            L += probs[a]*probs[b]*probs[c]*mp.iv.log(one-ra*rb*rc)

A_K = -series - 2*alpha*L

print("T04 THREE-SUPPORT 1RSB HARD-FIELD CERTIFICATE")
print("alpha = 439539/100000 = 4.39539")
print("s = 47/800 = 0.05875")
print("w = 4179/20000 = 0.20895")
print("middle weight = 5821/10000 = 0.58210")
print("KMAX =", KMAX)
print("interval dps =", DPS)
print("lambda =", lam)
print("L =", L)
print("mu_1 =", mu1)
print("mu_300 =", muK)
print("all mu_k intervals strictly positive =", all_mu_positive)
print("partial series =", series)
print("A_K =", A_K)
print("CERTIFIED_A_K_NEGATIVE =", bool(A_K.b < 0))
print("CERTIFIED_A_NEGATIVE =", bool(A_K.b < 0), "because A <= A_K")
print("fixed-count target density = 4.39539")
