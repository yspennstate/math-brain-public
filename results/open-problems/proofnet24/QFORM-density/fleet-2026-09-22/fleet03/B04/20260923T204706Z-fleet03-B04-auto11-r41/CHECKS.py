import sympy as sp

lam=sp.symbols('lam')
A=sp.Matrix([[0,2,1],[2,1,3],[1,3,-1]])
assert A.det()==15
chi=sp.expand(A.charpoly(lam).as_expr())
assert chi==lam**3-15*lam-15
signs={x:int(sp.sign(chi.subs(lam,x))) for x in [5,4,-4,-3,-2,-1]}
assert signs=={5:1,4:-1,-4:-1,-3:1,-2:1,-1:-1}

c,r,d,b,e=sp.symbols('c r d b e', nonzero=True)
B=sp.Matrix([[0,c,r],[c,d,b],[r,b,e]])
D=sp.expand(B.det())
assert sp.expand(D-(2*b*c*r-c**2*e-d*r**2))==0
kappa=d-2*b*c/r+e*c**2/r**2
assert sp.simplify(kappa+D/r**2)==0

DD=sp.symbols('DD', positive=True)
R=2**sp.Rational(-5,3)*DD**sp.Rational(1,3)
expr=4*sp.sqrt(2)*DD**sp.Rational(-1,2)*sp.sqrt(R)+sp.Rational(1,2)/R
target=3*2**sp.Rational(2,3)*DD**sp.Rational(-1,3)
assert sp.simplify(expr-target)==0

bu1,bu2,bv1,bv2,pu1,pu2,pv1,pv2=sp.symbols('bu1 bu2 bv1 bv2 pu1 pu2 pv1 pv2')
e11,e12,e21,e22=sp.symbols('e11 e12 e21 e22')
BU=sp.Matrix([bu1,bu2]); BV=sp.Matrix([bv1,bv2])
PU=sp.Matrix([pu1,pu2]); PV=sp.Matrix([pv1,pv2])
E=sp.Matrix([[e11,e12],[e21,e22]])
C=BU*PV.T+PU*BV.T+E
M=sp.Matrix([[0,bv1,bv2],[bu1,C[0,0],C[0,1]],[bu2,C[1,0],C[1,1]]])
ME=sp.Matrix([[0,bv1,bv2],[bu1,e11,e12],[bu2,e21,e22]])
assert sp.simplify(M.det()-ME.det())==0

print('det_A_star=', A.det())
print('charpoly=', chi)
print('signs=', signs)
print('new_constant=', float(3*2**sp.Rational(2,3)*15**sp.Rational(-1,3)))
print('peer_scalar_pivot_constant=', float(128*15**sp.Rational(-1,4)))
print('symbolic_det_identity=', D)
print('optimizer_verified=True')
print('star_minor_invariance_verified=True')
