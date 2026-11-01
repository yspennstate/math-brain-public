from fractions import Fraction
import math

# Exact Householder rotation O and canonical H0 for 2 z w + v^2.
O = [[Fraction(6,7),Fraction(-2,7),Fraction(-3,7)],
     [Fraction(-2,7),Fraction(3,7),Fraction(-6,7)],
     [Fraction(-3,7),Fraction(-6,7),Fraction(-2,7)]]
H = [[Fraction(0),Fraction(0),Fraction(1)],
     [Fraction(0),Fraction(1),Fraction(0)],
     [Fraction(1),Fraction(0),Fraction(0)]]

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):
    return [list(x) for x in zip(*A)]
def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
           -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
           +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))
I = mm(tr(O),O)
assert I == [[Fraction(int(i==j)) for j in range(3)] for i in range(3)]
C = mm(mm(tr(O),H),O)
C_expected = [[Fraction(-32,49),Fraction(-36,49),Fraction(9,49)],
              [Fraction(-36,49),Fraction(33,49),Fraction(4,49)],
              [Fraction(9,49),Fraction(4,49),Fraction(48,49)]]
assert C == C_expected
assert det3(C) == -1
# Since C^2=I and tr C=1, spectrum is {-1,1,1}.
assert mm(C,C) == [[Fraction(int(i==j)) for j in range(3)] for i in range(3)]
assert sum(C[i][i] for i in range(3)) == 1

# Three canonical null rays l1=(1,0,0), l2=(0,0,1), l3=(1,sqrt(2),-1).
# Check Gram values directly: diagonal zero; off-diagonals 1,-1,1.
def hpair(x,y):
    return x[0]*y[2] + x[2]*y[0] + x[1]*y[1]
s2=math.sqrt(2.0)
L=[(1.0,0.0,0.0),(0.0,0.0,1.0),(1.0,s2,-1.0)]
G=[[hpair(x,y) for y in L] for x in L]
assert max(abs(G[i][i]) for i in range(3)) < 1e-12
assert abs(G[0][1]-1)<1e-12 and abs(G[0][2]+1)<1e-12 and abs(G[1][2]-1)<1e-12

C_compiler = 256*2**0.25
C_trace = 2*C_compiler
assert C_compiler < 304.438
assert C_trace < 608.875
print('compiler_constant', C_compiler)
print('trace_constant', C_trace)
print('C', C)
print('QFORM_ALIGNED_THREE_BANK_COMPILER_CHECK_PASS')
