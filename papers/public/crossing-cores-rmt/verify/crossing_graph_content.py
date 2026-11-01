import os
"""Does the connected-graph conjecture say anything Bouchet does not?
If a connected class is realised by several inequivalent chord diagrams
and they still share a volume, the statement has content.  Diagrams are
counted up to the dihedral action on the 2n boundary points."""
import sys
from itertools import combinations, permutations
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "engine"))
import tk_core
from exact_volume import pairing_volume_exact

def cg(pm):
    n = len(pm)
    pairs = [(i, pm[i]) for i in range(n) if i < pm[i]]
    m = len(pairs)
    e = set()
    for x, y in combinations(range(m), 2):
        a,b = pairs[x]; c,d = pairs[y]
        if a < c < b < d or c < a < d < b: e.add((x,y))
    return m, e

def canon(m, e):
    best = None
    for p in permutations(range(m)):
        k = tuple(sorted(tuple(sorted((p[x],p[y]))) for x,y in e))
        if best is None or k < best: best = k
    return best

def connected(m, e):
    if m == 0: return True
    adj = {i: set() for i in range(m)}
    for x,y in e: adj[x].add(y); adj[y].add(x)
    seen, st = {0}, [0]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen: seen.add(v); st.append(v)
    return len(seen) == m

def dihedral_canon(pm):
    n2 = len(pm); best = None
    for r in range(n2):
        for s in (1, -1):
            new = [0]*n2
            for i in range(n2):
                new[(s*i + r) % n2] = (s*pm[i] + r) % n2
            t = tuple(new)
            if best is None or t < best: best = t
    return best

for n in (8, 10):
    cls = {}
    for pm in tk_core.all_pairings(n):
        m, e = cg(pm)
        key = (canon(m, e), m, connected(m, e))
        d = cls.setdefault(key, {"vols": set(), "diags": set()})
        d["vols"].add(pairing_volume_exact(pm, "T"))
        d["diags"].add(dihedral_canon(pm))
    multi = [(k, v) for k, v in cls.items()
             if k[2] and len(v["diags"]) > 1]
    print(f"order {n}: connected classes with >1 inequivalent diagram: "
          f"{len(multi)} of {sum(1 for k in cls if k[2])}")
    for k, v in sorted(multi, key=lambda z: -len(z[1]['diags'])):
        status = "PURE" if len(v["vols"]) == 1 else "IMPURE"
        print(f"    {k[0]}  diagrams={len(v['diags'])}  "
              f"vols={sorted(str(x) for x in v['vols'])}  {status}")
    sys.stdout.flush()
