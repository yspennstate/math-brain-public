#!/usr/bin/env python3
"""Finite controls for the spectral-sector composition theorem.

The theorem is analytic.  This script exhausts every ordered Boolean endpoint
pair through two variables against every Boolean selector through three
variables, and adds deterministic pseudorandom tests through six total bits.
"""

from fractions import Fraction
from itertools import product
from math import log2, sqrt
import random

TOL = 3e-12
SEED = 0xB12A0565


def fwht(values):
    a = [Fraction(x) for x in values]
    step = 1
    while step < len(a):
        for start in range(0, len(a), 2 * step):
            for j in range(start, start + step):
                x, y = a[j], a[j + step]
                a[j], a[j + step] = x + y, x - y
        step *= 2
    return [x / len(a) for x in a]


def h2(x):
    x = float(x)
    if x <= 0.0 or x >= 1.0:
        return 0.0
    return -x * log2(x) - (1.0 - x) * log2(1.0 - x)


def entropy(values):
    return sum(float(a * a) * log2(1.0 / float(a * a))
               for a in fwht(values) if a)


def influence(values):
    n = len(values).bit_length() - 1
    return sum(Fraction(sum(values[x] != values[x ^ (1 << j)]
                            for x in range(len(values))), len(values))
               for j in range(n))


def compose(u, v, h):
    # z is the low block and x the high block.
    return [v[z] if h[x] == 1 else u[z]
            for x in range(len(h)) for z in range(len(u))]


def stats(u, v, h):
    uh, vh, hh = fwht(u), fwht(v), fwht(h)
    r = Fraction(sum(x == 1 for x in h), len(h))
    q = 1 - r
    if r > Fraction(1, 2):
        # Swap branch labels so the activated branch is the minority.
        u, v = v, u
        uh, vh = vh, uh
        h = tuple(-x for x in h)
        hh = fwht(h)
        r = 1 - r
        q = 1 - r
    mu = 2 * r - 1
    delta = 1 - mu * mu
    beta = Fraction(sum(a != b for a, b in zip(u, v)), len(u))
    s = delta * beta

    pu = [a * a for a in uh]
    pv = [a * a for a in vh]
    w = [q * a + r * b for a, b in zip(pu, pv)]
    hw = sum(float(x) * log2(1.0 / float(x)) for x in w if x)
    hu = entropy(u); hv = entropy(v); hh_ent = entropy(h)
    js = hw - float(q) * hu - float(r) * hv

    rho = sum(a * b for a, b in zip(uh, vh))
    if beta <= Fraction(1, 2):
        disc = max(0.0, 1.0 - float(delta) * (1.0 - float(rho * rho)))
        lam = (1.0 - sqrt(disc)) / 2.0
        assert js <= h2(lam) + TOL
        assert lam <= float(s) + TOL
        assert js <= h2(s) + TOL
    else:
        assert js <= h2(r) + TOL

    assert h2(s) <= float(delta) * h2(beta) + float(beta) * h2(delta) + TOL
    assert h2(delta) <= 4.0 * h2(r) + TOL

    f = compose(u, v, h)
    hf = entropy(f)
    iu, iv, ih, inf = influence(u), influence(v), influence(h), influence(f)
    expected_i = q * iu + r * iv + beta * ih
    assert inf == expected_i

    sector_bound = (float(q) * hu + float(r) * hv + float(beta) * hh_ent
                    + 2.0 * float(delta) * h2(beta)
                    + 8.0 * float(beta) * h2(r))
    assert hf <= sector_bound + TOL

    # Boundary payments used in the analytic corollary.
    assert h2(beta) <= float(iu + iv) + TOL
    assert h2(r) <= float(ih) + TOL
    endpoint_i = q * iu + r * iv
    assert float(delta * (iu + iv)) <= 4.0 * float(endpoint_i) + TOL

    ratios = [e / float(i) for e, i in ((hu, iu), (hv, iv), (hh_ent, ih)) if i]
    c = max(ratios, default=0.0)
    assert hf <= (c + 8.0) * float(inf) + TOL
    return {
        "js_minus_hs": js - h2(s) if beta <= Fraction(1, 2) else None,
        "sector_slack": sector_bound - hf,
        "tax_ratio": (hf - c * float(inf)) / float(inf) if inf else 0.0,
    }


def all_signs(n):
    return list(product((-1, 1), repeat=1 << n))


def main():
    cases = 0
    min_sector_slack = float("inf")
    max_js_minus_hs = -float("inf")
    max_tax_ratio = -float("inf")
    for m in range(3):
        endpoints = all_signs(m)
        for n in range(1, 4):
            selectors = all_signs(n)
            for u in endpoints:
                for v in endpoints:
                    for h in selectors:
                        row = stats(u, v, h)
                        min_sector_slack = min(min_sector_slack, row["sector_slack"])
                        if row["js_minus_hs"] is not None:
                            max_js_minus_hs = max(max_js_minus_hs, row["js_minus_hs"])
                        max_tax_ratio = max(max_tax_ratio, row["tax_ratio"])
                        cases += 1

    rng = random.Random(SEED)
    random_cases = 20000
    for _ in range(random_cases):
        m = rng.randint(1, 4)
        n = rng.randint(1, 4)
        u = tuple(rng.choice((-1, 1)) for _ in range(1 << m))
        v = tuple(rng.choice((-1, 1)) for _ in range(1 << m))
        h = tuple(rng.choice((-1, 1)) for _ in range(1 << n))
        row = stats(u, v, h)
        min_sector_slack = min(min_sector_slack, row["sector_slack"])
        if row["js_minus_hs"] is not None:
            max_js_minus_hs = max(max_js_minus_hs, row["js_minus_hs"])
        max_tax_ratio = max(max_tax_ratio, row["tax_ratio"])

    print(f"seed={SEED}")
    print(f"exhaustive_boolean_triples={cases}")
    print(f"random_boolean_triples={random_cases}")
    print(f"minimum_sector_bound_slack={min_sector_slack:.17g}")
    print(f"maximum_JS_minus_h2_sector={max_js_minus_hs:.17g}")
    print(f"maximum_observed_additive_tax_ratio={max_tax_ratio:.17g}")
    print("analytic_composition_tax=8")
    print("full_FEI=OPEN")
    print("PASS")


if __name__ == "__main__":
    main()
