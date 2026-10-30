#!/usr/bin/env python3
from fractions import Fraction as F
import math
import mpmath as mp

# Exact rational matrix checks.
R=[[F(1,2),F(1,2),F(1,2)],
   [F(1,2),F(-1,2),F(1,2)],
   [F(1,2),F(1,2),F(-1,2)],
   [F(1,2),F(-1,2),F(-1,2)]]
B=[[F(599,697),F(-252,697),F(-252,697)],
   [F(-252,697),F(49,697),F(-648,697)],
   [F(-252,697),F(-648,697),F(49,697)]]
A_expected=[[F(-1607,2788),F(95,2788),F(95,2788),F(1797,2788)],
            [F(95,2788),F(1993,2788),F(-795,2788),F(1103,2788)],
            [F(95,2788),F(-795,2788),F(1993,2788),F(1103,2788)],
            [F(1797,2788),F(1103,2788),F(1103,2788),F(409,2788)]]

def T(M): return [list(x) for x in zip(*M)]
def mm(A,B):
    BT=T(B)
    return [[sum(x*y for x,y in zip(row,col)) for col in BT] for row in A]
def eye(n): return [[F(int(i==j)) for j in range(n)] for i in range(n)]
def tr(M): return sum(M[i][i] for i in range(len(M)))

assert mm(T(R),R)==eye(3)
assert mm(B,B)==eye(3)
A=mm(mm(R,B),T(R))
assert A==A_expected
assert mm(mm(A,A),A)==A
assert tr(A)==F(1)
assert tr(mm(A,A))==F(3)
assert all(A[i][j] != 0 for i in range(4) for j in range(4))

# Directed interval-style midpoint lower certificate for
# p(0)=1/sqrt(2) int_0^{2pi} 1/H(omega(theta)) dtheta.
# H=max_{i<j, signs} (sign_i*x_i+sign_j*x_j).
# h(theta)=H(omega(theta)) and 1/h(theta) are 1-Lipschitz, so
# the midpoint discretization error for the integral is <= pi^2/N.
mp.iv.dps=30
I=mp.iv
N=30000
r=I.mpf(7)/18
d=I.sqrt(r*r+2)
rt2=I.sqrt(2)
n=[r/d,1/d,1/d]
e1=[I.mpf(0),1/rt2,-1/rt2]
e2=[-rt2/d,r/(rt2*d),r/(rt2*d)]
twopi=2*I.pi
lower_sum=0.0
# Conversion of interval endpoints to IEEE double is padded by 2e-15;
# final density lower bound is padded again by 1e-10.
endpoint_pad=2e-15
for k in range(N):
    th=twopi*(I.mpf(k)+I.mpf('0.5'))/N
    c=I.cos(th); s=I.sin(th)
    w=[(n[j]+e1[j]*c+e2[j]*s)/rt2 for j in range(3)]
    H_uppers=[]
    for a,b in ((0,1),(0,2),(1,2)):
        for sa in (1,-1):
            for sb in (1,-1):
                v=sa*w[a]+sb*w[b]
                H_uppers.append(float(v.b)+endpoint_pad)
    H_upper=max(H_uppers)
    lower_sum += 1.0/H_upper

Delta=2*math.pi/N
midpoint_error=math.pi**2/N
p_lower=(Delta*lower_sum-midpoint_error)/math.sqrt(2)-1e-10
print('exact_matrix_checks=PASS')
print('N=',N)
print('certified_safe_lower=',repr(p_lower))
print('3sqrt2=',repr(3*math.sqrt(2)))
assert p_lower > 3.5605
assert 3.5605 < 3*math.sqrt(2)
print('PASS QFORM_B17_TETRA_RATIONAL_7_18')
