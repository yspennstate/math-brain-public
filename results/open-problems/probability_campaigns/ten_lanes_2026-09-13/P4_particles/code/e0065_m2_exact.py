import sympy as sp
A,B,C,x,lam = sp.symbols('A B C x lambda', real=True)
a = A-2*B+C; b = 2*B-2*C
f = sp.expand(a*x**2 + b*x + C)
fq = sp.expand(A*x**2+2*B*x*(1-x)+C*(1-x)**2)
print("CHECK f == QSO form:", sp.simplify(f-fq)==0)

# --- 1. H identity: f'(p) >= -1  <=>  H >= 0, H = 4AC-4B^2+4B-4C+3
H = 4*A*C-4*B**2+4*B-4*C+3
# derivation check: g(x0) * (3-b)^2 / C  should equal H  with x0 = 2C/(3-b)
g = sp.expand(f-x)
x0 = 2*C/(3-b)
expr = sp.simplify(sp.expand(g.subs(x,x0)*(3-b)**2/C))
print("CHECK g(x0)(3-b)^2/C == H :", sp.simplify(sp.expand(expr - H))==0, " expr=",sp.factor(sp.expand(expr)))

# --- 2. exact 2-cycle criterion: Q(x) = (f(f(x))-x)/(f(x)-x)
f2 = sp.expand(f.subs(x,f))
Q = sp.simplify(sp.cancel(sp.expand(f2-x)/sp.expand(f-x)))
Q = sp.expand(Q)
print("Q =", sp.collect(Q,x))
qa = sp.expand(Q.coeff(x,2)); qb=sp.expand(Q.coeff(x,1)); qc=sp.expand(Q.coeff(x,0))
disc = sp.expand(qb**2-4*qa*qc)
print("disc(Q) factored:", sp.factor(disc))
