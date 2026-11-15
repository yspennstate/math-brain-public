"""Exact finite checks of the localization lemma, not a lattice simulation.

Run with nice -n 15 env OMP_NUM_THREADS=1 python3 audit.py.
Only certificates.csv is written; no earlier files are imported or executed.
"""
from collections import Counter, defaultdict, deque
import csv
from fractions import Fraction as Q
from itertools import combinations, product
import os
from pathlib import Path
import resource
import signal
import time

signal.alarm(120)
start = time.monotonic()
assert os.environ.get("OMP_NUM_THREADS") == "1"
ROOT, STAR = -2, -1


def adjacency(edges, mask):
    adj = defaultdict(list)
    for i, (u, v) in enumerate(edges):
        if mask & (1 << i):
            adj[u].append((v, i))
            adj[v].append((u, i))
    return adj


def reach(adj, seeds):
    seen = set(seeds)
    todo = deque(seeds)
    while todo:
        u = todo.popleft()
        for v, _ in adj[u]:
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return seen


def simple_paths(adj, sources, targets):
    """Independent exhaustive witnesses as (vertex tuple, edge mask)."""
    targets = set(targets)
    paths = []

    def walk(vertices, mask):
        u = vertices[-1]
        if u in targets:
            paths.append((vertices, mask))
            return
        for v, i in adj[u]:
            if v not in vertices:
                walk(vertices+(v,), mask | (1 << i))

    for s in sources:
        walk((s,), 0)
    return paths


def partition(adj, terminals, marked_vertices=()):
    # Add the target wiring to a copy. STAR is otherwise an isolated terminal.
    work = defaultdict(list, {u: list(vs) for u, vs in adj.items()})
    for t in marked_vertices:
        work[t].append((STAR, -1))
        work[STAR].append((t, -1))
    return tuple(sorted({tuple(sorted(reach(work, (v,)) & set(terminals)))
                         for v in terminals}))


def local_components(adj, S, R):
    components = []
    seen = set()
    for s in S:
        if s not in seen:
            C = reach(adj, (s,))
            seen.update(C)
            components.append(C)
    active = [C for C in components if C & set(R)]
    return components, active


def all_partitions(vertices):
    if not vertices:
        yield ()
        return
    x, *rest = vertices
    for P in all_partitions(rest):
        yield tuple(sorted(((x,),)+P))
        for i in range(len(P)):
            yield tuple(sorted(P[:i]+(tuple(sorted((x,)+P[i])),)+P[i+1:]))


def kernel(pi, xi):
    """Equivalence closure by label propagation, separate from BFS."""
    vertices = {v for P in (pi, xi) for B in P for v in B}
    labels = {v: v for v in vertices}
    while True:
        old = labels.copy()
        for B in pi+xi:
            label = min(labels[v] for v in B)
            old_labels = {labels[v] for v in B}
            for v in vertices:
                if labels[v] in old_labels:
                    labels[v] = label
        if old == labels:
            return int(labels[ROOT] == labels[STAR])


def multi_disjoint(long_paths, short_paths, needed):
    """Brute-force independent check, with no use of component certificates."""
    short = sorted({mask for _, mask in short_paths})

    def choose(used, count, begin):
        if count == 0:
            return True
        return any(not (mask & used) and choose(used | mask, count-1, i+1)
                   for i, mask in enumerate(short[begin:], begin))

    return any(choose(mask, needed, 0) for _, mask in long_paths)


def probability(counts, edge_count, p):
    return sum((Q(count)*p**k*(1-p)**(edge_count-k)
                for k, count in counts.items()), Q(0))


def tv(P, Qlaw):
    return sum(abs(P.get(x, 0)-Qlaw.get(x, 0))
               for x in P.keys() | Qlaw.keys())/2


# In every case, local/far graphs meet only at R. The first case's all-open
# local configuration merges both S-to-R components, testing nonmonotonic N.
cases = [
    dict(name="two_sources_cycle", S=(0,1), R=(2,3),
         local=((0,2),(0,3),(1,2),(1,3),(2,3)),
         far=((2,4),(3,4),(4,5),(2,5),(3,5)), T=(5,)),
    dict(name="outer_merger", S=(0,1,2), R=(3,4,5),
         local=((0,3),(1,4),(2,5)),
         far=((3,6),(4,6),(5,6),(6,8)), T=(8,)),
    dict(name="two_stage_outer_merger", S=(0,1,2), R=(3,4,5),
         local=((0,3),(1,4),(2,5)),
         far=((3,6),(4,7),(5,9),(6,7),(7,9),(9,8)), T=(8,)),
    dict(name="local_return", S=(0,1,2), R=(3,4),
         local=((0,3),(3,1),(2,4)),
         far=((3,5),(4,6),(5,6),(6,8)), T=(8,)),
    dict(name="cyclic_local_return", S=(0,1,2), R=(3,4,5),
         local=((0,3),(3,4),(4,1),(1,5),(2,5)),
         far=((3,6),(5,7),(6,7),(7,8)), T=(8,)),
    dict(name="two_targets", S=(0,1,2), R=(3,4,5),
         local=((0,3),(1,4),(2,5)),
         far=((3,6),(4,7),(5,9),(6,7),(7,9)), T=(6,9)),
]

rows = []
states = inclusions = reconstructed = responses = tail_checks = 0
outer_merge_states = nonmonotone_pairs = 0
for case in cases:
    S, R, T = case["S"], case["R"], case["T"]
    local, far = case["local"], case["far"]
    edges = local+far
    ecount = len(edges)
    assert ({v for e in local for v in e} &
            {v for e in far for v in e}) <= set(R)
    assert not set(T) & {v for e in local for v in e}
    local_mask = (1 << len(local))-1
    pis = list(all_partitions([ROOT]+list(S)))
    assert len(pis) == len(set(pis))
    assert len(pis) == (5 if len(S) == 2 else 15)
    H, HR, bad, mismatch = Counter(), Counter(), Counter(), Counter()
    tails = {k: Counter() for k in range(1, len(S)+2)}
    full_law, approx_law = defaultdict(Counter), defaultdict(Counter)
    local_N = {}
    for mask in range(1 << ecount):
        adj = adjacency(edges, mask)
        ladj = adjacency(edges, mask & local_mask)
        components, active = local_components(ladj, S, R)
        N = len(active)
        local_N[mask & local_mask] = N
        nopen = mask.bit_count()
        long_paths = simple_paths(adj, S, T)
        short_paths = simple_paths(ladj, S, R)
        h, hr = bool(long_paths), bool(short_paths)
        assert hr == bool(N)
        assert h == bool(reach(adj, S) & set(T))
        assert not h or hr
        HR[nopen] += hr
        states += 1
        if not h:
            continue
        H[nopen] += 1
        for k in range(1, len(S)+2):
            if N >= k:
                assert multi_disjoint(long_paths, short_paths, k-1)
                tails[k][nopen] += 1
                inclusions += 1

        # Construct the actual certificate from the last visit to U, then
        # check each witness against independently enumerated simple paths.
        U = set().union(*components)
        vertices, _ = long_paths[0]
        last = max(i for i, v in enumerate(vertices) if v in U)
        v = vertices[last]
        chosen = next(C for C in components if v in C)
        assert chosen in active and v in R
        prefix = simple_paths(ladj, sorted(chosen & set(S)), (v,))[0]
        tail_vertices = vertices[last:]
        tail_mask = 0
        for u, w in zip(tail_vertices, tail_vertices[1:]):
            tail_mask |= 1 << next(i for w2, i in adj[u] if w2 == w)
        constructed_vertices = prefix[0]+tail_vertices[1:]
        witness = prefix[1] | tail_mask
        assert (constructed_vertices, witness) in long_paths
        used = witness
        for C in active:
            if C is chosen:
                continue
            candidates = simple_paths(ladj, sorted(C & set(S)), R)
            short_witness = candidates[0][1]
            assert not short_witness & used
            used |= short_witness

        marked = min(active, key=lambda C: min(C & set(S)))
        xi = partition(adj, S+(STAR,), T)
        reconstructed_xi = partition(ladj, S+(STAR,), sorted(marked & set(S)))
        full_law[xi][nopen] += 1
        approx_law[reconstructed_xi][nopen] += 1
        if N == 1:
            assert xi == reconstructed_xi
            reconstructed += 1
        else:
            bad[nopen] += 1
        mismatch[nopen] += xi != reconstructed_xi
        if any(reach(adj, (min(C & set(S)),)) & D
               for C, D in combinations(active, 2)):
            outer_merge_states += 1

    for mask, N in local_N.items():
        for i in range(len(local)):
            if not mask & (1 << i) and local_N[mask | (1 << i)] < N:
                nonmonotone_pairs += 1

    for p in (Q(1,3), Q(1,2), Q(2,3)):
        b = probability(H, ecount, p)
        c = probability(HR, ecount, p)
        assert b > 0 and c > 0
        # Independent HR calculation uses only the local product space.
        local_hr = sum((p**mask.bit_count()*(1-p)**(len(local)-mask.bit_count())
                        for mask, N in local_N.items() if N), Q(0))
        assert c == local_hr
        for k in range(1, len(S)+2):
            assert probability(tails[k], ecount, p) <= b*c**(k-1)
            tail_checks += 1
        P = {xi: probability(count, ecount, p)/b
             for xi, count in full_law.items()}
        L = {xi: probability(count, ecount, p)/b
             for xi, count in approx_law.items()}
        assert sum(P.values()) == sum(L.values()) == 1
        coupling_error = probability(mismatch, ecount, p)/b
        bad_probability = probability(bad, ecount, p)/b
        assert tv(P, L) <= coupling_error <= bad_probability <= c
        r, s = {}, {}
        for pi in pis:
            r[pi] = sum(kernel(pi, xi)*w for xi, w in P.items())
            s[pi] = sum(kernel(pi, xi)*w for xi, w in L.items())
            assert abs(r[pi]-s[pi]) <= coupling_error <= c
            responses += 1
        ref = (tuple(sorted((ROOT,)+S)),)
        assert r[ref] == s[ref] == 1
        # Normalization stress: positive abstract partition weights and small
        # reference mass. The algebra also applies to actual product weights.
        for tiny in (Q(1,100), Q(1,3)):
            a = {pi: (tiny if pi == ref else (1-tiny)/(len(pis)-1))
                 for pi in pis}
            Z = sum(a[pi]*r[pi] for pi in pis)
            W = sum(a[pi]*s[pi] for pi in pis)
            D = sum(a[pi]*abs(r[pi]-s[pi]) for pi in pis)
            normalized_tv = sum(abs(a[pi]*r[pi]/Z-a[pi]*s[pi]/W)
                                for pi in pis)/2
            assert Z >= tiny and W >= tiny and D <= c
            assert normalized_tv <= D/tiny <= c/tiny
        rows.append(dict(graph=case["name"], p=str(p), states=1 << ecount,
                         b_far=str(b), b_local=str(c),
                         conditional_multi_active=str(bad_probability),
                         coupling_error=str(coupling_error),
                         partition_TV=str(tv(P,L))))

assert outer_merge_states > 0
assert nonmonotone_pairs > 0
with Path("certificates.csv").open("w", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
    writer.writeheader()
    writer.writerows(rows)

# Recount boundary vertices directly, independently of expanding the cubes.
for m in range(1, 8):
    count = sum(max(abs(v) for v in x) == m
                for x in product(range(-m, m+1), repeat=3))
    assert count == 24*m*m+2
print(f"PASS: {len(cases)} graph models; {states} complete configurations")
print(f"PASS: {inclusions} multi-path inclusions, independent exhaustive witnesses")
print(f"PASS: {reconstructed} one-active exact partition reconstructions")
print(f"PASS: {tail_checks} exact BK-tail bounds across {len(rows)} graph/parameter models")
print(f"PASS: {responses} response approximation checks; {2*len(rows)} normalization checks")
print(f"PASS: {outer_merge_states} outer-merger test states; {nonmonotone_pairs} component-count decreases")
print("PASS: seven independent cubic-boundary counts; |S_m|=24m^2+2")
print("Exact p=1/2 certificates: graph, b_local, P(multi | far), partition TV")
for row in rows:
    if row["p"] == "1/2":
        print(row["graph"], row["b_local"], row["conditional_multi_active"],
              row["partition_TV"])
rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
assert rss < 1_000_000_000
print(f"Priority: {os.getpriority(os.PRIO_PROCESS, 0)}; OMP_NUM_THREADS=1")
print(f"Elapsed seconds: {time.monotonic()-start:.3f}")
print(f"Peak RSS bytes (macOS): {rss}")
print("PASS: all exact checks")
