# -*- coding: utf-8 -*-
"""Referee 3, part 3: the LONGITUDINAL-OVERSHOOT clause - the repair I propose for the
far-j sites in the G-a union. It costs no curvature at all.

CLAIM. Let n support B_g at u* = u/g(u) and phi(y) := <y,n>/<u*,n>, so phi <= g everywhere and
phi(x) = g(x) (convexity only - no enclosing ball, no arc). For any v,
    g(v) + g(x-v) - g(x) = [g(v)-phi(v)] + [g(x-v)-phi(x-v)]  >=  max(0,-phi(v)) + max(0,-phi(x-v)).
For an axis-aligned span x = r e_2 we have n = e_2 and phi(y) = g(e_2) y_2, so a site whose
longitudinal coordinate is j = -m (behind the origin) or j = r+m (beyond the far endpoint) has
excess >= g(e_2) m - LINEAR in the overshoot, not quadratic.
CONSEQUENCE. Those sites are killed by the SAME three-way split at exponent
~ c1 g(e_2) m /(3 sqrt(C_L' r)); at m = delta r/2 that is c' delta sqrt(r) - stretched
exponential - so the union may be restricted to j in [-delta r/2, r + delta r/2], where the
Euclidean distance from v* to the SEGMENT [0,x] is at most delta r/sqrt(2) < delta r and the
hypothesis applies as literally written. No offset reading, no widened arc, no constant loss.
"""
import math
import numpy as np


def sec(t):
    print("\n" + "=" * 78); print(t); print("=" * 78)


NORMS = {
    "l1": lambda h, y: abs(h) + abs(y),
    "l2": lambda h, y: math.hypot(h, y),
    "lp1.3": lambda h, y: (abs(h) ** 1.3 + abs(y) ** 1.3) ** (1 / 1.3),
    "l4": lambda h, y: (abs(h) ** 4 + abs(y) ** 4) ** 0.25,
    "hex": lambda h, y: max(abs(y), 0.6 * abs(y) + 0.9 * abs(h), 1.2 * abs(h)),
    "mix": lambda h, y: 0.5 * math.hypot(h, y) + 0.5 * (abs(h) ** 4 + abs(y) ** 4) ** 0.25,
}

sec("1. axis-aligned span: excess >= g(e_2) * overshoot, for EVERY norm (convexity only)")
r = 200.0
rho = 2.0
worst = None
for name, g in NORMS.items():
    gamma = g(0.0, 1.0)
    for d in (0.0, 1.0, 20.0, 60.0):
        for m in (1.0, 5.0, 25.0, 100.0):
            for j in (-m, r + m):
                exc = g(d, j) + g(-d, r - j) - g(0.0, r)
                ratio = exc / (gamma * m)
                if worst is None or ratio < worst[0]:
                    worst = (ratio, name, d, m, j)
print("min over all (norm, offset d, overshoot m, side) of  excess/(g(e2)*m) :")
print("   %.6f   at norm=%s d=%.0f m=%.0f j=%.0f" % worst)
print("   (claim needs >= 1.0)")

sec("2. tilted spans: same claim with the support functional at the tilted direction")
print("%-8s %6s %12s %12s" % ("norm", "tilt", "min ratio", "needs >= 1"))
for name, g in NORMS.items():
    for tilt in (0.0, 0.05, 0.2):
        ux, uy = math.sin(tilt), math.cos(tilt)
        px, py = math.cos(tilt), -math.sin(tilt)
        X = (r * ux, r * uy)
        gx = g(*X)
        gu = gx / r                      # = g(u) for the unit direction u
        mn = None
        for d in (0.0, 1.0, 20.0, 60.0):
            for m in (1.0, 5.0, 25.0, 100.0):
                for s in (-m, r + m):
                    vx, vy = s * ux + d * px, s * uy + d * py
                    exc = g(vx, vy) + g(X[0] - vx, X[1] - vy) - gx
                    ratio = exc / (gu * m)
                    mn = ratio if mn is None else min(mn, ratio)
        print("%-8s %6.2f %12.5f %12s" % (name, tilt, mn, "OK" if mn >= 1 - 1e-9 else "LOSS"))
print("(a tilted span costs the cross term d*<p,n>; with d <= delta r/2 and overshoot")
print(" m = delta r/2 the loss is a constant factor, never the order.)")

sec("3. what the far-j term costs in Form A")
print("exponent for a far-j site at overshoot m = delta r/2, next to the MAIN exponent")
print("%8s %8s %8s %10s %14s %14s" % ("r", "delta", "c1", "g(e2)", "far-j expo", "main expo (top)"))
for r_ in (1e6, 1e10, 1e14):
    for delta in (0.1, 1.0):
        c1, gamma, c_, rho_ = 0.2, 1.4, 0.2, 2.0
        CL = 2 + rho_
        cpp = c1 / (6 * math.sqrt(CL))
        C3 = 2.0
        far = c1 * (gamma * delta * r_ / 2 - C3 * math.sqrt(r_) * math.log(r_)) / (3 * math.sqrt(CL * r_))
        s2_top = delta ** 2 * math.sqrt(r_) / 4
        main = cpp * c_ * s2_top
        s2_cons = 50.0                     # a consumer-scale polylog quantile
        main_cons = cpp * c_ * s2_cons
        print("%8.0e %8.2f %8.2f %10.2f %14.4g %14.4g   (at a polylog quantile sigma^2=50 the main exponent is %.4g)"
              % (r_, delta, c1, gamma, far, main, main_cons))
print("=> at every consumed (polylog) quantile the far-j term exp(-c sqrt r) is negligible")
print("   against the main term exp(-c'' c_- polylog); only at the extreme top of the range are")
print("   the two comparable, and there both are stretched-exponential in sqrt(r).")
