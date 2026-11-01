"""sigma_t boxtimes nu for nu = (delta_{1/10} + delta_{10})/2, for a range of t.

1. The four roots of Lemma 4.1 (3) of Hasebe, Ueda and Wang at the angle used in the paper
   (t > 8: sin R / R = 8/t, level 1/8; t <= 8: R = sqrt(t)/2), counted as sign changes on a grid in u = log r.
2. The density g_t of log_*(sigma_t boxtimes nu) computed independently of Lemma 4.1, by subordination:
   eta_rho = eta_nu o omega, where omega(z) solves omega * Sigma_t(eta_nu(omega)) = z and
   Sigma_t(w) = exp((t/2)(w+1)/(w-1)). omega is continued from z = -1 (omega = -1) along the upper unit
   semicircle to z = e^{0.05 i}, then along z = e^{-y + 0.05 i}, and at each y down to z = e^{-y + 1e-10 i}
   by halving the angle; g_t(y) = Im(1/(1 - eta_rho)) / pi.
   Reported: mass; the mean against e^{t/2}(10 + 1/10)/2; the local maxima of g_t on y >= 0; g_t(0) / max g_t;
   points where the computed branch has the wrong sign; the largest deviation of |eta_rho| from 1 on the unit
   circle (rho = rho^{-1}, so |eta_rho| = 1 there).
Writes thmB_density.out, and thmB_curves.json (every fifth grid point of each density, for the figure).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import cmath
import json
import math
import sys


HERE = os.path.dirname(os.path.abspath(__file__))
out = []


def say(*x):
    s = " ".join(str(v) for v in x)
    print(s, flush=True)
    out.append(s)


A = math.log(10.0)


def psi(z):
    return 0.5 * (z / (10 - z) + 10 * z / (1 - 10 * z))


def dpsi(z):
    return 0.5 * (10 / (10 - z) ** 2 + 10 / (1 - 10 * z) ** 2)


def eta(z):
    p = psi(z)
    return p / (1 + p)


def deta(z):
    p = psi(z)
    return dpsi(z) / (1 + p) ** 2


def F(om, z, t):
    e = eta(om)
    return om * cmath.exp(0.5 * t * (e + 1) / (e - 1)) - z


def dF(om, t):
    e = eta(om)
    E = cmath.exp(0.5 * t * (e + 1) / (e - 1))
    return E * (1 + om * 0.5 * t * (-2 * deta(om) / (e - 1) ** 2))


def newton(z, om, t, it=80):
    for _ in range(it):
        step = F(om, z, t) / dF(om, t)
        om -= step
        if abs(step) < 1e-13 * max(1.0, abs(om)):
            return om, True
    return om, False


DELTA = 0.05     # height (angle) of the continuation path above the positive half-line
EPS = 1e-10      # final height


EDGE = [0]       # points where the descent stopped short of EPS (next to a support edge)


def descend(y, om, t, h_from, h_to):
    # Newton from angle h_from down to angle h_to at fixed modulus e^{-y}. The path stays in the upper
    # half-plane, where omega is analytic and d_omega F does not vanish; each step starts from the first-order
    # predictor omega + dz / F_omega and shrinks the angle by a factor 1/2, or by less when Newton fails (next to a
    # support edge, where omega has a square-root branch point on the real line). Below angle 1e-7 a failure ends
    # the descent there; the density is then read at that angle.
    h = h_from
    z = cmath.exp(complex(-y, h))
    while h > h_to:
        r = 0.5
        while True:
            hn = max(h * r, h_to)
            zn = cmath.exp(complex(-y, hn))
            pred = om + (zn - z) / dF(om, t)
            omn, ok = newton(zn, pred, t)
            if ok and omn.imag > -1e-12:
                break
            r = 1 - (1 - r) / 2
            if r > 0.999 or h < 1e-7:
                if h < 1e-7:
                    EDGE[0] += 1
                    return om
                raise RuntimeError("descent failed at y = %g, angle %g" % (y, h))
        om, h, z = omn, hn, zn
    return om


def density(t, h=0.004):
    om = -1.0 + 0j
    circ = 0.0
    n = 6000
    for k in range(1, n + 1):                       # z = e^{i alpha}, alpha from pi down to DELTA
        al = math.pi - (math.pi - DELTA) * k / n
        om, ok = newton(cmath.exp(1j * al), om, t)
        if not ok:
            raise RuntimeError("circle continuation failed at alpha = %g" % al)
        circ = max(circ, abs(abs(eta(om)) - 1))
    ymax = 0.5 * t + 3 * math.log(2 + t) + 8
    ys, gs, top = [], [], []
    bad = 0
    y = 0.0
    while y <= ymax:
        om, ok = newton(cmath.exp(complex(-y, DELTA)), om, t)
        if not ok:
            raise RuntimeError("continuation at angle DELTA failed at y = %g" % y)
        omb = descend(y, om, t, DELTA, EPS)
        g = (1 / (1 - eta(omb))).imag / math.pi
        if omb.imag < -1e-12 or g < -1e-12:
            bad += 1
        ys.append(y)
        gs.append(g)
        top.append(om)
        y += h
    return ys, gs, top, h, bad, circ


def roots_lemma41(t):
    if t > 8:
        lo, hi = 1e-12, math.pi - 1e-15             # sin R / R decreasing from 1 to 0
        for _ in range(200):
            m = 0.5 * (lo + hi)
            if math.sin(m) / m > 8 / t:
                lo = m
            else:
                hi = m
        R = 0.5 * (lo + hi)
    else:
        R = math.sqrt(t) / 2
    lam = R / (t * math.sin(R))
    c = math.cos(R)

    def Fr(u):
        k = lambda s: 1 / (2 * (math.cosh(s) - c))
        return 0.5 * (k(u - A) + k(u + A))

    us = [-30 + 60 * i / 600000 for i in range(600001)]
    vals = [Fr(u) - lam for u in us]
    ch = [0.5 * (us[i] + us[i + 1]) for i in range(len(us) - 1) if (vals[i] > 0) != (vals[i + 1] > 0)]
    win = (Fr(0), Fr(A))
    return R, lam, win, ch


if __name__ == "__main__":
    ts = [float(x) for x in sys.argv[1:]] or [0.05, 0.5, 2, 3, 4, 5, 6, 7, 8, 10, 12, 5 * math.pi, 20, 30, 50, 100]
    curves = {}
    say("nu = (delta_{1/10} + delta_{10})/2; Sigma_t(w) = exp((t/2)(w+1)/(w-1))")
    say("")
    say("Lemma 4.1 (3): angle R, level lambda = R/(t sin R), window (F_R(0), F_R(log 10)), sign changes of F_R - lambda")
    for t in ts:
        R, lam, win, ch = roots_lemma41(t)
        say("t = %-9.5g R = %.6f  lambda = %.6f  window (%.6f, %.6f)  roots in u: %s"
            % (t, R, lam, win[0], win[1], ", ".join("%.4f" % u for u in ch)))
    say("")
    say("density of log_*(sigma_t boxtimes nu) by subordination (even in y; y >= 0 shown)")
    for t in ts:
        ys, gs, top, h, bad, circ = density(t)
        curves["%g" % t] = {"y": [round(v, 6) for v in ys[::5]], "g": [float("%.8g" % v) for v in gs[::5]]}
        gmax = max(gs)
        tol = 1e-7 * gmax       # off the support the computed Im is of the order of the final angle 1e-10
        mass = 2 * sum((gs[i] + gs[i + 1]) / 2 * h for i in range(len(gs) - 1))
        # mean of sigma_t boxtimes nu is e^{t/2} (10 + 1/10)/2; g is even, so the mean is the integral of 2 cosh(y) g(y) over y >= 0
        mean = sum((math.cosh(ys[i]) * gs[i] + math.cosh(ys[i + 1]) * gs[i + 1]) * h for i in range(len(gs) - 1))
        mean_exact = math.exp(t / 2) * 5.05
        maxima = [ys[i] for i in range(1, len(gs) - 1) if gs[i] > gs[i - 1] + tol and gs[i] >= gs[i + 1] - tol and gs[i] > tol]
        if gs[1] < gs[0] - tol:
            maxima = [0.0] + maxima
        last = max(i for i in range(len(gs)) if gs[i] > tol)
        gaps, inside = [], False
        for i in range(last):
            if gs[i] <= tol and not inside:
                inside, s0 = True, ys[i]
            elif gs[i] > tol and inside:
                inside = False
                gaps.append((s0, ys[i]))
        minima = [ys[i] for i in range(1, len(gs) - 1) if gs[i] < gs[i - 1] - tol and gs[i] <= gs[i + 1] + tol and gs[i] > tol]
        if gs[1] > gs[0] + tol and gs[0] > tol:
            minima = [0.0] + minima
        say("t = %-9.5g mass %.6f  mean/exact %.6f  support edge y = %.3f  gaps %s  maxima at y = %s  minima at y = %s  g(0) = %.6g  max g = %.6g  g(0)/max %.6f  wrong-sign points %d  edge-stopped points %d  max ||eta| - 1| on the circle %.1e"
            % (t, mass, mean / mean_exact, ys[last], ", ".join("(%.3f, %.3f)" % g for g in gaps) or "none",
               ", ".join("%.4f" % m for m in maxima), ", ".join("%.4f" % m for m in minima) or "none",
               gs[0], gmax, gs[0] / gmax, bad, EDGE[0], circ))
        EDGE[0] = 0
    open(os.path.join(HERE, os.environ.get("THMB_OUT", "thmB_density.out")), "w", encoding="utf-8").write("\n".join(out) + "\n")
    json.dump(curves, open(os.path.join(HERE, "thmB_curves.json"), "w", encoding="utf-8"))
