from fractions import Fraction as F
from math import sqrt, pi

B = [
    [F(31,16), F(-1,16), F(1,4)],
    [F(-1,16), F(31,16), F(1,4)],
    [F(1,4), F(1,4), F(-1,1)],
]

def det2(M):
    return M[0][0]*M[1][1]-M[0][1]*M[1][0]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

tr = sum(B[i][i] for i in range(3))
e2 = (det2([[B[0][0],B[0][1]],[B[1][0],B[1][1]]])
      +det2([[B[0][0],B[0][2]],[B[2][0],B[2][2]]])
      +det2([[B[1][1],B[1][2]],[B[2][1],B[2][2]]]))
detB = det3(B)

# Expected characteristic polynomial:
# (lambda-2)(8 lambda^2 - 7 lambda - 16)/8
# = lambda^3 -(23/8)lambda^2 -(1/4)lambda + 4
# while det(lambda I-B)=lambda^3-tr(B)lambda^2+e2 lambda-det(B).
assert tr == F(23,8)
assert e2 == F(-1,4)
assert detB == F(-4,1)

# Pivot a=B_33=-1, b=(1/4,1/4), C=B[:2,:2].
a = B[2][2]
b = [B[0][2], B[1][2]]
C = [[B[0][0],B[0][1]],[B[1][0],B[1][1]]]
S = [[C[i][j]-b[i]*b[j]/a for j in range(2)] for i in range(2)]
assert S == [[F(2),F(0)],[F(0),F(2)]]
assert det2(S) == F(4)
assert detB == a*det2(S)

lam_mid = F(2)
lam_plus = (7+sqrt(561))/16
lam_minus = (7-sqrt(561))/16
assert float(lam_mid) >= 1
assert lam_plus > 1
assert lam_minus < -1

bound = 4*sqrt(pi)/(abs(float(a*detB))**0.25)
expected = 2*sqrt(2*pi)
assert abs(bound-expected) < 1e-14

print('trace=', tr)
print('e2=', e2)
print('detB=', detB)
print('Schur=', S)
print('eigenvalues=', float(lam_mid), lam_plus, lam_minus)
print('density_bound=', bound)
print('STATUS=PASS')
