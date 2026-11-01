#!/usr/bin/env python3
"""
Outward-interval certificate for the T04 classical iid random 3-SAT
hard-field one-step interpolation trial at alpha = 4.392.

Exact symmetric survey law:
    R in {179/3125, 1/2, 2946/3125}
with probabilities
    {20997/100000, 29003/50000, 20997/100000}.

For one literal orientation, warnings arrive as a compound Poisson process
with mean lambda = 3*alpha/2.  If P=R1*R2,
    Z = product_j (1-P_j), Q = 1-Z,
then
    E Z^j = exp(lambda*(E(1-R1*R2)^j - 1)),
    mu_k = E Q^k = sum_{j=0}^k (-1)^j C(k,j) E Z^j.
The m->0 hard-field coefficient is
    A = -sum_{k>=1} mu_k^2/k
        - 2*alpha*E log(1-R1*R2*R3).
Thus A <= A_K for every finite K.  A_K < 0 therefore certifies A < 0.

All arithmetic uses outward mpmath interval arithmetic.
"""
import math
import mpmath as mp

DPS = 850
KMAX = 1000
mp.iv.dps = DPS

zero = mp.iv.mpf([0, 0])
one = mp.iv.mpf([1, 1])

alpha = mp.iv.mpf([4392, 4392]) / 1000
s = mp.iv.mpf([179, 179]) / 3125
w = mp.iv.mpf([20997, 20997]) / 100000
mid = one - 2*w

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

print("T04 THREE-SUPPORT K=1000 1RSB HARD-FIELD CERTIFICATE")
print("alpha = 4392/1000 = 4.392")
print("s = 179/3125 = 0.05728")
print("w = 20997/100000 = 0.20997")
print("middle weight = 29003/50000 = 0.58006")
print("KMAX =", KMAX)
print("interval dps =", DPS)
print("all mu_k intervals strictly positive =", all_mu_positive)
print("mu_1 =", mu1)
print("mu_1000 =", muK)
print("L =", L)
print("partial series =", series)
print("A_K =", A_K)
print("CERTIFIED_A_K_NEGATIVE =", bool(A_K.b < 0))
print("CERTIFIED_A_NEGATIVE =", bool(A_K.b < 0), "because A <= A_K")
print("fixed-count target density = 4.392")
