# The characteristic function of the single hub itself, phi_Q(eta) = E exp(i eta (2 X_h L + lam V^2 + 2 eps L P)), for
# comb light laws on the spread frame (Gaussian cells, lattice part exact) and a comb hub of Nh teeth of width 1/Nh at
# the integers, centred. Given the lattice point z and the hub value x, the cell integral is Gaussian in (L, V, P) with
# the quadratic phase eta(lam V^2 + 2 eps L P) and the linear phase 2 eta x L: closed form. The hub is integrated by
# Gauss-Legendre inside each tooth. Prints eta |phi_Q(eta)| on a log grid: if it stays of order one, the transform is
# not integrable although the density is bounded.
import sys, math, time
import numpy as np
from jperp import triple_law, rot

N = int(sys.argv[1]); Nh = int(sys.argv[2]); eps = float(sys.argv[3]) if len(sys.argv) > 3 else 0.0
which = sys.argv[4] if len(sys.argv) > 4 else "irr"
fine = len(sys.argv) > 5 and sys.argv[5] == "fine"
lam = 1.0
R = rot([1, 2, 0], math.atan(math.sqrt(2))) @ rot([0, 1, 3], math.atan(math.sqrt(3))) if which == "irr" else \
    rot([3, -1, 2], math.atan(math.sqrt(5))) @ rot([1, 1, 1], math.atan(math.sqrt(7)))
z, p = triple_law(N)
Y = z @ R / math.sqrt(8.0) * (2.0 / N if fine else 1.0); L0, V0, P0 = Y[:, 0], Y[:, 1], Y[:, 2]
if fine:
    Y = Y - (p[:, None] * Y).sum(axis=0); L0, V0, P0 = Y[:, 0], Y[:, 1], Y[:, 2]
s2 = 1.0 / (12.0 * N * N)
gx, gw = np.polynomial.legendre.leggauss(6)
xs = ((2.0 * np.arange(Nh)[:, None] + (gx[None, :] + 1) / 2) / Nh).ravel() - 1.0 if fine else (np.arange(Nh)[:, None] + (gx[None, :] + 1) / (2 * Nh)).ravel() - Nh / 2.0
ws = np.tile(gw / 2.0, Nh) / Nh           # hub weights: density 1 on each tooth of width 1/Nh, total mass 1
etas = np.exp(np.linspace(math.log(0.05), math.log(4.0 / s2 ** 0.5 * 3), 400))
out = []
t0 = time.time()
for eta in etas:
    # cell G ~ N(0, s2 I_3) in (L, V, P); phase eta*lam*(V0+G2)^2 + 2 eta eps (L0+G1)(P0+G3) + 2 eta x (L0+G1)
    # V-part: E exp(i a (V0 + G)^2) = (1 - 2 i a s2)^{-1/2} exp(i a V0^2 / (1 - 2 i a s2)), a = eta lam
    a = eta * lam
    cv = np.exp(1j * a * V0 ** 2 / (1 - 2j * a * s2)) / np.sqrt(1 - 2j * a * s2)
    # (L, P)-part with bilinear phase k G1 G3 (k = 2 eta eps) and linear coefficients al = 2 eta (x + eps P0), ga = 2 eta eps L0
    k = 2 * eta * eps; den = 1.0 + k * k * s2 * s2
    tot = 0j
    for xi, wi in zip(xs, ws):
        al = 2 * eta * (xi + eps * P0); ga = 2 * eta * eps * L0
        lp = np.exp(1j * (2 * eta * xi * L0 + 2 * eta * eps * L0 * P0)) / math.sqrt(den) * \
             np.exp(-(s2 * (al * al + ga * ga) + 2j * k * s2 * s2 * al * ga) / (2 * den))
        tot += wi * np.dot(p, cv * lp)
    out.append((eta, abs(tot)))
out = np.array(out)
print("N=%d Nh=%d eps=%g frame=%s %s points=%d (%.0fs)" % (N, Nh, eps, which, "fine combs in [0,2]" if fine else "combs at the integers", len(p), time.time() - t0))
for lo, hi in [(0.05, 1), (1, 3), (3, 10), (10, 30), (30, 100), (100, 300), (300, 1e9)]:
    m = (out[:, 0] >= lo) & (out[:, 0] < hi)
    if m.any():
        e, f = out[m, 0], out[m, 1]
        print("  eta in [%g, %g): mean eta|phi| = %.3f, max eta|phi| = %.3f, mean |phi| eta^{3/2} = %.3f" % (lo, hi, (e * f).mean(), (e * f).max(), (e ** 1.5 * f).mean()))
# the integral of |phi| over the grid (trapezoid in log eta)
le = np.log(out[:, 0]); integ = np.trapezoid(out[:, 1] * out[:, 0], le)
print("  int_{0.05}^{max} |phi_Q| d eta = %.3f (twice this bounds 2 pi ||p_Q|| from above only if it converges)" % integ)
