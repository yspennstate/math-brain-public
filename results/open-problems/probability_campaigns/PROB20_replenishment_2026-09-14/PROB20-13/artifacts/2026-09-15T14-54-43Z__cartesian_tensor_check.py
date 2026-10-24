"""
PROB20-13 corroborative checker for the exact regular Cartesian-product theorem.

This script is NOT a proof. It solves the finite metric LP numerically on
selected small regular graphs and compares

    F(G □ H)

against the exact theorem prediction

    max((r+s)/r * F(G), (r+s)/s * F(H)).

It also checks the relaxation-time formula

    tau(G □ H) = max((r+s)/r tau(G), (r+s)/s tau(H)).

Requires: networkx, numpy, scipy.
"""

import itertools
import numpy as np
import networkx as nx
from scipy.optimize import linprog


def metric_dual_F(G):
    G = nx.convert_node_labels_to_integers(G)
    n = len(G)
    m = G.number_of_edges()

    A = nx.to_numpy_array(G, dtype=float)
    deg = A.sum(axis=1)
    pi = deg / (2 * m)

    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    idx = {p: k for k, p in enumerate(pairs)}
    N = len(pairs)

    # Maximize E_{pi x pi} d = 2 sum_{i<j} pi_i pi_j d_ij.
    objective = np.array([-2 * pi[i] * pi[j] for i, j in pairs])

    A_ub = []
    b_ub = []

    # Metric triangle inequalities.
    for i, j, k in itertools.combinations(range(n), 3):
        ij = idx[(i, j)]
        ik = idx[(i, k)]
        jk = idx[(j, k)]

        row = np.zeros(N)
        row[ij] = 1
        row[ik] -= 1
        row[jk] -= 1
        A_ub.append(row)
        b_ub.append(0)

        row = np.zeros(N)
        row[ik] = 1
        row[ij] -= 1
        row[jk] -= 1
        A_ub.append(row)
        b_ub.append(0)

        row = np.zeros(N)
        row[jk] = 1
        row[ij] -= 1
        row[ik] -= 1
        A_ub.append(row)
        b_ub.append(0)

    # Normalize E_{pi P} d = (1/m) sum_{uv in E} d_uv <= 1.
    row = np.zeros(N)
    for u, v in G.edges():
        row[idx[tuple(sorted((u, v)))]] += 1 / m
    A_ub.append(row)
    b_ub.append(1)

    res = linprog(
        objective,
        A_ub=np.array(A_ub),
        b_ub=np.array(b_ub),
        bounds=[(0, None)] * N,
        method="highs",
    )
    assert res.success, res.message

    # F = 2 * sup E_{pi pi} d / E_{pi P} d.
    return -2 * res.fun


def tau_rel(G):
    A = nx.to_numpy_array(G, dtype=float)
    deg = A.sum(axis=1)
    S = A / np.sqrt(np.outer(deg, deg))
    vals = np.linalg.eigvalsh(S)
    lam2 = np.sort(vals)[-2]
    return 1 / (1 - lam2)


def regular_degree(G):
    ds = {d for _, d in G.degree()}
    assert len(ds) == 1
    return next(iter(ds))


examples = [
    ("C3", nx.cycle_graph(3), "C4", nx.cycle_graph(4)),
    ("C3", nx.cycle_graph(3), "C5", nx.cycle_graph(5)),
    ("K3", nx.complete_graph(3), "Petersen", nx.petersen_graph()),
    ("C4", nx.cycle_graph(4), "K4", nx.complete_graph(4)),
]

for name_g, G, name_h, H in examples:
    r = regular_degree(G)
    s = regular_degree(H)

    FG = metric_dual_F(G)
    FH = metric_dual_F(H)

    K = nx.convert_node_labels_to_integers(nx.cartesian_product(G, H))
    FK = metric_dual_F(K)

    predicted_F = max((r + s) / r * FG, (r + s) / s * FH)

    tauG = tau_rel(G)
    tauH = tau_rel(H)
    tauK = tau_rel(K)
    predicted_tau = max(
        (r + s) / r * tauG,
        (r + s) / s * tauH,
    )

    print(f"{name_g} □ {name_h}")
    print("  F direct:    ", FK)
    print("  F predicted: ", predicted_F)
    print("  tau direct:  ", tauK)
    print("  tau predicted:", predicted_tau)

    assert abs(FK - predicted_F) < 1e-8
    assert abs(tauK - predicted_tau) < 1e-8

print("All corroborative checks passed.")
