#!/usr/bin/env python3
"""Consistency checks for PROB20-14 report 2026-09-16T07-43-30Z.

Finite-support checks only. They validate algebra/indexing for:
1) one-sided entropy-retention Lemma 3.1;
2) the pre-optimization categorical tilted-entropy inequality behind Theorem 6.1;
3) the exact k=1 prefix/forest entropy decomposition (8.2).

They are not evidence for the infinite-variance theorem.
"""

import math
from collections import defaultdict

PI = {0: 0.4, 1: 0.4, 2: 0.1, 4: 0.1}
assert abs(sum(PI.values()) - 1.0) < 1e-15
assert abs(sum(k * p for k, p in PI.items()) - 1.0) < 1e-15


def conv_dist(m, max_sum):
    dist = {0: 1.0}
    for _ in range(m):
        nxt = defaultdict(float)
        for s, ps in dist.items():
            for d, pd in PI.items():
                if s + d <= max_sum:
                    nxt[s + d] += ps * pd
        dist = dict(nxt)
    return dist


def conditioned_coordinate(n):
    dn = conv_dist(n, n - 1)
    a_n = dn.get(n - 1, 0.0)
    dm = conv_dist(n - 1, n - 1)
    mu = {}
    for d, pd in PI.items():
        if d <= n - 1:
            mu[d] = pd * dm.get(n - 1 - d, 0.0) / a_n
    return a_n, mu


def kl(q, p):
    out = 0.0
    for x, qx in q.items():
        if qx > 0.0:
            out += qx * math.log(qx / p[x])
    return out


def Lambda(theta):
    return math.log(sum(p * math.exp(-theta * (d - 1)) for d, p in PI.items()))


def forest_prob(b, m):
    if b == 0:
        return 1.0 if m == 0 else 0.0
    if m < b:
        return 0.0
    dm = conv_dist(m, m - b)
    return (b / m) * dm.get(m - b, 0.0)


def check_n(n):
    a_n, mu = conditioned_coordinate(n)
    assert abs(sum(mu.values()) - 1.0) < 5e-12
    assert abs(sum(d * p for d, p in mu.items()) - (1.0 - 1.0 / n)) < 5e-12

    drel = kl(mu, PI)
    x_n = n * drel

    # Lemma 3.1 with f(x)=(x/R)^2 1{x<=R}, R=4.
    R = 4.0
    EPf = sum(p * ((d / R) ** 2 if d <= R else 0.0) for d, p in PI.items())
    EQf = sum(p * ((d / R) ** 2 if d <= R else 0.0) for d, p in mu.items())
    c0 = 1.0 - math.exp(-1.0)
    assert EQf + 1e-12 >= c0 * EPf - drel

    # Categorical inequality before optimizing theta, with A1={2}, A2={4}.
    alphas = [mu.get(2, 0.0), mu.get(4, 0.0)]
    ps = [PI[2], PI[4]]
    ds = [2, 4]
    alpha = sum(alphas)
    M = sum(a * (d - 1) for a, d in zip(alphas, ds))
    ent = sum(a * math.log(a / p) for a, p in zip(alphas, ps) if a > 0.0)
    max_rhs = -1e300
    best_theta = 0.0
    for i in range(4001):
        theta = 4.0 * i / 4000.0
        rhs = (
            n * ent
            - n * alpha
            + theta * (1.0 + n * M)
            - n * (1.0 - alpha) * Lambda(theta)
        )
        if rhs > max_rhs:
            max_rhs = rhs
            best_theta = theta
    assert x_n + 2e-10 >= max_rhs

    # Exact k=1 prefix/forest entropy decomposition.
    nu_n = a_n / n
    qroot = {}
    fprob = {}
    for b, pb in PI.items():
        if b == 0:
            continue
        fp = forest_prob(b, n - 1)
        if fp > 0.0:
            qroot[b] = pb * fp / nu_n
            fprob[b] = fp
    z = sum(qroot.values())
    assert abs(z - 1.0) < 2e-10

    Dprefix = sum(qb * math.log(qb / PI[b]) for b, qb in qroot.items())
    forest_cost = sum(qroot[b] * (-math.log(fprob[b])) for b in qroot)
    total_cost = -math.log(nu_n)
    assert abs((Dprefix + forest_cost) - total_cost) < 2e-10

    return {
        "n": n,
        "a_n": a_n,
        "x_n": x_n,
        "retention_lhs": EQf,
        "retention_rhs": c0 * EPf - drel,
        "categorical_max_rhs": max_rhs,
        "categorical_best_theta": best_theta,
        "prefix_D": Dprefix,
        "forest_cost": forest_cost,
        "total_cost": total_cost,
    }


def main():
    rows = [check_n(n) for n in (12, 20, 40)]
    print("PROB20-14 consistency checks: PASS")
    for row in rows:
        print(
            "n={n} a_n={a_n:.12g} x_n={x_n:.12g} "
            "retention={retention_lhs:.12g}>={retention_rhs:.12g} "
            "cat_rhs={categorical_max_rhs:.12g} theta*={categorical_best_theta:.4g} "
            "prefix+forest={sumcost:.12g} total={total_cost:.12g}".format(
                sumcost=row["prefix_D"] + row["forest_cost"], **row
            )
        )


if __name__ == "__main__":
    main()
