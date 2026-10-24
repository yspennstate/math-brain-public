"""H0024: locating the critical constant of the one-sided and two-sided firework processes.

Radii: P(R >= m) = min(1, c/m).  Only the sites added at the previous step can extend the interval, so
the state is (g_right, g_left, N) and the growth laws are products that telescope into Gamma ratios:

  a new site at distance j inside the right end extends beyond it by (R - j)^+, so
  P(right growth <= s | g_R, g_L, N) = prod_{m=s+1}^{s+g_R}(1 - c/m) * prod_{m=s+N-g_L+1}^{s+N}(1 - c/m),
  and prod_{m=A}^{B}(1 - c/m) = Gamma(B+1-c)Gamma(A) / (Gamma(A-c)Gamma(B+1)).

Sampling by inverse c.d.f. with a binary search makes each step O(log), so the interval can be followed
to size 10^12 in about forty steps.  For the one-sided process the growth ratio U = g'/g satisfies
P(U < u) -> (u/(1+u))^c, whence E[log U] = psi(c) + gamma, zero exactly at c = 1: that is the control.
"""
import numpy as np, sys
from math import lgamma, log, inf
from scipy.special import digamma

def logprod(A, B, c):
    """log prod_{m=A}^{B} (1 - a(m)) with a(m) = c/(m+c), i.e. P(R >= m) = c/(m+c) ~ c/m.
    The shift keeps a(1) < 1 for every c > 0, which min(1, c/m) does not, and leaves the tail
    constant - the only thing the threshold depends on - unchanged."""
    if B < A: return 0.0
    return lgamma(B + 1) + lgamma(A + c) - lgamma(A) - lgamma(B + 1 + c)

def sample_growth(gR, gL, N, c, u, cfar=None):
    """smallest s >= 0 with P(growth <= s) >= u, growth of the RIGHT end"""
    def cdf(s):
        v = logprod(s + 1, s + gR, c)
        if gL > 0 and N > 0:
            v += logprod(s + N - gL + 1, s + N, c if cfar is None else cfar)
        return v
    if cdf(0) >= log(u): return 0
    lo, hi = 0, 1
    while cdf(hi) < log(u):
        lo, hi = hi, hi * 2
        if hi > 10 ** 15: return hi
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if cdf(mid) >= log(u): hi = mid
        else: lo = mid
    return hi

def trial(c, two_sided, nmax, rng, cL=None):
    cR = c; cL = c if cL is None else cL
    gR, gL, N = 1, (1 if two_sided else 0), 1
    while True:
        # the right end is extended by the right-new sites (rate cR) and the far left-new ones (also cR)
        nR = sample_growth(gR, gL, N, cR, rng.random())
        nL = sample_growth(gL, gR, N, cL, rng.random()) if two_sided else 0
        if nR == 0 and nL == 0:
            return N
        gR, gL = nR, nL
        N = N + nR + nL
        if N >= nmax:
            return N

if __name__ == '__main__':
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    rng = np.random.default_rng(4)
    print("P(interval reaches size N) for the one-sided and two-sided firework, radii tail c/m")
    print(f"{'c':>6} {'side':>10} " + " ".join(f"{10**e:>9.0e}" for e in (3, 5, 7, 9, 12)))
    for c in (0.5, 0.75, 0.9, 1.0, 1.1, 1.5):
        for two in (False, True):
            row = []
            for e in (3, 5, 7, 9, 12):
                nmax = 10 ** e
                hit = sum(1 for _ in range(trials) if trial(c, two, nmax, rng) >= nmax)
                row.append(hit / trials)
            print(f"{c:>6.2f} {'two' if two else 'one':>10} " + " ".join(f"{r:>9.4f}" for r in row))
    print("\ncontrol: one-sided drift E[log U] = psi(c) + gamma")
    for c in (0.5, 0.75, 0.9, 1.0, 1.1, 1.5):
        print(f"  c={c:.2f}  psi(c)+gamma = {digamma(c) + 0.5772156649015329:+.4f}")
