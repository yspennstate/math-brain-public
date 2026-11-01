"""Is there a sharp diameter constant for free convolution with a free stable law?

For the semicircle the answer is the theorem proved today: mu box+ S(0,t) is unimodal exactly from
t = D^2, and since S(0,t) has scale sqrt(t), that says D <= scale, a constant of 1.  Free convolution with
a stable law of scale s obeys the same scaling, D < c_free(alpha) * s, so the constant exists for every
alpha and the question is its value.

The symmetric two-atom measure is extremal in the semicircle case, so it is the natural probe: for each
alpha, bisect on D for the largest diameter at which (delta_{-D/2} + delta_{D/2})/2 box+ lambda_alpha stays
unimodal, with lambda_alpha the symmetric free stable law of R-transform -i(iw)^{alpha-1}, which is the
semicircle of variance one at alpha = 2 and the standard Cauchy at alpha = 1.

CONTROL: alpha = 2 must return 1.
"""
import numpy as np, cmath, sys
from free_stable_test import F_stable


def G_two(D):
    return lambda z: 0.5 / (z + D / 2) + 0.5 / (z - D / 2)


def density(alpha, D, xs, eps=1e-5, iters=400):
    G1 = G_two(D)
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
            if abs(nw1 - w1) < 1e-12 * max(1.0, abs(nw1)): w1 = nw1; break
            w1 = nw1
        out.append(-G1(w1).imag / np.pi)
    return np.array(out)


def interior_maxima(xs, f):
    d = np.diff(f)
    return [i + 1 for i in range(len(d) - 1) if d[i] > 0 and d[i + 1] <= 0]


def unimodal(alpha, D, n=260):
    span = D / 2 + 8.0
    xs = np.linspace(-span, span, n)
    f = density(alpha, D, xs)
    return len(interior_maxima(xs, f)) <= 1


def c_free(alpha, lo=0.2, hi=6.0, steps=11):
    if not unimodal(alpha, lo): return float('nan')
    for _ in range(steps):
        mid = 0.5 * (lo + hi)
        if unimodal(alpha, mid): lo = mid
        else: hi = mid
    return lo


if __name__ == '__main__':
    print("largest diameter D at which the symmetric pair stays unimodal after free convolution")
    print("with the stable law of index alpha and scale one; alpha = 2 must give 1")
    print(f"{'alpha':>7} {'c_free':>9}")
    for a in ([float(x) for x in sys.argv[1:]] or [2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.5]):
        print(f"{a:>7.2f} {c_free(a):>9.4f}", flush=True)
