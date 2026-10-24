#!/usr/bin/env python3
"""Finite-state sanity search for the conjectural Green-domination inequality.

This is NOT a proof.  It exactly exponentiates the interchange generator on
small finite graphs and checks, for every proper nonempty vertex subset S and
u in S,

    P(Cycle_pi_t(u) subset S) <= [K_S (I-K_S)^(-1)]_{u,u},

where K is the one-particle heat kernel.

The script also reports the largest ratio lhs/rhs observed.  It is intended
only as a counterexample search for the conjectural GDC target recorded in the
HARD10-03 report of 2026-09-15T22-18-50Z.
"""

from __future__ import annotations

import itertools
import json
import math

import numpy as np
from scipy.linalg import expm


def all_permutations(n: int):
    return list(itertools.permutations(range(n)))


def left_compose_transposition(p, edge):
    a, b = edge
    q = list(p)
    for i, x in enumerate(q):
        if x == a:
            q[i] = b
        elif x == b:
            q[i] = a
    return tuple(q)


def interchange_distribution(n, weighted_edges, t):
    ps = all_permutations(n)
    index = {p: i for i, p in enumerate(ps)}
    qgen = np.zeros((len(ps), len(ps)), dtype=float)
    for p in ps:
        i = index[p]
        for a, b, rate in weighted_edges:
            q = left_compose_transposition(p, (a, b))
            qgen[i, index[q]] += rate
            qgen[i, i] -= rate
    semigroup = expm(t * qgen)
    identity = tuple(range(n))
    return ps, semigroup[index[identity]]


def one_particle_kernel(n, weighted_edges, t):
    gen = np.zeros((n, n), dtype=float)
    for a, b, rate in weighted_edges:
        gen[a, b] += rate
        gen[b, a] += rate
        gen[a, a] -= rate
        gen[b, b] -= rate
    return expm(t * gen)


def cycle_vertices(p, u):
    out = []
    x = u
    while x not in out:
        out.append(x)
        x = p[x]
    return frozenset(out)


def check_instance(name, n, weighted_edges, times, tol=1e-10):
    worst_ratio = 0.0
    worst_record = None
    violations = []

    for t in times:
        ps, probs = interchange_distribution(n, weighted_edges, t)
        k = one_particle_kernel(n, weighted_edges, t)

        for size in range(1, n):
            for s_tuple in itertools.combinations(range(n), size):
                s = frozenset(s_tuple)
                order = list(s_tuple)
                ks = k[np.ix_(order, order)]
                resolvent = ks @ np.linalg.inv(np.eye(size) - ks)

                for u in order:
                    lhs = sum(
                        prob
                        for p, prob in zip(ps, probs)
                        if cycle_vertices(p, u).issubset(s)
                    )
                    iu = order.index(u)
                    rhs = float(resolvent[iu, iu])
                    ratio = lhs / rhs if rhs > 0 else math.inf
                    if ratio > worst_ratio:
                        worst_ratio = ratio
                        worst_record = {
                            "time": t,
                            "S": order,
                            "u": u,
                            "lhs": lhs,
                            "rhs": rhs,
                            "ratio": ratio,
                        }
                    if lhs > rhs + tol:
                        violations.append({
                            "time": t,
                            "S": order,
                            "u": u,
                            "lhs": lhs,
                            "rhs": rhs,
                            "gap": lhs - rhs,
                        })

    return {
        "name": name,
        "n": n,
        "weighted_edges": weighted_edges,
        "times": times,
        "num_violations": len(violations),
        "first_violation": violations[0] if violations else None,
        "worst_ratio": worst_ratio,
        "worst_record": worst_record,
    }


def main():
    times = [0.05, 0.2, 0.5, 1.0, 2.0, 5.0]
    graphs = [
        ("path3", 3, [(0, 1, 1.0), (1, 2, 1.0)]),
        ("path4", 4, [(0, 1, 1.0), (1, 2, 1.0), (2, 3, 1.0)]),
        ("cycle4", 4, [(0, 1, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 0, 1.0)]),
        ("star4", 4, [(0, 1, 1.0), (0, 2, 1.0), (0, 3, 1.0)]),
        ("K4", 4, [(a, b, 1.0) for a, b in itertools.combinations(range(4), 2)]),
        # deterministic nonuniform-rate examples
        ("weighted_path4", 4, [(0, 1, 0.17), (1, 2, 1.9), (2, 3, 0.43)]),
        ("weighted_cycle4", 4, [(0, 1, 0.2), (1, 2, 2.3), (2, 3, 0.7), (3, 0, 1.4)]),
    ]

    results = [check_instance(name, n, edges, times) for name, n, edges in graphs]
    payload = {
        "statement_checked": "P(Cycle_pi_t(u) subset S) <= [K_S(I-K_S)^(-1)]_uu",
        "status": "numerical counterexample search only; not a proof",
        "results": results,
        "total_violations": sum(r["num_violations"] for r in results),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
