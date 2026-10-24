from itertools import combinations
from collections import Counter, defaultdict, deque


def forest_components(n, edges, mask):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for i, (u, v) in enumerate(edges):
        if mask >> i & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return None
            parent[rv] = ru
    for i in range(n):
        parent[i] = find(i)
    return parent


def precompute_R(n, e, f):
    H = [x for x in combinations(range(n), 2) if x not in (e, f)]
    rind = bytearray(1 << len(H))
    a, b = e
    c, d = f
    for mask in range(1 << len(H)):
        comp = forest_components(n, H, mask)
        if comp is None:
            continue
        ra, rb, rc, rd = comp[a], comp[b], comp[c], comp[d]
        if ra == rb or rc == rd:
            continue
        if rc in (ra, rb) and rd in (ra, rb) and rc != rd:
            rind[mask] = 1
    return H, rind


def zeta_counts(rind, m):
    a = list(rind)
    for i in range(m):
        bit = 1 << i
        for s in range(1 << m):
            if s & bit:
                a[s] += a[s ^ bit]
    return a


def r_subsets(M, rind):
    out = []
    s = M
    while True:
        if rind[s]:
            out.append(s)
        if s == 0:
            break
        s = (s - 1) & M
    return out


def classify(M, rind):
    R = r_subsets(M, rind)
    roots = [a for a in R if not any(b != a and (b & a) == b for b in R)]
    fib = {p: [a for a in R if (a & p) == p] for p in roots}
    part = tuple(sorted((len(fib[p]) for p in roots), reverse=True))
    return part, roots, fib, R


def edges(mask, H):
    return [H[i] for i in range(len(H)) if mask >> i & 1]


def profile(p, F):
    return Counter((a & ~p).bit_count() for a in F)


def atom_idx(p, F):
    return [(a & ~p).bit_length() - 1 for a in F if (a & ~p).bit_count() == 1]


def cycle_edges(p, H, e, f):
    return edges(p, H) + [e, f]


def bridge(n, graph, h):
    a, b = h
    adj = defaultdict(list)
    removed = False
    for ed in graph:
        if ed == h and not removed:
            removed = True
            continue
        u, v = ed
        adj[u].append(v)
        adj[v].append(u)
    seen = {a}
    st = [a]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    return b not in seen


def path_vertices(start, end, eds):
    adj = defaultdict(list)
    for u, v in eds:
        adj[u].append(v)
        adj[v].append(u)
    prev = {start: None}
    q = deque([start])
    while q:
        u = q.popleft()
        if u == end:
            break
        for v in adj[u]:
            if v not in prev:
                prev[v] = u
                q.append(v)
    assert end in prev
    p = []
    x = end
    while x is not None:
        p.append(x)
        x = prev[x]
    return p[::-1]


def forest_counts(n, graph, e, f):
    ei = graph.index(e)
    fi = graph.index(f)
    Z = Ze = Zf = Zef = 0
    for m in range(1 << len(graph)):
        if forest_components(n, graph, m) is None:
            continue
        Z += 1
        he = (m >> ei) & 1
        hf = (m >> fi) & 1
        Ze += he
        Zf += hf
        Zef += he & hf
    return Z, Ze, Zf, Zef, Ze * Zf - Z * Zef


def terminal_response(n, K, q, s, t):
    qi = K.index(q)
    D = C = Dq = Cq = 0
    for m in range(1 << len(K)):
        comp = forest_components(n, K, m)
        if comp is None:
            continue
        conn = comp[s] == comp[t]
        has = (m >> qi) & 1
        if conn:
            C += 1
            Cq += has
        else:
            D += 1
            Dq += has
    return D * Cq - C * Dq


def star_info(p, F, H):
    atoms = atom_idx(p, F)
    if len(atoms) != 3:
        return None
    deg = Counter()
    for i in atoms:
        u, v = H[i]
        deg[u] += 1
        deg[v] += 1
    ctr = [v for v, d in deg.items() if d == 3]
    if len(ctr) != 1:
        return None
    w = ctr[0]
    A = sorted(v if u == w else u for u, v in (H[i] for i in atoms))
    return w, A, atoms


def check_pair(n, e, f):
    H, rind = precompute_R(n, e, f)
    z = zeta_counts(rind, len(H))
    type_counts = Counter()
    square_checks = 0
    star_checks = 0
    star_triples = Counter()

    for M, cnt in enumerate(z):
        if cnt != 8:
            continue
        part, roots, fib, R = classify(M, rind)
        if part != (4, 4):
            continue
        profs = [profile(p, fib[p]) for p in roots]
        graph = [e, f] + edges(M, H)

        if all(p == Counter({0: 1, 1: 2, 2: 1}) for p in profs):
            type_counts["square-square"] += 1
            atomsets = [set(atom_idx(p, fib[p])) for p in roots]
            assert atomsets[0] == atomsets[1]
            A = atomsets[0]
            assert all(bridge(n, graph, H[i]) for i in A)
            M0 = M
            for i in A:
                M0 &= ~(1 << i)
            assert classify(M0, rind)[0] == (1, 1)
            square_checks += 1
            continue

        assert all(p == Counter({0: 1, 1: 3}) for p in profs)
        type_counts["star-star"] += 1
        P, Q = roots
        sP = star_info(P, fib[P], H)
        sQ = star_info(Q, fib[Q], H)
        assert sP and sQ
        w, A, _ = sP
        x, B, _ = sQ
        Peds = set(edges(P, H))
        Qeds = set(edges(Q, H))
        usedA = sorted(a for a in A if tuple(sorted((w, a))) in Qeds)
        usedB = sorted(b for b in B if tuple(sorted((x, b))) in Peds)
        assert len(usedA) == len(usedB) == 2

        # Structural conclusions proved in the report.
        assert A == B and usedA == usedB
        u, v = usedA
        z0 = list(set(A) - set(usedA))
        assert len(z0) == 1
        z0 = z0[0]

        # Recover the common u-v path R by deleting P's alternative center x.
        Rpath_edges = [ed for ed in cycle_edges(P, H, e, f) if x not in ed]
        path = path_vertices(u, v, Rpath_edges)
        assert z0 in path
        iz = path.index(z0)
        Uv = set(path[: iz + 1])
        Vv = set(path[iz:])

        core = {
            tuple(sorted(ed))
            for ed in [(w, u), (w, v), (w, z0), (x, u), (x, v), (x, z0)]
        }
        for ed in graph:
            sed = tuple(sorted(ed))
            if sed in core:
                continue
            assert set(ed) <= Uv or set(ed) <= Vv, (ed, path, graph)

        KU = [ed for ed in graph if set(ed) <= Uv]
        KV = [ed for ed in graph if set(ed) <= Vv]
        if e in KU and f in KV:
            aU = terminal_response(n, KU, e, u, z0)
            aV = terminal_response(n, KV, f, z0, v)
        elif f in KU and e in KV:
            aU = terminal_response(n, KU, f, u, z0)
            aV = terminal_response(n, KV, e, z0, v)
        else:
            raise AssertionError((e, f, path, KU, KV))

        gap = forest_counts(n, graph, e, f)[-1]
        assert gap == 160 * aU * aV, (gap, aU, aV, graph)
        star_triples[(aU, aV, gap)] += 1
        star_checks += 1

    return type_counts, square_checks, star_checks, star_triples


def l56_same_endpoint_witness():
    n = 6
    e = (0, 1)
    f = (2, 3)
    G = [e, f, (0, 3), (1, 4), (2, 4), (1, 5), (2, 5)]
    H, rind = precompute_R(n, e, f)
    M = sum(1 << H.index(ed) for ed in G if ed not in (e, f))
    part, roots, fib, R = classify(M, rind)
    assert part == (3, 3)

    # The ears 1-4-2 and 1-5-2 have the same endpoint pair {1,2}.
    # Suppressing both in a simple graph yields one edge (1,2).
    B = [e, f, (0, 3), (1, 2)]
    MB = sum(1 << H.index(ed) for ed in B if ed not in (e, f))
    assert classify(MB, rind)[0] == (1,)

    # Two parallel unit length-two paths: D=9, C=6.
    K = [(1, 4), (2, 4), (1, 5), (2, 5)]
    D = C = 0
    for m in range(1 << len(K)):
        comp = forest_components(n, K, m)
        if comp is None:
            continue
        if comp[1] == comp[2]:
            C += 1
        else:
            D += 1
    assert (D, C) == (9, 6)
    return part, forest_counts(n, G, e, f), classify(MB, rind)[0], (D, C)


def main():
    print("L56_same_endpoint_witness", l56_same_endpoint_witness())
    for n, e, f, label in [
        (6, (0, 1), (0, 2), "n6_adjacent"),
        (6, (0, 1), (2, 3), "n6_disjoint"),
        (7, (0, 1), (0, 2), "n7_adjacent"),
        (7, (0, 1), (2, 3), "n7_disjoint"),
    ]:
        tc, sq, st, tr = check_pair(n, e, f)
        print(label)
        print(" type_counts", dict(tc))
        print(" square_bridge_checks", sq)
        print(" star_wheel_checks", st)
        print(" star_factor_triples", dict(tr))


if __name__ == "__main__":
    main()
