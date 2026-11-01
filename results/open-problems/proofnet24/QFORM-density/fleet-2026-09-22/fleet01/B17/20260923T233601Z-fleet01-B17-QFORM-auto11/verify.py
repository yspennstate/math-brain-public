import sympy as sp

# Exact matrix checks for QFORM-GAUSSIAN-SPECTRAL-SLACK-RIGIDITY-v1.
d = sp.symbols('d', real=True)
O = sp.Matrix([[6,-2,-3],[-2,3,-6],[-3,-6,-2]])/7
R0 = sp.Matrix([[1,1,1],[1,-1,1],[1,1,-1],[1,-1,-1]])/2
B = sp.simplify(O.T * sp.diag(1,1,-(1+d)) * O)
M = sp.simplify(R0 * B * R0.T)

assert sp.simplify(O.T*O-sp.eye(3)) == sp.zeros(3)
assert sp.simplify(R0.T*R0-sp.eye(3)) == sp.zeros(3)
lam = sp.symbols('lam')
assert sp.factor(B.charpoly(lam).as_expr()) == (lam-1)**2*(lam+1+d)

expected = sp.Matrix([
[-95-121*d, 71+11*d, -105-77*d, 61+55*d],
[71+11*d, 145-d, -35+7*d, 39-5*d],
[-105-77*d, -35+7*d, 49-49*d, 119+35*d],
[61+55*d, 39-5*d, 119+35*d, 97-25*d],
])
assert sp.simplify(196*M-expected) == sp.zeros(4)

# Every numerator has a fixed nonzero sign for 0 <= d < 1.
tests = [
    -95-121*d, 71+11*d, -105-77*d, 61+55*d,
    145-d, -35+7*d, 39-5*d, 49-49*d,
    119+35*d, 97-25*d,
]
for e in tests:
    # Endpoint signs; linear expressions cannot cross zero if same strict sign.
    e0 = sp.N(e.subs(d,0))
    e1 = sp.N(e.subs(d,sp.Rational(999999,1000000)))
    assert e0 != 0 and e1 != 0 and (e0 > 0) == (e1 > 0)

# Exact partner-family cone integral.
theta = sp.symbols('theta', real=True)
c, s = sp.cos(theta), sp.sin(theta)
inner = sp.integrate((1-sp.symbols('t')*c)*(1-sp.symbols('t')*s)*(1-sp.symbols('t')),
                     (sp.symbols('t'),0,1))
inner = sp.simplify(inner)
assert sp.simplify(inner - (sp.Rational(1,2)-(c+s)/6+c*s/12)) == 0
partner_tip = sp.simplify(8*sp.integrate(inner,(theta,0,sp.pi/2)))
assert partner_tip == 2*sp.pi-sp.Rational(7,3)
assert float(partner_tip) < float(3*sp.sqrt(2))

print('QFORM_B17_GAUSSIAN_SPECTRAL_SLACK_CHECK_PASS')
print('partner_tip =', sp.N(partner_tip, 18))
print('3sqrt2 =', sp.N(3*sp.sqrt(2), 18))
print('dense_core_196M =')
print(expected)
