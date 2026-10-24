#!/usr/bin/env python3
"""Finite-state sanity check for HARD10-03 NEW-L56.

This checks on the 5-cycle graph C5 that the exact interchange generator satisfies

    d/dt E[#cycles]/|V| = (|E|/|V|) * (2 P(edge endpoints same cycle)-1).

For C5, |E|/|V|=1.  The theorem in the report uses the same identity on T_n^3,
where |E|/|V|=3.  This script is a numerical certificate only, not the proof.
"""

import itertools
import json
import numpy as np
from scipy.linalg import expm


def cycle_count(p):
    n = len(p)
    seen = [False] * n
    out = 0
    for i in range(n):
        if seen[i]:
            continue
        out += 1
        x = i
        while not seen[x]:
            seen[x] = True
            x = p[x]
    return out


def same_cycle(p, a, b):
    x = a
    for _ in range(len(p)):
        if x == b:
            return True
        x = p[x]
        if x == a:
            return False
    return False


def left_transpose(p, a, b):
    # A clock ring on physical edge {a,b} left-composes the label-to-position
    # permutation with the transposition of positions a and b.
    return tuple(b if v == a else a if v == b else v for v in p)


def main():
    n = 5
    edges = [(i, (i + 1) % n) for i in range(n)]
    states = list(itertools.permutations(range(n)))
    index = {p: i for i, p in enumerate(states)}

    Q = np.zeros((len(states), len(states)), dtype=float)
    for i, p in enumerate(states):
        for a, b in edges:
            q = left_transpose(p, a, b)
            Q[i, index[q]] += 1.0
        Q[i, i] -= len(edges)

    identity_index = index[tuple(range(n))]
    cycle_counts = np.array([cycle_count(p) for p in states], dtype=float)
    same_edge = np.array([same_cycle(p, *edges[0]) for p in states], dtype=float)

    rows = []
    max_abs_error = 0.0
    for t in (0.1, 0.7, 2.0):
        dist = expm(t * Q)[identity_index]
        rho = float(dist @ cycle_counts / n)
        rho_prime = float((dist @ Q) @ cycle_counts / n)
        a = float(dist @ same_edge)
        rhs = (len(edges) / n) * (2.0 * a - 1.0)
        err = abs(rho_prime - rhs)
        max_abs_error = max(max_abs_error, err)
        rows.append(
            {
                "t": t,
                "cycle_density": rho,
                "cycle_density_derivative": rho_prime,
                "same_cycle_edge_probability": a,
                "drift_rhs": rhs,
                "abs_error": err,
            }
        )

    result = {
        "graph": "C5",
        "vertices": n,
        "edges": len(edges),
        "edge_density_E_over_V": len(edges) / n,
        "states": len(states),
        "checks": rows,
        "max_abs_error": max_abs_error,
        "pass_tolerance_1e-12": bool(max_abs_error < 1e-12),
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
