import sympy as sp
import mpmath as mp

# Exact algebra for the dense reflection/frame families.
n = sp.Matrix([1, 2, 4]) / sp.sqrt(21)
P = n * n.T
B = sp.eye(3) - 2 * P
V = sp.Matrix([
    [1, 1, 1],
    [1, -1, 1],
    [1, 1, -1],
    [1, -1, -1],
]) / 2

assert sp.simplify(P*P-P) == sp.zeros(3)
assert sp.simplify(B*B-sp.eye(3)) == sp.zeros(3)
assert B.eigenvals() == {sp.Integer(1): 2, sp.Integer(-1): 1}
assert sp.simplify(V.T*V-sp.eye(3)) == sp.zeros(3)

dots = [sp.simplify((V.row(i)*n)[0]) for i in range(4)]
assert [sp.simplify(2*sp.sqrt(21)*z) for z in dots] == [7, 3, -1, -5]

# q=1/2 compensated diffuse kernel C B C = I-(2-q)P = I-3P/2.
Kc = sp.simplify(V * (sp.eye(3) - sp.Rational(3,2)*P) * V.T)
Kc_expected = sp.Matrix([
    [-sp.Rational(1,8), -sp.Rational(1,8), sp.Rational(3,8), sp.Rational(3,8)],
    [-sp.Rational(1,8), sp.Rational(33,56), -sp.Rational(11,56), sp.Rational(29,56)],
    [sp.Rational(3,8), -sp.Rational(11,56), sp.Rational(41,56), sp.Rational(9,56)],
    [sp.Rational(3,8), sp.Rational(29,56), sp.Rational(9,56), sp.Rational(17,56)],
])
assert Kc == Kc_expected
assert all(z != 0 for z in Kc)

# Uncompensated diffuse kernel V B V^T, also entrywise nonzero.
K0 = sp.simplify(V*B*V.T)
K0_expected = sp.Matrix([
    [-sp.Rational(5,12), -sp.Rational(1,4), sp.Rational(5,12), sp.Rational(7,12)],
    [-sp.Rational(1,4), sp.Rational(15,28), -sp.Rational(5,28), sp.Rational(17,28)],
    [sp.Rational(5,12), -sp.Rational(5,28), sp.Rational(61,84), sp.Rational(11,84)],
    [sp.Rational(7,12), sp.Rational(17,28), sp.Rational(11,84), sp.Rational(13,84)],
])
assert K0 == K0_expected
assert all(z != 0 for z in K0)

# Scalar H(x)=sqrt(1+x)*int_{-1/2}^{1/2} exp(-6xu^2)du series.
x = sp.symbols('x', nonnegative=True)
Ftr = sum(
    (-6*x)**k/sp.factorial(k) * 2*sp.Rational(1,2)**(2*k+1)/(2*k+1)
    for k in range(7)
)
Hs = sp.series(sp.sqrt(1+x)*Ftr, x, 0, 6)
H_expected = 1 - sp.Rational(3,20)*x**2 + sp.Rational(11,70)*x**3 \
    - sp.Rational(129,1120)*x**4 + sp.Rational(237,3080)*x**5
assert sp.expand(Hs.removeO()-H_expected) == 0

# Orientation average: t is squared minority-axis component of v.
t, phi = sp.symbols('t phi', real=True)
beta = sp.sqrt(1-t)*sp.cos(phi) + sp.sqrt(t)
h = 2-beta**2
avg_h2 = sp.simplify(sp.integrate(sp.expand_trig(h**2), (phi, 0, 2*sp.pi))/(2*sp.pi))
assert sp.simplify(avg_h2 - (19+2*t-13*t**2)/8) == 0
# On t in [0,1], concavity makes the minimum an endpoint; values are 19/8 and 1.
assert sp.simplify(avg_h2.subs(t, 0)-sp.Rational(19,8)) == 0
assert sp.simplify(avg_h2.subs(t, 1)-1) == 0

# Exact compensated aligned q=1/2 cone-tip and partner q=1/2 global bound.
mp.mp.dps = 80
C0 = 3*mp.sqrt(2)
C_half = 2*mp.sqrt(3*mp.pi)*mp.erf(1/mp.sqrt(2))
C1 = 12*mp.e**(-mp.mpf('0.5'))/mp.sqrt(2*mp.pi)
J = mp.sqrt(mp.pi/3)*mp.erf(mp.sqrt(3)/2)
partner = C1 + (C0-C1)*J

assert C_half < C0
assert partner < mp.mpf('3.98')

print('PASS_QFORM_B17_ONE_MACRO_ORIENTATION_BARRIER')
print('C0_3sqrt2 =', mp.nstr(C0, 60))
print('compensated_q_half_tip =', mp.nstr(C_half, 60))
print('gap_to_3sqrt2 =', mp.nstr(C0-C_half, 60))
print('partner_q_half_global_bound =', mp.nstr(partner, 60))
print('avg_h2 = (19+2t-13t^2)/8; minimum 1 uniquely at t=1')
