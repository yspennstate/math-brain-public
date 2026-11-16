# Checks for the sharp quadratic Michael-Simon inequality behind the 2026 proofs of the generalized
# Cartan-Hadamard conjecture (arXiv 2610.37817, Theorem 1.4 and Section 2; OpenAI preprint of 23 Sep 2026).
#
#   Q(v) = int_S (q-2)|grad v|^2 + (n-1)(H^2 + kbar) v^2  >=  c_n ||v||_q^2,
#   q = 2(n-1)/(n-3),  c_n = (n-1) omega_{n-1}^{2/(n-1)},  H the normalized mean curvature, n >= 4.
#
# Part 1  the model identities (A.2)-(A.4) for f = lambda / (s'(r/2)^2 + lambda^2 s(r/2)^2), in curvature
#         kbar = -kappa^2 and kbar = 0, and the conformal factor of the map to the sphere.
# Part 2  the pointwise algebra that turns Lemma 2.2(ii) into the lower bound (2.8).
# Part 3  equality on geodesic spheres of the model spaces.
# Part 4  numerical test in Euclidean space: hypersurfaces of revolution in R^n, n = 4, 5, 6, with v = 1
#         and with non-constant v.
import math
import numpy as np
import sympy as sp


def out(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------- Part 1
r, lam, kap = sp.symbols("r lambda kappa", positive=True)
out("PART 1  model identities")
for name, s, kbar in (("kbar = -kappa^2", sp.sinh(kap * r) / kap, -kap ** 2), ("kbar = 0", r, sp.Integer(0))):
    sp_ = sp.diff(s, r)
    sh = s.subs(r, r / 2)
    sph = sp_.subs(r, r / 2)
    f = lam / (sph ** 2 + lam ** 2 * sh ** 2)
    u = sp.log(f)
    u1 = sp.diff(u, r)
    u2 = sp.diff(u, r, 2)
    e1 = u1 + (lam ** 2 - kbar) * s / (2 * (1 + (lam ** 2 - kbar) * sh ** 2))            # (A.2)
    e2 = -u1 * sp_ / s - sp.Rational(1, 2) * (-kbar + f ** 2 + u1 ** 2)                  # (A.3)
    e3 = u2 - u1 ** 2 - u1 * sp_ / s                                                      # (A.4)
    z = lam * sh / sph
    e4 = 2 * sp.diff(z, r) / (1 + z ** 2) - f                                             # radial conformal factor
    e5 = 2 * z / (1 + z ** 2) - f * s                                                     # angular conformal factor
    worst = 0.0
    rng = np.random.default_rng(1)
    for _ in range(40):
        vals = {r: float(rng.uniform(0.05, 6)), lam: float(rng.uniform(0.05, 5)), kap: float(rng.uniform(0.1, 2))}
        for e in (e1, e2, e3, e4, e5):
            worst = max(worst, abs(complex(sp.N(e.subs(vals), 30))))
    out("  %-16s largest residual of (A.2), (A.3), (A.4) and the two conformal-factor identities at 40 random points: %.2e" % (name, worst))

# ---------------------------------------------------------------- Part 2
out("PART 2  algebra of (2.8)")
n = sp.symbols("n", positive=True)
v, vx, ux, un, Hs, fs, kb = sp.symbols("v v_x u_x u_nu H f kbar", real=True)
q = 2 * (n - 1) / (n - 3)
a = (n - 3) / 2
# integrand of Q, with 4 v v_x u_x replaced through integration by parts by -2 v^2 Lap_S u and the lemma:
# -2 Lap_S u >= (n-3) u_x^2 + (n-1)(-kbar + f^2) + (n-1) u_nu^2 + 2 (n-1) H u_nu      (one tangential direction)
lhs = (q - 2) * vx ** 2 + (n - 1) * (Hs ** 2 + kb) * v ** 2
mid = (q - 2) * (vx - a * v * ux) ** 2 + 4 * v * vx * ux - (n - 3) * v ** 2 * ux ** 2 + (n - 1) * (Hs ** 2 + kb) * v ** 2
out("  completing the square is an identity:", sp.simplify(lhs - mid) == 0)
low = (q - 2) * (vx - a * v * ux) ** 2 + v ** 2 * ((n - 3) * ux ** 2 + (n - 1) * (-kb + fs ** 2) + (n - 1) * un ** 2 + 2 * (n - 1) * Hs * un) \
    - (n - 3) * v ** 2 * ux ** 2 + (n - 1) * (Hs ** 2 + kb) * v ** 2
tgt = (n - 1) * v ** 2 * (fs ** 2 + (Hs + un) ** 2) + (q - 2) * (vx - a * v * ux) ** 2
out("  after inserting the lemma the bound is exactly (2.8):", sp.simplify(low - tgt) == 0)

# ---------------------------------------------------------------- Part 3
out("PART 3  equality on geodesic spheres")


def omega(m):  # area of the unit sphere S^m
    return 2 * math.pi ** ((m + 1) / 2) / math.gamma((m + 1) / 2)


worst = 0.0
for nn in (4, 5, 6, 7, 9):
    for kk in (0.0, 0.5, 2.0):
        for R in (0.3, 1.0, 2.5):
            s = R if kk == 0 else math.sinh(kk * R) / kk
            s1 = 1.0 if kk == 0 else math.cosh(kk * R)
            P = omega(nn - 1) * s ** (nn - 1)
            Q1 = (nn - 1) * ((s1 / s) ** 2 - kk ** 2) * P
            rhs = (nn - 1) * omega(nn - 1) ** (2 / (nn - 1)) * P ** ((nn - 3) / (nn - 1))
            worst = max(worst, abs(Q1 / rhs - 1))
out("  largest |Q(1)/(c_n P^((n-3)/(n-1))) - 1| over 45 spheres: %.2e" % worst)

# ---------------------------------------------------------------- Part 4
out("PART 4  hypersurfaces of revolution in R^n: profile (rho(t), h(t)), 0 <= t <= pi")
out("        ratio = Q(v) / (c_n ||v||_q^2), claimed >= 1 with equality for the round sphere and v = 1")


def profile(kind, par, N=20001):
    t = np.linspace(0.0, math.pi, N)
    if kind == "spheroid":            # rho = sin t, h = par * cos t
        rho, h = np.sin(t), par * np.cos(t)
    elif kind == "peanut":            # non-convex for par > 1/3 or so
        g = 1 + par * np.cos(2 * t)
        rho, h = g * np.sin(t), g * np.cos(t)
    elif kind == "lens":              # flattened, with a bulge
        g = 1 - par * np.cos(2 * t)
        rho, h = g * np.sin(t), g * np.cos(t)
    return t, rho, h


def geometry(t, rho, h, m):
    dt = t[1] - t[0]
    r1, h1 = np.gradient(rho, dt, edge_order=2), np.gradient(h, dt, edge_order=2)
    r2, h2 = np.gradient(r1, dt, edge_order=2), np.gradient(h1, dt, edge_order=2)
    sp_ = np.sqrt(r1 ** 2 + h1 ** 2)
    k1 = (h1 * r2 - r1 * h2) / sp_ ** 3          # curvature of the profile (outward normal convention)
    with np.errstate(divide="ignore", invalid="ignore"):
        k2 = -h1 / (rho * sp_)                   # the m-1 rotational curvatures
    k2[0], k2[-1] = k1[0], k1[-1]                # umbilic poles
    H = (k1 + (m - 1) * k2) / m
    w = omega(m - 1) * rho ** (m - 1) * sp_      # area density in t
    return H, w, sp_, dt


def integ(y, dt):
    return float(np.sum((y[1:] + y[:-1]) / 2) * dt)


def ratio(kind, par, nn, vfun=None):
    m = nn - 1
    t, rho, h = profile(kind, par)
    H, w, sp_, dt = geometry(t, rho, h, m)
    qq = 2 * (nn - 1) / (nn - 3)
    v = np.ones_like(t) if vfun is None else vfun(t, rho, h)
    dv = np.gradient(v, dt, edge_order=2) / sp_
    Q = integ(((qq - 2) * dv ** 2 + (nn - 1) * H ** 2 * v ** 2) * w, dt)
    nrm = integ(np.abs(v) ** qq * w, dt) ** (2 / qq)
    cn = (nn - 1) * omega(nn - 1) ** (2 / (nn - 1))
    return Q / (cn * nrm)


tests = [("spheroid", 1.0), ("spheroid", 0.5), ("spheroid", 0.2), ("spheroid", 2.0), ("spheroid", 5.0),
         ("peanut", 0.2), ("peanut", 0.45), ("peanut", 0.7), ("lens", 0.3), ("lens", 0.6)]
vfuns = [("v = 1", None),
         ("v = 1 + 0.5 h/max|h|", lambda t, rho, h: 1 + 0.5 * h / np.max(np.abs(h))),
         ("v = exp(-2 t^2)", lambda t, rho, h: np.exp(-2 * t ** 2)),
         ("v = sin^2 t", lambda t, rho, h: np.sin(t) ** 2),
         ("v = (1+3cos^2(t/2))^(-(n-3)/2)", None)]
lowest = 1e9
for nn in (4, 5, 6):
    for kind, par in tests:
        row = []
        for name, vf in vfuns:
            if name.startswith("v = (1+3"):
                vf = (lambda e: (lambda t, rho, h: (1 + 3 * np.cos(t / 2) ** 2) ** (-e)))((nn - 3) / 2)
            x = ratio(kind, par, nn, vf)
            row.append(x)
            lowest = min(lowest, x)
        out("  n=%d %-9s %.2f   " % (nn, kind, par) + "  ".join("%8.4f" % x for x in row))
out("  columns: " + "; ".join(nm for nm, _ in vfuns))
out("  lowest ratio over %d cases: %.6f" % (3 * len(tests) * len(vfuns), lowest))
# conformal images of the constant: on the round sphere, v = f^((n-3)/2) with f the factor of a Moebius map are
# the extremals; the last column is of that type for the round sphere and should give ratio 1 there.
