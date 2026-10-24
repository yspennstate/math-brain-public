#!/usr/bin/env python3
"""Finite-state sanity checks for HARD10-03 NEW-L44/NEW-L46.

This is not a proof.  It exactly exponentiates small interchange generators and
checks, for every A containing root 0,

    P(C_0=A) <= P(P(A)=A)
              <= prod_{x in A} sum_{a in A} K(a,x).

The second inequality is the symmetric-exclusion negative-association bound
used analytically in the report.  A time-inhomogeneous example with forced
transpositions checks the conditional/no-peeking version in a genuinely
non-self-adjoint one-particle kernel.
"""

import itertools
import json
import numpy as np
from scipy.linalg import expm


def all_perms(n):
    return list(itertools.permutations(range(n)))


def ring(p, edge):
    """p maps initial label -> current physical position."""
    u, v = edge
    q = list(p)
    for i, x in enumerate(q):
        if x == u:
            q[i] = v
        elif x == v:
            q[i] = u
    return tuple(q)


def generator(perms, index, edges, rates=None):
    if rates is None:
        rates = [1.0] * len(edges)
    m = len(perms)
    Q = np.zeros((m, m))
    for i, p in enumerate(perms):
        for e, r in zip(edges, rates):
            j = index[ring(p, e)]
            Q[i, j] += r
            Q[i, i] -= r
    return Q


def deterministic_ring_matrix(perms, index, edge):
    T = np.zeros((len(perms), len(perms)))
    for i, p in enumerate(perms):
        T[i, index[ring(p, edge)]] = 1.0
    return T


def cycle_set(p, root=0):
    out = []
    x = root
    while x not in out:
        out.append(x)
        x = p[x]
    return frozenset(out)


def expected_perm_kernel(perms, law):
    n = len(perms[0])
    K = np.zeros((n, n))
    for p, mass in zip(perms, law):
        for a, x in enumerate(p):
            K[a, x] += mass
    return K


def check_law(perms, law, K):
    n = len(perms[0])
    root = 0
    max_cycle_minus_invariant = -1e100
    max_invariant_minus_product = -1e100
    max_cycle_over_product = 0.0
    worst = None

    for mask in range(1 << n):
        if not (mask & 1):
            continue
        A = frozenset(i for i in range(n) if (mask >> i) & 1)

        p_cycle = sum(
            mass for p, mass in zip(perms, law) if cycle_set(p, root) == A
        )
        p_invariant = sum(
            mass
            for p, mass in zip(perms, law)
            if frozenset(p[a] for a in A) == A
        )
        product_marginals = 1.0
        for x in A:
            product_marginals *= sum(K[a, x] for a in A)

        e1 = p_cycle - p_invariant
        e2 = p_invariant - product_marginals
        max_cycle_minus_invariant = max(max_cycle_minus_invariant, e1)
        max_invariant_minus_product = max(max_invariant_minus_product, e2)
        if product_marginals > 0:
            ratio = p_cycle / product_marginals
            if ratio > max_cycle_over_product:
                max_cycle_over_product = ratio
                worst = {
                    "A": sorted(A),
                    "p_cycle": p_cycle,
                    "p_invariant": p_invariant,
                    "product_marginals": product_marginals,
                    "ratio": ratio,
                }

    tol = 2e-12
    return {
        "pass": bool(
            max_cycle_minus_invariant <= tol
            and max_invariant_minus_product <= tol
        ),
        "max_cycle_minus_invariant": float(max_cycle_minus_invariant),
        "max_invariant_minus_product": float(max_invariant_minus_product),
        "max_cycle_over_product": float(max_cycle_over_product),
        "max_ratio_case": worst,
    }


def homogeneous_case(n, edges, t):
    perms = all_perms(n)
    index = {p: i for i, p in enumerate(perms)}
    Q = generator(perms, index, edges)
    law = expm(t * Q)[index[tuple(range(n))]]
    K = expected_perm_kernel(perms, law)
    out = check_law(perms, law, K)
    out["max_kernel_asymmetry"] = float(np.max(np.abs(K - K.T)))
    return out


def conditional_time_inhomogeneous_case():
    n = 4
    perms = all_perms(n)
    index = {p: i for i, p in enumerate(perms)}
    law = np.zeros(len(perms))
    law[index[tuple(range(n))]] = 1.0

    segments = [
        ("random", 0.35, [(0, 1), (1, 2), (2, 3)]),
        ("forced", (1, 2)),
        ("random", 0.40, [(0, 1), (2, 3), (3, 0)]),
        ("forced", (3, 0)),
        ("random", 0.25, [(1, 2), (2, 3)]),
    ]

    for seg in segments:
        if seg[0] == "random":
            _, dt, edges = seg
            law = law @ expm(dt * generator(perms, index, edges))
        else:
            _, edge = seg
            law = law @ deterministic_ring_matrix(perms, index, edge)

    K = expected_perm_kernel(perms, law)
    out = check_law(perms, law, K)
    out["max_kernel_asymmetry"] = float(np.max(np.abs(K - K.T)))
    out["kernel"] = K.tolist()
    return out


def main():
    cases = {
        "path4_t1.2": homogeneous_case(
            4, [(0, 1), (1, 2), (2, 3)], 1.2
        ),
        "cycle4_t1.2": homogeneous_case(
            4, [(0, 1), (1, 2), (2, 3), (3, 0)], 1.2
        ),
        "cycle5_t1.2": homogeneous_case(
            5, [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)], 1.2
        ),
        "star5_t1.2": homogeneous_case(
            5, [(0, 1), (0, 2), (0, 3), (0, 4)], 1.2
        ),
        "conditional_time_inhomogeneous_forced": conditional_time_inhomogeneous_case(),
    }

    payload = {
        "status": "PASS" if all(v["pass"] for v in cases.values()) else "FAIL",
        "interpretation": (
            "Finite-state sanity check only; analytic proof uses Borcea-Branden-Liggett "
            "strong-Rayleigh preservation and negative association."
        ),
        "cases": cases,
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
