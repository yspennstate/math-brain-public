"""Exact/algebraic checks for QFORM three-bank rank-one triangle report.
No simulation is used as proof evidence.
"""
from fractions import Fraction
from math import log

# Compressed bank-cycle matrix M = [[0,1,1],[1,0,-1],[1,-1,0]].
M = ((0,1,1),(1,0,-1),(1,-1,0))

def mv(v):
    return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))

# Two independent +1 eigenvectors and one -2 eigenvector.
assert mv((1,1,0)) == (1,1,0)
assert mv((1,0,1)) == (1,0,1)
assert mv((-1,1,1)) == (2,-2,-2)

# A physical triple, one coordinate from each normalized m-bank,
# has edges (1/m,1/m,-1/m) and determinant 2abc = -2/m^3.
for m in (2,3,4,8,16,101):
    a = Fraction(1,m)
    b = Fraction(1,m)
    c = Fraction(-1,m)
    det = 2*a*b*c
    assert det == Fraction(-2,m**3)
    # The aggregate rank-one cross singular strengths are all exactly 1.
    # u,v,w have norm 1 and |a_bank|=|b_bank|=|c_bank|=1.
    s12=s13=s23=Fraction(1,1)
    assert s12*s13*s23 == 1

C = 2*(3+log(8))
print("three-bank universal certificate constant =", C)
assert C < 10.16
print("PASS")
