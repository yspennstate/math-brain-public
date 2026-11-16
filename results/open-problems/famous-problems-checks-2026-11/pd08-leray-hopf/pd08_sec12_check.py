# Checks for Sections 1 and 2 (PDF pages 1 to 19) of arXiv 2611.06117v1. Standard library only; reads no file.
import math, random

res = []
def chk(name, ok, detail=""):
    res.append(ok)
    print(("PASS " if ok else "FAIL ") + name + ((" | " + detail) if detail else ""), flush=True)

def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3

# 1. ||Q_l(0)||_2^2 = 4 pi^{3/2} A^2 b l  (page 5)
for (A, b, l) in [(3.0, 5.0, 1.0), (2.0, 7.0, 0.25), (1.5, 2.0, 4.0)]:
    rad = simpson(lambda r: r ** 3 * math.exp(-r * r / (2 * l * l)), 0.0, 14 * l)
    ax = simpson(lambda z: math.exp(-z * z / (b * b * l * l)), -12 * b * l, 12 * b * l)
    num = (A * A / l ** 4) * 2 * math.pi * rad * ax
    ex = 4 * math.pi ** 1.5 * A * A * b * l
    chk("norm of one swirl, A=%g b=%g l=%g" % (A, b, l), abs(num / ex - 1) < 1e-8, "%.10g vs %.10g" % (num, ex))

# 2. geometric sum of the norms over radii R^-n
A, b, R = 2.0, 3.0, 4.0
s = sum(math.sqrt(4 * math.pi ** 1.5 * A * A * b * R ** (-n)) for n in range(200))
ex = math.sqrt(4 * math.pi ** 1.5 * A * A * b) / (1 - R ** -0.5)
chk("sum of the L2 norms over the radii is a geometric series", abs(s / ex - 1) < 1e-12)

# 3. Rayleigh discriminant of r e^{-r^2/4}
def rU2(r): return (r * r * math.exp(-r * r / 4)) ** 2
ok = True
for r in [0.3, 1.0, 2.0, 2.4495, 3.7]:
    h = 1e-5
    d = (rU2(r + h) - rU2(r - h)) / (2 * h) / r ** 3
    ok = ok and abs(d - (4 - r * r) * math.exp(-r * r / 2)) < 1e-7
chk("(1/r^3) d/dr (r U)^2 = (4 - r^2) e^{-r^2/2}", ok)
Phi = lambda r: (r * r - 4) * math.exp(-r * r / 2)
best = max((Phi(i * 1e-4), i * 1e-4) for i in range(1, 100000))
chk("potential (r^2 - 4) e^{-r^2/2}: maximum 2 e^-3 at r = sqrt 6",
    abs(best[0] - 2 * math.exp(-3)) < 1e-9 and abs(best[1] - math.sqrt(6)) < 2e-4, "max %.10g at %.5f" % best)
cstar = math.sqrt(2) * math.exp(-1.5)
chk("c_* = sqrt 2 e^{-3/2} = sqrt(2 e^-3)", abs(cstar - math.sqrt(2 * math.exp(-3))) < 1e-15, "c_* = %.8f" % cstar)

# 4. U_d = A r T^-2 e^{-r^2/(4T)} e_theta solves u_t = u_rr + u_r/r - u/r^2 (page 5, 13)
def u(t, r):
    T = 1 + t
    return r * T ** -2 * math.exp(-r * r / (4 * T))
ok = True
for (t, r) in [(0.0, 0.7), (0.5, 1.9), (2.0, 3.1), (0.1, 0.2)]:
    h = 1e-3
    ut = (u(t + h, r) - u(t - h, r)) / (2 * h) if t > h else (u(t + h, r) - u(t, r)) / h
    if t <= h:
        ut = (-3 * u(t, r) + 4 * u(t + h, r) - u(t + 2 * h, r)) / (2 * h)
    urr = (u(t, r + h) - 2 * u(t, r) + u(t, r - h)) / (h * h)
    ur = (u(t, r + h) - u(t, r - h)) / (2 * h)
    ok = ok and abs(ut - (urr + ur / r - u(t, r) / (r * r))) < 2e-5
chk("the swirl W_T solves the azimuthal heat equation", ok)

# 5. (1/r^3) d_r (r U_d)^2 = A^2 T^-4 (4 - r^2/T) e^{-r^2/(2T)} (page 14)
ok = True
A = 3.0
for (T, r) in [(1.0, 1.3), (2.5, 3.0), (4.0, 4.0), (1.7, 0.4)]:
    f = lambda x: (A * x * x * T ** -2 * math.exp(-x * x / (4 * T))) ** 2
    h = 1e-5
    d = (f(r + h) - f(r - h)) / (2 * h) / r ** 3
    ok = ok and abs(d - A * A * T ** -4 * (4 - r * r / T) * math.exp(-r * r / (2 * T))) < 1e-6
chk("discriminant of the evolving swirl, sign change at r = 2 sqrt T", ok)

# 6. (2.4): 2 Omega_1 B_1 = (4 - r^2) e^{-r^2/2}; B_1 is the vorticity of r e^{-r^2/4}
ok = True
for r in [0.2, 1.0, 2.0, 3.3]:
    Om = math.exp(-r * r / 4); B1 = (2 - r * r / 2) * math.exp(-r * r / 4)
    ok = ok and abs(2 * Om * B1 - (4 - r * r) * math.exp(-r * r / 2)) < 1e-14
    h = 1e-5
    g = lambda x: x * x * math.exp(-x * x / 4)
    ok = ok and abs((g(r + h) - g(r - h)) / (2 * h) / r - B1) < 1e-8
chk("(2.4): -2 k^2 Omega_1 B_1 = -k^2 (4 - r^2) e^{-r^2/2}, B_1 = (1/r)(r U)'", ok)

# 7. Duhamel integral on page 13: int_0^t (t/s)^eps s^{-3/4} ds = t^{1/4}/(1/4 - eps); s = w^8 removes the singularity
ok = True
for (t, eps) in [(1.0, 0.1), (0.3, 0.2), (5.0, 0.01), (2.0, 0.24)]:
    m = 2 / (0.25 - eps)          # s = w^m: the integrand becomes t^eps m w^{m(1/4 - eps) - 1} = t^eps m w
    f = lambda w: t ** eps * m * w ** (m * (0.25 - eps) - 1)
    num = simpson(f, 0.0, t ** (1 / m), 2000)
    ex = t ** 0.25 / (0.25 - eps)
    ok = ok and abs(num / ex - 1) < 2e-3
chk("Duhamel integral with the propagator exponent eps_Q < 1/4", ok)

# 8. the growth clock: int_{tp}^{t} (1+s)^-2 ds = 1/(1+tp) - 1/(1+t)
tp, t = 0.37, 9.0
num = simpson(lambda x: (1 + x) ** -2, tp, t)
chk("growth clock Gamma_src", abs(num - (1 / (1 + tp) - 1 / (1 + t))) < 1e-10)

# 9. time alignment: l_n^2 t_* = T_{n-1} with t_* = R^2 t_p, T_n = l_n^2 t_p
ok = True
for (R, A, Th) in [(7.0, 50.0, 3.0), (1e3, 200.0, 1.0)]:
    tp = (2 + Th * math.log(A)) / A
    for n in range(1, 6):
        ln = R ** -n
        ok = ok and abs(ln * ln * R * R * tp / ((R ** (-(n - 1))) ** 2 * tp) - 1) < 1e-12
chk("consecutive transitions meet at the same physical time", ok)

# 10. symbol identity -i P(xi) diag(1,1,0) xi = i xi_z P(xi) e_z (page 16); real parts compared after removing i
random.seed(5)
ok = True
for _ in range(50):
    xi = [random.uniform(-3, 3) for _ in range(3)]
    n2 = sum(x * x for x in xi)
    P = [[(1.0 if i == j else 0.0) - xi[i] * xi[j] / n2 for j in range(3)] for i in range(3)]
    v = [xi[0], xi[1], 0.0]
    lhs = [-sum(P[i][j] * v[j] for j in range(3)) for i in range(3)]
    rhs = [xi[2] * P[i][2] for i in range(3)]
    ok = ok and max(abs(lhs[i] - rhs[i]) for i in range(3)) < 1e-12
chk("symbol identity for the anisotropic stress", ok)

# 11. exponents at the two crossings (page 18) and the transfer error (page 16), for sample rho, omega
ok = True
for frac in [0.1, 0.5, 0.99]:
    rho = cstar / 8
    om = frac * rho / 64          # 2 omega < rho/32
    G = cstar - om
    up_minus = (2 * cstar - 3 * rho) - (13 * rho + rho / 32)      # upper bound for A(a_-)/a_-
    lo_plus = (2 * G - 3 * rho) - 12 * rho                         # lower bound for A(a_+)/a_+
    ok = ok and abs(up_minus + rho / 32) < 1e-15 and abs(lo_plus - (rho - 2 * om)) < 1e-15 and lo_plus > 0
    ok = ok and (-7 * rho / 4 + 2 * om) < 0
chk("crossing exponents -rho/32 and rho - 2 omega; transfer error exponent negative", ok,
    "rho = %.6f" % (cstar / 8))

# 12. scaling of the seed: || l^-1 F(x/l) ||_2 = l^{1/2} ||F||_2, with F a Gaussian (radial integral)
ok = True
for l in [0.5, 0.01]:
    n1 = 4 * math.pi * simpson(lambda r: r * r * math.exp(-r * r), 0.0, 12.0)
    n2 = 4 * math.pi * simpson(lambda r: r * r * (math.exp(-(r / l) ** 2 / 2) / l) ** 2, 0.0, 12.0 * l)
    ok = ok and abs(n2 / (l * n1) - 1) < 1e-8
chk("seed scaling l^{1/2}", ok)

# 13. interpolation exponent behind the mixed-norm range: t^{-(1-3/q) p/2} integrable at 0 iff 2/p + 3/q > 1
ok = True
for (p, q) in [(1.5, 1e9), (2.0, 1e9), (4.0, 6.0), (4.0, 5.9), (3.0, 9.0), (2.9, 9.0), (1.0, 1e9)]:
    integrable = (1 - 3 / q) * p / 2 < 1
    ok = ok and (integrable == (2 / p + 3 / q > 1 + 1e-12))
chk("mixed-norm range (1.6) is the integrability range of (9.18), q = infinity needs p < 2", ok)

print("%d checks, %d pass" % (len(res), sum(res)), flush=True)
print("ALL PASS" if all(res) else "SOME FAIL", flush=True)
