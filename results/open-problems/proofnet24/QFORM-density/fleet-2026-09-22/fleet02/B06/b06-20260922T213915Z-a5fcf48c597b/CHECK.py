from fractions import Fraction
import math
import sympy as sp

eps = sp.Rational(1, 8)

# Coordinates: U1,U2,V1,V2,W.
A = sp.zeros(5)
A[0,1] = A[1,0] = eps**-2
A[0,3] = A[3,0] = 1
A[1,2] = A[2,1] = 1
A[2,3] = A[3,2] = eps**2
A[4,4] = 1

charpoly = sp.factor(A.charpoly().as_expr())
expected = sp.factor(
    sp.Symbol("lambda")**2
    * (sp.Symbol("lambda") - 1)
    * (64*sp.Symbol("lambda") - 4097)
    * (64*sp.Symbol("lambda") + 4097) / 4096
)
assert sp.expand(charpoly - expected) == 0

eigs = A.eigenvals()
assert eigs[sp.Rational(4097,64)] == 1
assert eigs[-sp.Rational(4097,64)] == 1
assert eigs[sp.Integer(1)] == 1
assert eigs[sp.Integer(0)] == 2

# Prior two-sided-curvature stress matrix has cross block H=[[0,1],[1,0]].
H = sp.Matrix([[0,1],[1,0]])
assert H.singular_values() == [1,1]

c0_sq = sp.Rational(499487, 524256)
c0 = math.sqrt(float(c0_sq))
partner_exact_rank2_constant = 512 / math.sqrt(c0)
grouped_unit_projection_constant = 4 * math.sqrt(2) * math.e

print("PASS")
print("charpoly =", charpoly)
print("spectrum =", sorted([str(x) for x in eigs.keys()]))
print("c0^2 =", c0_sq)
print("c0 =", f"{c0:.12f}")
print("512/sqrt(c0) =", f"{partner_exact_rank2_constant:.12f}")
print("4*sqrt(2)*e =", f"{grouped_unit_projection_constant:.12f}")
