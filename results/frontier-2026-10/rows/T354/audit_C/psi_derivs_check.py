"""Symbolic check of psi'(1), psi''(1), psi'''(1) for psi(y) = (s+eps)/(s sqrt(y)+eps) (agent C, T354 audit)."""
import sympy as sp
y, s, e = sp.symbols("y s eps", positive=True)
psi = (s + e) / (s * sp.sqrt(y) + e)
r = s / (s + e)
claims = [-r / 2, s * (e + 3 * s) / (4 * (e + s) ** 2), -3 * s * (e ** 2 + 4 * e * s + 5 * s ** 2) / (8 * (e + s) ** 3)]
for k, c in enumerate(claims, 1):
    print(k, sp.simplify(sp.diff(psi, y, k).subs(y, 1) - c))
