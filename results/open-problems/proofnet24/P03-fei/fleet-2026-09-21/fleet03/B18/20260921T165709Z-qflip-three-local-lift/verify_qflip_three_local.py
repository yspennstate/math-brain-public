#!/usr/bin/env python3
from fractions import Fraction
from itertools import product
import json


def dot(x, y):
    return (x & y).bit_count() & 1


def rank_vecs(vecs):
    basis = {}
    for v in vecs:
        x = v
        while x:
            h = x.bit_length() - 1
            if h in basis:
                x ^= basis[h]
            else:
                basis[h] = x
                break
    return len(basis)


def influence(vals, u):
    N = len(vals)
    return Fraction(sum(vals[x] != vals[x ^ u] for x in range(N)), N)


def corr(vals, u):
    N = len(vals)
    return Fraction(sum(vals[x] * vals[x ^ u] for x in range(N)), N)


def tau(vals, u, v, w):
    N = len(vals)
    return Fraction(sum(vals[x] * vals[x ^ u] * vals[x ^ v] * vals[x ^ w]
                        for x in range(N)), N)


def spectral_law(vals, dirs):
    N = len(vals)
    out = {a: Fraction(0) for a in product((0, 1), repeat=3)}
    for xi in range(N):
        walsh = sum(vals[x] * (-1 if dot(xi, x) else 1) for x in range(N))
        wt = Fraction(walsh * walsh, N * N)
        key = tuple(dot(xi, u) for u in dirs)
        out[key] += wt
    return out


def sensitivity_law(vals, dirs):
    N = len(vals)
    out = {a: Fraction(0) for a in product((0, 1), repeat=3)}
    for x in range(N):
        key = tuple(int(vals[x] != vals[x ^ u]) for u in dirs)
        out[key] += Fraction(1, N)
    return out


summary = {}
global_max = Fraction(0)
for r in range(4):
    N = 1 << r
    triples = [t for t in product(range(N), repeat=3) if rank_vecs(t) == r]
    cases = equalities = 0
    max_ratio = Fraction(0)
    for vals in product((-1, 1), repeat=N):
        for dirs in triples:
            cases += 1
            u, v, w = dirs
            mu = spectral_law(vals, dirs)
            nu = sensitivity_law(vals, dirs)

            for i in range(3):
                assert sum(p for a, p in mu.items() if a[i]) == sum(p for a, p in nu.items() if a[i])
            for i, j in ((0, 1), (0, 2), (1, 2)):
                assert sum(p for a, p in mu.items() if a[i] and a[j]) == sum(p for a, p in nu.items() if a[i] and a[j])

            q = mu[(1, 1, 1)]
            s = nu[(1, 1, 1)]
            d = (tau(vals, u, v, w) - corr(vals, u ^ v ^ w)) / 8
            assert q - s == d

            for a in product((0, 1), repeat=3):
                expected = d if (sum(a) & 1) else -d
                assert mu[a] - nu[a] == expected

            tv = sum(abs(mu[a] - nu[a]) for a in mu) / 2
            assert tv == 4 * abs(d)

            I = sum((influence(vals, u), influence(vals, v), influence(vals, w)), Fraction(0))
            assert abs(d) <= I / 6
            if I:
                ratio = abs(d) / I
                max_ratio = max(max_ratio, ratio)
                global_max = max(global_max, ratio)
                if ratio == Fraction(1, 6):
                    equalities += 1

    summary[str(r)] = {
        "truth_tables": 1 << N,
        "ordered_direction_triples_spanning_rank": len(triples),
        "cases": cases,
        "equality_cases": equalities,
        "max_abs_d_over_sum_influences": str(max_ratio),
    }

out = {
    "all_ok": True,
    "theorem": "arbitrary F2 flip directions: pair-law equality, alternating cubic defect, TV=4|d|, |d|<=sum Inf/6",
    "total_exact_cases": sum(v["cases"] for v in summary.values()),
    "global_max_abs_d_over_sum_influences": str(global_max),
    "sharp_constant": "1/6",
    "ranks": summary,
}
print(json.dumps(out, indent=2, sort_keys=True))
