"""Search for a regular graph beating K_n in stationary antivoter variance."""
import os, sys, itertools, random
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from antivoter import pair_correlations, var_from_pairs, var_edge_identity, mk, complete, cycle
import networkx as nx
import numpy as np

def K_value(n):
    return F(n * (n - 2), 2 * n - 3)

def adj_of(G):
    n = G.number_of_nodes()
    return [set(G.neighbors(i)) for i in range(n)]

def admissible(G):
    n = G.number_of_nodes()
    if not nx.is_connected(G): return False
    if nx.is_bipartite(G): return False
    degs = set(dict(G.degree()).values())
    if len(degs) != 1: return False
    r = degs.pop()
    if r == 2: return False          # the n-cycle is excluded by the source
    return True

def stats(G):
    adj = adj_of(G)
    n = len(adj); r = len(adj[0])
    g = pair_correlations(adj)
    V = var_from_pairs(adj, g)
    assert V == var_edge_identity(adj, g)
    # cherry identity:  pbar = (1-1/r)(1-qbar)
    pbar = V / n
    num = F(0); cnt = 0
    for i in range(n):
        for j, k in itertools.permutations(sorted(adj[i]), 2):
            a, b = (j, k) if j < k else (k, j)
            num += (1 + g[(a, b)]) / 2
            cnt += 1
    qbar = num / cnt
    lhs = (1 - F(1, r)) * (1 - qbar)
    assert lhs == pbar, (lhs, pbar)
    ev = np.linalg.eigvalsh(nx.to_numpy_array(G, nodelist=range(n)))
    lam2 = sorted(ev)[-2]
    bound = n * n * (r + lam2) / (2 * r * n - r + lam2)
    return dict(n=n, r=r, var=V, pbar=pbar, qbar=qbar, lam2=lam2, specbound=bound)

# ---- exhaustive labelled enumeration of r-regular graphs on n vertices ----
def gen_regular(n, r):
    """Yield edge sets (frozenset of pairs) of all labelled r-regular graphs."""
    rem = [r] * n
    edges = []
    def rec(v):
        while v < n and rem[v] == 0:
            v += 1
        if v == n:
            yield tuple(edges); return
        cand = [u for u in range(v + 1, n) if rem[u] > 0]
        need = rem[v]
        if len(cand) < need: return
        for combo in itertools.combinations(cand, need):
            for u in combo: rem[u] -= 1
            rem[v] = 0
            edges.extend((v, u) for u in combo)
            yield from rec(v + 1)
            del edges[len(edges) - need:]
            rem[v] = need
            for u in combo: rem[u] += 1
    yield from rec(0)

def exhaustive(n, verbose=True):
    best = None; results = []
    for r in range(3, n):
        if (n * r) % 2: continue
        seen = {}     # invariant -> list of representative graphs
        classes = []
        for es in gen_regular(n, r):
            G = nx.Graph(); G.add_nodes_from(range(n)); G.add_edges_from(es)
            if not admissible(G): continue
            ev = np.linalg.eigvalsh(nx.to_numpy_array(G, nodelist=range(n)))
            key = tuple(np.round(np.sort(ev), 6)) + (sum(nx.triangles(G).values()),)
            bucket = seen.setdefault(key, [])
            if any(nx.is_isomorphic(G, H) for H in bucket): continue
            bucket.append(G); classes.append(G)
        for G in classes:
            s = stats(G); results.append(s)
            if best is None or s['var'] > best['var']: best = s
        if verbose:
            print(f"  n={n} r={r}: {len(classes)} admissible iso-classes")
    return best, results

if __name__ == "__main__":
    lo, hi = int(sys.argv[1]), int(sys.argv[2])
    for n in range(lo, hi + 1):
        best, res = exhaustive(n)
        kv = K_value(n)
        print(f"n={n}  K_n Var = {kv} = {float(kv):.8f}   best found = {best['var']} "
              f"= {float(best['var']):.8f} at r={best['r']}  -> "
              f"{'K_n IS MAX' if best['var'] == kv else 'BEATS K_n!!'}")
        top = sorted(res, key=lambda s: -s['var'])[:5]
        for s in top:
            print(f"     r={s['r']} var={s['var']}={float(s['var']):.8f} "
                  f"qbar={float(s['qbar']):.6f} lam2={s['lam2']:.4f} specbound={s['specbound']:.6f}")
        sys.stdout.flush()
