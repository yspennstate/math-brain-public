import itertools, json


def closure_from_edges(n, emask):
    reach = [0] * n
    bit = 0
    for i in range(n):
        for j in range(i + 1, n):
            if emask >> bit & 1:
                reach[i] |= 1 << j
            bit += 1
    for k in range(n - 1, -1, -1):
        rk = reach[k]
        for i in range(k):
            if (reach[i] >> k) & 1:
                reach[i] |= rk
    return tuple(reach)


def comparable(reach, i, j):
    if i < j:
        return (reach[i] >> j) & 1
    if j < i:
        return (reach[j] >> i) & 1
    return False


def width(reach, n):
    best = 0
    for mask in range(1, 1 << n):
        pc = mask.bit_count()
        if pc <= best:
            continue
        xs = [i for i in range(n) if mask >> i & 1]
        if all(not comparable(reach, xs[a], xs[b])
               for a in range(len(xs)) for b in range(a + 1, len(xs))):
            best = pc
    return best


def linexts(reach, n):
    preds = [0] * n
    for i in range(n):
        for j in range(i + 1, n):
            if (reach[i] >> j) & 1:
                preds[j] |= 1 << i
    out = []

    def rec(mask, perm):
        if mask == (1 << n) - 1:
            out.append(tuple(perm))
            return
        for v in range(n):
            if mask >> v & 1:
                continue
            if preds[v] & ~mask:
                continue
            rec(mask | 1 << v, perm + [v])

    rec(0, [])
    return out


def acyclic(adj, n):
    indeg = [0] * n
    for i in range(n):
        for j in range(n):
            if adj[i] >> j & 1:
                indeg[j] += 1
    stack = [i for i, d in enumerate(indeg) if d == 0]
    seen = 0
    while stack:
        v = stack.pop()
        seen += 1
        for j in range(n):
            if adj[v] >> j & 1:
                indeg[j] -= 1
                if indeg[j] == 0:
                    stack.append(j)
    return seen == n


def check_n(n):
    npairs = n * (n - 1) // 2
    closures = {closure_from_edges(n, mask) for mask in range(1 << npairs)}
    kept = []
    failures = []
    nonchain = 0
    max_e = 0
    for reach in closures:
        if width(reach, n) > 3:
            continue
        kept.append(reach)
        extensions = linexts(reach, n)
        E = len(extensions)
        max_e = max(max_e, E)
        if any(not comparable(reach, i, j)
               for i in range(n) for j in range(i + 1, n)):
            nonchain += 1
        positions = []
        for extension in extensions:
            pos = [0] * n
            for rank, vertex in enumerate(extension):
                pos[vertex] = rank
            positions.append(pos)
        adj = [0] * n
        for i in range(n):
            for j in range(i + 1, n):
                if (reach[i] >> j) & 1:
                    adj[i] |= 1 << j
                else:
                    cij = sum(pos[i] < pos[j] for pos in positions)
                    if 3 * cij > 2 * E:
                        adj[i] |= 1 << j
                    elif 3 * (E - cij) > 2 * E:
                        adj[j] |= 1 << i
        if not acyclic(adj, n):
            failures.append((reach, E, adj))
            if len(failures) >= 3:
                break
    return {
        "n": n,
        "unique_transitive_closures": len(closures),
        "width_le_3": len(kept),
        "width_le_3_nonchains": nonchain,
        "max_linear_extensions": max_e,
        "acyclicity_failures": len(failures),
    }, failures


results = []
all_failures = []
for n in range(2, 7):
    result, failures = check_n(n)
    results.append(result)
    all_failures.extend(failures)

rotations = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]


def before(a, b):
    return sum(p.index(a) < p.index(b) for p in rotations)


sharpness = {
    "0<1": before(0, 1),
    "1<2": before(1, 2),
    "2<0": before(2, 0),
    "den": 3,
}
assert sharpness["0<1"] == sharpness["1<2"] == sharpness["2<0"] == 2
assert not all_failures, all_failures[:1]

print(json.dumps({"finite_census": results, "threshold_sharpness": sharpness},
                 sort_keys=True, indent=2))
print("POS3_B19_AUGMENTED_ORDER_ACYCLICITY_PASS")
