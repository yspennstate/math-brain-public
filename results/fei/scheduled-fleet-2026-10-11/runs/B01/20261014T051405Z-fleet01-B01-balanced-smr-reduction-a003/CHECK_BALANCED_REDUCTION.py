#!/usr/bin/env python3
"""Finite corroboration of the balanced-lift/tensor identities.

The all-dimensional proof is in PROOF.md.  This checker exhausts every
Boolean sign through dimension three and tests both the fresh-character
lift h(y,x)=y f(x) and disjoint tensor products.  It uses direct Walsh
arithmetic and binary64 logarithms; it is not the proof.
"""

from __future__ import annotations

import itertools
import math


def fwht(values):
    a = [float(v) for v in values]
    h = 1
    while h < len(a):
        for j in range(0, len(a), 2 * h):
            for k in range(j, j + h):
                x, y = a[k], a[k + h]
                a[k], a[k + h] = x + y, x - y
        h *= 2
    n = len(a)
    return [x / n for x in a]


def uhi(values):
    n = len(values).bit_length() - 1
    p = [x * x for x in fwht(values)]
    caps = [
        sum(p[t] for t in range(len(p)) if (t & s) == s)
        for s in range(len(p))
    ]
    U = sum(
        p[s] * math.log2(caps[s] / p[s])
        for s in range(len(p))
        if p[s] > 0.0
    )
    H = sum(-x * math.log2(x) for x in p if x > 0.0)
    I = sum(s.bit_count() * p[s] for s in range(len(p)))
    return U, H, I, p


def quantities(values):
    n = len(values).bit_length() - 1
    U, H, I, p = uhi(values)
    G = 0.0
    for i in range(n):
        minus = []
        plus = []
        for x in range(1 << n):
            if x & (1 << i):
                continue
            minus.append(values[x])
            plus.append(values[x | (1 << i)])
        G += U - 0.5 * (uhi(minus)[0] + uhi(plus)[0])

    B = 0.0
    for i in range(n):
        bit = 1 << i
        for s in range(1 << n):
            if s & bit:
                continue
            a, b = p[s], p[s | bit]
            mass = a + b
            if a > 0.0:
                B -= a * math.log2(a / mass)
            if b > 0.0:
                B -= b * math.log2(b / mass)
    M = G - B
    return U, H, I, G, B, M


def balance_lift(values):
    # New high bit y: y=-1 gives -f, y=+1 gives f.
    return [-v for v in values] + list(values)


def tensor(left, right):
    # Disjoint blocks; left index runs fastest.
    return [a * b for b in right for a in left]


def close(a, b, tol=2e-11):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


def main():
    signs_checked = 0
    lift_checks = 0
    tensor_checks = 0
    max_error = 0.0

    samples = []
    for n in range(0, 4):
        N = 1 << n
        for bits in itertools.product((-1, 1), repeat=N):
            q = quantities(bits)
            lifted = balance_lift(bits)
            r = quantities(lifted)
            identities = [
                (r[0], q[0]),       # U invariant
                (r[2], q[2] + 1.0), # I gains one
                (r[3], q[3]),       # G invariant
                (r[4], q[4]),       # B invariant
                (r[5], q[5]),       # M invariant
                (sum(lifted), 0.0), # balanced truth table
            ]
            for a, b in identities:
                max_error = max(max_error, abs(a - b))
                assert close(a, b), (n, bits, q, r, a, b)
            signs_checked += 1
            lift_checks += len(identities)
            if n <= 2:
                samples.append(bits)

    for f in samples:
        qf = quantities(f)
        for g in samples:
            qg = quantities(g)
            qt = quantities(tensor(f, g))
            identities = [(qt[j], qf[j] + qg[j]) for j in range(6)]
            for a, b in identities:
                max_error = max(max_error, abs(a - b))
                assert close(a, b), (f, g, qf, qg, qt, a, b)
            tensor_checks += len(identities)

    print("status=PASS")
    print(f"boolean_signs_checked={signs_checked}")
    print(f"lift_identity_checks={lift_checks}")
    print(f"tensor_identity_checks={tensor_checks}")
    print(f"max_abs_error={max_error:.3e}")
    print("random_seed=None")


if __name__ == "__main__":
    main()
