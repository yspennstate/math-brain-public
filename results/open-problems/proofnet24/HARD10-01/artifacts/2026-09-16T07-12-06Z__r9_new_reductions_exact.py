#!/usr/bin/env python3
"""HARD10-01 exact self-checks for the 2026-09-16 07Z checkpoint.

Finite enumeration is supporting evidence only, not a proof premise.

For representative adjacent/disjoint distinguished pairs on n=6,7:
  * enumerate every labelled graph exactly via Boolean-zeta counts for R;
  * tabulate every |R|=9 root-fiber partition;
  * verify there are no (5,4), (3,3,3), or (3,3,1,1,1) instances.

The script also checks a family of explicit same-endpoint-cross-ear 5+4
candidate skeletons. Every tested skeleton acquires at least one extra
minimal common-cycle root, consistent with the mixed-cycle proof.
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
        # A+e and A+f are forests, but A+e+f is cyclic.
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


def r9_partitions(n, e, f):
    H, r, root, counts = fixed_R_arrays(n, e, f)
    r_masks = [m for m, x in enumerate(r) if x]
    root_masks = [m for m, x in enumerate(root) if x]
    out = Counter()
    for M, total in enumerate(counts):
        if total == 9:
            out[classify(M, r_masks, root_masks)] += 1
    return out


def is_forest_edges(n, E):
    idx = list(E)
    return forest_components(n, idx, (1 << len(idx)) - 1) is not None


def R_sets_for_graph(n, E, e, f):
    e, f = norm(e), norm(f)
    H = [g for g in sorted(set(map(norm, E))) if g not in (e, f)]
    ans = []
    for mask in range(1 << len(H)):
        A = {H[i] for i in range(len(H)) if (mask >> i) & 1}
        if not is_forest_edges(n, A):
            continue
        if not is_forest_edges(n, A | {e}):
            continue
        if not is_forest_edges(n, A | {f}):
            continue
        if is_forest_edges(n, A | {e, f}):
            continue
        ans.append(frozenset(A))
    return ans


def minimal_roots(Rs):
    return [A for A in Rs if not any(B < A for B in Rs)]


def check_same_endpoint_54_skeletons():
    # Common path R: u-p-a-b-c-q-v, with e=(u,p), f=(q,v).
    # w has u,v plus two internal attachments; x has u,v plus one.
    # These are the only potentially dangerous same-endpoint cross-ear
    # geometries after the 3+3 reduction. Every choice tested must have
    # at least a third minimal root.
    u, p, a, b, c, q, v, w, x = range(9)
    Rpath = [norm(z) for z in [(u, p), (p, a), (a, b), (b, c), (c, q), (q, v)]]
    e = norm((u, p))
    f = norm((q, v))
    internal = [a, b, c]
    checked = 0
    for wa, wb in combinations(internal, 2):
        for xc in internal:
            E = set(Rpath)
            E.update(map(norm, [
                (u, w), (v, w), (wa, w), (wb, w),
                (u, x), (v, x), (xc, x),
            ]))
            Rs = R_sets_for_graph(9, E, e, f)
            roots = minimal_roots(Rs)
            assert len(roots) >= 3
            checked += 1
    return checked


def main():
    configs = [
        (6, (0, 1), (0, 2), "n6_adjacent"),
        (6, (0, 1), (2, 3), "n6_disjoint"),
        (7, (0, 1), (0, 2), "n7_adjacent"),
        (7, (0, 1), (2, 3), "n7_disjoint"),
    ]
    forbidden = {(5, 4), (3, 3, 3), (3, 3, 1, 1, 1)}
    for n, e, f, label in configs:
        parts = r9_partitions(n, e, f)
        print(label, dict(parts))
        for p in forbidden:
            assert parts.get(p, 0) == 0
    print(
        "same_endpoint_5+4_candidate_skeletons_checked",
        check_same_endpoint_54_skeletons(),
    )
    print("OK")


if __name__ == "__main__":
    main()
