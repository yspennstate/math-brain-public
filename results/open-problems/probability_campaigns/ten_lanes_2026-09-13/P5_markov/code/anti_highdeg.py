"""High-degree targeted search: complements of small-degree regular graphs,
plus random regular graphs and a hill-climb that tries to beat K_n."""
import os, sys, itertools, random
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anti_search import K_value, adj_of, admissible, stats
from antivoter import pair_correlations, var_from_pairs
import networkx as nx

def cycle_partitions(n, minpart=3):
    def rec(rem, lo):
        if rem == 0: yield []; return
        for p in range(max(lo, minpart), rem + 1):
            if rem - p == 0 or rem - p >= minpart:
                for tail in rec(rem - p, p):
                    yield [p] + tail
    yield from rec(n, minpart)

def union_of_cycles(parts):
    G = nx.Graph(); off = 0
    for p in parts:
        for i in range(p):
            G.add_edge(off + i, off + (i + 1) % p)
        off += p
    return G

def comp(G):
    return nx.complement(G)

print("complement-degree families (r = n-1-d)")
print(f"{'n':>3} {'d':>2} {'family':32s} {'r':>3} {'Var':>16} {'K_n Var':>16}  cmp")
for n in range(6, 19):
    kv = K_value(n)
    rows = []
    # d = 1: perfect matching complement = cocktail party
    if n % 2 == 0:
        M = nx.Graph(); M.add_nodes_from(range(n))
        for i in range(0, n, 2): M.add_edge(i, i + 1)
        rows.append(("K_{n x 2} (comp perfect matching)", comp(M)))
    # d = 2: complements of disjoint unions of cycles
    for parts in cycle_partitions(n):
        rows.append(("comp of cycles " + "+".join(map(str, parts)), comp(union_of_cycles(parts))))
    # d = 3: sampled cubic complements
    if (n * 3) % 2 == 0 and n >= 4:
        seen = set()
        for _ in range(60):
            H = nx.random_regular_graph(3, n, seed=random.randint(0, 10**9))
            key = tuple(sorted(nx.to_numpy_array(H).sum(0)))  # placeholder
            rows.append(("comp of a cubic graph", comp(H)))
    for name, G in rows:
        if not admissible(G): continue
        if G.number_of_nodes() != n: continue
        adj = adj_of(G)
        g = pair_correlations(adj)
        V = var_from_pairs(adj, g)
        r = len(adj[0])
        if "cubic" in name and V != max(x[1] for x in [(name, V)]):
            pass
        print(f"{n:>3} {n-1-r:>2} {name:32s} {r:>3} {float(V):16.10f} {float(kv):16.10f}  "
              f"{'LOWER' if V < kv else ('EQUAL' if V == kv else 'HIGHER!!!')}")
    sys.stdout.flush()
