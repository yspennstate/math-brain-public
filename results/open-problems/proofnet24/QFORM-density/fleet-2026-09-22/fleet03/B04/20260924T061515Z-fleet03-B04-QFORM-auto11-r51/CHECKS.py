from fractions import Fraction as F
import math

# Exact dense orthogonal matrix.
O = [
    [F(6,7),F(-2,7),F(-3,7)],
    [F(-2,7),F(3,7),F(-6,7)],
    [F(-3,7),F(-6,7),F(-2,7)],
]

def dot(a,b): return sum(x*y for x,y in zip(a,b))
assert all(dot(O[i],O[j]) == (1 if i==j else 0) for i in range(3) for j in range(3))
assert all(x != 0 for row in O for x in row)

eps = F(1,128)
# B=eps[[1,1/2],[1/2,-1]].
delta = -F(5,65536)
assert abs(delta) == F(5,65536)
assert eps < F(1,64)

beta = F(4096,5)
# U=2 first two rows of O, M=beta third row.
U = [[2*x for x in O[0]],[2*x for x in O[1]]]
M = [beta*x for x in O[2]]
Delta_U = (dot(U[0],U[0])*dot(U[1],U[1]) - dot(U[0],U[1])**2)
M2 = dot(M,M)
assert Delta_U == 16
assert M2 == F(16777216,25)

Wsplit = delta*delta*M2
K = Delta_U*M2
assert Wsplit == F(1,256)
assert K == F(268435456,25)
assert Delta_U >= delta*delta

# Build exact 6x6 matrix and fixed-pair overlap packet.
B = [[eps, eps*F(1,2)],[eps*F(1,2), -eps]]
N = [[2*O[0][j] for j in range(3)],
     [2*O[1][j] for j in range(3)],
     [beta*O[2][j] for j in range(3)]]
A = [[F(0) for _ in range(6)] for __ in range(6)]
for i in range(2):
    for j in range(2): A[i][j]=B[i][j]
for i in range(3):
    for j in range(3):
        A[i][3+j]=N[i][j]
        A[3+j][i]=N[i][j]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
           -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
           +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def d_rc(r,c):
    rows=[0,1,r]; cols=[0,1,c]
    return det3([[A[i][j] for j in cols] for i in rows])

outside=[2,3,4,5]
Wtotal=sum(d_rc(r,c)**2 for r in outside for c in outside if r!=c)
assert Wtotal == F(7031,702464)
assert Wtotal > F(1,144)
assert sum(d_rc(2,c)**2 for c in [3,4,5]) == Wsplit

C_E3=3*2**(5/6)
bound=C_E3*float(K)**(-1/6)
operator_bound=C_E3*2304**(1/6)
partner_coeff=C_E3*(F(4,75))**(-1/12)

# Weyl target check: pure cross has +/-2,+/-2,+/-4096/5.
# Left perturbation B has norm eps*sqrt(5)/2=sqrt(5)/256.
pert=math.sqrt(5)/256
assert 2-pert > 1

print('QFORM_B04_R51_OMEGA2_TRANSVERSE_CHECK_PASS')
print('delta=', delta)
print('Delta_U=', Delta_U)
print('Mnorm2=', M2)
print('Wsplit=', Wsplit)
print('Wtotal=', Wtotal, float(Wtotal))
print('K=', K, float(K))
print('example_density_bound=', bound)
print('operator_H2_paid_branch_bound=', operator_bound)
print('partner_double_anchor_E3_coefficient=', float(partner_coeff))
print('weyl_margin=', 2-pert)
