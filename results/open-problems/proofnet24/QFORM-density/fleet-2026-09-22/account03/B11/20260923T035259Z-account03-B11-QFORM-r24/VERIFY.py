import sympy as sp
from sympy import Matrix

a,b1,b2,c11,c12,c22=sp.symbols('a b1 b2 c11 c12 c22', nonzero=True)
H=Matrix([[a,b1,b2],[b1,c11,c12],[b2,c12,c22]])
b=Matrix([b1,b2]); C=Matrix([[c11,c12],[c12,c22]])
K=b*b.T-a*C
assert sp.simplify(K.det()-a*H.det())==0

O=Matrix([[1,2,2],[2,1,-2],[-2,2,-1]])/3
assert sp.simplify(O.T*O-sp.eye(3))==sp.zeros(3)
Lam=sp.diag(-3,1,2)
Hex=sp.simplify(O*Lam*O.T)
Hexpected=Matrix([[1,-sp.Rational(4,3),sp.Rational(2,3)],[-sp.Rational(4,3),-sp.Rational(1,3),2],[sp.Rational(2,3),2,-sp.Rational(2,3)]])
assert Hex==Hexpected
assert sp.factor(Hex.det())==-6
assert Hex[2,2]*Hex.det()==4
assert Hex.charpoly().as_expr().factor()==(sp.Symbol('lambda')-2)*(sp.Symbol('lambda')-1)*(sp.Symbol('lambda')+3)
example_bound=sp.simplify(2*sp.sqrt(sp.pi)*4**(-sp.Rational(1,4)))
assert sp.simplify(example_bound-sp.sqrt(2*sp.pi))==0

C0=Matrix([[1,1,1],[1,1,-1],[1,-1,1]])
assert C0.det()==-4
assert C0.eigenvals()=={-1:1,2:2}

print('det(K)=a det(H):', sp.factor(K.det()))
print('rotated example H=')
print(Hex)
print('rotated example det=', Hex.det(), ' minority product=', Hex[2,2]*Hex.det())
print('rotated example eigenvalues=', Hex.eigenvals())
print('rotated example theorem bound=', sp.N(example_bound,15))
print('partner C0 det/eigenvalues=', C0.det(), C0.eigenvals())
print('QFORM_B11_R24_MINORITY_DISCRIMINANT_CHECK_PASS')
