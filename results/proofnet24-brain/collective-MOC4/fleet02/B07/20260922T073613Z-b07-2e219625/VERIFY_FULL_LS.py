from fractions import Fraction as F


def matmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def transpose(A):
    return [list(row) for row in zip(*A)]


def matadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))]
            for i in range(len(A))]


def mv(A, x):
    return [sum(a * b for a, b in zip(row, x)) for row in A]


def dot(x, y):
    return sum(a * b for a, b in zip(x, y))


Pdiag = [F(0), F(2), F(3), F(5)]
Ppdiag = [F(0), F(1, 2), F(1, 3), F(1, 5)]
P = [[Pdiag[i] if i == j else F(0) for j in range(4)] for i in range(4)]
Pp = [[Ppdiag[i] if i == j else F(0) for j in range(4)] for i in range(4)]
B = [
    [F(0), F(0)],
    [F(1), F(2)],
    [F(2), F(-1)],
    [F(1), F(1)],
]
Sc = [[F(7), F(0)], [F(0), F(11)]]
BtPpB = matmul(transpose(B), matmul(Pp, B))
C = matadd(BtPpB, Sc)

u = [F(0), F(1), F(-2), F(3)]
v = [F(4), F(-1)]
BTPpu = mv(transpose(B), mv(Pp, u))
r = [v[i] - BTPpu[i] for i in range(2)]

pair_reserve = dot(u, mv(Pp, u))
Scp = [[F(1, 7), F(0)], [F(0), F(1, 11)]]
cross_reserve = dot(r, mv(Scp, r))
full_reserve = pair_reserve + cross_reserve
q = F(-12)
pair_gate = q + 3 * pair_reserve
full_gate = q + 3 * full_reserve

# Exact congruence certificate A = T^T diag(P,Sc) T.
K = matmul(Pp, B)
I4 = [[F(int(i == j)) for j in range(4)] for i in range(4)]
I2 = [[F(int(i == j)) for j in range(2)] for i in range(2)]
T = [I4[i] + K[i] for i in range(4)]
T += [[F(0)] * 4 + I2[i] for i in range(2)]
D = []
for i in range(4):
    D.append(P[i] + [F(0), F(0)])
for i in range(2):
    D.append([F(0)] * 4 + Sc[i])
A_from_factor = matmul(transpose(T), matmul(D, T))
A_direct = []
for i in range(4):
    A_direct.append(P[i] + B[i])
Bt = transpose(B)
for i in range(2):
    A_direct.append(Bt[i] + C[i])

assert A_from_factor == A_direct
assert C == [[F(271, 30), F(8, 15)], [F(8, 15), F(203, 15)]]
assert r == [F(127, 30), F(-49, 15)]
assert pair_reserve == F(109, 30)
assert cross_reserve == F(27183, 7700)
assert full_reserve == F(165479, 23100)
assert full_reserve - pair_reserve == cross_reserve
assert pair_gate == F(-11, 10) and pair_gate <= 0
assert full_gate == F(73079, 7700) and full_gate > 0

print("PASS MOC4-FULL-HESSIAN-LS-CROSS-RESERVE calibration")
print("C =", C)
print("pair_reserve =", pair_reserve)
print("cross_residual =", r)
print("cross_reserve =", cross_reserve)
print("full_reserve =", full_reserve)
print("reserve_identity_error =", full_reserve - pair_reserve - cross_reserve)
print("pair_gate =", pair_gate)
print("full_gate =", full_gate)
