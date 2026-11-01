#!/usr/bin/env python3
"""
Finite-state sanity check for HARD10-03 NEW-L11--NEW-L13.

On the cycle graph C_n, enumerate the complete interchange semigroup and verify:
  1. Bernoulli cycle-hitting probability = det(I-(1-r)p_t).
  2. Expected cycle-transversal polynomial = det((I-p_t)+qI).
  3. Probability the permutation is one cycle = any cofactor of I-p_t.

This is numerical corroboration only; the analytic proofs are in the report.
"""
import itertools
import math
import json
import numpy as np
from scipy.linalg import expm


def compose(P, Q):
    return tuple(P[Q[i]] for i in range(len(P)))


def transposition(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def edges_cycle(n):
    return [(i, (i + 1) % n) for i in range(n)]


def full_generator(n):
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    G = np.zeros((len(perms), len(perms)))
    trs = [transposition(n, *e) for e in edges_cycle(n)]
    for p in perms:
        i = idx[p]
        for tr in trs:
            q = compose(tr, p)
            G[i, idx[q]] += 1.0
            G[i, i] -= 1.0
    return perms, idx, G


def tagged_generator(n):
    L = np.zeros((n, n))
    for a, b in edges_cycle(n):
        L[a, b] += 1.0
        L[b, a] += 1.0
        L[a, a] -= 1.0
        L[b, b] -= 1.0
    return L


def cycle_lengths(p):
    n = len(p)
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        x = i
        ell = 0
        while not seen[x]:
            seen[x] = True
            ell += 1
            x = p[x]
        out.append(ell)
    return out


def hitting_polynomial(lens, n):
    # Product_C ((1+q)^|C| - 1), returned in ascending powers of q.
    poly = np.array([1.0])
    for ell in lens:
        factor = np.array([math.comb(ell, k) for k in range(ell + 1)], dtype=float)
        factor[0] = 0.0
        poly = np.convolve(poly, factor)
    if len(poly) < n + 1:
        poly = np.pad(poly, (0, n + 1 - len(poly)))
    return poly[: n + 1]


def check(n=4, t=0.7, r=0.23):
    perms, idx, G = full_generator(n)
    identity = tuple(range(n))
    law = expm(t * G)[idx[identity]]
    p = expm(t * tagged_generator(n))

    hit_lhs = 0.0
    expected_poly = np.zeros(n + 1)
    one_cycle_probability = 0.0

    for weight, perm in zip(law, perms):
        lens = cycle_lengths(perm)
        hit_lhs += weight * np.prod([1.0 - (1.0 - r) ** ell for ell in lens])
        expected_poly += weight * hitting_polynomial(lens, n)
        if len(lens) == 1:
            one_cycle_probability += weight

    hit_rhs = float(np.linalg.det(np.eye(n) - (1.0 - r) * p))

    lap = np.eye(n) - p
    evals = np.linalg.eigvalsh(lap)
    forest_poly = np.array([1.0])
    for lam in evals:
        forest_poly = np.convolve(forest_poly, np.array([lam, 1.0]))

    cofactor = float(np.linalg.det(lap[1:, 1:]))

    result = {
        "n": n,
        "t": t,
        "mark_probability": r,
        "bernoulli_hitting_lhs": float(hit_lhs),
        "bernoulli_hitting_rhs": hit_rhs,
        "bernoulli_hitting_abs_error": float(abs(hit_lhs - hit_rhs)),
        "transversal_forest_poly_max_error": float(np.max(np.abs(expected_poly - forest_poly))),
        "one_cycle_probability": float(one_cycle_probability),
        "laplacian_cofactor": cofactor,
        "one_cycle_abs_error": float(abs(one_cycle_probability - cofactor)),
        "laplacian_eigenvalues": [float(x) for x in evals],
    }

    assert result["bernoulli_hitting_abs_error"] < 1e-12
    assert result["transversal_forest_poly_max_error"] < 1e-12
    assert result["one_cycle_abs_error"] < 1e-12
    return result


if __name__ == "__main__":
    print(json.dumps(check(), indent=2, sort_keys=True))
