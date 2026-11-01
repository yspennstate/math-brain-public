#!/usr/bin/env python3
"""
Outward-interval certificate for NM13-13 / T04.

For a symmetric three-support hard-field survey
    R in {s, 1/2, 1-s} with probabilities {w, 1-2w, w},
at clause density alpha, define for one root orientation
    lambda = 3 alpha / 2,
    Z = product_j (1-R_{j,1}R_{j,2}),  Q = 1-Z.
Then
    E Z^j = exp(lambda*(E(1-R1 R2)^j - 1)),
    mu_k = E Q^k = sum_{j=0}^k (-1)^j C(k,j) E Z^j,
and the m->0 hard-field coefficient of the rigorous 1RSB interpolation trial is
    A = -sum_{k>=1} mu_k^2/k - 2 alpha E log(1-R1 R2 R3).

For every K,
    A <= A_K := -sum_{k=1}^K mu_k^2/k - 2 alpha E log(1-R1 R2 R3),
so A_K < 0 is a one-sided rigorous certificate.

This script evaluates:
  candidate law: alpha=43911/10000, s=51/1000, w=43/200;
  predecessor law: same alpha, s=47/800, w=4179/20000;
with K=1200 and outward mpmath interval arithmetic.
"""
import math
import mpmath as mp

DPS = 620
KMAX = 1200
mp.iv.dps = DPS

ZERO = mp.iv.mpf([0, 0])
ONE = mp.iv.mpf([1, 1])

def point_ratio(num, den):
    return mp.iv.mpf([num, num]) / den

def evaluate(alpha, s, w):
    mid = ONE - 2*w
    vals = [s, ONE/2, ONE-s]
    probs = [w, mid, w]
    lam = 3*alpha/2

    pair = []
    for a, ra in enumerate(vals):
        for b, rb in enumerate(vals):
            pair.append((probs[a]*probs[b], ONE-ra*rb))

    EZ = [ONE]
    pows = [ONE for _ in pair]
    for j in range(1, KMAX+1):
        moment = ZERO
        for idx, (wt, base) in enumerate(pair):
            pows[idx] = pows[idx] * base
            moment += wt * pows[idx]
        EZ.append(mp.iv.exp(lam*(moment-ONE)))

    series = ZERO
    all_mu_positive = True
    mu1 = None
    muK = None
    for k in range(1, KMAX+1):
        mu = ZERO
        for j in range(k+1):
            mu += ((-1)**j) * math.comb(k, j) * EZ[j]
        if k == 1:
            mu1 = mu
        if k == KMAX:
            muK = mu
        all_mu_positive = all_mu_positive and bool(mu.a > 0)
        series += mu*mu/k

    L = ZERO
    for a, ra in enumerate(vals):
        for b, rb in enumerate(vals):
            for c, rc in enumerate(vals):
                L += probs[a]*probs[b]*probs[c]*mp.iv.log(ONE-ra*rb*rc)

    A_K = -series - 2*alpha*L
    return {
        "mid": mid,
        "lambda": lam,
        "L": L,
        "mu1": mu1,
        "muK": muK,
        "series": series,
        "A_K": A_K,
        "all_mu_positive": all_mu_positive,
    }

alpha = point_ratio(43911, 10000)
cand_s = point_ratio(51, 1000)
cand_w = point_ratio(43, 200)
old_s = point_ratio(47, 800)
old_w = point_ratio(4179, 20000)

cand = evaluate(alpha, cand_s, cand_w)
old = evaluate(alpha, old_s, old_w)
delta = old["A_K"] - cand["A_K"]

# Keep the computation at 620 digits, but print concise outward intervals.
mp.iv.dps = 60

print("NM13-13 T04 THREE-SUPPORT K=1200 OUTWARD-INTERVAL CERTIFICATE")
print("interval_dps =", DPS)
print("KMAX =", KMAX)
print("alpha = 43911/10000 = 4.3911")
print("candidate s = 51/1000 = 0.051")
print("candidate w = 43/200 = 0.215")
print("candidate middle weight = 57/100 = 0.57")
print("candidate all mu_k intervals strictly positive =", cand["all_mu_positive"])
print("candidate mu_1 =", cand["mu1"])
print("candidate mu_1200 =", cand["muK"])
print("candidate L =", cand["L"])
print("candidate partial_series =", cand["series"])
print("candidate A_1200 =", cand["A_K"])
print("CERTIFIED_CANDIDATE_A_1200_NEGATIVE =", bool(cand["A_K"].b < 0))
print("CERTIFIED_CANDIDATE_A_NEGATIVE =", bool(cand["A_K"].b < 0), "because A <= A_1200")
print()
print("predecessor comparison at the same alpha and K (diagnostic only)")
print("old s = 47/800 = 0.05875")
print("old w = 4179/20000 = 0.20895")
print("old all mu_k intervals strictly positive =", old["all_mu_positive"])
print("old A_1200 =", old["A_K"])
print("old truncation is positive =", bool(old["A_K"].a > 0))
print("A_1200(old) - A_1200(candidate) =", delta)
print("CERTIFIED_TRUNCATION_GAIN_POSITIVE =", bool(delta.a > 0))
print()
print("SOURCE_CANDIDATE_FIXED_COUNT_UPPER = 4.3911")
print("NOTE: positive old A_1200 is inconclusive about the old infinite A; only negative candidate A_1200 is used for the theorem.")
