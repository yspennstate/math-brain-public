"""Early targeted read on the RC-sufficient inequality, on the families most likely to break it.

Claim:  Z(G) <= (4/3)^{E - V + b},   b = 1 if G bipartite else 0   (G connected)
with Z = (2/3)^E * 2^-V * SUM_x 2^{cut(x)}.

Candidates for the extreme, chosen for a reason:
  - odd cycles: the measured tight family (C5 ratio 0.9971) - exponent 0, so the claim is Z <= 1
  - complete graphs K_n: densest non-bipartite, exponent kappa - 1
  - complete bipartite K_{n,m}: where Z is LARGEST (aligned configurations), exponent kappa
  - odd cliques with a pendant, wheels, Moebius-Kantor-ish: mixed parity
  - dense random graphs at V = 8..10, beyond the exhaustive scan's reach

Integer arithmetic; the weight is 4 when endpoints DIFFER (3 - x_u x_v), which is the sign I got
backwards once already - positive control on C3 = 26/27 and C4 = 82/81 runs first and gates the rest.
"""
import itertools
import random
import sys
from fractions import Fraction

rng = random.Random(7)


def Znum(V, edges):
    tot = 0
    for bits in range(1 << V):
        p = 1
        for (a, b) in edges:
            p *= 4 if ((bits >> a) ^ (bits >> b)) & 1 else 2
        tot += p
    return tot


def bipartite(V, edges):
    adj = {v: [] for v in range(V)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    col = {}
    for s in range(V):
        if s in col:
            continue
        col[s] = 0
        st = [s]
        while st:
            u = st.pop()
            for v in adj[u]:
                if v not in col:
                    col[v] = 1 - col[u]
                    st.append(v)
                elif col[v] == col[u]:
                    return False
    return True


def connected(V, edges):
    adj = {v: [] for v in range(V)}
    for a, b in edges:
        adj[a].append(b)
        adj[b].append(a)
    seen, st = {0}, [0]
    while st:
        u = st.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                st.append(v)
    return len(seen) == V


def report(name, V, edges):
    if not connected(V, edges):
        print("  %-24s disconnected - skipped" % name)
        return None
    E = len(edges)
    b = 1 if bipartite(V, edges) else 0
    Z = Fraction(Znum(V, edges), 3 ** E * 2 ** V)
    bound = Fraction(4, 3) ** (E - V + b)
    ratio = Z / bound
    flag = "*** VIOLATION" if Z > bound else ""
    print("  %-24s V=%-3d E=%-3d bip=%s  Z=%-12.6f bound=%-14.6f ratio=%.6f %s"
          % (name, V, E, "y" if b else "n", float(Z), float(bound), float(ratio), flag))
    return float(ratio)


# GATE: positive control
c3 = Fraction(Znum(3, [(0, 1), (0, 2), (1, 2)]), 3 ** 3 * 2 ** 3)
c4 = Fraction(Znum(4, [(0, 1), (1, 2), (2, 3), (3, 0)]), 3 ** 4 * 2 ** 4)
print("positive control: C3 Z = %s (expect 26/27), C4 Z = %s (expect 82/81)" % (c3, c4))
if c3 != Fraction(26, 27) or c4 != Fraction(82, 81):
    print("*** CONTROL FAILED - not reading anything below")
    sys.exit(1)
print("control OK")
print()

worst = []
print("odd cycles (the measured tight family):")
for m in (3, 5, 7, 9, 11, 13):
    worst.append(report("C%d" % m, m, [(i, (i + 1) % m) for i in range(m)]))

print()
print("complete graphs:")
for n in range(3, 9):
    worst.append(report("K%d" % n, n, list(itertools.combinations(range(n), 2))))

print()
print("complete bipartite:")
for (a, b) in ((2, 2), (2, 3), (3, 3), (3, 4), (4, 4), (2, 6), (3, 5)):
    edges = [(i, a + j) for i in range(a) for j in range(b)]
    worst.append(report("K%d,%d" % (a, b), a + b, edges))

print()
print("wheels (odd and even rims):")
for m in (3, 4, 5, 6, 7):
    edges = [(i, (i + 1) % m) for i in range(m)] + [(m, i) for i in range(m)]
    worst.append(report("W%d" % m, m + 1, edges))

print()
print("dense random, V = 8..10 (beyond the exhaustive scan):")
for t in range(12):
    V = rng.choice([8, 9, 10])
    alle = list(itertools.combinations(range(V), 2))
    p = rng.choice([0.4, 0.6, 0.8])
    edges = [e for e in alle if rng.random() < p]
    if not edges or not connected(V, edges):
        continue
    worst.append(report("rand%d V=%d p=%.1f" % (t, V, p), V, edges))

w = [x for x in worst if x is not None]
print()
print("worst ratio seen: %.6f   %s" % (max(w), "NO VIOLATION" if max(w) <= 1.0 else "*** VIOLATED"))
