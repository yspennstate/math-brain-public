#!/usr/bin/env python3
"""Rigorous outward-interval certificate for NM13-13 / T04.

A two-node Gaussian quadrature lower envelope is applied to the Hausdorff
moment tail of the hard-field one-step K-SAT interpolation functional.

Exact symmetric survey law:
  alpha = 4389/1000 = 4.389
  R in {19/2500, 2/25, 1/2, 23/25, 2481/2500}
  weights {107/2000, 1823/10000, 1321/2500, 1823/10000, 107/2000}.

Let mu_k=E[Q^k], 0<=Q<=1, and tilt by Q^K:
  m_j = mu_{K+j}/mu_K, j=0,1,2,3.
The two-node Gaussian rule for the tilted probability measure has nodes
x1,x2 and weights w1,w2 matching m_0,...,m_3. For t>=4, Hermite
interpolation of x^t at x1,x2 has nonnegative fourth derivative remainder,
so E_K[Q^t] >= w1*x1^t+w2*x2^t. Equality holds for t<=3.
Therefore for every finite T,
  sum_{t=1}^T mu_{K+t}^2/(K+t)
  >= mu_K^2 sum_{t=1}^T (w1*x1^t+w2*x2^t)^2/(K+t).
All arithmetic below is outward mpmath interval arithmetic.
"""
import mpmath as mp

DPS = 1350
KMAX = 2300
TTAIL = 60000
mp.iv.dps = DPS
Z0 = mp.iv.mpf([0, 0])
O1 = mp.iv.mpf([1, 1])

def q(n, d):
    return mp.iv.mpf([n, n]) / d

alpha = q(4389, 1000)
vals = [q(19, 2500), q(2, 25), O1/2, q(23, 25), q(2481, 2500)]
probs = [q(107, 2000), q(1823, 10000), q(1321, 2500),
         q(1823, 10000), q(107, 2000)]
lam = 3 * alpha / 2

pair = [(probs[a] * probs[b], O1 - vals[a] * vals[b])
        for a in range(5) for b in range(5)]

# E Z^j for Z=product(1-R_1 R_2) over a Poisson(lam) number of factors.
EZ = [O1]
pows = [O1 for _ in pair]
for j in range(1, KMAX + 4):
    moment = Z0
    for idx, (wt, base) in enumerate(pair):
        pows[idx] = pows[idx] * base
        moment = moment + wt * pows[idx]
    EZ.append(mp.iv.exp(lam * (moment - O1)))

# Binomial inversion: mu_k=E(1-Z)^k.  Forward differences avoid explicit
# binomial coefficients and are algebraically identical.
arr = EZ
mus = [O1]
series = Z0
all_mu_positive = True
for k in range(1, KMAX + 4):
    arr = [arr[j+1] - arr[j] for j in range(len(arr)-1)]
    mu = arr[0] if k % 2 == 0 else -arr[0]
    mus.append(mu)
    all_mu_positive = all_mu_positive and bool(mu.a > 0)
    if k <= KMAX:
        series = series + mu * mu / k

# Clause contribution L=E log(1-R1 R2 R3).
L = Z0
for a in range(5):
    for b in range(5):
        for c in range(5):
            L = L + probs[a]*probs[b]*probs[c] * mp.iv.log(
                O1 - vals[a]*vals[b]*vals[c])
A_K = -series - 2*alpha*L

# Two-node Gaussian quadrature for the K-tilted Hausdorff measure.
muK = mus[KMAX]
m1 = mus[KMAX+1] / muK
m2 = mus[KMAX+2] / muK
m3 = mus[KMAX+3] / muK
var = m2 - m1*m1
s = (m3 - m1*m2) / var
p = s*m1 - m2
disc = s*s - 4*p
sd = mp.iv.sqrt(disc)
x1 = (s - sd) / 2
x2 = (s + sd) / 2
w1 = (x2 - m1) / (x2 - x1)
w2 = O1 - w1

checks = {
    'all_mu_positive': all_mu_positive,
    'variance_positive': bool(var.a > 0),
    'discriminant_positive': bool(disc.a > 0),
    'x1_positive': bool(x1.a > 0),
    'x2_less_than_one': bool(x2.b < 1),
    'nodes_strictly_ordered': bool(x1.b < x2.a),
    'w1_positive': bool(w1.a > 0),
    'w2_positive': bool(w2.a > 0),
}

# Finite rigorous lower bound on the omitted positive moment sum.  The
# quadrature value is exact for t<=3 and is a lower bound for every t>=4.
pow1 = O1
pow2 = O1
gauss_tail = Z0
for t in range(1, TTAIL + 1):
    pow1 = pow1 * x1
    pow2 = pow2 * x2
    qt = w1*pow1 + w2*pow2
    gauss_tail = gauss_tail + qt*qt/(KMAX+t)
Tail_LB = muK*muK*gauss_tail
A_upper = A_K - Tail_LB

mp.iv.dps = 80
print('NM13-13 T04 TWO-NODE GAUSSIAN-TAIL CERTIFICATE')
print('alpha = 4389/1000 = 4.389')
print('survey support = {19/2500, 2/25, 1/2, 23/25, 2481/2500}')
print('survey weights = {107/2000, 1823/10000, 1321/2500, 1823/10000, 107/2000}')
print('KMAX =', KMAX)
print('TTAIL =', TTAIL)
print('interval computation dps =', DPS)
print('checks =', checks)
print('A_K =', A_K)
print('mu_K =', muK)
print('m1 =', m1)
print('m2 =', m2)
print('m3 =', m3)
print('variance =', var)
print('quadrature s =', s)
print('quadrature p =', p)
print('discriminant =', disc)
print('x1 =', x1)
print('x2 =', x2)
print('w1 =', w1)
print('w2 =', w2)
print('finite Gaussian tail lower bound =', Tail_LB)
print('A upper bound =', A_upper)
print('CERTIFIED_STRUCTURAL_CHECKS =', all(checks.values()))
print('CERTIFIED_A_UPPER_NEGATIVE =', bool(A_upper.b < 0))
print('CERTIFIED_A_NEGATIVE =', bool(A_upper.b < 0),
      'because A <= A_K - finite_Gaussian_tail_LB')
