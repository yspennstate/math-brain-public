#!/usr/bin/env python3
"""Finite-state sanity checks for HARD10-03 NEW-L69/70.

This is not a proof.  It enumerates interchange permutations on several small
finite graphs and checks

  P(P(A)=A) <= prod_{y in A} sum_{x in A} K(x,y) <= exp(-mu_A),
  P(C_u=A) <= exp(-mu_A),

for every nonempty A.  It also checks a genuinely time-inhomogeneous evolution
with a forced transposition between two random interchange segments, modelling
the form of conditional dynamics used in the no-peeking theorem.
"""

import itertools
import json
import math
import numpy as np
from scipy.linalg import expm


def permutations(n):
    return list(itertools.permutations(range(n)))


def swap_positions(p, edge):
    u, v = edge
    q = list(p)
    for i, a in enumerate(q):
        if a == u:
            q[i] = v
        elif a == v:
            q[i] = u
    return tuple(q)


def generator(n, edge_rates):
    ps = permutations(n)
    idx = {p: i for i, p in enumerate(ps)}
    qmat = np.zeros((len(ps), len(ps)))
    for i, p in enumerate(ps):
        total = 0.0
        for edge, rate in edge_rates:
            q = swap_positions(p, edge)
            qmat[i, idx[q]] += rate
            total += rate
        qmat[i, i] -= total
    return ps, idx, qmat


def homogeneous_distribution(n, edges, t):
    ps, idx, qmat = generator(n, [(e, 1.0) for e in edges])
    d = np.zeros(len(ps))
    d[idx[tuple(range(n))]] = 1.0
    return ps, idx, d @ expm(t * qmat)


def one_particle_kernel(ps, d, n):
    k = np.zeros((n, n))
    for prob, p in zip(d, ps):
        for label, position in enumerate(p):
            k[label, position] += prob
    return k


def invariant_probability(ps, d, A):
    A = set(A)
    return sum(prob for prob, p in zip(d, ps) if {p[a] for a in A} == A)


def cycle_set(p, u):
    seen = set()
    x = u
    while x not in seen:
        seen.add(x)
        x = p[x]
    return seen


def exact_cycle_probability(ps, d, A, u):
    A = set(A)
    return sum(prob for prob, p in zip(d, ps) if cycle_set(p, u) == A)


def check_distribution(ps, d, n):
    k = one_particle_kernel(ps, d, n)
    worst = {
        "survival_minus_exp": -1e100,
        "cycle_minus_exp": -1e100,
        "survival_minus_product": -1e100,
    }
    cases = 0
    for mask in range(1, 1 << n):
        A = [i for i in range(n) if (mask >> i) & 1]
        size = len(A)
        internal_heat = sum(k[x, y] for x in A for y in A)
        mu = size - internal_heat
        survival = invariant_probability(ps, d, A)
        product = 1.0
        for y in A:
            product *= sum(k[x, y] for x in A)
        exp_bound = math.exp(-mu)
        cycle_prob = exact_cycle_probability(ps, d, A, A[0])
        worst["survival_minus_exp"] = max(
            worst["survival_minus_exp"], survival - exp_bound
        )
        worst["cycle_minus_exp"] = max(
            worst["cycle_minus_exp"], cycle_prob - exp_bound
        )
        worst["survival_minus_product"] = max(
            worst["survival_minus_product"], survival - product
        )
        cases += 1
    return k, worst, cases


def main():
    graphs = {
        "path4": (4, [(0, 1), (1, 2), (2, 3)]),
        "cycle4": (4, [(0, 1), (1, 2), (2, 3), (3, 0)]),
        "star4": (4, [(0, 1), (0, 2), (0, 3)]),
        "cycle5": (5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]),
    }
    result = {"homogeneous": {}, "conditional_time_inhomogeneous": {}}
    max_violation = 0.0

    for name, (n, edges) in graphs.items():
        rows = []
        for t in (0.2, 1.0, 2.0):
            ps, _, d = homogeneous_distribution(n, edges, t)
            _, worst, cases = check_distribution(ps, d, n)
            rows.append({"t": t, "cases": cases, **worst})
            max_violation = max(max_violation, *(max(0.0, v) for v in worst.values()))
        result["homogeneous"][name] = rows

    # Genuinely time-inhomogeneous four-cycle.  The one-particle kernel is
    # non-self-adjoint because the two random segments have different rates
    # and a forced transposition is inserted between them.
    n = 4
    ps, idx, q1 = generator(
        n,
        [((0, 1), 1.0), ((1, 2), 0.4), ((2, 3), 1.3), ((3, 0), 0.2)],
    )
    _, _, q2 = generator(
        n,
        [((0, 1), 0.3), ((1, 2), 1.2), ((2, 3), 0.1), ((3, 0), 0.9)],
    )
    d = np.zeros(len(ps))
    d[idx[tuple(range(n))]] = 1.0
    d = d @ expm(0.7 * q1)
    after_forced = np.zeros_like(d)
    for i, p in enumerate(ps):
        after_forced[idx[swap_positions(p, (0, 1))]] += d[i]
    d = after_forced @ expm(0.9 * q2)
    k, worst, cases = check_distribution(ps, d, n)
    result["conditional_time_inhomogeneous"] = {
        "cases": cases,
        **worst,
        "one_particle_kernel_max_asymmetry": float(np.max(np.abs(k - k.T))),
    }
    max_violation = max(max_violation, *(max(0.0, v) for v in worst.values()))

    result["summary"] = {
        "status": "PASS" if max_violation < 5e-12 else "FAIL",
        "max_positive_numerical_violation": max_violation,
        "note": "Numerical finite-state sanity check only; analytic proof uses strong-Rayleigh negative association.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
