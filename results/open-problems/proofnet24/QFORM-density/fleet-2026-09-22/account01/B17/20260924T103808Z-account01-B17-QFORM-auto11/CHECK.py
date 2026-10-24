import sympy as sp
import mpmath as mp

mp.mp.dps = 50

J = sp.diag(1, 1, -1)
V = sp.Matrix([
    [1, 1, 1],
    [1,-1, 1],
    [1, 1,-1],
    [1,-1,-1],
]) / 2
assert sp.simplify(V.T*V - sp.eye(3)) == sp.zeros(3)

t = sp.symbols('t')
F = sp.simplify((sp.Integer(19) + 2*t - 13*t**2)/8)
assert sp.simplify((F-1) + (t-1)*(13*t+11)/8) == 0
assert sp.simplify(F.subs(t, sp.Rational(1,5))) == sp.Rational(59,25)
coeff = sp.simplify(sp.Rational(3,80)*sp.Rational(1,4)*(1 + sp.Rational(59,25)))
assert coeff == sp.Rational(63,2000)
extra = sp.simplify(coeff - sp.Rational(3,160))
assert extra == sp.Rational(51,4000)

v1 = sp.Matrix([0,0,1])
v2 = sp.Matrix([2,0,1])/sp.sqrt(5)
base = sp.simplify(V*J*V.T)
base_expected = sp.Matrix([
 [sp.Rational(1,4),-sp.Rational(1,4),sp.Rational(3,4),sp.Rational(1,4)],
 [-sp.Rational(1,4),sp.Rational(1,4),sp.Rational(1,4),sp.Rational(3,4)],
 [sp.Rational(3,4),sp.Rational(1,4),sp.Rational(1,4),-sp.Rational(1,4)],
 [sp.Rational(1,4),sp.Rational(3,4),-sp.Rational(1,4),sp.Rational(1,4)],
])
assert base == base_expected

m1 = [sp.simplify((v1.T*J*V.row(i).T)[0]) for i in range(4)]
m2 = [sp.simplify((v2.T*J*V.row(i).T)[0]) for i in range(4)]
assert set(m1) == {-sp.Rational(1,2), sp.Rational(1,2)}
assert set(m2) == {sp.sqrt(5)/10, 3*sp.sqrt(5)/10}
assert sp.simplify((v1.T*J*v1)[0] + 1) == 0
assert sp.simplify((v2.T*J*v2)[0] - sp.Rational(3,5)) == 0
assert sp.simplify((v1.T*J*v2)[0] + 1/sp.sqrt(5)) == 0

q = sp.Rational(1,10)
Hnorm = sp.simplify(q/2*(1+1/sp.sqrt(5)))
diffuse_pert = sp.simplify(sp.Rational(3,2)*Hnorm)
macro_pert = sp.simplify(sp.sqrt(3)/2*Hnorm)
assert float(sp.N(diffuse_pert,30)) < 0.25
assert float(sp.N(macro_pert,30)) < float(sp.N(1/(2*sp.sqrt(5)),30))

U = sp.Matrix([
 [1,1,1],
 [1,-1,1],
 [1,1,-1],
 [1,-1,-1],
]) / sp.sqrt(3)
assert sp.simplify(sp.Rational(3,4)*U.T*U - sp.eye(3)) == sp.zeros(3)

n = sp.Matrix([1,2,4])/sp.sqrt(21)
B = sp.simplify(sp.eye(3)-2*n*n.T)
assert sp.simplify(B*B-sp.eye(3)) == sp.zeros(3)
assert B.eigenvals() == {sp.Integer(-1):1, sp.Integer(1):2}
VBVT = sp.simplify(V*B*V.T)
expected = sp.Matrix([
 [-sp.Rational(5,12),-sp.Rational(1,4),sp.Rational(5,12),sp.Rational(7,12)],
 [-sp.Rational(1,4),sp.Rational(15,28),-sp.Rational(5,28),sp.Rational(17,28)],
 [sp.Rational(5,12),-sp.Rational(5,28),sp.Rational(61,84),sp.Rational(11,84)],
 [sp.Rational(7,12),sp.Rational(17,28),sp.Rational(11,84),sp.Rational(13,84)],
])
assert VBVT == expected
assert all(x != 0 for x in list(VBVT))

C0 = 3*mp.sqrt(2)
C1 = 12*mp.e**(-mp.mpf('0.5'))/mp.sqrt(2*mp.pi)
Ebound = 1 - 4*mp.e**(-4)*(1-mp.e**(-mp.mpf('4.5')))
partner_bound = C1 + (C0-C1)*Ebound
assert partner_bound < mp.mpf('4.146')
assert partner_bound < C0

print('PASS_QFORM_B17_MULTIMACRO_SECONDORDER_RIGIDITY')
print('F(1/5) =', sp.Rational(59,25))
print('noncollinear q^2 coefficient =', sp.Rational(63,2000))
print('extra over two-collinear coefficient =', sp.Rational(51,4000))
print('Hnorm(q=1/10) =', sp.N(Hnorm,18))
print('diffuse entry perturb upper bound =', sp.N(diffuse_pert,18))
print('macro-diffuse perturb upper bound =', sp.N(macro_pert,18))
print('partner C0 =', mp.nstr(C0,30))
print('partner C1 =', mp.nstr(C1,30))
print('E exp factor upper =', mp.nstr(Ebound,30))
print('strict tetrahedral partner bound =', mp.nstr(partner_bound,30))
