import math
import numpy as np

BETA_1_4_1_8=11.523251917996046609112364599
K_E=(3**(1/6)*math.e**(2/3)/4)*(BETA_1_4_1_8**(2/3))
C_PAIR=7*(math.pi/12)**(1/7)
C_E2=C_PAIR*K_E**(3/7)
C_OUTER=2*math.sqrt(C_E2)
print(f'BETA_1_4_1_8={BETA_1_4_1_8:.12f}')
print(f'K_E={K_E:.12f}')
print(f'C_PAIR_L3={C_PAIR:.12f}')
print(f'C_PAIR_E2={C_E2:.12f}')
print(f'C_OUTER_SQUARE_PAIR_E2={C_OUTER:.12f}')

A=np.zeros((6,6),float)
for i,j in [(0,1),(0,3),(1,5),(2,4),(3,5)]:
    A[i,j]=A[j,i]=1.0
w=np.linalg.eigvalsh(A)
print('spectrum=',np.array2string(w, precision=12))
print('rank=',np.linalg.matrix_rank(A))
assert np.allclose(w,[-2,-1,0,0,1,2],atol=1e-10)
L=[0,2,3]
R=[1,4,5]
H=A[np.ix_(L,R)]
print('cross_H=')
print(H)
assert np.allclose(H,np.eye(3))
z=H[0,0]
S_cross=H[1:,1:]-np.outer(H[1:,0],H[0,1:])/z
Delta_cross=np.linalg.det(S_cross@S_cross.T)
print('cross_only_S=')
print(S_cross)
print('cross_only_Delta2=',Delta_cross)
assert np.allclose(S_cross,np.eye(2))
assert abs(Delta_cross-1)<1e-12
P=[0,1]
Z=[2,3,4,5]
B=A[np.ix_(P,P)]
Rfull=A[np.ix_(Z,Z)]-A[np.ix_(Z,P)]@np.linalg.inv(B)@A[np.ix_(P,Z)]
S_true=Rfull[:2,2:]
Delta_true=np.linalg.det(S_true@S_true.T)
print('pair_B=')
print(B)
print('true_pair_schur_cross=')
print(S_true)
print('true_pair_schur_Delta2=',Delta_true)
assert np.allclose(S_true,np.diag([1.0,0.0]))
assert abs(Delta_true)<1e-12
print('QFORM_B06_AUTO11_CHECK_PASS')
