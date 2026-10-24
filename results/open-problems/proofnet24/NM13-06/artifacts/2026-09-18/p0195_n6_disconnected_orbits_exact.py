from itertools import permutations
from functools import lru_cache
from collections import Counter, defaultdict

N = 6
E = [(i, j) for i in range(N) for j in range(i + 1, N)]
EI = {e: k for k, e in enumerate(E)}
PERMS = list(permutations(range(N)))

# Induced permutation on the 15 edge positions.
EDGE_MAPS = []
for p in PERMS:
    mp = []
    for a, b in E:
        u, v = sorted((p[a], p[b]))
        mp.append(EI[(u, v)])
    EDGE_MAPS.append(tuple(mp))


def pmask(m, mp):
    out = 0
    for k in range(len(E)):
        if (m >> k) & 1:
            out |= 1 << mp[k]
    return out


def components(m):
    A = [[] for _ in range(N)]
    for k, (a, b) in enumerate(E):
        if (m >> k) & 1:
            A[a].append(b)
            A[b].append(a)
    seen = set()
    cc = []
    for s in range(N):
        if s in seen:
            continue
        stack = [s]
        seen.add(s)
        C = []
        while stack:
            v = stack.pop()
            C.append(v)
            for w in A[v]:
                if w not in seen:
                    seen.add(w)
                    stack.append(w)
        cc.append(tuple(sorted(C)))
    return tuple(sorted(cc))


# Method A: enumerate the 156 unlabeled graph classes, then quotient absent
# edges under each source graph's exact automorphism group.
canon = {}
classes = []
for m in range(1 << len(E)):
    if m in canon:
        continue
    orbit = {pmask(m, mp) for mp in EDGE_MAPS}
    c = min(orbit)
    classes.append(c)
    for q in orbit:
        canon[q] = c

assert len(classes) == 156


@lru_cache(None)
def aut_maps(m):
    return tuple(mp for mp in EDGE_MAPS if pmask(m, mp) == m)


def marked_type(m, k):
    cc = components(m)
    if len(cc) == 1:
        return "connected_source"
    ci = {}
    for j, C in enumerate(cc):
        for v in C:
            ci[v] = j
    a, b = E[k]
    return "cross_components" if ci[a] != ci[b] else "within_component"


A_counts = Counter()
A_connected_by_edges = Counter()
A_marked = 0
for m in classes:
    absent = [k for k in range(len(E)) if not ((m >> k) & 1)]
    seen = set()
    for k in absent:
        if k in seen:
            continue
        orb = {mp[k] for mp in aut_maps(m)}
        seen |= orb
        typ = marked_type(m, k)
        A_counts[typ] += 1
        A_marked += 1
        if typ == "connected_source":
            A_connected_by_edges[m.bit_count()] += 1

assert A_marked == 572
assert A_counts == Counter(
    connected_source=402,
    cross_components=112,
    within_component=58,
)
assert A_connected_by_edges == Counter(
    {5: 27, 6: 64, 7: 90, 8: 89, 9: 65,
     10: 39, 11: 18, 12: 7, 13: 2, 14: 1}
)

# Method B: independent Burnside count of marked-pair orbits, stratified by
# the same invariant source-connectivity categories.  For a vertex
# permutation p, a marked pair (G,e) is fixed only if e is a 1-cycle in the
# induced edge action and G is a union of edge-action cycles with e absent.
def edge_cycles(mp):
    seen = set()
    ans = []
    for k in range(len(E)):
        if k in seen:
            continue
        cyc = []
        q = k
        while q not in seen:
            seen.add(q)
            cyc.append(q)
            q = mp[q]
        ans.append(tuple(cyc))
    return tuple(ans)


fixed_sums = defaultdict(int)
for mp in EDGE_MAPS:
    cycles = edge_cycles(mp)
    fixed_edges = [cyc[0] for cyc in cycles if len(cyc) == 1]
    if not fixed_edges:
        continue
    for bits in range(1 << len(cycles)):
        m = 0
        for j, cyc in enumerate(cycles):
            if (bits >> j) & 1:
                for k in cyc:
                    m |= 1 << k
        for k in fixed_edges:
            if (m >> k) & 1:
                continue
            fixed_sums[marked_type(m, k)] += 1

B_counts = Counter()
for typ, total_fixed in fixed_sums.items():
    assert total_fixed % len(PERMS) == 0
    B_counts[typ] = total_fixed // len(PERMS)

assert B_counts == A_counts
assert sum(B_counts.values()) == 572

# Consequences for the current P0195 order-six program.
# The analytic bridge theorem covers every cross-components type.
# The already-proved complete n<=5 theorem covers every within-component
# addition, because every component of a disconnected 6-vertex source has
# at most five vertices.  Hence all 170 disconnected source marked types
# are covered.  The previous exact dense theorem covers the 3 connected
# types with 13 or 14 source edges.
disconnected_covered = A_counts["cross_components"] + A_counts["within_component"]
connected_dense_covered = sum(v for e, v in A_connected_by_edges.items() if e >= 13)
connected_remaining_after_dense = A_counts["connected_source"] - connected_dense_covered

assert disconnected_covered == 170
assert connected_dense_covered == 3
assert connected_remaining_after_dense == 399

print("N", N)
print("unlabeled_graphs", len(classes))
print("marked_edge_addition_orbits", A_marked)
print("method_A_counts", dict(sorted(A_counts.items())))
print("method_B_burnside_counts", dict(sorted(B_counts.items())))
print("connected_by_source_edge_count", dict(sorted(A_connected_by_edges.items())))
print("disconnected_marked_types_covered", disconnected_covered)
print("connected_dense_marked_types_already_covered", connected_dense_covered)
print("connected_marked_types_remaining_after_dense", connected_remaining_after_dense)
print("ALL_EXACT_CHECKS_PASS")
