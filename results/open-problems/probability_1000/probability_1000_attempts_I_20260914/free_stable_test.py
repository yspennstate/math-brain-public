"""Is a free alpha-stable law freely strongly unimodal?

The reduction leaves Hasebe and Ueda's Problem 3.11 open only for measures attracted to a free stable law
of index other than one and two, so the question is whether some unimodal nu has lambda_alpha box+ nu not
unimodal.

Test measure: nu = 0.1 U[0,0.05] + 0.9 U[0,16], which is nonincreasing on [0,infinity) and so unimodal,
and whose CAUCHY convolution is bimodal (verified separately).  Since lambda_1 box+ nu = nu * C_1, the
index alpha = 1 is a positive control: the method must report two modes there.  G_nu is elementary,
G(z) = sum_i (w_i/a_i) log(z/(z-a_i)), and G for the free stable law is solved from K(G) = z.

Free convolution by the Belinschi and Bercovici subordination iteration.
"""
import numpy as np, cmath, sys
from free_stable import R_stable


def G_nu(ws, as_):
    def G(z):
        return sum((w / a) * (cmath.log(z) - cmath.log(z - a)) for w, a in zip(ws, as_))
    return G


def F_stable(alpha):
    """F = 1/G for the symmetric free alpha-stable law.

    The Newton solve for K(G) = z is unreliable close to the real axis, so each evaluation walks down in
    the imaginary direction from a height where 1/z is a good start.  The shared warm start of the first
    version poisoned the whole run: one NaN propagated to every later point, and the alpha = 1 control
    caught it.
    """
    R = R_stable(alpha)
    K = lambda w: 1.0 / w + R(w)
    def solve(z, w):
        for _ in range(120):
            h = 1e-9 * max(1.0, abs(w))
            f = K(w) - z
            d = (K(w + h) - K(w - h)) / (2 * h)
            if d == 0 or not cmath.isfinite(d): return None
            step = f / d
            w = w - step
            if w.imag > -1e-14: w = complex(w.real, -abs(w.imag) - 1e-14)
            if not cmath.isfinite(w): return None
            if abs(step) < 1e-13 * max(1.0, abs(w)): return w
        return w
    def F(z):
        Y = max(4.0, 4.0 * abs(z))
        w = 1.0 / complex(z.real, Y)
        ys = np.geomspace(Y, max(z.imag, 1e-9), 40)
        for y in ys:
            w = solve(complex(z.real, y), w)
            if w is None: return complex('nan')
        return 1.0 / w
    return F


def density(alpha, ws, as_, xs, eps=1e-5, iters=600):
    G1 = G_nu(ws, as_)
    F1 = lambda w: 1.0 / G1(w)
    F2 = F_stable(alpha)
    out = []
    for x in xs:
        z = complex(x, eps)
        w1 = z
        for _ in range(iters):
            w2 = F1(w1) - w1 + z
            if w2.imag < eps: w2 = complex(w2.real, eps)
            nw1 = F2(w2) - w2 + z
            if nw1.imag < eps: nw1 = complex(nw1.real, eps)
            if abs(nw1 - w1) < 1e-12 * max(1.0, abs(nw1)):
                w1 = nw1; break
            w1 = nw1
        out.append(-G1(w1).imag / np.pi)
    return np.array(out)


def modes(xs, f, tol=1e-11):
    up = np.diff(f) > tol
    return int(np.sum(up[:-1] & ~up[1:]))


if __name__ == '__main__':
    ws, as_ = [0.10, 0.90], [0.05, 16.0]
    xs = np.linspace(-25, 45, int(sys.argv[1]) if len(sys.argv) > 1 else 1400)
    print("nu = 0.1 U[0,0.05] + 0.9 U[0,16], unimodal with mode 0")
    print(f"{'alpha':>7} {'modes':>6} {'peak':>10}   (alpha = 1 is the control and must show 2)")
    for a in (1.0, 1.5, 1.8, 1.2, 0.8, 0.5):
        f = density(a, ws, as_, xs)
        print(f"{a:>7.2f} {modes(xs, f):>6} {np.nanmax(f):>10.6f}", flush=True)
