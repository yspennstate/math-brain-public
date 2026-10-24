#!/usr/bin/env python3
"""
Finite-state sanity check for HARD10-03 NEW-L24/NEW-L27.

Graph: C4. The edge (3,0) is frozen to ring once at a deterministic time;
the other three edge clocks remain independent rate-one Poisson processes.
We enumerate the full conditional interchange semigroup on S4 and compare it
with the conditional one-particle kernel.

Checks:
  1. K_cond equals the endpoint kernel obtained from the conditional
     permutation distribution.
  2. E[det(I-A Pi) | frozen clocks] = det(I-A K_cond) for a fixed dense A.
  3. For S={0,1}, det(I-K_cond[S,S]) equals the conditional probability that
     no permutation cycle is wholly contained in S.
  4. K_cond is genuinely non-self-adjoint, demonstrating why the archived
     unconditional PSD argument cannot simply be reused after conditioning.
  5. For the singleton S={1}, the singular-value bound used in NEW-L27 is
     numerically valid when its h<=1/2 hypothesis holds.

Floating-point matrix exponentials are only a sanity check. The report contains
analytic proofs.
"""
import itertools
import json
import numpy as np
from scipy.linalg import expm


def compose(p, q):
    """p o q."""
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


def check(t=1.2, frozen_time=0.37):
    n = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    frozen_edge = (3, 0)
    free_edges = [e for e in edges if e != frozen_edge]
    tr = transposition(n, *frozen_edge)
    T = perm_matrix(tr)

    perms = list(itertools.permutations(range(n)))
    index = {p: i for i, p in enumerate(perms)}
    ident = tuple(range(n))

    # Conditional permutation generator: only free edges are random.
    Q = np.zeros((len(perms), len(perms)))
    for p in perms:
        i = index[p]
        for e in free_edges:
            q = compose(transposition(n, *e), p)
            Q[i, index[q]] += 1.0
            Q[i, i] -= 1.0

    # Conditional one-particle generator on free edges.
    L = np.zeros((n, n))
    for a, b in free_edges:
        L[a, b] += 1.0
        L[b, a] += 1.0
        L[a, a] -= 1.0
        L[b, b] -= 1.0

    intervals = [frozen_time, t - frozen_time]

    law = np.zeros(len(perms))
    law[index[ident]] = 1.0
    law = law @ expm(intervals[0] * Q)
    after = np.zeros_like(law)
    for p, w in zip(perms, law):
        after[index[compose(tr, p)]] += w
    law = after @ expm(intervals[1] * Q)

    K = np.eye(n) @ expm(intervals[0] * L) @ T @ expm(intervals[1] * L)

    K_from_perm = np.zeros((n, n))
    for p, w in zip(perms, law):
        for x in range(n):
            K_from_perm[x, p[x]] += w

    # Dense deterministic test matrix.
    A = np.array([
        [0.07, -0.03, 0.02, 0.01],
        [0.04, 0.05, -0.02, 0.03],
        [-0.01, 0.02, 0.06, -0.04],
        [0.03, 0.01, 0.02, 0.04],
    ])
    lhs = 0.0
    for p, w in zip(perms, law):
        lhs += w * np.linalg.det(np.eye(n) - A @ perm_matrix(p))
    rhs = np.linalg.det(np.eye(n) - A @ K)

    S = [0, 1]
    KS = K[np.ix_(S, S)]
    det_local = np.linalg.det(np.eye(len(S)) - KS)
    no_cycle_prob = 0.0
    for p, w in zip(perms, law):
        if not any(set(c).issubset(S) for c in cycles(p)):
            no_cycle_prob += w

    # Singleton test for NEW-L27's h<=1/2 regime.
    S1 = [1]
    K1 = K[np.ix_(S1, S1)]
    hs2 = float(np.sum(K1 * K1))
    h = hs2 ** 0.5
    trap1 = 1.0 - float(np.linalg.det(np.eye(1) - K1))
    bound1 = 2.0 * hs2

    out = {
        "t": t,
        "frozen_edge": list(frozen_edge),
        "frozen_ring_time": frozen_time,
        "kernel_from_permutation_max_error": float(np.max(np.abs(K - K_from_perm))),
        "conditional_master_det_error": float(abs(lhs - rhs)),
        "local_no_cycle_det_error": float(abs(det_local - no_cycle_prob)),
        "conditional_kernel_nonsymmetry": float(np.max(np.abs(K - K.T))),
        "singleton_h": h,
        "singleton_trap_probability": trap1,
        "singleton_2hs2_bound": bound1,
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
