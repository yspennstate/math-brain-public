from sympy import Matrix, eye, zeros, sqrt, diag, simplify
from itertools import combinations
from math import e

# 1. Exact half-cut identity.
Lam = diag(1,2,-3)
D = Matrix([[2,1,0],[1,-1,2],[0,2,1]])
I3 = eye(3)
R = Matrix.vstack(I3/sqrt(2), I3/sqrt(2))
C = Matrix.vstack(
    Matrix.hstack(D/2, -D/2),
    Matrix.hstack(-D/2, D/2)
)
A = R*Lam*R.T + C
assert simplify(R.T*R-eye(3)) == zeros(3)
assert simplify(A*R-R*Lam) == zeros(6,3)
S = A[:3,:3]
T = A[:3,3:6]
V = A[3:6,3:6]
assert simplify(S+T-Lam) == zeros(3)
assert simplify(V-S) == zeros(3)

# 2. Exact curvature-budget witness: normalized cross T0=diag(1,0,0).
T0 = diag(1,0,0)
D0 = Lam - 2*T0
C0 = Matrix.vstack(
    Matrix.hstack(D0/2, -D0/2),
    Matrix.hstack(-D0/2, D0/2)
)
A0 = R*Lam*R.T + C0
S0 = A0[:3,:3]
Tcheck = A0[:3,3:6]
assert Tcheck == T0
assert S0 == Lam-T0
assert sorted([abs(x) for x in S0.diagonal()], reverse=True)[1] >= 3/4

# 3. Two-row Cauchy--Binet aggregate.
M = Matrix([[1,2,0,1],[0,1,2,-1]])
lhs = (M*M.T).det()
rhs = 0
for r,s in combinations(range(M.cols),2):
    rhs += M[:,[r,s]].det()**2
assert lhs == rhs

# 4. Partner scalar-orthogonal control A=[[0,I_16],[I_16,0]].
m=16
delta = 3/(2*m)
threshold = 1/(6*(3/2)**0.5)
assert delta < threshold
partner_bound = e*(2**0.5)/4 * m/(m-4)
assert abs(partner_bound - e*(2**0.5)/3) < 1e-14

print('HALF_CUT_IDENTITY=PASS')
print('CURVATURE_BUDGET_EXACT_WITNESS=PASS')
print('TWO_ROW_CAUCHY_BINET=PASS', lhs)
print('DIFFUSE_DELTA=', delta)
print('FLOATING_THRESHOLD=', threshold)
print('PARTNER_ORTHOGONAL_CROSSBLOCK_BOUND=', partner_bound)
print('QFORM_B08_R17_CHECK_PASS')
