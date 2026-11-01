#!/usr/bin/env python3
"""Exact certificate for T07 right-matching augmentation.

G_{k,r}: left side L has 3 vertices, right side R has 2k+r vertices,
all L--R edges are present, and R contains k disjoint matching edges.
The script proves the 3-terminal transfer algebra and exact positivity of
all 14 edge-pair orbit Rayleigh numerators for every admissible k,r.

All enumeration and symbolic algebra are exact integer/rational arithmetic.
"""
from collections import defaultdict
from itertools import combinations
import sympy as sp


def canon(blocks):
    return tuple(sorted((tuple(sorted(b)) for b in blocks if b),
                        key=lambda z: (z[0], len(z), z)))


def gen_parts(items):
    items = list(items)
    if not items:
        yield ()
        return
    x = items[0]
    for p in gen_parts(items[1:]):
        yield canon(((x,),) + p)
        for i in range(len(p)):
            q = [set(b) for b in p]
            q[i].add(x)
            yield canon(q)


TERMS = (0, 1, 2)
PARTS = sorted(set(gen_parts(TERMS)), key=lambda p: (-len(p), p))
IDX = {p: i for i, p in enumerate(PARTS)}
assert len(PARTS) == 5


def transfer(nv, edges, marked=()):
    """Terminal-partition transfer; marked edges are required present."""
    marked = set(marked)
    A = sp.zeros(5)
    for ri, pstate in enumerate(PARTS):
        for mask in range(1 << len(edges)):
            chosen = {j for j in range(len(edges)) if (mask >> j) & 1}
            if not marked <= chosen:
                continue
            par = list(range(nv))

            def find(x):
                while par[x] != x:
                    par[x] = par[par[x]]
                    x = par[x]
                return x

            def union(x, y):
                x, y = find(x), find(y)
                if x == y:
                    return False
                par[y] = x
                return True

            for block in pstate:
                for x in block[1:]:
                    assert union(block[0], x)
            ok = True
            for j in chosen:
                if not union(*edges[j]):
                    ok = False
                    break
            if not ok:
                continue
            blocks = defaultdict(set)
            for x in TERMS:
                blocks[find(x)].add(x)
            A[ri, IDX[canon(blocks.values())]] += 1
    return A


# O-layer: one ordinary right vertex attached to all three terminals.
SE = [(3, 0), (3, 1), (3, 2)]
S = transfer(4, SE)
O = {i: transfer(4, SE, [i]) for i in range(3)}
O2 = {(i, j): transfer(4, SE, [i, j])
      for i, j in combinations(range(3), 2)}

# M-layer: two right vertices, each attached to all three terminals,
# plus their internal matching edge h (edge index 6).
PE = [(3, 0), (3, 1), (3, 2),
      (4, 0), (4, 1), (4, 2), (3, 4)]
P = transfer(5, PE)
H = transfer(5, PE, [6])
Q = {i: transfer(5, PE, [i]) for i in range(3)}
HQ = {i: transfer(5, PE, [6, i]) for i in range(3)}
QQs = {(i, j): transfer(5, PE, [i, j])
       for i, j in combinations(range(3), 2)}
QQd = {(i, j): transfer(5, PE, [i, 3 + j])
       for i in range(3) for j in range(3)}

N = S - 4 * sp.eye(5)
assert N ** 2 != sp.zeros(5)
assert N ** 3 == sp.zeros(5)
assert P == 23 * sp.eye(5) + 12 * N + sp.Rational(5, 3) * N ** 2
assert S * P == P * S
marked_mats = (list(O.values()) + list(O2.values()) + [H] + list(Q.values())
               + list(HQ.values()) + list(QQs.values()) + list(QQd.values()))
assert all(X * S == S * X and X * P == P * X for X in marked_mats)
print("TRANSFER_ALGEBRA_PASS")
print("S=4I+N, N^3=0")
print("P=23I+12N+(5/3)N^2")
print("S=", S.tolist())
print("P=", P.tolist())

k, r = sp.symbols("k r", integer=True, nonnegative=True)
K, R = sp.symbols("K R", integer=True, nonnegative=True)


def Rkr(ke, re):
    """P^ke S^re / (23^ke 4^re), using N^3=0."""
    u = sp.Rational(12, 23) * ke + sp.Rational(1, 4) * re
    v = (sp.Rational(5, 69) * ke
         + sp.Rational(72, 529) * ke * (ke - 1)
         + sp.Rational(1, 32) * re * (re - 1)
         + sp.Rational(3, 23) * ke * re)
    return sp.eye(5) + sp.expand(u) * N + sp.expand(v) * N ** 2


d = sp.Matrix([[1, 0, 0, 0, 0]])
one = sp.ones(5, 1)
sc = lambda X: sp.factor(X[0])
Z = sc(d * Rkr(k, r) * one)
Z_expected = ((6912*k**2 + 6624*k*r + 14432*k + 1587*r**2
               + 6877*r + 8464) / sp.Integer(8464))
assert sp.simplify(Z - Z_expected) == 0
print("FOREST_COUNT_NORMALIZED_PASS:", Z)

# First derivatives, with one marked layer removed from the base-factor power.
o = {i: sc(d * O[i] * Rkr(k, r - 1) * one) for i in range(3)}
h = sc(d * H * Rkr(k - 1, r) * one)
q = {i: sc(d * Q[i] * Rkr(k - 1, r) * one) for i in range(3)}

# Second derivatives in the orbit representatives.
os = {(i, j): sc(d * O2[(i, j)] * Rkr(k, r - 1) * one)
      for i, j in O2}
od = {(i, j): sc(d * O[i] * O[j] * Rkr(k, r - 2) * one)
      for i in range(3) for j in range(3)}
hq = {i: sc(d * HQ[i] * Rkr(k - 1, r) * one) for i in range(3)}
qqs = {(i, j): sc(d * QQs[(i, j)] * Rkr(k - 1, r) * one)
       for i, j in QQs}
qqd = {(i, j): sc(d * QQd[(i, j)] * Rkr(k - 1, r) * one)
       for i in range(3) for j in range(3)}
hh = sc(d * H * H * Rkr(k - 2, r) * one)
hqd = {i: sc(d * H * Q[i] * Rkr(k - 2, r) * one) for i in range(3)}
qqx = {(i, j): sc(d * Q[i] * Q[j] * Rkr(k - 2, r) * one)
       for i in range(3) for j in range(3)}
ho = {j: sc(d * H * O[j] * Rkr(k - 1, r - 1) * one) for j in range(3)}
qo = {(i, j): sc(d * Q[i] * O[j] * Rkr(k - 1, r - 1) * one)
      for i in range(3) for j in range(3)}

# Same-layer second derivatives remove one layer, while a product of two
# first derivatives removes it twice, hence the compensating factors 4 or 23.
g = {}
g["O.same_layer.diff_terminal"] = sp.factor(o[0]*o[1] - 4*Z*os[(0, 1)])
g["O.diff_layer.same_terminal"] = sp.factor(o[0]**2 - Z*od[(0, 0)])
g["O.diff_layer.diff_terminal"] = sp.factor(o[0]*o[1] - Z*od[(0, 1)])
g["M.same_layer.h_spoke"] = sp.factor(h*q[0] - 23*Z*hq[0])
g["M.same_layer.spokes.same_vertex.diff_terminal"] = sp.factor(q[0]*q[1] - 23*Z*qqs[(0, 1)])
g["M.same_layer.spokes.diff_vertex.same_terminal"] = sp.factor(q[0]**2 - 23*Z*qqd[(0, 0)])
g["M.same_layer.spokes.diff_vertex.diff_terminal"] = sp.factor(q[0]*q[1] - 23*Z*qqd[(0, 1)])
g["M.diff_layer.h_h"] = sp.factor(h**2 - Z*hh)
g["M.diff_layer.h_spoke"] = sp.factor(h*q[0] - Z*hqd[0])
g["M.diff_layer.spokes.same_terminal"] = sp.factor(q[0]**2 - Z*qqx[(0, 0)])
g["M.diff_layer.spokes.diff_terminal"] = sp.factor(q[0]*q[1] - Z*qqx[(0, 1)])
g["mixed.h_O"] = sp.factor(h*o[0] - Z*ho[0])
g["mixed.spoke_O.same_terminal"] = sp.factor(q[0]*o[0] - Z*qo[(0, 0)])
g["mixed.spoke_O.diff_terminal"] = sp.factor(q[0]*o[1] - Z*qo[(0, 1)])

domains = {
    "O.same_layer.diff_terminal": (0, 1),
    "O.diff_layer.same_terminal": (0, 2),
    "O.diff_layer.diff_terminal": (0, 2),
    "M.same_layer.h_spoke": (1, 0),
    "M.same_layer.spokes.same_vertex.diff_terminal": (1, 0),
    "M.same_layer.spokes.diff_vertex.same_terminal": (1, 0),
    "M.same_layer.spokes.diff_vertex.diff_terminal": (1, 0),
    "M.diff_layer.h_h": (2, 0),
    "M.diff_layer.h_spoke": (2, 0),
    "M.diff_layer.spokes.same_terminal": (2, 0),
    "M.diff_layer.spokes.diff_terminal": (2, 0),
    "mixed.h_O": (1, 1),
    "mixed.spoke_O.same_terminal": (1, 1),
    "mixed.spoke_O.diff_terminal": (1, 1),
}
assert len(g) == 14
print("RAYLEIGH_ORBIT_CERTIFICATES")
for name, val in g.items():
    num, den = sp.together(val).as_numer_denom()
    ks, rs = domains[name]
    poly = sp.Poly(sp.expand(num.subs({k: K + ks, r: R + rs})), K, R)
    coeff = [c for _, c in poly.terms()]
    assert coeff and all(c > 0 for c in coeff)
    print(name, "shift", (ks, rs), "den", den,
          "terms", len(coeff), "mincoef", min(coeff))
print("ALL_14_ORBITS_POSITIVE")

# Independent direct enumeration checks for small physical graphs.
def brute(kv, rv):
    right = list(range(3, 3 + 2*kv + rv))
    edges = [(u, v) for u in range(3) for v in right]
    edges += [(right[2*j], right[2*j + 1]) for j in range(kv)]
    nv, mm = 3 + len(right), len(edges)
    Z0 = 0
    Ze = [0] * mm
    Zef = [[0] * mm for _ in range(mm)]
    for mask in range(1 << mm):
        par = list(range(nv))

        def find(x):
            while par[x] != x:
                par[x] = par[par[x]]
                x = par[x]
            return x

        chosen = []
        ok = True
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                a0, b0 = find(u), find(v)
                if a0 == b0:
                    ok = False
                    break
                par[b0] = a0
                chosen.append(i)
        if not ok:
            continue
        Z0 += 1
        for i in chosen:
            Ze[i] += 1
        for i, j in combinations(chosen, 2):
            Zef[i][j] += 1
            Zef[j][i] += 1
    mingap = None
    for i, j in combinations(range(mm), 2):
        gap = Ze[i]*Ze[j] - Z0*Zef[i][j]
        assert gap > 0
        mingap = gap if mingap is None else min(mingap, gap)
    zform = sp.Integer(23)**kv * sp.Integer(4)**rv * Z.subs({k: kv, r: rv})
    assert sp.Integer(Z0) == sp.Integer(zform)
    print("BRUTE", kv, rv, "V", nv, "E", mm, "Z", Z0, "mingap", mingap)


for pair in [(1, 1), (2, 0), (2, 1)]:
    brute(*pair)

z11 = sp.simplify(sp.Integer(23)**4 * Z.subs({k: 4, r: 0}))
print("THEOREM_INSTANCE_11V", "G_4_0", "V", 11, "E", 28, "Z", z11)
print("ALL_EXACT_CHECKS_PASS")
