import sympy as sp

lam,d = sp.symbols('lam d', positive=True)
S,Sp,nu = sp.symbols('S Sp nu', positive=True)

D = lam - 1 + S
u = S/((nu+1)*D)
uprime_manual = sp.diff(u, lam) + sp.diff(u, S)*Sp
T = S + (1-lam)*Sp
q = T/(S*D)
assert sp.simplify(uprime_manual/u + q) == 0

qmax = (d-1)/((d-lam)*(d-lam/d))
qmin = 1/(d+1-lam/(d+1))
F = sp.factor(d/lam - sp.Rational(1,4)*(qmax-qmin))

endpoint = sp.factor(F.subs(lam, d-sp.Rational(1,4)))
endpoint_expected = (32*d**4+12*d**3+8*d**2+7*d-1)/((2*d-1)**2*(4*d-1)*(4*d**2+4*d+5))
assert sp.simplify(endpoint-endpoint_expected) == 0

F2 = sp.factor(F.subs(d,2))
F2_expected = (576-490*lam+104*lam**2-5*lam**3)/(4*lam*(9-lam)*(4-lam)*(2-lam))
assert sp.simplify(F2-F2_expected)==0
P2 = 576-490*lam+104*lam**2-5*lam**3
assert sp.simplify(P2.subs(lam,sp.Rational(9,5))-sp.Rational(9,5))==0
P2p = sp.diff(P2,lam)
assert sp.simplify(P2p.subs(lam,sp.Rational(9,5)) + sp.Rational(821,5)) == 0
assert sp.simplify(sp.diff(P2p,lam) - (208-30*lam)) == 0

num, den = map(sp.factor, sp.fraction(F))
print("uprime_over_u_plus_q =", sp.simplify(uprime_manual/u+q))
print("F_d =", F)
print("F_endpoint =", endpoint)
print("F2 =", F2)
print("P2(9/5) =", sp.factor(P2.subs(lam,sp.Rational(9,5))))
print("P2prime(9/5) =", sp.factor(P2p.subs(lam,sp.Rational(9,5))))
print("F_numerator =", num)
print("F_denominator =", den)
for dv in range(2,8):
    poly = sp.Poly(num.subs(d,dv),lam)
    roots = [complex(r) for r in sp.nroots(poly, n=30, maxsteps=200)]
    good = [r.real for r in roots if abs(r.imag)<1e-20 and 1<r.real<dv]
    print("d",dv,"criterion_root", good[0] if good else None)
print("ALL_EXACT_ALGEBRA_CHECKS_PASS")
