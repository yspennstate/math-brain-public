#!/usr/bin/env python3
"""
HARD10-03 finite-state sanity checker for the master determinant identity.

On the 4-cycle C4, enumerate all 4! interchange permutations exactly as a
finite-state continuous-time Markov chain and check numerically that

    E det(I - A Pi_t) = det(I - A p_t)

for several deterministic random matrices A. Also check the spatial corollary

    P(no permutation cycle is wholly contained in S)
      = det(I - p_t[S,S]).

This is a floating-point certificate only. The analytic proof is in
runs/2026-09-15/2026-09-15T15-34-11Z__report.md.
"""

import itertools
import numpy as np
from scipy.linalg import expm


def compose(P, Q):
    return tuple(P[Q[i]] for i in range(len(P)))


def transposition(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def permutation_matrix(P):
    n = len(P)
    M = np.zeros((n, n))
    # Column i is sent to basis vector P(i).
    for i, j in enumerate(P):
        M[j, i] = 1.0
    return M


def cycle_partition(P):
    n = len(P)
    seen = set()
    cycles = []
    for i in range(n):
        if i in seen:
            continue
        c = []
        x = i
        while x not in seen:
            seen.add(x)
            c.append(x)
            x = P[x]
        cycles.append(c)
    return cycles


def full_interchange_generator(n):
    edges = [(i, (i + 1) % n) for i in range(n)]
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    G = np.zeros((len(perms), len(perms)))
    for p in perms:
        i = idx[p]
        for a, b in edges:
            q = compose(transposition(n, a, b), p)
            G[i, idx[q]] += 1.0
            G[i, i] -= 1.0
    return edges, perms, idx, G


def one_particle_generator(n, edges):
    L = np.zeros((n, n))
    for a, b in edges:
        L[a, b] += 1.0
        L[b, a] += 1.0
        L[a, a] -= 1.0
        L[b, b] -= 1.0
    return L


def check(n=4, beta=0.7, seed=3):
    edges, perms, idx, G = full_interchange_generator(n)
    identity = tuple(range(n))
    law = expm(beta * G)[idx[identity]]

    L = one_particle_generator(n, edges)
    p_t = expm(beta * L)

    rng = np.random.default_rng(seed)
    determinant_errors = []
    for _ in range(5):
        A = rng.normal(size=(n, n)) / 4.0
        lhs = sum(
            w * np.linalg.det(np.eye(n) - A @ permutation_matrix(P))
            for w, P in zip(law, perms)
        )
        rhs = np.linalg.det(np.eye(n) - A @ p_t)
        determinant_errors.append(abs(lhs - rhs))

    S = {0, 1}
    lhs_avoid = sum(
        w
        for w, P in zip(law, perms)
        if all(not set(C).issubset(S) for C in cycle_partition(P))
    )
    inds = sorted(S)
    rhs_avoid = np.linalg.det(
        np.eye(len(inds)) - p_t[np.ix_(inds, inds)]
    )

    out = {
        "n": n,
        "beta": beta,
        "max_master_determinant_error": max(determinant_errors),
        "spatial_avoidance_probability": lhs_avoid,
        "spatial_avoidance_determinant": rhs_avoid,
        "spatial_avoidance_error": abs(lhs_avoid - rhs_avoid),
    }
    return out


if __name__ == "__main__":
    out = check()
    print(out)
    assert out["max_master_determinant_error"] < 2e-12
    assert out["spatial_avoidance_error"] < 2e-12
