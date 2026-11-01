#!/usr/bin/env python3
"""
HARD10-01 exact finite adversarial checks for the 2026-09-15T17:15:24Z report.

Standard library only.

Part A: fixed disjoint pair e=(0,1), f=(2,3) on seven labelled vertices.
Enumerate every simple graph containing e,f.  For every graph with |R|=4
and four minimal R-roots, verify:
  * a nonterminal two-vertex separator separates e from f;
  * the exact unit-weight two-separation factorization
        Delta_G = alpha_K(e;s,t) alpha_L(f;s,t);
  * the exact gap distribution is 72 graphs with gap 72 and 6 with gap 36.

Part B: classify the root-fiber partitions for |R|=5 through the bounded
families used in the report:
  * n=6 adjacent and disjoint representative pairs;
  * n=7 adjacent and disjoint representative pairs.
Every such graph must have partition (4,1) in these finite checks.

These computations are adversarial checks only.  They are not proof
dependencies for the universal separator theorem.
"""

from collections import Counter
from itertools import combinations


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for a, b in edges:
        ra, rb = find(a), find(b)
        if ra == rb:
            return False
        if rank[ra] < rank[rb]:
            ra, rb = rb, ra
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
    return True


def zeta(a, m):
    z = a[:]
    for i in range(m):
        bit = 1 << i
        for mask in range(1 << m):
            if mask & bit:
                z[mask] += z[mask ^ bit]
    return z


def fixed_arrays(n, e, f, need_classes=False):
    all_edges = list(combinations(range(n), 2))
    H = [g for g in all_edges if g not in (e, f)]
    m = len(H)
    N = 1 << m
    r = [0] * N
    root = [0] * N
    raw = {k: [0] * N for k in ("N0", "Ne", "Nf", "B", "R")} if need_classes else None

    for mask in range(N):
        A = [H[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        eok = is_forest(n, A + [e])
        fok = is_forest(n, A + [f])
        efok = is_forest(n, A + [e, f])
        if not eok and not fok:
            kind = "N0"
        elif eok and not fok:
            kind = "Ne"
        elif fok and not eok:
            kind = "Nf"
        elif efok:
            kind = "B"
        else:
            kind = "R"
            r[mask] = 1
        if raw is not None:
            raw[kind][mask] = 1

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

    out = {
        "H": H,
        "r": r,
        "root": root,
        "Rcnt": zeta(r, m),
        "rootcnt": zeta(root, m),
    }
    if raw is not None:
        out["Z"] = {k: zeta(v, m) for k, v in raw.items()}
    return out


def edges_from_mask(H, mask):
    return [H[i] for i in range(len(H)) if (mask >> i) & 1]


def components_after_deleting(n, edges, s, t):
    rem = set(range(n)) - {s, t}
    adj = {v: [] for v in rem}
    for a, b in edges:
        if a in rem and b in rem:
            adj[a].append(b)
            adj[b].append(a)
    comp = {}
    cid = 0
    for v in rem:
        if v in comp:
            continue
        stack = [v]
        comp[v] = cid
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in comp:
                    comp[y] = cid
                    stack.append(y)
        cid += 1
    return comp


def proper_separator(n, edges, e, f):
    terminals = set(e) | set(f)
    for s, t in combinations([v for v in range(n) if v not in terminals], 2):
        comp = components_after_deleting(n, edges, s, t)
        if (
            comp[e[0]] == comp[e[1]]
            and comp[f[0]] == comp[f[1]]
            and comp[e[0]] != comp[f[0]]
        ):
            return s, t, comp
    return None


def alpha_unit(vertices, edges, distinguished, s, t):
    edges = list(edges)
    ie = edges.index(distinguished)
    D = C = De = Ce = 0
    for mask in range(1 << len(edges)):
        A = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(max(vertices) + 1, A):
            continue
        parent = {v: v for v in vertices}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for a, b in A:
            ra, rb = find(a), find(b)
            if ra != rb:
                parent[rb] = ra
        connected = find(s) == find(t)
        has = (mask >> ie) & 1
        if connected:
            C += 1
            Ce += has
        else:
            D += 1
            De += has
    return D * Ce - C * De


def rayleigh_gap(n, edges, e, f):
    edges = list(edges)
    ie = edges.index(e)
    jf = edges.index(f)
    Z = Ze = Zf = Zef = 0
    for mask in range(1 << len(edges)):
        A = [edges[i] for i in range(len(edges)) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        se = (mask >> ie) & 1
        sf = (mask >> jf) & 1
        Z += 1
        Ze += se
        Zf += sf
        Zef += se * sf
    return Ze * Zf - Z * Zef


def split_at_separator(n, edges, e, f, s, t, comp):
    ce = comp[e[0]]
    cf = comp[f[0]]
    assert ce != cf
    VK = {s, t} | {v for v, c in comp.items() if c != cf}
    VL = {s, t} | {v for v, c in comp.items() if c == cf}
    st = (s, t) if s < t else (t, s)
    K, L = [], []
    for g in edges:
        a, b = g
        if g == st:
            K.append(g)  # assign a possible separator edge to one side
        elif a in VK and b in VK:
            K.append(g)
        elif a in VL and b in VL:
            L.append(g)
        else:
            raise AssertionError(("bypass edge", g, s, t))
    assert e in K and f in L
    return VK, VL, K, L


def roots_and_fibers(M, r_masks):
    Rs = [A for A in r_masks if (A & ~M) == 0]
    roots = [P for P in Rs if not any(Q != P and (Q & ~P) == 0 for Q in Rs)]
    fibers = {P: [A for A in Rs if (P & ~A) == 0] for P in roots}
    return Rs, roots, fibers


def part_a_r4_separators():
    n = 7
    e, f = (0, 1), (2, 3)
    data = fixed_arrays(n, e, f, need_classes=False)
    H = data["H"]
    Rcnt = data["Rcnt"]
    rootcnt = data["rootcnt"]

    count = 0
    gap_counter = Counter()
    for M in range(1 << len(H)):
        if Rcnt[M] != 4 or rootcnt[M] != 4:
            continue
        count += 1
        edges = [e, f] + edges_from_mask(H, M)
        sep = proper_separator(n, edges, e, f)
        assert sep is not None
        s, t, comp = sep
        VK, VL, K, L = split_at_separator(n, edges, e, f, s, t, comp)
        aK = alpha_unit(VK, K, e, s, t)
        aL = alpha_unit(VL, L, f, s, t)
        delta = rayleigh_gap(n, edges, e, f)
        assert delta == aK * aL
        gap_counter[delta] += 1

    assert count == 78
    assert gap_counter == Counter({72: 72, 36: 6})
    print("n=7 disjoint all-minimal |R|=4:", count)
    print("gap distribution:", gap_counter)
    print("all have proper separator and exact Delta=alpha_K*alpha_L")


def r5_partition_stats(n, e, f):
    data = fixed_arrays(n, e, f, need_classes=False)
    H, r = data["H"], data["r"]
    Rcnt = data["Rcnt"]
    r_masks = [i for i, v in enumerate(r) if v]
    stats = Counter()
    total = 0
    for M in range(1 << len(H)):
        if Rcnt[M] != 5:
            continue
        total += 1
        Rs, roots, fibers = roots_and_fibers(M, r_masks)
        assert len(Rs) == 5
        part = tuple(sorted((len(fibers[P]) for P in roots), reverse=True))
        stats[part] += 1
    return total, stats


def part_b_r5():
    checks = [
        (6, (0, 1), (0, 2), 99),
        (6, (0, 1), (2, 3), 288),
        (7, (0, 1), (0, 2), 1108),
        (7, (0, 1), (2, 3), 5040),
    ]
    for n, e, f, expected in checks:
        total, stats = r5_partition_stats(n, e, f)
        assert total == expected
        assert stats == Counter({(4, 1): expected})
        print(f"n={n}, e={e}, f={f}: |R|=5 graphs={total}, partitions={stats}")


def main():
    part_a_r4_separators()
    part_b_r5()
    print("ALL EXACT HARD10-01 R4/R5 CHECKS PASSED")


if __name__ == "__main__":
    main()
