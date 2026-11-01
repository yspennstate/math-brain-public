#!/usr/bin/env python3
"""
Corrected finite-state sanity check for HARD10-03 NEW-L24/NEW-L27.

This supersedes (without overwriting)
  artifacts/2026-09-15T19-41-00Z__conditional_determinant_check.py
whose final singleton check mistakenly used ||K_S||_HS^2 as the theorem's h^2.
NEW-L27 defines h^2 = |S| * a, where a is an upper bound on every entry of
K_S. The analytic report is unaffected; this file implements that parameter
correctly.

Graph: C4. Edge (3,0) is frozen to ring once at time 0.37. The other three
edge clocks remain rate-one Poisson. We use t=3 so the singleton h<=1/2
hypothesis is actually satisfied.
"""
import itertools
import json
import numpy as np
from scipy.linalg import expm


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def transposition(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def perm_matrix(p):
    n = len(p)
    M = np.zeros((n, n))
    for x, y in enumerate(p):
        M[x, y] = 1.0
    return M


def cycles(p):
    seen = set()
    out = []
    for x in range(len(p)):
        if x in seen:
            continue
        c = []
        y = x
        while y not in seen:
            seen.add(y)
            c.append(y)
            y = p[y]
        out.append(c)
    return out


def check(t=3.0, frozen_time=0.37):
    n = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    frozen_edge = (3, 0)
    free_edges = [e for e in edges if e != frozen_edge]
    tr = transposition(n, *frozen_edge)
    T = perm_matrix(tr)

    perms = list(itertools.permutations(range(n)))
    index = {p: i for i, p in enumerate(perms)}
    ident = tuple(range(n))

    Q = np.zeros((len(perms), len(perms)))
    for p in perms:
        i = index[p]
        for e in free_edges:
            q = compose(transposition(n, *e), p)
            Q[i, index[q]] += 1.0
            Q[i, i] -= 1.0

    L = np.zeros((n, n))
    for a, b in free_edges:
        L[a, b] += 1.0
        L[b, a] += 1.0
        L[a, a] -= 1.0
        L[b, b] -= 1.0

    law = np.zeros(len(perms))
    law[index[ident]] = 1.0
    law = law @ expm(frozen_time * Q)
    after = np.zeros_like(law)
    for p, w in zip(perms, law):
        after[index[compose(tr, p)]] += w
    law = after @ expm((t - frozen_time) * Q)

    K = expm(frozen_time * L) @ T @ expm((t - frozen_time) * L)

    K_from_perm = np.zeros((n, n))
    for p, w in zip(perms, law):
        for x in range(n):
            K_from_perm[x, p[x]] += w

    A = np.array([
        [0.07, -0.03, 0.02, 0.01],
        [0.04, 0.05, -0.02, 0.03],
        [-0.01, 0.02, 0.06, -0.04],
        [0.03, 0.01, 0.02, 0.04],
    ])
    lhs = sum(
        w * np.linalg.det(np.eye(n) - A @ perm_matrix(p))
        for p, w in zip(perms, law)
    )
    rhs = np.linalg.det(np.eye(n) - A @ K)

    S = [0, 1]
    KS = K[np.ix_(S, S)]
    det_local = np.linalg.det(np.eye(len(S)) - KS)
    no_cycle_prob = sum(
        w
        for p, w in zip(perms, law)
        if not any(set(c).issubset(S) for c in cycles(p))
    )

    # Correct implementation of NEW-L27 on S={1}.
    S1 = [1]
    K1 = K[np.ix_(S1, S1)]
    a = float(np.max(K1))
    h2 = len(S1) * a
    h = h2 ** 0.5
    trap1 = 1.0 - float(np.linalg.det(np.eye(1) - K1))
    bound1 = 2.0 * h2

    out = {
        "t": t,
        "frozen_edge": list(frozen_edge),
        "frozen_ring_time": frozen_time,
        "kernel_from_permutation_max_error": float(np.max(np.abs(K - K_from_perm))),
        "conditional_master_det_error": float(abs(lhs - rhs)),
        "local_no_cycle_det_error": float(abs(det_local - no_cycle_prob)),
        "conditional_kernel_nonsymmetry": float(np.max(np.abs(K - K.T))),
        "singleton_entry_upper_bound_a": a,
        "singleton_h2_equals_cardinality_times_a": h2,
        "singleton_h": h,
        "singleton_trap_probability": trap1,
        "singleton_2h2_bound": bound1,
        "singleton_bound_hypothesis_h_le_half": bool(h <= 0.5),
        "singleton_bound_verified": bool(trap1 <= bound1 + 1e-12),
    }

    assert out["kernel_from_permutation_max_error"] < 1e-12
    assert out["conditional_master_det_error"] < 1e-12
    assert out["local_no_cycle_det_error"] < 1e-12
    assert out["conditional_kernel_nonsymmetry"] > 1e-4
    assert out["singleton_bound_hypothesis_h_le_half"]
    assert out["singleton_bound_verified"]
    return out


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
