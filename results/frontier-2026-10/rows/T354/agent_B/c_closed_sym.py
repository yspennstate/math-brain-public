# Symbolic form of c(s) from c_closed.py, with r1 = z2/V^2 and r2 = E[bZ^2]/(B2 B3) kept general; small- and large-s expansions.
import sympy as sp
s, t, r1, r2 = sp.symbols('s t r1 r2', positive=True)
E = sp.exp(-t); q = sp.tanh(s/2)
av = lambda f: sp.simplify(sp.integrate(sp.expand(f), (t, 0, s)) / s)
k = 1 - (1 - E)/s
Qn = sp.Rational(1, 2) - (1 - E)**2/s - E**2*q/s
cbf = 1 - 2*(1 - E)/s - (1 - E**2)/(2*s) + 2*(1 - E)**2/s**2
K = av(k); Qb = av(Qn); cb = av(cbf); kQ = av(k*Qn)
c = K - sp.Rational(3, 8)*r1*Qb - sp.Rational(3, 4)*r2*cb/K + sp.Rational(15, 8)*r1*kQ/K
print("K  =", sp.simplify(K)); print("Qb =", sp.simplify(Qb)); print("cb =", sp.simplify(cb)); print("kQ =", sp.simplify(kQ))
c0 = sp.limit(c, s, 0); print("c(0+) =", sp.simplify(c0))
ainf = sp.limit((1 - c.subs(r2, r1))*s, s, sp.oo); print("two-valued (r2 = r1): lim (1-c) s =", sp.simplify(ainf))
cinf = sp.limit(c, s, sp.oo); print("c(oo) =", sp.simplify(cinf))
print("check s=5, r1=r2=64/9:", sp.N(c.subs({s: 5, r1: sp.Rational(64, 9), r2: sp.Rational(64, 9)})))
