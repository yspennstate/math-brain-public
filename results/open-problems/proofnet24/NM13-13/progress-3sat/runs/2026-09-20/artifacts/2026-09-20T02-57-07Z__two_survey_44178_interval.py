#!/usr/bin/env python3
"""
Rigorous interval certificate for the two-survey 1RSB hard-field coefficient used
in the T04 iid random 3-SAT upper-bound argument.

Poisson interpolation density:
    alpha0 = 22089/5000 = 4.4178
Survey bias:
    s = 11/50 = 0.22

For R taking s and 1-s with probability 1/2, let P=R1*R2.  On one root
orientation, warning arrivals form a Poisson process of mean lambda=3 alpha0/2.
Writing
    Z = product_j (1-P_j),  Q=1-Z,
we have
    E Z^j = exp(lambda*(E(1-P)^j - 1)),
    mu_k = E Q^k = sum_{j=0}^k (-1)^j C(k,j) E Z^j.

For independent Q_+,Q_-,
    E log(1-Q_+ Q_-) = - sum_{k>=1} mu_k^2/k.
Also
    L = E log(1-R1 R2 R3).

Thus the hard-field, m->0 coefficient is
    A = -sum_{k>=1} mu_k^2/k - 2 alpha0 L.
Every omitted series term is nonnegative before the minus sign, so
    A <= A_K := -sum_{k=1}^K mu_k^2/k - 2 alpha0 L.
A_K<0 is therefore sufficient.

All arithmetic below uses outward mpmath interval arithmetic.  No tail bound is
needed.
"""
import math
import mpmath as mp

DPS = 240
KMAX = 300
mp.iv.dps = DPS

zero = mp.iv.mpf([0, 0])
one = mp.iv.mpf([1, 1])
alpha = mp.iv.mpf([22089, 22089]) / 5000
s = mp.iv.mpf([11, 11]) / 50
lam = 3 * alpha / 2

Pvals = [s*s, (one-s)*(one-s), s*(one-s)]
Pprobs = [one/4, one/4, one/2]

EZ = [one]
for j in range(1, KMAX + 1):
    e_term = zero
    for w, P in zip(Pprobs, Pvals):
        e_term += w * (one-P)**j
    EZ.append(mp.iv.exp(lam * (e_term-one)))

series = zero
mu1 = None
muK = None
all_mu_positive = True
for k in range(1, KMAX + 1):
    mu = zero
    for j in range(k + 1):
        mu += ((-1)**j) * math.comb(k, j) * EZ[j]
    if k == 1:
        mu1 = mu
    if k == KMAX:
        muK = mu
    all_mu_positive = all_mu_positive and bool(mu.a > 0)
    series += mu * mu / k

L = zero
for r1 in [s, one-s]:
    for r2 in [s, one-s]:
        for r3 in [s, one-s]:
            L += mp.iv.log(one-r1*r2*r3) / 8

A_K = -series - 2 * alpha * L

print("T04 TWO-SURVEY HARD-FIELD COEFFICIENT CERTIFICATE")
print("alpha0 = 22089/5000 = 4.4178")
print("source target density for Poisson-to-proper transfer = 2209/500 = 4.418")
print("survey bias s = 11/50 = 0.22")
print("KMAX =", KMAX)
print("interval dps =", DPS)
print("lambda = 3*alpha0/2 =", lam)
print("L =", L)
print("mu_1 =", mu1)
print("mu_300 =", muK)
print("all mu_k intervals strictly positive =", all_mu_positive)
print("partial series =", series)
print("A_K =", A_K)
print("CERTIFIED_A_K_NEGATIVE =", bool(A_K.b < 0))
print("CERTIFIED_A_NEGATIVE =", bool(A_K.b < 0), "because A <= A_K")
print("density slack 4.418 - 4.4178 =", mp.iv.mpf([2209,2209])/500 - alpha)
