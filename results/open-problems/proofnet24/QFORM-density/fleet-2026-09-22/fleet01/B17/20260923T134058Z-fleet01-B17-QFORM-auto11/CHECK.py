#!/usr/bin/env python3
import math
from fractions import Fraction as F


def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))]
            for i in range(len(A))]


def same(A,B):
    return all(A[i][j] == B[i][j]
               for i in range(len(A)) for j in range(len(A[0])))


def simpson(f,a,b,n=400000):
    if n % 2:
        n += 1
    h=(b-a)/n
    s=f(a)+f(b)
    s += 4*sum(f(a+(2*k-1)*h) for k in range(1,n//2+1))
    s += 2*sum(f(a+2*k*h) for k in range(1,n//2))
    return s*h/3

# Exact six-coordinate unequal-bank stress matrix.
A=[[F(0) for _ in range(6)] for __ in range(6)]
A[0][0]=F(1)
P=[[F(1,2),F(1,2)],[F(1,2),F(1,2)]]
N=[[-F(4,9),-F(2,9),-F(4,9)],
   [-F(2,9),-F(1,9),-F(2,9)],
   [-F(4,9),-F(2,9),-F(4,9)]]
for i in range(2):
    for j in range(2):
        A[1+i][1+j]=P[i][j]
for i in range(3):
    for j in range(3):
        A[3+i][3+j]=N[i][j]
A2=matmul(A,A)
A3=matmul(A2,A)
assert same(A3,A)
assert sum(A[i][i] for i in range(6)) == F(1)
assert sum(A2[i][i] for i in range(6)) == F(3)
# Symmetric A^3=A => eigenvalues lie in {-1,0,1}; trace A=1 and trace A^2=3
# force multiplicities +1,+1,-1 and three zeros.

sqrt2=math.sqrt(2.0)
sqrt3=math.sqrt(3.0)
Ksec=math.pi*(5*sqrt2-2)/3 - 2*sqrt3*(sqrt2-1)
Kpartner=math.pi/2*(sqrt2+2**0.25)
Ktarget=3*sqrt2
Krational=(40*sqrt2+26)/21
assert Ksec < Krational < Ktarget
assert Ksec < Kpartner < Ktarget

# Verify the chord majorant u^{-1/2} <= (2sqrt2-1)+2(1-sqrt2)u.
for j in range(100001):
    u=0.5+0.5*j/100000
    chord=(2*sqrt2-1)+2*(1-sqrt2)*u
    assert u**(-0.5) <= chord + 2e-15

# A numerical scale check for the sharper integral K_cone.  Remove the endpoint
# singularity by u=sin(theta): integral from 1/2 to 1 becomes
# int_{pi/6}^{pi/2} [sin(theta)]^{-1/2} dtheta.
f=lambda th: 1/math.sqrt(math.sin(th))
I=simpson(f,math.pi/6,math.pi/2,200000)
Kcone=math.pi*sqrt2/3 + 2*I
assert Kcone < Ksec < Ktarget

print('K_cone_numeric = %.15f' % Kcone)
print('K_sec          = %.15f' % Ksec)
print('partner_Kstar  = %.15f' % Kpartner)
print('3sqrt2         = %.15f' % Ktarget)
print('rational_upper = %.15f' % Krational)
print('trace(A)       =', sum(A[i][i] for i in range(6)))
print('trace(A^2)     =', sum(A2[i][i] for i in range(6)))
print('A^3=A          =', same(A3,A))
print('QFORM_B17_UNEQUAL_BANK_CHECK_PASS')
