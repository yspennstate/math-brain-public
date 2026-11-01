#!/usr/bin/env python3
from itertools import combinations, product

def edge_list(n):
    return list(combinations(range(n), 2))

def popcount(x):
    return x.bit_count()

def spins_mod_global_flip(n):
    # Fix vertex 0 to +1; cut vector is unchanged by global spin flip.
    return [(1,) + bits for bits in product((-1, 1), repeat=n-1)]

def cut_mask(edges, spins):
    mask = 0
    for i, (u, v) in enumerate(edges):
        if spins[u] != spins[v]:
            mask |= 1 << i
    return mask

def graph_degrees(n, edges, gmask):
    deg = [0] * n
    for i, (u, v) in enumerate(edges):
        if (gmask >> i) & 1:
            deg[u] += 1
            deg[v] += 1
    return deg

def is_bipartite(n, edges, gmask):
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        if (gmask >> i) & 1:
            adj[u].append(v)
            adj[v].append(u)
    color = [None] * n
    for root in range(n):
        if color[root] is not None:
            continue
        color[root] = 0
        stack = [root]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if color[v] is None:
                    color[v] = color[u] ^ 1
                    stack.append(v)
                elif color[v] == color[u]:
                    return False
    return True

def verify_cutspace_identity(nmax=5):
    total_graphs = total_sigma = total_tau_tests = bipartite_graphs = 0
    for n in range(2, nmax + 1):
        edges = edge_list(n)
        M = len(edges)
        spins = spins_mod_global_flip(n)
        full_cut_masks = [cut_mask(edges, s) for s in spins]
        for gmask in range(1 << M):
            m = popcount(gmask)
            cuts = [cm & gmask for cm in full_cut_masks]
            maxcut = max(popcount(c) for c in cuts)
            q = m - maxcut

            # C202: for every cut C_sigma,
            # min_tau d_H(C_tau, E\C_sigma) = |E|-MaxCut(G).
            for Csigma in cuts:
                complement = gmask ^ Csigma
                best = min(popcount(Ctau ^ complement) for Ctau in cuts)
                assert best == q, (n, gmask, Csigma, best, q)
                total_sigma += 1
                total_tau_tests += len(cuts)

            # The distance vanishes iff the graph is bipartite.
            bip = is_bipartite(n, edges, gmask)
            assert (q == 0) == bip, (n, gmask, q, bip)
            bipartite_graphs += int(bip)
            total_graphs += 1
    return total_graphs, total_sigma, total_tau_tests, bipartite_graphs

def verify_cubic_frustration_matching():
    checked_graphs = checked_maxcuts = 0
    for n in (4, 6):
        edges = edge_list(n)
        M = len(edges)
        spins = spins_mod_global_flip(n)
        full_cut_masks = [cut_mask(edges, s) for s in spins]
        for gmask in range(1 << M):
            if graph_degrees(n, edges, gmask) != [3] * n:
                continue
            cuts = [cm & gmask for cm in full_cut_masks]
            maxcut = max(popcount(c) for c in cuts)
            for Ceta in cuts:
                if popcount(Ceta) != maxcut:
                    continue
                F = gmask ^ Ceta  # uncut / frustration edges
                degF = [0] * n
                for i, (u, v) in enumerate(edges):
                    if (F >> i) & 1:
                        degF[u] += 1
                        degF[v] += 1
                # C204: in any maximum cut of a cubic graph,
                # no vertex has two uncut incident edges.
                assert max(degF, default=0) <= 1, (n, gmask, Ceta, degF)
                checked_maxcuts += 1
            checked_graphs += 1
    return checked_graphs, checked_maxcuts

def verify_gauge_formula(nmax=5):
    # For every G, sigma, eta:
    # cut(sigma*eta) = m-cut(sigma)-sum_{e in F_eta} sigma_u sigma_v.
    checks = 0
    for n in range(2, nmax + 1):
        edges = edge_list(n)
        M = len(edges)
        spins = spins_mod_global_flip(n)
        for gmask in range(1 << M):
            m = popcount(gmask)
            gedges = [edges[i] for i in range(M) if (gmask >> i) & 1]
            for sigma in spins:
                cut_sigma = sum(sigma[u] != sigma[v] for u, v in gedges)
                for eta in spins:
                    tau = tuple(sigma[i] * eta[i] for i in range(n))
                    cut_tau = sum(tau[u] != tau[v] for u, v in gedges)
                    residual = sum(
                        sigma[u] * sigma[v]
                        for u, v in gedges
                        if eta[u] == eta[v]
                    )
                    assert cut_tau == m - cut_sigma - residual, (
                        n, gmask, sigma, eta, cut_tau, m-cut_sigma-residual
                    )
                    checks += 1
    return checks

if __name__ == "__main__":
    a = verify_cutspace_identity(5)
    b = verify_cubic_frustration_matching()
    c = verify_gauge_formula(5)
    print("C202_CUTSPACE_IDENTITY_PASS")
    print(f"graphs={a[0]} sigma_cases={a[1]} tau_distance_tests={a[2]} bipartite_graphs={a[3]}")
    print("C204_CUBIC_MAXCUT_FRUSTRATION_MATCHING_PASS")
    print(f"cubic_graphs_n4_n6={b[0]} maximum_cut_colorings={b[1]}")
    print("GAUGE_FORMULA_PASS")
    print(f"gauge_formula_checks={c}")
    print("ALL_EXACT_CHECKS_PASS")
