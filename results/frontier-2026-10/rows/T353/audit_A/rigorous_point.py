"""T353 audit: a rigorous (ball-arithmetic, python-flint arb) proof of the one-point inequality I_SAME(g1) > I_ANTI(g1).
Model (same as check_t2_grid.py; sigma = 1, eps = 1/2, E = e^eps): at fixed g1 the step-2 integrand is
  f(x) = u phi(x) + v (phi(x - a) - E phi(x - c)),  u = (phi(g1 + 2) - E phi(g1 + 1))/2,  v = phi(g1)/2,
ANTI (a, c) = (2, 1), SAME (a, c) = (0, -1), and I(g1) = integral of max(f, 0) dx.
f/phi(x) = u + v(e^{a x - a^2/2} - E e^{c x - c^2/2}), so the sign changes are closed form:
  ANTI: with y = e^x, v e^-2 y^2 - v E e^-1/2 y + u = 0 (f > 0 outside the roots when v > 0);
  SAME: one root x0 = -1/2 - log((u + v)/(v E)), f > 0 above it.
Each I is then a combination of Phi values at the roots, F(x) = u Phi(x) + v Phi(x - a) - v E Phi(x - c).
ANTI integrates to D(P_S||Q_S) exactly (flip g1 -> -g1), I is continuous in g1, so SAME > ANTI at one g1 gives a set of positive
measure where the adaptive switch gains, hence D(M(x)||M(x')) > D_{e^eps}(P_S||Q_S). argv: g1 values (decimal strings)."""
import sys
from flint import arb, ctx
ctx.prec = 200
E = arb("0.5").exp(); pi2 = (2 * arb.pi()).sqrt()
phi = lambda x: (-x * x / 2).exp() / pi2
Phi = lambda x: (1 + (x / arb(2).sqrt()).erf()) / 2


def parts(g1):
    return (phi(g1 + 2) - E * phi(g1 + 1)) / 2, phi(g1) / 2


def I_anti(g1):
    u, v = parts(g1); A = v * arb(-2).exp(); B = -v * E * arb("-0.5").exp(); disc = B * B - 4 * A * u
    F = lambda x: u * Phi(x) + v * Phi(x - 2) - v * E * Phi(x - 1)
    tot = u + v - v * E
    if disc < 0: return tot, "no root"
    assert disc > 0, "discriminant ball straddles 0: raise precision"
    yl, yh = (-B - disc.sqrt()) / (2 * A), (-B + disc.sqrt()) / (2 * A)
    if u < 0:  # one positive root: f > 0 above it only
        xh = yh.log(); return tot - F(xh), f"one root {xh.mid().str(8)}"
    assert u > 0 and yl > 0, "u ball straddles 0: raise precision"
    xl, xh = yl.log(), yh.log()
    return F(xl) + (tot - F(xh)), f"roots {xl.mid().str(8)} {xh.mid().str(8)}"


def I_same(g1):
    u, v = parts(g1)
    if u + v < 0: return arb(0), "f < 0 everywhere"
    r = (u + v) / (v * E); assert r > 0, "u + v ball straddles 0"
    x0 = arb("-0.5") - r.log()
    return (u + v) * (1 - Phi(x0)) - v * E * (1 - Phi(x0 + 1)), f"root {x0.mid().str(8)}"


for s in (sys.argv[1:] or ["-2.5", "-3", "-2", "0"]):
    g1 = arb(s); a, ra = I_anti(g1); b, rb = I_same(g1); d = b - a
    sign = "SAME > ANTI (proved)" if d > 0 else ("ANTI > SAME (proved)" if d < 0 else "undecided")
    print(f"g1={s}: I_ANTI={a.str(12)} ({ra})  I_SAME={b.str(12)} ({rb})  diff={d.str(10, radius=True)}  -> {sign}", flush=True)
