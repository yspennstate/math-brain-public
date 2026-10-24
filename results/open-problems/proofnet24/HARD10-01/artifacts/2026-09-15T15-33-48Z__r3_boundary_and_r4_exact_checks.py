#!/usr/bin/env python3
"""
HARD10-01 exact adversarial checks for the 2026-09-15T15:33:48Z report.

Standard library only.

Part A enumerates every full-support minimal R witness path-cover for
vertex-disjoint distinguished edges e=(0,1), f=(2,3), on n=4,...,9 vertices.
For every same-pair root pair satisfying the cross-only hypotheses of Lemma
L28 in both directions, it verifies the two boundary inversion pairs and the
two resulting distinct R forests.

Part B exhaustively analyzes every labelled graph on six vertices containing a
fixed representative adjacent or disjoint distinguished edge pair. Via subset
zeta transforms it records the exact |R|=4 distribution by number of minimal
R roots and the minimum unit-weight Rayleigh gap in each root-count stratum.

These checks support the report but are not logical dependencies of its proofs.
"""
from collections import Counter
from itertools import combinations, permutations


def edge(u, v):
    return (u, v) if u < v else (v, u)


def is_forest(n, edges):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a == b:
            return False
        if rank[a] < rank[b]:
            a, b = b, a
        parent[b] = a
        if rank[a] == rank[b]:
            rank[a] += 1
        return True

    return all(union(a, b) for a, b in edges)


def is_R(n, A, e=(0, 1), f=(2, 3)):
    A = list(A)
    return (
        is_forest(n, A)
        and is_forest(n, A + [e])
        and is_forest(n, A + [f])
        and not is_forest(n, A + [e, f])
    )


def gen_roots(n):
    internal = list(range(4, n))
    roots = {}
    pairings = [
        (0, ((0, 2), (1, 3))),
        (1, ((0, 3), (1, 2))),
    ]
    for typ, ((s1, t1), (s2, t2)) in pairings:
        for k in range(len(internal) + 1):
            for I1tuple in combinations(internal, k):
                I1 = set(I1tuple)
                I2 = [v for v in internal if v not in I1]
                for mid1 in permutations(I1tuple):
                    p1 = (s1,) + mid1 + (t1,)
                    E1 = {edge(p1[i], p1[i + 1]) for i in range(len(p1) - 1)}
                    for mid2 in permutations(I2):
                        p2 = (s2,) + mid2 + (t2,)
                        E = frozenset(
                            E1
                            | {
                                edge(p2[i], p2[i + 1])
                                for i in range(len(p2) - 1)
                            }
                        )
                        roots[E] = (typ, p1, p2)
    return roots


def cross_only(Pinfo, Q, P):
    _, X, Y = Pinfo
    side = {v: 0 for v in X}
    side.update({v: 1 for v in Y})
    return all(side[u] != side[v] for u, v in Q - P)


def cross_edges(path, side):
    return [edge(u, v) for u, v in zip(path, path[1:]) if side[u] != side[v]]


def orient_cross(h, posX, posY):
    u, v = h
    if u in posX and v in posY:
        return u, v
    if v in posX and u in posY:
        return v, u
    raise AssertionError(("not cross", h))


def segment_edges(path, i, j):
    return {edge(path[t], path[t + 1]) for t in range(i, j)}


def inversion_forest(Pinfo, h1, h2):
    _, X, Y = Pinfo
    posX = {v: i for i, v in enumerate(X)}
    posY = {v: i for i, v in enumerate(Y)}
    x1, y1 = orient_cross(h1, posX, posY)
    x2, y2 = orient_cross(h2, posX, posY)
    if not (posX[x1] < posX[x2] and posY[y2] < posY[y1]):
        x1, y1, x2, y2 = x2, y2, x1, y1
        h1, h2 = h2, h1
    assert posX[x1] < posX[x2] and posY[y2] < posY[y1]
    F = set()
    F |= segment_edges(X, 0, posX[x1])
    F.add(h1)
    F |= segment_edges(Y, posY[y1], len(Y) - 1)
    F |= segment_edges(Y, 0, posY[y2])
    F.add(h2)
    F |= segment_edges(X, posX[x2], len(X) - 1)
    return frozenset(F)


def check_boundary_inversions():
    expected = {4: 0, 5: 0, 6: 2, 7: 48, 8: 816, 9: 12480}
    for n in range(4, 10):
        roots = gen_roots(n)
        items = list(roots.items())
        tested = 0
        for i, (P, Pi) in enumerate(items):
            for Q, Qi in items[i + 1 :]:
                if Pi[0] != Qi[0]:
                    continue
                if not (cross_only(Pi, Q, P) and cross_only(Qi, P, Q)):
                    continue
                tested += 1
                _, X, Y = Pi
                side = {v: 0 for v in X}
                side.update({v: 1 for v in Y})
                A_cross = cross_edges(Qi[1], side)
                B_cross = cross_edges(Qi[2], side)
                assert len(A_cross) >= 2 and len(B_cross) >= 2
                ha, hc = A_cross[0], A_cross[-1]
                hb, hd = B_cross[0], B_cross[-1]
                posX = {v: i for i, v in enumerate(X)}
                posY = {v: i for i, v in enumerate(Y)}
                xa, ya = orient_cross(ha, posX, posY)
                xb, yb = orient_cross(hb, posX, posY)
                xd, yd = orient_cross(hd, posX, posY)
                xc, yc = orient_cross(hc, posX, posY)
                assert posX[xa] < posX[xb] and posY[yb] < posY[ya]
                assert posX[xd] < posX[xc] and posY[yc] < posY[yd]
                F1 = inversion_forest(Pi, ha, hb)
                F2 = inversion_forest(Pi, hd, hc)
                assert F1 != F2
                assert F1 not in (P, Q) and F2 not in (P, Q)
                assert is_R(n, F1) and is_R(n, F2)
        assert tested == expected[n], (n, tested, expected[n])
        print(
            f"n={n}: roots={len(roots)}, compatible same-pair pairs={tested}: PASSED"
        )


def fixed_pair_arrays(n, e, f):
    allE = list(combinations(range(n), 2))
    H = [g for g in allE if g not in (e, f)]
    m = len(H)
    N = 1 << m
    arr = {k: [0] * N for k in ("N0", "Ne", "Nf", "B", "R", "MINR")}
    rmask = [0] * N
    for mask in range(N):
        A = [H[i] for i in range(m) if (mask >> i) & 1]
        if not is_forest(n, A):
            continue
        eok = is_forest(n, A + [e])
        fok = is_forest(n, A + [f])
        efok = is_forest(n, A + [e, f])
        if not eok and not fok:
            k = "N0"
        elif eok and not fok:
            k = "Ne"
        elif fok and not eok:
            k = "Nf"
        elif efok:
            k = "B"
        else:
            k = "R"
            rmask[mask] = 1
        arr[k][mask] = 1

    for mask in range(N):
        if not rmask[mask]:
            continue
        sub = (mask - 1) & mask
        minimal = True
        while sub:
            if rmask[sub]:
                minimal = False
                break
            sub = (sub - 1) & mask
        if minimal:
            arr["MINR"][mask] = 1

    def zeta(a):
        z = a[:]
        for i in range(m):
            bit = 1 << i
            for mask in range(N):
                if mask & bit:
                    z[mask] += z[mask ^ bit]
        return z

    return H, {k: zeta(v) for k, v in arr.items()}


def r4_stats(e, f):
    H, Z = fixed_pair_arrays(6, e, f)
    rootdist = Counter()
    mingap = {}
    for M in range(1 << len(H)):
        R = Z["R"][M]
        if R != 4:
            continue
        roots = Z["MINR"][M]
        N0, Ne, Nf, B = [Z[k][M] for k in ("N0", "Ne", "Nf", "B")]
        delta = Ne * Nf + R * (Ne + Nf + B + R) - B * N0
        rootdist[roots] += 1
        mingap[roots] = min(mingap.get(roots, 10**99), delta)
    return rootdist, mingap


def check_r4():
    adj, madj = r4_stats((0, 1), (0, 2))
    dis, mdis = r4_stats((0, 1), (2, 3))
    assert adj == Counter({1: 201, 2: 99}), adj
    assert madj == {1: 32, 2: 28}, madj
    assert dis == Counter({2: 377, 1: 144, 4: 2}), dis
    assert mdis == {1: 64, 2: 24, 4: 36}, mdis
    print("n=6 |R|=4 adjacent root distribution:", dict(adj), "min gaps", madj)
    print("n=6 |R|=4 disjoint root distribution:", dict(dis), "min gaps", mdis)
    print("R4 EXACT CHECKS PASSED")


if __name__ == "__main__":
    check_boundary_inversions()
    check_r4()
    print("ALL EXACT CHECKS PASSED")
