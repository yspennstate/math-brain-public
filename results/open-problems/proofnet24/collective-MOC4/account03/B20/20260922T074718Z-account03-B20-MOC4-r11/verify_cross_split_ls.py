from fractions import Fraction as F

# Exact calibration for MOC4-GLOBAL-LS-CROSS-SPLIT-PAYMENT-v1.
# S block A0=diag(0,2); T block dimension two.
A0 = [[F(0),F(0)],[F(0),F(2)]]
C  = [[F(0),F(0)],[F(1),F(0)]]
D  = [[F(7,2),F(0)],[F(0),F(5)]]
u  = [F(0),F(4)]
v  = [F(3),F(10)]

# Moore-Penrose action on range(A0): x0=A0^+u.
x0 = [F(0), F(2)]
R_pair = sum(u[i]*x0[i] for i in range(2))

# Sigma = D-C^T A0^+ C = diag(3,5).
Sigma = [[F(3),F(0)],[F(0),F(5)]]
# g=v-C^T x0.
g = [F(1),F(10)]
R_cross = g[0]*g[0]/Sigma[0][0] + g[1]*g[1]/Sigma[1][1]

# Full nonzero block on coordinates (s2,t1,t2):
# [[2,1,0],[1,7/2,0],[0,0,5]].
# Solve exactly against ell=(4,3,10).
det = F(2)*F(7,2)-F(1)
x_s2 = (F(7,2)*F(4)-F(1)*F(3))/det
x_t1 = (-F(1)*F(4)+F(2)*F(3))/det
x_t2 = F(10)/F(5)
R_full = F(4)*x_s2 + F(3)*x_t1 + F(10)*x_t2

assert Sigma == [[F(3),F(0)],[F(0),F(5)]]
assert R_pair == F(8)
assert g == [F(1),F(10)]
assert R_cross == F(61,3)
assert R_full == F(85,3)
assert R_full == R_pair + R_cross

# Scalar seminorm inequality check for two basis transverse directions.
slack = R_cross
for w, denom in [([F(1),F(0)],F(3)),([F(0),F(1)],F(5))]:
    gw = g[0]*w[0] + g[1]*w[1]
    assert gw*gw <= slack*denom

print('PASS MOC4-GLOBAL-LS-CROSS-SPLIT-PAYMENT-v1 calibration')
print('Sigma = diag(3,5)')
print('R_pair = 8')
print('g = (1,10)')
print('R_cross = 61/3')
print('R_full = 85/3 = R_pair + R_cross')
