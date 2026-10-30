from fractions import Fraction as F
from itertools import permutations, combinations


def C(re=0, im=0):
    return (F(re), F(im))


def add(z, w):
    return (z[0] + w[0], z[1] + w[1])


def mul(z, w):
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def scale(q, z):
    return (q * z[0], q * z[1])


def sign(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def det(M):
    ans = C()
    for p in permutations(range(len(M))):
        t = C(1)
        for i, j in enumerate(p):
            t = mul(t, M[i][j])
        ans = add(ans, scale(F(sign(p)), t))
    return ans


U = [
    [F(636, 1105), -F(423, 1105), -F(12, 65), -F(772, 1105)],
    [F(3576, 5525), F(332, 5525), -F(144, 325), F(3411, 5525)],
    [F(164, 425), F(348, 425), F(9, 25), -F(96, 425)],
    [F(27, 85), -F(36, 85), F(4, 5), F(24, 85)],
]
a = [C(-4, 4), C(0, -1), C(-3, 2), C(-4, -4)]
b = [C(-4, -4), C(2, -1), C(2, -4), C(4, -1)]


def transpose(X):
    return [list(r) for r in zip(*X)]


def mm(A, B):
    return [
        [sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))]
        for i in range(len(A))
    ]


assert mm(U, transpose(U)) == [[F(i == j) for j in range(4)] for i in range(4)]


def physical_det(V):
    N = [[C() for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            z = C()
            for k in range(4):
                z = add(z, scale(V[i][k] * V[j][k], b[k]))
            if i == j:
                z = add(z, a[i])
            N[i][j] = z
    return det(N)


base = physical_det(U)
assert base == (F(-82603754544, 763140625), F(-3513801072, 763140625))

perms = list(permutations(range(4)))
H = {}
for s in perms:
    z = C(1)
    for i in range(4):
        z = mul(z, add(a[i], b[s[i]]))
    H[s] = z[0]

vals = sorted(H.values(), reverse=True)
M, M2 = vals[0], vals[1]
assert M == 256 and M2 == 240
assert M - M2 == 16


def trans(i, j):
    t = list(range(4))
    t[i], t[j] = t[j], t[i]
    return tuple(t)


def right(s, t):
    return tuple(s[t[i]] for i in range(4))  # s o t


def left(t, s):
    return tuple(t[s[i]] for i in range(4))  # t o s


row_gap = {}
col_gap = {}
for i, j in combinations(range(4), 2):
    t = trans(i, j)
    row_roof = max(H[s] + H[right(s, t)] for s in perms)
    col_roof = max(H[s] + H[left(t, s)] for s in perms)
    row_gap[(i, j)] = 2 * M - row_roof
    col_gap[(i, j)] = 2 * M - col_roof
    assert row_gap[(i, j)] >= M - M2 > 0
    assert col_gap[(i, j)] >= M - M2 > 0


def swap_rows(V, i, j):
    W = [r[:] for r in V]
    W[i], W[j] = W[j], W[i]
    return W


def swap_cols(V, i, j):
    W = [r[:] for r in V]
    for r in range(4):
        W[r][i], W[r][j] = W[r][j], W[r][i]
    return W


h0 = base[0]
for ij, g in row_gap.items():
    hs = physical_det(swap_rows(U, *ij))[0]
    assert h0 + hs <= 2 * M - g
for ij, g in col_gap.items():
    hs = physical_det(swap_cols(U, *ij))[0]
    assert h0 + hs <= 2 * M - g

print("PASS MOC4-PAIR-SPECIFIC-ENDPOINT-ROOF-v1")
print("top_support =", M)
print("second_support =", M2)
print("global_top_two_gap =", M - M2)
print("row_pair_gaps =", sorted(row_gap.items()))
print("column_pair_gaps =", sorted(col_gap.items()))
print("sum_row_pair_gaps =", sum(row_gap.values()))
print("sum_column_pair_gaps =", sum(col_gap.values()))
print("partner_base_support =", h0)
