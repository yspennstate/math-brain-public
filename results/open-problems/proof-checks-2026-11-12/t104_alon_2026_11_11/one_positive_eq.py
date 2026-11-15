"""Equality cases on the one-positive family: which coefficients of T^3 Psi can vanish for admissible (k, j)."""
import sympy as sp
z1, z2, z3, k, j, kap, iota = sp.symbols("z1 z2 z3 k j kap iota")
tau, t, b = z1, z1 + z2, z1 + z2 + z3
a = tau + k * t + b
n = k + 3 + j
T = a**2 + tau**2 + k * t**2 + b**2
P = a**3 - tau**3 - k * t**3 - b**3
Q = a**4 + tau**4 + k * t**4 + b**4
G = sp.Poly(sp.expand((n - 4) * (2 * Q - T**2) * T - 2 * (n - 3) * P**2 + (n - 1) * ((n**2 - 6 * n + 6) * T**2 + 2 * n * Q) * b * t), z1, z2, z3)
d = dict(G.terms())
print("z1^6:", sp.factor(d[(6, 0, 0)]))
for name, sub in (("A", {k: 2 + kap, j: iota}), ("B", {k: 1, j: 1 + iota})):
    nz = []
    for mon, c in d.items():
        cc = sp.Poly(sp.expand(c.subs(sub)), kap, iota)
        const = cc.eval({kap: 0, iota: 0})
        if const == 0:
            nz.append((mon, sp.factor(cc.as_expr())))
    print("case", name, "coefficients with zero constant term:", nz)
