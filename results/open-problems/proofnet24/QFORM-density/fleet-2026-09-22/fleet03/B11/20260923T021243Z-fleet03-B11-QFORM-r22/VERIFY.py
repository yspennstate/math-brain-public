#!/usr/bin/env python3
import math

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

I3=[[1,0,0],[0,1,0],[0,0,1]]
H0=[[0,0,1],[0,1,0],[1,0,0]]
assert matmul(H0,H0)==I3
assert sum(H0[i][i] for i in range(3))==1
assert det3(H0)==-1

pi_sqrt2=math.pi*math.sqrt(2)
minor_const=8*math.sqrt(math.pi*math.e)
partner=3*2**(2/3)
pair_quarter=4*(9.2+math.log(2500))
rotpair=9.2+math.log(10000)

print('H0_square_I', matmul(H0,H0))
print('H0_trace', 1, 'H0_det', -1)
print('pi_sqrt2', f'{pi_sqrt2:.15f}')
print('8sqrt(pi e)', f'{minor_const:.15f}')
print('partner_null', f'{partner:.15f}')
print('pair_eta_1_4', f'{pair_quarter:.15f}')
print('rotated_pair_D1', f'{rotpair:.15f}')

s=math.sqrt(3)/2
A=[[0.5,0,-s],[0,1,0],[-s,0,-0.5]]
A2=matmul(A,A)
assert max(abs(A2[i][j]-(1 if i==j else 0))
           for i in range(3) for j in range(3))<1e-12
D=A[0][0]*A[2][2]-A[0][2]**2
assert abs(D+1)<1e-12
print('rotated_pair_det', f'{D:.15f}')

# Finite sanity checks for the purely algebraic comparison used in (3.11).
# These checks are not the proof; REPORT.md contains the exact inequalities.
samples=[
    (1,1,1,0.1,0.2,0.8),
    (2,3,4,0.1,0.15,0.7),
    (1,5,2,0.05,0.1,0.9),
]
for l1,l2,mu,r1,r2,r3 in samples:
    c=mu*r3*r3-l1*r1*r1-l2*r2*r2
    if c<=0:
        continue
    q=math.sqrt(r1*r1+r2*r2+r3*r3)
    L=max(l1,l2,mu)
    a=math.sqrt(mu)*abs(r3)
    b=math.sqrt(l1*r1*r1+l2*r2*r2)
    d=a-b
    lower1=d/math.sqrt(2*L)
    lower2=c/(2*L*q)
    assert lower1+1e-15>=lower2
    print('margin_check', lower1, lower2, True)

print('QFORM_B11_R22_CHECK_PASS')
