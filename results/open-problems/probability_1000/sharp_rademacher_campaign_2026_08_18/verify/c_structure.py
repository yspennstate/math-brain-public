"""What IS the correlation excess c, structurally?

RC (the campaign's substantive conjecture) is exactly

    tightness = d_cb * beta / ell  <= 1     <=>     c <= beta * (k - d_cb),
    where c := k*beta - ell   and   ell = r - log2|A|.

Two things are already PROVED in the campaign:
  - disjoint unions of m NAE triples: ell = m*beta exactly, so c = 0
  - every triangle-TREE: ell = k*beta exactly regardless of topology, so c = 0

and its tri-cycle k=4 datum has ell/beta = 3.957 < k, i.e. c > 0. So c is zero on trees and
positive on cycles. If c is a FUNCTION OF THE CYCLE STRUCTURE, then RC becomes a comparison
between two integers-ish quantities and stops being a search.

This computes c exactly (rationally, via |A| counted by enumeration) on every connected linear
triangle system it can build, and lays c beside candidate structural invariants:

    k          triangles
    r          coordinates
    sh         number of coordinates shared by >= 2 triangles (hubs)
    inc_edges  edges of the intersection graph (one per shared coordinate incidence pair)
    cyc        cycle rank of the intersection graph = inc_edges - k + components
    r_pred     2k+1 - (extra sharing);  a tree has r = 2k+1

LINEAR means no two triangles share TWO coordinates. Read-only, self-contained.
"""
import itertools
import math
import sys
from fractions import Fraction

BETA = math.log2(4.0 / 3.0)
RMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 11
KMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 5


def fibre_size(r, T):
    """|A| = number of +-1 vectors with no monochromatic triple."""
    n = 0
    for s in itertools.product((1, -1), repeat=r):
        ok = True
        for (a, b, c) in T:
            if s[a] == s[b] == s[c]:
                ok = False
                break
        if ok:
            n += 1
    return n


def is_linear(T):
    for t, u in itertools.combinations(T, 2):
        if len(set(t) & set(u)) >= 2:
            return False
    return True


def connected(T, r):
    """connected through shared coordinates"""
    if not T:
        return False
    seen = {0}
    frontier = [0]
    while frontier:
        i = frontier.pop()
        for j in range(len(T)):
            if j not in seen and set(T[i]) & set(T[j]):
                seen.add(j)
                frontier.append(j)
    return len(seen) == len(T)


def invariants(T, r):
    used = sorted({x for t in T for x in t})
    cnt = {}
    for t in T:
        for x in t:
            cnt[x] = cnt.get(x, 0) + 1
    sh = sum(1 for x in cnt if cnt[x] >= 2)
    # intersection graph: one edge per pair of triangles sharing a coordinate
    edges = 0
    for i, j in itertools.combinations(range(len(T)), 2):
        if set(T[i]) & set(T[j]):
            edges += 1
    cyc = edges - len(T) + 1          # connected, so components = 1
    # total sharing excess: sum over coordinates of (deg - 1)
    excess = sum(cnt[x] - 1 for x in cnt)
    return len(used), sh, edges, cyc, excess


print("# c = k*beta - ell ;  ell = r - log2|A| ;  beta = %.6f" % BETA)
print("#  k   r  |A|        ell        c          c/beta     sh  incE  cyc  excess   shape")
rows = []
seen_sig = set()
for k in range(2, KMAX + 1):
    for r in range(3, RMAX + 1):
        allt = list(itertools.combinations(range(r), 3))
        # cap the enumeration; take a deterministic slice for reproducibility
        for T in itertools.combinations(allt, k):
            used = {x for t in T for x in t}
            if len(used) != r:
                continue                      # r is the number of USED coordinates
            if not is_linear(T):
                continue
            if not connected(T, r):
                continue
            sig = (k, r)
            n = fibre_size(r, T)
            ell = r - math.log2(n)
            c = k * BETA - ell
            rr, sh, edges, cyc, excess = invariants(T, r)
            rows.append((k, r, n, ell, c, c / BETA, sh, edges, cyc, excess, T))
        # keep the run bounded
        if len(rows) > 4000:
            break
    if len(rows) > 4000:
        break

# group by (k, r, cyc) and report the distinct c values seen
from collections import defaultdict
g = defaultdict(set)
for k, r, n, ell, c, cb, sh, edges, cyc, excess, T in rows:
    g[(k, r, cyc, excess)].add(round(c / BETA, 9))

print("# objects examined: %d" % len(rows))
print()
print("  k   r  cyc  excess   distinct c/beta values in this cell")
for key in sorted(g):
    k, r, cyc, excess = key
    vals = sorted(g[key])
    show = ", ".join("%.6f" % v for v in vals[:6]) + (" ..." if len(vals) > 6 else "")
    print("  %2d %3d %4d %7d   %s" % (k, r, cyc, excess, show))
