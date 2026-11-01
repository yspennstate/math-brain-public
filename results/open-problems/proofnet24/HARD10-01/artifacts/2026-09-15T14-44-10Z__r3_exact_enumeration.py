#!/usr/bin/env python3
"""Exact finite check for HARD10-01, 2026-09-15T14:44:10Z.

Enumerates all labelled graphs on n<=6 containing a fixed distinguished pair.
By vertex-label symmetry there are only two pair types: adjacent and disjoint.
For every graph it classifies all forests of H=G\{e,f} into the five classes
N0, Ne, Nf, B, R.  For the exact |R|=3 stratum it checks:
  * the number of inclusion-minimal R forests;
  * the exact integer Rayleigh gap
      Delta = Ne*Nf + R*(Ne+Nf+B+R) - B*N0.

No floating point arithmetic and no external packages are used.
This is finite adversarial evidence, not a proof of the universal conjecture.
"""

from collections import Counter
from itertools import combinations


def forest_components(n, edges, mask):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True

    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            if not union(u, v):
                return None
    return tuple(find(v) for v in range(n))


def zeta_subset_sums(values, m):
    out = values[:]
    for i in range(m):
        bit = 1 << i
        for mask in range(1 << m):
            if mask & bit:
                out[mask] += out[mask ^ bit]
    return out


def exact_summary(n, e, f):
    all_edges = list(combinations(range(n), 2))
    hedges = [g for g in all_edges if g not in (e, f)]
    m = len(hedges)

    cats = {k: [0] * (1 << m) for k in ("N0", "Ne", "Nf", "B", "R")}
    r_masks = []

    for mask in range(1 << m):
        comp = forest_components(n, hedges, mask)
        if comp is None:
            continue

        eu, ev = comp[e[0]], comp[e[1]]
        fu, fv = comp[f[0]], comp[f[1]]
        e_ok = eu != ev
        f_ok = fu != fv

        if not e_ok and not f_ok:
            cat = "N0"
        elif e_ok and not f_ok:
            cat = "Ne"
        elif f_ok and not e_ok:
            cat = "Nf"
        elif {eu, ev} == {fu, fv}:
            cat = "R"
        else:
            cat = "B"

        cats[cat][mask] = 1
        if cat == "R":
            r_masks.append(mask)

    counts = {k: zeta_subset_sums(v, m) for k, v in cats.items()}

    total_r3 = 0
    unique_minimal = 0
    nonpositive = 0
    min_delta = None
    size_signatures = Counter()

    for hmask in range(1 << m):
        if counts["R"][hmask] != 3:
            continue

        total_r3 += 1
        rs = [r for r in r_masks if (r & ~hmask) == 0]
        assert len(rs) == 3

        minimal = []
        for r in rs:
            if not any(s != r and (s & r) == s for s in rs):
                minimal.append(r)

        if len(minimal) == 1:
            unique_minimal += 1

        size_signatures[(len(minimal), tuple(sorted(r.bit_count() for r in rs)))] += 1

        N0 = counts["N0"][hmask]
        Ne = counts["Ne"][hmask]
        Nf = counts["Nf"][hmask]
        B = counts["B"][hmask]
        R = counts["R"][hmask]
        delta = Ne * Nf + R * (Ne + Nf + B + R) - B * N0

        if min_delta is None or delta < min_delta:
            min_delta = delta
        if delta <= 0:
            nonpositive += 1

    return total_r3, unique_minimal, min_delta, nonpositive, size_signatures


def main():
    expected = {
        (3, "adjacent"): (0, 0, None, 0),
        (4, "adjacent"): (2, 2, 18, 0),
        (4, "disjoint"): (0, 0, None, 0),
        (5, "adjacent"): (16, 16, 18, 0),
        (5, "disjoint"): (20, 20, 36, 0),
        (6, "adjacent"): (138, 138, 18, 0),
        (6, "disjoint"): (328, 328, 36, 0),
    }

    for n in range(3, 7):
        tests = [("adjacent", (0, 1), (0, 2))]
        if n >= 4:
            tests.append(("disjoint", (0, 1), (2, 3)))

        for kind, e, f in tests:
            result = exact_summary(n, e, f)
            head = result[:4]
            assert head == expected[(n, kind)], (n, kind, head)
            total, unique, mindelta, nonpositive, sigs = result
            print(
                f"n={n} {kind}: |R|=3 graphs={total}, "
                f"unique-minimal={unique}, min-Delta={mindelta}, "
                f"nonpositive={nonpositive}, signatures={dict(sigs)}"
            )

    print("ALL EXACT CHECKS PASSED")


if __name__ == "__main__":
    main()
