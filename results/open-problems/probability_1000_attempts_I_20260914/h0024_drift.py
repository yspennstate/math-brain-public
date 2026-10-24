"""The scaling limit of the two-sided firework, and the drift that decides survival.

Write N for the interval's length, g_R and g_L for the numbers of sites added at the two ends in the
last step, alpha = g_R/N, beta = g_L/N.  A site added at the right end at distance j inside it extends
the interval iff its right reach exceeds j, and a site added at the LEFT end, at distance about N, does
too iff its right reach exceeds that.  With P(R >= m) = c/m both blocks contribute, and for large N

    P(growth_R <= uN) -> [u/(u+alpha)]^c * [(u+1-beta)/(u+1)]^c,

the first factor from the near block and the second from the far one.  The far factor is the mutual
help between the two ends: at u -> 0 it leaves an atom of mass (1-beta)^c, so a right end that has just
stopped is revived with probability 1-(1-beta)^c per step while the left end still adds beta*N sites.
Iterating (alpha, beta) and averaging log(N'/N) gives the drift: positive means the interval grows
geometrically and the process survives, negative means it dies.

Control: with beta = 0 the law reduces to P(U <= u) = (u/(1+u))^c for U = g'/g, whose log-mean is
psi(c) + gamma - the classical one-sided drift, zero exactly at c = 1.
"""
import numpy as np, sys
from scipy.special import digamma
GAMMA = 0.5772156649015329

def sample_V(c, alpha, beta, u):
    """smallest v>0 with F(v) >= u, F(v) = [v/(v+alpha)]^c [(v+1-beta)/(v+1)]^c"""
    if alpha <= 0 and beta <= 0: return 0.0
    def F(v):
        if v <= 0: return 0.0
        a = (v / (v + alpha)) ** c if alpha > 0 else 1.0
        b = ((v + 1 - beta) / (v + 1)) ** c if beta > 0 else 1.0
        return a * b
    if F(1e-300) >= u: return 0.0
    lo, hi = 0.0, 1.0
    while F(hi) < u:
        hi *= 2.0
        if hi > 1e12: return hi
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if F(mid) >= u: hi = mid
        else: lo = mid
    return hi

def drift(c, two_sided, steps=200000, seed=3, burn=2000):
    rng = np.random.default_rng(seed)
    a, b = (0.5, 0.5) if two_sided else (1.0, 0.0)
    tot, n = 0.0, 0
    for k in range(steps):
        vR = sample_V(c, a, b, rng.random())
        vL = sample_V(c, b, a, rng.random()) if two_sided else 0.0
        g = 1.0 + vR + vL
        if vR + vL <= 0: return None          # absorbed in the limit (does not happen for c>0)
        if k >= burn:
            tot += np.log(g); n += 1
        a, b = vR / g, vL / g
    return tot / n

if __name__ == '__main__':
    steps = int(sys.argv[1]) if len(sys.argv) > 1 else 60000
    print("drift of log(interval length) per step in the scaling limit")
    print(f"{'c':>6} {'one-sided':>11} {'psi(c)+gamma':>13} {'two-sided':>11}")
    for c in (0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0, 1.1):
        d1 = drift(c, False, steps)
        d2 = drift(c, True, steps)
        print(f"{c:>6.2f} {d1:>11.4f} {digamma(c)+GAMMA:>13.4f} {d2:>11.4f}")
