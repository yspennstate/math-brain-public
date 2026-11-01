#!/usr/bin/env python3
from itertools import combinations

def edge_list(n):
    return list(combinations(range(n), 2))

def pc(x):
    return x.bit_count()

def cut_mask(n, edges, bits):
    out = 0
    for i, (u, v) in enumerate(edges):
        if ((bits >> u) & 1) != ((bits >> v) & 1):
            out |= 1 << i
    return out

def degrees(n, edges, gmask):
    deg = [0] * n
    for i, (u, v) in enumerate(edges):
        if (gmask >> i) & 1:
            deg[u] += 1
            deg[v] += 1
    return deg

def verify_c203(nmax=6):
    graph_count = 0
    constrained_cases = 0
    for n in range(2, nmax + 1, 2):
        edges = edge_list(n)
        M = len(edges)
        spins = [b for b in range(1 << n) if (b & 1) == 0]
        cuts_full = [cut_mask(n, edges, b) for b in spins]
        balanced = [i for i, b in enumerate(spins) if pc(b) == n // 2]

        for gmask in range(1 << M):
            m = pc(gmask)
            cuts = [c & gmask for c in cuts_full]
            maxbis = max(pc(cuts[i]) for i in balanced)

            for si in balanced:
                sigma = spins[si]
                target = gmask ^ cuts[si]
                admissible = [
                    ei for ei, eta in enumerate(spins)
                    if pc(sigma ^ eta) == n // 2
                ]
                best = min(pc(cuts[ei] ^ target) for ei in admissible)
                assert best == m - maxbis, (n, gmask, si, best, m - maxbis)
                constrained_cases += 1

            graph_count += 1
    return graph_count, constrained_cases

def verify_c205():
    graph_count = 0
    extremal_bisection_reps = 0

    for n in (4, 6):
        edges = edge_list(n)
        M = len(edges)
        spins = [b for b in range(1 << n) if (b & 1) == 0]
        cuts_full = [cut_mask(n, edges, b) for b in spins]
        balanced = [i for i, b in enumerate(spins) if pc(b) == n // 2]

        for gmask in range(1 << M):
            if degrees(n, edges, gmask) != [3] * n:
                continue

            m = pc(gmask)
            cuts = [c & gmask for c in cuts_full]
            bvals = [pc(cuts[i]) for i in balanced]
            minbis = min(bvals)
            maxbis = max(bvals)
            maxcut = max(pc(c) for c in cuts)
            maxcut_idx = [i for i, c in enumerate(cuts) if pc(c) == maxcut]

            def phi(si):
                sigma = spins[si]
                best = None
                for ei in maxcut_idx:
                    eta = spins[ei]
                    F = gmask ^ cuts[ei]
                    residual = pc(F) - 2 * pc(F & cuts[si])
                    overlap = abs(n - 2 * pc(sigma ^ eta))
                    value = abs(residual) + 3 * overlap / 2
                    if best is None or value < best:
                        best = value
                return best

            phi_min = min(
                phi(i) for i in balanced if pc(cuts[i]) == minbis
            )
            phi_max = min(
                phi(i) for i in balanced if pc(cuts[i]) == maxbis
            )

            total = minbis + maxbis
            assert total >= m - phi_min
            assert total <= m + phi_max
            assert abs(total - m) <= max(phi_min, phi_max)

            extremal_bisection_reps += sum(
                v == minbis or v == maxbis for v in bvals
            )
            graph_count += 1

    return graph_count, extremal_bisection_reps

if __name__ == "__main__":
    c203 = verify_c203()
    c205 = verify_c205()
    print("C203_ORTHOGONAL_CUTSPACE_IDENTITY_PASS")
    print(f"graphs={c203[0]} constrained_balanced_sigma_cases={c203[1]}")
    print("C205_GAUGE_DECORRELATION_REDUCTION_PASS")
    print(f"cubic_graphs_n4_n6={c205[0]} extremal_bisection_reps={c205[1]}")
    print("ALL_EXACT_CHECKS_PASS")
    print("exit_code=0")
