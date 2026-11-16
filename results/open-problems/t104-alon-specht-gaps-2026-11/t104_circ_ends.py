import sympy as sp
n, l = sp.symbols('n lam', positive=True)
K = 8*l/(n-2) - 32/(n*(n-2)) + 4*(1-l)*(n-4)/(n-2)**2
E = K/2 - 8*l/n
for name, val in (("2/(n-1)", 2/(n-1)), ("4/n", 4/n)):
    e = sp.factor(sp.together(E.subs(l, val)))
    num, den = sp.fraction(e)
    print(name, " E =", e)
    print("   numerator expanded:", sp.expand(num), "  real roots:", [r.evalf(6) for r in sp.real_roots(sp.Poly(sp.expand(num), n))])
