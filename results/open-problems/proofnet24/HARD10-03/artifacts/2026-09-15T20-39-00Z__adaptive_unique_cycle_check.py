#!/usr/bin/env python3
"""
HARD10-03 finite-state sanity checks for:
  * NEW-L28 adaptive/partial-space-time conditional determinant identity;
  * NEW-L30 exact unique-anchor-cycle identity;
  * the elementary resolvent bound used in NEW-L31.

The exploration history is represented by a concrete admissible branch:
  - edge (0,1) is exposed for the full period, with one known mark at t=.25;
  - edge (2,3) is exposed only on [0,.5], with one known mark at t=.40;
  - all other edge-time regions remain fresh Poisson.
Conditional on that history, the remaining process is time-inhomogeneous.
This is a numerical finite-state certificate only, not a proof.
"""
import itertools
import json
import numpy as np
from scipy.linalg import expm


def compose(P, Q):
    """P after Q."""
    return tuple(P[Q[i]] for i in range(len(P)))


def transposition(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def permutation_matrix(p):
    n = len(p)
    M = np.zeros((n, n))
    for source, dest in enumerate(p):
        M[dest, source] = 1.0
    return M


def group_generator(n, edges, perms, idx):
    G = np.zeros((len(perms), len(perms)))
    trs = [transposition(n, *e) for e in edges]
    for p in perms:
        i = idx[p]
        for tr in trs:
            q = compose(tr, p)
            G[i, idx[q]] += 1.0
            G[i, i] -= 1.0
    return G


def one_particle_generator(n, edges):
    L = np.zeros((n, n))
    for a, b in edges:
        L[a, b] += 1.0
        L[b, a] += 1.0
        L[a, a] -= 1.0
        L[b, b] -= 1.0
    return L


def deterministic_left_multiply(law, tr, perms, idx):
    out = np.zeros_like(law)
    for p, w in zip(perms, law):
        out[idx[compose(tr, p)]] += w
    return out


def root_cycle(p, u):
    out = [u]
    x = p[u]
    while x != u:
        out.append(x)
        x = p[x]
    return out


def complete_cycles_in_S(p, S):
    S = set(S)
    seen = set()
    cycles = []
    for u in range(len(p)):
        if u in seen:
            continue
        c = root_cycle(p, u)
        seen.update(c)
        if set(c).issubset(S):
            cycles.append(tuple(c))
    return cycles


def conditional_law_and_kernel():
    n = 4
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    ident = tuple(range(n))
    law = np.zeros(len(perms))
    law[idx[ident]] = 1.0
    K = np.eye(n)

    # (duration, random/free edges during interval, deterministic mark after interval)
    schedule = [
        (0.25, [(1, 2), (2, 3), (3, 0)], (0, 1)),
        (0.15, [(1, 2), (3, 0)], (2, 3)),
        (0.10, [(1, 2), (3, 0)], None),
        (0.50, [(1, 2), (2, 3), (3, 0)], None),
    ]

    for dt, free_edges, known_mark in schedule:
        G = group_generator(n, free_edges, perms, idx)
        law = law @ expm(dt * G)

        L = one_particle_generator(n, free_edges)
        K = expm(dt * L) @ K

        if known_mark is not None:
            tr = transposition(n, *known_mark)
            law = deterministic_left_multiply(law, tr, perms, idx)
            K = permutation_matrix(tr) @ K

    return n, perms, idx, law, K


def check():
    n, perms, idx, law, K = conditional_law_and_kernel()

    K_from_group = sum(
        w * permutation_matrix(p) for p, w in zip(perms, law)
    )
    one_particle_error = float(np.max(np.abs(K - K_from_group)))

    rng = np.random.default_rng(20260915)
    determinant_errors = []
    for _ in range(8):
        A = 0.12 * rng.normal(size=(n, n))
        lhs = sum(
            w * np.linalg.det(np.eye(n) - A @ permutation_matrix(p))
            for p, w in zip(perms, law)
        )
        rhs = np.linalg.det(np.eye(n) - A @ K)
        determinant_errors.append(abs(lhs - rhs))

    # NEW-L30 on S={0,1}; q<1 is enough for the exact identity.
    S = [0, 1]
    KS = K[np.ix_(S, S)]
    D = np.linalg.det(np.eye(len(S)) - KS)
    R = KS @ np.linalg.inv(np.eye(len(S)) - KS)
    u_local = S.index(0)

    p_unique = 0.0
    for p, w in zip(perms, law):
        c0 = set(root_cycle(p, 0))
        complete = complete_cycles_in_S(p, S)
        if c0.issubset(set(S)) and len(complete) == 1:
            p_unique += w
    unique_identity_error = float(abs(p_unique - D * R[u_local, u_local]))

    # NEW-L31 elementary resolvent bound on singleton S0={0},
    # which has row sum q=K00<1/2 for this concrete history.
    S0 = [0]
    K0 = K[np.ix_(S0, S0)]
    a = float(np.max(K0))
    q = float(np.max(K0.sum(axis=1)))
    R0 = K0 @ np.linalg.inv(np.eye(1) - K0)
    resolvent_diag = float(R0[0, 0])
    elementary_bound = float(a / (1.0 - q))
    fixed_point_probability = float(
        sum(w for p, w in zip(perms, law) if p[0] == 0)
    )

    return {
        "one_particle_kernel_error": one_particle_error,
        "conditional_determinant_max_error": float(max(determinant_errors)),
        "unique_anchor_cycle_identity_error": unique_identity_error,
        "unique_anchor_cycle_probability_S01": float(p_unique),
        "unique_anchor_cycle_rhs_S01": float(D * R[u_local, u_local]),
        "singleton_row_sum_q": q,
        "singleton_entry_bound_a": a,
        "singleton_resolvent_diag": resolvent_diag,
        "singleton_a_over_1_minus_q": elementary_bound,
        "singleton_fixed_point_probability": fixed_point_probability,
        "nonselfadjointness_max": float(np.max(np.abs(K - K.T))),
    }


if __name__ == "__main__":
    out = check()
    print(json.dumps(out, indent=2, sort_keys=True))
    assert out["one_particle_kernel_error"] < 2e-12
    assert out["conditional_determinant_max_error"] < 2e-12
    assert out["unique_anchor_cycle_identity_error"] < 2e-12
    assert out["singleton_row_sum_q"] < 0.5
    assert out["singleton_resolvent_diag"] <= out["singleton_a_over_1_minus_q"] + 1e-12
