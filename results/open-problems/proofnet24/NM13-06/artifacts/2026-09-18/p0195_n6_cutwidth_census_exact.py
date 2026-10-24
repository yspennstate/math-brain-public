from itertools import combinations, permutations
from collections import Counter

N = 6
EDGES = list(combinations(range(N), 2))
EIDX = {e:i for i,e in enumerate(EDGES)}
PERMS = list(permutations(range(N)))

# Each permutation is represented by its action on the 15 edge-bit positions.
PMAPS = []
for p in PERMS:
    mp = []
    for u,v in EDGES:
        a,b = sorted((p[u], p[v]))
        mp.append(EIDX[(a,b)])
    PMAPS.append(tuple(mp))

def transform(mask, mp):
    out = 0
    for i,j in enumerate(mp):
        if (mask >> i) & 1:
            out |= 1 << j
    return out

def connected(mask):
    adj = [0]*N
    for i,(u,v) in enumerate(EDGES):
        if (mask >> i) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    seen = 1
    frontier = 1
    while frontier:
        nxt = 0
        for v in range(N):
            if (frontier >> v) & 1:
                nxt |= adj[v]
        nxt &= ~seen
        seen |= nxt
        frontier = nxt
    return seen == (1 << N) - 1

def graph_representatives():
    # Ascending masks plus full S_6 orbit marking gives one exact representative
    # for every unlabeled simple six-vertex graph.
    seen = set()
    reps = []
    for mask in range(1 << len(EDGES)):
        if mask in seen:
            continue
        orbit = {transform(mask, mp) for mp in PMAPS}
        seen.update(orbit)
        reps.append(mask)
    assert len(seen) == 1 << len(EDGES)
    return reps

def automorphisms(mask):
    return tuple(mp for mp in PMAPS if transform(mask, mp) == mask)

def missing_edge_orbit_reps(mask):
    aut = automorphisms(mask)
    missing = [i for i in range(len(EDGES)) if not ((mask >> i) & 1)]
    seen = set()
    reps = []
    for i in missing:
        if i in seen:
            continue
        orbit = {mp[i] for mp in aut}
        assert orbit <= set(missing)
        seen |= orbit
        reps.append(min(orbit))
    assert seen == set(missing)
    return reps

def cutwidth(mask):
    # Exact exhaustive definition: minimum over all 6! vertex orderings of the
    # maximum number of edges crossing a prefix cut.
    adj = [0]*N
    deg = [0]*N
    for i,(u,v) in enumerate(EDGES):
        if (mask >> i) & 1:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
            deg[u] += 1
            deg[v] += 1

    best = len(EDGES) + 1
    for order in PERMS:
        S = 0
        crossing = 0
        worst = 0
        # No need to process the final vertex: the last nontrivial prefix is k=N-1.
        for v in order[:-1]:
            crossing += deg[v] - 2 * (adj[v] & S).bit_count()
            S |= 1 << v
            if crossing > worst:
                worst = crossing
            if worst >= best:
                break
        if worst < best:
            best = worst
    return best

reps = graph_representatives()
connected_reps = [m for m in reps if connected(m)]
assert len(reps) == 156
assert len(connected_reps) == 112

distribution = Counter()
ties_by_edges = Counter()
strict_by_edges = Counter()
tie_records = []
strict_records = []

for source in connected_reps:
    cws = cutwidth(source)
    for ei in missing_edge_orbit_reps(source):
        target = source | (1 << ei)
        cwt = cutwidth(target)
        # Edge addition cannot lower cutwidth. Check the monovariant directly.
        assert cwt >= cws
        rec = (source, source.bit_count(), ei, EDGES[ei], cws, cwt)
        distribution[(cws,cwt)] += 1
        if cwt == cws:
            tie_records.append(rec)
            ties_by_edges[source.bit_count()] += 1
        else:
            strict_records.append(rec)
            strict_by_edges[source.bit_count()] += 1

assert sum(distribution.values()) == 402
assert len(tie_records) == 162
assert len(strict_records) == 240

expected_distribution = {
    (1,2): 6,
    (2,2): 29,
    (2,3): 62,
    (3,3): 44,
    (3,4): 84,
    (4,4): 65,
    (4,5): 54,
    (5,5): 17,
    (5,6): 23,
    (6,6): 6,
    (6,7): 8,
    (7,7): 1,
    (7,8): 2,
    (8,9): 1,
}
assert dict(distribution) == expected_distribution

expected_ties_by_edges = {5:19, 6:15, 7:34, 8:49, 9:25, 10:13, 11:6, 12:1}
expected_strict_by_edges = {5:8, 6:49, 7:56, 8:40, 9:40, 10:26, 11:12, 12:6, 13:2, 14:1}
assert dict(sorted(ties_by_edges.items())) == expected_ties_by_edges
assert dict(sorted(strict_by_edges.items())) == expected_strict_by_edges

# Previous exact dense-class theorem covers exactly the three connected marked
# types whose source has at least 13 edges. All three have strict cutwidth rise.
dense = [r for r in tie_records + strict_records if r[1] >= 13]
assert len(dense) == 3
assert all(r[5] == r[4] + 1 for r in dense)
remaining = [r for r in tie_records + strict_records if r[1] <= 12]
assert len(remaining) == 399
remaining_ties = [r for r in remaining if r[5] == r[4]]
remaining_strict = [r for r in remaining if r[5] > r[4]]
assert len(remaining_ties) == 162
assert len(remaining_strict) == 237
assert all(r[5] == r[4] + 1 for r in strict_records)

# There is exactly one densest cutwidth tie: source K3 join independent-3,
# canonical mask 4095, with one of the three missing independent-set edges added.
ties12 = [r for r in tie_records if r[1] == 12]
assert ties12 == [(4095, 12, 12, (3,4), 7, 7)]

print("unlabeled_graphs_n6", len(reps))
print("connected_unlabeled_graphs_n6", len(connected_reps))
print("connected_marked_edge_addition_types", sum(distribution.values()))
print("cutwidth_transition_distribution", dict(sorted(distribution.items())))
print("cutwidth_strict", len(strict_records))
print("cutwidth_ties", len(tie_records))
print("ties_by_source_edge_count", dict(sorted(ties_by_edges.items())))
print("strict_by_source_edge_count", dict(sorted(strict_by_edges.items())))
print("previous_dense_types", len(dense))
print("remaining_after_dense", len(remaining))
print("remaining_strict_cutwidth", len(remaining_strict))
print("remaining_cutwidth_ties", len(remaining_ties))
print("unique_12_edge_tie", ties12[0])
print("unique_12_edge_tie_description", "K3 join 3K1; add one edge inside the independent 3-set")
print("scope_note", "cutwidth census only; no spectral-gap inequality is inferred from cutwidth")
print("ALL_EXACT_CHECKS_PASS")
