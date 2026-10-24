#!/usr/bin/env python3
"""Independent checks for B05-FIXED-SHARED-BLOCK-TRANSPORT-v1.

Checks the original k-weight potential, the reviewer-derived logarithmic
potential, and the odd-majority lower-bound family showing that a constant
empty-orbit payment is impossible at this abstraction.
"""

from __future__ import annotations

import itertools
import math
import random

TOL = 3e-12


def q(t):
    if t <= 0:
        return 0.0
    return t * math.log2(1.0 / t) + 2.0 * t / math.log(2.0)


def walsh(table):
    n = len(table).bit_length() - 1
    a = [float(x) for x in table]
    step = 1
    while step < len(a):
        for j in range(0, len(a), 2 * step):
            for r in range(step):
                u, v = a[j + r], a[j + r + step]
                a[j + r], a[j + r + step] = u + v, u - v
        step *= 2
    return [x / len(a) for x in a]


def mask_for(n, variables):
    return sum(1 << (n - 1 - i) for i in variables)


def orbit_energy(hat, n, k, base=()):
    base_mask = mask_for(n, base)
    ans = 0.0
    for pick in range(1 << k):
        m = base_mask
        for i in range(k):
            if (pick >> i) & 1:
                m |= 1 << (n - 1 - i)
        ans += hat[m] ** 2
    return ans


def phi(table):
    n = len(table).bit_length() - 1
    h = walsh(table)
    return sum(q(h[mask_for(n, (i,))] ** 2) for i in range(n))


def lambda_original(table, k):
    n = len(table).bit_length() - 1
    h = walsh(table)
    ans = k * q(orbit_energy(h, n, k))
    return ans + sum(q(orbit_energy(h, n, k, (i,))) for i in range(k, n))


def psi(k, e):
    return 0.0 if k == 0 else q(e) + e * math.log2(k)


def lambda_log(table, k):
    n = len(table).bit_length() - 1
    h = walsh(table)
    ans = psi(k, orbit_energy(h, n, k))
    return ans + sum(q(orbit_energy(h, n, k, (i,))) for i in range(k, n))


def restrict_first(table, bit):
    n = len(table).bit_length() - 1
    block = 1 << (n - 1)
    return tuple(table[bit * block:(bit + 1) * block])


def multiply_shared(f, g, k, uf, vg):
    out = []
    for bits in itertools.product((0, 1), repeat=k + uf + vg):
        x, u, v = bits[:k], bits[k:k + uf], bits[k + uf:]
        fi = sum(b << (k + uf - 1 - j) for j, b in enumerate(x + u))
        gi = sum(b << (k + vg - 1 - j) for j, b in enumerate(x + v))
        out.append(f[fi] * g[gi])
    return tuple(out)


def tables(n):
    for code in range(1 << (1 << n)):
        yield tuple(1 if (code >> j) & 1 else -1 for j in range(1 << n))


def shared_singleton_bound(table, k):
    n = len(table).bit_length() - 1
    h = walsh(table)
    z = [h[mask_for(n, (i,))] ** 2 for i in range(k)]
    s = sum(z)
    lhs = sum(q(t) for t in z)
    rhs = q(s) + (s * math.log2(k) if k else 0.0)
    return lhs, rhs, s


def exhaustive_k2():
    tt = list(tables(3))
    worst = {"orig_product": -1e100, "log_product": -1e100,
             "orig_reveal": -1e100, "log_reveal": -1e100}
    for f in tt:
        child_orig = sum(lambda_original(restrict_first(f, b), 1) for b in (0, 1)) / 2
        child_log = sum(lambda_log(restrict_first(f, b), 1) for b in (0, 1)) / 2
        worst["orig_reveal"] = max(worst["orig_reveal"], child_orig - lambda_original(f, 2))
        worst["log_reveal"] = max(worst["log_reveal"], child_log - lambda_log(f, 2))
        if child_orig > lambda_original(f, 2) + TOL:
            raise AssertionError("original reveal")
        if child_log > lambda_log(f, 2) + TOL:
            raise AssertionError("log reveal")
        for g in tt:
            h = multiply_shared(f, g, 2, 1, 1)
            go = phi(h) - lambda_original(f, 2) - lambda_original(g, 2)
            gl = phi(h) - lambda_log(f, 2) - lambda_log(g, 2)
            worst["orig_product"] = max(worst["orig_product"], go)
            worst["log_product"] = max(worst["log_product"], gl)
            if go > TOL:
                raise AssertionError("original product")
            if gl > TOL:
                raise AssertionError("log product")
    return worst


def random_checks(seed=19419, count=5000):
    rng = random.Random(seed)
    worst = -1e100
    for _ in range(count):
        k = rng.choice((1, 2, 3, 4))
        uf, vg = rng.choice((1, 2)), rng.choice((1, 2))
        f = tuple(rng.choice((-1, 1)) for _ in range(1 << (k + uf)))
        g = tuple(rng.choice((-1, 1)) for _ in range(1 << (k + vg)))
        h = multiply_shared(f, g, k, uf, vg)
        gap = phi(h) - lambda_log(f, k) - lambda_log(g, k)
        worst = max(worst, gap)
        if gap > TOL:
            raise AssertionError(("random log product", k, gap))
        if k >= 1:
            child = sum(lambda_log(restrict_first(f, b), k - 1) for b in (0, 1)) / 2
            if child > lambda_log(f, k) + TOL:
                raise AssertionError(("random log reveal", k, child - lambda_log(f, k)))
    return worst


def majority_data(max_k=1001):
    rows = []
    for k in (3, 5, 9, 17, 33, 65, 129, 257, 513, max_k):
        if k % 2 == 0:
            continue
        r = (k - 1) // 2
        a = math.comb(2 * r, r) / (2 ** (2 * r))
        mass = k * a * a
        p = k * q(a * a)
        rows.append((k, a, mass, p, p / math.log2(k)))
    return rows


def main():
    worst = exhaustive_k2()
    wr = random_checks()
    rows = majority_data()
    print("PASS independent fixed-block review")
    print("exhaustive k=2 factor pairs: 65536")
    for key, value in worst.items():
        print(f"worst {key} gap: {value:.17g}")
    print(f"random logarithmic-potential checks: 5000; worst product gap {wr:.17g}")
    print("odd-majority lower-bound data: k, first_coeff, singleton_mass, Phi, Phi/log2(k)")
    for row in rows:
        print("%d %.15g %.15g %.15g %.15g" % row)
    print("limit prediction for Phi/log2(k): 2/pi = %.15g" % (2 / math.pi))


if __name__ == "__main__":
    main()
