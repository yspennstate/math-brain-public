"""Independent finite recheck of round 5, using union-find and subset witnesses."""
from collections import Counter, defaultdict
from fractions import Fraction as Q
from itertools import combinations
import os
import resource
import signal
import time

signal.alarm(120)
assert os.environ.get("OMP_NUM_THREADS") == "1"
start = time.monotonic()


def labels(edges, mask, vertices):
    parent = {v: v for v in vertices}
    def find(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for j, (u, v) in enumerate(edges):
        if mask >> j & 1:
            parent[find(u)] = find(v)
    return {v: find(v) for v in vertices}


def code(lab, terminals, mark):
    groups = [{v for v in terminals if lab[v] == x}
              for x in {lab[v] for v in terminals}]
    marked = {lab[v] for v in mark}
    star_group = {-1} | {v for v in terminals if lab[v] in marked}
    return tuple(sorted([tuple(sorted(g)) for g in groups
                         if not any(lab[v] in marked for v in g)]
                        + [tuple(sorted(star_group))]))


cases = [
    ((0,1), (2,3), ((0,2),(0,3),(1,2),(1,3),(2,3)),
     ((2,4),(3,4),(4,5),(2,5),(3,5)), (5,)),
    ((0,1,2), (3,4,5), ((0,3),(1,4),(2,5)),
     ((3,6),(4,6),(5,6),(6,8)), (8,)),
    ((0,1,2), (3,4), ((0,3),(3,1),(2,4)),
     ((3,5),(4,6),(5,6),(6,8)), (8,)),
]
states = inclusions = reconstructions = inequalities = 0
for S, R, local, far, T in cases:
    edges = local + far
    vertices = {v for e in edges for v in e}
    short = []
    long = []
    # Enumerate inclusion-minimal open edge sets witnessing connections.
    for edge_list, targets, output in ((local, R, short), (edges, T, long)):
        for mask in range(1 << len(edge_list)):
            lab = labels(edge_list, mask, vertices)
            if any(lab[s] == lab[t] for s in S for t in targets):
                if not any(w & mask == w for w in output):
                    output.append(mask)
    counts = Counter()
    local_counts = Counter()
    tail_counts = {k: Counter() for k in range(1, len(S)+2)}
    mismatches = Counter()
    for mask in range(1 << len(edges)):
        lab = labels(edges, mask, vertices)
        llab = labels(local, mask, vertices)
        active = {llab[s] for s in S if any(llab[s] == llab[r] for r in R)}
        N = len(active)
        k_open = mask.bit_count()
        local_counts[k_open] += bool(N)
        states += 1
        if not any(lab[s] == lab[t] for s in S for t in T):
            continue
        counts[k_open] += 1
        for k in range(1, len(S)+2):
            if N < k:
                continue
            # An exhaustive set-packing check independent of last-exit paths.
            assert any(
                not (w & used) and all(not (a & b) for a, b in combinations(extra, 2))
                for w in long if w & mask == w
                for extra in combinations([v for v in short if v & mask == v], k-1)
                for used in [sum(extra)]
            )
            tail_counts[k][k_open] += 1
            inclusions += 1
        marked_s = min(s for s in S if llab[s] in active)
        exact = code(lab, S, T)
        approx = code(llab, S, (marked_s,))
        if N == 1:
            assert exact == approx
            reconstructions += 1
        mismatches[k_open] += exact != approx
    for p in (Q(1,3), Q(1,2), Q(2,3)):
        def prob(c):
            return sum((v*p**j*(1-p)**(len(edges)-j) for j,v in c.items()), Q(0))
        b, c = prob(counts), prob(local_counts)
        for k, tail in tail_counts.items():
            assert prob(tail) <= b*c**(k-1)
            inequalities += 1
        assert prob(mismatches)/b <= c

print(f"PASS: {states} configurations; {inclusions} independent disjoint-witness inclusions")
print(f"PASS: {reconstructions} exact one-active partition reconstructions")
print(f"PASS: {inequalities} exact BK-tail bounds and nine localization-error bounds")
print(f"Priority: {os.getpriority(os.PRIO_PROCESS, 0)}; OMP_NUM_THREADS=1")
print(f"Elapsed seconds: {time.monotonic()-start:.3f}")
assert resource.getrusage(resource.RUSAGE_SELF).ru_maxrss < 1_000_000_000
print(f"Peak RSS bytes: {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}")
print("PASS: round-5 result holds")
