#!/usr/bin/env python3
"""Deterministic regression for the B04 all-bias closure theorem.

This is supporting computation only.  The report contains the proof.
"""

from __future__ import annotations

import itertools
import math
import random


def h2(x: float) -> float:
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * math.log2(x) - (1.0 - x) * math.log2(1.0 - x)


def product_prob(x, p):
    ans = 1.0
    for xi, pi in zip(x, p):
        ans *= pi if xi else 1.0 - pi
    return ans


def output_prob(table, p):
    return sum(product_prob(x, p) for x, f in table.items() if f == 1)


def disagreement(table, p, i):
    n = len(p)
    total = 0.0
    for y in itertools.product((0, 1), repeat=n - 1):
        x0 = list(y[:i]) + [0] + list(y[i:])
        x1 = list(y[:i]) + [1] + list(y[i:])
        if table[tuple(x0)] != table[tuple(x1)]:
            total += product_prob(y, p[:i] + p[i + 1 :])
    return total


def coefficients(table, p):
    n = len(p)
    out = []
    for s in itertools.product((0, 1), repeat=n):
        a = 0.0
        for x, f in table.items():
            phi = 1.0
            for i in range(n):
                if s[i]:
                    if p[i] in (0.0, 1.0):
                        phi = 0.0
                        break
                    phi *= (x[i] - p[i]) / math.sqrt(p[i] * (1.0 - p[i]))
            a += product_prob(x, p) * f * phi
        out.append(a)
    return out


def spectral_entropy(table, p):
    ans = 0.0
    for a in coefficients(table, p):
        w = a * a
        if w > 0.0:
            ans -= w * math.log2(w)
    return ans


def defect(table, p):
    # Gamma=0: A(p)=h2(4p(1-p)).
    price = sum(
        disagreement(table, p, i) * h2(4.0 * p[i] * (1.0 - p[i]))
        for i in range(len(p))
    )
    return price - spectral_entropy(table, p)


def restrict(table, fixed):
    n = len(next(iter(table)))
    free = [i for i in range(n) if i not in fixed]
    out = {}
    for y in itertools.product((0, 1), repeat=len(free)):
        x = [None] * n
        for i, v in fixed.items():
            x[i] = v
        for i, v in zip(free, y):
            x[i] = v
        out[y] = table[tuple(x)]
    return out, free


def eta(r):
    return h2(min(4.0 * r, 0.5))


def fk(k, tau):
    tau = min(1.0, tau)
    if tau <= 1.0 - 2.0 ** (-k):
        return h2(tau) + tau * math.log2(2**k - 1)
    return float(k)


def modulus_rhs(p, q):
    k = len(p)
    delta = sum(abs(x - y) for x, y in zip(p, q))
    theta = sum(
        abs(math.asin(math.sqrt(x)) - math.asin(math.sqrt(y)))
        for x, y in zip(p, q)
    )
    return (k - 1) * delta + sum(eta(abs(x - y)) for x, y in zip(p, q)) + fk(k, min(1.0, 2.0 * theta))


def main():
    rng = random.Random(20260922)
    gates = 0
    physical = 0
    faces = 0
    modulus = 0

    for n in (1, 2, 3):
        vertices = list(itertools.product((0, 1), repeat=n))
        for mask in range(1 << len(vertices)):
            table = {x: (1 if (mask >> j) & 1 else -1) for j, x in enumerate(vertices)}
            gates += 1

            p = [0.13 + 0.71 * rng.random() for _ in range(n)]
            coeff = coefficients(table, p)
            for i in range(n):
                it = 0.0
                for s, a in zip(itertools.product((0, 1), repeat=n), coeff):
                    if s[i]:
                        it += a * a
                rhs = 4.0 * p[i] * (1.0 - p[i]) * disagreement(table, p, i)
                assert abs(it - rhs) < 2e-10, (n, mask, i, it, rhs)
                physical += 1

            for i in range(n):
                for value in (0, 1):
                    face_p = list(p)
                    face_p[i] = float(value)
                    small, free = restrict(table, {i: value})
                    small_p = [face_p[j] for j in free]
                    assert abs(defect(table, face_p) - defect(small, small_p)) < 3e-10
                    faces += 1

            q = [min(1.0, max(0.0, x + rng.uniform(-0.025, 0.025))) for x in p]
            lhs = abs(defect(table, p) - defect(table, q))
            rhs = modulus_rhs(p, q)
            assert lhs <= rhs + 1e-9, (n, mask, lhs, rhs)
            modulus += 1

    # Explicit zero-variance constant faces.
    for n in range(0, 5):
        table = {x: 1 for x in itertools.product((0, 1), repeat=n)}
        p = [0.0 if i % 2 == 0 else 1.0 for i in range(n)]
        assert abs(defect(table, p)) < 1e-12

    print(f"gates={gates}")
    print(f"physical_identity_checks={physical}")
    print(f"face_contraction_checks={faces}")
    print(f"modulus_checks={modulus}")
    print("PASS FEI-B04-ALLBIAS-CLOSURE-v1")


if __name__ == "__main__":
    main()
