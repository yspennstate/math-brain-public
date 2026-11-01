"""Independent exact checks of the unbounded-terminal/core-three theorem.

The direct checker enumerates subsets of the original graph's unmarked
edges and tests the two marked edges by disjoint-set connectivity.  It
does not use the frontier transfer or the claimed closed formula to
calculate A, B, or C.
"""
from fractions import Fraction
from math import comb
from pathlib import Path
import json


def closed_rayleigh(m, a, p, q, r):
    d = 1 + 3 * a
    X = p + q + r
    tree_weight = p * q + p * r + q * r
    L = 3 + 2 * X
    S = 1 + X + tree_weight
    bracket = (d ** 2 * (L ** 2 - 6 * S)
               + 6 * a * d * (1 + m * a) * L
               + 9 * a ** 2 + 30 * m * a ** 3 + 18 * m ** 2 * a ** 4)
    return 4 * a ** 4 * d ** (2 * m - 8) * bracket


def transfer_coefficients(m, a, p, q, r):
    """Closed nilpotent-transfer expressions, separate from subset checker."""
    d, h = 1 + 3 * a, 1 + 6 * a
    X, tree_weight = p + q + r, p * q + p * r + q * r
    L, S = 3 + 2 * X, 1 + X + tree_weight
    u, v = Fraction(a ** 2, d), Fraction(a ** 3, d)
    w, z = Fraction(4 * a ** 2, h), Fraction(8 * a ** 3, h)
    A = d ** m * (S + m * u * L + m * v + 3 * m * (m - 1) * u ** 2)
    b = m - 2
    B = h * d ** b * (S + (b * u + w) * L
        + b * v + z + 3 * b * (b - 1) * u ** 2 + 6 * b * u * w)
    c = m - 4
    C = h ** 2 * d ** c * (S + (c * u + 2 * w) * L
        + c * v + 2 * z + 3 * c * (c - 1) * u ** 2
        + 12 * c * u * w + 6 * w ** 2)
    return A, B, C


def direct_subset_coefficients(m, a, p, q, r):
    n = m + 3
    core = [m, m + 1, m + 2]
    edges = [(core[0], core[1], p), (core[0], core[2], q), (core[1], core[2], r)]
    edges += [(terminal, v, a) for terminal in range(m) for v in core]
    marked = [(0, 1), (2, 3)]
    totals = [0, 0, 0, 0]
    for mask in range(1 << len(edges)):
        if mask.bit_count() > n - 1:
            continue
        parent = list(range(n))

        def root(v):
            while parent[v] != v:
                v = parent[v]
            return v

        weight = 1
        for i, (u, v, w) in enumerate(edges):
            if mask >> i & 1:
                u, v = root(u), root(v)
                if u == v:
                    break
                parent[u] = v
                weight *= w
        else:
            if not weight:
                continue
            totals[0] += weight
            u, v = (root(i) for i in marked[0])
            x, y = (root(i) for i in marked[1])
            if u != v:
                totals[1] += weight
            if x != y:
                totals[2] += weight
            if u != v and x != y:
                # Adding e merges precisely the two roots u,v.  f fails
                # only if its roots were those same two roots.
                if {u, v} != {x, y}:
                    totals[3] += weight
    return totals


def main():
    direct_cases = [(4, 1, 2, 3, 5), (4, 2, 0, 3, 1), (5, 1, 1, 2, 3)]
    results = {"direct_original_graph_checks": [], "transfer_checks": []}
    for m, a, p, q, r in direct_cases:
        direct = direct_subset_coefficients(m, a, p, q, r)
        A, Be, Bf, C = direct
        assert Be == Bf
        transfer = transfer_coefficients(m, a, p, q, r)
        assert transfer == (A, Be, C), (direct_cases, direct, transfer)
        observed = Be * Bf - A * C
        predicted = closed_rayleigh(m, a, p, q, r)
        assert observed == predicted > 0
        row = {"m": m, "a": a, "p_q_r": [p, q, r],
               "A_Be_Bf_C": direct, "rayleigh": observed}
        results["direct_original_graph_checks"].append(row)
        print(row, flush=True)
    for m in (4, 5, 6, 7, 10, 25, 100):
        for a, p, q, r in ((1, 2, 3, 5), (2, 0, 3, 1), (Fraction(2, 3), Fraction(1, 5), 0, 7)):
            A, B, C = transfer_coefficients(m, a, p, q, r)
            assert B ** 2 - A * C == closed_rayleigh(m, a, p, q, r) > 0
            results["transfer_checks"].append({"m": m, "a": str(a), "p_q_r": [str(v) for v in (p, q, r)]})
    Path(__file__).with_name("twin_matching_core3_all_terminal_counts_results.json").write_text(json.dumps(results, indent=2) + "\n")
    print("All exact checks passed.", flush=True)


if __name__ == "__main__":
    main()
