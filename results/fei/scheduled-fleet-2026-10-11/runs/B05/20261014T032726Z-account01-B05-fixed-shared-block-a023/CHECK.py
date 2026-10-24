#!/usr/bin/env python3
"""Finite verification for the fixed-shared-block orbit-potential theorem.

The proof in REPORT.md is analytic.  This checker exhausts all pairs of
3-variable Boolean factors sharing two variables and checks the product,
full-revelation, and sequential-revelation inequalities.  It also samples
larger shared blocks.
"""

from __future__ import annotations

import itertools
import math
import random

TOL = 2.0e-12


def q(y: float) -> float:
    if y <= 0.0:
        return 0.0
    return y * math.log2(1.0 / y) + 2.0 * y / math.log(2.0)


def all_bits(n: int):
    return itertools.product((0, 1), repeat=n)


def idx(bits) -> int:
    ans = 0
    for b in bits:
        ans = (ans << 1) | b
    return ans


def walsh(table):
    n = (len(table)).bit_length() - 1
    out = []
    scale = 1.0 / (1 << n)
    for mask in range(1 << n):
        s = 0.0
        for z in range(1 << n):
            parity = (mask & z).bit_count() & 1
            s += table[z] * (-1.0 if parity else 1.0)
        out.append(scale * s)
    return out


def phi_from_hat(hat, n):
    return sum(q(hat[1 << (n - 1 - i)] ** 2) for i in range(n))


def orbit_energy(hat, n, shared, base):
    # Masks use the same left-to-right convention as idx().
    base_mask = sum(1 << (n - 1 - i) for i in base)
    total = 0.0
    for pick in range(1 << len(shared)):
        mask = base_mask
        for j, var in enumerate(shared):
            if (pick >> j) & 1:
                mask |= 1 << (n - 1 - var)
        total += hat[mask] ** 2
    return total


def lambda_block(table, k):
    n = (len(table)).bit_length() - 1
    hat = walsh(table)
    shared = tuple(range(k))
    ans = k * q(orbit_energy(hat, n, shared, ()))
    for i in range(k, n):
        ans += q(orbit_energy(hat, n, shared, (i,)))
    return ans


def multiply_shared(f, g, k, uf, vg):
    h = []
    for bits in all_bits(k + uf + vg):
        x = bits[:k]
        u = bits[k:k + uf]
        v = bits[k + uf:]
        h.append(f[idx(x + u)] * g[idx(x + v)])
    return tuple(h)


def restrict_var(table, var, value):
    n = (len(table)).bit_length() - 1
    out = []
    for child in all_bits(n - 1):
        bits = list(child)
        bits.insert(var, value)
        out.append(table[idx(bits)])
    return tuple(out)


def full_reveal_phi(table, k):
    vals = []
    work = [table]
    # Always reveal current coordinate 0; remaining shared coordinates shift.
    for _ in range(k):
        work = [restrict_var(t, 0, b) for t in work for b in (0, 1)]
    for t in work:
        n = (len(t)).bit_length() - 1
        vals.append(phi_from_hat(walsh(t), n))
    return sum(vals) / len(vals)


def truth_tables(n):
    for code in range(1 << (1 << n)):
        yield tuple(1 if (code >> j) & 1 else -1 for j in range(1 << n))


def check_exhaustive_two_shared():
    tabs = list(truth_tables(3))  # (x,y,u) or (x,y,v)
    hats = [walsh(t) for t in tabs]
    lambdas = [lambda_block(t, 2) for t in tabs]
    worst_product = (-1e9, None)
    for a, f in enumerate(tabs):
        # Revelation laws depend on one factor only.
        reveal_gap = full_reveal_phi(f, 2) - lambdas[a]
        if reveal_gap > TOL:
            raise AssertionError(("full reveal", a, reveal_gap))
        seq = 0.5 * (lambda_block(restrict_var(f, 0, 0), 1)
                     + lambda_block(restrict_var(f, 0, 1), 1))
        seq_gap = seq - lambdas[a]
        if seq_gap > TOL:
            raise AssertionError(("sequential reveal", a, seq_gap))
        for b, g in enumerate(tabs):
            h = multiply_shared(f, g, 2, 1, 1)
            product_gap = phi_from_hat(walsh(h), 4) - lambdas[a] - lambdas[b]
            if product_gap > worst_product[0]:
                worst_product = (product_gap, (a, b))
            if product_gap > TOL:
                raise AssertionError(("product", a, b, product_gap))
    return len(tabs) ** 2, worst_product


def check_random(seed=20261014, trials=6000):
    rng = random.Random(seed)
    worst = -1e9
    by_k = {1: 0, 2: 0, 3: 0}
    for _ in range(trials):
        k = rng.choice((1, 2, 3))
        nf = k + rng.choice((1, 2))
        ng = k + rng.choice((1, 2))
        f = tuple(rng.choice((-1, 1)) for _ in range(1 << nf))
        g = tuple(rng.choice((-1, 1)) for _ in range(1 << ng))
        lf = lambda_block(f, k)
        lg = lambda_block(g, k)
        h = multiply_shared(f, g, k, nf - k, ng - k)
        gap = phi_from_hat(walsh(h), nf + ng - k) - lf - lg
        worst = max(worst, gap)
        if gap > TOL:
            raise AssertionError(("random product", k, gap))
        if full_reveal_phi(f, k) - lf > TOL:
            raise AssertionError(("random full reveal", k))
        if k >= 2:
            child = 0.5 * (lambda_block(restrict_var(f, 0, 0), k - 1)
                           + lambda_block(restrict_var(f, 0, 1), k - 1))
            if child - lf > TOL:
                raise AssertionError(("random sequential reveal", k, child - lf))
        by_k[k] += 1
    return by_k, worst


def main():
    exhaustive, worst2 = check_exhaustive_two_shared()
    by_k, worst_random = check_random()
    print("PASS fixed-shared-block orbit-potential checks")
    print(f"exhaustive k=2 factor pairs: {exhaustive}")
    print(f"worst exhaustive product gap Phi-Lambda_f-Lambda_g: {worst2[0]:.17g}")
    print(f"worst pair codes: {worst2[1]}")
    print(f"random trials by k: {by_k}")
    print(f"worst random product gap: {worst_random:.17g}")
    print("scope: finite numerical validation only; analytic proof is in REPORT.md")


if __name__ == "__main__":
    main()
