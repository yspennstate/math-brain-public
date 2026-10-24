#!/usr/bin/env python3
"""Finite-state sanity check for HARD10-03 NEW-L15/A1.

Enumerates the interchange process on a cycle graph, compares the exact rooted
cycle sums against the determinant/resolvent formulas, and checks the elementary
short-cycle bound under the other-cycles-hitting tilt.

This is only a numerical certificate; the proof is in the Markdown reports.
"""
import itertools
import json
import numpy as np
from scipy.linalg import expm


def compose(P, Q):
    return tuple(P[Q[i]] for i in range(len(P)))


def tau(n, a, b):
    p = list(range(n))
    p[a], p[b] = p[b], p[a]
    return tuple(p)


def edges(n):
    return [(i, (i + 1) % n) for i in range(n)]


def full_generator(n):
    perms = list(itertools.permutations(range(n)))
    idx = {p: i for i, p in enumerate(perms)}
    G = np.zeros((len(perms), len(perms)))
    for p in perms:
        i = idx[p]
        for a, b in edges(n):
            tr = tau(n, a, b)
            q = compose(tr, p)
            G[i, idx[q]] += 1.0
            G[i, i] -= 1.0
    return perms, idx, G


def one_generator(n):
    G = np.zeros((n, n))
    for a, b in edges(n):
        G[a, b] += 1.0
        G[b, a] += 1.0
        G[a, a] -= 1.0
        G[b, b] -= 1.0
    return G


def cycles_of_perm(p):
    n = len(p)
    seen = [False] * n
    out = []
    for i in range(n):
        if seen[i]:
            continue
        c = []
        x = i
        while not seen[x]:
            seen[x] = True
            c.append(x)
            x = p[x]
        out.append(c)
    return out


def check(n=5, beta=1.2, z=0.67, root=0, M=2):
    perms, idx, G = full_generator(n)
    identity = tuple(range(n))
    law = expm(beta * G)[idx[identity]]
    K = expm(beta * one_generator(n))

    mat = np.eye(n) - z * K
    D = float(np.linalg.det(mat))
    R = float((K @ np.linalg.inv(mat))[root, root])

    rooted = 0.0
    other_weight = 0.0
    short_weight = 0.0

    for weight, p in zip(law, perms):
        cs = cycles_of_perm(p)
        c0 = next(c for c in cs if root in c)
        L = len(c0)

        W = 1.0
        for c in cs:
            if c is c0:
                continue
            W *= 1.0 - z ** len(c)

        rooted += weight * (z ** (L - 1)) * W
        other_weight += weight * W
        if L <= M:
            short_weight += weight * W

    tilted_short = short_weight / other_weight
    short_bound = (z ** (1 - M)) * R / (1.0 + z * R)

    result = {
        "n": n,
        "beta": beta,
        "z": z,
        "root": root,
        "M": M,
        "D": D,
        "R": R,
        "E_zLminus1_W": rooted,
        "D_times_R": D * R,
        "rooted_identity_abs_error": abs(rooted - D * R),
        "E_W": other_weight,
        "D_times_1_plus_zR": D * (1.0 + z * R),
        "other_weight_identity_abs_error": abs(other_weight - D * (1.0 + z * R)),
        "tilted_P_L_le_M": tilted_short,
        "tilted_short_cycle_bound": short_bound,
        "bound_holds": tilted_short <= short_bound + 1e-12,
    }
    return result


if __name__ == "__main__":
    ans = check()
    print(json.dumps(ans, indent=2, sort_keys=True))
    assert ans["rooted_identity_abs_error"] < 2e-12
    assert ans["other_weight_identity_abs_error"] < 2e-12
    assert ans["bound_holds"]
