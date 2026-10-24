#!/usr/bin/env python3
"""
Finite-state sanity checker for HARD10-03 NEW-L19 and NEW-L22.

Enumerates the interchange process on C4 exactly at the state-space level,
using floating-point matrix exponentials only for the continuous-time law.
The analytic proofs are in the corresponding Markdown report; this script is
not a substitute for those proofs.
"""
import itertools
import numpy as np
from scipy.linalg import expm


def compose(P, Q):
    return tuple(P[Q[i]] for i in range(len(P)))


def tau(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def cycle_edges(n):
    return [(i, (i + 1) % n) for i in range(n)]


def full_generator(n):
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    G = np.zeros((len(perms), len(perms)))
    for p in perms:
        i = idx[p]
        for a, b in cycle_edges(n):
            q = compose(tau(n, a, b), p)
            G[i, idx[q]] += 1.0
            G[i, i] -= 1.0
    return perms, idx, G


def tagged_generator(n):
    G = np.zeros((n, n))
    for a, b in cycle_edges(n):
        G[a, b] += 1.0
        G[b, a] += 1.0
        G[a, a] -= 1.0
        G[b, b] -= 1.0
    return G


def cycles_of_perm(p):
    seen = set()
    out = []
    for a in range(len(p)):
        if a in seen:
            continue
        c = []
        x = a
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = p[x]
        out.append(c)
    return out


def root_cycle(p, u):
    c = []
    x = u
    while True:
        x = p[x]
        c.append(x)
        if x == u:
            return c


def oriented_distance(p, u, v):
    c = root_cycle(p, u)
    for j, x in enumerate(c, 1):
        if x == v:
            return j
    return None


def localized_G(p, S, z, u, v):
    """Exact G_{S,z}^pi(u,v) from the report."""
    S = set(S)
    c = root_cycle(p, u)
    # If the entire root cycle lies in S, repetitions are geometric.
    if set(c).issubset(S):
        d = oriented_distance(p, u, v)
        if d is None:
            return 0.0
        L = len(c)
        return z ** (d - 1) / (1.0 - z ** L)

    # Otherwise only the segment before the first exit from S contributes.
    x = u
    for m in range(1, len(p) + 1):
        x = p[x]
        if x not in S:
            return 0.0
        if x == v:
            return z ** (m - 1)
    return 0.0


def check(n=4, t=0.7, z=0.43, u=0, v=2, S=(0, 1, 2)):
    perms, idx, G = full_generator(n)
    law = expm(t * G)[idx[tuple(range(n))]]
    K = expm(t * tagged_generator(n))

    # NEW-L19 global off-diagonal identity.
    D = np.linalg.det(np.eye(n) - z * K)
    R = K @ np.linalg.inv(np.eye(n) - z * K)
    lhs_global = 0.0
    for w, p in zip(law, perms):
        d = oriented_distance(p, u, v)
        if d is None:
            continue
        W = 1.0
        for c in cycles_of_perm(p):
            if u not in c:
                W *= 1.0 - z ** len(c)
        lhs_global += w * z ** (d - 1) * W
    rhs_global = D * R[v, u]

    # NEW-L22 localized identity.
    S = tuple(S)
    KS = K[np.ix_(S, S)]
    DS = np.linalg.det(np.eye(len(S)) - z * KS)
    RS = KS @ np.linalg.inv(np.eye(len(S)) - z * KS)
    iu, iv = S.index(u), S.index(v)

    lhs_local = 0.0
    lhs_local_unweighted = 0.0
    for w, p in zip(law, perms):
        Delta = 1.0
        for c in cycles_of_perm(p):
            if set(c).issubset(S):
                Delta *= 1.0 - z ** len(c)
        g = localized_G(p, S, z, u, v)
        lhs_local += w * Delta * g
        lhs_local_unweighted += w * g
    rhs_local = DS * RS[iv, iu]

    result = {
        "global_lhs": float(lhs_global),
        "global_rhs": float(rhs_global),
        "global_abs_error": float(abs(lhs_global - rhs_global)),
        "localized_lhs": float(lhs_local),
        "localized_rhs": float(rhs_local),
        "localized_abs_error": float(abs(lhs_local - rhs_local)),
        "localized_unweighted_lhs": float(lhs_local_unweighted),
        "localized_lower_bound_rhs": float(rhs_local),
        "lower_bound_holds": bool(lhs_local_unweighted + 1e-13 >= rhs_local),
    }
    print(result)
    assert result["global_abs_error"] < 2e-12
    assert result["localized_abs_error"] < 2e-12
    assert result["lower_bound_holds"]
    return result


if __name__ == "__main__":
    check()
