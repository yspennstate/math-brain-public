"""Checks of the explicit computations in Sections 7.1 and 7.2 of arXiv 2611.06117 (standard library only)."""
import math
from fractions import Fraction as Fr

ok = True


def line(name, got, want, tol=1e-8):
    global ok
    good = abs(got - want) <= tol * max(1.0, abs(want))
    ok = ok and good
    print("%-88s got %.12g  stated %.12g  %s" % (name, got, want, "PASS" if good else "FAIL"))


def holds(name, cond):
    global ok
    ok = ok and bool(cond)
    print("%-88s %s" % (name, "PASS" if cond else "FAIL"))


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


# (7.1): t_f + R^2 s_* = R^2 t_p with d = t_f/R^2, s_* = t_p - d; and the size conditions, which need A large
# (R = e^{rho A} with rho = c_*/8 = 0.039 passes A^2 only near A = 300; they are checked at A = 400, Theta = 1)
A = 400.0
rho = math.sqrt(2) * math.exp(-1.5) / 8
R = math.exp(rho * A)
Theta = 1.0
tp = (2 + Theta * math.log(A)) / A
tf = tp + 16 * A * A
d = tf / R ** 2
line("t_f + R^2 (t_p - t_f/R^2) (= R^2 t_p), A = 400", (tf + R ** 2 * (tp - d)) / (R ** 2 * tp), 1.0)
holds("d < t_p/2, s_* > 3/A, t_* < R^2, A <= t_f, R >= A^2, t_f + 1 <= R^2/(2A) at A = 400",
      d < tp / 2 and tp - d > 3 / A and R ** 2 * tp < R ** 2 and A <= tf and R >= A * A and tf + 1 <= R ** 2 / (2 * A))

# (7.2), (7.3)
T = 2.3
Om = lambda r: T ** -2 * math.exp(-r * r / (4 * T))
B = lambda r: (2 - r * r / (2 * T)) * Om(r)
line("int_0^inf B_T^2 r dr at T = 2.3 (= 2 T^-3)", simpson(lambda r: B(r) ** 2 * r, 0.0, 60.0, 60000), 2 * T ** -3)
line("int_0^inf (1 - z)^2 e^{-2z} dz (= 1/4)", simpson(lambda z: (1 - z) ** 2 * math.exp(-2 * z), 0.0, 40.0, 40000), 0.25)
holds("max(2 Omega_T, |B_T|) <= 2 T^-2 for all r",
      all(max(2 * Om(i / 100), abs(B(i / 100))) <= 2 * T ** -2 + 1e-15 for i in range(6001)))
r = 1.7
line("r B_T = d_r (r^2 Omega_T) at r = 1.7", ((r + 1e-5) ** 2 * Om(r + 1e-5) - (r - 1e-5) ** 2 * Om(r - 1e-5)) / 2e-5, r * B(r), 1e-7)
# |v_r(r)| <= |k|/sqrt 2 ||v_z||: (1/r) (int_0^r u du)^(1/2) = 1/sqrt 2
line("(1/r) (int_0^r u du)^(1/2) (= 1/sqrt 2)", (r * r / 2) ** 0.5 / r, 1 / math.sqrt(2))

# the scaling of an old column into parent coordinates, (7.7)
A_, ell, R_, tf_ = 3.0, 0.2, 5.0, 48.3
s, y = 0.07, 0.9
x, t = R_ * y, tf_ + R_ ** 2 * s
phys = A_ * ell ** 2 * (ell ** 2 + t) ** -2 * math.exp(-x * x / (4 * (ell ** 2 + t))) * x
rho_j, tau_j = ell / R_, (tf_ + ell ** 2) / R_ ** 2
par = A_ * rho_j ** 2 * (tau_j + s) ** -2 * math.exp(-y * y / (4 * (tau_j + s))) * y
line("R u(R y, t_f + R^2 s) for an old column (= A rho^2 (tau + s)^-2 e^{..} y)", R_ * phys, par)

# Lemma 7.1: C A int_0^{1/A} s^(-1/4) ds = (4/3) A^(1/4); leading size s^(-5/4) at s = 1/A is A^(5/4)
line("A int_0^{1/A} s^(-1/4) ds at A = 400 (= (4/3) A^(1/4))", A * (4 / 3) * (1 / A) ** 0.75, 4 / 3 * A ** 0.25)

# B_*: int_0^inf (tau + s)^(-3/2) ds = 2 tau^(-1/2), and rho^2 tau^(-1/2) = l^2/(R sqrt(t_f + l^2))
line("rho^2 tau^(-1/2) (= l^2/(R sqrt(t_f + l^2)))", rho_j ** 2 * tau_j ** -0.5, ell ** 2 / (R_ * math.sqrt(tf_ + ell ** 2)))
# || r e^{-r^2/(cT)} ||_{L^2(R^2)} = (sqrt pi c/2) T
c = 3.0
num = math.sqrt(2 * math.pi * simpson(lambda r: r ** 3 * math.exp(-2 * r * r / (c * T)), 0.0, 60.0, 60000))
line("|| r e^{-r^2/(cT)} ||_{L^2(R^2)} at c = 3, T = 2.3 (= sqrt(pi) c T/2)", num, math.sqrt(math.pi) * c * T / 2)
# E_psi: int_0^inf s (d+s)^-3 ds = 1/(2d), int_0^inf s (d+s)^(-7/2) ds = (4/15) d^(-3/2); interpolation exponents
dd = 0.01
line("int_0^inf s (d + s)^-3 ds at d = 0.01 (= 1/(2d))",
     simpson(lambda w: math.exp(w) ** 2 * (dd + math.exp(w)) ** -3, -30.0, 30.0, 120000), 1 / (2 * dd), 1e-6)
line("int_0^inf s (d + s)^(-7/2) ds at d = 0.01 (= (4/15) d^(-3/2))",
     simpson(lambda w: math.exp(w) ** 2 * (dd + math.exp(w)) ** -3.5, -30.0, 30.0, 120000), 4 / 15 * dd ** -1.5, 1e-6)
de = Fr(1, 3)
holds("interpolation between H^4 and H^5: t_f exponent (1-de)(-1) + de(-3/2) = -1 - de/2, R exponent de",
      (1 - de) * (-1) + de * Fr(-3, 2) == -1 - de / 2)
holds("A^((j+3)/2) (1/A)^((j-1)/2) = A^2 for j = 1, 2, 3, 4", all(Fr(j + 3, 2) - Fr(j - 1, 2) == 2 for j in (1, 2, 3, 4)))

# dual radial weight: int |z|^(2 ze) (1 + r^2 + z^2)^(-9/4) dz = C (1 + r^2)^(ze - 7/4)
ze = 0.5
I = lambda r: 2 * simpson(lambda w: math.exp(w) ** (2 * ze + 1) * (1 + r * r + math.exp(2 * w)) ** -2.25, -40.0, 25.0, 130000)
line("ratio of int |z| (1 + r^2 + z^2)^(-9/4) dz at r = 2 and r = 0 (= 5^(-5/4))", I(2.0) / I(0.0), 5 ** -1.25, 1e-6)

# (7.17): the two weighted norms, times the stated power of T, stay bounded as T grows
for p0 in (1.25, 1.75):
    v1, v2 = [], []
    for Tt in (1.0, 10.0, 100.0, 1000.0):
        up = 40 * math.sqrt(Tt)
        n1 = simpson(lambda r: (r * Tt ** -2 * math.exp(-r * r / (4 * Tt))) ** 2 * (1 + r * r) ** -p0 * r, 0.0, up, 200000)
        n2 = simpson(lambda r: (r ** 3 * Tt ** -2 * math.exp(-r * r / (4 * Tt))) ** 2 * (1 + r * r) ** -p0 * r, 0.0, up, 200000)
        v1.append(math.sqrt(n1) * Tt ** (1 + p0 / 2))
        v2.append(math.sqrt(n2) * Tt ** (p0 / 2))
    holds("(7.17), p0 = %.2f: ||W_T|| T^(1+p0/2) in [%.3f, %.3f], ||r^3 ..|| T^(p0/2) in [%.3f, %.3f]"
          % (p0, min(v1), max(v1), min(v2), max(v2)), max(v1) < 5 and max(v2) < 5)

# (7.18): the three right sides solve the radial heat equations with the stated initial values
Tq = 1.4
W = lambda TT, r: r * TT ** -2 * math.exp(-r * r / (4 * TT))
f1 = lambda u, r: (8 * Tq * u / (Tq + u) + Tq * Tq * r * r / (Tq + u) ** 2) * W(Tq + u, r)
f0 = lambda u, r: (4 * u / (Tq + u) ** 2 + Tq * r * r / (Tq + u) ** 3) * math.exp(-r * r / (4 * (Tq + u)))
line("second line of (7.18) at u = 0, r = 1.3 (= r^3 T^-2 e^{-r^2/(4T)})", f1(0.0, 1.3), 1.3 ** 3 * Tq ** -2 * math.exp(-1.69 / (4 * Tq)))
line("third line of (7.18) at u = 0, r = 1.3 (= r^2 T^-2 e^{-r^2/(4T)})", f0(0.0, 1.3), 1.69 * Tq ** -2 * math.exp(-1.69 / (4 * Tq)))
h = 1e-3
for (name, f, m) in (("second", f1, 1.0), ("third", f0, 0.0)):
    worst = 0.0
    for (u, r) in ((0.3, 0.7), (1.1, 2.4), (2.5, 0.2)):
        du = (f(u + h, r) - f(u - h, r)) / (2 * h)
        lap = (f(u, r + h) - 2 * f(u, r) + f(u, r - h)) / h ** 2 + (f(u, r + h) - f(u, r - h)) / (2 * h * r) - m * f(u, r) / r ** 2
        worst = max(worst, abs(du - lap))
    holds("%s line of (7.18) solves d_u f = (d_r^2 + d_r/r - %d/r^2) f (largest residual %.2e)" % (name, int(m), worst), worst < 1e-5)
rr, TT = 1.9, 2.2
dW = (W(TT + 1e-6, rr) - W(TT - 1e-6, rr)) / 2e-6
line("4 T^2 d_T W_T + 8 T W_T at r = 1.9, T = 2.2 (= r^2 W_T)", 4 * TT * TT * dW + 8 * TT * W(TT, rr), rr * rr * W(TT, rr), 1e-7)
P = lambda Tv: Tv ** -1 * math.exp(-rr * rr / (4 * Tv))
dP = (P(TT + 1e-6) - P(TT - 1e-6)) / 2e-6
line("4 T d_T P_T + 4 P_T (= r^2 T^-2 e^{-r^2/(4T)})", 4 * TT * dP + 4 * P(TT), rr * rr * TT ** -2 * math.exp(-rr * rr / (4 * TT)), 1e-7)

# the time integral of the leading term and the constant in c_mean
L = 3.0
num = simpson(lambda w: math.exp(w) * W(L + 2 * math.exp(w), rr), -30.0, 25.0, 110000)
line("int_0^inf W_{L+2u}(r) du at L = 3, r = 1.9 (= (2/r)(1 - e^{-r^2/(4L)}))", num, 2 / rr * (1 - math.exp(-rr * rr / (4 * L))), 1e-6)
line("8 pi sqrt(2 pi)/2 (= 4 pi sqrt(2 pi), the constant of (7.10))", 8 * math.pi * math.sqrt(2 * math.pi) / 2, 4 * math.pi * math.sqrt(2 * math.pi))

# moment exponents: H = R^2/(2A); H^(-7/8) and R^-2 H^(1/8) are R^(-7/4) up to powers of A
holds("2 (7/8) = 7/4 and 2 - 2 (1/8) = 7/4; 1 + 7/8 = 15/8 is the norm exponent of W_T at p0 = 7/4",
      2 * Fr(7, 8) == Fr(7, 4) and 2 - 2 * Fr(1, 8) == Fr(7, 4) and 1 + Fr(7, 4) / 2 == Fr(15, 8))
Hh, Ll = 5000.0, 3.0
holds("int_H^inf (L + 2u)^(-15/8) du = (4/7)(L + 2H)^(-7/8); over [0, H]: 8 2^(-15/8) H^(1/8) bounds the first, the second is 4((L+2H)^(1/8) - L^(1/8))",
      abs(simpson(lambda w: math.exp(w) * (Ll + 2 * math.exp(w)) ** -1.875, math.log(Hh), 60.0, 100000) - 4 / 7 * (Ll + 2 * Hh) ** -0.875) < 1e-9
      and simpson(lambda u: u * (Ll + 2 * u) ** -1.875, 0.0, Hh, 200000) <= 8 * 2 ** -1.875 * Hh ** 0.125
      and abs(simpson(lambda u: (Ll + 2 * u) ** -0.875, 0.0, Hh, 200000) - 4 * ((Ll + 2 * Hh) ** 0.125 - Ll ** 0.125)) < 1e-6)

# c_mean(k) - c_mean(0): the radial dual integral int (1 - e^{-r^2/(4L)})^2 r^-1 (1 + r^2)^(-1/4) dr is at most C L^(-1/4)
vals = []
for Lv in (1.0, 10.0, 100.0, 1e4):
    g = lambda w: (1 - math.exp(-math.exp(2 * w) / (4 * Lv))) ** 2 * (1 + math.exp(2 * w)) ** -0.25
    vals.append(simpson(g, -20.0, 40.0, 120000) * Lv ** 0.25)
holds("L^(1/4) int (1 - e^{-r^2/(4L)})^2 (1 + r^2)^(-1/4) dr/r for L = 1, 10, 100, 1e4 in [%.3f, %.3f]" % (min(vals), max(vals)), max(vals) < 4)

# |k| > K A: int_0^inf 2 A rho^2 (tau + s)^-2 ds = 2 A l^2/(t_f + l^2); ||F_R||_2 = R^(5/2) ||phi||_2/|m|
line("2 A rho^2/tau (= 2 A l^2/(t_f + l^2))", 2 * A_ * rho_j ** 2 / tau_j, 2 * A_ * ell ** 2 / (tf_ + ell ** 2))
holds("R^4 R^(-3/2) = R^(5/2); R^4 R^-1 = R^3 for the fibers (7.8)", Fr(4) - Fr(3, 2) == Fr(5, 2) and 4 - 1 == 3)
print("ALL PASS" if ok else "SOME FAIL")
