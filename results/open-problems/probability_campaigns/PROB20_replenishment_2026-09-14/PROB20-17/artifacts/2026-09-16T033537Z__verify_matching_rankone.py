#!/usr/bin/env python3
"""Deterministic corroborative checks for PROB20-17 T033537Z.

Numerics are not part of the proof.  This script checks:
  * maximum-matching counts/means for n=4,5,6;
  * direct owner averages on weak-interaction commuting PSD examples;
  * exact rank-one transfer identity;
  * scaled equiangular rank-one theorem for n=3,...,7;
  * rank-one coherence-certificate examples.
"""

import itertools
import math
import numpy as np

SEED = 20260916033537
rng = np.random.default_rng(SEED)


def opnorm(A):
    return np.linalg.norm(A, 2)


def owner_averages(mats):
    n = len(mats)
    d = mats[0].shape[0]
    distinct = 0.0
    for perm in itertools.permutations(range(n)):
        W = np.eye(d)
        for i in perm:
            W = W @ mats[i]
        distinct += opnorm(W)
    distinct /= math.factorial(n)

    replacement = 0.0
    for seq in itertools.product(range(n), repeat=n):
        W = np.eye(d)
        for i in seq:
            W = W @ mats[i]
        replacement += opnorm(W)
    replacement /= n ** n
    return distinct, replacement


def maximum_matchings(n):
    m = n // 2
    out = set()

    def pair_rec(rem, pairs):
        if not rem:
            key = tuple(sorted(tuple(sorted(e)) for e in pairs))
            out.add(key)
            return
        i = rem[0]
        for k in range(1, len(rem)):
            j = rem[k]
            pair_rec(rem[1:k] + rem[k + 1 :], pairs + [(i, j)])

    if n % 2 == 0:
        pair_rec(tuple(range(n)), [])
    else:
        for unmatched in range(n):
            rem = tuple(i for i in range(n) if i != unmatched)
            pair_rec(rem, [])

    assert all(len(M) == m for M in out)
    return sorted(out)


def matching_data(mats):
    n = len(mats)
    a = np.array([opnorm(A) for A in mats])
    gamma = np.eye(n)
    for i in range(n):
        for j in range(i + 1, n):
            gamma[i, j] = gamma[j, i] = opnorm(mats[i] @ mats[j]) / (a[i] * a[j])
    vals = []
    for M in maximum_matchings(n):
        z = 1.0
        for i, j in M:
            z *= gamma[i, j]
        vals.append(z)
    theta = np.sum(a ** n) / (n ** n * np.prod(a))
    return gamma, float(np.mean(vals)), theta


def weak_commuting_family(n, eps=0.01):
    mats = []
    for i in range(n):
        vals = np.full(n, eps)
        vals[i] = 1.0
        mats.append(np.diag(vals))
    return mats


def hamiltonian_average(G):
    n = G.shape[0]
    total = 0.0
    for p in itertools.permutations(range(n)):
        z = 1.0
        for k in range(n - 1):
            z *= G[p[k], p[k + 1]]
        total += z
    return total / math.factorial(n)


def rankone_transfer(a, G):
    n = len(a)
    q = np.sqrt(a)
    M = q[:, None] * G * q[None, :]
    replacement = (q @ np.linalg.matrix_power(M, n - 1) @ q) / (n ** n)
    distinct = np.prod(a) * hamiltonian_average(G)
    return distinct, replacement, M


def equiangular_check(n):
    a = np.exp(rng.normal(size=n))
    c = float(rng.uniform(0.05, 0.95))
    G = np.full((n, n), c)
    np.fill_diagonal(G, 1.0)
    lhs, rhs, M = rankone_transfer(a, G)
    qbar = (1.0 + (n - 1) * c) / n
    lower = np.prod(a) * qbar ** (n - 1)
    assert rhs + 1e-12 >= lower
    assert rhs + 1e-12 >= lhs
    return c, rhs / lhs, rhs / lower


def coherence_rankone_check(n, eps=0.15):
    d = n + 3
    common = np.zeros(d)
    common[-1] = 1.0
    U = []
    for i in range(n):
        v = np.zeros(d)
        v[i] = 1.0
        v += eps * common
        v /= np.linalg.norm(v)
        U.append(v)
    U = np.array(U)
    G = np.abs(U @ U.T)
    a = np.exp(rng.normal(size=n))
    lhs, rhs, _ = rankone_transfer(a, G)
    theta = np.sum(a ** n) / (n ** n * np.prod(a))
    gstar = np.max(G - np.eye(n))
    threshold = theta ** (1.0 / (n - 1))
    assert gstar <= threshold + 1e-12
    assert rhs + 1e-12 >= lhs
    return gstar, threshold, rhs / lhs


def main():
    print("seed", SEED)

    for n in (4, 5, 6):
        mats = weak_commuting_family(n)
        gamma, mm, theta = matching_data(mats)
        lhs, rhs = owner_averages(mats)
        gstar = np.max(gamma - np.eye(n))
        count = len(maximum_matchings(n))
        expected = math.prod(range(1, n, 2)) if n % 2 == 0 else n * math.prod(range(1, n - 1, 2))
        assert count == expected
        assert mm <= theta + 1e-14
        assert rhs + 1e-14 >= lhs
        print("weak", n, "count", count, "gstar", gstar, "matching", mm,
              "theta", theta, "rhs/lhs", rhs / lhs)

    for n in range(3, 8):
        c, ratio, lower_ratio = equiangular_check(n)
        print("equiangular", n, "c", c, "rhs/lhs", ratio,
              "rhs/JensenLower", lower_ratio)

    for n in (4, 5, 6):
        gstar, threshold, ratio = coherence_rankone_check(n)
        print("rankone-coherence", n, "gstar", gstar,
              "threshold", threshold, "rhs/lhs", ratio)

    print("PASS")


if __name__ == "__main__":
    main()
