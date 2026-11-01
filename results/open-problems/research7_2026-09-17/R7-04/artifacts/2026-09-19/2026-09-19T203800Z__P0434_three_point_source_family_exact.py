import sympy as sp
from math import comb

# Exact self-check for the R7-04 P0434 three-point/source-family run.
# No floating-point arithmetic is used in the proof certificate.

d,e,x,t = sp.symbols("d e x t", positive=True)
lam = (1-e)/(1+d**2)

p = 1-d
q = d*(1-d)
r = d**2
a = 1-d
b = sp.Integer(1)
c = 1+1/d
m = 1+d**2
mu1 = 1-d+d**2
nu1 = 1-2*d+3*d**2-d**3
nuinf = 2+3*d**2-d**3
r0 = sp.factor(mu1/(1-d**2))

A = sp.factor(1-lam*a)
B = sp.factor(1-lam*mu1)
C = sp.factor(1-lam*m)
assert sp.simplify(C-e) == 0

# Exact M-SERPT conditional and mean response times.
TMS_a = a + lam*a**2/(2*A)
TMS_b = 1/A + lam*nu1/(2*A*B)
TMS_c = c/B + lam*nuinf/(2*B*C)
EMS = sp.factor(p*TMS_a + q*TMS_b + r*TMS_c)

# Exact Gittins conditional and mean response times.
# For the short/medium tagged jobs at worst rank r0:
# X_new=0, X_old,0=min(X,1), X_old,1=r0*1_{X=c}.
Wsm = lam*(nu1 + d**2*r0**2)/(2*B)
TG_a = a + Wsm
TG_b = 1 + Wsm

# For the long tagged job at worst rank 1/d:
# X_new=min(X,1), X_old,0=X, no recycling.
Wlong = lam*nuinf/(2*B*C)
Rlong = (c-r0)/B + r0
TG_c = Wlong + Rlong
EG = sp.factor(p*TG_a + q*TG_b + r*TG_c)

# Numerator for 2 E[T_G] - E[T_MS] after rho=1-e.
P = (
 d**9 - 2*d**8 - 4*d**7 + d**5 + 2*d**4 + 2*d**3
 + e**3*(-2*d**8 + 5*d**7 - 14*d**5 + 17*d**4 - 7*d**3 + 2*d**2 - 2*d + 1)
 + e**2*(d**9 + 5*d**8 - 18*d**7 + 12*d**6 + 23*d**5 - 28*d**4 + 12*d**3 - 6*d**2 + 2*d + 1)
 + e*(-2*d**9 - 3*d**8 + 17*d**7 - 16*d**6 - 10*d**5 + 9*d**4 - 7*d**3 + 8*d**2)
)
F1 = d**2+d+e*(1-d)
F2 = d+e*(1-d+d**2)
D = 2*e*(1-d**2)*F1*F2
assert sp.cancel(2*EG-EMS-P/D) == 0

# The first source-family Gittins switch is exactly age 1-2d.
age = sp.symbols("age")
A1 = (a-age)/p
A2 = ((a-age)+d*d)/(1-d**2)
assert sp.solve(sp.together(A1-A2), age) == [1-2*d]

# Exact Bernstein certificate for P>=0 on 0<=d<=1/2, 0<=e<=1.
# Put u=2d.  In the tensor-product Bernstein basis of bidegree (9,3),
# every coefficient is nonnegative.
u = sp.symbols("u")
Q = sp.Poly(sp.expand(P.subs(d,u/2)),u,e)
n = Q.degree(u)
mdeg = Q.degree(e)
acoef = {mon:coef for mon,coef in Q.terms()}
Bcoef = {}
for i in range(n+1):
    for j in range(mdeg+1):
        s = sp.Rational(0)
        for k in range(i+1):
            for ell in range(j+1):
                aa = acoef.get((k,ell),0)
                if aa:
                    s += aa*sp.Rational(comb(i,k),comb(n,k))*sp.Rational(comb(j,ell),comb(mdeg,ell))
        Bcoef[(i,j)] = sp.factor(s)
assert all(v >= 0 for v in Bcoef.values())
assert any(v > 0 for v in Bcoef.values())

# Exact asymptotic along the source path e=d^(3/2): put d=t^2,e=t^3.
R = sp.cancel(EMS/EG)
series = sp.series(R.subs({d:t**2,e:t**3}),t,0,6)

print("degrees",n,mdeg)
for i in range(n+1):
    print(i,[str(Bcoef[(i,j)]) for j in range(mdeg+1)])
print("series",series)
print("ALL_EXACT_CHECKS_PASS")
