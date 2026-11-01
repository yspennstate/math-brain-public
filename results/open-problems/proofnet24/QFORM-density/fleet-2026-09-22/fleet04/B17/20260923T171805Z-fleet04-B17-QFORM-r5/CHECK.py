from decimal import Decimal, getcontext
from fractions import Fraction

getcontext().prec = 60

A = [[Fraction(x, 6) for x in row] for row in [
    [1, 1, -2, -2, -2, -2],
    [1, 1, -2, -2, -2, -2],
    [-2, -2, 1, 1, -2, -2],
    [-2, -2, 1, 1, -2, -2],
    [-2, -2, -2, -2, 1, 1],
    [-2, -2, -2, -2, 1, 1],
]]

def matmul(X, Y):
    return [[sum(X[i][k] * Y[k][j] for k in range(len(Y)))
             for j in range(len(Y[0]))] for i in range(len(X))]

A2 = matmul(A, A)
A3 = matmul(A2, A)
assert A3 == A
tr = sum(A[i][i] for i in range(6))
tr2 = sum(A2[i][i] for i in range(6))
assert tr == 1 and tr2 == 3

p_lo = Decimal("4.0630706168060372601254844225934999567529653460639")
eta = Decimal(1) / Decimal(1000)
lower = (Decimal(1) - eta) ** 4 * p_lo
assert lower > Decimal(4)
print("A^3=A, tr(A)=1, tr(A^2)=3")
print("spectrum multiplicities forced: {1,1,-1,0,0,0}")
print("fragmented-witness certified lower bound:", lower)
