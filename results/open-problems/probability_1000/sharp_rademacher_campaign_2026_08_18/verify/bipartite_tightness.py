"""Bipartiteness does both jobs. Check that, and check the rank claim it rests on.

Two facts, both about the SAME property of the sharing graph G:

 (1) Z = < prod_edges (1 - x_u x_v / 3) > is LARGE when G is bipartite, because the two
     configurations aligned with the bipartition make every factor 4/3 at once:
         Z >= 2 (4/3)^E / 2^V.
 (2) The pair-sum residual family {e_x + e_y : xy in E} has rank
         |V| - (number of BIPARTITE components),
     the classical unsigned-incidence rank. So d_cb <= |V| - 1 for connected bipartite G,
     one less than for non-bipartite.

RC needs c = log2 Z <= beta (k - d_cb). On a dense bipartite G with k = E triangles,
     log2 Z ~ E*beta - V + 1,  so  ell = k*beta - c ~ V - 1,
and with d_cb <= V - 1 the tightness is
     d_cb * beta / ell  ~  (V-1) beta / (V-1)  =  beta = 0.415,
comfortably below 1 and independent of how dense the graph is.

Checks here:
  A. the rank formula, against exact rank computation, on bipartite and non-bipartite graphs
  B. Z >= 2(4/3)^E/2^V, and how tight that lower bound is
  C. the resulting tightness bound on K_{n,n} and on other dense bipartite graphs
  D. the NON-bipartite comparison: does tightness stay below 1 there too?
"""
import itertools
import math
from fractions import Fraction

BETA = math.log2(4.0 / 3.0)


def rank_pairsums(edges):
    verts = sorted({v for e in edges for v in e})
    idx = {v: i for i, v in enumerate(verts)}
    rows = []
    for (a, b) in edges:
        row = [Fraction(0)] * len(verts)
        row[idx[a]] += 1
        row[idx[b]] += 1
        rows.append(row)
    r = 0
    ncol = len(verts)
    for c in range(ncol):
        piv = None
        for i in range(r, len(rows)):
            if rows[i][c] != 0:
                piv = i
                break
        if piv is None:
            continue
        rows[r], rows[piv] = rows[piv], rows[r]
        pr = rows[r]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c] / pr[c]
                rows[i] = [x - f * y for x, y in zip(rows[i], pr)]
        r += 1
    return r, len(verts)


def is_bipartite(edges):
    adj = {}
    for a, b in edges:
        adj.setdefault(a, []).append(b)
        adj.setdefault(b, []).append(a)
    col = {}
    for s in adj:
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


def Z_exact(edges):
    verts = sorted({v for e in edges for v in e})
    idx = {v: i for i, v in enumerate(verts)}
    n = len(verts)
    tot = Fraction(0)
    for bits in range(1 << n):
        p = Fraction(1)
        for (a, b) in edges:
            xa = 1 if (bits >> idx[a]) & 1 else -1
            xb = 1 if (bits >> idx[b]) & 1 else -1
            p *= Fraction(3 - xa * xb, 3)
        tot += p
    return tot / Fraction(2) ** n


GRAPHS = {}
for n in (2, 3, 4):
    GRAPHS["K_%d,%d" % (n, n)] = [(("u", i), ("v", j)) for i in range(n) for j in range(n)]
GRAPHS["C4"] = [((0,), (1,)), ((1,), (2,)), ((2,), (3,)), ((3,), (0,))]
GRAPHS["C5 (odd)"] = [((i,), ((i + 1) % 5,)) for i in range(5)]
GRAPHS["C6"] = [((i,), ((i + 1) % 6,)) for i in range(6)]
GRAPHS["K4 (odd)"] = [((a,), (b,)) for a, b in itertools.combinations(range(4), 2)]
GRAPHS["Petersen-ish K3,3"] = [(("u", i), ("v", j)) for i in range(3) for j in range(3)]
GRAPHS["cube Q3"] = []
for a in range(8):
    for bit in range(3):
        b = a ^ (1 << bit)
        if a < b:
            GRAPHS["cube Q3"].append(((a,), (b,)))

print("  graph            V   E   bip   rank(pairsums)  V-bipcomps   Z            log2Z      ell      tightness<=")
for name, edges in GRAPHS.items():
    rk, V = rank_pairsums(edges)
    E = len(edges)
    bip = is_bipartite(edges)
    pred_rank = V - 1 if bip else V     # connected assumed for these
    if V > 12:
        print("  %-16s V=%d too big for exact Z" % (name, V))
        continue
    Z = float(Z_exact(edges))
    c = math.log2(Z)
    k = E
    ell = k * BETA - c
    tight = rk * BETA / ell if ell > 0 else float("inf")
    print("  %-16s %3d %3d  %-5s %10d %12d    %-11.6f %+8.4f  %7.4f   %7.4f  %s"
          % (name, V, E, "yes" if bip else "no", rk, pred_rank, Z, c, ell, tight,
             "RANK OK" if rk == pred_rank else "*** RANK FORMULA WRONG"))

print()
print("  K_{n,n} asymptotics: d_cb <= 2n-1 from the pair-sum family, budget (2n-1)/beta ~ 4.82n")
for n in range(2, 13):
    k = n * n
    tot = Fraction(0)
    for p in range(n + 1):
        for q in range(n + 1):
            same = p * q + (n - p) * (n - q)
            diff = p * (n - q) + (n - p) * q
            tot += Fraction(math.comb(n, p) * math.comb(n, q)) * Fraction(2, 3) ** same * Fraction(4, 3) ** diff
    Z = float(tot / Fraction(2) ** (2 * n))
    c = math.log2(Z)
    ell = k * BETA - c
    dcb_bound = 2 * n - 1
    print("   n=%2d  k=%3d  ell=%8.4f  d_cb<=%3d  tightness <= %.4f   %s"
          % (n, k, ell, dcb_bound, dcb_bound * BETA / ell,
             "RC HOLDS" if dcb_bound * BETA / ell <= 1 else "*** RC AT RISK"))
