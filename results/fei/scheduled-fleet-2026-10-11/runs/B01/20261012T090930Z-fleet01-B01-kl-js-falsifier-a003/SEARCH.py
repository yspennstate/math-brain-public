#!/usr/bin/env python3
"""Deterministic floating discovery scan; CHECK.py supplies the exact proof."""

import math


def fwht(a):
    a = list(map(float, a))
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def caps(q, n):
    q = q[:]
    for b in range(n):
        for s in range(1 << n):
            if not s >> b & 1:
                q[s] += q[s | 1 << b]
    return q


def h2(p):
    return sum(-q * math.log2(q) for q in (p, 1 - p) if q)


def dber(a, b):
    return sum(p * math.log2(p / q)
               for p, q in (((1 + a) / 2, (1 + b) / 2),
                            ((1 - a) / 2, (1 - b) / 2)) if p)


def score(truth, n):
    a = fwht(truth)
    q = [x * x for x in a]
    pi = caps(q, n)
    influence = sum(s.bit_count() * q[s] for s in range(1 << n))
    kl = js = 0.0
    for i in range(n):
        bit = 1 << i
        for t in range(1 << n):
            if t & bit:
                continue
            u, v = a[t], a[t | bit]
            m = u * u + v * v
            if not m:
                continue
            eta = 2 * u * v / m
            c = sum(a[r] * a[r | bit] for r in range(1 << n)
                    if not r & bit and (r & t) == t)
            x = 2 * c / pi[t]
            kl += m * dber(eta, x)
            js += m * (1 - h2((1 + eta) / 2))
    return (kl - js) / influence if influence else 0.0


def main():
    for n in range(1, 5):
        size = 1 << n
        best = (-1.0, None)
        # Complement symmetry fixes the top truth-table bit to +1.
        for mask in range(1, 1 << (size - 1)):
            truth = [-1 if mask >> x & 1 else 1 for x in range(size)]
            value = score(truth, n)
            if value > best[0]:
                best = (value, mask)
        print(f"n={n} maximum_normalized_defect={best[0]:.15g} mask={best[1]}")
    print("SEARCH_SCOPE=all complement representatives through n=4")
    print("SEARCH_STATUS=FLOATING_DISCOVERY_ONLY; see CHECK.py for exact certificate")


if __name__ == "__main__":
    main()
