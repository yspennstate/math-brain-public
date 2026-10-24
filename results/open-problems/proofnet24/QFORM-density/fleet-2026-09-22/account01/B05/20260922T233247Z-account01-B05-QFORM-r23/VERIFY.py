import sympy as sp

# Rank-one scalar-pair determinant identity.
a,c,Cii,p,q=sp.symbols('a c Cii p q', nonzero=True)
d=c**2/a
T=sp.Matrix([[Cii,p,q],[p,a,c],[q,c,d]])
theta=q-c*p/a
assert sp.simplify(T.det()+a*theta**2)==0

# Constants in the two-regime bathtub optimization.
D=sp.Rational(2,9)
C1=36*(D/sp.E)**sp.Rational(1,3)
C2=8*sp.sqrt(2)*(sp.Rational(9,2))**sp.Rational(1,6)
print('det_identity=', sp.factor(T.det()))
print('C1=', sp.N(C1,16))
print('C2=', sp.N(C2,16))
assert float(C1)<16
assert float(C2)<16
print('QFORM_B05_RANK1_PAIR_CHECK_PASS')
