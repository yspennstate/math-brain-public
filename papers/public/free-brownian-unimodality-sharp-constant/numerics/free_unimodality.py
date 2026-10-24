"""Numerical companion to
    "The sharp diameter threshold for unimodality of free Brownian motion"

Four independent checks of the theorem  mu boxplus S(0,t) unimodal for all t >= D^2:

  1. symbolic: the two-atom identities, the (D,m) collapse, Lemma A, Lemma B, the Cauchy-profile
     factorisation and the symmetric-Bernoulli expansion, all verified in sympy;
  2. a scan of the two-atom criterion over a fine (D, m, s) grid;
  3. the level-set criterion (Lemma 3.1 of Hasebe-Ueda): for a given measure, the least t from
     which every equation xi_R(u) = 1/t has at most two solutions;
  4. the density itself, built from Biane's parametrisation with no use of the criterion, its modes
     counted, and the unimodality threshold t*(mu) found by bisection.

Run:  python free_unimodality.py            (writes results.md and the figures in ../figures)
Dependencies: numpy, sympy, matplotlib.
"""
import numpy as np, sympy as sp, math, os, sys, time
np.set_printoptions(linewidth=140)
HERE = os.path.dirname(os.path.abspath(__file__))
FIG = os.path.normpath(os.path.join(HERE, "..", "figures"))
os.makedirs(FIG, exist_ok=True)
out = []
def say(s=""):
    print(s); out.append(s)

# ----------------------------------------------------------------------------------------------
# 1. Symbolic checks
# ----------------------------------------------------------------------------------------------
def symbolic_checks():
    say("## 1. Symbolic checks (sympy)")
    a, b, s, m, D, u, c, t, y, A0, B0 = sp.symbols('a b s m D u c t y A0 B0', positive=True)
    A = a**2 + s; B = b**2 + s
    wb = sp.symbols('wb')
    # pair at -a, b; first-derivative condition G = 0 fixes the weights
    sol = sp.solve(sp.Eq((1 - wb) * (-a) / A**2 + wb * b / B**2, 0), wb)[0]
    wa = 1 - sol
    F = wa / A + sol / B
    H = wa * (3 * a**2 - s) / A**3 + sol * (3 * b**2 - s) / B**3
    Delta = b * A**2 + a * B**2
    Phi = b * A * (1 - A) + a * B * (1 - B)
    Psi = b * B * (3 * a**2 - s) + a * A * (3 * b**2 - s)
    ok1 = sp.simplify(F - 1 - Phi / Delta) == 0
    ok2 = sp.simplify(H - Psi / (Delta * A * B)) == 0
    say(f"weights positive and F - 1 = Phi/Delta : {ok1}")
    say(f"H = Psi/(Delta A B)                    : {ok2}")
    PsiD = sp.expand(Psi.subs(b, D - a)); PhiD = sp.expand(Phi.subs(b, D - a))
    tpsi = D * (3 * m**2 + s * (6 * m - D**2) - s**2)
    tphi = D * (3 * m**2 + m * (1 - D**2) + s * (1 - 2 * m) - s**2)
    ok3 = sp.simplify(PsiD - sp.expand(tpsi.subs(m, a * (D - a)))) == 0
    ok4 = sp.simplify(PhiD - sp.expand(tphi.subs(m, a * (D - a)))) == 0
    say(f"Psi/D = 3m^2 + s(6m - D^2) - s^2       : {ok3}")
    say(f"Phi/D = 3m^2 + m(1-D^2) + s(1-2m) - s^2: {ok4}")
    # Lemma A: at m = D^2/4 the value is (3D^2-4s)(D^2+4s)/16
    psiD = 3 * m**2 + s * (6 * m - D**2) - s**2
    ok5 = sp.simplify(psiD.subs(m, D**2 / 4) - (3 * D**2 - 4 * s) * (D**2 + 4 * s) / 16) == 0
    say(f"Lemma A value at m = D^2/4              : {ok5}; d/dm = {sp.factor(sp.diff(psiD, m))} > 0")
    phiD = 3 * m**2 + m * (1 - D**2) + s * (1 - 2 * m) - s**2
    ok6 = sp.simplify(phiD.subs(s, sp.Rational(3, 4)).subs(m, D**2 / 4) - (1 - D**2) * (D**2 + 3) / 16) == 0
    ok7 = sp.simplify(sp.diff(phiD.subs(s, sp.Rational(3, 4)), m).subs(m, D**2 / 4) - (D**2 - 1) / 2) == 0
    say(f"Lemma B value at s = 3/4, m = D^2/4     : {ok6}; slope there (D^2-1)/2: {ok7}; d2/ds2 = {sp.diff(phiD, s, 2)}")
    # Cauchy-profile route: factorisation
    ok8 = sp.expand((y - 3 * a) * (y + a) + (4 * a - D**2) * y - (y**2 + 2 * a * y - 3 * a**2 - D**2 * y)) == 0
    say(f"(y-3a)(y+a) + (4a-D^2)y factorisation    : {ok8}")
    # symmetric Bernoulli at +-c with R^2 = 3c^2: F_R(s) - 1/(4c^2) = -s^4/(4c^2 (s^4 + 4c^2 s^2 + 16 c^4))
    FR = sp.Rational(1, 2) * (1 / ((c - u)**2 + 3 * c**2) + 1 / ((c + u)**2 + 3 * c**2))
    ok9 = sp.simplify(FR - 1 / (4 * c**2) + u**4 / (4 * c**2 * (u**4 + 4 * c**2 * u**2 + 16 * c**4))) == 0
    say(f"Bernoulli profile at R^2 = 3c^2          : {ok9}")
    # sharpness: v_t''(0) for symmetric Bernoulli on {-c, c}, c^2 < t < 4c^2
    v = sp.Function('v')
    eq = sp.Rational(1, 2) * (1 / ((c - u)**2 + v(u)**2) + 1 / ((c + u)**2 + v(u)**2)) - 1 / t
    d2 = sp.diff(eq, u, 2)
    v0 = sp.sqrt(t - c**2)
    expr = d2.subs({sp.Derivative(v(u), (u, 2)): sp.Symbol('vpp'), sp.Derivative(v(u), u): 0}).subs(v(u), v0).subs(u, 0)
    vpp = sp.solve(sp.simplify(expr), sp.Symbol('vpp'))[0]
    ok10 = sp.simplify(vpp - (4 * c**2 - t) / (t * sp.sqrt(t - c**2))) == 0
    say(f"Bernoulli v_t''(0) = (4c^2 - t)/(t sqrt(t-c^2)) : {ok10}")
    # classical companion: H(kappa) = theta (a+b) (1 - t/(ab))
    th = sp.symbols('theta', positive=True)
    Hc = th / a * (a**2 - t) + th / b * (b**2 - t)
    ok11 = sp.simplify(Hc - th * (a + b) * (1 - t / (a * b))) == 0
    say(f"classical pair identity H = theta(a+b)(1 - t/ab): {ok11}")
    return all([ok1, ok2, ok3, ok4, ok5, ok6, ok7, ok8, ok9, ok10, ok11])

# ----------------------------------------------------------------------------------------------
# 2. Scan of the two-atom criterion
# ----------------------------------------------------------------------------------------------
def two_atom_scan(n=400):
    say("\n## 2. Two-atom scan")
    Dv = np.linspace(1e-3, 1.0, n); mmax = Dv**2 / 4
    worst = np.inf; worstA = np.inf; viol = 0; total = 0
    for D in Dv:
        m = np.linspace(1e-3 * D * D / 4, D * D / 4, n)[:, None]   # 0 < m <= D^2/4 for every D
        s = np.linspace(1e-6, 1.5, n)[None, :]
        psi = 3 * m**2 + s * (6 * m - D**2) - s**2
        phi = 3 * m**2 + m * (1 - D**2) + s * (1 - 2 * m) - s**2
        total += psi.size
        # Lemma A: psi >= 0 forces s <= 3 D^2 / 4
        bad = (psi >= 0) & (s > 0.75 * D * D + 1e-12)
        viol += int(bad.sum())
        # Lemma B: on s <= 3/4, phi >= 0
        sel = phi[(np.broadcast_to(s, phi.shape) <= 0.75)]
        worst = min(worst, float(sel.min()))
        # value F-1 = Phi/Delta at a separating minimum: min over the admissible region psi >= 0
        adm = phi[psi >= 0]
        if adm.size: worstA = min(worstA, float(adm.min()))
    say(f"grid points {total}; Lemma A violations {viol}; min Phi/D on s<=3/4: {worst:.6f}; min Phi/D where Psi>=0: {worstA:.6f}")
    return viol == 0 and worst >= -1e-12

# ----------------------------------------------------------------------------------------------
# 3. The level-set criterion for an atomic measure
# ----------------------------------------------------------------------------------------------
def xi(u, R, atoms, w):
    return sum(wi / ((xi_ - u)**2 + R * R) for xi_, wi in zip(atoms, w))

def separating_min_value(atoms, w, ngrid=4001, Rgrid=None):
    """min over R of the lowest interior local minimum of xi_R (returns +inf if none)."""
    D = max(atoms) - min(atoms)
    lo, hi = min(atoms) - 0.5, max(atoms) + 0.5
    u = np.linspace(lo, hi, ngrid)
    if Rgrid is None: Rgrid = np.linspace(0.02, 1.5 * max(D, 0.1), 600)
    best = np.inf; bestR = None
    for R in Rgrid:
        f = xi(u, R, atoms, w)
        loc = (f[1:-1] < f[:-2]) & (f[1:-1] <= f[2:])
        if loc.any():
            v = f[1:-1][loc].min()
            if v < best: best, bestR = v, R
    return best, bestR

def tstar_from_criterion(atoms, w):
    v, R = separating_min_value(atoms, w)
    return (1.0 / v if np.isfinite(v) else 0.0), R

# ----------------------------------------------------------------------------------------------
# 4. Biane's density, mode count, threshold by bisection
# ----------------------------------------------------------------------------------------------
def biane_density(atoms, w, t, ugrid):
    """Return (x, p) with x = psi_t(u), p = density of mu boxplus S(0,t) at x, for u in ugrid.
    v_t(u) is the positive root of  sum w_i/((x_i-u)^2+v^2) = 1/t  (0 if none);
    psi_t(u) = u + t * sum w_i (u-x_i)/((u-x_i)^2 + v^2);  p(psi_t(u)) = v/(pi t)."""
    atoms = np.asarray(atoms); w = np.asarray(w)
    xs = np.empty_like(ugrid); ps = np.empty_like(ugrid)
    for k, u in enumerate(ugrid):
        d2 = (atoms - u)**2
        g = lambda v: np.sum(w / (d2 + v * v)) - 1.0 / t
        if (d2 > 0).all() and g(0.0) <= 0:   # u on an atom: the integral is infinite, a root exists
            v = 0.0
        else:
            hi = math.sqrt(t) + 1.0
            while g(hi) > 0: hi *= 2
            lo = 0.0
            for _ in range(80):
                mid = 0.5 * (lo + hi)
                if g(mid) > 0: lo = mid
                else: hi = mid
            v = 0.5 * (lo + hi)
        xs[k] = u + t * np.sum(w * (u - atoms) / ((u - atoms)**2 + v * v))
        ps[k] = v / (math.pi * t)
    return xs, ps

def n_modes(p, tol=1e-12):
    """number of strict local maxima of the sampled density, plateaus merged."""
    q = p.copy()
    # count maximal runs of increasing then decreasing
    d = np.sign(np.diff(q))
    d = d[d != 0]
    # merge equal signs
    runs = [d[0]] if len(d) else []
    for x in d[1:]:
        if x != runs[-1]: runs.append(x)
    return sum(1 for i in range(len(runs) - 1) if runs[i] > 0 and runs[i + 1] < 0)

def unimodal_at(atoms, w, t, ngrid=6001):
    D = max(atoms) - min(atoms)
    u = np.linspace(min(atoms) - 3 * math.sqrt(t) - 1, max(atoms) + 3 * math.sqrt(t) + 1, ngrid)
    x, p = biane_density(atoms, w, t, u)
    return n_modes(p) <= 1, (x, p)

def tstar_density(atoms, w, lo=1e-3, hi=None, it=40):
    D = max(atoms) - min(atoms)
    if hi is None: hi = 1.5 * D * D + 0.5
    assert unimodal_at(atoms, w, hi)[0]
    if unimodal_at(atoms, w, lo)[0]: return lo
    for _ in range(it):
        mid = 0.5 * (lo + hi)
        if unimodal_at(atoms, w, mid)[0]: hi = mid
        else: lo = mid
    return 0.5 * (lo + hi)

def validate_semicircle():
    # mu = delta_0: the density must be the semicircle of variance t
    t = 1.7
    u = np.linspace(-math.sqrt(t), math.sqrt(t), 2001)
    x, p = biane_density([0.0], [1.0], t, u)
    ref = np.sqrt(np.maximum(4 * t - x**2, 0)) / (2 * math.pi * t)
    err = float(np.max(np.abs(p - ref)))
    say(f"Biane parametrisation control (mu = delta_0 gives the semicircle): max error {err:.2e}")
    return err < 1e-9

def measures():
    rng = np.random.default_rng(20260914)
    M = {
        "two equal atoms at +-1/2": ([-0.5, 0.5], [0.5, 0.5]),
        "atoms at +-1/2, weights 0.3 and 0.7": ([-0.5, 0.5], [0.3, 0.7]),
        "atoms at +-1/2, weights 0.1 and 0.9": ([-0.5, 0.5], [0.1, 0.9]),
        "three atoms -1/2, 0, 1/2 (equal)": ([-0.5, 0.0, 0.5], [1/3, 1/3, 1/3]),
        "three atoms -1/2, 0.1, 1/2 (equal)": ([-0.5, 0.1, 0.5], [1/3, 1/3, 1/3]),
        "two atoms and a spike near 1/2": ([-0.5, 0.45, 0.5], [0.45, 0.1, 0.45]),
        "four atoms, Dirichlet weights": (list(np.array([-0.5, -0.2, 0.15, 0.5])), list(rng.dirichlet([1, 1, 1, 1]))),
        "nine equally spaced atoms": (list(np.linspace(-0.5, 0.5, 9)), [1/9] * 9),
    }
    return M

def main():
    t0 = time.time()
    say("# Numerical companion: results\n")
    ok_sym = symbolic_checks()
    ok_scan = two_atom_scan()
    say("\n## 3-4. Thresholds per measure (all of diameter one; theorem: t* <= 1, equality only for the symmetric pair)")
    ok_semi = validate_semicircle()
    say("\n| measure | t* from the level-set criterion | t* from the density (bisection) | classical t* (Gaussian, bound 1/4) |")
    say("|---|---|---|---|")
    rows = []
    for name, (atoms, w) in measures().items():
        tc, R = tstar_from_criterion(atoms, w)
        td = tstar_density(atoms, w)
        # classical: density of mu * N(0,t) on a grid, bisection
        def uni_cl(t):
            x = np.linspace(-1.5, 1.5, 6001)
            p = sum(wi * np.exp(-(x - ai)**2 / (2 * t)) for ai, wi in zip(atoms, w))
            return n_modes(p) <= 1
        lo, hi = 1e-4, 0.6
        for _ in range(40):
            mid = 0.5 * (lo + hi)
            if uni_cl(mid): hi = mid
            else: lo = mid
        tcl = 0.5 * (lo + hi)
        rows.append((name, tc, td, tcl))
        say(f"| {name} | {tc:.5f} | {td:.5f} | {tcl:.5f} |")
    # Bernoulli on {-1,1}: D = 2, threshold 4 (criterion) and density
    tc, _ = tstar_from_criterion([-1.0, 1.0], [0.5, 0.5]); td = tstar_density([-1.0, 1.0], [0.5, 0.5], hi=6.0)
    say(f"\nsymmetric Bernoulli on {{-1,1}} (D = 2, D^2 = 4): criterion {tc:.5f}, density {td:.5f}")
    # the two figures are drawn by make_figures.py (it imports this module); the pair-threshold sweep is there too
    ws = np.linspace(0.05, 0.5, 19); ts = []
    for wv in ws:
        ts.append(tstar_density([-0.5, 0.5], [wv, 1 - wv]))
    say(f"\npair threshold vs weight: " + ", ".join(f"w={a:.2f}: {b:.4f}" for a, b in zip(ws, ts)))
    say(f"\nall symbolic checks: {ok_sym}; scan: {ok_scan}; semicircle control: {ok_semi}; elapsed {time.time()-t0:.0f} s")
    with open(os.path.join(HERE, "results.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()
