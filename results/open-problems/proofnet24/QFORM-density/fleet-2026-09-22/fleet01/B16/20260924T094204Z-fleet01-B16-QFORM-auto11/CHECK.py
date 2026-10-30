import sympy as sp

la=sp.symbols('la')
a,b,c,d=sp.symbols('a b c d')
B=sp.Matrix([[a,c,0],[c,d,b],[0,b,0]])
print('symbolic_det=', sp.factor(B.det()))

Bstar=sp.Matrix([[2,1,0],[1,1,2],[0,2,0]])
print('Bstar_det=', Bstar.det())
p=sp.expand(Bstar.charpoly(la).as_expr())
print('Bstar_charpoly=', p)
for x in (-2,-1,1,2,3,4):
    print(f'p({x})=', sp.expand(p).subs(la,x))
print('eigs_numeric=', [sp.N(e,16) for e in Bstar.eigenvals().keys()])
print('partner_eigs=', sp.Matrix([[2,0,0],[0,0,2],[0,2,0]]).eigenvals())

Cabs=3*2**(2/3)
Cproj=6*2**(2/3)
print('abstract_constant=', repr(Cabs))
print('projection_constant=', repr(Cproj))
print('Bstar_bound=', repr(Cproj/(8**(1/3))))
print('partner_old_bound=', repr(6*(2*(2**0.5))**(2/3)/(8**(1/3))))

assert sp.factor(B.det()+a*b*b)==0
assert [sp.expand(p).subs(la,x) for x in (-2,-1,1,2,3,4)] == [-6,7,3,-2,-1,12]
assert abs(Cproj/(8**(1/3))-Cabs)<1e-12
print('STATUS=PASS')
