from fractions import Fraction as F
from math import pi, e, sqrt
import numpy as np

# Constants
C_pair = 2 + 2*pi
C_half = 8 * 2**(3/8)
C_SN = C_pair * C_half**(2/3)
C_disj = C_SN * 16**(1/12)
B20_bound = C_disj * 64**(1/12) * 144**(1/6)
assert abs(C_SN - 8*2**(1/4)*(1+pi)) < 1e-12
assert abs(C_disj - 8*2**(7/12)*(1+pi)) < 1e-12

# tiny exact rational matrix helpers
def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def mt(A):
    return [list(x) for x in zip(*A)]
def madd(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def inv2(B):
    d=B[0][0]*B[1][1]-B[0][1]*B[1][0]
    return [[B[1][1]/d,-B[0][1]/d],[-B[1][0]/d,B[0][0]/d]]

B=[[F(3),F(1,5)],[F(1,5),F(-3)]]
C=[[F(1,20),F(2,20)],[F(2,20),F(-1,20)],[F(-1,20),F(3,20)],[F(3,20),F(1,20)]]
R=[[F(1,10),F(1,20),F(3),F(1)],
   [F(1,20),F(-1,10),F(1),F(-3)],
   [F(3),F(1),F(1,20),F(-1,25)],
   [F(1),F(-3),F(-1,25),F(-1,20)]]
Binv=inv2(B)
D=madd(R,mm(mm(C,Binv),mt(C)))
A=[B[0]+mt(C)[0], B[1]+mt(C)[1]] + [C[i]+D[i] for i in range(4)]
detB=B[0][0]*B[1][1]-B[0][1]*B[1][0]
assert detB==F(-226,25)
assert all(x != 0 for row in A for x in row)

# N=det(B)R from D=R+CB^{-1}C^T.
adjB=[[B[1][1],-B[0][1]],[-B[1][0],B[0][0]]]
N1=[[detB*D[i][j] for j in range(4)] for i in range(4)]
CadjCt=mm(mm(C,adjB),mt(C))
N=[[N1[i][j]-CadjCt[i][j] for j in range(4)] for i in range(4)]
assert N==[[detB*R[i][j] for j in range(4)] for i in range(4)]
M=[[N[0][2],N[0][3]],[N[1][2],N[1][3]]]
detM=M[0][0]*M[1][1]-M[0][1]*M[1][0]
Z=detM*detM
assert detM==F(-102152,125)
assert Z==F(10435031104,15625)
example_bound=C_SN * float(Z)**(-1/12)

# Rigorous Weyl margin used in report.
m=sqrt(226)/5
delta=sqrt(F(3,40)) + 3/(8*sqrt(226))
assert m-delta > 1

# Numerical spectrum only as a redundant finite check.
Af=np.array([[float(x) for x in row] for row in A],dtype=float)
evals=np.linalg.eigvalsh(Af)
assert np.min(np.abs(evals)) > 1

print('QFORM_B04_R52_SCHUR_NUMERATOR_CHECK_PASS')
print('C_SN',repr(C_SN))
print('C_disj',repr(C_disj))
print('B20_theta_1_over_64_bound',repr(B20_bound))
print('detB',detB)
print('det_N_cross',detM)
print('Z_N',Z,float(Z))
print('example_bound',repr(example_bound))
print('weyl_margin',repr(m-delta))
print('eigvals',','.join(f'{x:.10f}' for x in evals))
