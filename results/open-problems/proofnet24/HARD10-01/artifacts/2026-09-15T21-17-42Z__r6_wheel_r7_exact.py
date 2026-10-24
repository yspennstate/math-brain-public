#!/usr/bin/env python3
"""HARD10-01 exact checks for the 2026-09-15T21:17:42Z checkpoint.

Standard library only.  The computations are finite checks, not universal proof
premises.

Checks:
  1. the bare decorated-core graph K5 minus a matching has unit pair-Rayleigh
     gap 84 for the distinguished pair used in the R=6 proof;
  2. every observed R=6, fiber-partition (4,1,1) instance through n=7 has
     exactly one of the two shared-ear direct edges;
  3. suppressing the absent-direct singleton ear gives exactly two incomparable
     R roots, with the present and suppressed edges in opposite root differences;
  4. extraction of the two distinguished terminal networks gives the exact
     identity Delta_G = 84 * alpha_1 * alpha_2 in every such instance;
  5. exact R=7 root-fiber partition counts for representative adjacent and
     disjoint distinguished pairs on n=6,7.
"""

from collections import Counter, defaultdict
from itertools import combinations


def norm(e):
    return tuple(sorted(e))


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
    return True


def zeta(a, m):
    z = a[:]
    for i in range(m):
        bit = 1 << i
        for mask in range(1 << m):
            if mask & bit:
                z[mask] += z[mask ^ bit]
    return z


def fixed_R_arrays(n, e, f):
    e, f = norm(e), norm(f)
    H = [g for g in combinations(range(n), 2) if g not in (e, f)]
    m = len(H)
    N = 1 << m
    r = [0] * N

    for mask in range(N):
        A = [H[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        eo = is_forest(n, A + [e])
        fo = is_forest(n, A + [f])
        efo = is_forest(n, A + [e, f])
        if eo and fo and not efo:
            r[mask] = 1

    root = [0] * N
    for mask in range(N):
        if not r[mask]:
            continue
        x = mask
        minimal = True
        while x:
            bit = x & -x
            if r[mask ^ bit]:
                minimal = False
                break
            x -= bit
        if minimal:
            root[mask] = 1

    return H, r, root, zeta(r, m)


def edge_set(H, mask):
    return {H[i] for i in range(len(H)) if (mask >> i) & 1}


def root_fibers(Rs, roots):
    return {P: [A for A in Rs if (P & ~A) == 0] for P in roots}


def extension_single_edges(H, P, fiber):
    out = []
    for A in fiber:
        if A == P:
            continue
        d = A ^ P
        assert d.bit_count() == 1
        out.append(H[(d & -d).bit_length() - 1])
    return out


def direct_delta(n, E, e, f):
    E = sorted(set(map(norm, E)))
    e, f = norm(e), norm(f)
    ie, jf = E.index(e), E.index(f)
    A = B = C = D = 0
    for mask in range(1 << len(E)):
        F = [E[i] for i in range(len(E)) if (mask >> i) & 1]
        if not is_forest(n, F):
            continue
        he = (mask >> ie) & 1
        hf = (mask >> jf) & 1
        if not he and not hf:
            A += 1
        elif he and not hf:
            B += 1
        elif hf and not he:
            C += 1
        else:
            D += 1
    return B * C - A * D, (A, B, C, D)


def component_edges(E, target):
    adj = defaultdict(set)
    for a, b in E:
        adj[a].add(b)
        adj[b].add(a)
    seen = set()
    stack = [target[0]]
    while stack:
        x = stack.pop()
        if x in seen:
            continue
        seen.add(x)
        stack.extend(adj[x] - seen)
    return {g for g in E if g[0] in seen and g[1] in seen}, seen


def alpha_unit(n, K, terminals, distinguished):
    K = sorted(set(map(norm, K)))
    s, t = terminals
    q = norm(distinguished)
    iq = K.index(q)
    D = C = Dq = Cq = 0

    for mask in range(1 << len(K)):
        F = [K[i] for i in range(len(K)) if (mask >> i) & 1]
        if not is_forest(n, F):
            continue

        parent = list(range(n))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in F:
            a, b = find(a), find(b)
            if a != b:
                parent[b] = a
        connected = find(s) == find(t)
        has_q = (mask >> iq) & 1
        if connected:
            C += 1
            Cq += has_q
        else:
            D += 1
            Dq += has_q

    return D * Cq - C * Dq


def wheel_core_certificate():
    n = 5
    e, f = (0, 1), (2, 3)
    E = {
        (0, 1), (0, 2), (0, 3), (0, 4),
        (1, 3), (1, 4), (2, 3), (2, 4),
    }
    other = sorted(E - {e, f})
    table = {}
    totals = {}
    for he, hf, name in ((0, 0, "A"), (1, 0, "B"), (0, 1, "C"), (1, 1, "D")):
        row = Counter()
        for mask in range(1 << len(other)):
            F = [other[i] for i in range(len(other)) if (mask >> i) & 1]
            if he:
                F.append(e)
            if hf:
                F.append(f)
            if is_forest(n, F):
                row[mask.bit_count()] += 1
        table[name] = row
        totals[name] = sum(row.values())

    assert table["A"] == Counter({0: 1, 1: 6, 2: 15, 3: 19, 4: 11})
    assert table["B"] == Counter({0: 1, 1: 6, 2: 13, 3: 10})
    assert table["C"] == Counter({0: 1, 1: 6, 2: 14, 3: 13})
    assert table["D"] == Counter({0: 1, 1: 6, 2: 11})
    assert totals == {"A": 52, "B": 30, "C": 34, "D": 18}
    assert totals["B"] * totals["C"] - totals["A"] * totals["D"] == 84
    print("W4 CORE VERIFIED: (A,B,C,D)=(52,30,34,18), Delta=84")


def partition_counts(H, r, root, counts, target):
    r_masks = [m for m, x in enumerate(r) if x]
    root_masks = [m for m, x in enumerate(root) if x]
    out = Counter()
    for M, value in enumerate(counts):
        if value != target:
            continue
        Rs = [A for A in r_masks if (A & ~M) == 0]
        roots = [P for P in root_masks if (P & ~M) == 0]
        fibers = root_fibers(Rs, roots)
        part = tuple(sorted((len(v) for v in fibers.values()), reverse=True))
        out[part] += 1
    return out


def check_411(n, e, f, H, r, root, counts, expected_number, expected_triples):
    e, f = norm(e), norm(f)
    r_masks = [m for m, x in enumerate(r) if x]
    root_masks = [m for m, x in enumerate(root) if x]
    triples = Counter()
    checked = 0

    for M, value in enumerate(counts):
        if value != 6:
            continue
        Rs = [A for A in r_masks if (A & ~M) == 0]
        roots = [P for P in root_masks if (P & ~M) == 0]
        fibers = root_fibers(Rs, roots)
        part = tuple(sorted((len(v) for v in fibers.values()), reverse=True))
        if part != (4, 1, 1):
            continue
        checked += 1

        P = next(P for P in roots if len(fibers[P]) == 4)
        singles = [Q for Q in roots if len(fibers[Q]) == 1]
        spokes = extension_single_edges(H, P, fibers[P])
        assert len(spokes) == 3
        common = set(spokes[0]) & set(spokes[1]) & set(spokes[2])
        assert len(common) == 1
        w = next(iter(common))

        def attachment(g):
            return next(x for x in g if x != w)

        def singleton_pair(Q):
            Qset = edge_set(H, Q)
            return frozenset(attachment(g) for g in spokes if g in Qset)

        pairs = [singleton_pair(Q) for Q in singles]
        assert all(len(p) == 2 for p in pairs)
        shared = set(pairs[0]) & set(pairs[1])
        assert len(shared) == 1
        u = next(iter(shared))

        E = edge_set(H, M) | {e, f}
        direct_flags = [norm(tuple(p)) in E for p in pairs]
        assert sum(direct_flags) == 1
        present_pair = pairs[direct_flags.index(True)]
        absent_pair = pairs[direct_flags.index(False)]
        v = next(iter(set(present_pair) - {u}))
        z = next(iter(set(absent_pair) - {u}))
        uv, uz = norm((u, v)), norm((u, z))

        def Q_for_pair(pair):
            return next(Q for Q in singles if singleton_pair(Q) == frozenset(pair))

        Q1 = Q_for_pair((u, v))
        Q2 = Q_for_pair((u, z))
        Pset = edge_set(H, P)
        Q1set = edge_set(H, Q1)
        Q2set = edge_set(H, Q2)
        assert uv in Pset
        assert Q1set == (Pset - {uv}) | {norm((u, w)), norm((v, w))}
        assert uv not in Q2set
        assert uz not in E

        # Compress the absent-direct singleton ear.
        MB = M
        for s in spokes:
            MB &= ~(1 << H.index(s))
        MB |= 1 << H.index(uz)
        assert counts[MB] == 2
        rootsB = [R for R in root_masks if (R & ~MB) == 0]
        assert len(rootsB) == 2
        Qp = next(R for R in rootsB if R != P)
        Qpset = edge_set(H, Qp)
        assert uv in Pset - Qpset
        assert uz in Qpset - Pset
        exchange = (Pset - Qpset) | (Qpset - Pset)
        assert len(exchange) == 4

        # Extract the two distinguished terminal networks from the exact-two base.
        B_edges = (E - set(spokes)) | {uz}
        remainder = B_edges - exchange
        Ke, Ve = component_edges(remainder, e)
        Kf, Vf = component_edges(remainder, f)
        assert not (Ve & Vf)
        Te = {x for x in Ve if any(x in g for g in exchange)}
        Tf = {x for x in Vf if any(x in g for g in exchange)}
        assert len(Te) == len(Tf) == 2
        ae = alpha_unit(n, Ke, tuple(Te), e)
        af = alpha_unit(n, Kf, tuple(Tf), f)
        delta, _ = direct_delta(n, E, e, f)
        assert delta == 84 * ae * af
        triples[(delta, ae, af)] += 1

    assert checked == expected_number
    assert triples == Counter(expected_triples)
    print(f"n={n} R=6 (4,1,1): checked={checked}, triples={dict(triples)}")


if __name__ == "__main__":
    wheel_core_certificate()

    # Disjoint pair arrays are reused for both R=6 factor checks and R=7 reconnaissance.
    H6d, r6d, root6d, c6d = fixed_R_arrays(6, (0, 1), (2, 3))
    check_411(
        6, (0, 1), (2, 3), H6d, r6d, root6d, c6d, 144,
        {(84, 1, 1): 16, (168, 1, 2): 64, (168, 2, 1): 64},
    )

    H7d, r7d, root7d, c7d = fixed_R_arrays(7, (0, 1), (2, 3))
    check_411(
        7, (0, 1), (2, 3), H7d, r7d, root7d, c7d, 2520,
        {
            (84, 1, 1): 24,
            (168, 1, 2): 192,
            (168, 2, 1): 192,
            (336, 2, 2): 768,
            (336, 1, 4): 672,
            (336, 4, 1): 672,
        },
    )

    # R=7 partition reconnaissance.
    p6d = partition_counts(H6d, r6d, root6d, c6d, 7)
    p7d = partition_counts(H7d, r7d, root7d, c7d, 7)
    assert p6d == Counter({(3, 3, 1): 72, (7,): 64, (5, 1, 1): 36, (4, 3): 32})
    assert p7d == Counter({(7,): 1542, (3, 3, 1): 1260, (4, 3): 864, (5, 1, 1): 630})

    H6a, r6a, root6a, c6a = fixed_R_arrays(6, (0, 1), (0, 2))
    H7a, r7a, root7a, c7a = fixed_R_arrays(7, (0, 1), (0, 2))
    p6a = partition_counts(H6a, r6a, root6a, c6a, 7)
    p7a = partition_counts(H7a, r7a, root7a, c7a, 7)
    assert p6a == Counter({(7,): 82, (4, 3): 30})
    assert p7a == Counter({(7,): 918, (4, 3): 396})

    assert sum(p6a.values()) + sum(p6d.values()) + sum(p7a.values()) + sum(p7d.values()) == 5926
    print("R=7 n=6 adjacent:", dict(p6a))
    print("R=7 n=6 disjoint:", dict(p6d))
    print("R=7 n=7 adjacent:", dict(p7a))
    print("R=7 n=7 disjoint:", dict(p7d))
    print("TOTAL VERIFIED R=7 INSTANCES: 5926")
    print("ALL HARD10-01 R=6 WHEEL / R=7 EXACT CHECKS PASSED")
