#!/usr/bin/env python3
"""Deterministic product-biased checks for the block restriction lemma."""

import json
import math
import numpy as np

from check_numaro_multiplicity import reconstruct as reconstruct_numaro, PIVOTS


def entropy(w):
    w = np.asarray(w, dtype=float)
    w = w[w > 0]
    return float(np.sum(-w * np.log2(w)))


def biased_coefficients(table, biases):
    n = len(biases)
    a = np.asarray(table, dtype=float).reshape([2] * n, order="F")
    # Start with sqrt(mu(x)) f(x), then apply U_i^T on each axis.
    for i, p in enumerate(biases):
        weights = np.array([math.sqrt(1-p), math.sqrt(p)])
        shape = [1] * n
        shape[i] = 2
        a = a * weights.reshape(shape)
    for i, p in enumerate(biases):
        U = np.array([[math.sqrt(1-p), -math.sqrt(p)],
                      [math.sqrt(p), math.sqrt(1-p)]])
        a = np.moveaxis(a, i, 0)
        a = np.tensordot(U.T, a, axes=(1, 0))
        a = np.moveaxis(a, 0, i)
    return a.reshape(-1, order="F")


def restrict_table(table, n, A, z):
    A = tuple(A)
    B = tuple(i for i in range(n) if i not in A)
    out = []
    for y in range(1 << len(B)):
        x = sum(((z >> j) & 1) << i for j, i in enumerate(A))
        x += sum(((y >> j) & 1) << i for j, i in enumerate(B))
        out.append(table[x])
    return np.array(out, dtype=np.int8)


def block_metrics(table, biases, A):
    n = len(biases)
    A = tuple(sorted(A))
    B = tuple(i for i in range(n) if i not in A)
    mask = sum(1 << i for i in A)
    w = biased_coefficients(table, biases) ** 2
    H = entropy(w)
    q = {}
    for s, mass in enumerate(w):
        q[s & ~mask] = q.get(s & ~mask, 0.0) + mass
    M = H - entropy(list(q.values()))
    avg_child_H = 0.0
    for z in range(1 << len(A)):
        prob = 1.0
        for j, i in enumerate(A):
            prob *= biases[i] if ((z >> j) & 1) else 1-biases[i]
        child = restrict_table(table, n, A, z)
        avg_child_H += prob * entropy(biased_coefficients(child, [biases[i] for i in B]) ** 2)
    L = H - avg_child_H
    J = L - M
    delta = sum(
        entropy([p, 1-p]) + math.log2(max(p, 1-p))
        for i, p in enumerate(biases) if i in A
    )
    return dict(H=H, M=M, J=J, L=L, delta_MU=delta,
                upper_gap=2*M+delta-L, child_H=avg_child_H)


def quadratic_pair():
    return np.array([1, 1, 1, -1], dtype=np.int8)


def main():
    rows = []
    # Two-bit genuine Boolean gate: sweep one input bias, retain the other uniform.
    for p in [1/1024, 1/64, 1/8, 1/4, 3/8, 1/2, 5/8, 3/4, 7/8, 63/64, 1023/1024]:
        r = block_metrics(quadratic_pair(), [p, .5], [0])
        assert r["J"] >= -2e-10 and r["upper_gap"] >= -2e-10
        r.update(family="quadratic_pair", p=p, A=[0])
        rows.append(r)

    # Exact composition-prime 18-bit Numaro source gate at the known adversarial bias.
    gate = reconstruct_numaro()
    for p in [3/8, 223/456, 1/2]:
        biases = [p] + [.5] * 17
        for A in [[0], [0, 9], [9], [9, PIVOTS[0]]]:
            r = block_metrics(gate, biases, A)
            assert r["J"] >= -2e-9 and r["upper_gap"] >= -2e-9
            r.update(family="numaro_prime", p0=p, A=A)
            rows.append(r)

    print(json.dumps({"status":"PASS", "randomness":"NONE", "rows":rows}, indent=2))


if __name__ == "__main__":
    main()
