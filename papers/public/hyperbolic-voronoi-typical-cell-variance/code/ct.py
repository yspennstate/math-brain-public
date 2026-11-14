"""E area(C_2 minus T_2(R1)) in the natural coupling (D'Achille et al., Section 5.3), d = 2, truncated to |u| < U.
Upper half-plane, o = (0, 1). Given R1, C removes half-discs (x, rho) with intensity kappa dx drho / rho^3 on
1 + x^2 >= rho^2, T(R1) removes all of them, kappa = 2 R1 / pi (so that the discs containing o number Pois(R1)).
For z = (u, v): P(z in C, z notin T | kappa) = exp(-kappa (pi/(2v) - I)) (1 - exp(-kappa I)), I = I(u, v) the
dx drho / rho^3 measure of discs containing both z and o. Averaging over R1 ~ Exp(1):
    E area(C \\ T) = int du dv / v^2 [1 / (1 + 1/v - 2I/pi) - 1 / (1 + 1/v)].
For |u| large I ~ 2/|u|, so the integral over |u| < U grows like (8/pi) log U.
Each window edge U is a panel boundary of the u rule, the arctangents are evaluated as positive atan2 tails, and the
bracket is written as c / ((1 + 1/v)(1 + 1/v - c)), so no step subtracts nearly equal numbers. Usage: python ct.py"""
import math
import numpy as np


def gl_pieces(cuts, n):
    g, w = np.polynomial.legendre.leggauss(n); xs, ws = [], []
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        xs.append((lo + hi) / 2 + (hi - lo) / 2 * g); ws.append((hi - lo) / 2 * w)
    return np.concatenate(xs), np.concatenate(ws)


def I(u, v):                        # u > 0; pi/2 + arctan z = atan2(1, -z), pi/2 - arctan z = atan2(1, z)
    xs = (u * u + v * v - 1) / (2 * u)
    return 0.5 * (np.arctan2(1.0, (u - xs) / v) / v + np.arctan2(1.0, xs))


def check_I(u, v):                  # brute force for the closed form; the two tails beyond |x| = 4000 add 1/4000
    x = np.linspace(-4000, 4000, 4_000_001)
    f = 0.5 / np.maximum((x - u) ** 2 + v * v, x * x + 1)
    return float(np.trapezoid(f, x)) + 1 / 4000


def inner(u, V):                    # int_0^inf dv / v^2 [...] at fixed u > 0
    v, w = V
    c = 2 * I(u, v) / math.pi
    q = 1 + 1 / v
    br = c / (q * (q - c))
    return float((w * br / v ** 2).sum())


def window_volumes(Ucuts, n_v=40, n_u=30):
    vc = [0, 1e-3, 1e-2, 0.1, 0.3, 1, 3, 10, 30, 100, 1e3, 1e4, 1e5, 1e6, 1e7]
    V = gl_pieces(vc, n_v)
    # tail of v: beyond 1e7 the bracket is O(1/v), the integrand O(1/v^3): negligible
    cuts = sorted(set([0.0, 1e-6, 1e-3, 0.03, 0.3, 1, 3] + [3 * 2 ** k for k in range(1, 28)] + list(Ucuts)))
    out = {}
    total = 0.0
    for lo, hi in zip(cuts[:-1], cuts[1:]):
        uu, ww = gl_pieces([lo, hi], n_u)
        total += 2 * float(sum(w * inner(u, V) for u, w in zip(uu, ww)))     # both signs of u
        if hi in Ucuts:
            out[hi] = total
    return out


if __name__ == '__main__':
    for u, v in [(0.3, 0.5), (2.0, 0.7), (5.0, 3.0), (50.0, 1.0)]:
        print(f'I({u},{v}) closed {I(u, v):.8f} brute {check_I(u, v):.8f}  u*I={u * I(u, v):.5f}')
    Us = [10.0, 100.0, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8]
    A = window_volumes(Us)
    B = window_volumes(Us, n_v=60, n_u=45)
    for U in Us:
        print(f'U={U:<8g} E area(C\\T; |u|<U) = {B[U]:.9f}   minus (8/pi) log U = {B[U] - 8 / math.pi * math.log(U):.9f}'
              f'   (coarser rule {A[U] - 8 / math.pi * math.log(U):.9f})')
    V = gl_pieces([0, 1e-3, 1e-2, 0.1, 0.3, 1, 3, 10, 30, 100, 1e3, 1e4, 1e5, 1e6, 1e7], 40)
    print('u * inner(u) at large u (should tend to 4/pi = %.6f):' % (4 / math.pi), [round(u * inner(u, V), 6) for u in (1e2, 1e3, 1e4, 1e5)])
