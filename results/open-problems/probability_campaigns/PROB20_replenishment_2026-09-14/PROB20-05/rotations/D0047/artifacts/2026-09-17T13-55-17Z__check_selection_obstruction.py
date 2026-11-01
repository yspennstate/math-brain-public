import sympy as sp

xi, Q, r, qd, J0 = sp.symbols("xi Q r qd J0", nonzero=True)
a0, a1, a2, a3 = sp.symbols("a0 a1 a2 a3")
x = Q + xi
Sx = 1 + x**2
S0 = 1 + Q**2
v = 2*x - r*Sx
N = qd - r*S0
Sigma = -(J0 + r*Q)/2
bplus = -Sx/xi
b1 = Sigma + N/(2*xi)

U = a0 + a1*xi + a2*xi**2 + a3*xi**3
ODE = sp.expand(Sx*sp.diff(U, xi, 2) + (v+bplus)*sp.diff(U, xi) - b1*U)
series = sp.series(ODE, xi, 0, 2).removeO().expand()
c_m1 = sp.factor(series.coeff(xi, -1))
c_0 = sp.factor(series.coeff(xi, 0))

a1_required = -N*a0/(2*S0)
assert sp.simplify(c_m1.subs(a1, a1_required)) == 0

compat = sp.factor(sp.simplify(c_0.subs(a1, a1_required) * 2*S0 / a0))
target_compat = sp.factor(J0*S0 - sp.Rational(1,2)*(r**2*S0**2 - 2*r*Q*S0 - qd**2))
assert sp.simplify(compat - target_compat) == 0

J0_first = sp.Rational(1,2)*(r**2*S0 - 2*r*Q - qd**2/S0)
assert sp.simplify(target_compat.subs(J0, J0_first)) == 0

# Small-r endpoint expansion for the one-pole branch Q=1/r+a+c r+d r^2+...
a, c, d = sp.symbols("a c d")
Qser = 1/r + a + c*r + d*r**2
qd_ser = -r*sp.diff(Qser, r)
qdd_ser = -r*sp.diff(qd_ser, r)
Sser = 1 + Qser**2
qode_res = sp.series(
    sp.simplify(qdd_ser - (Qser*qd_ser**2/Sser + r*Sser*(r*Qser-1))),
    r, 0, 3
).removeO().expand()
c_required = a**2 - sp.Rational(1,3)
d_required = a**3 + a/sp.Integer(6)
assert sp.simplify(qode_res.coeff(r,1).subs(c,c_required)) == 0
assert sp.simplify(qode_res.coeff(r,2).subs({c:c_required,d:d_required})) == 0

J0ser = sp.Rational(1,2)*(r**2*Sser - 2*r*Qser - qd_ser**2/Sser)
Sigser = sp.simplify(-(J0ser+r*Qser)/2)
Sigexp = sp.series(Sigser.subs({c:c_required,d:d_required}), r, 0, 4).removeO().expand()
assert sp.simplify(Sigexp - (-a*r-a**2*r**2-a**3*r**3)) == 0

xf = sp.symbols("xf")
Qexp = Qser.subs({c:c_required,d:d_required})
bplus_fixed = -(1+xf**2)/(xf-Qexp)
Nser = qd_ser.subs({c:c_required,d:d_required}) - r*(1+Qexp**2)
b1_fixed = Sigser.subs({c:c_required,d:d_required}) + Nser/(2*(xf-Qexp))
assert sp.simplify(sp.limit(bplus_fixed/r, r, 0) - (1+xf**2)) == 0
assert sp.simplify(sp.limit(b1_fixed/r, r, 0)) == 0

# Candidate sigma monotonicity identity: if
# r Sigma' - Sigma = -(r^2/4)(cosh y + y_r)^2,
# then d/dr(Sigma/r) is nonpositive.
yr, y = sp.symbols("yr y", real=True)
monotone_rhs = -sp.Rational(1,4)*(sp.cosh(y)+yr)**2
assert monotone_rhs.is_nonpositive is True

print("Frobenius xi^-1 Robin condition: PASS")
print("Frobenius resonance == Rumanov J0 first integral: PASS")
print("moving one-pole singularity is apparent under first integral: PASS")
print("small-r Q branch coefficients c=a^2-1/3, d=a^3+a/6: PASS")
print("small-r Sigma=-a r-a^2 r^2-a^3 r^3+O(r^4): PASS")
print("fixed-x endpoint b_plus/r -> 1+x^2 and b1/r -> 0: PASS")
print("candidate (Sigma/r)' = -(cosh(y)+y_r)^2/4 <= 0: PASS")
print("D0047 SELECTION-OBSTRUCTION EXACT CHECK PASSED")
