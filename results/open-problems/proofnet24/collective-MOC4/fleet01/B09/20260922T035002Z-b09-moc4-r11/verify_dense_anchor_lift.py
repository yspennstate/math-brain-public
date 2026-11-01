from fractions import Fraction as F
from itertools import permutations
from collections import Counter
from math import prod


def parity(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def det_frac(A):
    n = len(A)
    return sum(F(parity(p)) * prod(A[i][p[i]] for i in range(n))
               for p in permutations(range(n)))


def g(re=0, im=0):
    return (F(re), F(im))


def gadd(z, w):
    return (z[0] + w[0], z[1] + w[1])


def gsub(z, w):
    return (z[0] - w[0], z[1] - w[1])


def gmul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def gscale(a, z):
    return (a * z[0], a * z[1])


def gsum(xs):
    out = g()
    for z in xs:
        out = gadd(out, z)
    return out


def gprod(xs):
    out = g(1, 0)
    for z in xs:
        out = gmul(out, z)
    return out


def gdet(A):
    n = len(A)
    out = g()
    for p in permutations(range(n)):
        t = gprod([A[i][p[i]] for i in range(n)])
        out = gadd(out, gscale(parity(p), t))
    return out


def det_derivative(X, dX):
    n = len(X)
    out = g()
    for p in permutations(range(n)):
        s = parity(p)
        for r in range(n):
            factors = [dX[r][p[r]]] + [X[i][p[i]] for i in range(n) if i != r]
            out = gadd(out, gscale(s, gprod(factors)))
    return out


U = [
    [F(-656, 21025), F(2433, 3625), F(2688, 4205), F(-1356, 3625)],
    [F(-5856, 47125), F(-192, 325), F(35733, 47125), F(16, 65)],
    [F(35733, 47125), F(16, 65), F(5856, 47125), F(192, 325)],
    [F(2688, 4205), F(-1356, 3625), F(656, 21025), F(-2433, 3625)],
]

for i in range(4):
    for j in range(4):
        s = sum(U[i][k] * U[j][k] for k in range(4))
        assert s == F(int(i == j))
assert det_frac(U) == -1
assert all(U[i][j] != 0 for i in range(4) for j in range(4))
minors = []
for i in range(4):
    for k in range(i + 1, 4):
        for j in range(4):
            for l in range(j + 1, 4):
                m = U[i][j] * U[k][l] - U[i][l] * U[k][j]
                minors.append(m)
assert len(minors) == 36 and all(m != 0 for m in minors)

cost = {
    (1, 1): 0, (1, 2): 2, (1, 3): 1,
    (2, 1): 1, (2, 2): 0, (2, 3): 2,
    (3, 1): 2, (3, 2): 1, (3, 3): 0,
}
pointwise = []
for p in permutations(range(4)):
    ell = (int(p[1] == 3) + int(p[2] == 1) + int(p[3] == 2)
           - int(p[1] == 2) - int(p[2] == 3) - int(p[3] == 1))
    anchor = 0
    for i in range(1, 4):
        for j in range(1, 4):
            if {p[0], p[i]} == {0, j}:
                anchor += cost[i, j]
    pointwise.append(ell + anchor)
assert min(pointwise) >= 0
assert Counter(pointwise) == Counter({0: 13, 3: 10, 6: 1})

P = [[x * x for x in row] for row in U]


def minor2(i, k, j, l):
    return U[i][j] * U[k][l] - U[i][l] * U[k][j]


Q = {(i, j): minor2(0, i, 0, j) ** 2 for i in range(1, 4) for j in range(1, 4)}
singleton = P[1][3] + P[2][1] + P[3][2] - P[1][2] - P[2][3] - P[3][1]
anchor_cost = sum(F(cost[i, j]) * Q[i, j] for i in range(1, 4) for j in range(1, 4))
lift_gap = singleton + anchor_cost
assert singleton == F(-1758848358993, 1867663890625)
assert anchor_cost == F(1088931150054849, 1167289931640625)
assert lift_gap == F(-10349074315776, 1167289931640625)
assert lift_gap < 0

a = [g(-4, 4), g(0, -1), g(-3, 2), g(-4, -4)]
b = [g(-4, -4), g(2, -1), g(2, -4), g(4, -1)]
assert len(set(a)) == 4 and len(set(b)) == 4
assert all(z[1] != 0 for z in a + b)

X = []
for i in range(4):
    row = []
    for j in range(4):
        z = gsum([gscale(U[i][k] * U[j][k], b[k]) for k in range(4)])
        if i == j:
            z = gadd(z, a[i])
        row.append(z)
    X.append(row)

D = gdet(X)
D_expected = (F(-339555707994799046, 2244788330078125),
              F(1180709302197143977, 29182248291015625))
assert D == D_expected


def target(p):
    return gprod([gadd(a[i], b[p[i]]) for i in range(4)])


verts = {p: target(p) for p in permutations(range(4))}
assert len(set(verts.values())) == 24
p1, p2, p3 = (0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3)
z1, z2, z3 = verts[p1], verts[p2], verts[p3]
assert z1 == g(80, -240)
assert z2 == g(64, 256)
assert z3 == g(-280, 120)

w1 = F(54558530528515739941, 210112187695312500000)
w2 = F(478548274942418793, 4669159726562500000)
w3 = F(67009492397193957187, 105056093847656250000)
assert min(w1, w2, w3) > 0 and w1 + w2 + w3 == 1
cert = gsum([gscale(w1, z1), gscale(w2, z2), gscale(w3, z3)])
assert cert == D
area2 = ((z2[0] - z1[0]) * (z3[1] - z1[1])
         - (z2[1] - z1[1]) * (z3[0] - z1[0]))
assert area2 == 172800

# Direct application of fleet02/B07 MOC4-BIRAYLEIGH-ORBIT-v1.
p, q = 0, 3
C = [[g() for _ in range(4)] for __ in range(4)]
C[p][q] = gsub(b[q], b[p])
C[q][p] = gsub(b[q], b[p])
dX = []
for i in range(4):
    row = []
    for j in range(4):
        row.append(gsum([gscale(U[i][r] * U[j][s], C[r][s])
                         for r in range(4) for s in range(4)]))
    dX.append(row)
dD = det_derivative(X, dX)
assert dD[0] == F(3697747106152704, 6939892578125)
assert dD[0] != 0

print("PASS MOC4-DENSE-ANCHOR-MARGINAL-LIFT-v1")
print("det(U) =", det_frac(U), "all_entries_nonzero =", True, "all_2x2_minors_nonzero =", True)
print("pointwise_values =", dict(sorted(Counter(pointwise).items())))
print("singleton_part =", singleton)
print("anchor_cost_part =", anchor_cost)
print("projected_lift_gap =", lift_gap)
print("det(A+B) =", D)
print("hull_triangle =", z1, z2, z3)
print("barycentric_weights =", w1, w2, w3, "area2 =", area2)
print("eta1_pair03_derivative_real =", dD[0])
