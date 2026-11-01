# E0065: reproduce lambda_2 = (3-sqrt7)/2 as sup over NON-REGULAR QSOs on S^1 of min_{ijk} P_{ij,k}
import sympy as sp

A,B,C,x,t = sp.symbols('A B C x t', real=True)
f = A*x**2 + 2*B*x*(1-x) + C*(1-x)**2
f = sp.expand(f)
print("f(x) =", f)
fp = sp.diff(f,x)
print("f'(x) =", sp.expand(fp))

# Claim 1: for 0<C and A<1 there is exactly one fixed point in (0,1)
g = sp.expand(f - x)
print("g(0)=",g.subs(x,0), " g(1)=", sp.simplify(g.subs(x,1)))
