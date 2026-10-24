from itertools import combinations, permutations
from functools import lru_cache


def transitive_closure(n, rel_edges):
    reach = [0] * n
    for i, j in rel_edges:
        reach[i] |= 1 << j
    for k in range(n):
        mk = 1 << k
        for i in range(n):
            if reach[i] & mk:
                reach[i] |= reach[k]
    return tuple(reach)


def all_natural_posets(n):
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    seen = {}
    for mask in range(1 << len(pairs)):
        edges = [pairs[k] for k in range(len(pairs)) if (mask >> k) & 1]
        seen[transitive_closure(n, edges)] = None
    return list(seen.keys())


def incomparability_components(n, reach):
    def comparable(i, j):
        return bool((reach[i] >> j) & 1 or (reach[j] >> i) & 1)

    seen = [False] * n
    comps = []
    for s in range(n):
        if seen[s]:
            continue
        stack = [s]
        seen[s] = True
        comp = []
        while stack:
            u = stack.pop()
            comp.append(u)
            for v in range(n):
                if not seen[v] and u != v and not comparable(u, v):
                    seen[v] = True
                    stack.append(v)
        comps.append(tuple(sorted(comp)))
    return comps


def uniform_component_order(comps, reach):
    def lt(i, j):
        return bool((reach[i] >> j) & 1)

    directions = {}
    for a in range(len(comps)):
        for b in range(a + 1, len(comps)):
            vals = set()
            for x in comps[a]:
                for y in comps[b]:
                    if lt(x, y):
                        vals.add(1)
                    elif lt(y, x):
                        vals.add(-1)
                    else:
                        return None
            if len(vals) != 1:
                return None
            directions[a, b] = next(iter(vals))

    below = [0] * len(comps)
    for (a, b), value in directions.items():
        if value == 1:
            below[b] += 1
        else:
            below[a] += 1
    order = sorted(range(len(comps)), key=lambda x: below[x])
    for ii in range(len(order)):
        for jj in range(ii + 1, len(order)):
            A, B = order[ii], order[jj]
            for x in comps[A]:
                for y in comps[B]:
                    if not lt(x, y):
                        return None
    return order


def extension_count(vertices, reach):
    verts = tuple(sorted(vertices))
    m = len(verts)
    pred = [0] * m
    for j, v in enumerate(verts):
        for i, u in enumerate(verts):
            if (reach[u] >> v) & 1:
                pred[j] |= 1 << i

    @lru_cache(None)
    def dp(mask):
        if mask == (1 << m) - 1:
            return 1
        total = 0
        for j in range(m):
            if not (mask >> j) & 1 and pred[j] & ~mask == 0:
                total += dp(mask | (1 << j))
        return total

    return dp(0)


def linear_extensions(vertices, reach):
    verts = tuple(vertices)
    out = []
    for perm in permutations(verts):
        pos = {v: i for i, v in enumerate(perm)}
        ok = True
        for u in verts:
            r = reach[u]
            for v in verts:
                if ((r >> v) & 1) and pos[u] > pos[v]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(perm)
    return out


counts = []
bad = []
total = 0
for n in range(1, 7):
    posets = all_natural_posets(n)
    counts.append(len(posets))
    total += len(posets)
    for reach in posets:
        comps = incomparability_components(n, reach)
        if uniform_component_order(comps, reach) is None:
            bad.append(("uniform", n, reach))
            continue
        e_p = extension_count(range(n), reach)
        product = 1
        for comp in comps:
            product *= extension_count(comp, reach)
        if e_p != product:
            bad.append(("factor", n, reach, e_p, product))
print("counts_by_n", counts)
print("component_factorization", total, "checked;", len(bad), "failures")

prob_bad = []
prob_total = 0
for n in range(1, 6):
    for reach in all_natural_posets(n):
        prob_total += 1
        exts = linear_extensions(range(n), reach)
        e = len(exts)

        def comparable(i, j):
            return bool((reach[i] >> j) & 1 or (reach[j] >> i) & 1)

        b_p = None
        for i in range(n):
            for j in range(i + 1, n):
                if not comparable(i, j):
                    count = sum(perm.index(i) < perm.index(j) for perm in exts)
                    q = min(count / e, 1 - count / e)
                    b_p = q if b_p is None else max(b_p, q)

        component_values = []
        for comp in incomparability_components(n, reach):
            if len(comp) <= 1:
                continue
            comp_exts = linear_extensions(comp, reach)
            ce = len(comp_exts)
            b_c = 0
            for i, j in combinations(comp, 2):
                if not comparable(i, j):
                    count = sum(perm.index(i) < perm.index(j) for perm in comp_exts)
                    q = min(count / ce, 1 - count / ce)
                    b_c = max(b_c, q)
            component_values.append(b_c)
        rhs = max(component_values) if component_values else None
        if b_p is None and rhs is None:
            continue
        if abs(b_p - rhs) > 1e-12:
            prob_bad.append((n, reach, b_p, rhs))
print("probability_identity", prob_total, "checked;", len(prob_bad), "failures")
