"""Checks for "Corner angles of sandpile aggregates on a background of holes" (Y. Shmalo, 2026).

Part A stabilizes n chips at the origin of Z^2, every site (the origin included) starting with a hole of depth H,
in exact integer arithmetic, and tests the finite statements used in the paper on every run: the stabilization
identity, conservation, the height bounds, the symmetries of the square, the monotonicity of the odometer along the
coordinate directions (Lemma 2.1), the order-ideal shape of the set of fired sites, and the weighted last-firing
inequality (Lemma 2.2) for random and structured weights. It also prints the inner and outer radii of the fired
set. Part B checks the identities of the corner lemma with SymPy. Part C checks the polygon inequalities with
mpmath and tests the corner inequality on explicit corner solutions.

Needs Python 3 with NumPy, Numba, SymPy and mpmath. Usage: python checks.py > checks_output.txt
"""
import math
import sys
import time

import mpmath as mp
import numpy as np
import sympy as sp
from numba import njit

FAILURES = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (("  " + detail) if detail else ""), flush=True)
    if not ok:
        FAILURES.append(name)


# ---------------------------------------------------------------- Part A: exact stabilizations

@njit(cache=False)
def stabilize(n, H, R):
    """Legal stabilization with a FIFO queue; a site with height h fires h // 4 times at once."""
    L = 2 * R + 1
    eta = np.full((L, L), -H, np.int64)
    u = np.zeros((L, L), np.int64)
    eta[R, R] += n
    inq = np.zeros((L, L), np.bool_)
    cap = L * L
    qi = np.empty(cap, np.int64)
    qj = np.empty(cap, np.int64)
    head = 0
    size = 1
    qi[0] = R
    qj[0] = R
    inq[R, R] = True
    di = (1, -1, 0, 0)
    dj = (0, 0, 1, -1)
    while size > 0:
        i = qi[head]
        j = qj[head]
        head = (head + 1) % cap
        size -= 1
        inq[i, j] = False
        k = eta[i, j] // 4
        if k <= 0:
            continue
        if i <= 1 or j <= 1 or i >= L - 2 or j >= L - 2:
            raise ValueError("the array is too small")
        eta[i, j] -= 4 * k
        u[i, j] += k
        for t in range(4):
            a = i + di[t]
            b = j + dj[t]
            eta[a, b] += k
            if eta[a, b] >= 4 and not inq[a, b]:
                tail = (head + size) % cap
                qi[tail] = a
                qj[tail] = b
                inq[a, b] = True
                size += 1
    return eta, u


def laplacian(u):
    out = -4 * u
    out[1:, :] += u[:-1, :]
    out[:-1, :] += u[1:, :]
    out[:, 1:] += u[:, :-1]
    out[:, :-1] += u[:, 1:]
    return out


def edge_min_sum(phi):
    return int(np.minimum(phi[:, 1:], phi[:, :-1]).sum() + np.minimum(phi[1:, :], phi[:-1, :]).sum())


def edge_var_sum(phi):
    return int(np.abs(phi[:, 1:] - phi[:, :-1]).sum() + np.abs(phi[1:, :] - phi[:-1, :]).sum())


def run_case(n, H, rng):
    R = math.isqrt(n) + 10
    t0 = time.perf_counter()
    eta, u = stabilize(n, H, R)
    secs = time.perf_counter() - t0
    tag = "H=%d n=%d" % (H, n)
    L = 2 * R + 1
    eta0 = np.full((L, L), -H, np.int64)
    eta0[R, R] += n
    fired = u > 0
    ok = True
    # stabilization identity, stability, conservation, an untouched border
    ok &= np.array_equal(eta, eta0 + laplacian(u))
    ok &= int(eta.max()) <= 3
    ok &= int((eta + H).sum()) == n
    ok &= not (u[:3].any() or u[-3:].any() or u[:, :3].any() or u[:, -3:].any())
    # heights: fired sites end at >= 0, the others at >= -H
    ok &= int(eta[fired].min()) >= 0 and int(eta[~fired].min()) >= -H
    # symmetries of the square
    ok &= np.array_equal(u, u.T) and np.array_equal(u, u[::-1, :]) and np.array_equal(u, u[:, ::-1])
    # Lemma 2.1: u(x1, x2) <= u(x1 - 1, x2) for x1 >= 1, and the same in the other three directions
    mono = (np.all(u[:, R + 1:] <= u[:, R:-1]) and np.all(u[:, :R] <= u[:, 1:R + 1])
            and np.all(u[R + 1:, :] <= u[R:-1, :]) and np.all(u[:R, :] <= u[1:R + 1, :]))
    ok &= bool(mono)
    # order ideal: every row of the fired set is an interval centred on the axis, of width nonincreasing in |x2|
    widths = []
    for i in range(L):
        cols = np.nonzero(fired[i])[0]
        if cols.size == 0:
            widths.append(-1)
            continue
        w = int(cols.max()) - R
        ok &= cols.size == 2 * w + 1 and int(cols.min()) == R - w
        widths.append(w)
    widths = np.array(widths)
    ok &= bool(np.all(widths[R + 1:] <= widths[R:-1]))
    check("A " + tag + " stabilization, conservation, heights, symmetry, monotonicity, order ideal", ok,
          "(%d fired sites, %.1f s)" % (int(fired.sum()), secs))
    # Lemma 2.2: sum eta*phi >= sum over edges of min(phi_x, phi_y) for phi >= 0 supported on fired sites
    weights = [fired.astype(np.int64), u.copy()]
    for _ in range(20):
        weights.append(np.where(fired, rng.integers(0, 1001, size=fired.shape), 0).astype(np.int64))
    for _ in range(5):
        weights.append(np.where(fired & (rng.random(fired.shape) < 0.3), 1, 0).astype(np.int64))
    inner_layer = fired & ~(np.roll(fired, 1, 0) & np.roll(fired, -1, 0) & np.roll(fired, 1, 1) & np.roll(fired, -1, 1))
    weights.append(inner_layer.astype(np.int64))
    ok2 = True
    slack = []
    for phi in weights:
        lhs = int((eta * phi).sum())
        rhs = edge_min_sum(phi)
        ok2 &= lhs >= rhs
        ok2 &= 2 * rhs == 4 * int(phi.sum()) - edge_var_sum(phi)
        if rhs > 0:
            slack.append((lhs - rhs) / rhs)
    edges_S = edge_min_sum(fired.astype(np.int64))
    check("A " + tag + " weighted last-firing inequality on %d weights" % len(weights), ok2,
          "(sum of heights on the fired set %d >= %d internal edges; least relative slack %.4f)"
          % (int(eta[fired].sum()), edges_S, min(slack)))
    if H == -2:
        w = int(widths[R])
        Y, X = np.ogrid[-R:R + 1, -R:R + 1]
        check("A " + tag + " the fired set is a square (Fey-den Boer and Redig)",
              np.array_equal(fired, (np.abs(X) <= w) & (np.abs(Y) <= w)), "(half side %d)" % w)
    Y, X = np.mgrid[-R:R + 1, -R:R + 1]
    dist = np.sqrt(X.astype(float) ** 2 + Y.astype(float) ** 2)
    rin = float(dist[~fired].min()) / math.sqrt(n)
    rout = float(dist[fired].max()) / math.sqrt(n)
    supp = [float((X * math.cos(a) + Y * math.sin(a))[fired].max()) / math.sqrt(n)
            for a in (0.0, math.pi / 12, math.pi / 6, math.pi / 4)]
    mean_s = float((eta[fired] + H).mean())
    line = ("     radii/sqrt(n): inner %.4f outer %.4f; support at 0,15,30,45 deg: %s; mean of eta+H on the fired set %.4f"
            % (rin, rout, ", ".join("%.4f" % s for s in supp), mean_s))
    if H >= -1:
        line += ("; Levine-Peres constants (H+3)^(-1/2)/sqrt(pi) = %.4f, (H+2)^(-1/2)/sqrt(pi) = %.4f"
                 % ((H + 3) ** -0.5 / math.sqrt(math.pi), (H + 2) ** -0.5 / math.sqrt(math.pi)))
    print(line, flush=True)


def part_a():
    print("Part A: exact stabilizations", flush=True)
    rng = np.random.default_rng(20261013)
    stabilize(64, 0, 20)  # compile
    for H in (-2, -1, 0, 1, 2):
        for n in (1024, 4096, 16384, 65536):
            run_case(n, H, rng)
    for H in (-1, 0):
        run_case(262144, H, rng)


# ---------------------------------------------------------------- Part B: identities of the corner lemma

def part_b():
    print("Part B: identities (SymPy)", flush=True)
    th, al, r, t, b, C, kap = sp.symbols("theta alpha r t b C kappa", real=True)
    I1 = sp.integrate(sp.cos(2 * th), (th, -sp.pi / 4, sp.pi / 4))
    check("B integral of cos(2 theta) over (-pi/4, pi/4) is 1", sp.simplify(I1 - 1) == 0)
    I2 = sp.integrate(sp.cos(2 * th), (th, sp.pi / 4, al / 2))
    check("B integral of cos(2 theta) over (pi/4, alpha/2) is (sin(alpha) - 1)/2",
          sp.simplify(I2 - (sp.sin(al) - 1) / 2) == 0)
    I3 = sp.integrate(sp.cos(2 * th), (th, -al / 2, al / 2))
    check("B integral of cos(2 theta) over (-alpha/2, alpha/2) is sin(alpha)", sp.simplify(I3 - sp.sin(al)) == 0)
    f = sp.Function("f")
    F = r ** 2 * f(r)
    op = sp.diff(F, r, 2) + sp.diff(F, r) / r - 4 * F / r ** 2
    check("B F = r^2 f gives F'' + F'/r - 4F/r^2 = r^2 f'' + 5 r f'",
          sp.simplify(op - (r ** 2 * sp.diff(f(r), r, 2) + 5 * r * sp.diff(f(r), r))) == 0)
    check("B (r^5 f')' = r^3 (F'' + F'/r - 4F/r^2)",
          sp.simplify(sp.diff(r ** 5 * sp.diff(f(r), r), r) - r ** 3 * op) == 0)
    x, y = sp.symbols("x y", real=True)
    s = sp.Symbol("s", positive=True)
    rr = sp.sqrt(x ** 2 + y ** 2)
    ok = True
    for test in (s ** 3, s ** 4 * (1 - s) ** 2, sp.exp(-s) * s ** 5):
        phi_t = test.subs(s, rr) * (x ** 2 - y ** 2) / rr ** 2
        lap_t = sp.diff(phi_t, x, 2) + sp.diff(phi_t, y, 2)
        pred = ((sp.diff(test, s, 2) + sp.diff(test, s) / s - 4 * test / s ** 2).subs(s, rr)
                * (x ** 2 - y ** 2) / rr ** 2)
        ok &= sp.simplify(lap_t - pred) == 0
    check("B Laplacian of psi(r) cos(2 theta) is (psi'' + psi'/r - 4 psi/r^2) cos(2 theta) (three test functions psi)",
          ok)
    M1 = sp.integrate(b * t / 2, (t, 0, r))
    check("B integral over (0, r) of b t/2 is b r^2/4", sp.simplify(M1 - b * r ** 2 / 4) == 0)
    fp = (C + sp.integrate(t ** 3 * kap, (t, 0, r))) / r ** 5
    check("B r^5 f' = C + kappa r^4/4 gives f' = C/r^5 + kappa/(4r)", sp.simplify(fp - (C / r ** 5 + kap / (4 * r))) == 0)
    rp, r0 = sp.symbols("rp r0", positive=True)
    check("B integral of kappa/(4t) over (r, r0) is (kappa/4) log(r0/r)",
          sp.simplify(sp.integrate(kap / (4 * t), (t, rp, r0)) - kap / 4 * sp.log(r0 / rp)) == 0
          or sp.simplify(sp.expand_log(sp.integrate(kap / (4 * t), (t, rp, r0)) - kap / 4 * sp.log(r0 / rp), force=True)) == 0)
    a_, b_ = sp.symbols("a b", positive=True)
    lower = a_ * I1 + b_ * 2 * I2
    check("B the lower bound a*1 + 2b*(sin(alpha) - 1)/2 equals a - b(1 - sin(alpha))",
          sp.simplify(lower - (a_ - b_ * (1 - sp.sin(al)))) == 0)
    # explicit corner solutions u = r^2 c(theta), c = cos(pi theta/alpha)^2 on |theta| < alpha/2, zero outside
    c = sp.cos(sp.pi * th / al) ** 2
    gg = 4 * c + sp.diff(c, th, 2)
    check("B for u = r^2 cos(pi theta/alpha)^2, Delta u = 2 + (2 - 2 pi^2/alpha^2) cos(2 pi theta/alpha)",
          sp.simplify(gg - (2 + (2 - 2 * sp.pi ** 2 / al ** 2) * sp.cos(2 * sp.pi * th / al))) == 0)
    check("B that u is C^1 across the edges: c and c' vanish at theta = alpha/2",
          sp.simplify(c.subs(th, al / 2)) == 0 and sp.simplify(sp.diff(c, th).subs(th, al / 2)) == 0)
    mp.mp.dps = 30
    gfun = sp.lambdify((th, al), gg * sp.cos(2 * th), "mpmath")
    vals = []
    for v in (mp.pi * 3 / 5, mp.pi * 3 / 4, mp.pi * 5 / 6, mp.pi * 17 / 18):
        vals.append(mp.quad(lambda z: gfun(z, v), [-v / 2, 0, v / 2]))
    check("B its Fourier projection G = integral of Delta u * cos(2 theta) vanishes (alpha = 108, 135, 150, 170 deg)",
          all(abs(v) < 1e-25 for v in vals), "(max %.1e)" % max(abs(float(v)) for v in vals))


# ---------------------------------------------------------------- Part C: polygon inequalities

def part_c():
    print("Part C: polygon inequalities (mpmath, 50 digits)", flush=True)
    mp.mp.dps = 50
    margins = [k * mp.sin(mp.pi / (2 * k)) - 1 for k in range(2, 1001)]
    check("C k sin(pi/(2k)) - 1 > 0 for k = 2..1000 (a regular 4k-gon violates a <= b(1 - sin alpha) with a = k-1, b = k)",
          min(margins) > 0, "(least margin %s at k = 2)" % mp.nstr(min(margins), 8))
    ok = True
    rows = []
    for H in range(-1, 21):
        k = H + 3
        bound = 2 * mp.pi / mp.asin(mp.mpf(1) / k)
        m = 4 * int(mp.ceil(bound / 4 - mp.mpf(10) ** -40))
        ok &= bound > 4 * k and m >= 4 * H + 16
        rows.append((H, bound, m, mp.degrees(mp.pi - mp.asin(mp.mpf(1) / k))))
    check("C for H = -1..20, 2 pi/arcsin(1/(H+3)) > 4H + 12 and the least admissible multiple of 4 is >= 4H + 16", ok)
    for H, bound, m, deg in rows[:6]:
        print("     H = %2d: angles >= %s deg, 2 pi/arcsin(1/(H+3)) = %s, at least %d vertices (4H+12 = %d)"
              % (H, mp.nstr(deg, 8), mp.nstr(bound, 8), m, 4 * H + 12), flush=True)
    check("C H = -1: 2 pi/arcsin(1/2) = 12 exactly", abs(2 * mp.pi / mp.asin(mp.mpf(1) / 2) - 12) < mp.mpf(10) ** -45)
    check("C H = 0: sin(pi/9) > 1/3, so arcsin(1/3) < pi/9 and 2 pi/arcsin(1/3) > 18", mp.sin(mp.pi / 9) > mp.mpf(1) / 3,
          "(sin(pi/9) = %s)" % mp.nstr(mp.sin(mp.pi / 9), 10))
    # the corner inequality on the explicit corner solutions of Part B (Delta u ranges over [a, b] with a > 0
    # exactly when alpha > pi/sqrt(2)); the inequality a <= b(1 - sin alpha) must hold for them
    ok = True
    worst = None
    for i in range(1, 400):
        alpha = mp.pi / mp.sqrt(2) + (mp.pi - mp.pi / mp.sqrt(2)) * mp.mpf(i) / 400
        t = 2 * mp.pi ** 2 / alpha ** 2
        a = 4 - t
        b = t
        gap = b * (1 - mp.sin(alpha)) - a
        ok &= gap > 0
        worst = gap if worst is None else min(worst, gap)
    check("C the explicit corner solutions satisfy a <= b(1 - sin alpha) for 399 angles in (pi/sqrt(2), pi)", ok,
          "(least gap %s, tending to 0 as alpha -> pi)" % mp.nstr(worst, 6))


if __name__ == "__main__":
    t0 = time.perf_counter()
    print("python %s, numpy %s, sympy %s, mpmath %s" % (sys.version.split()[0], np.__version__, sp.__version__, mp.__version__))
    part_a()
    part_b()
    part_c()
    print("%d failures; total %.0f s" % (len(FAILURES), time.perf_counter() - t0))
    sys.exit(1 if FAILURES else 0)
