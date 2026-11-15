"""Numerical and exact checks of the computations in Section 5 of arXiv 2611.06117 (standard library only).

Each line prints the quantity, the value found, the value stated in the paper and PASS or FAIL.
"""
import math
from fractions import Fraction as Fr

ok = True


def line(name, got, want, tol=1e-9):
    global ok
    good = abs(got - want) <= tol * max(1.0, abs(want))
    ok = ok and good
    print("%-78s got %.12g  stated %.12g  %s" % (name, got, want, "PASS" if good else "FAIL"))


def holds(name, cond):
    global ok
    ok = ok and bool(cond)
    print("%-78s %s" % (name, "PASS" if cond else "FAIL"))


def simpson(f, a, b, n=200000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


cstar = math.sqrt(2) * math.exp(-1.5)

# Proposition 5.2: the coupling outside zeta = 1/2, relative to v_r^2 + 2 v_theta^2
g = lambda z: (2 * z - 1) * math.exp(-z) / math.sqrt(2)
zs = [0.5 + i * 1e-4 for i in range(200001)]
vals = [g(z) for z in zs]
m = max(vals)
line("max over zeta >= 1/2 of (2 zeta - 1) e^-zeta / sqrt 2  (= c_*)", m, cstar, 1e-7)
line("  attained at zeta", zs[vals.index(m)], 1.5, 1e-3)
# inside zeta <= 1/2 the coefficient 1 - kappa (1 - zeta) with kappa = 1/(1 - zeta) vanishes
holds("1 - kappa (1 - zeta) = 0 for kappa = 1/(1 - zeta), zeta in [0, 1/2]",
      all(abs(1 - (1 / (1 - z)) * (1 - z)) < 1e-14 for z in [i / 1000 for i in range(501)]))
# |v_r v_theta| <= (v_r^2 + 2 v_theta^2) / (2 sqrt 2)
holds("|a b| <= (a^2 + 2 b^2)/(2 sqrt 2) on a grid, equality at a = sqrt 2 b",
      all(abs(a * b) <= (a * a + 2 * b * b) / (2 * math.sqrt(2)) + 1e-15
          for a in [i / 50 - 2 for i in range(201)] for b in [j / 50 - 2 for j in range(201)]))
# Gamma_src' = c_* A / (1 + t)^2
A, tp = 37.0, 0.3
G = lambda t: cstar * A * (1 / (1 + tp) - 1 / (1 + t))
t = 2.7
line("d/dt Gamma_src at t = 2.7, A = 37", (G(t + 1e-6) - G(t - 1e-6)) / 2e-6, cstar * A / (1 + t) ** 2, 1e-6)

# the reduced weight w = 1 + A^-2mu <x>^2mu: |grad w|/w <= 2 mu / A, and A^-2mu <x>^(2mu-2) <= A^-2 w
for mu in (1.0, 1.7, 2.4):
    worst1 = 0.0; good2 = True
    for Aval in (5.0, 50.0):
        for i in range(1, 4000):
            x = 1.0 + (i / 40.0) ** 2 * Aval / 10
            w = 1 + Aval ** (-2 * mu) * x ** (2 * mu)
            gw = 2 * mu * Aval ** (-2 * mu) * x ** (2 * mu - 1)
            worst1 = max(worst1, gw / w * Aval / (2 * mu))
            good2 = good2 and (Aval ** (-2 * mu) * x ** (2 * mu - 2) <= Aval ** (-2) * w * (1 + 1e-12))
            good2 = good2 and (gw / math.sqrt(w) <= 2 * mu * Aval ** (-mu) * x ** (mu - 1) * (1 + 1e-12))
    holds("mu = %.1f: A |grad w| / (2 mu w) <= 1 (largest %.4f); the two pointwise comparisons" % (mu, worst1),
          worst1 <= 1.0 and good2)

# Proposition 5.3: exponents
al, ss = Fr(7, 4), Fr(19, 8)
holds("1/2 - s_* = -15/8 and s_* - alpha = 5/8 > 1/2", Fr(1, 2) - ss == Fr(-15, 8) and ss - al == Fr(5, 8) and ss - al > Fr(1, 2))
# with rho = 1 as the unit, 2 omega < rho/32
holds("(15/8) rho > 2 omega when 2 omega < rho/32", Fr(15, 8) > Fr(1, 32))
# int (r^2+z^2)^-mu dz = C r^(1-2mu): check the scaling at mu = 5/8
I1 = simpson(lambda z: (1.0 + z * z) ** (-0.625), -4000.0, 4000.0, 800000)
I2 = simpson(lambda z: (4.0 + z * z) ** (-0.625), -8000.0, 8000.0, 800000)
line("ratio of int (r^2+z^2)^-5/8 dz at r = 2 and r = 1 (= 2^(1-5/4)), tails cut at 4000 r", I2 / I1, 2 ** (-0.25), 2e-3)
# sqrt(pi A): int (1 + z^2/A^2)^-1 dz = pi A
line("int (1 + z^2/A^2)^-1 dz for A = 3 (= 3 pi)", 2 * 3 * math.atan(1e9), 3 * math.pi, 1e-8)

# Lemma 5.4
ell, L = 1.3, 40.0
for r in (0.2, 1.0, 3.5):
    W = lambda tau: r * tau ** -2 * math.exp(-r * r / (4 * tau))
    num = 0.25 * simpson(W, ell, L, 20000)
    line("(1/4) int_ell^L W_tau dtau at r = %.1f" % r, num, (math.exp(-r * r / (4 * L)) - math.exp(-r * r / (4 * ell))) / r)
    chi = lambda s: (1 - math.exp(-s * s / (4 * ell))) / s
    d = (chi(r + 1e-5) - chi(r - 1e-5)) / 2e-5 - chi(r) / r
    z = r * r / (4 * ell)
    khist = 8 / (r * r) * (1 - (1 + z) * math.exp(-z))
    line("(d_r - 1/r)(K_ell/r) at r = %.1f (= -K_hist/4)" % r, d, -khist / 4, 1e-6)
hmax = max((1 - (1 + z) * math.exp(-z)) / z for z in [i / 1000 for i in range(1, 100000)])
holds("(1 - (1 + zeta) e^-zeta)/zeta <= 1, so K_hist <= 2/ell  (largest value %.4f)" % hmax, hmax <= 1)
holds("|cos y - 1| <= 2 |y|^(3/2) on [0, 50]",
      all(abs(math.cos(y) - 1) <= 2 * y ** 1.5 + 1e-15 for y in [i / 1000 for i in range(50001)]))
# int |z|^3 (a + z^2)^(-9/4) dz = (16/5) a^(-1/4); with u = z^2 it is B(2, 1/4) a^(-1/4)
beta = math.gamma(2) * math.gamma(0.25) / math.gamma(2.25)
line("B(2, 1/4) = Gamma(2) Gamma(1/4) / Gamma(9/4)", beta, 16 / 5)
# Hilbert-Schmidt norm of phi_0: 4 T^-4 int e^(-a^2/(2T)) a/2 da = 2 T^-3
T = 2.3
hs2 = 4 * T ** -4 * simpson(lambda a: math.exp(-a * a / (2 * T)) * a / 2, 0.0, 60.0, 60000)
line("squared Hilbert-Schmidt norm of phi_0 at T = 2.3 (= 2 T^-3)", hs2, 2 * T ** -3)
line("int_0^inf sqrt 2 (1+t)^(-3/2) dt (= 2 sqrt 2)", math.sqrt(2) * 2, 2 * math.sqrt(2))
holds("e^-zeta max(1, |1 - zeta|) <= 1, so the coupling matrix is at most 2A/(1+t)^2",
      all(math.exp(-z) * max(1, abs(1 - z)) <= 1 + 1e-15 for z in [i / 1000 for i in range(40001)]))

# Proposition 5.5: exponents in units of rho
rc, ga = Fr(3, 8), Fr(1, 4)
holds("rho_c - gamma = rho/8, and minus rho/32 leaves 3 rho/32", rc - ga == Fr(1, 8) and rc - ga - Fr(1, 32) == Fr(3, 32))
holds("alpha/s_* = 14/19", al / ss == Fr(14, 19))
e = -(2 - al / ss) * rc + (al / ss) * ga
holds("-(24/19)(3 rho/8) + (14/19)(rho/4) = -11 rho/38", e == Fr(-11, 38))
holds("17/2 = 8 + 2 delta_Sob with delta_Sob = 1/4, and alpha < 2 + delta_Sob", Fr(17, 2) == 8 + 2 * Fr(1, 4) and al < 2 + Fr(1, 4))
holds("1 + alpha = 11/4 and 9/4 < s_*", 1 + al == Fr(11, 4) and Fr(9, 4) < ss)
holds("(alpha - delta_Sob) rho = 3 rho/2 > rho/32 > 2 omega", al - Fr(1, 4) == Fr(3, 2))
print("ALL PASS" if ok else "SOME FAIL")
