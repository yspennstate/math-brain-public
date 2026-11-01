import os
"""Refined test: is the volume determined by the crossing graph whenever
that graph is CONNECTED?  A disconnected graph leaves the diagram free to
nest one component inside another rather than juxtapose them, and that is
the freedom the order-ten failure exploits."""
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

for n in (6, 8, 10):
    cls = {}
    for pm in tk_core.all_pairings(n):
        m, e = cg(pm)
        cls.setdefault((canon(m, e), m, connected(m, e)), set()).add(
            pairing_volume_exact(pm, "T"))
    conn = [(k, v) for k, v in cls.items() if k[2]]
    disc = [(k, v) for k, v in cls.items() if not k[2]]
    ci = [k for k, v in conn if len(v) > 1]
    di = [k for k, v in disc if len(v) > 1]
    print(f"order {n}: connected {len(conn)} classes, {len(ci)} impure | "
          f"disconnected {len(disc)} classes, {len(di)} impure")
    for k in di:
        print(f"    disconnected impure: {k[0]} -> "
              f"{sorted(str(x) for x in cls[k])}")
    sys.stdout.flush()
