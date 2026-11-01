"""The log-uniform family mu_L boxtimes mu_L for a range of L: centre curvature sign, threshold L_c, number of modes.

For each L: t_* from tan((L/2) cot t) = tanh(L/2) cot(t/2) on (arctan(L/pi), pi/2); the bracket
B + A cot t_* = -cot t_* + L^2 a (1 - a^2) sin(phi) / (D^2 sin^4 t_*); g_L(0) = cot(t_*)/(2 pi);
the density g_L by continuation of W(e^{-y}) from y = 0 (Newton on Q_L(w) = e^{-y}); its mass and its local maxima.
Writes lscan.out and lscan_curves.json (for the figure).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
import cmath
import json
import math
import sys

import mpmath as mp


mp.mp.dps = 30
HERE = os.path.dirname(os.path.abspath(__file__))
out = []


def say(*x):
    s = " ".join(str(v) for v in x)
    print(s, flush=True)
    out.append(s)


def tstar(L):
    L = mp.mpf(L)
    k = mp.tanh(L / 2)
    f = lambda t: mp.tan(L / 2 * mp.cot(t)) - k * mp.cot(t / 2)
    lo, hi = mp.atan(L / mp.pi), mp.pi / 2
    # f(lo+) = +inf (tan near pi/2 from below), f(pi/2) = -k cot(pi/4) < 0: bisection on (lo, hi)
    a_, b_ = lo + mp.mpf(10) ** -25, hi
    for _ in range(200):
        m = (a_ + b_) / 2
        if f(m) > 0:
            a_ = m
        else:
            b_ = m
    return (a_ + b_) / 2


def bracket(L):
    L = mp.mpf(L)
    a = mp.e ** (-L)
    t = tstar(L)
    phi = L * mp.cot(t)
    D = 1 - 2 * a * mp.cos(phi) + a ** 2
    P = (1 - a ** 2) / D
    A = L / mp.sin(t) ** 2 * P - 1
    br = -mp.cot(t) + L ** 2 * a * (1 - a ** 2) * mp.sin(phi) / (D ** 2 * mp.sin(t) ** 4)
    g2 = -(1 / mp.sin(t) ** 2) / (4 * mp.pi * A ** 3) * br
    return t, A, br, g2


def density(L, hstep):
    af = math.exp(-L)

    def Qf(w):
        E = cmath.exp(2 * L * w / (1 - w))
        q = (1 - E) / (af - E / af)
        return q * q / w

    def newton(z, w):
        for _ in range(80):
            h = 1e-7
            d = (Qf(w + h) - Qf(w - h)) / (2 * h)
            step = (Qf(w) - z) / d
            w -= step
            if abs(step) < 1e-15:
                break
        return w

    t = float(tstar(L))
    w0 = cmath.exp(2j * t)
    ys, gs = [0.0], [(1 / (1 - w0)).imag / math.pi]
    w, y = w0, 0.0
    while True:
        y += hstep
        wn = newton(math.exp(-y), w)
        if wn.imag < 1e-10 or abs(wn - w) > 0.2 or y > 2 * L + 1:
            break
        w = wn
        ys.append(y)
        gs.append((1 / (1 - w)).imag / math.pi)
    mass = 2 * sum((gs[i] + gs[i + 1]) / 2 * hstep for i in range(len(gs) - 1))
    # local maxima of the even function on [0, y_max]: interior maxima, plus y = 0 if g decreases from 0
    maxima = [ys[i] for i in range(1, len(gs) - 1) if gs[i] > gs[i - 1] and gs[i] >= gs[i + 1]]
    if gs[1] < gs[0]:
        maxima = [0.0] + maxima
    return ys, gs, mass, maxima


if __name__ == "__main__":
    say("L     t_*            g''(0) sign of bracket   g(0)        modes (y >= 0)       mass      edge")
    curves = {}
    for L in [2, 3, 3.5, 4, 4.25, 4.5, 4.75, 5, 5.5, 6, 7, 8, 10, 12]:
        t, A, br, g2 = bracket(L)
        ys, gs, mass, maxima = density(L, 0.001)
        say("%-5g %.10f  %+.4e   %s   %.6f   %-20s %.6f  %.4f"
            % (L, float(t), float(g2), "neg (dip)" if br < 0 else "pos (peak)", float(mp.cot(t) / (2 * mp.pi)),
               ",".join("%.3f" % m for m in maxima), mass, ys[-1]))
        if L in (3, 4, 5, 6, 8):
            curves[str(L)] = {"y": ys[::5], "g": gs[::5]}
    # threshold: bracket changes sign
    lo, hi = mp.mpf(2), mp.mpf(6)
    assert bracket(lo)[2] > 0 and bracket(hi)[2] < 0
    for _ in range(80):
        m = (lo + hi) / 2
        if bracket(m)[2] > 0:
            lo = m
        else:
            hi = m
    say("threshold L_c (g''(0) = 0):", mp.nstr((lo + hi) / 2, 12))
    open(os.path.join(HERE, "lscan.out"), "w", encoding="utf-8").write("\n".join(out) + "\n")
    json.dump(curves, open(os.path.join(HERE, "lscan_curves.json"), "w", encoding="utf-8"))
