"""Open Problem 4.49(ii): the ratio inf_f psi(f) / (tau_2 * diameter) on named families, with a sparse LP
so that graphs of a few dozen vertices are reachable. The exhaustive scan over all connected graphs on
four to seven vertices put the maximum at exactly 2, attained by the complete graphs."""
import numpy as np, sys
from scipy.optimize import linprog
from scipy.sparse import coo_matrix
import networkx as nx


def inf_psi_sparse(G):
    nodes = list(G.nodes()); n = len(nodes); idx = {v: i for i, v in enumerate(nodes)}
    deg = np.array([G.degree(v) for v in nodes], float); pi = deg / deg.sum()
    edges = [(idx[u], idx[v]) for u, v in G.edges()]; m = len(edges)
    inc = [[] for _ in range(n)]
    for e, (i, j) in enumerate(edges):
        inc[i].append((e, 1.0)); inc[j].append((e, -1.0))
    NF, NU, T = 0, n * m, 2 * n * m
    nv = 2 * n * m + 1
    c = np.zeros(nv); c[T] = 1.0
    # conservation: for each source a, each vertex v
    r, col, val, beq = [], [], [], []
    row = 0
    for a in range(n):
        for v in range(n):
            for e, s in inc[v]:
                r.append(row); col.append(NF + a * m + e); val.append(s)
            beq.append((1.0 if a == v else 0.0) - pi[v]); row += 1
    Aeq = coo_matrix((val, (r, col)), shape=(row, nv))
    # |f| <= u  and congestion
    r, col, val, bub = [], [], [], []
    row = 0
    for a in range(n):
        for e in range(m):
            r += [row, row]; col += [NF + a * m + e, NU + a * m + e]; val += [1.0, -1.0]; bub.append(0.0); row += 1
            r += [row, row]; col += [NF + a * m + e, NU + a * m + e]; val += [-1.0, -1.0]; bub.append(0.0); row += 1
    condinv = 2.0 * m   # pi_i p_ij = 1/(2m) for a regular-weight simple walk on any graph
    for e in range(m):
        for a in range(n):
            r.append(row); col.append(NU + a * m + e); val.append(pi[a] * condinv)
        r.append(row); col.append(T); val.append(-1.0); bub.append(0.0); row += 1
    Aub = coo_matrix((val, (r, col)), shape=(row, nv))
    bounds = [(None, None)] * (2 * n * m) + [(0, None)]
    res = linprog(c, A_ub=Aub, b_ub=np.array(bub), A_eq=Aeq, b_eq=np.array(beq), bounds=bounds, method='highs')
    return res.fun if res.success else None


def tau2(G):
    A = nx.to_numpy_array(G); d = A.sum(1); P = A / d[:, None]
    ev = np.sort(np.linalg.eigvals(P).real)[::-1]
    return 1.0 / (1.0 - ev[1])


FAMS = []
for n in (8, 12, 16, 20):
    FAMS.append((f'complete K{n}', nx.complete_graph(n)))
for d in (3, 4):
    FAMS.append((f'hypercube Q{d}', nx.hypercube_graph(d)))
for n in (10, 16, 24):
    FAMS.append((f'cycle C{n}', nx.cycle_graph(n)))
for n in (10, 16):
    FAMS.append((f'path P{n}', nx.path_graph(n)))
for n in (12, 20):
    FAMS.append((f'star S{n}', nx.star_graph(n - 1)))
for a, b in ((3, 9), (5, 15)):
    FAMS.append((f'complete bipartite K{a},{b}', nx.complete_bipartite_graph(a, b)))
FAMS.append(('Petersen', nx.petersen_graph()))
for n in (8, 12, 16, 20):
    g = nx.random_regular_graph(3, n, seed=7)
    if nx.is_connected(g): FAMS.append((f'random cubic n={n}', g))
for k in (4, 6, 8):
    g = nx.barbell_graph(k, 1)
    FAMS.append((f'barbell {k}+{k}+path1', g))
for n in (9, 16):
    FAMS.append((f'grid {int(n**0.5)}x{int(n**0.5)}', nx.grid_2d_graph(int(n ** 0.5), int(n ** 0.5))))
FAMS.append(('2d torus 4x4', nx.grid_2d_graph(4, 4, periodic=True)))
FAMS.append(('2d torus 5x5', nx.grid_2d_graph(5, 5, periodic=True)))

print(f"{'family':26s} {'n':>4} {'m':>4} {'inf psi':>9} {'tau2':>9} {'diam':>5} {'psi/(tau2 D)':>13} {'psi/(tau2 log n)':>16}")
worst = []
for name, G in FAMS:
    G = nx.convert_node_labels_to_integers(G)
    if not nx.is_connected(G): continue
    n, m = G.number_of_nodes(), G.number_of_edges()
    if n * m > 2600:
        print(f"{name:26s} {n:>4} {m:>4}   (skipped, LP too large)"); continue
    ip = inf_psi_sparse(G)
    if ip is None:
        print(f"{name:26s} {n:>4} {m:>4}   (LP failed)"); continue
    t2 = tau2(G); D = nx.diameter(G)
    rd = ip / (t2 * D); rl = ip / (t2 * np.log(n))
    worst.append((rd, name))
    print(f"{name:26s} {n:>4} {m:>4} {ip:>9.4f} {t2:>9.4f} {D:>5} {rd:>13.4f} {rl:>16.4f}")
worst.sort(reverse=True)
print("\nlargest ratios:", ', '.join(f"{w[1]} {w[0]:.3f}" for w in worst[:5]))
