#!/usr/bin/env python3
"""Targeted exact sanity checks for B15 valuation-tail majorization.

This is not an exhaustive FEI search.  It verifies the rational tail inequalities
on four named Boolean examples and 64 deterministic six-variable truth tables.
The analytic theorem is proved in REPORT.md and does not rely on this script.
"""
from collections import defaultdict
from fractions import Fraction
import json
import random


def fwht(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                x, y = a[j], a[j+h]
                a[j], a[j+h] = x+y, x-y
        h *= 2
    return a


def v2(z):
    z = abs(int(z))
    assert z
    return (z & -z).bit_length() - 1


def analyze(vals):
    N = len(vals)
    n = N.bit_length() - 1
    assert 1 << n == N
    W = fwht(vals)
    packets = defaultdict(list)
    for s, w in enumerate(W):
        if w:
            packets[abs(w)].append((s, 1 if w > 0 else -1))

    rows = []
    den = N*N
    for mag, entries in sorted(packets.items()):
        eps = [0]*N
        for s, sign in entries:
            eps[s] = sign
        V = fwht(eps)
        r = min(v2(x) for x in V if x)
        p = Fraction(len(entries)*mag*mag, den)
        rows.append((mag, len(entries), r, p))
    assert sum((r[3] for r in rows), Fraction()) == 1

    j = []
    for i in range(n):
        num = sum(w*w for s, w in enumerate(W) if (s >> i) & 1)
        j.append(Fraction(num, den))
    q = sorted((min(x, 1-x) for x in j), reverse=True)

    tails = []
    for m in range(1, n+1):
        lhs = sum((p * max(0, r-m+1) for _, _, r, p in rows), Fraction())
        rhs = 2 * sum(q[m-1:], Fraction())
        assert lhs <= rhs, (m, lhs, rhs, rows, q)
        # The packet-mass tail follows because (r-m+1)_+ >= 1_{r>=m}.
        mass_tail = sum((p for _, _, r, p in rows if r >= m), Fraction())
        assert mass_tail <= rhs
        tails.append({
            "m": m,
            "integrated_tail": str(lhs),
            "packet_mass_tail": str(mass_tail),
            "influence_tail_budget": str(rhs),
        })
    return {
        "n": n,
        "packets": [
            {"walsh_magnitude": mag, "count": count, "r": r, "p": str(p)}
            for mag, count, r, p in rows
        ],
        "folded_marginals_desc": [str(x) for x in q],
        "tails": tails,
    }


def one_point(n):
    return [-1] + [1]*((1 << n)-1)


def majority5():
    return [1 if x.bit_count() >= 3 else -1 for x in range(32)]


def fstar5():
    vals = []
    for z in range(32):
        x1, x2, x3 = (z >> 0) & 1, (z >> 1) & 1, (z >> 2) & 1
        y1, y2 = (z >> 3) & 1, (z >> 4) & 1
        hit = (y1 == (x1 & x2)) and (y2 == (x1 & x3))
        vals.append(1 - 2*int(hit))
    return vals


def address2():
    vals = []
    for z in range(64):
        addr = z & 3
        data = (z >> 2) & 15
        vals.append(1 if ((data >> addr) & 1) == 0 else -1)
    return vals


def main():
    out = {"named": {}, "seeded_random_n6": []}
    named = {
        "one_point_n6": one_point(6),
        "majority_n5": majority5(),
        "five_variable_lattice_counterexample": fstar5(),
        "addressing_k2_n6": address2(),
    }
    for name, vals in named.items():
        out["named"][name] = analyze(vals)

    rng = random.Random(20260921)
    max_r = 0
    for t in range(64):
        vals = [1 if rng.getrandbits(1) else -1 for _ in range(64)]
        rec = analyze(vals)
        max_r = max(max_r, max(p["r"] for p in rec["packets"]))
        out["seeded_random_n6"].append({
            "case": t,
            "max_r": max(p["r"] for p in rec["packets"]),
            "tail_checks": len(rec["tails"]),
        })
    out["summary"] = {
        "named_examples": len(named),
        "seeded_random_examples": 64,
        "all_tail_checks_passed": True,
        "largest_packet_r_seen_in_seeded_random": max_r,
        "scope": "finite sanity check only; theorem is analytic",
    }
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
