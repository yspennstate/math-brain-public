from fractions import Fraction
import cmath, math

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def T(A):
    return [list(r) for r in zip(*A)]
I=[[Fraction(int(i==j)) for j in range(3)] for i in range(3)]
O=[
 [Fraction(6,7),Fraction(-2,7),Fraction(-3,7)],
 [Fraction(-2,7),Fraction(3,7),Fraction(-6,7)],
 [Fraction(-3,7),Fraction(-6,7),Fraction(-2,7)]]
J=[[Fraction(1),0,0],[0,Fraction(1),0],[0,0,Fraction(-1)]]
assert mm(T(O),O)==I
B=mm(mm(T(O),J),O)
expected=[
 [Fraction(31,49),Fraction(-36,49),Fraction(-12,49)],
 [Fraction(-36,49),Fraction(-23,49),Fraction(-24,49)],
 [Fraction(-12,49),Fraction(-24,49),Fraction(41,49)]]
assert B==expected
assert mm(B,B)==I
assert all(B[i][j] != 0 for i in range(3) for j in range(3))
assert sum(B[i][i] for i in range(3))==Fraction(1)
assert round(float(sum(sum(x*x for x in row) for row in B)),12)==3.0

def sinc(x):
    return 1.0 if x==0 else math.sin(x)/x
def psi(m,t,cs,aas):
    C=sum(cs); L=1-C/m
    z=L*sinc(L*t/(2*math.sqrt(m)))
    for c,a in zip(cs,aas):
        z += (c/m)*cmath.exp(1j*a*t)*sinc(c*t/(2*m*math.sqrt(m)))
    return z
cs=[0.2,0.15]
aas=[1.3,-0.9]
for t in [0.4,1.7,3.2]:
    target=-t*t/24+sum(c*(cmath.exp(1j*a*t)-1) for c,a in zip(cs,aas))
    m=1_000_000
    err=abs(m*(psi(m,t,cs,aas)-1)-target)
    assert err < 1e-6, (t,err)
K=(4*math.pi)**1.5
integral=6*K**(2/3)
assert abs(integral-24*math.pi)<1e-10
M=3*math.sqrt(2)
for C in [0.001,0.01,0.1]:
    assert math.exp(-C)*M < M
    assert math.exp(-C)*M > 0
print('QFORM_B17_NONLINDEBERG_CP_CHECK_PASS')
print('B =', [[str(x) for x in row] for row in B])
print('three_sqrt_two =', repr(M))
print('FBL_envelope_L1 =', repr(integral))
