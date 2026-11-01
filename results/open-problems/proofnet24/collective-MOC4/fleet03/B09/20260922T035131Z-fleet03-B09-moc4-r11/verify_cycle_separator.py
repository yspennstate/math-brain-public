from fractions import Fraction as F
from itertools import permutations, product


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matmul(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(len(B))), F(0))
             for j in range(len(B[0]))] for i in range(len(A))]


def perm_sign(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def det(A):
    ans = F(0)
    for p in permutations(range(len(A))):
        z = F(perm_sign(p))
        for i in range(len(A)):
            z *= A[i][p[i]]
        ans += z
    return ans


def givens(n, a, b, c, s):
    G = eye(n)
    G[a][a] = c
    G[a][b] = -s
    G[b][a] = s
    G[b][b] = c
    return G


def block(A, i, j):
    return [[A[2 * i + r][2 * j + c] for c in range(2)] for r in range(2)]


G26 = givens(6, 1, 5, F(7, 25), F(24, 25))
G46 = givens(6, 3, 5, F(20, 29), F(21, 29))
O = matmul(G46, G26)

assert matmul(transpose(O), O) == eye(6)
assert det(O) == 1

t = [[F(0) for _ in range(3)] for _ in range(3)]
y = [[F(0) for _ in range(3)] for _ in range(3)]
qp = [[F(0) for _ in range(3)] for _ in range(3)]
qm = [[F(0) for _ in range(3)] for _ in range(3)]
for i in range(3):
    for j in range(3):
        B = block(O, i, j)
        t[i][j] = sum((z * z for row in B for z in row), F(0)) / 2
        y[i][j] = B[0][0] * B[1][1] - B[0][1] * B[1][0]
        qp[i][j] = (t[i][j] + y[i][j]) / 2
        qm[i][j] = (t[i][j] - y[i][j]) / 2
        assert qp[i][j] >= 0 and qm[i][j] >= 0

assert all(sum(t[i], F(0)) == 1 for i in range(3))
assert all(sum((t[i][j] for i in range(3)), F(0)) == 1 for j in range(3))

expected_t = [
    [F(337, 625), 0, F(288, 625)],
    [F(127008, 525625), F(1241, 1682), F(21609, 1051250)],
    [F(4608, 21025), F(441, 1682), F(21809, 42050)],
]
expected_y = [
    [F(7, 25), 0, 0],
    [0, F(20, 29), 0],
    [0, 0, F(28, 145)],
]
assert t == [[F(z) for z in row] for row in expected_t]
assert y == [[F(z) for z in row] for row in expected_y]

# Previous B09 family: all 16 odd checkerboard channel-mass inequalities.
twists = []
for r1, r2 in product((1, -1), repeat=2):
    r = (1, r1, r2)
    for c in product((1, -1), repeat=3):
        if r[0] * r[1] * r[2] * c[0] * c[1] * c[2] == -1:
            S = tuple(tuple(r[i] * c[j] for j in range(3)) for i in range(3))
            if S not in twists:
                twists.append(S)
assert len(twists) == 16


def twist_mass(S):
    return sum((qp[i][j] if S[i][j] == 1 else qm[i][j])
               for i in range(3) for j in range(3))


masses = [twist_mass(S) for S in twists]
assert max(masses) == F(1369, 725)
assert max(masses) < 2

# The 24 even signed matching endpoints.
S3 = list(permutations(range(3)))
even_signs = [e for e in product((1, -1), repeat=3) if e[0] * e[1] * e[2] == 1]
endpoints = []
for rho in S3:
    for eps in even_signs:
        tt = [[F(0) for _ in range(3)] for _ in range(3)]
        yy = [[F(0) for _ in range(3)] for _ in range(3)]
        for i in range(3):
            tt[i][rho[i]] = 1
            yy[i][rho[i]] = eps[i]
        endpoints.append((tt, yy))
assert len(endpoints) == 24


def cycle_cut(tt, yy, pi, s, tau):
    diag = 3 * sum((F(s[i]) * yy[i][pi[i]] for i in range(3)), F(0))
    cw = sum((tt[i][pi[(i - 1) % 3]] for i in range(3)), F(0))
    ccw = sum((tt[i][pi[(i + 1) % 3]] for i in range(3)), F(0))
    return diag + tau * (cw - ccw)


odd_signs = [s for s in product((1, -1), repeat=3) if s[0] * s[1] * s[2] == -1]
family = []
for pi in S3:
    for s in odd_signs:
        for tau in (1, -1):
            vals = [cycle_cut(tt, yy, pi, s, tau) for tt, yy in endpoints]
            assert max(vals) == 3
            family.append((pi, s, tau))
assert len(family) == 48

pi = (0, 1, 2)
s = (1, 1, -1)
tau = 1
witness_value = cycle_cut(t, y, pi, s, tau)
assert witness_value == F(1605549, 525625)
assert witness_value - 3 == F(28674, 525625) > 0

print("PASS")
print("det_O =", det(O))
print("max_odd_twist_mass =", max(masses))
print("cycle_family_count =", len(family))
print("cycle_endpoint_max =", 3)
print("witness_cycle_value =", witness_value)
print("witness_excess =", witness_value - 3)
