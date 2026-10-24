"""Numerical checks for the log-uniform counterexample to Hasebe-Ueda-Wang Problem 4.3.

mu_L(dx) = dx/(2 L x) on [e^-L, e^L], rho_L = mu_L boxtimes mu_L, g_L = density of log_* rho_L.

1. the branch: eta_rho(1 + i0) by two routes, (a) continuation of Q_L(w) = z from the negative axis along the upper
   unit semicircle, (b) the subordination fixed point omega = z h_mu(omega) iterated at z = 1 + i eps (no use of Q_L);
2. g_L''(0): closed form of the paper (phase function), complex derivatives of Q_L, finite differences of g_L;
3. g_L on its whole support by continuation: total mass, symmetry, the two maxima;
4. random matrices: log-eigenvalues of A^(1/2) U B U* A^(1/2), A, B with mu_L quantiles, U Haar unitary.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")
import cmath
import math
import sys

import mpmath as mp


mp.mp.dps = 40
L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
a = mp.e ** (-L)
af = math.exp(-L)


def q(w):
    E = mp.e ** (2 * L * w / (1 - w))
    return (1 - E) / (a - E / a)


def Q(w):
    return q(w) ** 2 / w


def qf(w):
    E = cmath.exp(2 * L * w / (1 - w))
    return (1 - E) / (af - E / af)


def Qf(w):
    return qf(w) ** 2 / w


def dQf(w, h=1e-7):
    return (Qf(w + h) - Qf(w - h)) / (2 * h)


def newton_f(z, w, it=60):
    for _ in range(it):
        f = Qf(w) - z
        d = dQf(w)
        step = f / d
        w -= step
        if abs(step) < 1e-15 * max(1.0, abs(w)):
            break
    return w


def newton_mp(z, w, it=100):
    for _ in range(it):
        f = Q(w) - z
        step = f / mp.diff(Q, w)
        w -= step
        if abs(step) < mp.mpf(10) ** (-35):
            break
    return w


out = []


def say(*x):
    s = " ".join(str(v) for v in x)
    print(s)
    out.append(s)


say("L =", L)

# ---- 1a. continuation from the negative axis, then along the upper unit semicircle
# near 0 on the negative axis eta(z) ~ m1 z with m1 = (E_mu x)^2
m1 = ((1 / af - af) / (2 * L)) ** 2
z = -1e-9
w = m1 * z
w = newton_f(z, complex(w))
for s in [10 ** (k / 20) for k in range(-180, 1)]:     # z = -s from -1e-9 to -1
    w = newton_f(complex(-s), w)
say("eta(-1) by continuation:", w)
n = 20000
for k in range(1, n + 1):                            # z = e^{i alpha}, alpha from pi down to 0
    al = math.pi * (1 - k / n)
    if al <= 0:
        break
    w = newton_f(cmath.exp(1j * al), w)
w_cont = w
say("eta(e^{i alpha}) at alpha = pi/%d:" % n, w_cont, "|w| =", abs(w_cont))


# ---- 1b. subordination: omega = z h(omega), h = eta_mu / omega, eta_rho(z) = eta_mu(omega)
def eta_mu(om):
    psi = (cmath.log(1 - af * om) - cmath.log(1 - om / af)) / (2 * L)
    return psi / (1 + psi)


def eta_rho_sub(z, om=None, it=200000):
    om = z if om is None else om
    for i in range(it):
        new = z * eta_mu(om) / om
        if abs(new - om) < 1e-14:
            return eta_mu(new), new, i
        om = 0.5 * om + 0.5 * new
    return eta_mu(om), om, -1


om = None
for eps in (0.5, 0.2, 0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001):
    ws, om, its = eta_rho_sub(complex(1, eps), om)
    say("subordination z = 1 + %g i: eta = %s  (iterations %d, Q(eta) - z = %.2e)"
        % (eps, ws, its, abs(Qf(ws) - complex(1, eps))))
w_sub = newton_f(1 + 0j, ws)
say("subordination root polished at z = 1:", w_sub)

# ---- 2. g''(0) three ways
ws_mp = newton_mp(mp.mpf(1), mp.mpc(w_cont))
tstar = mp.arg(ws_mp) / 2
say("w_* =", mp.nstr(ws_mp, 25), " t_* =", mp.nstr(tstar, 25), " |w_*| - 1 =", mp.nstr(abs(ws_mp) - 1, 5))
say("continuation root polished at z = 1 against the subordination root polished at z = 1: distance %.2e"
    % abs(complex(ws_mp) - w_sub))
t0 = mp.atan(L / mp.pi)
say("t_0 = arctan(L/pi) =", mp.nstr(t0, 15), " t_* > t_0:", tstar > t0, " t_* < pi/2:", tstar < mp.pi / 2)


def Pa(phi):
    return (1 - a ** 2) / (1 - 2 * a * mp.cos(phi) + a ** 2)


def beta(phi):                                       # continuous argument of B_a(e^{i phi}), beta(0) = 0
    return mp.quad(Pa, [0, phi])


def varphi(theta):
    return 2 * mp.pi - theta - 2 * beta(L * mp.cot(theta / 2))


th = 2 * tstar
say("varphi_L(theta_*) =", mp.nstr(varphi(th), 10), " (should be 0)")
A = mp.diff(varphi, th)
B = mp.diff(varphi, th, 2)
g2_closed = -(mp.csc(tstar) ** 2 / (4 * mp.pi * A ** 3)) * (B + A * mp.cot(tstar))
say("A =", mp.nstr(A, 15), " B =", mp.nstr(B, 15), " A > 1993/401:", A > mp.mpf(1993) / 401)
D = 1 - 2 * a * mp.cos(L * mp.cot(tstar)) + a ** 2
bracket2 = -mp.cot(tstar) + L ** 2 * a * (1 - a ** 2) * mp.sin(L * mp.cot(tstar)) / (D ** 2 * mp.sin(tstar) ** 4)
say("B + A cot t_* =", mp.nstr(B + A * mp.cot(tstar), 15), " cancellation formula:", mp.nstr(bracket2, 15))
C_L = a * (1 - a ** 2) * (L ** 2 + mp.pi ** 2) ** 2 / (L * (1 - a) ** 4)
say("C_L =", mp.nstr(C_L, 15), " F(L) =", mp.nstr(mp.e ** (-L) * (L ** 2 + 10) ** 2 / (L * (1 - mp.e ** (-L)) ** 4), 15))

d1 = mp.diff(Q, ws_mp)
d2 = mp.diff(Q, ws_mp, 2)
w1 = -1 / d1                                         # Q(w(y)) = e^{-y}: w' = -e^{-y}/Q'
w2 = (1 - d2 * w1 ** 2) / d1                         # w'' = (e^{-y} - Q'' w'^2)/Q'
G2 = w2 / (1 - ws_mp) ** 2 + 2 * w1 ** 2 / (1 - ws_mp) ** 3
g2_deriv = mp.im(G2) / mp.pi
say("g''(0): closed form %s, complex derivatives %s" % (mp.nstr(g2_closed, 15), mp.nstr(g2_deriv, 15)))


def g_at(y, wguess):
    wy = newton_mp(mp.e ** (-y), wguess)
    return mp.im(1 / (1 - wy)) / mp.pi, wy


h = mp.mpf("1e-4")
gp, _ = g_at(h, ws_mp)
g0, _ = g_at(mp.mpf(0), ws_mp)
gm, _ = g_at(-h, ws_mp)
say("g(0) =", mp.nstr(g0, 15), " g''(0) by finite differences (h = 1e-4):", mp.nstr((gp - 2 * g0 + gm) / h ** 2, 12),
    " g(h) - g(-h) =", mp.nstr(gp - gm, 5))

# ---- 3. the whole density by continuation from y = 0 in both directions
hstep = 0.0005


def sweep(sign):
    w = complex(ws_mp)                               # the root at z = 1, polished above
    ys, gs = [0.0], [(1 / (1 - w)).imag / math.pi]
    y = 0.0
    while True:
        y += hstep
        wn = newton_f(cmath.exp(-sign * y), w)
        if wn.imag < 1e-10 or abs(wn - w) > 0.2 or y > 2 * L + 1:
            break
        w = wn
        ys.append(y)
        gs.append((1 / (1 - w)).imag / math.pi)
    return ys, gs


yp, gpos = sweep(+1)
yn, gneg = sweep(-1)
mass = sum((gpos[i] + gpos[i + 1]) / 2 * hstep for i in range(len(gpos) - 1)) \
    + sum((gneg[i] + gneg[i + 1]) / 2 * hstep for i in range(len(gneg) - 1))
say("support of log_* rho reached by continuation: [-%.4f, %.4f]" % (yn[-1], yp[-1]))
say("total mass (trapezoid, edge cut where Im w < 1e-10): %.6f" % mass)
asym = max(abs(gpos[i] - gneg[i]) for i in range(min(len(gpos), len(gneg))))
say("max |g(y) - g(-y)| on the grid: %.2e" % asym)
imax = max(range(len(gpos)), key=lambda i: gpos[i])
say("g(0) = %.6f, max g = %.6f at y = +-%.4f, ratio g(0)/max = %.6f" % (gpos[0], gpos[imax], yp[imax], gpos[0] / gpos[imax]))
for yy in (0, 0.5, 1, 2, 3, 4, 6, 8, 10, 11):
    i = int(round(yy / hstep))
    if i < len(gpos):
        say("   g(%g) = %.6f" % (yy, gpos[i]))

# ---- 4. random matrices (optional, argument 'rmt')
if "rmt" in sys.argv:
    import numpy as np
    rng = np.random.default_rng(20261011)
    N, trials = 2000, 8
    x = np.exp(-L + 2 * L * (np.arange(N) + 0.5) / N)          # mu_L quantiles
    logs = []
    for _ in range(trials):
        Z = (rng.standard_normal((N, N)) + 1j * rng.standard_normal((N, N))) / math.sqrt(2)
        Qm, Rm = np.linalg.qr(Z)
        Qm = Qm * (np.diag(Rm) / np.abs(np.diag(Rm)))
        M = (np.sqrt(x)[:, None] * Qm) * x[None, :] @ Qm.conj().T * np.sqrt(x)[None, :]
        M = (M + M.conj().T) / 2
        ev = np.linalg.eigvalsh(M)
        logs.append(np.log(ev[ev > 0]))
    lg = np.concatenate(logs)
    say("RMT: N = %d, %d trials, %d log-eigenvalues, range [%.3f, %.3f]" % (N, trials, lg.size, lg.min(), lg.max()))
    hw = 1.0                                         # windows |y| < 1 and ||y| - y_max| < 1, folded by symmetry
    for c in (0.0, 2.0, 4.0, yp[imax], 9.0):
        lo, hi = (0.0, hw) if c == 0 else (c - hw, c + hw)
        frac = np.mean((np.abs(lg) >= lo) & (np.abs(lg) < hi)) / (2 * (hi - lo))
        i0, i1 = int(round(lo / hstep)), min(int(round(hi / hstep)), len(gpos) - 1)
        gavg = sum((gpos[i] + gpos[i + 1]) / 2 * hstep for i in range(i0, i1)) / (hi - lo)
        say("   window |y| in [%.3f, %.3f): RMT density %.5f, mean of g %.5f" % (lo, hi, frac, gavg))

open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "numerics_L%d.out" % L), "w", encoding="utf-8").write(
    "\n".join(out) + "\n")
