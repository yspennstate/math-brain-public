from itertools import combinations, permutations
from collections import Counter
import heapq

N = 6
EDGES = list(combinations(range(N), 2))
EIDX = {e:i for i,e in enumerate(EDGES)}
PERMS = list(permutations(range(N)))

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
    seen = frontier = 1
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

def cut_heights(mask):
    vals = [0]*(1 << N)
    active = [e for i,e in enumerate(EDGES) if (mask >> i) & 1]
    for s in range(1 << N):
        vals[s] = sum((((s >> u) & 1) ^ ((s >> v) & 1)) for u,v in active)
    return vals

def cutwidth(mask):
    vals = cut_heights(mask)
    best = len(EDGES) + 1
    for order in PERMS:
        s = 0
        worst = 0
        for v in order[:-1]:
            s |= 1 << v
            worst = max(worst, vals[s])
            if worst >= best:
                break
        best = min(best, worst)
    return best

def communication_barrier(mask):
    """Minimax cut height along all hypercube paths from all-plus to all-minus."""
    vals = cut_heights(mask)
    start = 0
    goal = (1 << N) - 1
    INF = len(EDGES) + 1
    dist = [INF]*(1 << N)
    dist[start] = vals[start]
    pq = [(dist[start], start)]
    while pq:
        d,s = heapq.heappop(pq)
        if d != dist[s]:
            continue
        if s == goal:
            return d
        for v in range(N):
            t = s ^ (1 << v)
            nd = max(d, vals[t])
            if nd < dist[t]:
                dist[t] = nd
                heapq.heappush(pq, (nd,t))
    raise AssertionError("unreachable hypercube target")

reps = graph_representatives()
connected_reps = [m for m in reps if connected(m)]
assert len(reps) == 156
assert len(connected_reps) == 112

# Exact graph-level barrier theorem at order six.
barrier_cutwidth_distribution = Counter()
for m in connected_reps:
    b = communication_barrier(m)
    c = cutwidth(m)
    assert b == c
    barrier_cutwidth_distribution[(b,c)] += 1

expected_graph_distribution = {
    (1,1): 1,
    (2,2): 18,
    (3,3): 28,
    (4,4): 35,
    (5,5): 17,
    (6,6): 8,
    (7,7): 3,
    (8,8): 1,
    (9,9): 1,
}
assert dict(sorted(barrier_cutwidth_distribution.items())) == expected_graph_distribution

# Reconstruct the full connected marked-edge frontier and certify the barrier
# separation exactly on every strict-cutwidth transition.
transition_distribution = Counter()
strict = []
ties = []
for source in connected_reps:
    cws = cutwidth(source)
    bs = communication_barrier(source)
    assert bs == cws
    for ei in missing_edge_orbit_reps(source):
        target = source | (1 << ei)
        cwt = cutwidth(target)
        bt = communication_barrier(target)
        assert bt == cwt
        assert cwt >= cws
        rec = (source, source.bit_count(), ei, EDGES[ei], cws, cwt, bs, bt)
        transition_distribution[(cws,cwt)] += 1
        if cwt > cws:
            assert cwt == cws + 1
            assert bt > cws
            strict.append(rec)
        else:
            assert bt == cws
            ties.append(rec)

assert len(strict) == 240
assert len(ties) == 162
assert len(strict) + len(ties) == 402

expected_transition_distribution = {
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
assert dict(sorted(transition_distribution.items())) == expected_transition_distribution

# Preserve the previous unique densest tie as a cross-check.
ties12 = [r for r in ties if r[1] == 12]
assert ties12 == [(4095, 12, 12, (3,4), 7, 7, 7, 7)]

print("unlabeled_graphs_n6", len(reps))
print("connected_unlabeled_graphs_n6", len(connected_reps))
print("barrier_equals_cutwidth_connected_graphs", len(connected_reps))
print("barrier_cutwidth_distribution", dict(sorted(barrier_cutwidth_distribution.items())))
print("connected_marked_edge_addition_types", len(strict)+len(ties))
print("transition_distribution", dict(sorted(transition_distribution.items())))
print("strict_cutwidth_and_barrier_separation", len(strict))
print("barrier_ties", len(ties))
print("unique_12_edge_tie", ties12[0])
print("theorem_scope", "all 240 connected six-vertex marked edge additions with strict cutwidth increase have b(target) > cw(source)")
print("metric", "n_edge^* remains >= 6; the 162 barrier ties are not decided by this low-temperature exponent route")
print("ALL_EXACT_CHECKS_PASS")
