"""HARD10-04 Palm entropy algebra checker.

This script is only a finite-dimensional consistency certificate for the
identities in the 2026-09-15T16:50:00Z report.  It is not a simulation of DLA
and is not evidence for the unresolved growth exponent.

For random finite time blocks it generates probability vectors p_k and
admissible capacity increments d_k(x)=kappa_k(x) p_k(x)^2.  It checks:

1. the exact particle-Palm / capacity-Palm KL entropy budget;
2. the KL chain rule into temporal and spatial intermittency;
3. the exact reverse Renyi identity for a noninteger q>1.
"""

import math
import random


def kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def renyi(order, p, q):
    return math.log(
        sum((pi ** order) * (qi ** (1.0 - order)) for pi, qi in zip(p, q))
    ) / (order - 1.0)


def check_trial(times=7, max_sites=8, order=2.3):
    ps = []
    ds = []
    a = []
    entropy = []
    mu = []
    spatial_kl = []

    for _ in range(times):
        m = random.randint(2, max_sites)
        raw = [random.expovariate(1.0) for _ in range(m)]
        total = sum(raw)
        p = [x / total for x in raw]

        # Uniformly bounded response coefficients mimic d ~ p^2.
        kappa = [random.uniform(0.7, 3.1) for _ in range(m)]
        d = [kappa[i] * p[i] ** 2 for i in range(m)]
        ak = sum(p[i] * d[i] for i in range(m))
        r = [p[i] * d[i] / ak for i in range(m)]

        ps.append(p)
        ds.append(d)
        a.append(ak)
        entropy.append(-sum(x * math.log(x) for x in p))
        mu.append(sum(p[i] * math.log(kappa[i]) for i in range(m)))
        spatial_kl.append(kl(p, r))

    block_mass = sum(a)
    n = times

    # Joint particle-Palm P and capacity-Palm Q laws.
    P = []
    Q = []
    for k in range(times):
        for i in range(len(ps[k])):
            P.append(ps[k][i] / n)
            Q.append(ps[k][i] * ds[k][i] / block_mass)

    forward = kl(P, Q)

    # Exact entropy budget:
    # D(P||Q) = log A - log N - mean(mu) + 2 mean(H).
    budget = (
        math.log(block_mass)
        - math.log(n)
        - sum(mu) / n
        + 2.0 * sum(entropy) / n
    )
    assert abs(forward - budget) < 1e-10

    # Exact chain rule:
    # D(P||Q) = D(U||w) + mean_k D(p_k||r_k).
    uniform = [1.0 / n] * n
    w = [ak / block_mass for ak in a]
    chain = kl(uniform, w) + sum(spatial_kl) / n
    assert abs(forward - chain) < 1e-10

    # Exact reverse Renyi identity:
    # (q-1)D_q(Q||P) = (q-1)log N - q log A + log sum_k E_p[d^q].
    mq = sum(
        sum(ps[k][i] * ds[k][i] ** order for i in range(len(ps[k])))
        for k in range(times)
    )
    reverse_renyi = renyi(order, Q, P)
    reverse_formula = (
        (order - 1.0) * math.log(n)
        - order * math.log(block_mass)
        + math.log(mq)
    ) / (order - 1.0)
    assert abs(reverse_renyi - reverse_formula) < 1e-10


if __name__ == "__main__":
    random.seed(20260915)
    for _ in range(10_000):
        check_trial()
    print("All 10,000 Palm-entropy algebra checks passed.")
