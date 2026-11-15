"""Checks of the explicit computations on PDF pages 99 to 101 of arXiv 2611.06117: Lemma 8.3, (9.1) to (9.10)
(standard library only)."""
import math

ok = True


def line(name, got, want, tol=1e-8):
    global ok
    good = abs(got - want) <= tol * max(1.0, abs(want))
    ok = ok and good
    print("%-104s got %.12g  stated %.12g  %s" % (name, got, want, "PASS" if good else "FAIL"))


def holds(name, cond):
    global ok
    ok = ok and bool(cond)
    print("%-104s %s" % (name, "PASS" if cond else "FAIL"))


def simpson(f, a, b, n=20000):
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += f(a + i * h) * (4 if i % 2 else 2)
    return s * h / 3


# Lemma 8.3 in a model: a continuous transition map with A(a_-) < a_- and A(a_+) > a_+ that is not monotone
am, ap = 1.0, 2.0
clip = lambda v: min(ap, max(am, v))
step = lambda a, j: a + 0.9 * (a - 1.5) + 0.35 * math.sin(7 * a + j)   # at 1: 0.55 +- 0.35 < 1; at 2: 2.45 +- 0.35 > 2
holds("model transition: output below a_- at a_- and above a_+ at a_+ for every stage",
      all(step(am, j) < am and step(ap, j) > ap for j in range(6)))


def terminal(lam, N=6, clipped=True):
    a = clip(2 * lam) if clipped else 2 * lam
    hit = False
    for j in range(N):
        v = step(a, j)
        if clipped:
            hit = hit or not (am < v < ap)
            a = clip(v)
        else:
            a = v
    return a, hit


lo, hi = am / 2, ap / 2 * 1.0   # initial amplitude 2 lam: a_- at lam = a_-/2, a_+ at lam = a_+/2
holds("clipped terminal amplitude is a_- at the left end and a_+ at the right end", terminal(lo)[0] == am and terminal(hi)[0] == ap)
target = 1.37
for _ in range(200):
    mid = (lo + hi) / 2
    if terminal(mid)[0] < target:
        lo = mid
    else:
        hi = mid
tv, hit = terminal(lo)
holds("bisection finds a parameter with terminal value 1.37 and no clipping acted on that orbit", abs(tv - target) < 1e-9 and not hit)
line("the unclipped orbit from the same parameter has the same terminal value", terminal(lo, clipped=False)[0], tv, 1e-9)

# ||Q_l(0)||_q = C_q A b^(1/q) l^(3/q - 1): ratio of the norms at two (l, b) pairs, radial-axial quadrature
def qnorm(l, b, q, A=1.0):
    # |Q| = (A/l^2) r exp(-r^2/(4 l^2) - z^2/(2 b^2 l^2)); integral over r dr dtheta dz factorises
    ir = simpson(lambda r: r * (r / l ** 2 * math.exp(-r * r / (4 * l * l))) ** q, 0.0, 30 * l, 6000)
    iz = simpson(lambda z: math.exp(-q * z * z / (2 * b * b * l * l)), -30 * b * l, 30 * b * l, 6000)
    return (A ** q * 2 * math.pi * ir * iz) ** (1 / q)


for q in (1.0, 2.0, 2.5):
    line("||Q_l||_q ratio between (l, b) = (0.3, 5) and (1, 2), q = %.1f (= (5/2)^(1/q) 0.3^(3/q - 1))" % q,
         qnorm(0.3, 5.0, q) / qnorm(1.0, 2.0, q), (5 / 2) ** (1 / q) * 0.3 ** (3 / q - 1), 1e-7)
holds("3/q - 1 > 0 exactly for q < 3", 3 / 2.99 - 1 > 0 and 3 / 3 - 1 == 0)
line("max of s^4 e^{-s^2/4} (at s^2 = 8, = 64 e^-2)", max((0.001 * k) ** 4 * math.exp(-(0.001 * k) ** 2 / 4) for k in range(1, 20000)), 64 * math.exp(-2), 1e-6)
R = 4.7
for rho_ in (0.013, 0.4, 1.0):
    s1 = sum(R ** (2 * n) for n in range(0, 80) if R ** -n >= rho_)
    s2 = sum(R ** (-2 * n) for n in range(0, 80) if R ** -n < rho_)
    holds("rho = %.3f: sum_{l_n >= rho} l_n^-2 <= rho^-2/(1 - R^-2) and sum_{l_n < rho} l_n^2 <= rho^2/(1 - R^-2)" % rho_,
          s1 <= rho_ ** -2 / (1 - R ** -2) * (1 + 1e-12) and s2 <= rho_ ** 2 / (1 - R ** -2) * (1 + 1e-12))
holds("exponent |x_h|^2/(4 l^2) + z^2/(2 b^2 l^2) >= rho^2/(4 l^2) since 1/2 >= 1/4; |x_h| <= rho", 0.5 >= 0.25)
bb, aa = 3.0, 0.7
line("volume of the ellipsoid rho < a, b = 3, a = 0.7 (= 4 pi b a^3/3)",
     simpson(lambda z: math.pi * max(0.0, aa * aa - z * z / (bb * bb)), -bb * aa, bb * aa, 20000), 4 * math.pi * bb * aa ** 3 / 3, 1e-7)
N = 5
line("sum_{n > N} l_n^(1/2) at R = 4.7, N = 5 (= l_{N+1}^(1/2)/(1 - R^(-1/2)))", sum(R ** (-n / 2) for n in range(N + 1, 400)), R ** (-(N + 1) / 2) / (1 - R ** -0.5), 1e-12)
holds("scaling of the input: -1 + 3/2 = 1/2; ||J_eta||_2 exponent -2 + 3/4 = -5/4", -1 + 1.5 == 0.5 and -2 + 0.75 == -1.25)
l = 0.2
line("|D_n| at l = 0.2 (= 6 pi l^3)", math.pi * ((2 * l) ** 2 - l ** 2) * 2 * l, 6 * math.pi * l ** 3)
worst = min((r / l ** 2) * math.exp(-r * r / (4 * l * l) - z * z / (2 * 1.0 * l * l))
            for r in (l + l * i / 50 for i in range(51)) for z in (l * j / 50 for j in range(51)))
holds("on D_n with b = 1 the n-th summand is at least e^-3/2/l (A = 1)", worst >= math.exp(-1.5) / l * (1 - 1e-12))
line("6 pi l^3 (e^-3/2/l)^3 (= 6 pi e^-9/2)", 6 * math.pi * l ** 3 * (math.exp(-1.5) / l) ** 3, 6 * math.pi * math.exp(-4.5))
holds("D_n and J_n are disjoint for R > 2: 2 l_{n+1} < l_n and c_0 A R/(2 l_n) > c_0 A/l_n", 2 / R < 1 and R / 2 > 1)
line("logarithmic length of J_n (= log 2)", math.log((1 / l) / (1 / (2 * l))), math.log(2))
line("(c_0 A/(2 l)) (6 pi l^3)^(1/3) with c_0 A = 1 (= (6 pi)^(1/3)/2)", (1 / (2 * l)) * (6 * math.pi * l ** 3) ** (1 / 3), (6 * math.pi) ** (1 / 3) / 2)
holds("exponents: (3/2)(4/3) = 2; 1 - 3/4 = 1/4; 10/3 and 5/3 from energy interpolation (2 + 4/3, half of it)",
      abs(1.5 * 4 / 3 - 2) < 1e-15 and 1 - 0.75 == 0.25 and abs((2 + 4 / 3) - 10 / 3) < 1e-15)

# pages 102 to 104
th = 1 / 6
line("interpolation L^3 between L^2 and L^(10/3): theta/2 + (1 - theta) 3/10 at theta = 1/6 (= 1/3)", th / 2 + (1 - th) * 3 / 10, 1 / 3, 1e-14)
holds("(9.12): 3/2 times 4/3 = 2 and 1/4 + 3/4 = 1", abs(1.5 * 4 / 3 - 2) < 1e-15)
tp_, Rr = 0.02, 4.7
g = True
for n in range(1, 9):
    ln = Rr ** -n
    for fr in (0.0, 0.3, 1.0):
        t = ln * ln * tp_ * (1 + fr * (Rr * Rr - 1))
        g = g and ln ** 0.5 <= tp_ ** -0.25 * t ** 0.25 * (1 + 1e-12) and 1 / ln <= Rr * math.sqrt(tp_) * t ** -0.5 * (1 + 1e-12)
holds("(9.15): l_n^(1/2) <= t_p^(-1/4) t^(1/4) and l_n^-1 <= R sqrt(t_p) t^(-1/2) on T_n <= t <= R^2 T_n", g)
for q in (2.0, 3.0, 7.0):
    line("(9.16) exponent at q = %.0f: (1/4)(2/q) - (1/2)(1 - 2/q) (= (3/q - 1)/2)" % q, 0.25 * 2 / q - 0.5 * (1 - 2 / q), (3 / q - 1) / 2, 1e-14)


def qnorm_t(l, b, t, q, A=1.0):
    amp = A / l ** 2 * (l * l / (l * l + t)) ** 2 * math.sqrt(b * b * l * l / (b * b * l * l + 2 * t))
    sr = math.sqrt(l * l + t)
    sz = math.sqrt(b * b * l * l + 2 * t)
    ir = simpson(lambda r: r * (r * math.exp(-r * r / (4 * (l * l + t)))) ** q, 0.0, 30 * sr, 6000)
    iz = simpson(lambda z: math.exp(-q * z * z / (2 * sz * sz)), -30 * sz, 30 * sz, 6000)
    return amp * (2 * math.pi * ir * iz) ** (1 / q)


def formula(l, b, t, q):
    return b * l ** 3 * (l * l + t) ** (-1.5 + 1 / q) * (b * b * l * l + 2 * t) ** (-0.5 + 1 / (2 * q))


for q in (2.0, 3.0, 5.0):
    line("||Q_l(t)||_q ratio between (l, b, t) = (0.3, 2, 0.5) and (1, 3, 0.1), q = %.0f (stated formula)" % q,
         qnorm_t(0.3, 2.0, 0.5, q) / qnorm_t(1.0, 3.0, 0.1, q), formula(0.3, 2.0, 0.5, q) / formula(1.0, 3.0, 0.1, q), 1e-7)
# the heat evolution of r e^{-r^2/(4 l^2)} along a line through the origin in the plane (x1 component of x times the Gaussian)
l0, t0, x0 = 0.8, 0.35, 0.9
conv = simpson(lambda y1: (x0 - y1) * math.exp(-(x0 - y1) ** 2 / (4 * l0 * l0)) * math.exp(-y1 * y1 / (4 * t0)) / math.sqrt(4 * math.pi * t0), -12.0, 12.0, 40000)
conv2 = simpson(lambda y2: math.exp(-y2 * y2 / (4 * l0 * l0)) * math.exp(-y2 * y2 / (4 * t0)) / math.sqrt(4 * math.pi * t0), -12.0, 12.0, 40000)
line("heat flow of x_1 e^{-|x|^2/(4 l^2)} at (0.9, 0), l = 0.8, t = 0.35 (= (l^2/(l^2+t))^2 x_1 e^{-x_1^2/(4 (l^2+t))})",
     conv * conv2, (l0 * l0 / (l0 * l0 + t0)) ** 2 * x0 * math.exp(-x0 * x0 / (4 * (l0 * l0 + t0))), 1e-8)
holds("b >= 1 and q >= 1: (b^2 l^2 + 2t)^(-1/2 + 1/(2q)) <= (l^2 + t)^(-1/2 + 1/(2q)); exponents add to -2 + 3/(2q)",
      all(abs((-1.5 + 1 / q) + (-0.5 + 1 / (2 * q)) - (-2 + 3 / (2 * q))) < 1e-14 for q in (1.0, 2.0, 3.0, 9.0)))
for q in (2.0, 3.0, 6.0):
    worst = 0.0
    for k in range(1, 40):
        t = 0.02 * 0.5 ** k
        small = sum((Rr ** -n) ** 3 * (Rr ** (-2 * n) + t) ** (-2 + 3 / (2 * q)) for n in range(0, 200) if Rr ** -n < math.sqrt(t))
        large = sum((Rr ** -n) ** 3 * (Rr ** (-2 * n) + t) ** (-2 + 3 / (2 * q)) for n in range(0, 200) if Rr ** -n >= math.sqrt(t))
        bound = 1.0 if q < 3 else (1 + abs(math.log(t)) if q == 3 else t ** ((3 / q - 1) / 2))
        worst = max(worst, (small + large) / bound)
    holds("q = %.0f: sum_n l_n^3 (l_n^2 + t)^(-2 + 3/(2q)) / stated profile stays bounded for t down to 4e-14 (max %.3f)" % (q, worst), worst < 5.0)
for (p, q) in ((1.9, 1e9), (4.0, 5.9), (2.5, 14.0)):
    holds("(9.18) at p = %.1f, q = %.3g: p (1 - 3/q)/2 < 1 iff 2/p + 3/q > 1" % (p, q), (p * (1 - 3 / q) / 2 < 1) == (2 / p + 3 / q > 1))
Mq, Eq = 1.7, 0.4
lam0 = Mq * Eq ** (-1 / 3)
line("int_0^inf min(|E|, M^3 lam^-3) d lam at M = 1.7, |E| = 0.4 (= (3/2) M |E|^(2/3))", Eq * lam0 + Mq ** 3 / (2 * lam0 ** 2), 1.5 * Mq * Eq ** (2 / 3), 1e-13)
holds("(9.21): 1/3 = (2/3)/2 + (1/3)/inf and (1/4)(2/3) - (1/2)(1/3) = 0", abs(0.25 * 2 / 3 - 0.5 / 3) < 1e-16)

# pages 105 to 107
holds("(9.23): powers of l_n: -1 - 3/2 + 3 = 1/2; ||psi_n||_2: -3/2 + 3/2 = 0", -1 - 1.5 + 3 == 0.5)
EA, am_, l1 = 7.3, 0.2, 0.21
holds("test replacement: 2 sqrt(E_A) times a_- l_1^(1/2)/(4 sqrt(E_A)) = a_- l_1^(1/2)/2",
      abs(2 * math.sqrt(EA) * am_ * math.sqrt(l1) / (4 * math.sqrt(EA)) - am_ * math.sqrt(l1) / 2) < 1e-15)
# -int (w . grad) v . w = int (w . grad) w . v on the torus for a divergence-free trigonometric w (exact on a 12^3 grid)
Ng = 12
pts = [2 * math.pi * i / Ng for i in range(Ng)]


def wf(x, y, z):   # curl of (sin y cos z, sin 2z, cos x sin y) : divergence free
    return (math.cos(x) * math.cos(y) - 2 * math.cos(2 * z), -math.sin(y) * math.sin(z) + math.sin(x) * math.sin(y), -math.cos(y) * math.cos(z))


def dwf(x, y, z):  # rows: components, columns: derivatives
    return ((-math.sin(x) * math.cos(y), -math.cos(x) * math.sin(y), 4 * math.sin(2 * z)),
            (math.cos(x) * math.sin(y), -math.cos(y) * math.sin(z) + math.sin(x) * math.cos(y), -math.sin(y) * math.cos(z)),
            (0.0, math.sin(y) * math.cos(z), math.cos(y) * math.sin(z)))


def vf(x, y, z):
    return (math.sin(x + z), math.cos(2 * y) + math.sin(x), math.cos(x - y) * math.sin(z))


def dvf(x, y, z):
    return ((math.cos(x + z), 0.0, math.cos(x + z)),
            (math.cos(x), -2 * math.sin(2 * y), 0.0),
            (-math.sin(x - y) * math.sin(z), math.sin(x - y) * math.sin(z), math.cos(x - y) * math.cos(z)))


I1 = I2 = dv = 0.0
for x in pts:
    for y in pts:
        for z in pts:
            w, dw, v, dvv = wf(x, y, z), dwf(x, y, z), vf(x, y, z), dvf(x, y, z)
            dv = max(dv, abs(dw[0][0] + dw[1][1] + dw[2][2]))
            I1 -= sum(w[j] * dvv[i][j] * w[i] for i in range(3) for j in range(3))
            I2 += sum(w[j] * dw[i][j] * v[i] for i in range(3) for j in range(3))
holds("the chosen w is divergence free (max |div w| on the grid %.1e)" % dv, dv < 1e-12)
line("-int (w . grad) v . w against int (w . grad) w . v (grid sums, equal)", I1, I2, 1e-10)
holds("Young: a b <= a^2/2 + b^2/2", all(a * b <= a * a / 2 + b * b / 2 + 1e-15 for a in (0.1, 1.0, 3.0) for b in (0.2, 1.0, 5.0)))
holds("chi_seed beta > 6 rho with chi_seed = 1/16 is beta/16 > 6 rho; (A.1) at p = 3 has the factor 3 of (9.8)", 1 / 16 == 0.0625)

# pages 107 to 110 (Appendix A)
holds("heat powers: (3/2)(1/3 - 1/4) = 1/8; (3/2)(1/3) = 1/2; (3/4) 0 + (1/4)(1/2) = 1/8",
      abs(1.5 * (1 / 3 - 1 / 4) - 1 / 8) < 1e-15 and 1.5 / 3 == 0.5 and 0.25 * 0.5 == 1 / 8)
holds("kernel powers: 1/2 + (3/2)(1/2 - 1/4) = 7/8 and 1/2 + (3/2)(1/2 - 1/3) = 3/4; Lorentz product 1/3 + 1/6 = 1/2",
      abs(0.5 + 1.5 * 0.25 - 7 / 8) < 1e-15 and abs(0.5 + 1.5 * (0.5 - 1 / 3) - 0.75) < 1e-15 and abs(1 / 3 + 1 / 6 - 0.5) < 1e-15)
beta = lambda p, q: math.gamma(p) * math.gamma(q) / math.gamma(p + q)
# int_0^1 (1 - s)^(-7/8) s^(-1/4) ds = B(1/8, 3/4), computed with the substitutions that remove both singularities
num = simpson(lambda u: 8 * (1 - u ** 8) ** (-0.25), 0.0, 0.5 ** 0.125, 40000) + simpson(lambda w: (4 / 3) * (1 - w ** (4 / 3)) ** (-7 / 8), 0.0, 0.5 ** 0.75, 40000)
line("int_0^1 (1 - s)^(-7/8) s^(-1/4) ds (= B(1/8, 3/4))", num, beta(1 / 8, 3 / 4), 1e-7)
tt = 0.37
line("int_0^t (t - s)^(-7/8) s^(-1/4) ds at t = 0.37 (= t^(-1/8) B(1/8, 3/4)): exponent 1 - 7/8 - 1/4", 1 - 7 / 8 - 1 / 4, -1 / 8)
line("with 3/4 in place of 7/8 the power of t is 1 - 3/4 - 1/4 (= 0) and the constant is B(1/4, 3/4) = pi sqrt 2", beta(1 / 4, 3 / 4), math.pi * math.sqrt(2), 1e-12)
holds("fixed point on the ball of radius 2 X: X + C (2X)^2 <= 2X and Lipschitz constant 4 C X < 1 once 4 C X <= 1/2",
      all(X + Cc * (2 * X) ** 2 <= 2 * X + 1e-15 for Cc in (0.5, 3.0) for X in (1 / (8 * Cc), 1 / (20 * Cc))))
holds("(A.16): 1/4 + 1/4 = 1/2 leaves half of the dissipation; a b <= a^2/4 + b^2", all(a * b <= a * a / 4 + b * b + 1e-15 for a in (0.3, 2.0) for b in (0.1, 1.0, 4.0)))
print("ALL PASS" if ok else "SOME FAIL")
