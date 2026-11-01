import sympy as sp

rt3 = sp.sqrt(3)
t = [
    sp.Matrix([1, 1, 1]) / rt3,
    sp.Matrix([1, -1, -1]) / rt3,
    sp.Matrix([-1, 1, -1]) / rt3,
    sp.Matrix([-1, -1, 1]) / rt3,
]
frame = sum((u*u.T for u in t), sp.zeros(3))
assert sp.simplify(frame - sp.Rational(4,3)*sp.eye(3)) == sp.zeros(3)

n = sp.Matrix([1,2,3]) / sp.sqrt(14)
B = sp.eye(3) - 2*n*n.T
assert sp.simplify(B*B-sp.eye(3)) == sp.zeros(3)
assert sp.simplify(B.det()) == -1
assert B.eigenvals() == {-1: 1, 1: 2}

C = sp.Matrix([[sp.simplify((u.T*B*v)[0]) for v in t] for u in t])
assert all(x != 0 for x in C)
expected = sp.Matrix([
    [sp.Rational(-5,7), sp.Rational(17,21), sp.Rational(5,21), sp.Rational(-1,3)],
    [sp.Rational(17,21), sp.Rational(5,21), sp.Rational(-5,7), sp.Rational(-1,3)],
    [sp.Rational(5,21), sp.Rational(-5,7), sp.Rational(17,21), sp.Rational(-1,3)],
    [sp.Rational(-1,3), sp.Rational(-1,3), sp.Rational(-1,3), 1],
])
assert C == expected

# The common Theorem-F majorant M(t)=min(1,K|t|^(-3/2)), K=(4*pi)^(3/2),
# has mass 2[K^(2/3) + 2K*K^(-1/3)] = 6K^(2/3) = 24*pi.
K23 = 4*sp.pi
assert sp.simplify(6*K23 - 24*sp.pi) == 0

print("PASS_QFORM_FINITE_TIGHT_FRAME_POISSON_LOCATION_BARRIER")
print("frame_sum =")
print(frame)
print("B =")
print(B)
print("det(B) =", B.det())
print("spectrum(B) =", B.eigenvals())
print("group coefficient table =")
print(C)
print("Theorem-F majorant L1 mass =", 24*sp.pi)
print("sharp Gaussian barrier =", 3*sp.sqrt(2), "~", sp.N(3*sp.sqrt(2), 16))
