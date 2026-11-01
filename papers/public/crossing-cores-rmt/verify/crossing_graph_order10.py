import os
"""BREAK-TEST: does the crossing graph still determine the volume at
order ten?  Order eight alone could be coincidence - 11 classes, 6
volumes.  Order ten has 945 pairings and many more graph classes."""
import sys, time
from itertools import combinations, permutations
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact

def crossing_graph(pm):
    n = len(pm)
    pairs = [(i, pm[i]) for i in range(n) if i < pm[i]]
    m = len(pairs)
    edges = set()
    for x, y in combinations(range(m), 2):
        a, b = pairs[x]; c, d = pairs[y]
        if a < c < b < d or c < a < d < b:
            edges.add((x, y))
    return m, edges

def canon(m, edges):
    best = None
    for p in permutations(range(m)):
        key = tuple(sorted(tuple(sorted((p[x], p[y]))) for x, y in edges))
        if best is None or key < best:
            best = key
    return best

for n2k in (6, 10):
    groups = {}
    t0 = time.time()
    for pm in tk_core.all_pairings(n2k):
        m, e = crossing_graph(pm)
        groups.setdefault(canon(m, e), set()).add(pairing_volume_exact(pm, "T"))
    bad = {k: v for k, v in groups.items() if len(v) > 1}
    print(f"order {n2k}: {len(groups)} crossing-graph classes, "
          f"{len(bad)} impure  ({time.time()-t0:.0f}s)", flush=True)
    for k, vs in list(bad.items())[:4]:
        print(f"      {sorted(k)} -> {sorted(str(x) for x in vs)}", flush=True)
    if not bad:
        print(f"      the crossing graph determines the volume at order {n2k}",
              flush=True)
