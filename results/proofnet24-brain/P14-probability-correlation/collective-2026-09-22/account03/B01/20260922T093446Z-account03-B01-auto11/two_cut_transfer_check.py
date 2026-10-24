from itertools import combinations


def is_forest(n, es):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for u, v in es:
        a, b = find(u), find(v)
        if a == b:
            return False
        p[a] = b
    return True


def connected(n, es):
    if n == 0:
        return True
    adj = [[] for _ in range(n)]
    for u, v in es:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def counts(n, edges, e, f):
    z = ze = zf = zef = 0
    m = len(edges)
    for mask in range(1 << m):
        F = [edges[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, F):
            continue
        z += 1
        ae = e in F
        af = f in F
        ze += ae
        zf += af
        zef += ae and af
    return z, ze, zf, zef


def gap(n, edges, e, f):
    z, ze, zf, zef = counts(n, edges, e, f)
    return ze * zf - z * zef


def bridge_sides(n, edges, g):
    rem = [h for h in edges if h != g]
    adj = [[] for _ in range(n)]
    for u, v in rem:
        adj[u].append(v)
        adj[v].append(u)
    seen = {g[0]}
    stack = [g[0]]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return seen, set(range(n)) - seen


def crosses(edge, A):
    return (edge[0] in A) ^ (edge[1] in A)


def side_stats(vertices, internal_edges, mark, b1, b2):
    vs = sorted(vertices)
    ix = {v: i for i, v in enumerate(vs)}
    ed = [(ix[u], ix[v]) for u, v in internal_edges]
    mk = (ix[mark[0]], ix[mark[1]])
    z = c = em = ec = 0
    m = len(ed)
    for mask in range(1 << m):
        F = [ed[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(len(vs), F):
            continue
        z += 1
        has = mk in F
        em += has
        if b1 == b2:
            conn = True
        else:
            p = list(range(len(vs)))

            def find(x):
                while p[x] != x:
                    p[x] = p[p[x]]
                    x = p[x]
                return x

            for u, v in F:
                a, b = find(u), find(v)
                p[a] = b
            conn = find(ix[b1]) == find(ix[b2])
        c += conn
        ec += conn and has
    return z, c, em, ec


bridge_checks = 0
for n in range(3, 6):
    E = list(combinations(range(n), 2))
    for mask in range(1 << len(E)):
        edges = [E[i] for i in range(len(E)) if (mask >> i) & 1]
        if len(edges) < 3:
            continue
        for e, f in combinations(edges, 2):
            G0 = [h for h in edges if h not in (e, f)]
            if not connected(n, G0):
                continue
            for g in G0:
                A, B = bridge_sides(n, G0, g)
                if g[1] in A:
                    continue
                for mark, other in ((e, f), (f, e)):
                    if crosses(mark, A) and not crosses(other, A):
                        assert gap(n, edges, mark, other) == gap(n, edges, g, other)
                        bridge_checks += 1


twocut_checks = 0
for n in range(4, 6):
    E = list(combinations(range(n), 2))
    V = set(range(n))
    for mask in range(1 << len(E)):
        edges = [E[i] for i in range(len(E)) if (mask >> i) & 1]
        if len(edges) < 4:
            continue
        for r in range(1, n):
            for At in combinations(range(n), r):
                A = set(At)
                if 0 not in A or A == V:
                    continue
                cut = [h for h in edges if crosses(h, A)]
                if len(cut) != 2:
                    continue
                g, h = cut
                B = V - A

                def orient(x):
                    u, v = x
                    return (u, v) if u in A else (v, u)

                ag, bg = orient(g)
                ah, bh = orient(h)
                EA = [x for x in edges if x not in cut and x[0] in A and x[1] in A]
                EB = [x for x in edges if x not in cut and x[0] in B and x[1] in B]
                for e in EA:
                    for f in EB:
                        ZL, CL, EL, ECL = side_stats(A, EA, e, ag, ah)
                        ZR, CR, FR, FCR = side_stats(B, EB, f, bg, bh)
                        AL = CL * EL - ECL * ZL
                        AR = CR * FR - FCR * ZR
                        assert gap(n, edges, e, f) == 4 * AL * AR
                        assert gap(n, edges, e, g) == -2 * CR * ZR * AL
                        assert gap(n, edges, f, g) == -2 * CL * ZL * AR
                        twocut_checks += 1

print(f"BRIDGE_TRANSFER_CONFIGS={bridge_checks}")
print(f"TWO_CUT_SEPARATED_MARK_CONFIGS={twocut_checks}")
print("ALL_EXACT_ASSERTIONS_PASSED")
