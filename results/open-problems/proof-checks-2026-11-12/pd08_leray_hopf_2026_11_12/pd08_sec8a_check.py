"""Checks of the exponent arithmetic on pages 93 to 95 of arXiv 2611.06117, (8.13) to (8.26) (standard library only)."""
import math
import random

ok = True


def line(name, got, want, tol=1e-9):
    global ok
    good = abs(got - want) <= tol * max(1.0, abs(want))
    ok = ok and good
    print("%-100s got %.12g  stated %.12g  %s" % (name, got, want, "PASS" if good else "FAIL"))


def holds(name, cond):
    global ok
    ok = ok and bool(cond)
    print("%-100s %s" % (name, "PASS" if cond else "FAIL"))


cs = math.sqrt(2) * math.exp(-1.5)
rho = cs / 8
sst, gam, rc = 19 / 8, rho / 4, 3 * rho / 8
xlo, xhi = 12 * rho, 13 * rho + rho / 32

line("2 c_* in units of rho (= 16), so x <= 13 rho + rho/32 < 2 c_*", 2 * cs / rho, 16.0)
line("rho - 2x + 2 c_* at x = 12 rho, in units of rho (= -7)", (rho - 2 * xlo + 2 * cs) / rho, -7.0)
g = True
for k in range(1, 200):
    om = (rho / 64) * k / 200
    G = cs - om
    for j in range(0, 41):
        x = xlo + (xhi - xlo) * j / 40
        r1 = x + 2.5 * rho - 2 * G
        r2 = -x + 3 * cs + 2.5 * rho - 2 * G
        r3 = -2 * x + 4 * cs + 3.5 * rho - 2 * G
        g = g and r1 <= -15 * rho / 32 + 2 * om + 1e-15 and r2 <= -1.5 * rho + 2 * om + 1e-15 and r3 <= -4.5 * rho + 2 * om + 1e-15
        g = g and r1 < -13 * rho / 32 and 7.5 * rho - 2 * x + 4 * cs - 2 * G <= -rho / 2 + 2 * om + 1e-15
        xi = (2.5 - sst) * rho + x - 2 * G + 2 * rho
        g = g and xi + gam <= -19 * rho / 32 + 2 * om + 1e-15 and -19 * rho / 32 + 2 * om < 0
    g = g and 13 * rho / 32 < 15 * rho / 32 - 2 * om and 13 * rho / 32 > rc
    g = g and rho / 8 + 2 * om < 5 * rho / 32 < gam
holds("(8.17) rates and their bounds on 12 rho <= x <= 13 rho + rho/32; Lemma 7.8 hypotheses; (8.26) margins", g)
om = rho / 100
G = cs - om
line("x + (5/2) rho - 2G at x = 13 rho + rho/32, in units of rho (= -15/32 + 2 omega/rho)", (xhi + 2.5 * rho - 2 * G) / rho, -15 / 32 + 2 * om / rho)
line("-x + 3 c_* + (5/2) rho - 2G at x = 12 rho (= -3/2 + 2 omega/rho)", (-xlo + 3 * cs + 2.5 * rho - 2 * G) / rho, -1.5 + 2 * om / rho)
line("-2x + 4 c_* + (7/2) rho - 2G at x = 12 rho (= -9/2 + 2 omega/rho)", (-2 * xlo + 4 * cs + 3.5 * rho - 2 * G) / rho, -4.5 + 2 * om / rho)
line("xi_lin + gamma at x = 13 rho + rho/32 (= -19/32 + 2 omega/rho)", ((2.5 - sst) * rho + xhi - 2 * G + 2 * rho + gam) / rho, -19 / 32 + 2 * om / rho)
line("2 rho - 24 rho + 16 rho in units of rho (= -6)", (2 * rho - 2 * xlo + 2 * cs) / rho, -6.0)
line("delta_A B_mom exponent: -rho_c + gamma in units of rho (= -1/8)", (-rc + gam) / rho, -1 / 8)
holds("powers of R: -1/2 + 3 = 5/2; 1 - 1/2 + 3 = 7/2; 3 - s_* - 1/2 = 5/2 - s_* = 1/8; 1 - s - 3/2 = -s - 1/2",
      -0.5 + 3 == 2.5 and 1 - 0.5 + 3 == 3.5 and 3 - sst - 0.5 == 2.5 - sst == 1 / 8)

# (8.18) in a finite-dimensional model: g a unit vector, h_out = -A_lead g + r
random.seed(11)
n = 7
gv = [random.gauss(0, 1) for _ in range(n)]
ng = math.sqrt(sum(v * v for v in gv)); gv = [v / ng for v in gv]
r = [0.05 * random.gauss(0, 1) for _ in range(n)]
Al = 0.9
hout = [-Al * a + b for a, b in zip(gv, r)]
rg = sum(a * b for a, b in zip(r, gv))
Aamp = -sum(a * b for a, b in zip(hout, gv))
line("A = -<h_out, g> (= A_lead - <r_out, g>)", Aamp, Al - rg)
F = [-v / Aamp for v in hout]
err = max(abs((F[i] - gv[i]) - (rg * gv[i] - r[i]) / Aamp) for i in range(n))
holds("F - g = (<r_out, g> g - r_out)/A and <F, g> = 1", err < 1e-14 and abs(sum(a * b for a, b in zip(F, gv)) - 1) < 1e-14)

# the heat matrix on [t_f, t_*]: A/t_f, A t_p, A t_p/R^2
A = 400.0
Th = 1.0
tp = (2 + Th * math.log(A)) / A
tf = tp + 16 * A * A
R2 = math.exp(2 * rho * A)
ts = R2 * tp
line("int_{t_f}^{t_*} A R^2/(R^2 + t)^2 dt (= A R^2 (1/(R^2 + t_f) - 1/(R^2 + t_*)), at most A t_p)",
     A * R2 * (1 / (R2 + tf) - 1 / (R2 + ts)), A * R2 * (ts - tf) / ((R2 + tf) * (R2 + ts)))
holds("that integral <= A t_p = 2 + Theta log A; int_{t_f}^inf A/t^2 = A/t_f <= 1/(16 A)",
      A * R2 * (1 / (R2 + tf) - 1 / (R2 + ts)) <= A * tp and abs(A * tp - (2 + Th * math.log(A))) < 1e-9 and A / tf <= 1 / (16 * A))

# pages 96 to 98
line("exponent of |eps| eta^(-13/4) at |eps| = a_+, in units of rho (= -35/4)", -12 + 13 / 4, -35 / 4)
line("exponent of |eps| eta^(-13/2) at |eps| = a_+, in units of rho (= -11/2)", -12 + 13 / 2, -11 / 2)
holds("eta^-2 J_1(x/sqrt eta): j-th derivative in L^2 scales as eta^(-2 - j/2 + 3/4) = eta^(-5/4 - j/2); j = 4: 13/4; j = 5: 15/4 <= 4",
      -2 - 4 / 2 + 3 / 4 == -13 / 4 and -2 - 5 / 2 + 3 / 4 == -15 / 4 and 15 / 4 <= 4)
holds("s_* + chi_seed = 39/16 < 5/2; chi beta > 6 rho gives 4 rho - chi beta < -2 rho; chi = 1/16 < 1/2",
      sst + 1 / 16 == 39 / 16 < 2.5 and 4 * rho - 6.0001 * rho < -2 * rho and 1 / 16 < 0.5)


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


lam = 37.0
line("int_0^inf s^(-1/2) e^{-lam s} ds at lam = 37 (= sqrt(pi/lam))", simpson(lambda w: 2 * math.exp(-lam * w * w), 0.0, 3.0, 60000), math.sqrt(math.pi / lam))
# tail |x|^-4 in three dimensions: the moment of order mu is finite iff 2 mu - 8 + 2 < -1, i.e. mu < 5/2
for mu, T in ((2.4, 1 / (5 - 2 * 2.4)),):
    line("int_1^inf r^(2 mu - 6) dr at mu = 2.4 (= 1/(5 - 2 mu))", simpson(lambda w: math.exp(w * (2 * mu - 5)), 0.0, 400.0, 400000), T, 1e-6)
holds("the same integral diverges at mu = 5/2 (integrand 1/r)", 2 * 2.5 - 6 == -1)
A2 = 400.0
tp2 = (2 + math.log(A2)) / A2
Kc = 3.0
line("e^{K (A+1) t_p} at K = 3, A = 400, Theta = 1 (= (e^2 A)^(K (1 + 1/A)))", math.exp(Kc * (A2 + 1) * tp2), (math.e ** 2 * A2) ** (Kc * (1 + 1 / A2)))
lamb, dg = 0.3, 0.04
gg = [1.0, 0.0, 0.0]
dvec = [dg, 0.02, -0.01]
diff = [-lamb * (gg[i] + dvec[i]) for i in range(3)]
Bj = -sum(diff[i] * gg[i] for i in range(3))
line("B_J(lam) = -<u - ubar, g> (= lam (1 + <d, g>))", Bj, lamb * (1 + dg))
Fj = [-diff[i] / Bj for i in range(3)]
holds("F_J - g = (d - <d, g> g)/(1 + <d, g>)", max(abs((Fj[i] - gg[i]) - (dvec[i] - dg * gg[i]) / (1 + dg)) for i in range(3)) < 1e-15)
print("ALL PASS" if ok else "SOME FAIL")
