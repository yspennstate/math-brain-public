#!/usr/bin/env python3
from itertools import permutations, combinations
import sympy as sp

PAIR_CLASSES = [
    {frozenset((0, 1)), frozenset((2, 3))},
    {frozenset((0, 2)), frozenset((1, 3))},
    {frozenset((0, 3)), frozenset((1, 2))},
]
PERMS4 = list(permutations(range(4)))
SUBS2 = list(combinations(range(4), 2))


def quotient_perm(p):
    out = []
    for cls in PAIR_CLASSES:
        image = {frozenset(p[i] for i in pair) for pair in cls}
        out.append(next(j for j, c in enumerate(PAIR_CLASSES) if image == c))
    return tuple(out)


Q_A = {(0, 2, 1), (1, 0, 2)}
Q_B = {(1, 2, 0), (2, 0, 1)}

z = sp.symbols("z", nonzero=True)
a = sp.symbols("a0:4")
b = sp.symbols("b0:4")
U = sp.Matrix([
    [1, 1, 1, 1],
    [1, z, -1, -z],
    [1, -1, 1, -1],
    [1, -z, -1, z],
]) / 2
Ustar = U.subs(z, 1 / z).T
Da = sp.diag(*a)
Db = sp.diag(*b)
D = sp.expand((Da + U * Db * Ustar).det())
c = (z + 1 / z) / 2

endpoint = {}
for p in PERMS4:
    t = sp.Integer(1)
    for i in range(4):
        t *= a[i] + b[p[i]]
    endpoint[p] = sp.expand(t)

lift = sp.Integer(0)
for p in PERMS4:
    q = quotient_perm(p)
    if q in Q_A:
        w = (1 - c) / 16
    elif q in Q_B:
        w = (1 + c) / 16
    else:
        w = 0
    lift += w * endpoint[p]

assert sp.simplify(sp.together(D - lift)) == 0

for i in range(4):
    for j in range(4):
        marg = sp.Integer(0)
        for p in PERMS4:
            q = quotient_perm(p)
            w = (1 - c) / 16 if q in Q_A else ((1 + c) / 16 if q in Q_B else 0)
            if p[i] == j:
                marg += w
        assert sp.simplify(marg - sp.Rational(1, 4)) == 0

for S in SUBS2:
    for T in SUBS2:
        marg = sp.Integer(0)
        TT = frozenset(T)
        for p in PERMS4:
            q = quotient_perm(p)
            w = (1 - c) / 16 if q in Q_A else ((1 + c) / 16 if q in Q_B else 0)
            if frozenset(p[i] for i in S) == TT:
                marg += w
        m = sp.expand(U.extract(S, T).det())
        mbar = sp.expand(m.subs(z, 1 / z))
        qtrue = sp.simplify(m * mbar)
        assert sp.simplify(marg - qtrue) == 0

aa = [-4 + 4 * sp.I, -sp.I, -3 + 2 * sp.I, -4 - 4 * sp.I]
bb = [-4 - 4 * sp.I, 2 - sp.I, 2 - 4 * sp.I, 4 - sp.I]


def det_at(zz):
    Uz = U.subs(z, zz)
    return sp.expand((sp.diag(*aa) + Uz * sp.diag(*bb) * Uz.conjugate().T).det())


D1 = det_at(1)
Di = det_at(sp.I)
Dm1 = det_at(-1)
assert D1 == -194 + sp.Rational(491, 4) * sp.I
assert Di == -209 + sp.Rational(521, 4) * sp.I
assert Dm1 == -224 + sp.Rational(551, 4) * sp.I
assert D1 != Di

Z = []
for p in PERMS4:
    t = sp.Integer(1)
    for i in range(4):
        t *= aa[i] + bb[p[i]]
    Z.append(sp.expand(t))
assert len(set(map(str, Z))) == 24

V0 = 80 - 240 * sp.I
V1 = 64 + 256 * sp.I
V2 = -280 + 120 * sp.I
assert V0 in Z and V1 in Z and V2 in Z

cc = sp.symbols("c", real=True)
w0 = sp.Rational(613, 17280) + sp.Rational(462, 17280) * cc
w1 = sp.Rational(65, 384) + sp.Rational(6, 384) * cc
w2 = sp.Rational(6871, 8640) - sp.Rational(366, 8640) * cc
Dline = -209 + sp.Rational(521, 4) * sp.I + cc * (15 - sp.Rational(15, 2) * sp.I)
assert sp.simplify(w0 + w1 + w2 - 1) == 0
assert sp.simplify(w0 * V0 + w1 * V1 + w2 * V2 - Dline) == 0
for w in (w0, w1, w2):
    assert sp.simplify(w.subs(cc, -1)) > 0
    assert sp.simplify(w.subs(cc, 1)) > 0

print("PASS MOC4-HADAMARD-FIBER-LIFT-v1")
print("universal_symbolic_identity = PASS")
print("level1_and_level2_common_permutation_marginals = PASS")
print("active_S4_fibers = (12),(23),(123),(132) in the S4/V4 ~= S3 quotient")
print("weights_per_endpoint = (1-c)/16 on two transposition fibers; (1+c)/16 on two 3-cycle fibers")
print("concrete_D(1) =", D1)
print("concrete_D(i) =", Di)
print("concrete_D(-1) =", Dm1)
print("P_only_full_lift_same_coefficients = REFUTED by D(1) != D(i) at identical P=J/4")
print("triangle_weights(c) =", sp.factor(w0), sp.factor(w1), sp.factor(w2))
