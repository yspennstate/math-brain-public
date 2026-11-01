"""Exact regression checks for fleet01/B18 r35.

Requires sympy only for the symbolic determinant factorization.
"""
import sympy as sp

g1,g2,b1,b2,l1,l2,d=sp.symbols('g1 g2 b1 b2 l1 l2 d', real=True)
A=sp.Matrix([
    [0,g1,g2],
    [g1,2*l1*g1+d*b1**2,l1*g2+l2*g1+d*b1*b2],
    [g2,l1*g2+l2*g1+d*b1*b2,2*l2*g2+d*b2**2],
])
expected=-d*(g1*b2-g2*b1)**2
assert sp.expand(A.det()-expected)==0

# Target-level concentrated-minor constant for |det| >= 1/320.
C=3*(2**(2/3))*(320**(1/3))
print('det factor:', sp.factor(A.det()))
print('C_1/320 =', C)
assert C < 32.574

# Heavy-star counting check: if at most 32 nonzero summands are each <1/320,
# their total is <1/10, contradicting the target-normalized sum >1/10.
assert sp.Rational(32,320)==sp.Rational(1,10)
