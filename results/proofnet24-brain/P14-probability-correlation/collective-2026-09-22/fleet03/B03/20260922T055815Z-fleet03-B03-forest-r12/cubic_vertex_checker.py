#!/usr/bin/env python3
from itertools import combinations

TERMINALS = (0, 1, 2)


def forest_components(n, edges):
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for u, v in edges:
        ru, rv = find(u), find(v)
        if ru == rv:
            return None
        parent[ru] = rv
    return [find(i) for i in range(n)]


def partition_type(n, edges):
    comp = forest_components(n, edges)
    if comp is None:
        return None
    a, b, c = (comp[i] for i in TERMINALS)
    if a == b == c:
        return "C"
    if a == b != c:
        return "B12"
    if a == c != b:
        return "B13"
    if b == c != a:
        return "B23"
    return "A"


def partition_sums(n, edges, weights):
    out = {k: 0 for k in ("A", "B12", "B13", "B23", "C")}
    m = len(edges)
    for mask in range(1 << m):
        chosen = [edges[i] for i in range(m) if (mask >> i) & 1]
        p = partition_type(n, chosen)
        if p is None:
            continue
        w = 1
        for i in range(m):
            if (mask >> i) & 1:
                w *= weights[i]
        out[p] += w
    return out


def direct_gap(nH, Hedges, Hweights, g=1):
    v = nH
    edges = Hedges + [(v, 0), (v, 1), (v, 2)]
    weights = Hweights + [1, 1, g]
    m = len(edges)
    Z = Z1 = Z2 = Z12 = 0
    for mask in range(1 << m):
        chosen = [edges[i] for i in range(m) if (mask >> i) & 1]
        if forest_components(nH + 1, chosen) is None:
            continue
        w = 1
        for i in range(m):
            if (mask >> i) & 1:
                w *= weights[i]
        Z += w
        in1 = bool((mask >> (m - 3)) & 1)
        in2 = bool((mask >> (m - 2)) & 1)
        if in1:
            Z1 += w
        if in2:
            Z2 += w
        if in1 and in2:
            Z12 += w
    return Z, Z1, Z2, Z12, Z1 * Z2 - Z * Z12


def formula_unit(s):
    A, b, c, d, C = (s[k] for k in ("A", "B12", "B13", "B23", "C"))
    T = A + b + c + d + C
    Z = 8 * A + 6 * (b + c + d) + 4 * C
    Z1 = 4 * A + 2 * b + 2 * c + 3 * d + C
    Z2 = 4 * A + 2 * b + 3 * c + 2 * d + C
    Z12 = 2 * A + c + d
    gap = 4 * b * T + (c + C) * (d + C)
    return Z, Z1, Z2, Z12, gap


def weighted_gap_formula(s, g):
    A, b, c, d, C = (s[k] for k in ("A", "B12", "B13", "B23", "C"))
    T = A + b + c + d + C
    L = A * b - A * C + b * b + b * c + b * d + c * d
    return L * g * g + 2 * b * T * g + (b + C) * T, L


def run():
    # Exhaust every simple H on terminals 0,1,2 plus vertex 3.
    all_edges = list(combinations(range(4), 2))
    checked = 0
    min_gap = None
    for mask in range(1 << len(all_edges)):
        H = [all_edges[i] for i in range(len(all_edges)) if (mask >> i) & 1]
        weights = [1] * len(H)
        s = partition_sums(4, H, weights)
        d = direct_gap(4, H, weights, 1)
        f = formula_unit(s)
        assert d == f, (H, s, d, f)
        assert d[-1] >= 0
        min_gap = d[-1] if min_gap is None else min(min_gap, d[-1])
        for g in (2, 3, 5):
            dg = direct_gap(4, H, weights, g)[-1]
            fg, _ = weighted_gap_formula(s, g)
            assert dg == fg, (H, g, s, dg, fg)
        checked += 1

    # Positive-integer weighted H stress cases.
    cases = [
        ("triangle", 3, [(0, 1), (1, 2), (0, 2)], [2, 3, 5]),
        ("path_plus", 4, [(0, 3), (3, 1), (1, 2), (0, 2)], [2, 1, 3, 4]),
        ("K4", 4, list(combinations(range(4), 2)), [1, 2, 1, 3, 2, 1]),
        ("C4", 4, [(0, 3), (3, 1), (1, 2), (2, 0)], [3, 2, 5, 7]),
    ]
    rows = []
    for name, n, H, w in cases:
        s = partition_sums(n, H, w)
        d1 = direct_gap(n, H, w, 1)
        assert d1 == formula_unit(s)
        gs = []
        for g in (2, 5):
            dg = direct_gap(n, H, w, g)[-1]
            fg, L = weighted_gap_formula(s, g)
            assert dg == fg
            gs.append((g, dg, L))
        rows.append((name, s, d1, gs))

    print("PASS cubic-vertex terminal-partition identities")
    print("exhaustive_unweighted_H_on_4_vertices=", checked)
    print("minimum_unit_gap_in_exhaustive_family=", min_gap)
    print("weighted_stress_cases=", len(rows))
    for name, s, d1, gs in rows:
        print(name, "partition=", s, "unit=", d1, "weighted=", gs)


if __name__ == "__main__":
    run()
