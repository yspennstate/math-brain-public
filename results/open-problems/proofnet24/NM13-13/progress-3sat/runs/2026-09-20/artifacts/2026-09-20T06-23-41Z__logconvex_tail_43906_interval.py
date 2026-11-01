#!/usr/bin/env python3
"""Rigorous outward-interval certificate for the NM13-13 / T04 hard-field
one-step interpolation trial at alpha=4.3906.

The new ingredient is a rigorous tail accelerator for the Hausdorff moment
sequence mu_k = E[Q^k], 0<=Q<=1.  Cauchy-Schwarz gives
    mu_k^2 <= mu_{k-1} mu_{k+1},
so r_k=mu_k/mu_{k-1} is nondecreasing.  Therefore for t>=1,
    mu_{K+t} >= mu_K r_K^t,
and the omitted interpolation series has the finite rigorous lower bound
    sum_{k>K} mu_k^2/k >= mu_K^2 sum_{t=1}^T r_K^(2t)/(K+t).
Hence
    A <= A_K - Tail_LB.

Exact symmetric survey law:
  alpha = 21953/5000 = 4.3906
  R in {31/625, 1/2, 594/625}
  weights {27/125, 71/125, 27/125}.

All numerical arithmetic below is outward mpmath interval arithmetic.
"""
import mpmath as mp

DPS = 1350
KMAX = 2400
TTAIL = 10000
mp.iv.dps = DPS
Z0 = mp.iv.mpf([0, 0])
O1 = mp.iv.mpf([1, 1])

def q(num, den):
    return mp.iv.mpf([num, num]) / den

alpha = q(21953, 5000)
s = q(31, 625)
w = q(27, 125)
mid = O1 - 2*w
vals = [s, O1/2, O1-s]
probs = [w, mid, w]
lam = 3*alpha/2

pair = [(probs[a]*probs[b], O1-vals[a]*vals[b])
        for a in range(3) for b in range(3)]
EZ = [O1]
pows = [O1 for _ in pair]
for j in range(1, KMAX+1):
    moment = Z0
    for idx, (wt, base) in enumerate(pair):
        pows[idx] = pows[idx] * base
        moment = moment + wt*pows[idx]
    EZ.append(mp.iv.exp(lam*(moment-O1)))

# mu_k = sum_j (-1)^j C(k,j) EZ[j] = (-1)^k Delta^k EZ[0].
# The forward-difference form is algebraically identical and avoids huge
# integer binomial multipliers; interval arithmetic still encloses the exact
# transform.
arr = EZ
series = Z0
mu_prev = None
mu_K = None
all_mu_positive = True
for k in range(1, KMAX+1):
    arr = [arr[j+1]-arr[j] for j in range(len(arr)-1)]
    mu = arr[0] if k % 2 == 0 else -arr[0]
    all_mu_positive = all_mu_positive and bool(mu.a > 0)
    series = series + mu*mu/k
    if k == KMAX-1:
        mu_prev = mu
    if k == KMAX:
        mu_K = mu

L = Z0
for a in range(3):
    for b in range(3):
        for c in range(3):
            L = L + probs[a]*probs[b]*probs[c]*mp.iv.log(
                O1-vals[a]*vals[b]*vals[c])

A_K = -series - 2*alpha*L

# Rigorous log-convex moment tail lower bound.
r = mu_K/mu_prev
r2 = r*r
rp = r2
geo = Z0
for t in range(1, TTAIL+1):
    geo = geo + rp/(KMAX+t)
    rp = rp*r2
Tail_LB = mu_K*mu_K*geo
A_upper = A_K - Tail_LB

# Keep the computation at full DPS, then display compact outward intervals.
mp.iv.dps = 70
print('NM13-13 T04 LOG-CONVEX MOMENT-TAIL CERTIFICATE')
print('alpha = 21953/5000 = 4.3906')
print('survey support = {31/625, 1/2, 594/625}')
print('survey weights = {27/125, 71/125, 27/125}')
print('KMAX =', KMAX)
print('TTAIL =', TTAIL)
print('interval computation dps =', DPS)
print('all mu_1..mu_K intervals strictly positive =', all_mu_positive)
print('mu_2399 =', mu_prev)
print('mu_2400 =', mu_K)
print('r_2400 = mu_2400/mu_2399 =', r)
print('A_2400 =', A_K)
print('finite log-convex tail lower bound =', Tail_LB)
print('A upper bound = A_2400 - tail_LB =', A_upper)
print('CERTIFIED_A_UPPER_NEGATIVE =', bool(A_upper.b < 0))
print('CERTIFIED_A_NEGATIVE =', bool(A_upper.b < 0),
      'because A <= A_2400 - tail_LB')
