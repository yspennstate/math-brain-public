#!/usr/bin/env python3
"""Exact self-check for the NM13-11 E0082 ladder-composition quotient.

No external dependencies.  Every matching-matrix entry and quotient entry is
computed with integers/Fraction.  For square first-passage families n=m^2,
m=2,3,4, the script verifies:
  (i) the Dyck-block composition partition and class sizes;
  (ii) class-summed matching rows are identical inside each composition class;
  (iii) the closed quotient-entry formula agrees exactly with direct overlap
        enumeration for every ordered pair of classes;
  (iv) the total pattern count agrees with the ballot/reflection formula.
"""

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb


def catalan(r):
    return comb(2 * r, r) // (r + 1)


def meander_count(t, e):
    """Nonnegative +/-1 paths of length t from 0 to e."""
    if t < e or ((t - e) & 1):
        return 0
    up = (t + e) // 2
    return comb(t, up) - (comb(t, up + 1) if up + 1 <= t else 0)


def first_passage_words(m, n):
    """Words ending at -m and first hitting -m at time n."""
    if (n - m) & 1:
        return []
    nplus = (n - m) // 2
    out = []
    for pos in combinations(range(n), nplus):
        plus = set(pos)
        w = tuple(1 if i in plus else -1 for i in range(n))
        s = 0
        ok = True
        for i, a in enumerate(w):
            s += a
            if i < n - 1 and s <= -m:
                ok = False
                break
        if ok and s == -m:
            out.append(w)
    return out


def ladder_composition(w, m):
    """Semilengths of the m Dyck words between descending ladder steps."""
    r = []
    level = 0
    i = 0
    for j in range(1, m + 1):
        start = i
        while True:
            level += w[i]
            i += 1
            if level == -j:
                break
        block_len = i - start
        assert block_len & 1
        r.append((block_len - 1) // 2)
    assert i == len(w)
    return tuple(r)


def tau(r, d):
    return 2 * sum(r[:d]) + d


def quotient_formula(r, s, n, m):
    """Closed formula for sum_{B in class s} M[A,B], A in class r."""
    value = Fraction(int(r == s), 1)
    R = [0]
    for a in r:
        R.append(R[-1] + a)

    for d in range(1, m):
        shift = n - tau(r, d)
        weight = Fraction(1, 2 ** shift)
        for e in range(d):
            k = m - d + e
            # 0-based form of s_{k+2..m}=r_{e+2..d}.
            if tuple(s[k + 1 : m]) != tuple(r[e + 1 : d]):
                continue
            t = 2 * (s[k] - R[e + 1]) - e
            count = 1
            for j in range(k):
                count *= catalan(s[j])
            count *= meander_count(t, e)
            value += weight * count
    return value


def suffix_class_maps(words, cls, n):
    maps = []
    for shift in range(n):
        d = defaultdict(lambda: defaultdict(int))
        for w in words:
            d[w[shift:]][cls[w]] += 1
        maps.append(d)
    return maps


def direct_class_row(A, suffix_maps, n):
    """Direct exact class-summed row using the source matching convention."""
    row = defaultdict(Fraction)
    for shift in range(n):
        counts = suffix_maps[shift].get(A[: n - shift], {})
        weight = Fraction(1, 2 ** shift)
        for s, multiplicity in counts.items():
            row[s] += weight * multiplicity
    return row


def expected_pattern_count(m, n):
    # Standard first-passage count: m/n * binom(n,(n-m)/2).
    return m * comb(n, (n - m) // 2) // n


def check_m(m):
    n = m * m
    words = first_passage_words(m, n)
    cls = {w: ladder_composition(w, m) for w in words}
    classes = defaultdict(list)
    for w in words:
        classes[cls[w]].append(w)

    N = (n - m) // 2
    expected_classes = comb(N + m - 1, m - 1)
    assert len(words) == expected_pattern_count(m, n)
    assert len(classes) == expected_classes

    for r, ws in classes.items():
        assert sum(r) == N
        expected_size = 1
        for a in r:
            expected_size *= catalan(a)
        assert len(ws) == expected_size

    suffix_maps = suffix_class_maps(words, cls, n)

    # Strong exact equitable-partition check: every row in a source class has
    # the same class-summed row.
    representative_rows = {}
    for r, ws in classes.items():
        base = direct_class_row(ws[0], suffix_maps, n)
        representative_rows[r] = base
        for A in ws[1:]:
            assert direct_class_row(A, suffix_maps, n) == base

    # Closed formula versus direct enumeration, every ordered class pair.
    comparisons = 0
    for r, row in representative_rows.items():
        for s in classes:
            direct = row.get(s, Fraction(0, 1))
            formula = quotient_formula(r, s, n, m)
            assert direct == formula, (m, r, s, direct, formula)
            comparisons += 1

    print(
        f"m={m} n={n} patterns={len(words)} classes={len(classes)} "
        f"class_pairs={comparisons} exact_invariance=PASS formula=PASS"
    )


def main():
    for m in (2, 3, 4):
        check_m(m)

    # A source-relevant next square size, counted without enumerating 653752
    # patterns: the quotient has only 1001 weak-composition states.
    m = 5
    n = m * m
    N = (n - m) // 2
    print(
        f"m=5 n=25 patterns={expected_pattern_count(m,n)} "
        f"classes={comb(N+m-1,m-1)} (closed-form counts only)"
    )
    print("ALL_EXACT_CHECKS_PASS")


if __name__ == "__main__":
    main()
