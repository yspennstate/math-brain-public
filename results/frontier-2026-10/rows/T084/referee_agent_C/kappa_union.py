"""Edge-support version of kappa.py, for any graph.

N = Z_e Z_f - Z Z_ef is a signed sum over edge-set pairs (A, B): A ∋ e, B ∋ f with sign +, and A arbitrary,
B ⊇ {e, f} with sign -, each weighted lam^(|A|+|B|) q^(k(A)+k(B)). Grouping pairs by H = A ∪ B gives
N_G = sum over H ⊆ G of K(H), where K(H) uses only the pairs with A ∪ B = H exactly. On a fixed vertex set,
k(A) = n - rank(A), so K(H)'s q-powers sit at 2n - |A| - |B| + (cycle rank), and isolated vertices only shift
them. If D3 holds for K(H) - the q-series of K(H)/(1-q)^2 has no negative coefficient at any lam power - for
every H containing e and f, it holds for every G, since a sum of such series has none either.

This script tests that for every graph H on V <= VMAX vertices up to isomorphism (networkx atlas), every edge
pair e, f in H, by direct enumeration of the 3^|E(H)| pairs with A ∪ B = H.
python kappa_union.py VMAX MMAX"""
import sys, itertools
import networkx as nx
from d3 import series_ok_dict

VMAX, MMAX = int(sys.argv[1]), int(sys.argv[2])


def rank(n, edges):
    par = list(range(n))

    def f(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    r = 0
    for a, b in edges:
        x, y = f(a), f(b)
        if x != y:
            par[x] = y
            r += 1
    return r


def K_of(n, E, e, f):
    """K(H) as {(lam power, u power): coeff}, H = (n, E) with every edge used by A or B."""
    m = len(E)
    rk = {}
    poly = {}  # (lam, q) -> coeff
    ie, jf = E.index(e), E.index(f)
    # each edge: in A only (1), B only (2), both (3)
    for lab in itertools.product((1, 2, 3), repeat=m):
        A = [E[k] for k in range(m) if lab[k] & 1]
        B = [E[k] for k in range(m) if lab[k] & 2]
        inA_e, inB_f = lab[ie] & 1, lab[jf] & 2
        inB_e = lab[ie] & 2
        sgn = 0
        if inA_e and inB_f:
            sgn += 1
        if inB_e and inB_f:
            sgn -= 1
        if not sgn:
            continue
        ka = rk.setdefault(tuple(A), n - rank(n, A))
        kb = rk.setdefault(tuple(B), n - rank(n, B))
        key = (len(A) + len(B), ka + kb)
        poly[key] = poly.get(key, 0) + sgn
    # to (lam, u): q^s = (1-u)^s
    from math import comb
    out = {}
    for (i, s), c in poly.items():
        if not c:
            continue
        for k in range(s + 1):
            out[(i, k)] = out.get((i, k), 0) + c * comb(s, k) * (-1) ** k
    return {k: v for k, v in out.items() if v}


seen = bad = zero = 0
for G in nx.graph_atlas_g():
    n, m = G.number_of_nodes(), G.number_of_edges()
    if n < 3 or n > VMAX or m < 2 or m > MMAX:
        continue
    if any(d == 0 for _, d in G.degree()):
        continue  # isolated vertices only shift q-powers; the graph without them is in the atlas
    E = [tuple(sorted(x)) for x in G.edges()]
    for e, f in itertools.permutations(E, 2):
        K = K_of(n, E, e, f)
        if not K:
            zero += 1
            continue
        seen += 1
        neg, _ = series_ok_dict(K)
        if neg:
            bad += 1
            if bad <= 8:
                print('NEG n', n, 'E', E, 'e', e, 'f', f, neg[:3], flush=True)
print('graphs up to %d vertices, %d edges, no isolated vertex: pairs with K != 0: %d, K = 0: %d, failures %d'
      % (VMAX, MMAX, seen, zero, bad))
