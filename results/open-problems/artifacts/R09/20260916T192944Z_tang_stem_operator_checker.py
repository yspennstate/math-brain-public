from fractions import Fraction as F
import sympy as sp

p,t = sp.symbols('p t', positive=True)

# 1. Exact transitive test graph: Cayley graph of C3 * C3 with standard symmetric generators.
# One entered triangle has offspring X in {0,1,2}.
a = (1-p)**2
b = 2*p*(1-p)**2
c = p**2*(3-2*p)
assert sp.expand(a+b+c-1) == 0

phi = sp.expand(a + b*t + c*t**2)
assert sp.factor(phi-t) == sp.factor((t-1)*(c*t-a))

# Mean and critical equation.
mu = sp.expand(sp.diff(phi,t).subs(t,1))
h = sp.expand(c-a)
assert sp.expand(mu-1-h) == 0
# h' > 0 on (0,1): h' = 2(1-p)(3p+1)
assert sp.simplify(sp.diff(h,p)-2*(1-p)*(3*p+1)) == 0
assert h.subs(p,F(2,5)) < 0
assert h.subs(p,F(41,100)) > 0

# For p>pc, physical extinction root q=a/c.
q = sp.factor(a/c)
theta = sp.factor(1-q**2)
theta2 = sp.factor(sp.diff(theta,p,2))
R = 2*p**4 - 12*p**3 + 30*p**2 - 34*p + 15
target = sp.factor(-12*(1-p)**2*R/(p**6*(3-2*p)**4))
assert sp.simplify(theta2-target) == 0

# Positive Bernstein representation of R on [0,1].
bern = 15*(1-p)**4 + 26*p*(1-p)**3 + 18*p**2*(1-p)**2 + 6*p**3*(1-p) + p**4
assert sp.expand(bern-R) == 0

# 2. Stem operator identity.
k = sp.symbols('k', integer=True, positive=True)
f = sp.Function('f')
expr = sp.diff(p**k*f(p),p,2)
expected = p**(k-2)*(k*(k-1)*f(p) + 2*k*p*sp.diff(f(p),p) + p**2*sp.diff(f(p),p,2))
assert sp.simplify(expr-expected) == 0

# 3. Concrete source witness recovered from prior run: binary tail plus 3-edge stem.
beta = sp.factor((2*p-1)/p**2)
theta3 = sp.factor(p**3*beta)
assert sp.expand(theta3-(2*p**2-p)) == 0
assert sp.diff(theta3,p,2) == 4

print("R09 Tang Q4.11 checker")
print("triangle-block offspring pgf =", phi)
print("critical equation h(p)=c-a =", sp.factor(h))
print("pc bracket: 2/5 < pc < 41/100")
print("theta_C3*C3(p) =", theta)
print("theta'' =", theta2)
print("R Bernstein form =", sp.expand(bern))
print("all Bernstein coefficients positive: 15, 13/2, 3, 3/2, 1")
print("=> theta''<0 on (pc,1) for this transitive Cayley graph")
print("stem operator second derivative identity =", expected)
print("T3 theta'' =", sp.diff(theta3,p,2))
print("PASS")
