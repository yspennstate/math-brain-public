#!/usr/bin/env python3
"""
Corroborative checker for PROB20-13 distance-regular theorem.

For each supplied graph:
  * verifies the distance-regular intersection-number definition;
  * constructs the radial source flows from the run report;
  * checks div f^x = delta_x - uniform;
  * checks all weighted absolute edge loads are equal;
  * checks psi = 2 * mean graph distance;
  * solves the metric LP dual with scipy and compares.

Floating-point checks are corroborative only; the proof is in the Markdown report.
"""
import itertools
import numpy as np
import networkx as nx
from scipy.optimize import linprog

TOL = 1e-9

def normalize(G):
    return nx.convert_node_labels_to_integers(nx.Graph(G))

def distance_regular_data(G):
    G = normalize(G)
    n = G.number_of_nodes()
    if not nx.is_connected(G):
        raise ValueError("graph not connected")
    degrees = [G.degree(v) for v in G]
    if len(set(degrees)) != 1:
        raise ValueError("graph not regular")
    k = degrees[0]
    dist = dict(nx.all_pairs_shortest_path_length(G))
    D = max(max(row.values()) for row in dist.values())

    params = {}
    k_layers = None
    for x in G:
        layers = [[y for y in G if dist[x][y] == r] for r in range(D + 1)]
        sizes = tuple(len(L) for L in layers)
        if k_layers is None:
            k_layers = sizes
        elif sizes != k_layers:
            raise ValueError("distance-layer sizes depend on base vertex")

        for r in range(D + 1):
            for y in layers[r]:
                counts = [0,0,0]
                for z in G.neighbors(y):
                    dz = dist[x][z]
                    if dz == r-1: counts[0] += 1
                    elif dz == r: counts[1] += 1
                    elif dz == r+1: counts[2] += 1
                    else:
                        raise ValueError("edge jumps more than one layer")
                val = tuple(counts)
                if r not in params:
                    params[r] = val
                elif params[r] != val:
                    raise ValueError(f"not distance-regular at radius {r}: {params[r]} vs {val}")
    return G, dist, D, k, k_layers, params

def radial_flows(G):
    G, dist, D, k, k_layers, params = distance_regular_data(G)
    n = G.number_of_nodes()
    edges = [tuple(sorted(e)) for e in G.edges()]
    edge_index = {e:i for i,e in enumerate(edges)}
    flows = np.zeros((n, len(edges)), dtype=float)

    M = [sum(k_layers[t] for t in range(r+1, D+1)) for r in range(D)]
    q = []
    for r in range(D):
        b_r = params[r][2]
        q.append(M[r] / (n * k_layers[r] * b_r))

    for x in G:
        for u,v in G.edges():
            du,dv = dist[x][u], dist[x][v]
            if abs(du-dv) != 1:
                continue
            if du < dv:
                a,b = u,v
                amount = q[du]
            else:
                a,b = v,u
                amount = q[dv]
            e = tuple(sorted((u,v)))
            sign = +1 if (a,b) == e else -1
            flows[x, edge_index[e]] = sign * amount

    for x in G:
        div = np.zeros(n)
        for e_idx,(u,v) in enumerate(edges):
            val = flows[x,e_idx]
            div[u] += val
            div[v] -= val
        target = np.full(n, -1/n)
        target[x] += 1
        assert np.max(np.abs(div-target)) < TOL, (x,div,target)

    loads = np.mean(np.abs(flows), axis=0)
    assert np.max(loads)-np.min(loads) < TOL

    m = G.number_of_edges()
    capacity = 1/(2*m)
    psi = float(np.max(loads)/capacity)
    mean_d = sum(dist[x][y] for x in G for y in G)/(n*n)
    assert abs(psi - 2*mean_d) < 1e-8
    return psi, mean_d, loads

def metric_lp_F(G):
    G = normalize(G)
    n = G.number_of_nodes()
    m = G.number_of_edges()
    deg = np.array([G.degree(i) for i in range(n)], dtype=float)
    pi = deg/(2*m)
    pairs = [(i,j) for i in range(n) for j in range(i+1,n)]
    idx = {p:t for t,p in enumerate(pairs)}
    N = len(pairs)
    c = np.array([-2*pi[i]*pi[j] for i,j in pairs])

    A, b = [], []
    for i,j,k in itertools.combinations(range(n),3):
        ij,ik,jk = idx[(i,j)],idx[(i,k)],idx[(j,k)]
        for pos,a1,a2 in [(ij,ik,jk),(ik,ij,jk),(jk,ij,ik)]:
            row = np.zeros(N)
            row[pos] = 1
            row[a1] -= 1
            row[a2] -= 1
            A.append(row); b.append(0.0)

    row = np.zeros(N)
    for u,v in G.edges():
        row[idx[tuple(sorted((u,v)))]] += 1/(2*m)
    A.append(row); b.append(1.0)

    res = linprog(c, A_ub=np.array(A), b_ub=np.array(b),
                  bounds=[(0,None)]*N, method="highs")
    assert res.success
    return -res.fun

def examples():
    out = []
    out.append(("K5", nx.complete_graph(5)))
    out.append(("C7", nx.cycle_graph(7)))
    out.append(("Q3", nx.hypercube_graph(3)))
    out.append(("Petersen", nx.petersen_graph()))
    out.append(("K4,4", nx.complete_bipartite_graph(4,4)))
    P = nx.Graph(nx.paley_graph(13))
    P.remove_edges_from(nx.selfloop_edges(P))
    out.append(("Paley13", P))
    return out

if __name__ == "__main__":
    for name,G in examples():
        G = normalize(G)
        psi,mean_d,loads = radial_flows(G)
        F_lp = metric_lp_F(G)
        D = nx.diameter(G)
        print(f"{name:10s} n={len(G):2d} D={D}  radial psi={psi:.12g} "
              f"2mean={2*mean_d:.12g} LP={F_lp:.12g}")
        assert abs(F_lp-psi) < 1e-7
    print("ALL CORROBORATIVE CHECKS PASSED")
