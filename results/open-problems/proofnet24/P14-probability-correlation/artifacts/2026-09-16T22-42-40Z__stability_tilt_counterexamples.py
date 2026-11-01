from fractions import Fraction
from itertools import combinations

F = Fraction


def det_bareiss(M):
    n = len(M)
    if n == 0:
        return 1
    A = [list(map(int, row)) for row in M]
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            for i in range(k + 1, n):
                if A[i][k] != 0:
                    A[k], A[i] = A[i], A[k]
                    sign *= -1
                    break
            else:
                return 0
        pivot = A[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                A[i][j] = (A[i][j] * pivot - A[i][k] * A[k][j]) // prev
        prev = pivot
    return sign * A[n - 1][n - 1]


def fracstr(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


# Certificate A: a positive-definite determinantal L-ensemble whose rare
# factor-two event tilt breaks the Rayleigh inequality. Items are e,f,p,q.
A = [
    [2, -1, 2, -1],
    [2, 0, -2, 0],
    [-2, 1, 2, -1],
    [0, 0, 1, -1],
]
assert det_bareiss(A) == -4
L = [[sum(A[i][k] * A[j][k] for k in range(4)) for j in range(4)] for i in range(4)]
assert L == [
    [10, 0, 0, 3],
    [0, 8, -8, -2],
    [0, -8, 10, 3],
    [3, -2, 3, 2],
]

principal = {}
for mask in range(16):
    S = [i for i in range(4) if (mask >> i) & 1]
    principal[mask] = det_bareiss([[L[i][j] for j in S] for i in S])
    assert principal[mask] >= 0

# Written in binary-string order e f p q, lexicographically 0000,...,1111.
principal_binary_order = []
for i in range(16):
    bits = f"{i:04b}"
    S = [j for j, b in enumerate(bits) if b == "1"]
    principal_binary_order.append(det_bareiss([[L[a][b] for b in S] for a in S]))
assert principal_binary_order == [
    1, 2, 10, 11,
    8, 12, 16, 16,
    10, 11, 100, 20,
    80, 48, 160, 16,
]

fields = [F(1), F(1), F(1, 3), F(1, 3)]

def dpp_stats(double_H=False):
    Z = Ze = Zf = Zef = Hmass = F(0)
    for mask, minor in principal.items():
        wt = F(minor)
        for i in range(4):
            if (mask >> i) & 1:
                wt *= fields[i]
        in_H = bool((mask >> 2) & 1 and (mask >> 3) & 1)
        if in_H:
            Hmass += wt
            if double_H:
                wt *= 2
        Z += wt
        if mask & 1:
            Ze += wt
        if mask & 2:
            Zf += wt
        if (mask & 1) and (mask & 2):
            Zef += wt
    return Z, Ze, Zf, Zef, Hmass

base = dpp_stats(False)
tilt = dpp_stats(True)
assert base == (F(677, 3), F(601, 3), F(1532, 9), F(1360, 9), F(7))
assert tilt == (F(698, 3), F(613, 3), F(1564, 9), F(1376, 9), F(7))
base_gap = base[1] * base[2] - base[0] * base[3]
tilt_gap = tilt[1] * tilt[2] - tilt[0] * tilt[3]
r = base[4] / base[0]
assert base_gap == F(4, 9)
assert r == F(21, 677)
assert r < F(1, 31)
assert tilt_gap == F(-572, 9)

print("DPP_CERTIFICATE")
print("detA=", det_bareiss(A))
print("L=", L)
print("principal_minors_binary_efpq=", principal_binary_order)
print("base=(Z,Ze,Zf,Zef,Hmass)=", tuple(fracstr(x) for x in base))
print("base_gap=", fracstr(base_gap))
print("H_probability=", fracstr(r), "<1/31")
print("factor_two_tilt=(Z,Ze,Zf,Zef,Hmass)=", tuple(fracstr(x) for x in tilt))
print("tilted_gap=", fracstr(tilt_gap))


# Certificate B: a literal GRAPHIC spanning-tree measure with a triangle
# circuit at the physical field mu=1/4 and R<3/31. The symmetric factor-4/3
# tilt of the sector using exactly two triangle edges breaks Rayleigh.
# This is a route-kill, not a counterexample to the uniform-all-forests source.
vertices = list(range(6))
edges = [
    (0, 1),
    (0, 4),
    (0, 5),
    (1, 4),
    (1, 5),
    (2, 4),
    (2, 5),
    (3, 4),
    (3, 5),
    (4, 5),
]
assert len(set(tuple(sorted(e)) for e in edges)) == len(edges)
T = {1, 2, 9}              # (0,4), (0,5), (4,5)
e_idx = 0                   # (0,1)
f_idx = 5                   # (2,4)
mu = F(1, 4)
lambda_sector = F(1, 3)     # sector multiplier 1+lambda = 4/3


def is_tree(subset):
    parent = list(range(len(vertices)))

    def find(a):
        while parent[a] != a:
            parent[a] = parent[parent[a]]
            a = parent[a]
        return a

    for j in subset:
        u, v = edges[j]
        ru, rv = find(u), find(v)
        if ru == rv:
            return False
        parent[ru] = rv
    return len(subset) == len(vertices) - 1 and len({find(v) for v in vertices}) == 1


trees = [sub for sub in combinations(range(len(edges)), len(vertices) - 1) if is_tree(sub)]
assert len(trees) == 96


def tree_stats(lam):
    Z = Ze = Zf = Zef = Kmass = F(0)
    for sub in trees:
        k = sum(j in T for j in sub)
        wt0 = mu ** k
        in_K = (k == 2)
        if in_K:
            Kmass += wt0
        wt = wt0 * (1 + lam if in_K else 1)
        Z += wt
        if e_idx in sub:
            Ze += wt
        if f_idx in sub:
            Zf += wt
        if e_idx in sub and f_idx in sub:
            Zef += wt
    return Z, Ze, Zf, Zef, Kmass

base_tree = tree_stats(F(0))
tilt_tree = tree_stats(lambda_sector)
assert base_tree == (F(105, 4), F(75, 4), F(133, 8), F(95, 8), F(9, 4))
assert tilt_tree == (F(27), F(19), F(17), F(12), F(9, 4))
tree_base_gap = base_tree[1] * base_tree[2] - base_tree[0] * base_tree[3]
tree_tilt_gap = tilt_tree[1] * tilt_tree[2] - tilt_tree[0] * tilt_tree[3]
R = base_tree[4] / base_tree[0]
assert tree_base_gap == 0
assert R == F(3, 35)
assert R < F(3, 31)
assert tree_tilt_gap == -1

print("GRAPHIC_SPANNING_TREE_CERTIFICATE")
print("vertices=", vertices)
print("edges=", edges)
print("triangle_edges=", [edges[i] for i in sorted(T)])
print("tested_pair=", (edges[e_idx], edges[f_idx]))
print("spanning_tree_count_unweighted=", len(trees))
print("mu=", fracstr(mu), "sector_multiplier=4/3")
print("base=(Z,Ze,Zf,Zef,Kmass)=", tuple(fracstr(x) for x in base_tree))
print("base_gap=", fracstr(tree_base_gap))
print("K_probability=", fracstr(R), "<3/31")
print("tilted=(Z,Ze,Zf,Zef,Kmass)=", tuple(fracstr(x) for x in tilt_tree))
print("tilted_gap=", fracstr(tree_tilt_gap))
print("P14_STABILITY_TILT_NOGO_57 PASS")
print("SCOPE: route-kill only; neither certificate is a counterexample to Grimmett's uniform-all-forests Conjecture 4.2")
