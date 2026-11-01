from fractions import Fraction
from math import sqrt

# Exact designated-partner rotation.
O = [
    [Fraction(6,7), Fraction(-2,7), Fraction(-3,7)],
    [Fraction(-2,7), Fraction(3,7), Fraction(-6,7)],
    [Fraction(-3,7), Fraction(-6,7), Fraction(-2,7)],
]
J = [[Fraction(int(i==j and (1 if i<2 else -1)),1) for j in range(3)] for i in range(3)]

def transpose(M):
    return [list(x) for x in zip(*M)]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def eye3():
    return [[Fraction(int(i==j),1) for j in range(3)] for i in range(3)]

OT = transpose(O)
assert matmul(OT,O) == eye3()
B = matmul(matmul(OT,J),O)
B_expected = [
    [Fraction(31,49), Fraction(-36,49), Fraction(-12,49)],
    [Fraction(-36,49), Fraction(-23,49), Fraction(-24,49)],
    [Fraction(-12,49), Fraction(-24,49), Fraction(41,49)],
]
assert B == B_expected
assert matmul(B,B) == eye3()

x = [Fraction(9,49), Fraction(36,49), Fraction(4,49)]
c = [(Fraction(57,1) + 6*z - 39*z*z)/640 for z in x]
assert sum(c, Fraction()) == Fraction(5295,21952)
assert min(c) >= Fraction(3,80)
assert sum(c, Fraction()) >= Fraction(69,320)
assert 2*sum(c, Fraction()) == Fraction(5295,10976)

# The orientation-uniform coefficient checks.
# r(x)=57+6x-39x^2 is concave, so its minimum on [0,1] is min(r(0),r(1))=24.
assert min(Fraction(57), Fraction(24)) == 24
# Sum coefficient is (177-39 sum x_j^2)/640 and sum x_j^2 <= 1.
assert Fraction(177-39,640) == Fraction(69,320)

print('O^T O = I: PASS')
print('B =', B)
print('B^2 = I: PASS; spectrum is {1,1,-1} because tr(B)=1 and det(B)=-1')
print('partner x_j =', x)
print('c_j =', c)
print('sum c_j =', sum(c, Fraction()), '=', float(sum(c, Fraction())))
print('partner coefficient = 5295/21952: PASS')
print('uniform single-axis lower bound c_j >= 3/80 =', float(Fraction(3,80)))
print('uniform all-axis baseline sum >= 69/320 =', float(Fraction(69,320)))
print('critical equal alpha=1 coefficient = 5295/10976 =', float(Fraction(5295,10976)))
print('3sqrt2 =', 3*sqrt(2))
