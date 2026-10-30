from itertools import combinations


def components(n, edge_subset):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        p[b] = a
        return True

    acyclic = True
    for u, v in edge_subset:
        if not union(u, v):
            acyclic = False
            break
    return acyclic, [find(i) for i in range(n)]


def is_forest(n, subset):
    return components(n, subset)[0]


def connected(n, subset):
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            p[b] = a

    for u, v in subset:
        union(u, v)
    r = find(0)
    return all(find(i) == r for i in range(n))


def forests(n, edges):
    out = []
    m = len(edges)
    for mask in range(1 << m):
        s = [edges[i] for i in range(m) if (mask >> i) & 1]
        if is_forest(n, s):
            out.append(frozenset(s))
    return out


def spanning_trees(n, edges):
    if n == 1:
        return [frozenset()]
    return [frozenset(s) for s in combinations(edges, n - 1) if connected(n, s)]


def internal_active(n, edges, T, order_index):
    active = set()
    for g in T:
        rest = set(T)
        rest.remove(g)
        _, roots = components(n, list(rest))
        crossing = []
        for h in edges:
            u, v = h
            if roots[u] != roots[v]:
                crossing.append(h)
        if min(crossing, key=lambda h: order_index[h]) == g:
            active.add(g)
    return frozenset(active)


def addable(n, H, g):
    return is_forest(n, list(H | {g}))


def check_graph(n, edges):
    Fs = forests(n, edges)
    Ts = spanning_trees(n, edges)
    if not Ts:
        return True, 0, 0, None

    ordered_pairs = 0
    q_positive = 0
    for e in edges:
        for f in edges:
            if e == f:
                continue
            ordered_pairs += 1
            order = [e, f] + [g for g in edges if g not in (e, f)]
            order_index = {g: i for i, g in enumerate(order)}
            IA = {T: internal_active(n, edges, T, order_index) for T in Ts}
            w = {T: 1 << len(IA[T]) for T in Ts}
            W = sum(w.values())
            if W != len(Fs):
                return False, ordered_pairs, q_positive, ("partition_count", n, edges, e, f, W, len(Fs))

            owners = {}
            for T in Ts:
                base = T - IA[T]
                act = list(IA[T])
                for mask in range(1 << len(act)):
                    F = set(base)
                    for i, g in enumerate(act):
                        if (mask >> i) & 1:
                            F.add(g)
                    F = frozenset(F)
                    if F in owners:
                        return False, ordered_pairs, q_positive, ("cube_overlap", n, edges, e, f, F)
                    owners[F] = T
            if set(owners) != set(Fs):
                return False, ordered_pairs, q_positive, ("cube_cover", n, edges, e, f)

            base_edges = [g for g in edges if g not in (e, f)]
            Hs = forests(n, base_edges)
            q = 0
            for H in Hs:
                if addable(n, H, e) and addable(n, H, f) and not is_forest(n, list(H | {e, f})):
                    q += 1
            if q:
                q_positive += 1

            exchange_f = []
            for T in Ts:
                if f in T and e not in T:
                    Tp = frozenset((set(T) - {f}) | {e})
                    if Tp in Ts:
                        exchange_f.append(T)
                        if IA[Tp] != IA[T] | {e}:
                            return False, ordered_pairs, q_positive, (
                                "activity_exchange", n, edges, e, f, T, IA[T], Tp, IA[Tp]
                            )
            WA = sum(w[T] for T in exchange_f)
            if WA != q:
                return False, ordered_pairs, q_positive, ("q_bridge", n, edges, e, f, WA, q)

            exchange_e = []
            for Tp in Ts:
                if e in Tp and f not in Tp:
                    T = frozenset((set(Tp) - {e}) | {f})
                    if T in Ts:
                        exchange_e.append(Tp)
            WAE = sum(w[Tp] for Tp in exchange_e)
            if WAE != 2 * q:
                return False, ordered_pairs, q_positive, ("exchange_mass", n, edges, e, f, WAE, 2 * q)

            Ze = sum(1 for F in Fs if e in F)
            Zf = sum(1 for F in Fs if f in F)
            Zef = sum(1 for F in Fs if e in F and f in F)
            We = sum(w[T] for T in Ts if e in T)
            Wf = sum(w[T] for T in Ts if f in T)
            Wef = sum(w[T] for T in Ts if e in T and f in T)
            if We != 2 * Ze:
                return False, ordered_pairs, q_positive, ("Ze", n, edges, e, f, We, 2 * Ze)
            if Wef != 4 * Zef:
                return False, ordered_pairs, q_positive, ("Zef", n, edges, e, f, Wef, 4 * Zef)
            if Wf + q != 2 * Zf:
                return False, ordered_pairs, q_positive, ("Zf", n, edges, e, f, Wf, q, 2 * Zf)
            Delta = Ze * Zf - len(Fs) * Zef
            if We * (Wf + q) - W * Wef != 4 * Delta:
                return False, ordered_pairs, q_positive, ("Delta", n, edges, e, f)

    return True, ordered_pairs, q_positive, None


graphs = 0
ordered_pairs = 0
q_positive = 0
for n in range(2, 6):
    all_edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    for mask in range(1 << len(all_edges)):
        edges = [all_edges[i] for i in range(len(all_edges)) if (mask >> i) & 1]
        if len(edges) < max(1, n - 1) or not connected(n, edges):
            continue
        graphs += 1
        ok, op, qp, bad = check_graph(n, edges)
        ordered_pairs += op
        q_positive += qp
        if not ok:
            print("FAIL", bad)
            raise SystemExit(1)

print(f"connected_graphs_n2_to_n5={graphs}")
print(f"ordered_distinguished_pairs={ordered_pairs}")
print(f"q_positive_pairs={q_positive}")
print("identity_failures=0")
print("ALL_EXACT_CHECKS_PASSED")
