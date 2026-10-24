# m=2 exact: f(x)= a x^2 + 2 b x(1-x) + c (1-x)^2  (convention of eq. (4): ordered pairs).
# Local criterion f'(p) = -1 at the fixed point p.  Take a=al, c=1-al, and optimise over b.
import sympy as sp
al,b,x=sp.symbols('alpha b x', positive=True)
a=al; c=1-al
f=a*x**2+2*b*x*(1-x)+c*(1-x)**2
fp=sp.diff(f,x)
# conditions: f(p)=p, f'(p)=-1 ; eliminate p
res=sp.resultant(sp.expand(f-x), sp.expand(fp+1), x)
res=sp.factor(res)
print("resultant in (alpha,b):",res)
# For each alpha, the set of b with f'(p)=-1; the threshold alpha is where the discriminant in b vanishes
# or where b hits the boundary b=alpha or b=1-alpha.
for bb in [al,1-al,(1-al)/2, sp.Rational(1,2)]:
    sols=sp.solve(sp.expand(res.subs(b,bb)),al)
    print("b=",bb,"->",[sp.nsimplify(s) for s in sols],[sp.N(s) for s in sols])
disc=sp.discriminant(sp.expand(res),b)
print("disc in b:",sp.factor(disc))
print("roots:",[ (s,sp.N(s)) for s in sp.solve(disc,al)])
