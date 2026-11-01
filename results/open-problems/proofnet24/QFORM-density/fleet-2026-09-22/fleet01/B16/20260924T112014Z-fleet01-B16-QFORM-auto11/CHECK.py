import sympy as sp

c11,c12,c22,e1,e2,c=sp.symbols('c11 c12 c22 e1 e2 c')
C=sp.Matrix([[c11,c12],[c12,c22]])
ell=sp.Matrix([e1,e2])
B=C.row_join(ell).col_join(sp.Matrix([[e1,e2,c]]))
K=ell*ell.T-c*C
assert sp.factor(K.det()-c*B.det()) == 0

Bstar=sp.diag(1,-1,1)
assert Bstar.det() == -1
assert sorted(Bstar.eigenvals().keys()) == [-1,1]

Bp=sp.Matrix([[-4,0,0],[0,4,4],[0,4,0]])
assert Bp.det() == 64
lam=sorted([sp.N(x) for x in Bp.eigenvals().keys()])
assert all(abs(float(x)) > 1 for x in lam)
partner=sp.simplify(6*(2*sp.sqrt(2))**(sp.Rational(2,3))*64**(-sp.Rational(1,3)))
assert sp.simplify(partner-3) == 0

print('detK-cdetB =', sp.factor(K.det()-c*B.det()))
print('Bstar spectrum =', Bstar.eigenvals())
print('Bp determinant =', Bp.det())
print('Bp eigenvalues =', Bp.eigenvals())
print('partner bound =', partner)
print('16sqrt30 =', sp.N(16*sp.sqrt(30), 14))
print('16sqrt60 =', sp.N(16*sp.sqrt(60), 14))
print('4sqrtpi =', sp.N(4*sp.sqrt(sp.pi), 14))
print('STATUS=PASS')
