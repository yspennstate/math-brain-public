import sympy as sp


t = sp.symbols("t")
k = sp.Rational(1, 2)
den = t**2 + 1 + k**2
x = 2*t/den
y = -2*k/den
z = (t**2 + k**2 - 1)/den

assert sp.simplify(x*x + y*y + z*z - 1) == 0
assert sp.simplify(y + k*(1-z)) == 0

# Degree <=2 polynomials in (x,y,z), restricted to the rational circle.
mons = [1,x,y,z,x**2,y**2,z**2,x*y,x*z,y*z]
polys = [sp.Poly(sp.expand(sp.together(m*den**2)), t) for m in mons]
M = sp.Matrix([[p.coeff_monomial(t**d) for p in polys] for d in range(5)])
assert M.rank() == 5
assert len(M.nullspace()) == 5

X,Y,Z = sp.symbols("X Y Z")
ell = Y + k*(1-Z)
sphere = X**2 + Y**2 + Z**2 - 1
monXYZ = [1,X,Y,Z,X**2,Y**2,Z**2,X*Y,X*Z,Y*Z]

def vec(expr):
    p = sp.Poly(sp.expand(expr), X,Y,Z)
    return sp.Matrix([p.coeff_monomial(m) for m in monXYZ])

ideal_basis = [sphere, ell, ell*X, ell*Y, ell*Z]
B = sp.Matrix.hstack(*[vec(e) for e in ideal_basis])
N = sp.Matrix.hstack(*M.nullspace())
assert B.rank() == 5
assert sp.Matrix.hstack(B,N).rank() == 5

# Affine functions vanishing on the circle are exactly multiples of ell.
aff = [1,x,y,z]
ap = [sp.Poly(sp.expand(sp.together(m*den)), t) for m in aff]
A = sp.Matrix([[p.coeff_monomial(t**d) for p in ap] for d in range(3)])
assert A.rank() == 3
ns = A.nullspace()
assert len(ns) == 1
v = ns[0]
assert v == sp.Matrix([-1,0,-2,1]) or v == sp.Matrix([1,0,2,-1])

print("PASS MOC4-MSQR-TRANSVERSE-TRUST-SQUARE-v1 algebra check")
print("circle_parameterization_exact = True")
print("quadratic_restriction_rank =", M.rank())
print("quadratic_vanishing_dimension =", len(M.nullspace()))
print("circle_ideal_degree2_rank =", B.rank())
print("combined_rank =", sp.Matrix.hstack(B,N).rank())
print("affine_vanishing_dimension =", len(ns))
print("affine_null_vector =", tuple(v))
