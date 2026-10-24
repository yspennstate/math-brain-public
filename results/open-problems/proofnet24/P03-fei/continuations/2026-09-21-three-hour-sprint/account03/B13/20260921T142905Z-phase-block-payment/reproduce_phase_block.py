#!/usr/bin/env python3
import math


def fwht(vals):
    a = [float(x) for x in vals]
    n = len(a)
    h = 1
    while h < n:
        for i in range(0, n, 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / n for x in a]


def spectral(vals):
    return [x * x for x in fwht(vals)]


def entropy(p):
    return -sum(x * math.log2(x) for x in p if x > 0.0)


def upper_masses(p, k):
    u = list(p)
    for bit in range(k):
        for A in range(1 << k):
            if ((A >> bit) & 1) == 0:
                u[A] += u[A | (1 << bit)]
    return u


def bcan(p, k):
    u = upper_masses(p, k)
    return sum(x * math.log2(y / x) for x, y in zip(p, u) if x > 0.0)


def js2(p, q):
    m = [(x + y) / 2 for x, y in zip(p, q)]
    return entropy(m) - (entropy(p) + entropy(q)) / 2


def bent_vals(k):
    assert k % 2 == 0
    out = []
    for x in range(1 << k):
        bit = 0
        for j in range(0, k, 2):
            bit ^= ((x >> j) & 1) & ((x >> (j + 1)) & 1)
        out.append(-1.0 if bit else 1.0)
    return out


def phase_stats(k):
    h = bent_vals(k)
    hp = list(h)
    hp[0] *= -1.0
    ah = fwht(h)
    bh = fwht(hp)
    a = [(x + y) / 2 for x, y in zip(ah, bh)]
    b = [(x - y) / 2 for x, y in zip(ah, bh)]
    p = [x * x for x in a]
    q = [x * x + y * y for x, y in zip(a, b)]
    phi = sum(x * math.log2(y / x) for x, y in zip(p, q) if x > 0.0)
    J = sum(x * x for x in b)
    M = js2(spectral(h), spectral(hp))
    return phi / J, M / J, (phi + M) / J, J


def boolean_pair_counterexample():
    # Truth-table order x=0,...,7.  Both tables are Boolean on three bits.
    h0 = [1, -1, -1, -1, 1, 1, 1, -1]
    h1 = [1, -1, -1, 1, -1, 1, 1, -1]
    p = spectral(h0)
    q = spectral(h1)
    m = [(x + y) / 2 for x, y in zip(p, q)]
    gap = bcan(m, 3) - (bcan(p, 3) + bcan(q, 3)) / 2
    j = js2(p, q)
    return p, q, m, bcan(p, 3), bcan(q, 3), bcan(m, 3), gap, j, gap - j


print("phase_block_bent_flip")
for k in range(2, 14, 2):
    pr, mr, jr, J = phase_stats(k)
    print(k, "Phi/J=%.15f M/J=%.15f joint/J=%.15f J=%.15g" % (pr, mr, jr, J))
print("limits", 1 / math.log(2), 2 / math.log(2), 3 / math.log(2))

print("boolean_pair_mixing_counterexample")
p, q, m, bp, bq, bm, gap, j, d = boolean_pair_counterexample()
print("p", p)
print("q", q)
print("m", m)
print("Bcan(p)", bp, "Bcan(q)", bq, "Bcan(m)", bm)
print("gap", gap, "JS", j, "gap-JS", d)
