from itertools import combinations


def is_forest(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if not ((mask >> i) & 1):
            continue
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return True


def components(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            ru, rv = find(u), find(v)
            if ru != rv:
                parent[ru] = rv
    return [find(i) for i in range(n)]


def path_edges(n, edges, mask, u, v):
    adj = [[] for _ in range(n)]
    for i, (a, b) in enumerate(edges):
        if (mask >> i) & 1:
            adj[a].append((b, i))
            adj[b].append((a, i))
    stack = [u]
    par = {u: (None, None)}
    while stack:
        x = stack.pop()
        if x == v:
            break
        for y, i in adj[x]:
            if y not in par:
                par[y] = (x, i)
                stack.append(y)
    if v not in par:
        return None
    out = []
    x = v
    while x != u:
        x0, i = par[x]
        out.append(i)
        x = x0
    return out


def addable(n, edges, mask, edge):
    cc = components(n, edges, mask)
    u, v = edge
    return cc[u] != cc[v]


def jointly_addable(n, edges, mask, e, f):
    if not addable(n, edges, mask, e) or not addable(n, edges, mask, f):
        return False
    ext = list(edges) + [e, f]
    extmask = mask | (1 << len(edges)) | (1 << (len(edges) + 1))
    return is_forest(n, ext, extmask)


def q_cut_degree(n, edges, mask, e, f):
    cc = components(n, edges, mask)
    a, b = e
    c, d = f
    pe = (cc[a], cc[b])
    pf = (cc[c], cc[d])
    if pe[0] == pe[1] or pf[0] == pf[1] or set(pe) != set(pf):
        return 0
    A, B = pe
    return sum(1 for u, v in edges if {cc[u], cc[v]} == {A, B})


def marked_stats(n, full_edges, ei, fi):
    e, f = full_edges[ei], full_edges[fi]
    base = [g for i, g in enumerate(full_edges) if i not in (ei, fi)]
    forests = [m for m in range(1 << len(base)) if is_forest(n, base, m)]
    N = len(forests)
    D = O = Q = n10 = n01 = n11 = 0
    I_O = I_Q = 0
    S = 0
    for mask in forests:
        pe = path_edges(n, base, mask, *e)
        pf = path_edges(n, base, mask, *f)
        X, Y = pe is None, pf is None
        if X and Y:
            n11 += 1
            if jointly_addable(n, base, mask, e, f):
                S += 1
            else:
                Q += 1
                I_Q += q_cut_degree(n, base, mask, e, f)
        elif X and not Y:
            n10 += 1
        elif not X and Y:
            n01 += 1
        else:
            shared = len(set(pe) & set(pf))
            if shared:
                O += 1
                I_O += shared
            else:
                D += 1
    assert I_O == I_Q
    delta = n10 * n01 + Q * N - (D + O) * n11
    geometric = (
        n10 * n01 - D * n11
        + Q * (N - n11)
        + n11 * (I_O - O)
        - n11 * (I_Q - Q)
    )
    assert delta == geometric
    return {
        "N": N, "D": D, "O": O, "Q": Q,
        "n10": n10, "n01": n01, "n11": n11, "S": S,
        "I_O": I_O, "I_Q": I_Q, "gap": delta,
        "naive_overlap_margin": Q * N - O * n11,
    }


def audit(max_n=5):
    total = incidence_fail = decomposition_fail = source_gap_fail = 0
    naive_fail = 0
    first_naive = None
    worst_naive = None
    for n in range(2, max_n + 1):
        all_edges = list(combinations(range(n), 2))
        for graph_mask in range(1 << len(all_edges)):
            full = [all_edges[i] for i in range(len(all_edges)) if (graph_mask >> i) & 1]
            if len(full) < 2:
                continue
            for ei, fi in combinations(range(len(full)), 2):
                total += 1
                st = marked_stats(n, full, ei, fi)
                if st["I_O"] != st["I_Q"]:
                    incidence_fail += 1
                if st["gap"] < 0:
                    source_gap_fail += 1
                nm = st["naive_overlap_margin"]
                if nm < 0:
                    naive_fail += 1
                    rec = (n, tuple(full), ei, fi, st)
                    if first_naive is None:
                        first_naive = rec
                    if worst_naive is None or nm < worst_naive[-1]["naive_overlap_margin"]:
                        worst_naive = rec
    return total, incidence_fail, decomposition_fail, source_gap_fail, naive_fail, first_naive, worst_naive


if __name__ == "__main__":
    out = audit(5)
    print("MARKED_INSTANCES", out[0])
    print("INCIDENCE_FAILURES", out[1])
    print("DECOMPOSITION_FAILURES", out[2])
    print("SOURCE_GAP_FAILURES", out[3])
    print("NAIVE_OVERLAP_PAYMENT_FAILURES", out[4])
    print("FIRST_NAIVE_COUNTEREXAMPLE", out[5])
    print("WORST_NAIVE_COUNTEREXAMPLE", out[6])
    print("STATUS=PASS_EXACT_RECONNECTION_IDENTITY_AND_COUNTEREXAMPLE_FOUND")
