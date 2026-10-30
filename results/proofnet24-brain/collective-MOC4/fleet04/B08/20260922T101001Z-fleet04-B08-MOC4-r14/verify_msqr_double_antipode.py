import sympy as sp

# Positive square roots of the two scalar pair curvatures.
A, B = sp.symbols('A B', positive=True)
theta, phi, t = sp.symbols('theta phi t', real=True)

lam = B**2
mu = A**2
m33 = (lam + mu) / 2
mab = A*B

# Verify the exact square algebraically in independent half-angle variables.
u, v = sp.symbols('u v', real=True)
cos_th = (1-u**2)/(1+u**2)
sin_th = 2*u/(1+u**2)
cos_ph = (1-v**2)/(1+v**2)
sin_ph = 2*v/(1+v**2)
E_uv = (
    lam*(cos_th - 1)
    + mu*(cos_ph - 1)
    + m33*(cos_th - 1)*(cos_ph - 1)
    + mab*sin_th*sin_ph
)
square_uv = -2*(B*u/sp.sqrt(1+u**2)/sp.sqrt(1+v**2)
                 - A*v/sp.sqrt(1+v**2)/sp.sqrt(1+u**2))**2
residual = sp.factor(E_uv - square_uv)
print('two_angle_square_residual =', residual)
assert residual == 0

# Keep the trigonometric form for differentiation below.
ct, st = sp.cos(theta), sp.sin(theta)
cp, spn = sp.cos(phi), sp.sin(phi)
E = (
    lam*(ct - 1)
    + mu*(cp - 1)
    + m33*(ct - 1)*(cp - 1)
    + mab*st*spn
)

# Rational half-angle parametrization of the exact zero locus:
# B tan(theta/2) = A tan(phi/2).
v_flat = B*u/A
E_zero = sp.factor(E_uv.subs(v, v_flat))
print('flat_curve_half_angle_residual =', E_zero)
assert E_zero == 0

# The lead's canonical kernel great-circle ray has theta=A t, phi=B t.
square_geo = -2*(B*sp.sin(A*t/2)*sp.cos(B*t/2)
                - A*sp.sin(B*t/2)*sp.cos(A*t/2))**2
# The general half-angle calculation above proves Egeo equals this square exactly.
Egeo = square_geo
J = {k: sp.factor(sp.diff(Egeo, t, k).subs(t, 0)) for k in range(2, 7)}
for k in range(2, 7):
    print(f'J{k} =', J[k])
assert J[2] == J[3] == J[4] == J[5] == 0
J6_expected = -sp.Rational(5,2)*A**2*B**2*(A**2-B**2)**2
print('J6_expected =', sp.factor(J6_expected))
assert sp.factor(J[6]-J6_expected) == 0

# Exact nonlinear flat curve tangent to the kernel ray.
phi_curve = 2*sp.atan((B/A)*sp.tan(A*t/2))
phi_series = sp.series(phi_curve, t, 0, 7).removeO().expand()
print('phi_curve_series =', phi_series)
assert sp.expand(phi_series.coeff(t,1) - B) == 0
assert sp.expand(phi_series.coeff(t,3) - (A**2*B-B**3)/12) == 0
assert sp.expand(phi_series.coeff(t,5) - (A**4*B/sp.Integer(120) - A**2*B**3/sp.Integer(48) + B**5/sp.Integer(80))) == 0

# Standard simple-kernel Lyapunov-Schmidt sixth-order coefficient:
# if beta=0, then E6 = J6 + 10 <delta#, A^+ delta#>.
a, d, j6 = sp.symbols('a d j6', positive=True)
y3 = d/(6*a)
# Model Taylor term: -a y^2/2 + d t^3 y/6 + j6 t^6/720.
coef6 = sp.expand(-a*y3**2/2 + d*y3/6 + j6/sp.Integer(720))
E6 = sp.factor(720*coef6)
print('LS6_one_range =', E6)
assert sp.factor(E6 - (j6 + 10*d**2/a)) == 0

S_required = sp.factor(-J6_expected/10)
print('LS6_flat_curve_reserve =', S_required)
assert sp.factor(S_required - sp.Rational(1,4)*A**2*B**2*(A**2-B**2)**2) == 0

# Balanced scalar case: the canonical kernel geodesic itself is exactly flat.
balanced = sp.simplify(Egeo.subs(B,A))
print('balanced_geodesic_profile =', balanced)
assert balanced == 0

print('PASS MOC4-MSQR-DOUBLE-ANTIPODE-FLAT-CURVE-v1')
