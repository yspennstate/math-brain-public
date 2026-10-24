#!/usr/bin/env python3
"""Exact finite audit for the three-parallel-affine-coset local theorem."""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations
import json

getcontext().prec = 70


def span(gens):
    out = {0}
    for g in gens:
        out |= {x ^ g for x in tuple(out)}
    return frozenset(out)


def subspaces(n):
    spaces = {frozenset({0})}
    for x in range(1, 1 << n):
        for v in tuple(spaces):
            if x not in v:
                spaces.add(span(tuple(v) + (x,)))
    return spaces


def cosets(n, v):
    unseen = set(range(1 << n))
    out = []
    while unseen:
        a = min(unseen)
        c = frozenset(a ^ x for x in v)
        unseen -= c
        out.append((a, c))
    return out


def fwht(vals):
    a = [Fraction(x) for x in vals]
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2 * h):
            for j in range(i, i + h):
                x, y = a[j], a[j + h]
                a[j], a[j + h] = x + y, x - y
        h *= 2
    return [x / len(a) for x in a]


def phi(q):
    if q == 0:
        return Decimal(0)
    x = Decimal(q.numerator) / Decimal(q.denominator)
    return x * (Decimal(1) / x).ln()


def eraw(vals):
    return sum(phi(c * c) for c in fwht(vals))


def influence(vals):
    n = len(vals).bit_length() - 1
    ans = Fraction(0)
    for bit in range(n):
        ans += sum((Fraction(vals[x]) - Fraction(vals[x ^ (1 << bit)])) ** 2
                   for x in range(len(vals))) / (4 * len(vals))
    return ans


def rank_from_size(v):
    return len(v).bit_length() - 1


def local_objects(n, support):
    s = [int(z in support) for z in range(1 << n)]
    d, a0, f = [], [], []
    for selector in (0, 1):
        x = 1 if selector == 0 else -1
        for z in range(1 << n):
            dv = selector * s[z]
            d.append(dv)
            a0.append(x + dv)
            f.append(x + 2 * dv)
    return s, d, eraw(f) - eraw(a0) - eraw(d)


def main():
    total = spectrum_checks = influence_checks = local_checks = 0
    largest_ratio = Decimal(0)
    largest_case = None
    ln2 = Decimal(2).ln()
    for n in range(2, 5):
        for v in subspaces(n):
            cs = cosets(n, v)
            if len(cs) < 3:
                continue
            k = n - rank_from_size(v)
            y = Fraction(len(v), 1 << n)
            for triple in combinations(cs, 3):
                reps = [q[0] for q in triple]
                pieces = [q[1] for q in triple]
                support = frozenset().union(*pieces)
                u = span(tuple(v) + (reps[1] ^ reps[0], reps[2] ^ reps[0]))
                if len(u) != 4 * len(v):
                    raise AssertionError((n, v, reps, "affine-plane rank"))
                m_v = sum((1 << i) not in v for i in range(n))
                m_u = sum((1 << i) not in u for i in range(n))
                s, d, omega = local_objects(n, support)
                coeffs = fwht(s)
                mags = {}
                for c in coeffs:
                    mags[abs(c)] = mags.get(abs(c), 0) + 1
                expected = {Fraction(0): (1 << n) - 1 // (4 * y)}
                # Avoid fragile dictionary construction: check the two nonzero shells directly.
                if sum(abs(c) == 3 * y for c in coeffs) != 1 // (4 * y):
                    raise AssertionError((n, v, reps, "large spectral shell"))
                if sum(abs(c) == y for c in coeffs) != 3 // (4 * y):
                    raise AssertionError((n, v, reps, "small spectral shell"))
                if sum(c != 0 for c in coeffs) != 1 // y:
                    raise AssertionError((n, v, reps, "spectral support"))
                spectrum_checks += 1
                i_s = influence(s)
                i_d = influence(d)
                expected_is = y * Fraction(m_v + 2 * m_u, 2)
                expected_id = expected_is / 2 + 3 * y / 4
                if i_s != expected_is or i_d != expected_id:
                    raise AssertionError((n, v, reps, i_s, expected_is, i_d, expected_id))
                influence_checks += 1
                rhs = 8 * ln2 * (Decimal(i_d.numerator) / Decimal(i_d.denominator))
                if omega > rhs + Decimal("1e-60"):
                    raise AssertionError((n, v, reps, omega, rhs))
                local_checks += 1
                if i_d:
                    ratio = omega / (Decimal(i_d.numerator) / Decimal(i_d.denominator))
                    if ratio > largest_ratio:
                        largest_ratio = ratio
                        largest_case = {"n": n, "V": sorted(v), "representatives": reps}
                total += 1

    asymptotic = []
    for k in range(2, 31):
        y = Decimal(2) ** (-k)
        eraw_formula = 6 * k * y * ln2 - Decimal(9) * y * Decimal(3).ln() / 2
        id_lower = y * Decimal(3 * k - 1) / 4
        asymptotic.append({"k": k, "eraw_over_Id_lower": str(eraw_formula / id_lower)})
    out = {
        "status": "PASS",
        "parallel_triples_checked": total,
        "ambient_dimensions": [2, 3, 4],
        "spectrum_checks": spectrum_checks,
        "physical_influence_checks": influence_checks,
        "local_8ln2_checks": local_checks,
        "largest_observed_Omega_over_Id": str(+largest_ratio),
        "largest_case": largest_case,
        "coordinate_minimal_eraw_ratio_k30": asymptotic[-1],
        "limit": "8 ln(2)",
        "randomness": "none",
        "scope": "Finite corroboration only; the all-dimensional result is proved analytically in PARALLEL_TRIPLE_THEOREM.tex."
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
