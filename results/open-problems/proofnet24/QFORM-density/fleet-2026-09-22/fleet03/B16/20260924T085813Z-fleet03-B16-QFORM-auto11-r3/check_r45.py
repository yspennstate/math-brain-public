from fractions import Fraction
import sympy as sp

mu, lam = sp.symbols('mu lam')

# Strict target family from REPORT Section 6.
B0 = sp.Matrix([[1,0,1],[0,0,1],[1,1,0]])
B = 3*B0
p = sp.factor(B0.charpoly(mu).as_expr())
assert sp.expand(p - (mu**3 - mu**2 - 2*mu + 1)) == 0
assert p.subs(mu, -2) == -7
assert p.subs(mu, -1) == 1
assert p.subs(mu, sp.Rational(1,3)) == sp.Rational(7,27)
assert p.subs(mu, 1) == -1
assert p.subs(mu, 2) == 1
assert B.det() == -27

# Bound for a=b=3 and unit projection norms.
main_bound = sp.Rational(256,3)
assert main_bound < sp.Rational(85334,1000)

# Partner strict-target family from REPORT Section 7.
P = sp.Matrix([[-2,2,0],[2,2,0],[0,0,2]])
pc = sp.factor(P.charpoly(lam).as_expr())
assert sp.expand(pc - (lam-2)*(lam**2-8)) == 0
assert P.det() == -16
partner_eigs = sorted([sp.N(e, 20) for e in P.eigenvals().keys()], key=lambda z: float(sp.re(z)))

print('STATUS=PASS')
print('B0_charpoly=', p)
print('B_det=', B.det())
print('B_eigs_numeric=', [sp.N(e, 20) for e in B.eigenvals().keys()])
print('main_bound_256_over_3=', sp.N(main_bound, 20))
print('P_charpoly=', pc)
print('P_eigs=', partner_eigs)
print('partner_bound_pi=', sp.N(sp.pi, 20))
