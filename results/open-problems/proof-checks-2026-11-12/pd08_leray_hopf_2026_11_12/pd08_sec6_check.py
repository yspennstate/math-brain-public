"""Checks of the explicit computations in Section 6 of arXiv 2611.06117 (standard library only)."""
import cmath
import math
import random

ok = True


def line(name, got, want, tol=1e-8):
    global ok
    good = abs(got - want) <= tol * max(1.0, abs(want))
    ok = ok and good
    print("%-84s got %.12g  stated %.12g  %s" % (name, got, want, "PASS" if good else "FAIL"))


def holds(name, cond):
    global ok
    ok = ok and bool(cond)
    print("%-84s %s" % (name, "PASS" if cond else "FAIL"))


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


# the logarithm in (6.8): integral over the unit disk of 1/(|xi|^2 + k^2) = pi log((1 + k^2)/k^2)
for k in (0.05, 0.4):
    num = 2 * math.pi * simpson(lambda p: p / (p * p + k * k), 0.0, 1.0, 200000)
    line("unit-disk integral of 1/(|xi_h|^2 + k^2), k = %.2f" % k, num, math.pi * math.log((1 + k * k) / (k * k)))

# holomorphic extension: for |Im k| < |Re k|/8, |xi^2 + k^2| >= c0 (xi^2 + |k|^2)
random.seed(1)
worst = 1.0
for _ in range(200000):
    re = random.uniform(-3, 3)
    im = random.uniform(-1, 1) * abs(re) / 8
    xi2 = random.uniform(0, 9)
    k = complex(re, im)
    if abs(k) > 1e-9:
        worst = min(worst, abs(xi2 + k * k) / (xi2 + abs(k) ** 2))
holds("|xi^2 + k^2| / (xi^2 + |k|^2) >= 0.9 on the sector |Im k| < |Re k|/8 (smallest %.4f)" % worst, worst >= 0.9)

# the coupling operators of (6.2): d_r Phi g = 2 Omega g and K h = 2 Omega (1 - zeta) (1/r) int_0^r u h
A, ell, t = 3.0, 1.7, 0.9
T = ell * ell + t
g = lambda u: math.exp(-0.3 * u) * (1 + u * u)
Phi = lambda r: -2 * A * ell ** 2 * T ** -2 * simpson(lambda u: math.exp(-u * u / (4 * T)) * g(u), r, r + 80.0, 40000)
r = 1.3
Om = A * ell ** 2 * T ** -2 * math.exp(-r * r / (4 * T))
line("d_r Phi_{l,t} g at r = 1.3 (= 2 Omega_l g)", (Phi(r + 1e-4) - Phi(r - 1e-4)) / 2e-4, 2 * Om * g(r), 1e-6)
zeta = r * r / (4 * T)
line("the factor (2 - r^2/(2T)) e^-zeta A l^2 T^-2 (= 2 Omega_l (1 - zeta))",
     A * ell ** 2 * T ** -2 * (2 - r * r / (2 * T)) * math.exp(-zeta), 2 * Om * (1 - zeta))

# scaling exponents of (6.5).  Phi_{l,t} = A l^2 T^(-3/2) D Phi_* D^-1 (checked below) and P_k = D P_{k sqrt T} D^-1,
# so the meridional block is A l^2 T^-2 D R_*(k sqrt T) D^-1; each k-derivative gives sqrt T and the L^2_k norm T^(-1/4).
holds("two derivatives: -2 + 2 (1/2) - 1/4 = -5/4; one derivative: -2 + 1/2 - 1/4 = -7/4; sup norm of one: -3/2",
      abs(-2 + 1.0 - 0.25 - (-1.25)) < 1e-15 and abs(-2 + 0.5 - 0.25 - (-1.75)) < 1e-15 and abs(-2 + 0.5 - (-1.5)) < 1e-15)
# the dilation identity: with (D g)(r) = T^(-1/2) g(r/sqrt T), (D Phi_* D^-1 g)(r) = T^(-1/2) (-2) int_r^inf e^(-u^2/(4T)) g(u) du
Tt = 2.9
gg = lambda u: math.exp(-0.2 * u) * (2 + math.sin(u))
rr = 0.8
lhs = Tt ** -0.5 * (-2) * simpson(lambda s: math.exp(-s * s / 4) * math.sqrt(Tt) * gg(math.sqrt(Tt) * s),
                                  rr / math.sqrt(Tt), rr / math.sqrt(Tt) + 60.0, 60000)
rhs_ = Tt ** -0.5 * (-2) * simpson(lambda u: math.exp(-u * u / (4 * Tt)) * gg(u), rr, rr + 100.0, 60000)
line("dilation identity for Phi_* at T = 2.9, r = 0.8", lhs, rhs_, 1e-7)
# time integrals: l^2 (l^2 + t)^(-5/4 + th/2) over [0, inf) converges for th < 1/2 and is C l^(-1/2 + th)
th = 0.3
for l in (1.0, 50.0):
    num = simpson(lambda s: l * l * (l * l + s * s) ** (-1.25 + th / 2) * 2 * s, 0.0, 3e4, 600000)
    exact_tail = l * l * (l * l + 9e8) ** (-0.25 + th / 2) / (0.25 - th / 2)
    exact = l * l * (l * l) ** (-0.25 + th / 2) / (0.25 - th / 2)
    line("int_0^inf l^2 (l^2 + t)^(-5/4 + th/2) dt, l = %g, th = 0.3 (= l^(3/2 + th)/(1/4 - th/2))" % l,
         num + exact_tail, exact, 1e-5)
# note: on [t_p, t_f] the integral is also at most 16 A^2 l^(-1/2 + th), the bound used for l >= R

# the axial heat filter: -L k^2 + C A |k| = -L (|k| - C A/(2L))^2 + C^2 A^2/(4L)
L, C, Aa = 16 * 37.0 ** 2, 2.5, 37.0
m = max(-L * k * k + C * Aa * k for k in [i * 1e-5 for i in range(200001)])
line("max over k of -L k^2 + C A k with L = 16 A^2 (= C^2/64)", m, C * C / 64, 1e-6)

# cutoff: 1 - (1 + x)^(-1/2) <= sqrt(x/2) and 1 - exp(-y^2/2) <= |y|/sqrt 2
holds("1 - (1 + x)^(-1/2) <= min(x/2, sqrt(x/2)) for x in (0, 100]",
      all(1 - (1 + x) ** -0.5 <= min(x / 2, math.sqrt(x / 2)) + 1e-15 for x in [i / 100 for i in range(1, 10001)]))
holds("1 - exp(-y^2/2) <= y/sqrt 2 for y in [0, 20]",
      all(1 - math.exp(-y * y / 2) <= y / math.sqrt(2) + 1e-15 for y in [i / 1000 for i in range(20001)]))

# triangular system with equality: x0' = a x0, x1' = a x1 + b x0, x2' = a x2 + b x1
a = lambda s: 0.7 + 0.2 * math.sin(s)
b = lambda s: 1.1 + 0.5 * math.cos(2 * s)
x = [1.3, 0.4, 2.2]
x0 = list(x)
n = 200000
h = 1.5 / n
s = 0.0


def rhs(s, x):
    return [a(s) * x[0], a(s) * x[1] + b(s) * x[0], a(s) * x[2] + b(s) * x[1]]


for i in range(n):
    k1 = rhs(s, x)
    k2 = rhs(s + h / 2, [x[j] + h / 2 * k1[j] for j in range(3)])
    k3 = rhs(s + h / 2, [x[j] + h / 2 * k2[j] for j in range(3)])
    k4 = rhs(s + h, [x[j] + h * k3[j] for j in range(3)])
    x = [x[j] + h / 6 * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]) for j in range(3)]
    s += h
A0 = simpson(a, 0.0, 1.5)
B0 = simpson(b, 0.0, 1.5)
line("x1(t) in the equality case (= e^{A0}(x1(0) + B0 x0(0)))", x[1], math.exp(A0) * (x0[1] + B0 * x0[0]))
line("x2(t) in the equality case (= e^{A0}(x2(0) + B0 x1(0) + B0^2 x0(0)/2))", x[2],
     math.exp(A0) * (x0[2] + B0 * x0[1] + B0 * B0 * x0[0] / 2))
# the omitted translations: int_{|h| > kappa} 4/|h|^(1 + 2 th) dh = (4/th) kappa^(-2 th)
kap = 0.07
line("int_{|h| > kappa} 4 |h|^(-1 - 2 th) dh (= (4/th) kappa^(-2 th))",
     2 * 4 * kap ** (-2 * th) / (2 * th), 4 / th * kap ** (-2 * th))
print("ALL PASS" if ok else "SOME FAIL")
