import sympy as sp

lam = sp.symbols('lambda')
tau, c, d, e = sp.symbols('tau c d e', nonzero=True, real=True)
H = sp.Matrix([[0,tau,0],[tau,c,d],[0,d,e]])
print('det(H)=', sp.factor(H.det()))
print('H^{-1}=')
print(H.inv())

H0 = sp.Matrix([
    [0, sp.sqrt(sp.Rational(3,2)), 0],
    [sp.sqrt(sp.Rational(3,2)), sp.Rational(2,3), sp.sqrt(sp.Rational(7,18))],
    [0, sp.sqrt(sp.Rational(7,18)), sp.Rational(4,3)]
])
print('example charpoly=', sp.factor(H0.charpoly(lam).as_expr()))
print('example eigenvalues=', H0.eigenvals())
