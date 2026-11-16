"""Checks of the explicit computations in Sections 7.5 to 7.7 and 8.1, and of the series on page 92, of
arXiv 2611.06117 (standard library only)."""
import math
import random

ok = True


def line(name, got, want, tol=1e-8):
    global ok
    good = abs(got - want) <= tol * max(1.0, abs(want))
    ok = ok and good
    print("%-96s got %.12g  stated %.12g  %s" % (name, got, want, "PASS" if good else "FAIL"))


def holds(name, cond):
    global ok
    ok = ok and bool(cond)
    print("%-96s %s" % (name, "PASS" if cond else "FAIL"))


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


cs = math.sqrt(2) * math.exp(-1.5)
rho = cs / 8

# Section 7.5: velocity rescaling H(y) = R h(R y) in three dimensions, radial Gaussian h(x) = exp(-|x|^2/2)
Rv = 3.7
n2 = lambda c: math.sqrt(4 * math.pi * simpson(lambda r: r * r * math.exp(-c * c * r * r), 0.0, 40.0 / c, 40000))
line("||R h(R .)||_2 / ||h||_2 at R = 3.7 (= R^(-1/2))", Rv * n2(Rv) / n2(1.0), Rv ** -0.5)
# fourth radial derivative of exp(-c^2 r^2/2) along a line scales as c^4; the L^2 norm of a fourth derivative as c^(4 - 3/2)
holds("exponents: 1 - 3/2 = -1/2 and 1 + 4 - 3/2 = 7/2", 1 - 1.5 == -0.5 and 1 + 4 - 1.5 == 3.5)
hh = 1 / 400.0
line("int_{s-h}^s (s - u)^(-1/2) du, h = 1/400 (= 2 sqrt h)", simpson(lambda w: 2.0, 0.0, math.sqrt(hh), 10), 2 * math.sqrt(hh))
# the point distribution: symbol of degree 1 lies in H^-3, y_3 times it (degree 0) in H^-4 (already in H^-2)
line("int_0^inf r^4 (1 + r^2)^-3 dr (finite, = 3 pi/16)", simpson(lambda w: math.exp(5 * w) * (1 + math.exp(2 * w)) ** -3, -30.0, 30.0, 120000), 3 * math.pi / 16, 1e-7)
line("int_0^inf r^2 (1 + r^2)^-4 dr (finite, = pi/32)", simpson(lambda w: math.exp(3 * w) * (1 + math.exp(2 * w)) ** -4, -30.0, 30.0, 120000), math.pi / 32, 1e-7)
line("int_0^inf r^2 (1 + r^2)^-2 dr (degree 0 is already in H^-2, = pi/4)", simpson(lambda w: math.exp(3 * w) * (1 + math.exp(2 * w)) ** -2, -30.0, 30.0, 120000), math.pi / 4, 1e-7)
A = 400.0
for Th in (0.5, 1.0, 3.0):
    tp = (2 + Th * math.log(A)) / A
    line("e^{C A t_p} at C = 2.5, Theta = %.1f (= e^{2C} A^{C Theta})" % Th, math.exp(2.5 * A * tp), math.exp(5.0) * A ** (2.5 * Th))
    R = math.exp(rho * A)
    tf = tp + 16 * A * A
    d = tf / R ** 2
    ss = tp - d
    holds("Theta = %.1f, A = 400: s >= t_p/2 on (s_* - 2/A, s_*), d <= 17 A^2 R^-2, s <= d leaves t_p - s >= t_p/2" % Th,
          ss - 2 / A >= tp / 2 and d <= 17 * A * A / R ** 2 and tp - d >= tp / 2)
    line("int_{1/A}^{s_*} A R^-2 s^-2 ds, Theta = %.1f (= A R^-2 (A - 1/s_*), at most A^2 R^-2)" % Th,
         simpson(lambda w: A / R ** 2 * math.exp(-w), math.log(1 / A), math.log(ss), 20000), A / R ** 2 * (A - 1 / ss), 1e-7)

# Proposition 7.7 and Section 8.1: the exponent margins, for every omega with 0 < 2 omega < rho/32
al, de, sst, gam = 7 / 4, 1 / 4, 19 / 8, rho / 4
good = True
for k in range(1, 200):
    om = (rho / 64) * k / 200
    G = cs - om
    good = good and (al - de) * rho - 2 * om > rho and 1.5 * rho - 2 * om > rho and 1.75 * rho - 2 * om > rho
    good = good and 2 * G - 4.5 * rho > rho and 2 * G - 7.5 * rho > rho
    good = good and rho / 8 + 2 * om < 5 * rho / 32 < gam
    for x0 in (12 * rho, 12.5 * rho, 13 * rho + rho / 32):
        e = 7.5 * rho - 2 * x0 + 4 * cs - 2 * G
        good = good and e <= -rho / 2 + 2 * om + 1e-15 and -rho / 2 + 2 * om < -15 * rho / 32
    good = good and 15 * rho / 32 - 2 * om < rho / 2 - 2 * om
    # (8.10): A(a_-) < a_-/2 and A(a_+) > 2 a_+ up to powers of A
    good = good and (2 * cs - 3 * rho) - (13 * rho + rho / 32) < 0 and (2 * G - 3 * rho) - 12 * rho > 0
    # convergence of the series on the source interval: a_+ e^{Gamma_src} <= e^{(-12 rho + c_*) A}
    good = good and -12 * rho + cs < 0
holds("rates (7.48), (7.50), (7.51) exceed rho; (7.54); moment cost < 5 rho/32 < gamma; (8.10); series", good)
line("2 c_* - 3 rho - (13 rho + rho/32) in units of rho (= -1/32)", ((2 * cs - 3 * rho) - (13 * rho + rho / 32)) / rho, -1 / 32)
line("-12 rho + c_* in units of rho (= -4)", (-12 * rho + cs) / rho, -4.0)
holds("alpha = 7/4 < s_* - 1/2 = 15/8, s_* - alpha = 5/8 > 1/2, s_* + 1/16 = 39/16 < 5/2, rho_c = 3 rho/8 = 12 rho/32 < 13 rho/32",
      al < sst - 0.5 == 15 / 8 and sst - al == 5 / 8 > 0.5 and sst + 1 / 16 == 39 / 16 < 2.5 and 3 / 8 == 12 / 32 < 13 / 32)
holds("powers of R: 6 - 1 - 2 = 3; 3 + 1 + 7/2 = 15/2; 1 + 7/2 + 3 = 15/2; 4 - 3/2 = 5/2 and 5/2 + 2 = 9/2",
      6 - 1 - 2 == 3 and 3 + 1 + 3.5 == 7.5 and 1 + 3.5 + 3 == 7.5 and 4 - 1.5 == 2.5 and 2.5 + 2 == 4.5)
random.seed(4)
Rr, m, w, a, S = 5.3, -2.9, random.random(), 1.01, random.random()
line("(R^4/m) w - a S, times m R^-3 (= R w + a |m| R^-3 S for m < 0)", ((Rr ** 4 / m) * w - a * S) * m / Rr ** 3, Rr * w + a * abs(m) * S / Rr ** 3)

# (8.3), (8.4)
tp = (2 + math.log(A)) / A
tf = tp + 16 * A * A
Gs = lambda t: cs * A * (1 / (1 + tp) - 1 / (1 + t))
holds("Gamma_src increasing, Gamma_src(t_f) < c_* A; int_{t_p}^t e^{-2(m-1)(Gamma(t) - Gamma(u))} du <= t - t_p",
      Gs(tf) < cs * A and all(Gs(tp + 10.0 * (i + 1)) > Gs(tp + 10.0 * i) for i in range(50)))
t0 = 1.7
line("Gamma_src'(t) at t = 1.7 (= c_* A/(1 + t)^2)", (Gs(t0 + 1e-6) - Gs(t0 - 1e-6)) / 2e-6, cs * A / (1 + t0) ** 2, 1e-6)

# page 92: d_1 = L, d_m = L sum d_j d_{m-j}; d_m = Catalan(m-1) L^(2m-1) <= 4^(m-1) L^(2m-1); generating function
L = 1.7
dd = [0.0, L]
for mm in range(2, 16):
    dd.append(L * sum(dd[j] * dd[mm - j] for j in range(1, mm)))
cat = lambda q: math.comb(2 * q, q) // (q + 1)
holds("d_m = Catalan(m-1) L^(2m-1) and d_m <= 4^(m-1) L^(2m-1) for m = 1..15, L = 1.7",
      all(abs(dd[mm] - cat(mm - 1) * L ** (2 * mm - 1)) <= 1e-9 * dd[mm] and dd[mm] <= 4 ** (mm - 1) * L ** (2 * mm - 1) for mm in range(1, 16)))
z = 0.2 / (4 * L * L)
ser = sum(cat(q - 1) * L ** (2 * q - 1) * z ** q for q in range(1, 200))
line("sum d_m z^m at 4 L^2 z = 0.2 (= (1 - sqrt(1 - 4 L^2 z))/(2 L))", ser, (1 - math.sqrt(1 - 4 * L * L * z)) / (2 * L), 1e-12)
line("D = L z + L D^2 at the same point", ser, L * z + L * ser * ser, 1e-12)
print("ALL PASS" if ok else "SOME FAIL")
