"""Finite-model corroboration for the multiband entropy inequality.

The theorem checked is
    D(mu || pi) >= sum_j Phi(a_j,Q_j)/L_j,
where
    a_j = sum_{k in I_j} k mu_k,
    Q_j = sum_{k in I_j} k pi_k,
and Phi(a,Q)=a log(a/Q)-a+Q for a>Q, else 0.

This computation is not part of the proof. It checks bookkeeping on 5,000
pseudorandom finite distributions using a fixed seed.
"""

import math
import random


def phi(a, q):
    if a <= q + 1e-15:
        return 0.0
    if q <= 0.0:
        return math.inf if a > 0.0 else 0.0
    return a * math.log(a / q) - a + q


def kl(mu, pi):
    ans = 0.0
    for m, p in zip(mu, pi):
        if m == 0.0:
            continue
        if p == 0.0:
            return math.inf
        ans += m * math.log(m / p)
    return ans


rng = random.Random(20260915)
bands = [(1, 5), (6, 11), (12, 20), (21, 30), (31, 40)]
worst = math.inf
worst_record = None

for trial in range(5000):
    raw_pi = [rng.random() + 0.01 for _ in range(41)]
    raw_mu = [rng.random() + 0.01 for _ in range(41)]
    s_pi = sum(raw_pi)
    s_mu = sum(raw_mu)
    pi = [x / s_pi for x in raw_pi]
    mu = [x / s_mu for x in raw_mu]

    rhs = 0.0
    for lo, hi in bands:
        a = sum(k * mu[k] for k in range(lo, hi + 1))
        q = sum(k * pi[k] for k in range(lo, hi + 1))
        rhs += phi(a, q) / hi

    lhs = kl(mu, pi)
    margin = lhs - rhs
    if margin < worst:
        worst = margin
        worst_record = (trial, lhs, rhs, margin)
    if margin < -1e-10:
        raise AssertionError((trial, lhs, rhs, margin))

print("MULTIBAND ENTROPY CHECK PASSED")
print("trials = 5000")
print("seed = 20260915")
print("worst trial, KL, RHS, margin =", worst_record)
