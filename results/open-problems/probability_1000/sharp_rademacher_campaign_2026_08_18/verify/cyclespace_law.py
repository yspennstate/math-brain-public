"""CONJECTURED LAW, and a deliberate attempt to break it.

    |A| / (2^r (3/4)^k)  =  SUM over the CYCLE SPACE C of (-1/3)^{|S|}

where the graph G has vertices = shared coordinates and edges = triangles carrying two shared
coordinates; S ranges over EVEN SUBGRAPHS (the cycle space, dimension |E|-|V|+comps) and |S| is its
edge count. Equivalently c = log2 of that sum.

Where it came from: exact rationals, not a fit.
    pure m-cycle        1 + (-1/3)^m                      (cycle space {0, C})
    two disjoint 4-cyc  1 + 2(1/81) + (1/3)^8 = 6724/6561 (cross term PRESENT)
    theta(2,2,2)        1 + 3(1/81)  = 28/27              (three cycles, no cross term)
    theta(2,3,4)        1 - 1/243 + 1/729 - 1/2187 = 2180/2187
The theta cases have C_a + C_b = C_c, so the cycle space has 4 elements and the "cross term" IS the
third cycle - which is exactly why a BASIS sum fails and a cycle-SPACE sum works. That is the
van der Waerden / high-temperature Ising expansion.

This is a surprising result, so the point of this file is to FALSIFY it, not confirm it. Tested on
shapes chosen to break it:
  - triangles carrying THREE shared coordinates (G stops being a graph - hyperedge)
  - two cycles sharing a single TRIANGLE (edge-sharing, not vertex-sharing)
  - K4 and K_{3,3}-like sharing patterns (rich cycle spaces, many even subgraphs)
  - long girth vs many short cycles
  - random linear systems, where the law has no reason to hold if it is a small-case artefact
A single exact mismatch kills it.
"""
import itertools
import math
import random

BETA = math.log2(4.0 / 3.0)
rng = random.Random(20260820)


def fibre_size(r, T):
    n = 0
    for s in itertools.product((0, 1), repeat=r):
        if all(not (s[a] == s[b] == s[c]) for (a, b, c) in T):
            n += 1
    return n


def is_linear(T):
    return all(len(set(x) & set(y)) < 2 for x, y in itertools.combinations(T, 2))


def shared_coords(T):
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    return {x for x in cnt if cnt[x] >= 2}


def cycle_space_sum(T):
    """sum over even subgraphs of (-1/3)^{#edges}. Edges = triangles with exactly 2 shared coords.
    Returns None when some triangle has 3 shared coordinates (G is not a graph then)."""
    sh = shared_coords(T)
    edges = []
    for t in T:
        s = [x for x in t if x in sh]
        if len(s) == 3:
            return None
        if len(s) == 2:
            edges.append(tuple(s))
    m = len(edges)
    if m > 22:
        return None
    verts = sorted({v for e in edges for v in e})
    idx = {v: i for i, v in enumerate(verts)}
    total = 0.0
    # enumerate all edge subsets; keep the even ones (every vertex even degree)
    for mask in range(1 << m):
        deg = [0] * len(verts)
        cnt = 0
        mm = mask
        i = 0
        while mm:
            if mm & 1:
                a, b = edges[i]
                deg[idx[a]] += 1
                deg[idx[b]] += 1
                cnt += 1
            mm >>= 1
            i += 1
        if all(d % 2 == 0 for d in deg):
            total += (-1.0 / 3.0) ** cnt
    return total


def check(name, T):
    lab = {x: i for i, x in enumerate(sorted({x for t in T for x in t}))}
    T2 = [tuple(lab[x] for x in t) for t in T]
    r, k = len(lab), len(T2)
    if not is_linear(T2):
        print("  %-32s NOT LINEAR - skipped" % name)
        return None
    if r > 21:
        print("  %-32s r=%d too big - skipped" % (name, r))
        return None
    pred = cycle_space_sum(T2)
    if pred is None:
        print("  %-32s has a 3-shared-coordinate triangle - law not defined here" % name)
        return None
    n = fibre_size(r, T2)
    ratio = n / ((2.0 ** r) * (0.75 ** k))
    ok = abs(ratio - pred) < 1e-9
    print("  %-32s k=%-2d r=%-3d |A|=%-7d ratio=%.9f pred=%.9f  %s"
          % (name, k, r, n, ratio, pred, "MATCH" if ok else "*** MISMATCH ***"))
    return ok


def cyc(m, sh0, pr0):
    return [(sh0 + i, sh0 + (i + 1) % m, pr0 + i) for i in range(m)]


res = []
print("# controls (must match, they generated the law)")
res.append(check("pure 4-cycle", cyc(4, 0, 100)))
res.append(check("pure 5-cycle", cyc(5, 0, 100)))
res.append(check("two disjoint 4-cycles", cyc(4, 0, 100) + cyc(4, 20, 120)))

print()
print("# ATTACKS")
# two cycles sharing one triangle (edge-sharing)
T = [(0, 1, 100), (1, 2, 101), (2, 0, 102)]          # 3-cycle on 0,1,2
T += [(0, 3, 103), (3, 1, 104)]                       # second cycle 0-3-1 reusing edge (0,1)? no: path
res.append(check("two cycles sharing a vertex-path", T))

# K4 sharing pattern: 4 shared coords, 6 triangles as the 6 edges of K4
T = []
for i, (a, b) in enumerate(itertools.combinations(range(4), 2)):
    T.append((a, b, 100 + i))
res.append(check("K4 (6 triangles, cyc space 3)", T))

# theta with unequal arms - the case that killed the basis law
def theta(p, q, s):
    T, c = [], [200]
    def path(L, tag):
        prev = "U"
        for i in range(L):
            nxt = "V" if i == L - 1 else "%s_s%d" % (tag, i)
            T.append((prev, nxt, "%s_a%d" % (tag, i)))
            prev = nxt
    path(p, "P"); path(q, "Q"); path(s, "R")
    return T
res.append(check("theta(2,2,3)", theta(2, 2, 3)))
res.append(check("theta(2,3,4)", theta(2, 3, 4)))

# a cycle with a chord path (two cycles sharing several edges)
T = cyc(6, 0, 100)
T += [(0, 3, 150)]     # chord triangle joining opposite shared coords
res.append(check("6-cycle + chord", T))

# many short cycles: two 4-cycles sharing a vertex
A = cyc(4, 0, 100)
B = [tuple(0 if x == 20 else x for x in t) for t in cyc(4, 20, 120)]
res.append(check("two 4-cycles at a vertex", A + B))

print()
print("# random linear systems (no reason to hold if the law is a small-case artefact)")
ok_r = 0
tot_r = 0
for trial in range(14):
    r = rng.choice([9, 10, 11, 12])
    allt = list(itertools.combinations(range(r), 3))
    rng.shuffle(allt)
    T = []
    for t in allt:
        if all(len(set(t) & set(u)) < 2 for u in T):
            T.append(t)
        if len(T) >= rng.choice([4, 5, 6]):
            break
    used = {x for t in T for x in t}
    if len(used) < 6:
        continue
    v = check("random #%d" % trial, T)
    if v is not None:
        tot_r += 1
        ok_r += 1 if v else 0

print()
good = [x for x in res if x is not None]
print("structured cases: %d/%d matched" % (sum(1 for x in good if x), len(good)))
print("random cases:     %d/%d matched" % (ok_r, tot_r))
