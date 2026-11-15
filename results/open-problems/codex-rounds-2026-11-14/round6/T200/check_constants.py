"""Numerical check of the constants in the proof of Theorem 1.1.

Every quantity is computed with mpmath at sixty significant digits. The proof itself
uses only the exact inequalities printed in the paper; this script confirms them.
Run: python check_constants.py
"""
from mpmath import mp, mpf, sqrt, pi, erfc, exp, log, quad, beta as Beta

mp.dps = 60
a, b, u, s, c = mpf(19) / 10, mpf(17) / 5, mpf(81) / 730, mpf(43) / 2, mpf(5) / 121
ok = True


def check(name, cond):
    global ok
    ok = ok and bool(cond)
    print(f"{'PASS' if cond else 'FAIL'}  {name}")


# Lemma 2.1: g(a,b) and the Green function minimum (r = 1) on a grid of radii and angles.
g = 1 / (1 + a) - b / (b**2 + a)
check("g(a,b) = 1800/19517", abs(g - mpf(1800) / 19517) < mpf(10) ** -50)
check("g(a,b) = (b-1)(b-a)/((1+a)(b^2+a))", abs(g - (b - 1) * (b - a) / ((1 + a) * (b**2 + a))) < mpf(10) ** -50)
check("(1+a)^2 + (b^2-1)(b^2-a^2)/b^2 = (b^2+a)^2/b^2",
      abs((1 + a) ** 2 + (b**2 - 1) * (b**2 - a**2) / b**2 - (b**2 + a) ** 2 / b**2) < mpf(10) ** -50)


def green(x, y, cosang):
    d = sqrt(x * x + y * y - 2 * x * y * cosang)
    A = (b * b - x * x) * (b * b - y * y) / (b * b)
    return 1 / d - 1 / sqrt(d * d + A)


gmin = min(green(mpf(i) / 40, a * mpf(j) / 40, mpf(k) / 20 - 1)
           for i in range(1, 41) for j in range(1, 41) for k in range(0, 40))
print("      Green function grid minimum", mp.nstr(gmin, 12), " g =", mp.nstr(g, 12))
check("grid minimum >= g", gmin >= g - mpf(10) ** -40)
check("a g(a,b) < 1", a * g < 1)

# Lemma 3.3: the Riesz potential of rho is the constant J.
Bc = Beta(mpf(3) / 4, mpf(3) / 4)
J = pi * sqrt(2) / Bc
for v in (mpf(1) / 10, mpf(3) / 10, mpf(1) / 2, mpf(9) / 10):
    p = quad(lambda w: abs(v - w) ** mpf(-0.5) * (w * (1 - w)) ** mpf(-0.25) / Bc, [0, v, 1])
    check(f"potential at v = {mp.nstr(v, 2)} equals J (|diff| = {mp.nstr(abs(p - J), 3)})", abs(p - J) < mpf(10) ** -20)
print("      J =", mp.nstr(J, 15))
check("J < 21/8", J < mpf(21) / 8)

# Proof of Theorem 1.1.
x = (a - 1) / sqrt(u)
check("x^2 = 73/10", abs(x * x - mpf(73) / 10) < mpf(10) ** -50)
phi = exp(-x * x / 2) / sqrt(2 * pi)
tail_exact = 2 * a * erfc(x / sqrt(2)) / 2
tail_mills = 2 * a * phi * (x * x + 2) / (x * (x * x + 3))
print("      2a Phibar(x): exact", mp.nstr(tail_exact, 10), " Mills bound", mp.nstr(tail_mills, 10))
check("exact tail < Mills bound", tail_exact < tail_mills)
energy = J / (exp(1) * s) * sqrt(2 / (pi * u))
print("      energy term", mp.nstr(energy, 10))
m = tail_mills + energy
print("      m(a,u,s) with the Mills bound", mp.nstr(m, 10))
check("m < 151/1250", m < mpf(151) / 1250)
beta_star = exp(s * c) * mpf(151) / 1250
print("      beta_* bound", mp.nstr(beta_star, 10), " 1/b =", mp.nstr(1 / b, 10))
check("beta_* < 1/b", beta_star < 1 / b)
delta = g * c / log(b)
check("delta_1 = 9000/(2361557 log(17/5))", abs(delta - mpf(9000) / (2361557 * log(b))) < mpf(10) ** -50)
print("      delta_1 =", mp.nstr(delta, 15), " xi_3(1,1) <=", mp.nstr(1 - delta, 15))
check("1 - delta_1 < 0.99689", 1 - delta < mpf("0.99689"))

# Liu's margin, for comparison.
d0 = -log(1 - mpf(1) / 1800) / (4 * log(4))
print("      Liu's delta_0 =", mp.nstr(d0, 10), " ratio delta_1/delta_0 =", mp.nstr(delta / d0, 6))

print("ALL PASS" if ok else "SOME CHECK FAILED")
raise SystemExit(0 if ok else 1)
