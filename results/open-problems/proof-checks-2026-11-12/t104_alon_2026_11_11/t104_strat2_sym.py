"""Symbolic check of STRAT2 bound (2): the lower bound assembled from X1 >= D(lam s - s^2), X2 >= 0, X3 exact,
Q <= 2(lam/n + kappa s)(n S2 + D s), S2 <= eta s, lam = (s+2)/(n-1), equals D s/((D+1)n(n-2)^2)(B(3n-8) - Z s);
and d eps_{n,D}/dD = n^2(n-1)(n-2)^2(3n-8)/Z^2; and the n=5 D=3 threshold."""
import sympy as sp
n, D, s = sp.symbols("n D s", positive=True)
lam = (s + 2) / (n - 1); beta = (1 - lam) / (n - 2); c = 2 * n / (n - 2)
kap = (n - 2) / (2 * n); eta = D * (n - 1) / (n * (D + 1))
E = D * (lam * s - s ** 2) + beta * (D * s - c * eta * s) - 2 * (lam / n + kap * s) * (n * eta * s + D * s)
B = (D - 1) * n - 2 * D; Z = (n - 1) * (n - 2) ** 2 * (n + 2 * D) - B * (n - 4)
R = D * s / ((D + 1) * n * (n - 2) ** 2) * (B * (3 * n - 8) - Z * s)
print("bound (2) assembly - stated:", sp.simplify(E - R))
ep = B * (3 * n - 8) / Z
print("d eps/dD - stated:", sp.simplify(sp.diff(ep, D) - n ** 2 * (n - 1) * (n - 2) ** 2 * (3 * n - 8) / Z ** 2))
g = sp.symbols("g")
print("n=5 bracket at m4=13/20:", sp.expand(7 + 16 * g + (70 - 200 * g) * sp.Rational(13, 20)), " root", sp.solve(sp.Rational(105, 2) - 114 * g, g),
      " lam", (2 + sp.Rational(35, 76)) / 4)
