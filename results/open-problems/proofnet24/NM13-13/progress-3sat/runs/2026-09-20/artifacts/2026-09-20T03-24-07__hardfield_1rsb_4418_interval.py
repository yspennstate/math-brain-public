#!/usr/bin/env python3
"""Rigorous interval certificate for an explicit hard-field 1RSB trial in iid random 3-SAT.

Trial parameters:
    alpha = 2209/500 = 4.418
    s     = 11/50    = 0.22

Let R be s or 1-s equiprobably.  In the zero-temperature two-survey
Panchenko--Talagrand 1RSB trial, a warning to one spin side has activation
probability P=R1*R2 and the number of potential messages on that side is
Poisson(lambda), lambda=3 alpha/2.  Set

    Z = product_j (1-P_j),   Q = 1-Z.

The coefficient of the 1RSB functional after multiplication by the Parisi
parameter m and taking m down to zero is

    A = E log(1-Q1*Q2) - 2 alpha E log(1-R1*R2*R3)
      = -sum_{k>=1} mu_k^2/k - 2 alpha L,

where mu_k=E Q^k and L=E log(1-R1*R2*R3).  Compound-Poisson moments give

    E Z^j = exp(lambda*( E(1-P)^j - 1)),
    mu_k  = sum_{j=0}^k (-1)^j C(k,j) E Z^j.

Every series term mu_k^2/k is nonnegative.  Therefore

    A <= A_K := -sum_{k=1}^K mu_k^2/k - 2 alpha L.

This script evaluates A_K at K=300 by outward interval arithmetic.  A_K<0
is a rigorous certificate that A<0; no infinite-tail estimate is needed.
"""
import math
import mpmath as mp

DPS = 220
KMAX = 300
mp.iv.dps = DPS

zero = mp.iv.mpf([0, 0])
one = mp.iv.mpf([1, 1])
alpha = mp.iv.mpf([2209, 2209]) / 500
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
mu_first = None
mu_last = None
for k in range(1, KMAX + 1):
    mu = zero
    for j in range(k + 1):
        mu += ((-1)**j) * math.comb(k, j) * EZ[j]
    if k == 1:
        mu_first = mu
    if k == KMAX:
        mu_last = mu
    # For this run all mu intervals are positive; in any event mu_k=E[Q^k]>=0 mathematically.
    series += mu * mu / k

Rvals = [s, one-s]
L = zero
for r1 in Rvals:
    for r2 in Rvals:
        for r3 in Rvals:
            L += mp.iv.log(one-r1*r2*r3) / 8

A_K = -series - 2 * alpha * L

print("T04 HARD-FIELD 1RSB INTERVAL CERTIFICATE")
print("alpha = 2209/500 = 4.418")
print("survey bias s = 11/50 = 0.22")
print("KMAX =", KMAX)
print("interval dps =", DPS)
print("lambda = 3*alpha/2 interval =", lam)
print("L interval =", L)
print("mu_1 interval =", mu_first)
print("mu_300 interval =", mu_last)
print("partial series interval =", series)
print("A_K interval =", A_K)
print("CERTIFIED_A_K_NEGATIVE =", bool(A_K.b < 0))
print("CERTIFIED_A_NEGATIVE =", bool(A_K.b < 0), " because A <= A_K")
print("old explicit upper = 4.4898")
print("new candidate rigorous upper = 4.418")
print("strict upper-endpoint improvement = 0.0718")
print("old explicit bracket width = 0.9698")
print("new candidate bracket width = 0.898")
