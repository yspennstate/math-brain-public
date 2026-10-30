#!/usr/bin/env python3
"""Exact regression checks for the POS3 endpoint critical-swap residual theorem.

No external packages.  The checks are finite regression evidence only; the theorem
is proved symbolically in REPORT.md.
"""
from itertools import permutations, combinations

def closure(vertices, generators):
    rel = set(generators)
    changed = True
    while changed:
        changed = False
        for a, b in list(rel):
            for c, d in list(rel):
                if b == c and a != d and (a, d) not in rel:
                    rel.add((a, d))
                    changed = True
    return rel

def extensions(vertices, generators):
    rel = closure(vertices, generators)
    out = []
    for p in permutations(vertices):
        pos = {v: i for i, v in enumerate(p)}
        if all(pos[a] < pos[b] for a, b in rel):
            out.append(p)
    return rel, out

def incomparable(a, b, rel):
    return (a, b) not in rel and (b, a) not in rel

def minimal_subset(S, rel):
    return {s for s in S
            if not any(t != s and (t, s) in rel for t in S)}

def width(vertices, rel):
    ans = 0
    for r in range(1, len(vertices) + 1):
        for S in combinations(vertices, r):
            if all(incomparable(a, b, rel) for a, b in combinations(S, 2)):
                ans = max(ans, r)
    return ans

def analyze(name, vertices, generators, x, y, blockers, C):
    rel, ex = extensions(vertices, generators)
    E = len(ex)
    assert width(vertices, rel) <= 3

    A = [L for L in ex if all(L.index(y) < L.index(s) for s in blockers)]
    B = [L for L in ex if L.index(y) < L.index(x)]
    assert all(L in A for L in B)

    aug = set(generators) | {(y, s) for s in blockers}
    relp, exp = extensions(vertices, aug)
    assert set(exp) == set(A)

    pred = lambda a: {z for z in vertices if (z, a) in relp}
    succ = lambda a: {z for z in vertices if (a, z) in relp}
    assert pred(y) <= pred(x)
    assert succ(x) <= succ(y)

    source = [L for L in exp if L.index(x) < L.index(y)]
    target = [L for L in exp if L.index(y) < L.index(x)]

    image = set()
    for L in source:
        M = list(L)
        ix, iy = M.index(x), M.index(y)
        M[ix], M[iy] = M[iy], M[ix]
        T = tuple(M)
        assert T in target
        image.add(T)
    assert len(image) == len(source)

    unmatched = set(target) - image
    R = 2 * len(B) - len(A)
    assert R == len(unmatched)

    lam = 0
    for j, c in enumerate(C, 1):
        if (c, y) in rel:
            lam = j
    assert C[-1] == x
    left = set()
    if len(C) >= 2 and lam <= len(C) - 2:
        cprev = C[-2]
        left = {L for L in exp
                if L.index(y) < L.index(cprev) < L.index(x)}

    Syx = {u for u in vertices if (y, u) in rel and incomparable(x, u, rel)}
    T = minimal_subset(Syx, rel)
    assert len(T) <= 2
    right = set()
    for t in T:
        right |= {L for L in exp if L.index(y) < L.index(t) < L.index(x)}

    assert unmatched == left | right

    return {
        "name": name,
        "E": E,
        "Q": len(A),
        "B": len(B),
        "R": R,
        "Q_x_before_y": len(source),
        "Q_y_before_x": len(target),
        "lambda_y": lam,
        "right_blockers": sorted(T, key=str),
        "left_obstruction_count": len(left),
        "right_obstruction_union_count": len(right),
    }

cases = []

v = [0, 1, 2, 3, 4, 5, 6]
g = {(0,2),(0,3),(0,4),(0,5),(0,6),
     (1,2),(1,5),(2,5),(4,5),(4,6)}
cases.append(analyze("source_bound_79", v, g, 0, 1, {3,4}, [0]))

v = ["c","x","y","s1","s2"]
g = {("c","x"),("x","s1"),("x","s2")}
cases.append(analyze("left_obstruction", v, g, "x", "y", {"s1","s2"}, ["c","x"]))

v = ["x","y","s1","s2","t"]
g = {("x","s1"),("x","s2"),("y","t")}
cases.append(analyze("right_obstruction", v, g, "x", "y", {"s1","s2"}, ["x"]))

for c in cases:
    print(c)
print("POS3_ENDPOINT_CRITICAL_SWAP_RESIDUAL_PASS")
