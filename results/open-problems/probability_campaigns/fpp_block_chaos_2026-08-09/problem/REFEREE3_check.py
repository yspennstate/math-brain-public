# -*- coding: utf-8 -*-
"""Referee 3 arithmetic checks for localization_tail_draft_iter106.md.

Each block is a DISCONFIRMATION attempt: it searches parameter space for a counterexample to
a claim the draft makes, and prints the worst case found. Nothing here is a proof; it is a
bug-catcher for the constants, plus two exact-norm checks of a geometric claim I use to REPAIR
the draft (the dogleg-excess monotonicity in the longitudinal coordinate).
"""
import itertools
import json
import math
import os

import numpy as np

OUT = {}
HERE = os.path.dirname(os.path.abspath(__file__))


def sec(name):
    print("\n" + "=" * 78)
    print(name)
    print("=" * 78)


# ---------------------------------------------------------------------------
sec("1. G-b band cap: a(r+2D) > br  <=>  D > r(b-a)/(2a)   [exact algebra, spot-checked]")
worst = None
for a in (0.2, 0.5, 1.0, 1.7):
    for b in (a * 1.01, a * 1.5, a * 2.0, a * 5.0):
        for r in (16, 64, 1024):
            cap = r * (b - a) / (2 * a)
            # the cap is exactly the D where the excursion cost equals the direct-path cost
            lhs = a * (r + 2 * cap)
            rhs = b * r
            err = abs(lhs - rhs) / rhs
            if worst is None or err > worst[0]:
                worst = (err, a, b, r)
print("max relative mismatch at the cap over the grid:", worst)
OUT["G-b_cap_identity_max_rel_err"] = worst[0]

# ---------------------------------------------------------------------------
sec("2. G-a / G-c site count N: draft says N <= 6 rho r; sharper count from the SAME facts")
# geodesic edge count N_e <= (b/a) r = rho r  (T <= br, each edge >= a)
# a vertex at longitudinal j needs r + 2*max(0,-j,j-r) vertical + 2*Dbar horizontal steps
rows = []
for rho in (1.5, 2.0, 4.0, 10.0):
    for r in (100, 10_000):
        for Dbar in (1, int(0.1 * r)):
            jmin = -(rho * r - r - 2 * Dbar) / 2.0
            jmax = r + (rho * r - r - 2 * Dbar) / 2.0
            n_per_level = math.floor(jmax) - math.ceil(jmin) + 1
            draft_per_level = 2 * rho * r + 1          # |j| <= rho r
            rows.append((rho, r, Dbar, n_per_level, draft_per_level,
                         2 * n_per_level <= 4 * rho * r, 2 * draft_per_level <= 6 * rho * r))
for row in rows:
    print("rho=%5.1f r=%6d Dbar=%5d  sharp/level=%8d  draft/level=%8d  sharp<=4rho r:%s  draft<=6rho r:%s"
          % row)
OUT["site_count_sharp_ok"] = all(row[5] for row in rows)
OUT["site_count_draft_ok"] = all(row[6] for row in rows)
print("=> draft's N <= 6 rho r is VALID; sharp N <= 2(rho r + 1) <= 4 rho r, so the Form A")
print("   prefactor improves 18 C1 rho r -> 12 C1 rho r (one-sided G-e: 6 C1 rho r).")

# ---------------------------------------------------------------------------
sec("3. G-c full chain: brute-force search for a parameter point where a printed step FAILS")
# Free parameters. C1,c1 = (P-conc); C2 = its range constant; C3 = Alexander; c_ = c_-.
fails = []
grid = itertools.product(
    (0.5, 1.0, 3.0),        # C1
    (0.02, 0.2, 1.0),       # c1
    (0.1, 1.0, 5.0),        # C2
    (0.5, 2.0, 10.0),       # C3
    (0.05, 0.5, 3.0),       # c_-
    (1.5, 2.0, 6.0),        # rho = b/a
    (1e3, 1e6, 1e10),       # r
)
for C1, c1, C2, C3, c_, rho, r in grid:
    delta = min(1.0, 3 * C2 / c_)
    CL = 2.0 + rho
    cpp = c1 / (6.0 * math.sqrt(CL))
    s2_lo = max((2 * C3 / c_) * math.log(r), (2.0 / (cpp * c_)) * math.log(18 * C1 * rho * r))
    s2_hi = delta ** 2 * math.sqrt(r)
    if s2_lo > s2_hi:
        fails.append(("EMPTY RANGE", C1, c1, C2, C3, c_, rho, r, s2_lo, s2_hi))
        continue
    for s2 in (s2_lo, math.sqrt(s2_lo * s2_hi), s2_hi):
        sigma = math.sqrt(s2)
        D = sigma * r ** 0.75
        Dbar = math.ceil(D)
        Delta = c_ * Dbar ** 2 / r - C3 * math.sqrt(r) * math.log(r)
        # (i) claimed floor Delta >= (1/2) c_ s2 sqrt(r)
        if Delta < 0.5 * c_ * s2 * math.sqrt(r) - 1e-9 * abs(Delta):
            fails.append(("DELTA FLOOR", C1, c1, C2, C3, c_, rho, r, s2))
        # (ii) claimed exponent
        expo = c1 * Delta / (3 * math.sqrt(CL * r))
        if expo < cpp * c_ * s2 - 1e-9 * expo:
            fails.append(("EXPONENT", C1, c1, C2, C3, c_, rho, r, s2))
        # (iii) range check on span (length r) and short leg (length Dbar)
        if Delta > 3 * C2 * r:
            fails.append(("RANGE-SPAN", C1, c1, C2, C3, c_, rho, r, s2, Delta, 3 * C2 * r))
        if Delta > 3 * C2 * Dbar:
            fails.append(("RANGE-SHORTLEG", C1, c1, C2, C3, c_, rho, r, s2, Delta, 3 * C2 * Dbar))
        # (iv) curvature window: the hypothesis is assumed for displacement <= delta r,
        #      but the site used is at level Dbar = ceil(D)
        if Dbar > delta * r:
            fails.append(("WINDOW-CEIL", C1, c1, C2, C3, c_, rho, r, s2, Dbar, delta * r))
print("failures found:", len(fails))
kinds = {}
for f in fails:
    kinds[f[0]] = kinds.get(f[0], 0) + 1
print("by kind:", kinds)
for f in fails[:6]:
    print("  ", f)
OUT["G-c_chain_failures"] = kinds

# ---------------------------------------------------------------------------
sec("4. The MIDDLE BAND: is Form A proved on the WHOLE stated range sigma^2 <= C''' sqrt r ?")
# derivation is valid for s2 >= S_low = (2C3/c_-) log r
# statement is vacuous (RHS >= 1) for s2 <= L/(c'' c_-), L = log(18 C1 rho r)
# uncovered band exists iff L/(c'' c_-) < S_low  <=>  log(18 C1 rho r) < 2 C3 c'' log r
holes = []
for C1, c1, C3, rho, r in itertools.product((0.5, 1.0, 3.0), (0.02, 0.2, 1.0, 3.0),
                                            (0.5, 2.0, 10.0), (1.5, 2.0, 6.0),
                                            (1e3, 1e6, 1e10)):
    cpp = c1 / (6.0 * math.sqrt(2 + rho))
    L = math.log(18 * C1 * rho * r)
    lhs = L / cpp            # = (c_-)*(upper end of the vacuous region)*... c_- cancels
    rhs = 2 * C3 * math.log(r)
    if lhs < rhs:
        holes.append((C1, c1, C3, rho, r, 2 * C3 * cpp))
print("parameter points with an UNPROVED middle band:", len(holes), "of",
      3 * 4 * 3 * 3 * 3)
for h in holes[:6]:
    print("   C1=%s c1=%s C3=%s rho=%s r=%.0e  2*C3*c''=%.3f" % h)
print("condition for NO hole:  2 C3 c'' <= 1 + log(18 C1 rho)/log r,  i.e. essentially c'' <= 1/(2C3).")
print("REPAIR: (P-conc) holds with any c1' <= c1, so WLOG c1 <= 3 sqrt(2+rho)/C3, i.e. c'' <= 1/(2C3).")
OUT["middle_band_holes"] = len(holes)

# ---------------------------------------------------------------------------
sec("5. Ceiling slack: the window is stated as D <= delta r but the SITE is at ceil(D)")
bad = [(delta, r) for delta in (0.01, 0.1, 1.0) for r in (10, 100, 1e4)
       if math.ceil(delta * r) > delta * r]
print("points where ceil(D) exceeds the stated window at D = delta r:", bad[:6], "...")
print("REPAIR: state C''' = delta^2/4 (then Dbar <= (delta/2) r + 1 <= delta r for r >= 2/delta),")
print("        or read the window as ceil(D) <= delta r. Constant-level, but it is the exact")
print("        place the MID-BAND clause and the short-leg range check are evaluated.")

# ---------------------------------------------------------------------------
sec("6. G-f (i): the endpoint-pair count")
# draft: each boundary carries <= C n sites 'by (G-b)'s band cap at slab scale n'
# but the crossing points sit on the SCALE-R geodesic, R = M n: the band cap gives C M n.
for rho, M, n in ((2.0, 5, 1e4), (2.0, 8, 1e6), (6.0, 5, 1e8)):
    a_, b_ = 1.0, rho
    capR = (b_ - a_) / (2 * a_) * M * n
    capn = (b_ - a_) / (2 * a_) * n
    print("rho=%.1f M=%d n=%.0e : band cap at TOP scale = %.3e sites/boundary; at slab scale = %.3e"
          % (rho, M, n, capR, capn))
print("=> the printed justification gives C M n, not C n. Draft's C' M n^3 would become")
print("   M * (CMn)^2 * 18C1 rho * (C M n) = C'' M^4 n^3   if that were the only route.")
print("   Correct route (available only AFTER (ii), which was written one iteration later):")
print("   intersect with the complement of {global dev >= theta n/2}; then |h| <= theta n/2 on")
print("   every boundary, sites/boundary <= theta n + 1, pairs <= M (theta n)^2, prefactor ~ n:")
print("   total ~ C M theta^2 n^3  -> the draft's C' M n^3 SURVIVES, with a different reason.")

# ---------------------------------------------------------------------------
sec("7. G-f (ii): range identity, quantile, and the honest threshold")
# identity: sigma^2 <= delta^2 sqrt(R)  <=>  D <= delta R  for D = sigma R^{3/4}
for R in (1e5, 1e9, 1e13):
    for delta in (0.05, 0.5, 1.0):
        s2 = delta ** 2 * math.sqrt(R)
        D = math.sqrt(s2) * R ** 0.75
        print("R=%.0e delta=%.2f : sigma^2 = delta^2 sqrt R -> D = %.6e vs delta R = %.6e (ratio %.12f)"
              % (R, delta, D, delta * R, D / (delta * R)))
print()
print("quantile at D = theta n/2, R = M n:  sigma^2 = (theta^2/4) sqrt(n) M^{-3/2}")
grid_rows = []
for M in (5, 8):
    for n in (1e4, 1e6, 1e8):
        for theta in (0.05, 0.2, 0.5):
            R = M * n
            D = theta * n / 2
            s2 = D ** 2 / R ** 1.5
            s2_formula = (theta ** 2 / 4) * math.sqrt(n) * M ** -1.5
            assert abs(s2 - s2_formula) < 1e-9 * s2_formula
            for delta in (1.0, 0.1, 0.01):
                in_range = s2 <= delta ** 2 * math.sqrt(R)
                needed = (theta / 2 <= delta * M)
                assert in_range == needed or abs(s2 - delta ** 2 * math.sqrt(R)) < 1e-9
                grid_rows.append((M, n, theta, delta, s2, in_range))
print("delta = 1.0 : in range at every gridded (M,n,theta)? ",
      all(r_[5] for r_ in grid_rows if r_[3] == 1.0))
print("delta = 0.1 : ", all(r_[5] for r_ in grid_rows if r_[3] == 0.1),
      " delta = 0.01 : ", all(r_[5] for r_ in grid_rows if r_[3] == 0.01))
bad_rows = [r_ for r_ in grid_rows if not r_[5]]
for r_ in bad_rows[:6]:
    print("   OUT OF RANGE: M=%d n=%.0e theta=%.2f delta=%.2f  (needs theta/2 <= delta M = %.3f)"
          % (r_[0], r_[1], r_[2], r_[3], r_[3] * r_[0]))
OUT["Gf_ii_out_of_range_rows"] = len(bad_rows)

print()
print("threshold: draft says the exponent is LARGE once n >~ M^3/theta^4.")
print("exponent (with c'' c_- = 1) and the honest requirement exponent >= log(C M n):")
for M in (5, 8):
    for n in (1e4, 1e6, 1e8, 1e12, 1e16):
        for theta in (0.05, 0.2, 0.5):
            expo = (theta ** 2 / 4) * math.sqrt(n) * M ** -1.5
            need = math.log(M * n)
            print("  M=%d n=%.0e theta=%.2f : exponent=%.4g  log(Mn)=%.3g  union o(1)? %s"
                  % (M, n, theta, expo, need, expo > need))
print("=> honest threshold carries a log^2: n >~ (16/(c'' c_-)^2) (M^3/theta^4) log^2(C M n),")
print("   and the SAME largeness is forced independently by the lemma's own lower threshold")
print("   sigma^2 >= (2 C3/c_-) log R. The draft's n >~ M^3/theta^4 omits both logs and c''c_-.")

# ---------------------------------------------------------------------------
sec("8. SEAM: v2's upper-range claim 'sigma^2 = Theta(log l) <= delta^2 sqrt(r') for l large'")
# consumer: sigma^2 = 2A log l/(c'' c_-), r' >= l^cb/K, cb = base exponent <= 0.12
def l_needed(A, cpp, c_, delta, K, cb):
    """smallest 10^x with 2A ln l/(c'' c_-) <= delta^2 (l^cb/K)^{1/2}"""
    x = 1.0
    while x < 100000:
        l = 10 ** x
        lhs = 2 * A * math.log(l) / (cpp * c_)
        rhs = delta ** 2 * (l ** cb / K) ** 0.5
        if lhs <= rhs:
            return x
        x += 1.0
    return float("inf")
print("log10(l) needed for the seam's upper-range line, as constants vary (A=2, K=10, cb=0.12):")
for cppc in (1.0, 0.1, 0.01):
    for delta in (1.0, 0.1, 0.01):
        x = l_needed(2.0, cppc, 1.0, delta, 10.0, 0.12)
        flag = "" if x <= 80 else "   <-- EXCEEDS the document's own l_0 ~ 1e80"
        print("   c''*c_-=%5.2f delta=%5.2f  ->  l >= 1e%.0f%s" % (cppc, delta, x, flag))
OUT["seam_l_threshold_examples"] = {
    "c''c_-=0.01,delta=0.1": l_needed(2.0, 0.01, 1.0, 0.1, 10.0, 0.12),
    "c''c_-=1,delta=1": l_needed(2.0, 1.0, 1.0, 1.0, 10.0, 0.12),
}

# ---------------------------------------------------------------------------
sec("9. The dogleg-excess claim I use to REPAIR the arc/longitudinal-range hole")
# CLAIM: for x = r e_2 (axis-aligned) and any norm g with g(-h, y) = g(h, y),
#        F(h, j) := g(h, j) + g(-h, r - j) is convex in j and symmetric about j = r/2,
#        hence F(h, j) >= F(h, r/2) for EVERY j - including j < 0 and j > r.
# Consequence: assuming (H-curv-LOWER) only at the MIDPOINT displacement (the enclosing-ball
# statement Newman-Piza print) already gives the excess for every longitudinal position, so
# G-b(ii)'s reading of the hypothesis costs nothing.
def make_norms():
    norms = {}
    norms["l1"] = lambda h, y: abs(h) + abs(y)
    norms["l2"] = lambda h, y: math.hypot(h, y)
    norms["lp1.3"] = lambda h, y: (abs(h) ** 1.3 + abs(y) ** 1.3) ** (1 / 1.3)
    norms["l4"] = lambda h, y: (abs(h) ** 4 + abs(y) ** 4) ** 0.25
    # a non-smooth symmetric norm: max of two symmetric linear functionals
    norms["hex"] = lambda h, y: max(abs(y), 0.6 * abs(y) + 0.9 * abs(h), 1.2 * abs(h))
    return norms

viol = 0
worst_ratio = 1.0
for name, g in make_norms().items():
    for r in (10.0, 100.0, 1000.0):
        for h in (0.5, 1.0, 5.0, 0.1 * r, 0.4 * r):
            Fmid = g(h, r / 2) + g(-h, r / 2)
            for j in np.linspace(-3 * r, 4 * r, 1401):
                F = g(h, j) + g(-h, r - j)
                if F < Fmid - 1e-9 * Fmid:
                    viol += 1
                worst_ratio = min(worst_ratio, F / Fmid)
print("violations of  F(h,j) >= F(h,r/2)  over 5 norms x 3 scales x 5 offsets x 1401 j-values:", viol)
print("min observed F(h,j)/F(h,r/2) =", worst_ratio)
OUT["midpoint_minimality_violations"] = viol
OUT["midpoint_minimality_min_ratio"] = worst_ratio

# and the same check for a TILTED axis, where the reflection symmetry is NOT a lattice symmetry
sec("9b. Same check with a TILTED span (no reflection symmetry about the chord)")
def tilted_min_check(g, r, tilt, h):
    """x = r*(sin t, cos t)/|.|; measure F along the line at transversal offset h."""
    ux, uy = math.sin(tilt), math.cos(tilt)
    px, py = math.cos(tilt), -math.sin(tilt)      # unit transversal
    X = (r * ux, r * uy)
    Fmid = None
    Fmin, jmin = None, None
    for s in np.linspace(-3 * r, 4 * r, 2801):
        vx, vy = s * ux + h * px, s * uy + h * py
        F = g(vx, vy) + g(X[0] - vx, X[1] - vy)
        if Fmin is None or F < Fmin:
            Fmin, jmin = F, s
    vx, vy = (r / 2) * ux + h * px, (r / 2) * uy + h * py
    Fmid = g(vx, vy) + g(X[0] - vx, X[1] - vy)
    return Fmid, Fmin, jmin

for name, g in make_norms().items():
    for tilt in (0.0, 0.05, 0.3):
        Fmid, Fmin, jmin = tilted_min_check(g, 100.0, tilt, 5.0)
        print("norm=%-6s tilt=%.2f : F(mid)=%.6f  min_j F=%.6f  (deficit %.3e, argmin s=%.1f)"
              % (name, tilt, Fmid, Fmin, Fmid - Fmin, jmin))
print("=> for tilted spans the midpoint is NOT always the minimiser, so the free upgrade in 9")
print("   is available only for AXIS-ALIGNED spans (which is what every consumer uses).")

with open(os.path.join(HERE, "REFEREE3_check_output.json"), "w", encoding="utf-8") as f:
    json.dump(OUT, f, indent=1, default=str)
print("\nwrote REFEREE3_check_output.json")
