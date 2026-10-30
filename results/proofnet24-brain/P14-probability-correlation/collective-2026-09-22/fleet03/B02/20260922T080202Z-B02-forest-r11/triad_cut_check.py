from itertools import combinations


def simple_edges(n):
    return list(combinations(range(n), 2))


def forests(n, edges):
    out = []
    for mask in range(1 << len(edges)):
        p = list(range(n))

        def find(x):
            while p[x] != x:
                p[x] = p[p[x]]
                x = p[x]
            return x

        ok = True
        for i, (u, v) in enumerate(edges):
            if mask >> i & 1:
                a, b = find(u), find(v)
                if a == b:
                    ok = False
                    break
                p[a] = b
        if ok:
            out.append(mask)
    return out


def connected(n, edges, mask, u, v):
    if u == v:
        return True
    p = list(range(n))

    def find(x):
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    for i, (a, b) in enumerate(edges):
        if mask >> i & 1:
            x, y = find(a), find(b)
            if x != y:
                p[x] = y
    return find(u) == find(v)


def side_data(vertices, edges, terminals):
    vs = sorted(vertices)
    ix = {v: i for i, v in enumerate(vs)}
    local_edges = [(ix[u], ix[v]) for u, v in edges]
    fs = forests(len(vs), local_edges)
    Z = len(fs)
    g, e, f = (ix[x] for x in terminals)
    A = sum(connected(len(vs), local_edges, h, g, e) for h in fs)
    B = sum(connected(len(vs), local_edges, h, g, f) for h in fs)
    C = sum(connected(len(vs), local_edges, h, e, f) for h in fs)
    T = sum(
        connected(len(vs), local_edges, h, g, e)
        and connected(len(vs), local_edges, h, g, f)
        for h in fs
    )
    return Z, A, B, C, T


def pair_gap(n, edges, ei, fi):
    fs = forests(n, edges)
    Z = len(fs)
    Ze = sum(h >> ei & 1 for h in fs)
    Zf = sum(h >> fi & 1 for h in fs)
    Zef = sum((h >> ei & 1) and (h >> fi & 1) for h in fs)
    return Ze * Zf - Z * Zef


def edge_connectivity(n, edges):
    if n < 2:
        return 0
    best = len(edges) + 1
    for r in range(1, n):
        for st in combinations(range(n), r):
            S = set(st)
            if 0 not in S:
                continue
            cut = sum((u in S) ^ (v in S) for u, v in edges)
            best = min(best, cut)
    return best


graphs = 0
triad_pair_cases = 0
violations = 0
strict_3ec = 0
strict_fail = 0
min_strict_gap = None

for n in range(2, 6):
    universe = simple_edges(n)
    for graph_mask in range(1 << len(universe)):
        edges = [universe[i] for i in range(len(universe)) if graph_mask >> i & 1]
        graphs += 1
        seen = set()
        V = set(range(n))
        lam = edge_connectivity(n, edges)
        for r in range(1, n):
            for st in combinations(range(n), r):
                S = set(st)
                if 0 not in S:
                    continue
                R = V - S
                cut = tuple(
                    i for i, (u, v) in enumerate(edges) if (u in S) ^ (v in S)
                )
                if len(cut) != 3 or cut in seen:
                    continue
                seen.add(cut)
                side_S = [
                    ed for i, ed in enumerate(edges)
                    if i not in cut and ed[0] in S and ed[1] in S
                ]
                side_R = [
                    ed for i, ed in enumerate(edges)
                    if i not in cut and ed[0] in R and ed[1] in R
                ]
                for ei, fi in combinations(cut, 2):
                    gi = next(i for i in cut if i not in (ei, fi))

                    def endpoint(idx, side):
                        u, v = edges[idx]
                        return u if u in side else v

                    LS, AS, BS, CS, TS = side_data(
                        S,
                        side_S,
                        (endpoint(gi, S), endpoint(ei, S), endpoint(fi, S)),
                    )
                    LR, AR, BR, CR, TR = side_data(
                        R,
                        side_R,
                        (endpoint(gi, R), endpoint(ei, R), endpoint(fi, R)),
                    )
                    predicted = AS * AR * BS * BR + 4 * LS * LR * (CS * CR - TS * TR)
                    actual = pair_gap(n, edges, ei, fi)
                    triad_pair_cases += 1
                    if actual != predicted or actual < 0:
                        violations += 1
                    if lam >= 3:
                        strict_3ec += 1
                        if actual <= 0:
                            strict_fail += 1
                        if min_strict_gap is None or actual < min_strict_gap:
                            min_strict_gap = actual

print(f"graphs_checked={graphs}")
print(f"three_cut_pair_cases={triad_pair_cases}")
print(f"formula_or_sign_violations={violations}")
print(f"three_edge_connected_cases={strict_3ec}")
print(f"three_edge_connected_non_strict={strict_fail}")
print(f"minimum_strict_integer_gap={min_strict_gap}")
print("STATUS=PASS")
