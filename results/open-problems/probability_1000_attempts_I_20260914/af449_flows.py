"""Aldous and Fill, Open Problem 4.49(ii) (intake I row I0026).

Sinclair's inequality (4.49) reads  inf_f psi(f) <= K tau_2 log n,  where f = (f^(a)) ranges over
families of unit flows, f^(a) a unit flow from a to pi, and

    psi(f) = max over edges (i,j) of  sum_a pi_a |f^(a)_ij| / (pi_i p_ij).

Open Problem 4.49 asks (i) for a simple proof and (ii) whether log n may be replaced by the diameter.

inf_f psi(f) is a linear program: the flows are free variables, conservation is linear, and the max of
sums of absolute values is linearised with one auxiliary per (source, edge). So for small graphs the
quantity is exactly computable, and so are tau_2 = 1/gap and the diameter. This scans graphs and
reports the largest values of inf psi / (tau_2 * diameter), which is the ratio Open Problem 4.49(ii)
asks to be bounded.
"""
import numpy as np, sys, itertools
from scipy.optimize import linprog
import networkx as nx


def inf_psi(G):
    """exact inf over flow families of psi(f), for the simple random walk on G (discrete time)"""
    nodes = list(G.nodes()); n = len(nodes); idx = {v: i for i, v in enumerate(nodes)}
    deg = np.array([G.degree(v) for v in nodes], float)
    pi = deg / deg.sum()
    edges = [(idx[u], idx[v]) for u, v in G.edges()]
    m = len(edges)
    # conductance pi_i p_ij = deg_i/(2m) * 1/deg_i = 1/(2m) for the simple walk: the same for every edge
    cond = np.full(m, 1.0 / (2 * m))
    # variables: f[a, e] (signed, m*n), u[a, e] (abs, m*n), t  -> total 2*n*m + 1
    NF, NU, T = 0, n * m, 2 * n * m
    nv = 2 * n * m + 1
    c = np.zeros(nv); c[T] = 1.0
    Aeq, beq = [], []
    for a in range(n):
        for v in range(n):
            row = np.zeros(nv)
            for e, (i, j) in enumerate(edges):
                if i == v: row[NF + a * m + e] = 1.0      # flow leaves v along e
                elif j == v: row[NF + a * m + e] = -1.0
            Aeq.append(row); beq.append((1.0 if a == v else 0.0) - pi[v])
    Aub, bub = [], []
    for a in range(n):
        for e in range(m):
            r1 = np.zeros(nv); r1[NF + a * m + e] = 1.0; r1[NU + a * m + e] = -1.0
            r2 = np.zeros(nv); r2[NF + a * m + e] = -1.0; r2[NU + a * m + e] = -1.0
            Aub += [r1, r2]; bub += [0.0, 0.0]
    for e in range(m):
        r = np.zeros(nv)
        for a in range(n): r[NU + a * m + e] = pi[a] / cond[e]
        r[T] = -1.0
        Aub.append(r); bub.append(0.0)
    bounds = [(None, None)] * (2 * n * m) + [(0, None)]
    res = linprog(c, A_ub=np.array(Aub), b_ub=np.array(bub), A_eq=np.array(Aeq), b_eq=np.array(beq),
                  bounds=bounds, method='highs')
    return res.fun if res.success else None


def tau2(G):
    """relaxation time of the simple random walk (discrete time): 1/(1 - second largest eigenvalue)"""
    A = nx.to_numpy_array(G); d = A.sum(1)
    P = A / d[:, None]
    ev = np.linalg.eigvals(P)
    ev = np.sort(ev.real)[::-1]
    lam2 = ev[1]
    return 1.0 / (1.0 - lam2) if lam2 < 1 - 1e-12 else np.inf


if __name__ == '__main__':
    nmin = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    nmax = int(sys.argv[2]) if len(sys.argv) > 2 else 7
    from networkx.generators.atlas import graph_atlas_g
    best = []
    for G in graph_atlas_g():
        n = G.number_of_nodes()
        if n < nmin or n > nmax or not nx.is_connected(G) if n else True:
            continue
        if n < 2: continue
        try:
            if not nx.is_connected(G): continue
        except Exception:
            continue
        ip = inf_psi(G)
        if ip is None: continue
        t2 = tau2(G); D = nx.diameter(G)
        best.append((ip / (t2 * D), ip, t2, D, n, nx.to_graph6_bytes(G, header=False).strip().decode()))
    best.sort(reverse=True)
    print(f"{len(best)} connected graphs on {nmin}..{nmax} vertices")
    print(f"{'psi/(tau2*diam)':>16} {'inf psi':>9} {'tau2':>8} {'diam':>5} {'n':>3}  graph6")
    for r in best[:12]:
        print(f"{r[0]:>16.4f} {r[1]:>9.3f} {r[2]:>8.3f} {r[3]:>5} {r[4]:>3}  {r[5]}")
    print("\nby vertex count, the maximum ratio:")
    for n in range(nmin, nmax + 1):
        s = [r for r in best if r[4] == n]
        if s: print(f"  n={n}: max {s[0][0]:.4f}  (inf psi {s[0][1]:.3f}, tau2 {s[0][2]:.3f}, diam {s[0][3]}, {s[0][5]})")
