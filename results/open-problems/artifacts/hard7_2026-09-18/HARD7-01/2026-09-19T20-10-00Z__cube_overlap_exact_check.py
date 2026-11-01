from sympy import symbols, Rational, pi, sin, integrate, simplify, expand, factor

# HARD7-01 exact symbolic self-check for the 3D cube overlap proof.
# This checks only algebraic identities used in the on-page analytic proof.

a,b = symbols("a b", real=True)
x = symbols("x", positive=True)
f = x**Rational(-3,2)
fp = f.diff(x).subs(x,1)
fpp = f.diff(x,2).subs(x,1)
xp = -2*a
xpp = 4*b
h1 = simplify(fp*xp)
h2 = simplify(fpp*xp**2 + fp*xpp)
assert h1 == 3*a
assert h2 == 15*a**2 - 6*b
print("RADIAL_TAYLOR_PASS", h1, h2)

p,q,D,O = symbols("p q D O", real=True)
Area = 3*p + 6*q
interior = expand(5*((p-q)*D + 2*q*O) - Rational(2,3)*Area*(D+O))
assert simplify(interior - (p-3*q)*(3*D-2*O)) == 0
print("INTERIOR_DECOMP_PASS", factor(interior))

alpha,phi = symbols("alpha phi", real=True)
M = 2*pi - 8*alpha
S2 = 4*integrate(sin(2*phi)**2, (phi,alpha,pi/2-alpha))
assert simplify(S2 - (M/2 + sin(4*alpha))) == 0
print("FACE_ARC_INTEGRAL_PASS", simplify(S2))

u = symbols("u", real=True)
z = (1+u)/2
gap = simplify(2*z - z**2 - Rational(1,2))
assert expand(gap - (Rational(1,4) + u*(2-u)/4)) == 0
print("SCALAR_GAP_DECOMP_PASS", factor(gap))
print("For 0<=u<=1, gap >= 1/4 exactly.")

# Boundary-energy bookkeeping for A_12=A_21=1:
s,r0,S2sym,Msym = symbols("s r0 S2 M", positive=True)
J = 8*s**2*r0**3*Msym + 2*r0**5*S2sym
penalty_half = expand((s/r0)*J/2)
expected = 4*s**3*r0**2*Msym + s*r0**4*S2sym
assert simplify(penalty_half-expected)==0
print("BOUNDARY_BOOKKEEPING_PASS", expected)

print("ALL_EXACT_CHECKS_PASS = True")
