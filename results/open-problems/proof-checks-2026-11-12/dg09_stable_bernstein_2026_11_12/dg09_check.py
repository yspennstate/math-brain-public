# Checks for Hong-Li-Wang, "The stable Bernstein theorem in R^7" (arXiv 2609.15720):
# the flat model behind the critical exponent 5/2 and every constant of Section 13 (terminal Green flux).
import sympy as sp


def out(*a):
    print(*a, flush=True)


t, r = sp.symbols("t r", positive=True)
w5 = sp.pi ** 3                      # area of the unit sphere S^5
n = 6

# flat six-plane: G = 1 / (4 w5 r^4)
G = 1 / ((n - 2) * w5 * r ** (n - 2))
lap = sp.simplify(sp.diff(G, r, 2) + (n - 1) / r * sp.diff(G, r))
gradG = -sp.diff(G, r)
flux = sp.simplify(gradG * w5 * r ** (n - 1))
out("1. flat model: Laplacian of G away from the pole =", lap, "; flux through a sphere =", flux)

rt = sp.solve(sp.Eq(G, t), r)[0]     # radius of the level set {G = t}
J = sp.simplify((gradG ** 3 * w5 * r ** (n - 1)).subs(r, rt))
out("2. J(t) = int_{G=t} |grad G|^3 =", sp.simplify(J / t ** sp.Rational(5, 2)), "* t^(5/2);  32 sqrt(w5) =", sp.simplify(32 * sp.sqrt(w5)),
    "; equal:", sp.simplify(J / t ** sp.Rational(5, 2) - 32 * sp.sqrt(w5)) == 0)
out("   so int_0 J(t) t^(-sigma-1) dt converges exactly for sigma < 5/2 (integrand t^(3/2 - sigma))")

V = sp.simplify((w5 / n * r ** n).subs(r, rt))
out("3. flat model volume of {G > t}: V(t) t^(3/2) =", sp.simplify(V * t ** sp.Rational(3, 2)), "; 1/(48 sqrt(w5)) =", sp.simplify(1 / (48 * sp.sqrt(w5))),
    "; equal:", sp.simplify(V * t ** sp.Rational(3, 2) - 1 / (48 * sp.sqrt(w5))) == 0)

# Brendle's sharp inequality for a minimal hypersurface O^6: |dO| >= 6 |B^6|^(1/6) |O|^(5/6), |B^6| = w5/6
B6 = sp.pi ** 3 / 6
out("4. |B^6| = w5/6:", sp.simplify(B6 - w5 / 6) == 0)
# -V' >= |d{G>t}|^2 >= 36 (w5/6)^(1/3) V^(5/3)   =>   (V^(-2/3))' >= 24 (w5/6)^(1/3)
c1 = sp.Rational(2, 3) * 36 * (w5 / 6) ** sp.Rational(1, 3)
out("5. (V^(-2/3))' bound: (2/3)*36*(w5/6)^(1/3) equals 24 (w5/6)^(1/3):", sp.simplify(c1 - 24 * (w5 / 6) ** sp.Rational(1, 3)) == 0)
# V(t) <= [24 (w5/6)^(1/3) t]^(-3/2) = t^(-3/2) / (48 sqrt(w5))
c2 = (24 * (w5 / 6) ** sp.Rational(1, 3)) ** sp.Rational(3, 2)
out("6. (13.4): [24 (w5/6)^(1/3)]^(3/2) equals 48 sqrt(w5):", sp.simplify(c2 - 48 * sp.sqrt(w5)) == 0)
# 2 / (3 J_inf) <= 1 / (48 sqrt(w5))   =>   J_inf >= 32 sqrt(w5)
Jinf = sp.symbols("Jinf", positive=True)
sol = sp.solve(sp.Eq(sp.Rational(2, 3) / Jinf, 1 / (48 * sp.sqrt(w5))), Jinf)[0]
out("7. threshold for J_inf:", sp.simplify(sol), "; equals J_pole = 32 sqrt(w5):", sp.simplify(sol - 32 * sp.sqrt(w5)) == 0)
# in the flat model every inequality of the chain is an equality
dV = sp.simplify(-sp.diff(V, t))
out("8. flat model: J(t) * (-V'(t)) =", sp.simplify(J * dV), " (Cauchy-Schwarz is an equality)")
area = sp.simplify((w5 * r ** (n - 1)).subs(r, rt))
out("   flat model: -V' / |d{G>t}|^2 =", sp.simplify(dV / area ** 2), "; |dO| / (6 (w5/6)^(1/6) |O|^(5/6)) =",
    sp.simplify(area / (6 * (w5 / 6) ** sp.Rational(1, 6) * V ** sp.Rational(5, 6))))
