import sympy as sp

p, theta, rho = sp.symbols("p theta rho", positive=True)
q = 1-p
a = sp.Integer(1)
d = theta/p
b = 1+d
m = sp.simplify(p*a + q*b)
lam = sp.simplify(rho/m)
h = 1/p
c = sp.simplify(b-h)
EX2 = sp.simplify(p*a**2 + q*b**2)
den_y = 1-lam*a

T_MS_short = sp.simplify(a + lam*a**2/(2*den_y))
T_G_short = sp.simplify(a + lam*(a**2+q*h**2)/(2*den_y))
common = sp.simplify(lam*EX2/(2*(1-rho)*den_y))
T_MS_long = sp.simplify(common + b/den_y)
T_G_long = sp.simplify(common + c/den_y + h)

T_MS = sp.simplify(p*T_MS_short + q*T_MS_long)
T_G = sp.simplify(p*T_G_short + q*T_G_long)
D = sp.factor(T_MS-T_G)
assert sp.simplify(D - q*rho/(2*(p*(1-rho)+q*theta))) == 0

R = sp.factor(T_MS/T_G)
N = sp.factor(sp.fraction(T_G)[0])
H = p**2*rho - p*rho*theta + p*rho + 2*p*theta - 2*p + rho*theta - 2*theta
dR = sp.factor(sp.diff(R, theta))
expected_dR = sp.factor(-2*p*rho*(p-1)**2*(rho-1)*H/N**2)
assert sp.simplify(dR-expected_dR) == 0
assert sp.factor(H - (p*(rho*(p+1)-2) - (1-p)*(2-rho)*theta)) == 0
assert sp.factor(H.subs(theta,1) - (rho*(1+p**2)-2)) == 0

delta1 = sp.factor(R.subs(theta,1)-1)
expected_delta1 = sp.factor(p*rho*(1-p)*(1-rho)/((1-p*rho)*(2-rho*(p**2-p+1))))
assert sp.simplify(delta1-expected_delta1) == 0

F = p**4*rho**2 - 2*p**3*rho**2 + 2*p**2*rho + 2*p*rho - 4*p - rho + 2
G = p**3*rho**2 - 2*p**2*rho**2 - rho**2 + 4*rho - 2
dp = sp.factor(sp.diff(delta1,p))
dr = sp.factor(sp.diff(delta1,rho))
assert sp.factor(dp - (-rho*(rho-1)*F/((p*rho-1)**2*(p**2*rho-p*rho+rho-2)**2))) == 0
assert sp.factor(dr - (p*(p-1)*G/((p*rho-1)**2*(p**2*rho-p*rho+rho-2)**2))) == 0
assert sp.factor(F-p*G-(p*rho-1)*(2*p+rho-2)) == 0

Q = 2*p**5-8*p**4+10*p**3-6*p**2+1
assert sp.factor(G.subs(rho,2*(1-p)) - 2*Q) == 0
assert sp.factor(sp.diff(Q,p) - 2*p*(p-2)*(5*p**2-6*p+3)) == 0
assert sp.simplify(Q.subs(p,sp.Rational(1,2))-sp.Rational(5,16)) == 0
assert sp.simplify(Q.subs(p,1)+1) == 0

delta_crit = sp.factor(delta1.subs(rho,2*(1-p)))
expected_delta_crit = sp.factor((p-1)**2*(2*p-1)/((p**2-2*p+2)*(2*p**2-2*p+1)))
assert sp.simplify(delta_crit-expected_delta_crit) == 0

root = sp.nroots(Q, n=60, maxsteps=200)
realroots = [z for z in root if abs(sp.im(z)) < sp.Float('1e-50') and 0 < sp.re(z) < 1]
assert len(realroots)==1
pstar = sp.N(sp.re(realroots[0]),50)
rstar = sp.N(2*(1-pstar),50)
Cstar = sp.N(1+expected_delta_crit.subs(p,pstar),50)

print("ALL_SYMBOLIC_CHECKS_PASS")
print("D =", D)
print("dR/dtheta factor verified")
print("delta_boundary =", expected_delta1)
print("Q(1/2) =", Q.subs(p,sp.Rational(1,2)), "Q(1) =", Q.subs(p,1))
print("p_star =", pstar)
print("rho_star =", rstar)
print("C2 =", Cstar)
