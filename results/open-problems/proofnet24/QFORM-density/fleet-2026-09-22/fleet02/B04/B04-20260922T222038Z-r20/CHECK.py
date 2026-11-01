import math
import sympy as sp

lam, d = sp.symbols('lambda d', real=True)
K = sp.Matrix([[2, 2, -2], [2, 2+d, 2], [-2, 2, 2]])
print('charpoly =', sp.factor(K.charpoly(lam).as_expr()))
Kd1 = K.subs(d, 1)
print('d1 exact eigenvalues =', sorted([str(x) for x in Kd1.eigenvals().keys()]))
print('d1 numeric eigenvalues =', sorted([float(sp.N(x, 16)) for x in Kd1.eigenvals().keys()]))
print('d1 negative magnitude =', (math.sqrt(41)-3)/2)
H6 = 10.6187196675779193598881105947637
print('partner d0 three-bank bound =', 2*H6/math.sqrt(8))
print('new d1 three-bank bound =', 16*math.sqrt(2)/math.sqrt(8))
A = sp.Matrix([[1,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,-1]])
print('two-sided counterexample charpoly =', sp.factor(A.charpoly(lam).as_expr()))
print('two-sided counterexample eigenvalues =', sorted([float(x) for x in A.eigenvals().keys()]))
print('target-family direct grouped bound =', math.pi)
