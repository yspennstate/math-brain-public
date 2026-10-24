import sympy as sp

rt2, rt3 = sp.sqrt(2), sp.sqrt(3)
B = sp.Matrix([
    [sp.Rational(1,3), -sp.Rational(2,3), -sp.Rational(2,3)],
    [-sp.Rational(2,3), sp.Rational(1,3), -sp.Rational(2,3)],
    [-sp.Rational(2,3), -sp.Rational(2,3), sp.Rational(1,3)],
])
assert B * B == sp.eye(3)
assert sp.trace(B) == 1 and sp.det(B) == -1

d0 = sp.Matrix([1, 1, 4 - 3 * rt2])
assert sp.simplify((d0.T * B * d0)[0]) == 0
Bd0 = sp.simplify(B * d0)
assert sp.simplify(Bd0[2] + rt2) == 0
assert sp.simplify((d0.T * d0)[0] - 12 * (rt2 - 1) ** 2) == 0

R = sp.Integer(2)
explicit_bound = sp.simplify(2 / (R - rt3 / 2))
assert explicit_bound < 2
assert 2 < 3 * rt2

# Exact base-cone value from the completed account03/B17 finite witness.
p0 = (
    -sp.Rational(165, 4)
    + 12 * rt3
    + 15 * rt2
    + 22 * rt3 * sp.log((sp.sqrt(6) + 3 * rt2) / 6)
    + rt3 * sp.log((1 + rt2 - 1 / rt3) / (1 + rt2 + 1 / rt3))
)
gap = 3 * rt2 - p0
assert gap > 0

print("PASS QFORM-HOUSEHOLDER-IRRATIONAL-FINITE-FRAGMENT-NOESCAPE-v1")
print("B^2 =", B * B)
print("trace(B), det(B) =", sp.trace(B), sp.det(B))
print("q(d0) =", sp.simplify((d0.T * B * d0)[0]))
print("B d0 =", list(Bd0))
print("||d0||^2 =", sp.simplify((d0.T * d0)[0]))
print("explicit R=2 global null-cell bound =", sp.N(explicit_bound, 30))
print("base p_*(0) =", sp.N(p0, 50))
print("3sqrt2-p_*(0) =", sp.N(gap, 50))
