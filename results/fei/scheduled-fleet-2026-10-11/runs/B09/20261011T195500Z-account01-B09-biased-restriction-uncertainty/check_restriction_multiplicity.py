#!/usr/bin/env python3
"""Deterministic checks for the physical-restriction multiplicity/KL ledger.

Fourier convention: normalized Walsh transform on {0,1}^n; truth values are signs.
No randomness is used.
"""

import json
import math
from functools import lru_cache

import numpy as np


def fwht(a):
    a = np.asarray(a, dtype=np.int64).copy()
    h = 1
    while h < len(a):
        v = a.reshape(-1, 2 * h)
        x, y = v[:, :h].copy(), v[:, h:].copy()
        v[:, :h], v[:, h:] = x + y, x - y
        h *= 2
    return a


def entropy(w):
    w = np.asarray(w, dtype=float)
    w = w[w > 0]
    return float(np.sum(-w * np.log2(w)))


def spectral_law(table):
    W = fwht(table).astype(float)
    return W * W / (len(table) ** 2)


def restrict_table(table, n, A, z):
    A = tuple(A)
    B = tuple(i for i in range(n) if i not in A)
    out = []
    for y in range(1 << len(B)):
        x = 0
        for j, i in enumerate(A):
            x |= ((z >> j) & 1) << i
        for j, i in enumerate(B):
            x |= ((y >> j) & 1) << i
        out.append(int(table[x]))
    return np.array(out, dtype=np.int8)


def block_metrics(table, n, A):
    A = tuple(sorted(A))
    mask = sum(1 << i for i in A)
    w = spectral_law(table)
    H = entropy(w)
    q = {}
    for s, p in enumerate(w):
        q[s & ~mask] = q.get(s & ~mask, 0.0) + p
    M = H - entropy(list(q.values()))
    child_H = np.mean([
        entropy(spectral_law(restrict_table(table, n, A, z)))
        for z in range(1 << len(A))
    ])
    L = H - child_H
    J = L - M
    return {"H": H, "M": M, "J": J, "L": L, "child_H": child_H}


def influence(table, n):
    w = spectral_law(table)
    return sum(p * s.bit_count() for s, p in enumerate(w))


def one_point_defect(n):
    out = np.ones(1 << n, dtype=np.int8)
    out[-1] = -1
    return out


def majority3():
    return np.array([1 if x.bit_count() <= 1 else -1 for x in range(8)], dtype=np.int8)


def sparse_activate(k, core):
    d = int(round(math.log2(len(core))))
    out = np.ones(1 << (k + d), dtype=np.int8)
    for x in range(1 << (k + d)):
        trigger = (x & ((1 << k) - 1)) == (1 << k) - 1
        if trigger:
            out[x] = core[x >> k]
    return out


def addressing(m):
    n = m + (1 << m)
    out = np.empty(1 << n, dtype=np.int8)
    for x in range(1 << n):
        address = x & ((1 << m) - 1)
        data = (x >> (m + address)) & 1
        out[x] = 1 if data == 0 else -1
    return out


def tensor(a, b):
    return np.array([a[x] * b[y] for y in range(len(b)) for x in range(len(a))], dtype=np.int8)


def quadratic_bent_tensor(m):
    # Product of m copies of (-1)^(x_{2j} x_{2j+1}).
    out = np.empty(1 << (2 * m), dtype=np.int8)
    for x in range(len(out)):
        phase = sum(((x >> (2*j)) & 1) * ((x >> (2*j+1)) & 1) for j in range(m)) & 1
        out[x] = -1 if phase else 1
    return out


def check_case(name, table, n, A):
    r = block_metrics(table, n, A)
    tol = 2e-10
    assert r["J"] >= -tol, (name, r)
    assert r["J"] <= r["M"] + tol, (name, r)
    assert abs(r["L"] - r["M"] - r["J"]) <= tol
    r.update(name=name, n=n, A=list(A), I=influence(table, n), H_over_I=r["H"] / influence(table, n))
    return r


def main():
    rows = []
    # Endpoint equality J=M: address block of an addressing function.
    for m in range(1, 4):
        rows.append(check_case(f"addressing_{m}", addressing(m), m + (1 << m), range(m)))

    # Endpoint equality J=0: reveal every bit of a sparse one-point defect.
    for n in range(2, 9):
        rows.append(check_case(f"one_point_full_{n}", one_point_defect(n), n, range(n)))

    # Genuine rare restrictions: trigger block of an activated majority gate.
    for k in range(1, 6):
        rows.append(check_case(f"activated_majority3_k{k}", sparse_activate(k, majority3()), k + 3, range(k)))

    # Tensor endpoint and block scaling.
    for m in range(1, 8):
        f = quadratic_bent_tensor(m)
        rows.append(check_case(f"quadratic_bent_{m}", f, 2*m, range(0, 2*m, 2)))

    print(json.dumps({"status": "PASS", "randomness": "NONE", "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
