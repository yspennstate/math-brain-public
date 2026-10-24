from itertools import combinations


def closure(n, edges):
    r = [[False] * n for _ in range(n)]
    for i, j in edges:
        r[i][j] = True
    for k in range(n):
        for i in range(n):
            if r[i][k]:
                for j in range(n):
                    if r[k][j]:
                        r[i][j] = True
    return r


def reach_key(r):
    n = len(r)
    return tuple((i, j) for i in range(n) for j in range(n) if r[i][j])


def linexts(r):
    n = len(r)
    pred = [0] * n
    for v in range(n):
        for u in range(n):
            if r[u][v]:
                pred[v] |= 1 << u
    full = (1 << n) - 1
    out = []

    def rec(mask, order):
        if mask == full:
            out.append(tuple(order))
            return
        for v in range(n):
            bit = 1 << v
            if not (mask & bit) and pred[v] & ~mask == 0:
                rec(mask | bit, order + [v])

    rec(0, [])
    return out


def relation_sets(r, v):
    n = len(r)
    return (
        {u for u in range(n) if r[u][v]},
        {u for u in range(n) if r[v][u]},
    )


def check_pair(r, exts, a, b):
    pa, sa = relation_sets(r, a)
    pb, sb = relation_sets(r, b)
    da = pa - pb
    db = pb - pa
    ua = sa - sb
    ub = sb - sa
    nba = nab = bminus = bplus = 0
    for order in exts:
        pos = {v: i for i, v in enumerate(order)}
        if pos[b] < pos[a]:
            nba += 1
        else:
            nab += 1
        bm = any(pos[b] < pos[d] for d in da) or any(pos[u] < pos[a] for u in ub)
        bp = any(pos[a] < pos[d] for d in db) or any(pos[u] < pos[b] for u in ua)
        bminus += int(bm)
        bplus += int(bp)
    assert nba - nab == bminus - bplus
    return nba, nab, bminus, bplus


# Exhaust every transitively closed relation compatible with 0<1<...<4.
n = 5
upper = list(combinations(range(n), 2))
seen = {}
for mask in range(1 << len(upper)):
    edges = [upper[k] for k in range(len(upper)) if (mask >> k) & 1]
    r = closure(n, edges)
    seen[reach_key(r)] = r

ordered_incomparable_pairs = 0
aligned_pairs = 0
for r in seen.values():
    exts = linexts(r)
    for a in range(n):
        for b in range(n):
            if a == b or r[a][b] or r[b][a]:
                continue
            nba, nab, bminus, bplus = check_pair(r, exts, a, b)
            ordered_incomparable_pairs += 1
            pa, sa = relation_sets(r, a)
            pb, sb = relation_sets(r, b)
            if not (pb - pa) and not (sa - sb):
                assert bplus == 0
                assert nba - nab == bminus
                aligned_pairs += 1

# Exact 15-point sharp two-distinguisher witness from account02/B19.
covers = [
    (0, 1), (0, 10), (1, 2), (2, 3), (2, 12), (3, 4), (3, 9),
    (5, 6), (6, 2), (6, 11), (7, 3), (7, 8), (7, 13), (8, 4),
    (8, 9), (9, 14), (10, 6), (11, 7), (11, 12), (12, 8),
    (12, 13), (13, 4), (13, 14),
]
r = closure(15, covers)
exts = linexts(r)
assert len(exts) == 1810
a, b, d, u = 13, 3, 12, 9
pa, sa = relation_sets(r, a)
pb, sb = relation_sets(r, b)
assert pa - pb == {d}
assert pb - pa == set()
assert sb - sa == {u}
assert sa - sb == set()

nab = sum(order.index(a) < order.index(b) for order in exts)
nba = len(exts) - nab
lower = sum(order.index(b) < order.index(d) for order in exts)
upper = sum(order.index(u) < order.index(a) for order in exts)
both = sum(
    (order.index(b) < order.index(d)) and (order.index(u) < order.index(a))
    for order in exts
)
union = lower + upper - both
assert (nab, nba) == (603, 1207)
assert (lower, upper, both, union) == (336, 352, 84, 604)
assert nba - nab == union

print("unique_five_point_posets", len(seen))
print("ordered_incomparable_pairs_checked", ordered_incomparable_pairs)
print("aligned_pairs_checked", aligned_pairs)
print("sharp_E", len(exts))
print("sharp_N_a_before_b", nab)
print("sharp_N_b_before_a", nba)
print("sharp_lower_blocker", lower)
print("sharp_upper_blocker", upper)
print("sharp_intersection", both)
print("sharp_union", union)
print("sharp_signed_defect", nba - nab)
print("POS3_BLOCKER_EXCHANGE_IDENTITY_PASS")
