#!/usr/bin/env python3
"""Exact finite verifier for HARD8-03 nullity-three profile normal forms.

This checks the project profile inequality obstruction at real nullity three
through rank 8. It uses only integer arithmetic, finite enumeration, and
bit masks. No floating point, randomness, external solver, or timeout
inference is used.
"""

from itertools import product, combinations

SIGNS = (-1, 0, 1)
PAIR_TYPES = tuple((x, y) for x in SIGNS for y in SIGNS)


def compositions(total, parts, prefix=()):
    if parts == 1:
        yield prefix + (total,)
        return
    for x in range(total + 1):
        yield from compositions(total - x, parts - 1, prefix + (x,))


def collinear(v, w):
    ratio = None
    for x, y in zip(v, w):
        if x == 0 and y == 0:
            continue
        if x == 0 or y == 0:
            return False
        if ratio is None:
            ratio = (x, y)
        else:
            a, b = ratio
            if x * b != y * a:
                return False
    return True


def relation_data(a, b, c):
    r = len(a)
    out = []
    for la, lb, lc in product(SIGNS, repeat=3):
        if la == lb == lc == 0:
            continue
        comb = [la * a[i] + lb * b[i] + lc * c[i] for i in range(r)]
        if not all(-1 <= x <= 1 for x in comb):
            continue
        coeff = tuple([-x for x in comb] + [la, lb, lc])
        support = negmask = posmask = 0
        for i, x in enumerate(coeff):
            if x:
                support |= 1 << i
                if x == -1:
                    negmask |= 1 << i
                else:
                    posmask |= 1 << i
        out.append((coeff, support, negmask, posmask))
    return out


def profile_violation(a, b, c, k):
    """True iff every maximal dissociated set has heavy rank at least two."""
    r = len(a)
    n = r + 3
    basis = [tuple(1 if i == j else 0 for i in range(r)) for j in range(r)]
    cfg = basis + [a, b, c]
    rels = relation_data(a, b, c)
    supports = [z[1] for z in rels]

    for mask in range(1 << n):
        if mask.bit_count() < r:
            continue
        if any((supp & ~mask) == 0 for supp in supports):
            continue

        maximal = True
        for i in range(n):
            if (mask >> i) & 1:
                continue
            mm = mask | (1 << i)
            if not any((supp & ~mm) == 0 for supp in supports):
                maximal = False
                break
        if not maximal:
            continue

        heavy = []
        for v in range(n):
            if (mask >> v) & 1:
                continue
            target_mask = mask | (1 << v)
            best_width = 10**9
            for coeff, supp, negmask, posmask in rels:
                if supp & ~target_mask:
                    continue
                if coeff[v] == -1:
                    width = (negmask & ~(1 << v)).bit_count()
                    if width < best_width:
                        best_width = width
                elif coeff[v] == 1:
                    width = (posmask & ~(1 << v)).bit_count()
                    if width < best_width:
                        best_width = width
            if best_width > k:
                heavy.append(v)

        if len(heavy) <= 1:
            return False
        if not any(not collinear(cfg[i], cfg[j]) for i, j in combinations(heavy, 2)):
            return False

    return True


def pair_tables(r, k):
    for counts in compositions(r, 9):
        a_neg = sum(m for (x, y), m in zip(PAIR_TYPES, counts) if x == -1)
        a_pos = sum(m for (x, y), m in zip(PAIR_TYPES, counts) if x == 1)
        b_neg = sum(m for (x, y), m in zip(PAIR_TYPES, counts) if y == -1)
        b_pos = sum(m for (x, y), m in zip(PAIR_TYPES, counts) if y == 1)
        if a_neg < k + 1 or b_neg < k + 1:
            continue
        if a_pos < 1 or b_pos < 1:
            continue

        transpose = tuple(counts[PAIR_TYPES.index((y, x))] for x, y in PAIR_TYPES)
        if counts > transpose:
            continue

        a = []
        b = []
        for (x, y), m in zip(PAIR_TYPES, counts):
            a.extend([x] * m)
            b.extend([y] * m)
        a, b = tuple(a), tuple(b)
        if collinear(a, b):
            continue
        yield counts


def splits3(m):
    for nneg in range(m + 1):
        for nzero in range(m - nneg + 1):
            yield (nneg, nzero, m - nneg - nzero)


def triple_representatives(counts, r):
    active = [(idx, m) for idx, m in enumerate(counts) if m]

    def rec(j, cneg, cpos, parts):
        if cneg > r // 2:
            return
        if j == len(active):
            if cpos < cneg + 1:
                return
            amap = dict(parts)
            a = []
            b = []
            c = []
            for idx, (x, y) in enumerate(PAIR_TYPES):
                m = counts[idx]
                if not m:
                    continue
                nn, nz, np = amap[idx]
                a.extend([x] * nn); b.extend([y] * nn); c.extend([-1] * nn)
                a.extend([x] * nz); b.extend([y] * nz); c.extend([0] * nz)
                a.extend([x] * np); b.extend([y] * np); c.extend([1] * np)
            yield tuple(a), tuple(b), tuple(c)
            return

        idx, m = active[j]
        for sp in splits3(m):
            nn, nz, np = sp
            yield from rec(j + 1, cneg + nn, cpos + np, parts + ((idx, sp),))

    yield from rec(0, 0, 0, ())


def check_case(r, k):
    pair_count = triple_count = minimum_relation_count = violations = 0
    for counts in pair_tables(r, k):
        pair_count += 1
        for a, b, c in triple_representatives(counts, r):
            triple_count += 1

            if sum(x == 1 for x in c) == 1 and sum(x != 0 for x in c) == 1:
                continue
            if c == a or c == b:
                continue

            rels = relation_data(a, b, c)
            c_relation_support = 1 + sum(x != 0 for x in c)
            minimum_support = min((supp.bit_count() for _, supp, _, _ in rels), default=10**9)
            if c_relation_support != minimum_support:
                continue
            minimum_relation_count += 1

            if profile_violation(a, b, c, k):
                violations += 1

    return pair_count, triple_count, minimum_relation_count, violations


def check_abstract_nonboolean_counterexample():
    a = (-1, -1, -1, 0, 0)
    b = (-1, -1, 0, -1, 0)
    c = (1, 1, 0, 0, -1)
    rels = relation_data(a, b, c)
    assert 1 + sum(x != 0 for x in c) == min(s.bit_count() for _, s, _, _ in rels)
    assert profile_violation(a, b, c, 2)
    assert sum(x == 1 for x in a) == 0 and sum(x == 1 for x in b) == 0


def main():
    total_pairs = total_triples = total_min = total_viol = 0
    for r in range(1, 9):
        for k in range(r):
            if 2 * (k + 1) <= r:
                continue
            p, t, m, v = check_case(r, k)
            total_pairs += p; total_triples += t; total_min += m; total_viol += v
            print(f"RANK {r} K {k} PAIR_ORBITS {p} TRIPLE_ORBITS {t} MINREL_CANDIDATES {m} VIOLATIONS {v}")

    assert total_viol == 0
    check_abstract_nonboolean_counterexample()

    print(f"TOTAL_PAIR_ORBITS {total_pairs}")
    print(f"TOTAL_TRIPLE_ORBITS {total_triples}")
    print(f"TOTAL_MINREL_CANDIDATES {total_min}")
    print("TOTAL_VIOLATIONS 0")
    print("ABSTRACT_NONBOOLEAN_COUNTEREXAMPLE_CONFIRMED")
    print("NULLITY3_PROFILE_SAFE_THROUGH_RANK_8")
    print("ALL_CHECKS_PASSED")


if __name__ == "__main__":
    main()
