"""PD08, second paper (arXiv 2611.06117), Section 3 (PDF pages 20 to 29): the explicit computations redone.

Standard library only. Every line prints PASS or FAIL; the last line is ALL PASS or FAILED n.
"""
import math
import random

fails = 0
count = 0


def line(name, ok, detail=""):
    global fails, count
    count += 1
    if not ok:
        fails += 1
    print("%s  %s  %s" % ("PASS" if ok else "FAIL", name, detail))


def simpson(f, a, b, n=2000):
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3


def close(a, b, tol=1e-6):
    return abs(a - b) <= tol * max(1.0, abs(a), abs(b))


random.seed(20261112)
SQ2 = math.sqrt(2.0)

# ---- Section 3.1, Lemma 3.1 ------------------------------------------------------------------------------
line("thresholds", 2 * 2.5 - 6 == -1 and 2 * 1.5 - 4 == -1,
     "r^(2 mu - 6) integrable at infinity iff mu < 5/2; r^(2 lambda - 4) iff lambda < 3/2")
ok = True
for j in range(0, 13):
    for k in range(0, 13):
        ok &= (1.5 * j + k - 4 * j + 1.5 * k == -2.5 * (j - k))
        ok &= (1.5 * j - 3 * j + 1.5 * k == -1.5 * (j - k))
        ok &= (1.5 * j - 3 * k + 1.5 * k == -1.5 * (k - j))
        ok &= (1.5 * j - 4 * j + 1.5 * k == -2.5 * (j - k) - k)
        ok &= (1.5 * j - 4 * k + 1.5 * k == -1.5 * (k - j) - k)
line("shell exponents", ok, "-5(j-k)/2 with cancellation, -3(j-k)/2 without, -3(k-j)/2 inward; heat-div: extra -k")
ok = True
for mu in (0.0, 1.0, 2.0, 2.4):
    out = sum(2.0 ** (-(2.5 - mu) * d) for d in range(3, 400))
    inw = sum(2.0 ** (-(1.5 + mu) * d) for d in range(3, 400))
    ok &= out < 1.0 / (1 - 2.0 ** (-(2.5 - mu))) and inw < 1.0
line("weighted shell sums", ok, "geometric for mu < 5/2")
m1 = max((s / 100.0) ** 1.5 * math.exp(-s / 100.0) for s in range(1, 4000))
m2 = max((s / 100.0) ** 2.5 * math.exp(-s / 100.0) for s in range(1, 4000))
line("heat kernel sup", close(m1, 1.5 ** 1.5 * math.exp(-1.5)) and close(m2, 2.5 ** 2.5 * math.exp(-2.5)),
     "s^(3/2) e^-s <= %.4f, s^(5/2) e^-s <= %.4f" % (m1, m2))


# ---- Section 3.2: profiles (3.6), the columns -------------------------------------------------------------
def Om(T, r):
    return T ** -2 * math.exp(-r * r / (4 * T))


def W(T, r):
    return r * Om(T, r)


def B(T, r):
    return 2 * (1 - r * r / (4 * T)) * Om(T, r)


ok = True
for T in (0.5, 2.0):
    for r in (0.3, 1.0, 2.5):
        h = 1e-5
        d = ((r + h) * W(T, r + h) - (r - h) * W(T, r - h)) / (2 * h) / r
        ok &= close(d, B(T, r), 1e-7)
line("(3.6) B_T", ok, "B_T = (1/r) d(r W_T)/dr")


def f2(t, x, y, l):
    T = l * l + t
    return x * T ** -2 * math.exp(-(x * x + y * y) / (4 * T))


def g1(t, z, b, l):
    D = b * b * l * l + 2 * t
    return b * l / math.sqrt(D) * math.exp(-z * z / (2 * D))


ok = True
h = 1e-3
for (t, x, y, l) in ((0.2, 0.7, -0.4, 1.0), (1.5, 1.1, 0.6, 0.5)):
    dt = (f2(t + h, x, y, l) - f2(t - h, x, y, l)) / (2 * h)
    lap = (f2(t, x + h, y, l) + f2(t, x - h, y, l) + f2(t, x, y + h, l) + f2(t, x, y - h, l) - 4 * f2(t, x, y, l)) / (h * h)
    ok &= abs(dt - lap) < 1e-5
for (t, z, b, l) in ((0.2, 0.9, 3.0, 1.0), (1.5, -2.0, 2.0, 0.5)):
    dt = (g1(t + h, z, b, l) - g1(t - h, z, b, l)) / (2 * h)
    lap = (g1(t, z + h, b, l) + g1(t, z - h, b, l) - 2 * g1(t, z, b, l)) / (h * h)
    ok &= abs(dt - lap) < 1e-5
line("heat evolution of one column", ok, "horizontal and vertical factors solve the heat equation; eta(0) is the Gaussian of variance b^2 l^2")
ok = True
for T in (0.3, 4.0):
    mx = max(r / 1000.0 * math.exp(-(r / 1000.0) ** 2 / (4 * T)) for r in range(1, 20000))
    ok &= close(mx, math.sqrt(2 * T) * math.exp(-0.5), 1e-5)
for D in (0.3, 4.0):
    mx = max(z / 1000.0 * math.exp(-(z / 1000.0) ** 2 / (2 * D)) for z in range(1, 20000))
    ok &= close(mx, math.sqrt(D) * math.exp(-0.5), 1e-5)
line("Gaussian suprema", ok, "sup r e^{-r^2/4T} = sqrt(2T) e^-1/2, sup |z| e^{-z^2/2D} = sqrt(D) e^-1/2")
ok = True
for (b, l, t) in ((1.0, 1.0, 0.0), (3.0, 0.2, 0.5), (10.0, 2.0, 7.0)):
    D = b * b * l * l + 2 * t
    T = l * l + t
    ok &= D >= T - 1e-15 and b * l / math.sqrt(D) <= 1 + 1e-15
    ok &= b * l * math.exp(-0.5) / D <= 1.0 / (b * l) + 1e-15
line("axial factor bounds", ok, "D >= T, b l/sqrt(D) <= 1, ||eta'||_inf = b l e^-1/2/D <= 1/(b l)")


def radii2(R, J=80):
    return [R ** (2.0 * j) for j in range(-J, J + 1)]


ok = True
worst = 0.0
for R in (2.0, 3.0, math.exp(2.0)):
    rr = radii2(R)
    for t in (1e-6, 0.37, 1.0, 5.0, 1e5):
        s = sum(2 * l2 / (l2 + t) ** 2 for l2 in rr)
        worst = max(worst, s * 3 * t / 16)
        ok &= s <= 16 / (3 * t)
line("(3.8) first bound", ok, "sum of c_coup <= 16A/(3t); largest ratio %.4f" % worst)

# ---- Lemma 3.2: (3.9), (3.10), the integral bound ---------------------------------------------------------
ok = True
for T in (0.5, 2.0):
    hs = 2 * simpson(lambda p: p * Om(T, p) ** 2, 0.0, 40.0, 8000)
    nb = simpson(lambda p: p * B(T, p) ** 2, 0.0, 40.0, 8000)
    sb = max(abs(B(T, r / 500.0)) for r in range(0, 20000))
    ok &= close(hs, 2 * T ** -3) and close(nb, 2 * T ** -3) and close(sb, 2 * T ** -2)
line("Hilbert-Schmidt and B_T norms", ok, "2 int rho Omega^2 = 2 T^-3; ||B_T||^2 in L^2(r dr) = 2 T^-3; sup |B_T| = 2 T^-2")

# a sample of the two operator bounds on a grid (cumulative trapezoid)
N = 6000
RMAX = 14.0
dr = RMAX / N
T = 0.8
vth = [(i * dr) * math.exp(-(i * dr) ** 2 / 1.7) * (1 + 0.5 * math.sin(3 * i * dr)) for i in range(N + 1)]
vz = [math.exp(-(i * dr) ** 2 / 2.3) * math.cos(2 * i * dr) for i in range(N + 1)]
pv = [0.0] * (N + 1)
for i in range(N - 1, -1, -1):
    a = 2 * Om(T, i * dr) * vth[i]
    b = 2 * Om(T, (i + 1) * dr) * vth[i + 1]
    pv[i] = pv[i + 1] - 0.5 * (a + b) * dr
n_p = math.sqrt(sum(pv[i] ** 2 * i * dr * dr for i in range(N + 1)))
n_v = math.sqrt(sum(vth[i] ** 2 * i * dr * dr for i in range(N + 1)))
line("pressure primitive bound", n_p <= SQ2 * T ** -1.5 * n_v, "||p_v|| = %.4f <= sqrt2 T^-3/2 ||v_theta|| = %.4f" % (n_p, SQ2 * T ** -1.5 * n_v))
n_z = math.sqrt(sum(vz[i] ** 2 * i * dr * dr for i in range(N + 1)))
cum = 0.0
worst = 0.0
for i in range(1, N + 1):
    cum += 0.5 * ((i - 1) * dr * vz[i - 1] + i * dr * vz[i]) * dr
    worst = max(worst, abs(cum) / (i * dr))
line("(3.10)", worst <= n_z / SQ2, "sup |v_r|/|k| = %.4f <= ||v_z||/sqrt2 = %.4f" % (worst, n_z / SQ2))
ok = True
for (l, hh, k) in ((1.0, 0.5, 2.0), (0.1, 3.0, 0.4), (5.0, 1e-2, 30.0)):
    # t = l^2 (e^w - 1): the integrands are peaked at t = 0 on the scale l^2, smooth in w
    wm = math.log(1 + hh / (l * l))
    tw = lambda w: l * l * (math.exp(w) - 1)
    jw = lambda w: l * l * math.exp(w)
    i1 = simpson(lambda w: 2 * l * l / (l * l + tw(w)) ** 2 * jw(w), 0.0, wm, 4000)
    i2 = simpson(lambda w: SQ2 * l * l * k / (l * l + tw(w)) ** 1.5 * jw(w), 0.0, wm, 4000)
    ok &= close(i1, 2 * hh / (l * l + hh)) and close(i2, 2 * SQ2 * l * k * (1 - l / math.sqrt(l * l + hh)))
    ok &= i2 <= 2 * SQ2 * l * k
line("one summand over an interval", ok, "2Ah/(l^2 + h) and at most 2 sqrt2 A l |k|")
c1 = 2 * SQ2 / (1 - 0.5) + 2 + 2 / (1 - 0.25)
c2 = 2 * SQ2 / (1 - 0.5) + 2 / (1 - 0.25)
line("constant parts", c1 < 12 and c2 < 12, "R >= 2: %.4f A and %.4f A, both below 12 A" % (c1, c2))


def exact_int(l2, k, s, hh):
    """integral over [s, s + hh] of min(c_coup, L |k|) for A = 1"""
    tc = 2.0 / (k * k) - l2
    a, b = s, s + hh
    tot = 0.0
    m = min(b, tc)
    if m > a:
        tot += 2 * SQ2 * l2 * abs(k) * (1 / math.sqrt(l2 + a) - 1 / math.sqrt(l2 + m))
    lo = max(a, tc)
    if b > lo:
        tot += 2 * l2 * (1 / (l2 + lo) - 1 / (l2 + b))
    return tot


ok = True
worst = 0.0
for R in (2.0, 3.0, math.exp(2.0)):
    rr = radii2(R, 60)
    for s in (0.0, 0.1, 5.0):
        for hh in (1e-3, 1.0, 1e3):
            for k in (1e-3, 0.1, 1.0, 30.0, 1e3):
                v = sum(exact_int(l2, k, s, hh) for l2 in rr)
                bd = 12 + 2 / math.log(R) * max(0.0, math.log(abs(k) * math.sqrt(hh)))
                worst = max(worst, v / bd)
                ok &= v <= bd
line("(3.8) second bound", ok, "exact integrals, 135 cases, R = 2, 3, e^2; largest ratio to the bound %.4f" % worst)

# ---- Lemma 3.3 ---------------------------------------------------------------------------------------------
ok = True
for z in (1.0, 3.0, 10.0):
    mx = max(4 * z * math.log(x / 1000.0) - (x / 1000.0) ** 2 / 2 for x in range(1000, 20000))
    ok &= close(mx, 2 * z * math.log(4 * z / math.e), 1e-5)
line("maximisation in |k| sqrt h", ok, "max of 4 zeta log x - x^2/2 is 2 zeta log(4 zeta/e), so Phi <= 2 log K_Q")
line("active set and d_Q", 64.0 / 3 <= 24, "u < 64A/(3 k^2); 64A/3 <= 24A <= d_Q")
ok = True
for (b, l, t) in ((2.0, 1.0, 0.3), (5.0, 0.2, 1.0)):
    D = b * b * l * l + 2 * t
    G = lambda q: b * l / math.sqrt(2 * math.pi) * math.exp(-D * q * q / 2)
    w = 12 / math.sqrt(D)
    i0 = simpson(G, -w, w, 4000)
    i1 = simpson(lambda q: abs(q) * G(q), -w, w, 4000)
    ok &= close(i0, b * l / math.sqrt(D)) and close(i1, math.sqrt(2 / math.pi) * b * l / D, 1e-5) and i0 <= 1
    # the kernel is (2 pi)^-1/2 times the unitary transform of eta
    q0 = 0.7
    ft = simpson(lambda z: math.cos(q0 * z) * g1(t, z, b, l), -12 * math.sqrt(D), 12 * math.sqrt(D), 4000) / (2 * math.pi)
    ok &= close(ft, G(q0), 1e-6)
line("convolution kernel G_l", ok, "int G = b l/sqrt(D) <= 1, int |q| G = sqrt(2/pi) b l/D")
ok = True
for (l, t) in ((1.0, 0.2), (0.3, 2.0)):
    T = l * l + t
    mx = max(l * l * W(T, r / 2000.0) for r in range(1, 40000))
    ok &= close(mx, SQ2 * l * l * T ** -1.5 / math.sqrt(math.e), 1e-5)
line("shear multiplier", ok, "sup A l^2 W_T = L_l/sqrt(e)")
ok = all(1 + K * (d + 2) + K / math.sqrt(math.e) <= K * (d + 4) for K in (1.0, 2.0, 1e6) for d in (0.0, 24.0, 300.0))
line("(3.16) constant", ok, "1 + K (d + 2) + K/sqrt(e) <= K (d + 4) for K >= 1")
ok = True
worst = 0.0
for R in (2.0, 3.0):
    for t in (1e-4, 1.0, 37.0):
        s = sum(math.sqrt(l2) / (l2 + t) ** 1.5 for l2 in radii2(R, 60))
        worst = max(worst, s * 3 * t / 10)
        ok &= s <= 10 / (3 * t)
for (b, l, t) in ((2.0, 1.0, 0.3), (5.0, 0.2, 1.0)):
    T = l * l + t
    D = b * b * l * l + 2 * t
    Lm = SQ2 * l * l / T ** 1.5 * math.sqrt(2 / math.pi) * b * l / D
    ok &= close(Lm, 2 / math.sqrt(math.pi) * b * l ** 3 / (T ** 1.5 * D)) and Lm <= 2 / (math.sqrt(math.pi) * b) * l / T ** 1.5 + 1e-15
line("(3.17)", ok, "L_l mu_l <= (2A/(sqrt(pi) b)) l (l^2 + t)^-3/2; sum <= 10/(3t), largest ratio %.4f" % worst)
ok = True
for _ in range(20000):
    b0v = random.uniform(0, 50)
    k = random.uniform(-10, 10)
    ok &= b0v - 0.5 * max(0.0, 2 * b0v - k * k / 2) <= k * k / 4 + 1e-12
line("(3.18) bracket", ok, "b_0 - (2 b_0 - k^2/2)_+/2 <= k^2/4, 20000 random cases")
ok = True
for eps in (0.0, 0.05, 0.125):
    kap = 0.25 - eps
    t = 1.7
    y = t ** 0.25 / kap
    dy = 0.25 * t ** -0.75 / kap
    ok &= close(dy, eps / t * y + t ** -0.75)
    ok &= close((4.0 / 3) * 2 * (eps + kap) / kap ** 2, 2 / (3 * kap ** 2))
line("(3.20)", ok, "E^1/2 <= K M t^1/4/kappa solves the comparison equation; int D <= 2 K^2 M^2 sqrt(t)/(3 kappa^2)")


def beta_num(a, b):
    left = simpson(lambda x: (1 / a) * (1 - x ** (1 / a)) ** (b - 1), 0.0, 0.5 ** a, 4000)
    right = simpson(lambda y: (1 / b) * (1 - y ** (1 / b)) ** (a - 1), 0.0, 0.5 ** b, 4000)
    return left + right


ok = True
for eps in (0.0, 0.125):
    kap = 0.25 - eps
    for bb in (0.5, 0.25):
        ok &= close(beta_num(kap, bb), math.gamma(kap) * math.gamma(bb) / math.gamma(kap + bb), 1e-5)
    ok &= close(eps + (-eps - 0.75 - 0.5 + 1), -0.25) and close(eps + (-eps - 0.75 - 0.75 + 1), -0.5)
line("Beta integrals", ok, "powers t^-1/4 and t^-1/2 with B(kappa, 1/2), B(kappa, 1/4)")
ok = all(min((t - s) / 2, t / (8 * (1 + A))) >= (t - s) / (8 * (1 + A)) - 1e-15
         for A in (1.0, 7.0) for t in (0.5, 3.0) for s in (0.01, 0.2, 0.49))
line("last interval and interpolation", ok and 0.25 * 1.5 + 0.75 * (1.5 - 2) == 0,
     "h_0 >= (t - s)/(8 (1 + A)); ||v||_inf <= C ||v||_2^1/4 ||grad^2 v||_2^3/4 is scale invariant")


# ---- the linearisations (3.9) and (3.19) by finite differences in Cartesian coordinates -------------------
def ddir(F, p, d, h=1e-5):
    a = F([p[i] + h * d[i] for i in range(3)])
    b = F([p[i] - h * d[i] for i in range(3)])
    return [(a[i] - b[i]) / (2 * h) for i in range(3)]


def vfield(p):
    x, y, z = p
    r = math.hypot(x, y)
    vr = r * r * math.exp(-r * r / 2) * math.cos(0.7 * z)
    vt = r * math.exp(-r * r / 3) * (1 + 0.5 * math.sin(z))
    vzz = math.exp(-r * r) * math.sin(1.1 * z)
    return [vr * x / r - vt * y / r, vr * y / r + vt * x / r, vzz], (vr, vt, vzz)


TT = 1.3


def Vswirl(p):
    x, y, z = p
    o = Om(TT, math.hypot(x, y))
    return [-o * y, o * x, 0.0]


ok = True
for p in ([0.7, 0.4, 0.3], [-0.5, 1.1, -0.8]):
    x, y, z = p
    r = math.hypot(x, y)
    v, (vr, vt, vzz) = vfield(p)
    V = Vswirl(p)
    lhs = [a + b for a, b in zip(ddir(lambda q: vfield(q)[0], p, V), ddir(Vswirl, p, v))]
    er = [x / r, y / r, 0.0]
    et = [-y / r, x / r, 0.0]
    rhs = [-2 * Om(TT, r) * vt * er[i] + B(TT, r) * vr * et[i] for i in range(3)]
    ok &= all(abs(lhs[i] - rhs[i]) < 1e-7 for i in range(3))
line("(3.9) linearisation", ok, "(V . grad) v + (v . grad) V = -2 Omega v_theta e_r + B_T v_r e_theta for axisymmetric v")


def OmQ(r, z):
    return math.exp(-r * r / 3 - z * z / 5) * (1 + 0.2 * z)


def Qf(p):
    x, y, z = p
    o = OmQ(math.hypot(x, y), z)
    return [-o * y, o * x, 0.0]


ok = True
for p in ([0.7, 0.4, 0.3], [-0.5, 1.1, -0.8]):
    x, y, z = p
    r = math.hypot(x, y)
    v, _ = vfield(p)
    Q = Qf(p)
    lhs = [a + b for a, b in zip(ddir(lambda q: vfield(q)[0], p, Q), ddir(Qf, p, v))]
    o = OmQ(r, z)
    dro = -(2 * r / 3) * o
    dzo = math.exp(-r * r / 3 - z * z / 5) * (0.2 - (2 * z / 5) * (1 + 0.2 * z))
    fac = dro * (x * v[0] + y * v[1]) / r + dzo * v[2]
    rhs = [2 * o * (-v[1]) + fac * (-y), 2 * o * v[0] + fac * x, 0.0]
    ok &= all(abs(lhs[i] - rhs[i]) < 1e-7 for i in range(3))
line("(3.19) linearisation", ok, "M_Q v = -[(Q . grad) v + (v . grad) Q] in the stated Cartesian form")

# ---- Proposition 3.4 ----------------------------------------------------------------------------------------
ok = True
for (l, lt, t, b, r, z) in ((1.0, 2.0, 0.3, 3.0, 0.8, 0.5), (0.25, 0.5, 1.0, 2.0, 1.4, -0.7)):
    T1, T2 = l * l + t, lt * lt + t
    e1, e2 = g1(t, z, b, l), g1(t, z, b, lt)

    def P(rr):
        return -2 * l * l * lt * lt / (T1 * T2 * (T1 + T2)) * e1 * e2 * math.exp(-rr * rr * (T1 + T2) / (4 * T1 * T2))

    h = 1e-5
    dP = (P(r + h) - P(r - h)) / (2 * h)
    q1 = l * l * e1 * W(T1, r)
    q2 = lt * lt * e2 * W(T2, r)
    ok &= close(dP, q1 * q2 / r, 1e-7)
line("(3.25)", ok, "d_r P = Q_theta Q~_theta/r, so (Q . grad) Q + grad P_Q = (d_z P_Q) e_z")
ok = True
for (D1, D2) in ((1.0, 1.0), (0.3, 5.0), (2.0, 2.5)):
    ok &= D1 * D2 / (D1 + D2) >= D1 / 2 - 1e-15
for sg in (0.4, 2.0):
    n2 = simpson(lambda z: (z / sg ** 2) ** 2 * math.exp(-z * z / sg ** 2), -12 * sg, 12 * sg, 4000)
    ok &= close(n2, math.sqrt(math.pi) / 2 / sg)
for (T1, T2) in ((0.5, 2.0), (1.0, 1.0)):
    n2 = simpson(lambda r: 2 * math.pi * r * math.exp(-r * r * (T1 + T2) / (2 * T1 * T2)), 0.0, 40.0, 8000)
    ok &= close(n2, 2 * math.pi * T1 * T2 / (T1 + T2))
line("norms in the residual bound", ok,
     "variance D D~/(D + D~) >= D/2; ||d_z Gaussian||^2 = sqrt(pi)/(2 sigma); horizontal norm^2 = 2 pi T T~/(T + T~)")


def fuv(u, v):
    return u ** 1.5 * v * v / (math.sqrt((1 + u * u) * (1 + v * v)) * (2 + u * u + v * v) ** 1.5)


ok = True
for (l, lt, t) in ((1.0, 2.0, 0.3), (0.25, 4.0, 9.0)):
    T1, T2 = l * l + t, lt * lt + t
    lhs = l ** 1.5 * lt ** 2 / (math.sqrt(T1 * T2) * (T1 + T2) ** 1.5)
    ok &= close(lhs, t ** -0.75 * fuv(l / math.sqrt(t), lt / math.sqrt(t)))
for i in range(-40, 41):
    for j in range(i, 41):
        u, v = 1.3 ** i, 1.3 ** j
        if v <= 1:
            bd = u ** 1.5 * v * v
        elif u <= 1:
            bd = u ** 1.5 / (v * v)
        else:
            bd = math.sqrt(u) / (v * v)
        ok &= fuv(u, v) <= bd * (1 + 1e-12)
line("f(u, v)", ok, "the rescaled factor is t^-3/4 f(u, v) and the three bounds hold with C = 1")
vals = []
for t in (1e-4, 1.0, 4.0, 37.0, 1e5):
    rs = [2.0 ** j / math.sqrt(t) for j in range(-45, 46)]
    s = 0.0
    for a in rs:
        for c in rs:
            s += fuv(min(a, c), max(a, c))
    vals.append(s)
line("(3.26)", max(vals) < 10 and close(vals[1], vals[2], 1e-9),
     "sum over ordered pairs, R = 2: %s (same at t and 4t)" % ", ".join("%.4f" % v for v in vals))
ok = True
for (L, M) in ((1.0, 0.125), (30.0, 1.0 / 7200), (5.0, 0.004)):
    ok &= 8 * L * L * M <= 1 + 1e-12
    rad = 2 * L * M
    ok &= L * (M + rad * rad) <= rad + 1e-15 and L * 2 * rad <= 0.5 + 1e-12
line("contraction", ok, "8 L^2 M <= 1: the ball of radius 2 L M is mapped into itself, Lipschitz constant 4 L^2 M <= 1/2")
ok = True
for (rho, A) in ((0.1, 5.0), (0.7, 2.0)):
    R = math.exp(rho * A)
    zeta = A / math.log(R)
    K1 = math.exp(12 * A + zeta * max(0.0, math.log(4 * zeta / math.e)))
    K2 = math.exp(12 * A + max(0.0, math.log(4 / (math.e * rho))) / rho)
    ok &= close(zeta, 1 / rho) and close(K1, K2, 1e-9)
line("K_Q for R = e^{rho A}", ok, "zeta_Q = 1/rho, K_Q = e^{12A + c_Q(rho)}")


def Qcol(l, b, t, p):
    x, y, z = p
    T = l * l + t
    o = l * l * g1(t, z, b, l) * Om(T, math.hypot(x, y))
    return [-o * y, o * x, 0.0]


ok = True
for (l, b, t, R, p) in ((1.0, 3.0, 0.2, 2.0, [0.3, -0.6, 0.9]), (8.0, 2.0, 5.0, 4.0, [1.0, 2.0, -3.0])):
    a = [R * c for c in Qcol(l, b, R * R * t, [R * c for c in p])]
    bq = Qcol(l / R, b, t, p)
    ok &= all(close(a[i], bq[i], 1e-10) for i in range(3))
I, J = 4, 3
ok &= sorted(j - 1 for j in range(-I, J + 1)) == list(range(-(I + 1), J))
line("(3.23) scaling", ok, "R Q_l(R^2 t, R x) = Q_{l/R}(t, x); radii -I..J become -(I+1)..(J-1)")
line("exponents", (-0.5 - 0.25 == -0.75) and (-0.5 + 0.25 == -0.25) and (1.5 * 4 / 3 == 2) and (1 - 0.75 == 0.25),
     "(3.28): t^-1/2 t^-1/4; Q e and e^2 are O(t^-1/4) in L^2; (3.29): Holder with 4/3 and 4")

# ---- the multiplier of Lemma 3.3 computed for a concrete array (A = 1 and 4, R = 2) -----------------------
RAD = [4.0 ** j for j in range(-30, 31)]


def b0(u, k, A):
    s = 0.0
    ak = abs(k)
    for l2 in RAD:
        T = l2 + u
        c = 2 * A * l2 / (T * T)
        L = SQ2 * A * l2 / T ** 1.5 * ak
        s += c if c < L else L
    return s


def Phi(t, k, A):
    k = abs(k)
    if k == 0.0 or 2 * b0(t, k, A) <= k * k / 2:
        return 0.0, t
    lo, hi = math.log(t), math.log(64 * A / (3 * k * k) * 1.0001)
    if hi <= lo:
        return 0.0, t
    a, b = lo, hi
    for _ in range(50):
        mid = 0.5 * (a + b)
        if 2 * b0(math.exp(mid), k, A) > k * k / 2:
            a = mid
        else:
            b = mid
    ustar = math.exp(a)
    val = simpson(lambda w: (2 * b0(math.exp(w), k, A) - k * k / 2) * math.exp(w), lo, a, 400)
    return val, ustar


ok1 = ok2 = ok3 = ok4 = True
supPhi = 0.0
supd = 0.0
lowd = 0.0
for A in (1.0, 4.0):
    zeta = A / math.log(2.0)
    logK = 12 * A + zeta * max(0.0, math.log(4 * zeta / math.e))
    dQ = 2 * logK
    K = math.exp(logK)
    for t in (1e-8, 1e-3, 1.0):
        store = {}
        for k in (0.05, 0.3, 1.0, 1.4, 2.0, 5.0, 20.0, 300.0):
            ph, us = Phi(t, k, A)
            store[k] = ph
            ok1 &= -1e-9 <= ph <= 2 * logK
            ok2 &= us <= 64 * A / (3 * k * k) * 1.001 or ph == 0.0
            hk = 0.01
            dp = (Phi(t, k * math.exp(hk), A)[0] - Phi(t, k * math.exp(-hk), A)[0]) / (2 * hk)
            ok3 &= -64 * A / 3 - 0.2 <= dp <= ph + 0.2 and abs(dp) <= dQ
            supPhi = max(supPhi, ph / (2 * logK))
            supd = max(supd, dp / dQ)
            lowd = min(lowd, dp / dQ)
        l2 = 1.0
        Tl = l2 + t
        c = 2 * A * l2 / Tl ** 2
        L = SQ2 * A * l2 / Tl ** 1.5
        ks = list(store.keys())
        for k in ks:
            for kp in ks:
                for sg in (1.0, -1.0):
                    if k == kp and sg > 0:
                        continue
                    Bl = min(c, L * max(k, kp))
                    lhs = Bl * abs(math.exp((store[k] - store[kp]) / 2) - 1)
                    ok4 &= lhs <= K * (dQ + 2) * L * abs(k - sg * kp)
line("(3.14) on a concrete array", ok1 and ok2, "0 <= Phi <= 2 log K_Q (largest Phi/(2 log K_Q) = %.3f); active set below 64A/(3 k^2)" % supPhi)
line("k d_k Phi", ok3, "-64A/3 <= k d_k Phi <= Phi, so |k d_k Phi| <= d_Q (range found %.3f d_Q to %.3f d_Q)" % (lowd, supd))
line("(3.15) on a concrete array", ok4, "B_l |m(k)/m(k') - 1| <= K_Q (d_Q + 2) L_l |k - k'|, both signs, l = 1")

print("%d lines" % count)
print("ALL PASS" if fails == 0 else "FAILED %d" % fails)
