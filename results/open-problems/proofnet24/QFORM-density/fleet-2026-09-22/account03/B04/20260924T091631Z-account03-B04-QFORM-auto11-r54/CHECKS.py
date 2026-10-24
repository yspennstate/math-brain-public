from fractions import Fraction as F
from math import e, sqrt

# Constants in REPORT.md
C_E2 = 8*sqrt(e/2)
heavy = 8*(2**(1/8))
overlap = 128*sqrt(2*e)*(3**0.25)
assert heavy < C_E2
assert abs(C_E2 - 9.326575926388497) < 1e-12
assert abs(overlap - 392.782854609543) < 1e-9

# Stress matrix data.
v = [F(1,100), F(1,50), F(3,100), F(1,25)]
M = [[F(5,2),F(1,2)],[F(1,2),F(5,2)]]
detM = M[0][0]*M[1][1]-M[0][1]*M[1][0]
assert detM == 6
Z2 = detM*detM
assert Z2 == 36
anchor = F(2,1)
F_anchor = anchor*anchor*Z2
assert F_anchor == 144

def outer(a,b):
    return [[x*y for y in b] for x in a]

S = [[F(0) for _ in range(4)] for _ in range(4)]
for i in range(2):
    for j in range(2):
        S[i][j+2]=M[i][j]
        S[j+2][i]=M[i][j]
vv = outer(v,v)
D = [[S[i][j]+vv[i][j]/2 for j in range(4)] for i in range(4)]
A = [[F(0) for _ in range(5)] for _ in range(5)]
A[0][0]=anchor
for i in range(4):
    A[0][i+1]=v[i]
    A[i+1][0]=v[i]
for i in range(4):
    for j in range(4):
        A[i+1][j+1]=D[i][j]
assert all(A[i][j] != 0 for i in range(5) for j in range(5))

# Exact scalar Schur complement is S.
for i in range(4):
    for j in range(4):
        assert A[i+1][j+1] - A[i+1][0]*A[0][j+1]/A[0][0] == S[i][j]

# Rigorous perturbation margin used in the report.
pert_bound = sqrt(30)/100 + 3/2000
assert pert_bound < 0.057
assert 2-pert_bound > 1.943

test_bound = C_E2*(2**(-1/4))*(144**(-1/8))
assert abs(test_bound - 4.213756346951995) < 1e-12

print('QFORM_B04_R54_E2_HALFRIESZ_CHECK_PASS')
print('C_E2', C_E2)
print('heavy_constant', heavy)
print('overlap_one_2^-16_bound', overlap)
print('stress_detM', detM, 'stress_Z2', Z2, 'stress_F', F_anchor)
print('stress_perturbation_bound', pert_bound)
print('stress_density_bound', test_bound)
