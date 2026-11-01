"""Independent symbolic check of T084-C017 identities in arbitrary n, t, r (sympy, not FLINT)."""
import json
import sympy as sp

n, t, r, u, c, x = sp.symbols("n t r u c x")
h = (n - 2) * (n - 3)
delta = t * h
a = t - 2 * (n - 4) * t ** 2
b = -1 + (2 * n - 9) * t + n * (n - 4) * t ** 2
F = delta * r ** 2 - b * r - a
B = n ** 2 * t ** 2 + (2 * n + 1) * t - 1
phi = t - 2 * n * t ** 2 + B * r - n * (n - 1) * t * r ** 2
G = 2 * t ** 2 * sp.diff(F, t) + sp.diff(F, r) * phi
L = (n ** 3 * (n - 4) * t ** 4 + 2 * n * (n ** 2 - 4 * n - 6) * t ** 3
     + 3 * (n ** 2 - 9 * n + 3) * t ** 2 + 2 * (n ** 2 - 9 * n + 9) * t - (2 * n - 3))
C = 2 * n ** 2 * (n - 4) * t ** 3 + 3 * n * (n - 6) * t ** 2 + (2 * n ** 2 - 16 * n + 15) * t - (2 * n - 3)
A = n * (n - 4)
J = 2 * A ** 2 * t ** 3 - 6 * A * (n - 2) * t ** 2 + 6 * (n - 1) * (n - 3) * t - (2 * n - 3)
res = {}
z = lambda e: sp.expand(e) == 0
res["(1)"] = z(h * G - (F * (-2 * h * n * (n - 1) * t * r + 2 * h * t + 2 * h * B - n * (n - 1) * b) + 2 * (L * r - t * C)))
res["(2)"] = z(delta * t ** 2 * C ** 2 - b * t * L * C - a * L ** 2 + h ** 2 * t ** 5 * J)
# (3) via Vieta, symbolic
ell, c0 = 2 * L / h, -2 * t * C / h
prod = ell ** 2 * (-a / delta) + ell * c0 * (b / delta) + c0 ** 2
res["(3)"] = sp.simplify(prod + 4 * t ** 4 * J / h) == 0
res["(4)"] = z(sp.diff(J, t) - 6 * ((A * t - (n - 2)) ** 2 - 1))
res["J(ta)"] = sp.simplify(J.subs(t, (n - 3) / A) + (n - 6) / (n - 4)) == 0
res["J(tb)"] = sp.simplify(J.subs(t, (n - 1) / A) + (n - 2) / n) == 0
Dscr = b ** 2 + 4 * delta * a
res["(6)"] = z(Dscr - (1 + (18 - 4 * n) * t + (6 * n ** 2 - 48 * n + 105) * t ** 2
                       + (-4 * n ** 3 + 38 * n ** 2 - 136 * n + 192) * t ** 3 + n ** 2 * (n - 4) ** 2 * t ** 4))
Dc = Dscr.subs(n, c + 3)
p7 = sp.Poly(sp.expand(sp.cancel(c ** 4 * (1 + u) ** 4 * Dc.subs(t, u / (c * (1 + u))))), u)
want7 = [c ** 4, 6 * c ** 3, c ** 2 * (6 * c + 15), -2 * c * (c + 1) * (2 * c - 9), -3 * (c - 3) * (c + 1)]
res["(7)"] = [sp.expand(p7.coeff_monomial(u ** k) - w) == 0 for k, w in enumerate(want7)] + [p7.degree() == 4]
p8 = sp.Poly(sp.expand(c ** 4 * Dc.subs(t, (1 + u) / c)), u)
want8 = [-3 * (c - 3) * (c + 1), 2 * (2 * c ** 3 - 13 * c ** 2 + 3 * c + 18), 9 * (2 * c ** 3 - 5 * c ** 2 - 2 * c + 6),
         6 * (c - 1) * (3 * c ** 2 - c - 6), (c + 3) ** 2 * (c - 1) ** 2]
res["(8)"] = [sp.expand(p8.coeff_monomial(u ** k) - w) == 0 for k, w in enumerate(want8)] + [p8.degree() == 4]
res["x-sub"] = [z((2 * c ** 3 - 5 * c ** 2 - 2 * c + 6).subs(c, x + 4) - (2 * x ** 3 + 19 * x ** 2 + 54 * x + 46)),
                z((3 * c ** 2 - c - 6).subs(c, x + 4) - (3 * x ** 2 + 23 * x + 38))]
res["Dscr(tc)"] = sp.simplify(Dc.subs(t, 1 / c) + 3 * (c - 3) * (c + 1) / c ** 4) == 0
# numeric sanity of the root picture for a few n (independent of the sign argument)
pic = {}
for nn in (7, 8, 12, 30, 200):
    Jn = sp.Poly(J.subs(n, nn), t)
    Dn = sp.Poly(Dscr.subs(n, nn), t)
    jr = sorted(float(q) for q in Jn.real_roots() if q > 0)
    dr = sorted(float(q) for q in Dn.real_roots() if q > 0)
    pic[nn] = {"J_pos_roots": jr, "Dscr_pos_roots": dr, "tc": 1 / (nn - 3), "tb": (nn - 1) / (nn * (nn - 4))}
res["picture"] = pic
print(json.dumps(res, indent=1, default=str))
json.dump(res, open(r"(local file)", "w"), indent=1, default=str)
