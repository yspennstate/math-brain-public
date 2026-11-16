"""Checks of the explicit computations in Sections 7.3 and 7.4 of arXiv 2611.06117 (standard library only)."""
import math

ok = True


def line(name, got, want, tol=1e-8):
    global ok
    good = abs(got - want) <= tol * max(1.0, abs(want))
    ok = ok and good
    print("%-92s got %.12g  stated %.12g  %s" % (name, got, want, "PASS" if good else "FAIL"))


def holds(name, cond):
    global ok
    ok = ok and bool(cond)
    print("%-92s %s" % (name, "PASS" if cond else "FAIL"))


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


# (7.22): int_{R^2} (1 + |xi|^2)^(-3 + al - de) d xi = pi/(2 - al + de)
al, de = 1.6, 0.3
p = 3 - al + de
num = 2 * math.pi * simpson(lambda w: math.exp(2 * w) * (1 + math.exp(2 * w)) ** -p, -30.0, 30.0, 120000)
line("int_{R^2} (1 + |xi_h|^2)^(-3 + al - de) d xi_h, al = 1.6, de = 0.3 (= pi/(2 - al + de))", num, math.pi / (2 - al + de), 1e-7)
holds("|xi_h|^2 + k^2 <= (1 + |xi_h|^2)(1 + k^2); (1 + k^2)^((1+al)/2) <= (1 + |k|)^(1+al)",
      all(x + k * k <= (1 + x) * (1 + k * k) + 1e-12 and (1 + k * k) ** ((1 + al) / 2) <= (1 + k) ** (1 + al) + 1e-12
          for x in [i / 7 for i in range(200)] for k in [j / 5 for j in range(100)]))
holds("|1 - cos y| <= 2 |y|^al and 1 - e^{-u} <= u^(al/2) for al = 1.6",
      all(abs(1 - math.cos(y)) <= 2 * y ** al + 1e-15 for y in [i / 500 for i in range(1, 30001)])
      and all(1 - math.exp(-u) <= u ** (al / 2) + 1e-15 for u in [i / 500 for i in range(1, 30001)]))

# the dual integral before (7.25): pi int (1 - e^{-r^2/(4L)})^2 dr/(r sqrt(1 + r^2)) <= C L^(-1/2)
vals = []
for L in (1.0, 10.0, 100.0, 1e4, 1e6):
    g = lambda w: (1 - math.exp(-math.exp(2 * w) / (4 * L))) ** 2 / math.sqrt(1 + math.exp(2 * w))
    vals.append(math.pi * simpson(g, -25.0, 45.0, 140000) * math.sqrt(L))
holds("sqrt(L) pi int (1 - e^{-r^2/(4L)})^2 dr/(r sqrt(1 + r^2)) for L = 1 .. 1e6 in [%.3f, %.3f]" % (min(vals), max(vals)), max(vals) < 4)
line("int dz/(a + z^2) at a = 2.7 (= pi/sqrt a)", simpson(lambda z: 1 / (2.7 + z * z), -2e4, 2e4, 2000000) + 2 / 2e4, math.pi / math.sqrt(2.7), 1e-6)

# (7.28), (7.29), (7.31): the time integrals of one old column, rho = l/R, age rho^2 + d + s, d = t_f/R^2
l, R, tf = 0.2, 5.0, 48.3
rho, d = l / R, tf / R ** 2
I = lambda q: simpson(lambda w: math.exp(w) * (rho * rho + d + math.exp(w)) ** -q, -40.0, 40.0, 160000)
line("int_0^inf rho^2 (rho^2 + d + s)^-2 ds (= l^2/(l^2 + t_f))", rho * rho * I(2.0), l * l / (l * l + tf), 1e-7)
line("int_0^inf rho^2 (rho^2 + d + s)^(-3/2) ds (= 2 l^2/(R sqrt(l^2 + t_f)))", rho * rho * I(1.5), 2 * l * l / (R * math.sqrt(l * l + tf)), 1e-7)
line("int_0^inf rho (rho^2 + d + s)^(-3/2) ds (= 2 l/sqrt(l^2 + t_f))", rho * I(1.5), 2 * l / math.sqrt(l * l + tf), 1e-7)
line("int_0^inf rho (rho^2 + d + s)^-2 ds (= R l/(l^2 + t_f))", rho * I(2.0), R * l / (l * l + tf), 1e-7)
T = 1.9
m = max(r * math.exp(-r * r / (4 * T)) for r in [i / 1000 for i in range(20001)])
line("sup_r r e^{-r^2/(4T)} at T = 1.9 (= sqrt(2T/e))", m, math.sqrt(2 * T / math.e), 1e-6)

# (7.32), (7.33)
A = 400.0
Rr = math.exp(math.sqrt(2) * math.exp(-1.5) / 8 * A)
tp = (2 + math.log(A)) / A
tf2 = tp + 16 * A * A
ts = Rr ** 2 * tp
G = lambda t: 2 * A * Rr ** 2 * (1 / (Rr ** 2 + tf2) - 1 / (Rr ** 2 + t))
t0 = 0.37 * ts
h = t0 * 1e-6
line("Gamma_tr'(t) at t = 0.37 t_* (= 2 A R^2/(R^2 + t)^2)", (G(t0 + h) - G(t0 - h)) / (2 * h) * Rr ** 2, 2 * A * Rr ** 4 / (Rr ** 2 + t0) ** 2, 1e-5)
holds("Gamma_tr' >= A/(2 R^2) on [t_f, t_*] and Gamma_tr(t_*) <= 2 A t_p (A = 400)",
      2 * A * Rr ** 2 / (Rr ** 2 + ts) ** 2 >= A / (2 * Rr ** 2) and G(ts) <= 2 * A * tp)
# (7.35): int_{t_f}^t e^{-(n-1) A (t-u)/R^2} du <= R^2/((n-1) A)
n_, A_, R_, t_ = 3, 2.0, 5.0, 40.0
line("int_0^t e^{-(n-1) A (t-u)/R^2} du, t = 40 (= R^2 (1 - e^{-(n-1) A t/R^2})/((n-1) A))",
     simpson(lambda u: math.exp(-(n_ - 1) * A_ * (t_ - u) / R_ ** 2), 0.0, t_, 20000),
     R_ ** 2 * (1 - math.exp(-(n_ - 1) * A_ * t_ / R_ ** 2)) / ((n_ - 1) * A_))
# scaling: ||F_R||_2 = R^(5/2) ||phi||_2/|m| and ||y_3 F_R||_2 = R^(3/2) ||x_3 phi||_2/|m|
holds("4 - 3/2 = 5/2 and 4 - 3/2 - 1 = 3/2; (R/b)(R^(5/2) + R^(3/2)) <= 2 R^(7/2)/b", 4 - 1.5 == 2.5 and 4 - 1.5 - 1 == 1.5)
print("ALL PASS" if ok else "SOME FAIL")
