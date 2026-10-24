import sympy as sp

lam, a, r, x = sp.symbols('lam a r x', positive=True)
M = sp.Matrix([[a,a,0],[a,a,r],[0,r,0]])
p = sp.factor(M.charpoly(lam).as_expr())
assert sp.expand(p - (lam**3 - 2*a*lam**2 - r**2*lam + a*r**2)) == 0

# Threshold comparison for a>1.
Tpos = (2*a-1)/(a-1)
Tneg = (2*a+1)/(a+1)
assert sp.simplify(Tpos-Tneg - 2*a/(a**2-1)) == 0

# Boundary minimization ar = sqrt(x)(x-1)/(x-2), x>2.
F = sp.sqrt(x)*(x-1)/(x-2)
num = sp.factor(sp.together(sp.diff(F,x)/F).as_numer_denom()[0])
assert sp.factor(num) == x**2 - 5*x + 2
xstar = (sp.Integer(5)+sp.sqrt(17))/2
astar = sp.simplify((xstar-1)/(xstar-2))
assert sp.simplify(astar - (sp.Integer(7)+sp.sqrt(17))/8) == 0
mustar2 = sp.simplify(xstar*astar**2)
assert sp.simplify(mustar2 - (sp.Integer(71)+17*sp.sqrt(17))/16) == 0
mustar = sp.sqrt(mustar2)
Cstar = sp.simplify(2**sp.Rational(9,4)/sp.sqrt(mustar))

# Diffuse stress compression a=r=2.
Ms = sp.Matrix([[2,2,0],[2,2,2],[0,2,0]])
ps = sp.factor(Ms.charpoly(lam).as_expr())
assert ps == lam**3 - 4*lam**2 - 4*lam + 8
roots = sorted([float(sp.re(z)) for z in sp.nroots(ps)])
assert roots[0] < -1 and 1 < roots[1] < 2 and roots[2] > 4

print('charpoly =', p)
print('x* =', sp.N(xstar, 16))
print('a* =', sp.N(astar, 16))
print('mu* =', sp.N(mustar, 16))
print('C* =', sp.N(Cstar, 16))
print('stress roots =', roots)
print('stress bound =', float(2**sp.Rational(5,4)))
