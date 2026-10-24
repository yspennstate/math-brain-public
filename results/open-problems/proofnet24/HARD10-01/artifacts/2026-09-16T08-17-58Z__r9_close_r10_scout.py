#!/usr/bin/env python3
"""HARD10-01 exact self-checks for the 2026-09-16 08Z checkpoint.

Supporting evidence only; universal proofs are in the Markdown checkpoint.

Checks:
  * exact |R|=9 partitions for representative adjacent/disjoint e,f on n=6,7;
  * absence there of the newly eliminated 8+1, 7+1+1, 6+1+1+1, 5+1+1+1+1;
  * abstract classification of eight-element downward-closed root fibers;
  * small pair-graph classifications used for 5+1^4 and 6+1^3;
  * first exact |R|=10 reconnaissance on the same finite ranges.
"""
from collections import Counter
from itertools import combinations


def norm(e):
    return tuple(sorted(e))


def forest_components(n, edges, mask):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, (a, b) in enumerate(edges):
        if not ((mask >> i) & 1):
            continue
        a, b = find(a), find(b)
        if a == b:
            return None
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1

    for i in range(n):
        parent[i] = find(i)
    return parent


def fixed_R_arrays(n, e, f):
    e, f = norm(e), norm(f)
    H = [g for g in combinations(range(n), 2) if g not in (e, f)]
    N = 1 << len(H)

    r = bytearray(N)
    a, b = e
    c, d = f
    for mask in range(N):
        comp = forest_components(n, H, mask)
        if comp is None:
            continue
        ra, rb, rc, rd = comp[a], comp[b], comp[c], comp[d]
        if ra == rb or rc == rd:
            continue
        if rc in (ra, rb) and rd in (ra, rb) and rc != rd:
            r[mask] = 1

    root = bytearray(N)
    for mask in range(N):
        if not r[mask]:
            continue
        x = mask
        while x:
            bit = x & -x
            if r[mask ^ bit]:
                break
            x -= bit
        else:
            root[mask] = 1

    counts = list(r)
    for i in range(len(H)):
        bit = 1 << i
        for mask in range(N):
            if mask & bit:
                counts[mask] += counts[mask ^ bit]
    return H, r, root, counts


def root_fibers(Rs, roots):
    return {P: [A for A in Rs if (P & ~A) == 0] for P in roots}


def classify(M, r_masks, root_masks):
    Rs = [A for A in r_masks if (A & ~M) == 0]
    roots = [P for P in root_masks if (P & ~M) == 0]
    fib = root_fibers(Rs, roots)
    return tuple(sorted((len(v) for v in fib.values()), reverse=True))


def rN_partitions(n, e, f, target):
    _, r, root, counts = fixed_R_arrays(n, e, f)
    r_masks = [m for m, x in enumerate(r) if x]
    root_masks = [m for m, x in enumerate(root) if x]
    out = Counter()
    for M, total in enumerate(counts):
        if total == target:
            out[classify(M, r_masks, root_masks)] += 1
    return out


def downward_closed_size8(k):
    base = {0} | {1 << i for i in range(k)}
    extras = [m for m in range(1 << k) if m not in base]
    need = 8 - len(base)
    out = []
    for choice in combinations(extras, need):
        fam = base | set(choice)
        ok = True
        for m in fam:
            x = m
            while x:
                bit = x & -x
                if (m ^ bit) not in fam:
                    ok = False
                    break
                x -= bit
            if not ok:
                break
        if ok:
            out.append(fam)
    return out


def double_edges(k, fam):
    ans = []
    for m in fam:
        if m.bit_count() == 2:
            v = [i for i in range(k) if (m >> i) & 1]
            ans.append(tuple(v))
    return ans


def degree_sequence(n, edges):
    d = [0] * n
    for a, b in edges:
        d[a] += 1
        d[b] += 1
    return tuple(sorted(d, reverse=True))


def check_size8_downsets():
    expected = {
        7: (1, {(0, 0)}),
        6: (15, {(1, 0)}),
        5: (45, {(2, 0)}),
        4: (20, {(3, 0)}),
        3: (1, {(3, 1)}),
    }
    summary = {}
    for k in range(3, 8):
        fams = downward_closed_size8(k)
        sig = {
            (
                sum(1 for m in fam if m.bit_count() == 2),
                sum(1 for m in fam if m.bit_count() == 3),
            )
            for fam in fams
        }
        assert (len(fams), sig) == expected[k]
        summary[k] = (len(fams), sorted(sig))

    degs = Counter(
        degree_sequence(4, double_edges(4, fam))
        for fam in downward_closed_size8(4)
    )
    assert set(degs) == {
        (2, 2, 1, 1),
        (2, 2, 2, 0),
        (3, 1, 1, 1),
    }
    return summary, degs


def check_pair_graphs():
    deg4 = Counter()
    K4edges = list(combinations(range(4), 2))
    for E in combinations(K4edges, 4):
        deg4[degree_sequence(4, E)] += 1
    assert set(deg4) == {(2, 2, 2, 2), (3, 2, 2, 1)}

    sols = []
    for x01 in (0, 1):
        for x12 in (0, 1):
            for x23 in (0, 1):
                for x30 in (0, 1):
                    if (
                        (x01 ^ x12)
                        and (x12 ^ x23)
                        and (x23 ^ x30)
                        and (x30 ^ x01)
                    ):
                        sols.append((x01, x12, x23, x30))
    assert set(sols) == {(1, 0, 1, 0), (0, 1, 0, 1)}

    deg5 = Counter()
    K5edges = list(combinations(range(5), 2))
    for E in combinations(K5edges, 3):
        deg5[degree_sequence(5, E)] += 1
    assert set(deg5) == {
        (2, 2, 1, 1, 0),
        (3, 1, 1, 1, 0),
        (2, 2, 2, 0, 0),
        (2, 1, 1, 1, 1),
    }
    return deg4, sols, deg5


def main():
    configs = [
        (6, (0, 1), (0, 2), "n6_adjacent"),
        (6, (0, 1), (2, 3), "n6_disjoint"),
        (7, (0, 1), (0, 2), "n7_adjacent"),
        (7, (0, 1), (2, 3), "n7_disjoint"),
    ]

    newly_eliminated = {
        (8, 1),
        (7, 1, 1),
        (6, 1, 1, 1),
        (5, 1, 1, 1, 1),
    }

    for n, e, f, label in configs:
        p9 = rN_partitions(n, e, f, 9)
        print(label, "R9", dict(p9))
        for p in newly_eliminated:
            assert p9.get(p, 0) == 0

    summary, deg8 = check_size8_downsets()
    print("size8_downsets", summary)
    print("k4_allowed_double_degree_sequences", dict(deg8))

    deg4, sols, deg5 = check_pair_graphs()
    print("four_pairs_on_four_degree_sequences", dict(deg4))
    print("C4_direct_indicator_solutions", sols)
    print("three_pairs_on_five_degree_sequences", dict(deg5))

    for n, e, f, label in configs:
        p10 = rN_partitions(n, e, f, 10)
        print(label, "R10", dict(p10))

    print("OK")


if __name__ == "__main__":
    main()
