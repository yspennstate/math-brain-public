"""Psi >= 0 on x = (a, -tau, -t x k, -b, 0 x j), a = tau + k t + b, 0 <= tau <= t <= b, n = k + 3 + j >= 5.
Coordinates tau = z1, t = z1 + z2, b = z1 + z2 + z3, z >= 0.  G = Psi T^3 is a sextic in z with coefficients in
Z[k, j].  Case A: k >= 2, j >= 0 (k = 2 + kap, j = iota).  Case B: k = 1, j >= 1 (j = 1 + iota).  Each coefficient
must have no negative coefficient as a polynomial in (kap, iota).  Then a numerical comparison of G / T^3 with Psi
computed from the definition (m by brute force over pairs) at random points.  an agent, 11 Nov 2026."""
import random
from fractions import Fraction
import sympy as sp
z1, z2, z3, k, j, kap, iota = sp.symbols("z1 z2 z3 k j kap iota")
tau, t, b = z1, z1 + z2, z1 + z2 + z3
a = tau + k * t + b
n = k + 3 + j
T = a**2 + tau**2 + k * t**2 + b**2
P = a**3 - tau**3 - k * t**3 - b**3
Q = a**4 + tau**4 + k * t**4 + b**4
G = sp.expand((n - 4) * (2 * Q - T**2) * T - 2 * (n - 3) * P**2 + (n - 1) * ((n**2 - 6 * n + 6) * T**2 + 2 * n * Q) * b * t)
Gp = sp.Poly(G, z1, z2, z3)
for name, sub in (("A: k>=2, j>=0", {k: 2 + kap, j: iota}), ("B: k=1, j>=1", {k: 1, j: 1 + iota})):
    bad, zero, tot = 0, [], 0
    for mon, c in Gp.terms():
        cc = sp.Poly(sp.expand(c.subs(sub)), kap, iota)
        tot += 1
        if cc.is_zero:
            zero.append(mon)
        elif any(v < 0 for v in cc.coeffs()):
            bad += 1
            print("  NEGATIVE in", mon, sp.factor(cc.as_expr()))
    print(f"case {name}: monomials {tot}, identically zero {zero}, with a negative coefficient {bad}", flush=True)
absent = [m for m in [(6, 0, 0), (0, 0, 6)] if m not in dict(Gp.terms())]
print("pure powers absent from G:", absent, "(star z1^6, edge z3^6)")

def psi_def(x):
    nn = len(x)
    T_ = sum(v * v for v in x)
    q = sum(v**4 for v in x) / T_**2
    p3sq = Fraction(sum(v**3 for v in x)) ** 2 / T_**3
    m = max(x[i] * x[l] for i in range(nn) for l in range(i + 1, nn)) / T_
    return (nn - 4) * (2 * q - 1) - 2 * (nn - 3) * p3sq + (nn - 1) * (nn * nn - 6 * nn + 6 + 2 * nn * q) * m

rnd = random.Random(11)
Gf = sp.lambdify((z1, z2, z3, k, j), G, "math")
mism = 0
for _ in range(300):
    kk, jj = rnd.randint(1, 9), rnd.randint(0, 5)
    if kk + jj < 2:
        continue
    zz = [Fraction(rnd.randint(0, 6), rnd.randint(1, 5)) for _ in range(3)]
    if sum(zz) == 0:
        continue
    ta, tt, bb = zz[0], zz[0] + zz[1], zz[0] + zz[1] + zz[2]
    aa = ta + kk * tt + bb
    x = [aa, -ta] + [-tt] * kk + [-bb] + [Fraction(0)] * jj
    assert sum(x) == 0
    T_ = sum(v * v for v in x)
    g = G.subs({z1: zz[0], z2: zz[1], z3: zz[2], k: kk, j: jj})
    if sp.Rational(psi_def(x).numerator, psi_def(x).denominator) * sp.Rational(T_.numerator, T_.denominator) ** 3 != g:
        mism += 1
print("exact comparison with the definition at random rational points: mismatches", mism)
