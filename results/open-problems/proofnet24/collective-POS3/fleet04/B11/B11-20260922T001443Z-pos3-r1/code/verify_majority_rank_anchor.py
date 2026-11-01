#!/usr/bin/env python3
"""Deterministic finite regression for the POS3 width-three majority-rank anchor.

Enumerates distinct transitively closed strict relations compatible with the
natural order on n<=6. Every finite poset admits such a labeling by a linear
extension; this is regression evidence, not a substitute for the proof.
"""
from fractions import Fraction
from itertools import combinations

ONE_THIRD = Fraction(1, 3)
TWO_THIRDS = Fraction(2, 3)
ANCHOR = Fraction(1, 81)
ENDPOINT = Fraction(4, 9)


def closure_from_mask(n, mask):
    rows = [0] * n
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (mask >> bit) & 1:
                rows[i] |= 1 << j
            bit += 1
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if (rows[i] >> j) & 1:
                rows[i] |= rows[j]
    return tuple(rows)


def incomparable(rows, a, b):
    return not ((rows[a] >> b) & 1 or (rows[b] >> a) & 1)


def width(rows):
    n = len(rows)
    for k in range(n, 0, -1):
        for S in combinations(range(n), k):
            if all(incomparable(rows, a, b) for a, b in combinations(S, 2)):
                return k
    return 0


def linear_extensions(rows):
    n = len(rows)
    pred = [0] * n
    for i in range(n):
        for j in range(n):
            if (rows[i] >> j) & 1:
                pred[j] |= 1 << i
    out = []

    def rec(mask, order):
        if len(order) == n:
            out.append(tuple(order))
            return
        for v in range(n):
            if not ((mask >> v) & 1) and pred[v] & ~mask == 0:
                rec(mask | (1 << v), order + [v])

    rec(0, [])
    return out


def maximal(S, rows):
    return [a for a in S if not any(a != z and (rows[a] >> z) & 1 for z in S)]


def minimal(S, rows):
    return [a for a in S if not any(a != z and (rows[z] >> a) & 1 for z in S)]


def main():
    width3_posets = 0
    qualifying = 0
    two_sided = 0
    one_sided = 0
    min_anchor = Fraction(1, 1)
    min_one_sided = Fraction(1, 1)
    min_reduced_product = Fraction(1, 1)

    for n in range(1, 7):
        seen = set()
        pairs = n * (n - 1) // 2
        for mask in range(1 << pairs):
            rows = closure_from_mask(n, mask)
            if rows in seen:
                continue
            seen.add(rows)
            if width(rows) > 3:
                continue
            width3_posets += 1
            exts = linear_extensions(rows)
            E = len(exts)
            positions = []
            for L in exts:
                p = [0] * n
                for i, v in enumerate(L):
                    p[v] = i
                positions.append(p)

            for x in range(n):
                D, U = [], []
                locally_unbalanced = True
                for y in range(n):
                    if y == x:
                        continue
                    pxy = Fraction(sum(p[x] < p[y] for p in positions), E)
                    if ONE_THIRD <= pxy <= TWO_THIRDS:
                        locally_unbalanced = False
                        break
                    if pxy < ONE_THIRD:
                        D.append(y)
                    else:
                        U.append(y)
                if not locally_unbalanced:
                    continue

                qualifying += 1
                canonical_mass = Fraction(sum(p[x] == len(D) for p in positions), E)
                assert canonical_mass > ANCHOR
                min_anchor = min(min_anchor, canonical_mass)

                if not D or not U:
                    one_sided += 1
                    assert canonical_mass > ENDPOINT
                    min_one_sided = min(min_one_sided, canonical_mass)
                    continue

                two_sided += 1
                A = maximal(D, rows)
                B = minimal(U, rows)
                assert len(A) <= 3 and len(B) <= 3
                Ai = [a for a in A if incomparable(rows, a, x)]
                Bi = [b for b in B if incomparable(rows, b, x)]
                assert len(Ai) <= 2 and len(Bi) <= 2

                if Ai and Bi:
                    reduced_product = Fraction(1, 1)
                    for a in Ai:
                        for b in Bi:
                            r = Fraction(sum(p[a] < p[x] < p[b] for p in positions), E)
                            reduced_product *= r
                    assert canonical_mass >= reduced_product
                    min_reduced_product = min(min_reduced_product, reduced_product)

    print("POS3_MAJORITY_RANK_ANCHOR_CHECK_PASS")
    print(f"width_le_3_posets={width3_posets}")
    print(f"qualifying_local_x={qualifying}")
    print(f"two_sided_cases={two_sided}")
    print(f"one_sided_cases={one_sided}")
    print(f"theoretical_anchor={ANCHOR}={float(ANCHOR):.12f}")
    print(f"min_observed_anchor={min_anchor}")
    print(f"theoretical_one_sided={ENDPOINT}={float(ENDPOINT):.12f}")
    print(f"min_observed_one_sided={min_one_sided}")
    print(f"min_observed_reduced_product={min_reduced_product}")


if __name__ == "__main__":
    main()
