"""Exact/scalar checks for B16-20260922T135620Z-r11.
Not a proof certificate; the analytic proof is in REPORT.md.
"""
from fractions import Fraction
from math import exp, sqrt

H = [[1,1,1],[1,1,-1],[1,-1,1]]

def det3(M):
    return (M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])
            -M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])
            +M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0]))

def det_lambda(M, lam):
    N = [[Fraction(M[i][j]) - (Fraction(lam) if i==j else 0)
          for j in range(3)] for i in range(3)]
    return det3(N)

assert det3(H) == -4
assert det_lambda(H, -1) == 0
assert det_lambda(H, 2) == 0
# trace=3 and determinant=-4 force roots {-1,2,2} given the two checked roots.
assert sum(H[i][i] for i in range(3)) == 3

# Pivot a=1, b=(1,1), C=[[1,-1],[-1,1]].
a = Fraction(1)
b0,b1 = Fraction(1),Fraction(1)
C = [[Fraction(1),Fraction(-1)],[Fraction(-1),Fraction(1)]]
S = [[C[0][0]-b0*b0/a, C[0][1]-b0*b1/a],
     [C[1][0]-b1*b0/a, C[1][1]-b1*b1/a]]
assert S == [[0, -2],[-2,0]]
assert S[0][0]*S[1][1]-S[0][1]*S[1][0] == -4

# Weak-L2 scalar calculus constant used in REPORT.md.
assert 64*exp(-1.5) < 15
# Pure-bilinear Hadamard bound: 4 sqrt(2) |det S|^{-1/4} = 4.
pure = 4*sqrt(2)*(4**(-0.25))
assert abs(pure-4.0) < 1e-12
print("PASS")
print("det(H)=-4; roots checked at -1 and 2; Schur=[[0,-2],[-2,0]]")
print("64*exp(-3/2)=", 64*exp(-1.5))
print("Hadamard pure-bilinear bound=", pure)
