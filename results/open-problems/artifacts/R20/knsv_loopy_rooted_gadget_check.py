#!/usr/bin/env python3
"""Exact check for R20 / KNSV-2026-LOOPY-U.

Seed pair: Kirillov--Nenashev--Shapiro--Vaintrob, Prop. 7.5,
graph6 I?bB@_wYO and I?bB@_wk_.  The source states that these
10-vertex simple graphs collide for both L and refined L.

We test every simple rooted gadget obtained by adjoining exactly two new
vertices a,b and choosing an arbitrary subset of the three possible gadget
edges va,vb,ab.  Up to swapping the two new vertices there are six gadget
types (patterns 0,1,3,4,5,7); the omitted labeled patterns 2 and 6 are
isomorphic to 1 and 5.  The gadget is allowed to be disconnected.  For each
of the 10 roots on each seed graph we compute the ordinary U-polynomial
exactly, compare all 60 x 60 cross pairs, and for every nontrivial U-collision
compute L(1,x) exactly by the spanning-forest activity formula.  Since the
paper proves L(1,x) and the graded L(t,x) determine one another, a difference
at t=1 would be a source-valid separator.

No floating point arithmetic is used.
"""
from collections import defaultdict, Counter
import hashlib

CODES = ("I?bB@_wYO", "I?bB@_wk_")


def decode_graph6(s):
    vals = [ord(c) - 63 for c in s]
    if not vals or not (0 <= vals[0] <= 62):
        raise ValueError("checker only implements one-byte graph6 order")
    n = vals[0]
    bits = []
    for v in vals[1:]:
        bits.extend((v >> sh) & 1 for sh in range(5, -1, -1))
    need = n * (n - 1) // 2
    if len(bits) < need:
        raise ValueError("truncated graph6")
    edges = []
    k = 0
    for j in range(1, n):
        for i in range(j):
            if bits[k]:
                edges.append((i, j))
            k += 1
    return n, tuple(edges)


def find(p, x):
    while p[x] != x:
        p[x] = p[p[x]]
        x = p[x]
    return x


def union(p, sz, a, b):
    a, b = find(p, a), find(p, b)
    if a == b:
        return False
    if sz[a] < sz[b]:
        a, b = b, a
    p[b] = a
    sz[a] += sz[b]
    return True


def u_poly(n, edges):
    """Exact U dictionary via a partition-state edge DP.

    Basis: prod z_size * (y-1)^cyclomatic.  The DP merges all edge subsets
    leading to the same set partition and edge count, avoiding a fresh DSU
    construction for every subset.
    """
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    init = tuple(range(n))
    dp = {(init, 0): 1}
    for u, v in edges:
        nd = defaultdict(int)
        for (part, ec), cnt in dp.items():
            nd[(part, ec)] += cnt
            ru, rv = part[u], part[v]
            if ru == rv:
                p2 = part
            else:
                a, b = (ru, rv) if ru < rv else (rv, ru)
                p2 = tuple(a if x == b else x for x in part)
            nd[(p2, ec + 1)] += cnt
        dp = nd
    out = defaultdict(int)
    for (part, ec), cnt in dp.items():
        mult = Counter(part)
        sizes = tuple(sorted(mult.values()))
        cyc = ec - n + len(mult)
        out[(sizes, cyc)] += cnt
    return dict(out)


def l1_poly(n, edges):
    """Dictionary for L_G(1,x) from the exact forest-activity expansion.

    We call a nonforest edge externally active when it is larger than every
    edge on its fundamental cycle.  This is just the standard activity order
    with the chosen total edge order; the resulting polynomial is order
    independent.
    """
    edges = tuple(sorted(tuple(sorted(e)) for e in edges))
    m = len(edges)
    out = defaultdict(int)
    for mask in range(1 << m):
        p = list(range(n)); sz = [1] * n; acyclic = True
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1 and not union(p, sz, u, v):
                acyclic = False
                break
        if not acyclic:
            continue
        comps = {}
        for v in range(n):
            r = find(p, v)
            comps[r] = sz[r]
        final_root = [find(p, v) for v in range(n)]
        eps = {r: 0 for r in comps}

        # Prefix forest contains precisely the chosen forest edges preceding i.
        pp = list(range(n)); ss = [1] * n
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                union(pp, ss, u, v)
            elif find(pp, u) == find(pp, v):
                eps[final_root[u]] += 1

        mon = tuple(sorted((s - 1) + eps[r] for r, s in comps.items()))
        out[mon] += 1
    return dict(out)


def attach_two(n, edges, root, pattern):
    """Add labeled a=n,b=n+1; bits select root-a, root-b, a-b."""
    a, b = n, n + 1
    e = list(edges)
    opts = ((root, a), (root, b), (a, b))
    for bit, edge in enumerate(opts):
        if (pattern >> bit) & 1:
            e.append(edge)
    return n + 2, tuple(e)


def digest(poly):
    payload = repr(sorted(poly.items())).encode()
    return hashlib.sha256(payload).hexdigest()


def main():
    seeds = [decode_graph6(c) for c in CODES]
    assert seeds[0][0] == seeds[1][0] == 10
    assert len(seeds[0][1]) == len(seeds[1][1]) == 14

    U0 = u_poly(*seeds[0]); U1 = u_poly(*seeds[1])
    L0 = l1_poly(*seeds[0]); L1 = l1_poly(*seeds[1])
    assert U0 == U1, "source seed pair failed U collision sanity check"
    assert L0 == L1, "source seed pair failed L(1,x) collision sanity check"

    ext_u = [{}, {}]
    for side, (n, edges) in enumerate(seeds):
        for pattern in (0, 1, 3, 4, 5, 7):
            for root in range(10):
                H = attach_two(n, edges, root, pattern)
                ext_u[side][(pattern, root)] = u_poly(*H)

    matches = []
    for k0, p0 in ext_u[0].items():
        for k1, p1 in ext_u[1].items():
            if p0 == p1:
                matches.append((k0, k1))

    # Patterns 0 (two isolates) and 4 (a--b disjoint from root) are disjoint
    # unions with the same added graph.  Since the seed L-polynomials agree,
    # their L-polynomials agree multiplicatively without further enumeration.
    trivial = [x for x in matches if x[0][0] in (0, 4) and x[1][0] in (0, 4)]
    nontrivial = [x for x in matches if x not in trivial]

    lcache = [{}, {}]
    for side, keys in enumerate((sorted({a for a, _ in nontrivial}),
                                 sorted({b for _, b in nontrivial}))):
        n, edges = seeds[side]
        for key in keys:
            pattern, root = key
            lcache[side][key] = l1_poly(*attach_two(n, edges, root, pattern))

    separators = []
    for k0, k1 in nontrivial:
        if lcache[0][k0] != lcache[1][k1]:
            separators.append((k0, k1))

    by_pattern = Counter((a[0], b[0]) for a, b in matches)
    print("R20 KNSV-2026-LOOPY-U exact rooted-two-vertex gadget check")
    print(f"seed_graph6={CODES[0]} ; {CODES[1]}")
    print("seed_n=10 seed_m=14")
    print(f"seed_U_equal={U0 == U1} U_terms={len(U0)} U_sha256={digest(U0)}")
    print(f"seed_L1_equal={L0 == L1} L1_terms={len(L0)} L1_sha256={digest(L0)}")
    print("unlabeled_gadget_types=6 roots_per_seed=10 extensions_per_seed=60")
    print("cross_extension_pairs=3600")
    print(f"U_equal_cross_pairs={len(matches)}")
    print(f"trivial_disjoint_U_equal_pairs={len(trivial)}")
    print(f"nontrivial_U_equal_pairs={len(nontrivial)}")
    print("U_equal_pattern_pair_counts=" + repr(sorted(by_pattern.items())))
    print("nontrivial_U_equal_pairs_list=" + repr(nontrivial))
    print(f"U_equal_but_L1_different_pairs={len(separators)}")
    print("separators=" + repr(separators))
    assert len(matches) == 208
    assert len(trivial) == 200
    assert len(nontrivial) == 8
    assert not separators
    print("VERDICT=PASS: this seed collision cannot be turned into a Conjecture-8.2 separator by any rooted simple gadget on exactly two new vertices attached only through one old root.")
    print("SCOPE=PARTIAL_ONLY: this does not exclude general 12-vertex separators and does not prove Conjecture 8.2.")

if __name__ == "__main__":
    main()
