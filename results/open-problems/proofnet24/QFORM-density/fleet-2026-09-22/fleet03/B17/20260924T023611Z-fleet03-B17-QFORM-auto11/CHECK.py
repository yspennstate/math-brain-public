from fractions import Fraction
import sympy as sp

m, ell, c = sp.symbols('m ell c', positive=True)
u = sp.Matrix([sp.Rational(10,51), sp.Rational(10,51), sp.Rational(49,51)])
B = sp.eye(3) - 2*u*u.T
assert sp.simplify((u.T*u)[0]) == 1
assert sp.simplify(B*B-sp.eye(3)) == sp.zeros(3)
assert all(B[i,j] != 0 for i in range(3) for j in range(3))

sum4 = sum(u[j]**4 for j in range(3))
coef = sp.factor((sp.Rational(177)-39*sum4)/640)
assert coef == sp.Rational(53990741,240540480)

S = sp.factor(ell**2 + (1-ell)**2/m)
S_vertex_gap = sp.factor(S - 1/(m+1))
assert S_vertex_gap == ((m+1)*ell-1)**2/(m*(m+1))

T = sp.factor(ell**3 + (1-ell)**3/m**2)
h = sp.symbols('h', positive=True)
S_meso = sp.expand(S.subs({m:1/h**2, ell:c*h}))
T_meso = sp.expand(T.subs({m:1/h**2, ell:c*h}))
assert sp.expand(S_meso - ((1+c**2)*h**2 - 2*c*h**3 + c**2*h**4)) == 0
assert sp.expand(T_meso - (c**3*h**3 + h**4 - 3*c*h**5 + 3*c**2*h**6 - c**3*h**7)) == 0

print('B_star =', B)
print('c(u_star) =', coef, float(coef))
print('S - 1/(m+1) =', S_vertex_gap)
print('S_mesoscopic =', S_meso)
print('T_mesoscopic =', T_meso)
print('aligned coefficient =', sp.Rational(69,320))
print('PASS QFORM_WEIGHTED_BANK_GLOBAL_TIP_RIGIDITY')
