#!/usr/bin/env python3
from collections import Counter
from fractions import Fraction

def is_forest(n, edges, mask):
    parent = list(range(n))
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, (u, v) in enumerate(edges):
        if (mask >> i) & 1:
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            parent[ru] = rv
    return True

def theta3_local():
    edges = []
    for w in (2, 3, 4):
        edges.extend([(0, w), (w, 1)])
    D = C = Dx = Cx = 0
    for mask in range(1 << 6):
        if not is_forest(5, edges, mask):
            continue
        connected = any(((mask >> (2*j)) & 3) == 3 for j in range(3))
        if connected:
            C += 1
            Cx += mask & 1
        else:
            D += 1
            Dx += mask & 1
    assert (D, C, Dx, Cx) == (27, 27, 9, 15)
    assert Fraction(Dx, D) == Fraction(1, 3)
    assert Fraction(Cx, C) == Fraction(5, 9)
    return D, C, Dx, Cx

def expand_theta3(n, medges):
    edges = []
    groups = []
    nxt = n
    for u, v in medges:
        inds = []
        for _ in range(3):
            w = nxt
            nxt += 1
            inds.append(len(edges)); edges.append((u, w))
            inds.append(len(edges)); edges.append((w, v))
        groups.append(inds)
    return nxt, edges, groups

def multigraph_forest_masks(n, medges):
    return [m for m in range(1 << len(medges)) if is_forest(n, medges, m)]

def original_covariance(n, medges, a, b):
    masks = multigraph_forest_masks(n, medges)
    Z = len(masks)
    Za = sum((m >> a) & 1 for m in masks)
    Zb = sum((m >> b) & 1 for m in masks)
    Zab = sum(((m >> a) & 1) * ((m >> b) & 1) for m in masks)
    return Fraction(Zab, Z) - Fraction(Za, Z) * Fraction(Zb, Z), (Z, Za, Zb, Zab)

def expanded_projection_and_cov(n, medges, a, b):
    N, edges, groups = expand_theta3(n, medges)
    xa = groups[a][0]
    yb = groups[b][0]
    projection = Counter()
    Z = Zx = Zy = Zxy = 0
    for mask in range(1 << len(edges)):
        if not is_forest(N, edges, mask):
            continue
        Z += 1
        x = (mask >> xa) & 1
        y = (mask >> yb) & 1
        Zx += x
        Zy += y
        Zxy += x*y
        pmask = 0
        for gi, inds in enumerate(groups):
            connected = any(
                ((mask >> inds[2*j]) & 1) and ((mask >> inds[2*j+1]) & 1)
                for j in range(3)
            )
            if connected:
                pmask |= 1 << gi
        projection[pmask] += 1
    cov = Fraction(Zxy, Z) - Fraction(Zx, Z) * Fraction(Zy, Z)
    return cov, (Z, Zx, Zy, Zxy), projection

def check_case(name, n, medges, a, b, expected_cov):
    cov_m, counts_m = original_covariance(n, medges, a, b)
    assert cov_m == expected_cov
    cov_s, counts_s, projection = expanded_projection_and_cov(n, medges, a, b)
    forest_masks = multigraph_forest_masks(n, medges)
    lift = 27 ** len(medges)
    assert set(projection) == set(forest_masks)
    assert set(projection.values()) == {lift}
    assert counts_s[0] == counts_m[0] * lift
    assert cov_s == Fraction(4, 81) * cov_m
    print(name)
    print("  original_counts", counts_m)
    print("  original_cov", cov_m)
    print("  expanded_counts", counts_s)
    print("  expanded_cov", cov_s)
    print("  exact_scale", Fraction(4, 81))
    print("  lift_per_original_forest", lift)

def main():
    D, C, Dx, Cx = theta3_local()
    print("theta3_local", {"D": D, "C": C, "Dx": Dx, "Cx": Cx})
    print("conditional_edge_probs", Fraction(Dx, D), Fraction(Cx, C))
    check_case("triangle_nonparallel_pair", 3, [(0,1), (1,2), (2,0)], 0, 1, Fraction(-2, 49))
    check_case("parallel_pair_with_tail", 3, [(0,1), (0,1), (1,2)], 0, 1, Fraction(-1, 9))
    print("THETA3_SIMULATION_PASS")

if __name__ == "__main__":
    main()
