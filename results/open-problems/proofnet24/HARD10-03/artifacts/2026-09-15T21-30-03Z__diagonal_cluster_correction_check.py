#!/usr/bin/env python3
"""Finite-state sanity checks for HARD10-03 report 2026-09-15T21-28-05Z.

Checks on C4:
1. an admissible time-inhomogeneous conditional law with non-self-adjoint K;
2. the previously claimed off-diagonal same-cycle interpretation is false;
3. the mixed *diagonal* two-anchor identity NEW-L32 is correct;
4. in the unconditioned reversible law, the pair compensation is nonnegative
   and bounded by the two-point inclusion determinant of the shadow DPP.

Numerics are certificates/sanity checks only, not proofs.
"""
import itertools
import json
import numpy as np
from scipy.linalg import expm


def compose(P, Q):
    return tuple(P[Q[i]] for i in range(len(P)))


def transposition(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def permutation_matrix(p):
    M = np.zeros((len(p), len(p)))
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


def left_multiply_law(law, tr, perms, idx):
    out = np.zeros_like(law)
    for p, w in zip(perms, law):
        out[idx[compose(tr, p)]] += w
    return out


def root_cycle(p, u):
    c = [u]
    x = p[u]
    while x != u:
        c.append(x)
        x = p[x]
    return c


def complete_cycles_in_S(p, S):
    S = set(S)
    seen = set()
    out = []
    for u in range(len(p)):
        if u in seen:
            continue
        c = root_cycle(p, u)
        seen.update(c)
        if set(c).issubset(S):
            out.append(tuple(c))
    return out


def conditional_law():
    n = 4
    edges_all = [(0, 1), (1, 2), (2, 3), (3, 0)]
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    law = np.zeros(len(perms))
    law[idx[tuple(range(n))]] = 1.0
    K = np.eye(n)
    schedule = [
        (0.25, [(1, 2), (2, 3), (3, 0)], (0, 1)),
        (0.15, [(1, 2), (3, 0)], (2, 3)),
        (0.10, [(1, 2), (3, 0)], None),
        (0.50, [(1, 2), (2, 3), (3, 0)], None),
    ]
    for dt, free_edges, mark in schedule:
        law = law @ expm(dt * group_generator(n, free_edges, perms, idx))
        K = expm(dt * one_particle_generator(n, free_edges)) @ K
        if mark is not None:
            tr = transposition(n, *mark)
            law = left_multiply_law(law, tr, perms, idx)
            K = permutation_matrix(tr) @ K
    return n, edges_all, perms, idx, law, K


def unconditioned_law(t=1.0):
    n = 4
    edges = [(0, 1), (1, 2), (2, 3), (3, 0)]
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    law = expm(t * group_generator(n, edges, perms, idx))[idx[tuple(range(n))]]
    K = expm(t * one_particle_generator(n, edges))
    return perms, law, K


def anchored_probabilities(perms, law, S, u, v):
    p_one_same = 0.0
    p_two_distinct = 0.0
    for p, w in zip(perms, law):
        cycles = complete_cycles_in_S(p, S)
        if len(cycles) == 1:
            c = set(cycles[0])
            if u in c and v in c:
                p_one_same += w
        elif len(cycles) == 2:
            cu = next((set(c) for c in cycles if u in c), None)
            cv = next((set(c) for c in cycles if v in c), None)
            if cu is not None and cv is not None and cu != cv:
                p_two_distinct += w
    return p_one_same, p_two_distinct


def run():
    S = [0, 1, 2]
    u, v = 0, 1
    loc = {x: i for i, x in enumerate(S)}

    _, _, perms, _, law, K = conditional_law()
    KS = K[np.ix_(S, S)]
    D = np.linalg.det(np.eye(len(S)) - KS)
    R = KS @ np.linalg.inv(np.eye(len(S)) - KS)
    p1, p2 = anchored_probabilities(perms, law, S, u, v)
    cluster_rhs = D * np.linalg.det(R[np.ix_([loc[u], loc[v]], [loc[u], loc[v]])])

    # This is precisely the old, now-withdrawn off-diagonal interpretation.
    old_claim_rhs = D * R[loc[v], loc[u]]
    old_claim_gap = old_claim_rhs - p1

    # Verify the conditional one-particle kernel from the permutation law.
    K_group = sum(w * permutation_matrix(p) for p, w in zip(perms, law))

    perms_u, law_u, K_u = unconditioned_law(1.0)
    KSu = K_u[np.ix_(S, S)]
    Du = np.linalg.det(np.eye(len(S)) - KSu)
    Ru = KSu @ np.linalg.inv(np.eye(len(S)) - KSu)
    p1u, p2u = anchored_probabilities(perms_u, law_u, S, u, v)
    pair_cluster = Du * np.linalg.det(Ru[np.ix_([loc[u], loc[v]], [loc[u], loc[v]])])
    pair_inclusion = np.linalg.det(KSu[np.ix_([loc[u], loc[v]], [loc[u], loc[v]])])

    out = {
        "conditional_kernel_reconstruction_error": float(np.max(np.abs(K - K_group))),
        "conditional_kernel_nonselfadjointness": float(np.max(np.abs(K - K.T))),
        "old_offdiag_actual_unique_same_cycle": float(p1),
        "old_offdiag_claimed_rhs": float(old_claim_rhs),
        "old_offdiag_claim_gap": float(old_claim_gap),
        "conditional_two_anchor_lhs_p2_minus_p1": float(p2 - p1),
        "conditional_two_anchor_rhs": float(cluster_rhs),
        "conditional_two_anchor_error": float(abs((p2 - p1) - cluster_rhs)),
        "unconditioned_p1_same_unique_cycle": float(p1u),
        "unconditioned_p2_two_distinct_cycles": float(p2u),
        "unconditioned_pair_compensation": float(p2u - p1u),
        "unconditioned_shadow_dpp_exact_pair": float(pair_cluster),
        "unconditioned_dpp_pair_inclusion_bound": float(pair_inclusion),
    }

    assert out["conditional_kernel_reconstruction_error"] < 2e-12
    assert out["conditional_kernel_nonselfadjointness"] > 1e-4
    assert abs(out["old_offdiag_claim_gap"]) > 1e-2
    assert out["conditional_two_anchor_error"] < 2e-12
    assert out["unconditioned_pair_compensation"] >= -2e-12
    assert abs(out["unconditioned_pair_compensation"] - out["unconditioned_shadow_dpp_exact_pair"]) < 2e-12
    assert out["unconditioned_shadow_dpp_exact_pair"] <= out["unconditioned_dpp_pair_inclusion_bound"] + 2e-12
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    run()
