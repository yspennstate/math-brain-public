#!/usr/bin/env python3
"""Finite checks for the 2026-09-19 FEI continuation; standard library only.

Fourier arithmetic, distances and erasure tests are exact integers/Fractions.
Entropy inequalities use rational enclosures for logarithms, not float tests.
These checks do not prove the infinite-dimensional theorems or full FEI.
Run: python3 check_recovery.py > checks.json
"""
from __future__ import annotations
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations
from math import comb
import json
import random


def fwht(values: list[int]) -> list[int]:
    a = values.copy()
    n = len(a)
    assert n and not n & (n - 1)
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    return a


def spectrum(values: list[int]) -> dict[int, F]:
    n = len(values)
    p = {s: F(a * a, n * n) for s, a in enumerate(fwht(values)) if a}
    assert sum(p.values()) == F(sum(x*x for x in values), n)
    return p


def influence(p: dict[int, F], mask: int | None = None) -> F:
    return sum((v * (s if mask is None else s & mask).bit_count()
                for s, v in p.items()), F(0))


def ln_unit_interval(t: F, terms: int = 40) -> tuple[F, F]:
    """Certified ln(t), 1 <= t <= 2, by the positive atanh series."""
    assert 1 <= t <= 2
    z = (t - 1) / (t + 1)
    total, power = F(0), z
    for j in range(terms):
        total += 2 * power / (2 * j + 1)
        power *= z * z
    tail = 2 * power / ((2 * terms + 1) * (1 - z*z))
    return total, total + tail


LN2_LO, LN2_HI = ln_unit_interval(F(2))


@lru_cache(maxsize=None)
def log2_bounds(q: F) -> tuple[F, F]:
    assert q >= 1
    exponent = q.numerator.bit_length() - q.denominator.bit_length()
    if F(2) ** exponent > q:
        exponent -= 1
    t = q / (F(2) ** exponent)
    assert 1 <= t < 2
    if t == 1:
        return F(exponent), F(exponent)
    lo, hi = ln_unit_interval(t)
    return exponent + lo / LN2_HI, exponent + hi / LN2_LO


def entropy_bounds(probabilities) -> tuple[F, F]:
    lo, hi = F(0), F(0)
    for p in probabilities:
        if p:
            a, b = log2_bounds(1 / p)
            lo += p * a
            hi += p * b
    return lo, hi


def interval_json(interval: tuple[F, F]) -> dict:
    return {"lower": float(interval[0]), "upper": float(interval[1]),
            "certified_width_upper": float(interval[1] - interval[0])}


def check_small_functions() -> dict:
    count, atoms = 0, 0
    rng = random.Random(19092026)
    for n in range(1, 5):
        size = 1 << n
        truth_tables = (range(1 << size) if n <= 3 else
                        [rng.randrange(1 << size) for _ in range(128)])
        for table in truth_tables:
            values = [1 - 2 * ((table >> x) & 1) for x in range(size)]
            p = spectrum(values)
            inf = influence(p)
            for s, weight in p.items():
                assert entropy_bounds([weight, 1-weight])[1] <= 2 * inf
                if s:
                    coeff = F(abs(fwht(values)[s]), size)
                    for i in range(n):
                        if s >> i & 1:
                            assert coeff <= influence(p, 1 << i)
                atoms += 1
            if len(p) >= 2:
                d = min((s ^ t).bit_count() for s, t in combinations(p, 2))
                rhs_lo = (2 + F(2, d) * log2_bounds(F(len(p)))[0]) * inf
                assert entropy_bounds(p.values())[1] <= rhs_lo
            count += 1
    return {"functions_checked": count, "exhaustive_through_n": 3,
            "seeded_n4_checks": 128, "atom_checks": atoms,
            "entropy_comparison": "certified rational logarithm bounds", "pass": True}


def image(columns: list[int], word: int) -> int:
    answer = 0
    for i, col in enumerate(columns):
        if word >> i & 1:
            answer ^= col
    return answer


def coding_case(columns: list[int], r: int, erased: int) -> dict:
    n = len(columns)
    def h(x: int) -> int:
        return (-1) ** sum(((x >> i) & 1) * ((x >> (i+1)) & 1)
                            for i in range(0, n, 2))
    base = spectrum([h(x) for x in range(1 << n)])
    lifted_values = []
    for w in range(1 << (n+r)):
        x, z = w & ((1 << n)-1), w >> n
        shifted = x
        for i, col in enumerate(columns):
            shifted ^= ((col & z).bit_count() & 1) << i
        lifted_values.append(h(shifted))
    actual = spectrum(lifted_values)
    predicted = {s | image(columns, s) << n: p for s, p in base.items()}
    assert actual == predicted
    code = [s | image(columns, s) << n for s in range(1 << n)]
    distance = min(w.bit_count() for w in code[1:])
    assert distance > erased
    blocks = 0
    for k in range(erased + 1):
        for coords in combinations(range(n+r), k):
            mask = sum(1 << i for i in coords)
            outside = [(s & ~mask) for s in actual]
            assert len(set(outside)) == len(outside)
            blocks += 1
    assert entropy_bounds(actual.values()) == entropy_bounds(base.values())
    extra = sum((p * image(columns, s).bit_count() for s, p in base.items()), F(0))
    assert influence(actual) == influence(base) + extra
    return {"N": n, "r": r, "columns": columns, "minimum_distance": distance,
            "zero_conditional_entropy_blocks_checked": blocks,
            "maximum_erased_block": erased, "H_exact": str(entropy_bounds(actual.values())[0]),
            "I_base": str(influence(base)), "I_lift": str(influence(actual)), "pass": True}


def coding_union_bounds() -> list[dict]:
    answers = []
    for n, k in [(128, 2), (1024, 16), (10000, 100)]:
        # e < 3; use the slightly larger, fully integer-computable redundancy.
        num, den = (3*n) ** (2*k), k ** (2*k)
        r = max(0, num.bit_length() - den.bit_length())
        while (1 << r) * den < num:
            r += 1
        assert r <= n
        volume = sum(comb(n+r, j) for j in range(k+1))
        assert volume < (1 << r)
        answers.append({"N": n, "k": k, "r": r,
                        "exact_volume_less_than_2_power_r": True})
    return answers


def subcube_example() -> dict:
    patterns = ['0**', '10*', '110', '111']
    signs, labels = [1, 1, 1, -1], [1, 2, 4, 1]
    def matches(x: int, pattern: str) -> bool:
        return all(c == '*' or ((x >> i) & 1) == int(c) for i, c in enumerate(pattern))
    owner = [next(j for j, pat in enumerate(patterns) if matches(x, pat)) for x in range(8)]
    pieces = [[signs[j] if owner[x] == j else 0 for x in range(8)] for j in range(4)]
    coeff = [[F(a, 8) for a in fwht(v)] for v in pieces]
    values = [signs[owner[x]] * (-1) ** ((labels[owner[x]] & y).bit_count())
              for y in range(8) for x in range(8)]
    p = spectrum(values)
    delta = [F(owner.count(j), 8) for j in range(4)]
    hj = sum((delta[j] * sum(c != '*' for c in patterns[j]) for j in range(4)), F(0))
    assert entropy_bounds(p.values())[1] <= 2 * hj
    for x in range(8):
        for i in range(3):
            j, ell = owner[x], owner[x ^ (1 << i)]
            if j != ell:
                assert labels[j] != labels[ell] or signs[j] != signs[ell]
    ix = influence(p, 7)
    assert hj <= 2 * ix
    a = [coeff[0][s]**2 + coeff[3][s]**2 for s in range(8)]
    coherent = [(coeff[0][s] + coeff[3][s])**2 for s in range(8)]
    assert len(set(a)) > 1
    lam = max(coherent[s] / a[s] for s in range(8) if a[s])
    return {"patterns": patterns, "signs": signs, "labels": labels,
            "H": interval_json(entropy_bounds(p.values())), "HJ_exact": str(hj),
            "I_selector_exact": str(ix), "repeated_group_nonflat": True,
            "Lambda_exact": str(lam), "pass": True}


def addressing_example(s: int, r: int) -> dict:
    nx, ny = s+r, 1 << s
    values = []
    for w in range(1 << (nx+ny)):
        x, y = w & ((1 << nx)-1), w >> nx
        address, parity_bits = x & ((1 << s)-1), x >> s
        values.append((-1) ** (parity_bits.bit_count() + ((y >> address) & 1)))
    p = spectrum(values)
    assert entropy_bounds(p.values()) == (F(2*s), F(2*s))
    assert influence(p, (1 << nx)-1) == F(s, 2) + r
    return {"address_bits": s, "parity_bits": r, "H_exact": 2*s,
            "I_selector_exact": str(F(s,2)+r), "Lambda_from_formula": 1 << r,
            "pass": True}


def main() -> None:
    columns5 = [x for x in range(32) if x.bit_count() == 3][:8]
    result = {
        "status": "PASS", "scope": "Finite checks only; not a proof of full FEI.",
        "small_boolean_checks": check_small_functions(),
        "systematic_lifts": [coding_case([3,5,6,9],4,2), coding_case(columns5,5,3)],
        "random_code_union_bounds": coding_union_bounds(),
        "nonflat_repeated_label_example": subcube_example(),
        "unbounded_collision_family_samples": [addressing_example(2,r) for r in range(5)],
    }
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
