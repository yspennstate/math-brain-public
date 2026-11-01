#!/usr/bin/env python3
"""Audit the cylinder-safe event-local telescope for parallel triples."""

from decimal import Decimal, getcontext
from fractions import Fraction
from itertools import combinations, permutations
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
        out.append(c)
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
    return sum(
        sum((Fraction(vals[x]) - Fraction(vals[x ^ (1 << bit)])) ** 2
            for x in range(len(vals))) / (4 * len(vals))
        for bit in range(n)
    )


def omega(source):
    d, a0, f = [], [], []
    for selector in (0, 1):
        x = 1 if selector == 0 else -1
        for sv in source:
            dv = selector * sv
            d.append(dv)
            a0.append(x + dv)
            f.append(x + 2 * dv)
    return eraw(f) - eraw(a0) - eraw(d)


def restrict_bit(vals, bit, value):
    n = len(vals).bit_length() - 1
    out = []
    for y in range(1 << (n - 1)):
        low = y & ((1 << bit) - 1)
        high = y >> bit
        x = low | (value << bit) | (high << (bit + 1))
        out.append(vals[x])
    return out


def telescope(source, order):
    """Return weighted sum of Gamma over a complete fixed-order tree."""
    frontier = [(Decimal(1), source, list(range(len(source).bit_length() - 1)))]
    total = Decimal(0)
    for original_bit in order:
        nxt = []
        for weight, vals, labels in frontier:
            bit = labels.index(original_bit)
            left = restrict_bit(vals, bit, 0)
            right = restrict_bit(vals, bit, 1)
            gamma = omega(vals) - (omega(left) + omega(right)) / 2
            total += weight * gamma
            new_labels = labels[:bit] + labels[bit + 1:]
            nxt.append((weight / 2, left, new_labels))
            nxt.append((weight / 2, right, new_labels))
        frontier = nxt
    terminal = sum(weight * omega(vals) for weight, vals, _ in frontier)
    return total, terminal


def main():
    ln2 = Decimal(2).ln()
    finite_certificates = {
        2: 2 ** 96 * 3 ** 9 > 5 ** 25,
        3: 2 ** 416 * 3 ** 45 * 5 ** 100 > 13 ** 169,
        4: 2 ** 1536 * 3 ** 117 * 13 ** 676 > 29 ** 841,
    }
    if not all(finite_certificates.values()):
        raise AssertionError(finite_certificates)
    total = bound_checks = telescope_checks = 0
    max_ratio = Decimal("-Infinity")
    max_case = None
    for n in range(2, 5):
        for v in subspaces(n):
            cs = cosets(n, v)
            if len(cs) < 3:
                continue
            for triple in combinations(cs, 3):
                support = frozenset().union(*triple)
                s = [int(z in support) for z in range(1 << n)]
                p = Fraction(len(support), 1 << n)
                om = omega(s)
                isrc = influence(s)
                # Selector splice influence.
                idv = isrc / 2 + p / 4
                compensated = om + 2 * (
                    Decimal(p.numerator) / Decimal(p.denominator)
                ) * ln2
                rhs = 8 * ln2 * (
                    Decimal(idv.numerator) / Decimal(idv.denominator)
                )
                if compensated > rhs + Decimal("1e-60"):
                    raise AssertionError((n, v, support, compensated, rhs))
                bound_checks += 1
                ratio = compensated / (
                    Decimal(idv.numerator) / Decimal(idv.denominator)
                )
                if ratio > max_ratio:
                    max_ratio = ratio
                    max_case = {"n": n, "V": sorted(v), "support": sorted(support)}
                order = tuple(range(n))
                charge, terminal = telescope(s, order)
                if abs(charge - compensated) > Decimal("1e-60"):
                    raise AssertionError(("telescope", n, order, charge, compensated))
                expected_terminal = -2 * (
                    Decimal(p.numerator) / Decimal(p.denominator)
                ) * ln2
                if abs(terminal - expected_terminal) > Decimal("1e-60"):
                    raise AssertionError(("terminal", n, order, terminal, expected_terminal))
                telescope_checks += 1
                total += 1

    # Dummy-cylinder invariance at the exact base from the preceding no-go.
    base = [int(z in {0, 1, 2}) for z in range(8)]
    base_p = Decimal(3) / Decimal(8)
    base_compensated = omega(base) + 2 * base_p * ln2
    for order in permutations(range(3)):
        charge, terminal = telescope(base, order)
        if abs(charge - base_compensated) > Decimal("1e-60"):
            raise AssertionError(("base permutation", order))
        telescope_checks += 1
    lifted = base * 2
    left = restrict_bit(lifted, 3, 0)
    right = restrict_bit(lifted, 3, 1)
    dummy_gamma = omega(lifted) - (omega(left) + omega(right)) / 2
    if dummy_gamma != 0:
        raise AssertionError(("dummy Gamma", dummy_gamma))

    out = {
        "status": "PASS",
        "parallel_triples_checked": total,
        "compensated_8ln2_bounds": bound_checks,
        "complete_ordered_tree_telescopes": telescope_checks,
        "ambient_dimensions": [2, 3, 4],
        "largest_compensated_ratio": str(+max_ratio),
        "largest_case": max_case,
        "dummy_cylinder_Gamma": str(dummy_gamma),
        "small_k_integer_certificates": {
            "k=2": "2^96 3^9 > 5^25",
            "k=3": "2^416 3^45 5^100 > 13^169",
            "k=4": "2^1536 3^117 13^676 > 29^841"
        },
        "terminal_identity": "average leaf Omega = -2 p ln(2)",
        "randomness": "none",
        "scope": "Finite corroboration; the theorem is analytic in EVENT_LOCAL_TELESCOPE.tex."
    }
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
