import sympy as sp

# Exact certificate for Q_* = one-way 3-cycle with rates (a,b,c)=(10,1,1).
Q = sp.Matrix([[-10,10,0],[0,-1,1],[1,0,-1]])
lam = sp.symbols('lam')
char = sp.expand(Q.charpoly(lam).as_expr())
assert char == sp.expand(lam*(lam**2 + 12*lam + 21)), char

sqrt15 = sp.sqrt(15)
mu1 = 6 - sqrt15
mu2 = 6 + sqrt15
assert sp.expand(mu1 + mu2) == 12
assert sp.expand(mu1 * mu2) == 21

pi = sp.Matrix([[sp.Rational(1,21), sp.Rational(10,21), sp.Rational(10,21)]])
assert pi*Q == sp.zeros(1,3)
assert sum(pi) == 1

h = sp.Matrix([0,1,1])
mean = (pi*h)[0]
# Var_pi(h) = E h - (E h)^2 because h is {0,1}-valued.
V = sp.simplify(mean - mean**2)
# derivative of stationary covariance at 0: E[h(X0) (Qh)(X0)]
Qh = Q*h
Cp0 = sp.simplify((pi * sp.diag(*list(h)) * Qh)[0])
assert mean == sp.Rational(20,21)
assert V == sp.Rational(20,441)
assert Cp0 == -sp.Rational(10,21)

# C(t)=A e^{-mu1 t}+B e^{-mu2 t}; solve C(0)=V, C'(0)=Cp0.
A, B = sp.symbols('A B')
sol = sp.solve([sp.Eq(A+B,V), sp.Eq(-mu1*A-mu2*B,Cp0)],[A,B], dict=True)[0]
Aex = sp.simplify(sol[A]); Bex = sp.simplify(sol[B])
assert sp.simplify(Aex - (10-3*sqrt15)/441) == 0
assert sp.simplify(Bex - (10+3*sqrt15)/441) == 0
# Exact sign checks: (3 sqrt15)^2 =135 >100=10^2.
assert 135 > 100
assert Aex.is_negative is True
assert Bex.is_positive is True

# Turning time where C'(t) changes sign; ratio is >1 so t_* >0.
ratio = sp.simplify(mu2*Bex / (-mu1*Aex))
assert sp.simplify(ratio - (31+8*sqrt15)) == 0
# Verify ratio >1 exactly.
assert 31 > 1

# General one-way cycle algebra used in report.
a,b,c,s,S,D = sp.symbols('a b c s S D', positive=True)
s_expr = a+b+c
S_expr = a*b+b*c+c*a
Delta = sp.expand(s_expr**2 - 4*S_expr)
# Stationary weights pi proportional to (bc, ca, ab).
p1,p2,p3 = b*c/S_expr, c*a/S_expr, a*b/S_expr
assert sp.simplify(p1+p2+p3-1)==0
# Upper-tail h2=1_{>=2}, h3=1_{>=3}; C_rs(0) and derivative at zero.
h2 = sp.Matrix([0,1,1]); h3 = sp.Matrix([0,0,1])
Qg = sp.Matrix([[-a,a,0],[0,-b,b],[c,0,-c]])
pig = sp.Matrix([[p1,p2,p3]])

def cov0(x,y):
    ex=(pig*x)[0]; ey=(pig*y)[0]
    exy=(pig*sp.diag(*list(x))*y)[0]
    return sp.factor(exy-ex*ey)

def covp0(x,y):
    return sp.factor((pig*sp.diag(*list(x))*(Qg*y))[0])

C22=sp.factor(cov0(h2,h2)); C23=sp.factor(cov0(h2,h3)); C32=sp.factor(cov0(h3,h2)); C33=sp.factor(cov0(h3,h3))
D22=sp.factor(covp0(h2,h2)); D23=sp.factor(covp0(h2,h3)); D32=sp.factor(covp0(h3,h2)); D33=sp.factor(covp0(h3,h3))
assert sp.simplify(C22 - a*b*c*(b+c)/S_expr**2)==0
assert sp.simplify(C23 - a*b**2*c/S_expr**2)==0
assert sp.simplify(C32 - a*b**2*c/S_expr**2)==0
assert sp.simplify(C33 - a*b*c*(a+b)/S_expr**2)==0
assert sp.simplify(D22 + a*b*c/S_expr)==0
assert D23==0
assert sp.simplify(D32 + a*b*c/S_expr)==0
assert sp.simplify(D33 + a*b*c/S_expr)==0

# For two exponential modes mu1<mu2, A=(D(0)+mu2*C(0))/(mu2-mu1).
m1,m2=sp.symbols('m1 m2', positive=True)
A22_num=sp.factor(D22+m2*C22)
A23_num=sp.factor(D23+m2*C23)
A32_num=sp.factor(D32+m2*C32)
A33_num=sp.factor(D33+m2*C33)
# Remove common positive abc/S^2 factors; verify the claimed brackets.
assert sp.simplify(A22_num / (a*b*c/S_expr**2) - (m2*(b+c)-S_expr))==0
assert sp.simplify(A23_num / (a*b*c/S_expr**2) - (m2*b))==0
assert sp.simplify(A32_num / (a*b*c/S_expr**2) - (m2*b-S_expr))==0
assert sp.simplify(A33_num / (a*b*c/S_expr**2) - (m2*(a+b)-S_expr))==0

print('charpoly_Qstar =', char)
print('mu1 =', mu1)
print('mu2 =', mu2)
print('pi =', tuple(pi))
print('mean_h =', mean)
print('C(0) =', V)
print("C'(0) =", Cp0)
print('A_slow =', Aex)
print('B_fast =', Bex)
print('turning_ratio =', ratio)
print('general_C0 =', C22, C23, C32, C33)
print('general_Cprime0 =', D22, D23, D32, D33)
print('general_slow_numerators =', A22_num, A23_num, A32_num, A33_num)
print('ALL_EXACT_CHECKS_PASS')
