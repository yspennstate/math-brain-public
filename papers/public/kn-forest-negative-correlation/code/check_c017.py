"""Independent sympy check of the T084-C016/C017 algebra used by the C018 sign argument."""
import sympy as sp
n, t, r, u = sp.symbols("n t r u")
h = (n - 2) * (n - 3)
delta = t * h
a = t - 2 * (n - 4) * t**2
b = -1 + (2 * n - 9) * t + n * (n - 4) * t**2
F = delta * r**2 - b * r - a
B = n**2 * t**2 + (2 * n + 1) * t - 1
phi = t - 2 * n * t**2 + B * r - n * (n - 1) * t * r**2
G = 2 * t**2 * sp.diff(F, t) + sp.diff(F, r) * phi
L = (n**3 * (n - 4) * t**4 + 2 * n * (n**2 - 4 * n - 6) * t**3
     + 3 * (n**2 - 9 * n + 3) * t**2 + 2 * (n**2 - 9 * n + 9) * t - (2 * n - 3))
C = 2 * n**2 * (n - 4) * t**3 + 3 * n * (n - 6) * t**2 + (2 * n**2 - 16 * n + 15) * t - (2 * n - 3)
A = n * (n - 4)
J = 2 * A**2 * t**3 - 6 * A * (n - 2) * t**2 + 6 * (n - 1) * (n - 3) * t - (2 * n - 3)
ok = True
def chk(name, expr):
    global ok
    z = sp.expand(expr) == 0
    ok &= z
    print(name, "OK" if z else "FAIL")
chk("(1) hG identity", h * G - (F * (-2 * h * n * (n - 1) * t * r + 2 * h * t + 2 * h * B - n * (n - 1) * b) + 2 * (L * r - t * C)))
chk("(2) boundary product", delta * t**2 * C**2 - b * t * L * C - a * L**2 + h**2 * t**5 * J)
Dscr = sp.expand(b**2 + 4 * delta * a)
chk("(6) discriminant", Dscr - (1 + (18 - 4 * n) * t + (6 * n**2 - 48 * n + 105) * t**2
                         + (-4 * n**3 + 38 * n**2 - 136 * n + 192) * t**3 + n**2 * (n - 4)**2 * t**4))
chk("J' form", sp.diff(J, t) - 6 * ((A * t - (n - 2))**2 - 1))
chk("J(t_a)", sp.simplify(J.subs(t, (n - 3) / A) + (n - 6) / (n - 4)))
chk("J(t_b)", sp.simplify(J.subs(t, (n - 1) / A) + (n - 2) / n))
c = sp.symbols("c")
Dc = Dscr.subs(n, c + 3)
p7 = sp.Poly(sp.expand(sp.cancel(c**4 * (1 + u)**4 * Dc.subs(t, u / (c * (1 + u))))), u)
want7 = [c**4, 6 * c**3, c**2 * (6 * c + 15), -2 * c * (c + 1) * (2 * c - 9), -3 * (c - 3) * (c + 1)]
for k, w in enumerate(want7):
    chk(f"(7) u^{k}", p7.coeff_monomial(u**k) - w)
p8 = sp.Poly(sp.expand(c**4 * Dc.subs(t, (1 + u) / c)), u)
want8 = [-3 * (c - 3) * (c + 1), 2 * (2 * c**3 - 13 * c**2 + 3 * c + 18), 9 * (2 * c**3 - 5 * c**2 - 2 * c + 6),
         6 * (c - 1) * (3 * c**2 - c - 6), (c + 3)**2 * (c - 1)**2]
for k, w in enumerate(want8):
    chk(f"(8) u^{k}", p8.coeff_monomial(u**k) - w)
x = sp.symbols("x")
chk("(8) x-shift 1", (2 * c**3 - 5 * c**2 - 2 * c + 6).subs(c, x + 4) - (2 * x**3 + 19 * x**2 + 54 * x + 46))
chk("(8) x-shift 2", (3 * c**2 - c - 6).subs(c, x + 4) - (3 * x**2 + 23 * x + 38))
# numeric sanity of the ordering tau_1 < t_c < tau_2 < beta for n = 7..40
for nv in range(7, 41):
    Dn = sp.Poly(Dscr.subs(n, nv), t)
    roots = sorted(float(z) for z in sp.real_roots(Dn) if z > 0)
    jb = [float(z) for z in sp.real_roots(sp.Poly(J.subs(n, nv), t)) if z > 0]
    good = len(roots) == 2 and len(jb) == 1 and roots[0] < 1 / (nv - 3) < roots[1] < jb[0]
    ok &= good
    if not good or nv in (7, 40):
        print("n", nv, "tau", roots, "beta", jb, good)
print("ALL OK" if ok else "FAIL")
