# Exact inner integral for the T=2 best-of-two value of the shuffled-ABLQ paper.
# g(s) = A phi(s) + be phi(s-a) - E be phi(s-c), A = al - E ga. g(s)/phi(s) = A + be e^{as-a^2/2} - E be e^{cs-c^2/2}
# is a sum of three exponentials, so it has at most two real roots; on each interval where g > 0 the integral of g is
# a combination of normal CDF differences. The outer integral over z is then smooth enough for quad at 1e-13.
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import ndtr
from scipy.stats import norm
E = np.exp(0.5)
phi = norm.pdf
GRID = np.linspace(-60, 60, 24001)

def I(a, c, al, be, ga):
    A = al - E * ga
    h = lambda s: A + be * np.exp(a * s - a * a / 2) - E * be * np.exp(c * s - c * c / 2)
    hv = h(GRID)
    roots = [brentq(h, GRID[i], GRID[i + 1], xtol=1e-15, rtol=1e-15)
             for i in range(len(GRID) - 1) if hv[i] == 0 or hv[i] * hv[i + 1] < 0]
    edges = [-np.inf] + roots + [np.inf]
    tot = 0.0
    for l, u in zip(edges, edges[1:]):
        mid = (max(l, -70) + min(u, 70)) / 2 if np.isfinite(l) or np.isfinite(u) else 0.0
        if h(mid) <= 0:
            continue
        P = lambda m: ndtr(u - m) - ndtr(l - m)
        tot += A * P(0) + be * P(a) - E * be * P(c)
    return tot

def w2(z):
    return 0.5 * phi(z - 2), 0.5 * phi(z), 0.5 * phi(z - 1)

pair_f = lambda z: I(2, 1, *w2(z))
anti_f = lambda z: I(0, -1, *w2(z))
diff = lambda z: anti_f(z) - pair_f(z)
for z in [1.9, 1.99, 2.0, 2.01, 2.1, 5.0, 11.955, 15.0]:
    print("z=%.3f  SAME-ANTI = % .6e" % (z, diff(z)), flush=True)
pc = [-14.0, -6.0, -2.0, 0.0, 1.0, 2.0, 3.0, 4.5, 7.0, 10.0, 16.0]
pair = sum(quad(pair_f, a, b, limit=200, epsabs=1e-14, epsrel=1e-12)[0] for a, b in zip(pc, pc[1:]))
gc = [2.0, 2.5, 3.0, 4.0, 5.5, 7.5, 10.0, 16.0]
gain = sum(quad(diff, a, b, limit=200, epsabs=1e-14, epsrel=1e-12)[0] for a, b in zip(gc, gc[1:]))
best_direct = sum(quad(lambda z: max(pair_f(z), anti_f(z)), a, b, limit=200, epsabs=1e-14, epsrel=1e-12)[0]
                  for a, b in zip(pc, pc[1:]))
print("pair %.12f  gain %.12e  best %.12f  best(direct max) %.12f" % (pair, gain, pair + gain, best_direct), flush=True)
