import sympy as sp

m=sp.symbols('m', positive=True)
eps=m**(-sp.Rational(2,3))
a=m**(-sp.Rational(1,12))
D=m**sp.Rational(1,4)

O=sp.Matrix([[6,-2,-3],[-2,3,-6],[-3,-6,-2]])/7
J=sp.diag(1,1,-1)
B=sp.simplify(O.T*J*O)
assert sp.simplify(O.T*O-sp.eye(3))==sp.zeros(3)
assert sp.factor(B.charpoly().as_expr())==(sp.Symbol('lambda')-1)**2*(sp.Symbol('lambda')+1)
assert all(x != 0 for x in B)

v=sp.simplify((1-eps)/12 + eps*D**2 + eps**3/48)
assert sp.simplify(v-(sp.Rational(1,12)+m**(-sp.Rational(1,6))-sp.Rational(1,12)*m**(-sp.Rational(2,3))+sp.Rational(1,48)*m**-2))==0
assert sp.limit(v,m,sp.oo)==sp.Rational(1,12)

E4=sp.simplify((1-eps)/80 + eps*D**4 + eps**3*D**2/8 + eps**5/1280)
assert sp.limit(E4/m**sp.Rational(1,3),m,sp.oo)==1
assert sp.limit(D,m,sp.oo)==sp.oo
assert sp.limit(D/sp.sqrt(m),m,sp.oo)==0
assert sp.simplify(m*eps)==m**sp.Rational(1,3)

gaussian_tip=sp.simplify(1/(2*sp.sqrt(2)*sp.Rational(1,12)))
assert gaussian_tip==3*sp.sqrt(2)

print('QFORM_B17_GROWING_FRAGMENT_SATURATION_CHECK_PASS')
print('B =')
print(B)
print('charpoly(B) =', sp.factor(B.charpoly().as_expr()))
print('variance =', v, '; limit =', sp.limit(v,m,sp.oo))
print('fourth moment =', E4)
print('E4 / m^(1/3) ->', sp.limit(E4/m**sp.Rational(1,3),m,sp.oo))
print('remote center D_m =', D, '; D_m/sqrt(m) =', sp.simplify(D/sp.sqrt(m)))
print('activity m eps_m =', sp.simplify(m*eps))
print('Gaussian cone-tip constant =', gaussian_tip, '=', sp.N(gaussian_tip,16))
