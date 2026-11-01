"""A general criterion for a convolution to be unimodal, and what it gives for stable laws.

Let p be a symmetric density, smooth and positive, strictly decreasing on (0, infinity), and set

    psi(x) = -(log|p'(x)|)' = -p''(x)/p'(x)     for x > 0.

CLAIM.  If mu is a probability measure whose support has diameter at most D, then mu * p is unimodal
provided
    sup { psi(a) + psi(b) : a, b > 0, a + b <= D }  <  0.

Reason: at a local minimum of the density with a local maximum on each side, translated to 0, the
reflected measure rho satisfies int p'(d) drho = 0 and int p''(d) drho >= 0, both linear in rho.  The
measures obeying the first form a convex compact set whose extreme points carry at most two atoms; a
single atom must sit where p' vanishes, i.e. at 0, where p''(0) < 0; and for a pair at -a and b the first
condition gives p |p'(a)| = q |p'(b)|, so the second becomes psi(a) + psi(b) >= 0 after dividing by
p|p'(a)|.  Both atoms lie in an interval of length D, so a + b <= D.

For the Gaussian of variance t, psi(x) = (x^2-t)/(tx), the supremum is attained at a = b = D/2 and equals
D/2 - 2t/D... which is negative exactly when t > D^2/4, recovering the sharp classical constant.

Scaling: for p_s(x) = p(x/s)/s one has psi_s(x) = psi(x/s)/s, so the criterion depends only on D/s, and
there is a constant c(p) with unimodality guaranteed whenever D < c(p) * s.  This computes c for the
symmetric stable laws with characteristic function exp(-|u|^alpha).
"""
import numpy as np
from scipy.integrate import quad


def stable_derivs(alpha):
    """p'(x) and p''(x) for the symmetric alpha-stable density with c.f. exp(-|u|^alpha)"""
    def p1(x):
        f = lambda u: -u * np.exp(-u ** alpha) * np.sin(u * x) / np.pi
        return quad(f, 0, np.inf, limit=400)[0]
    def p2(x):
        f = lambda u: -u * u * np.exp(-u ** alpha) * np.cos(u * x) / np.pi
        return quad(f, 0, np.inf, limit=400)[0]
    return p1, p2


def psi_of(alpha):
    p1, p2 = stable_derivs(alpha)
    def psi(x):
        a, b = p1(x), p2(x)
        if a >= 0: return np.inf          # p' must be negative on (0, inf)
        return -b / a
    return psi


def c_constant(alpha, rmax=8.0, n=260):
    """largest r such that psi(a)+psi(b) < 0 whenever a+b <= r"""
    psi = psi_of(alpha)
    xs = np.linspace(1e-3, rmax, n)
    vals = np.array([psi(x) for x in xs])
    def sup_on(r):
        best = -np.inf
        for i, a in enumerate(xs):
            if a >= r: break
            b = r - a                      # the supremum is on the boundary a+b=r when psi is increasing
            j = np.searchsorted(xs, b)
            if j >= len(xs): continue
            best = max(best, vals[i] + vals[j])
        return best
    lo, hi = 1e-3, rmax
    if sup_on(hi) < 0: return hi
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if sup_on(mid) < 0: lo = mid
        else: hi = mid
    return lo


if __name__ == '__main__':
    print("CONTROL: the Gaussian.  With variance 1 the criterion must give c = 2, i.e. D <= 2 sigma,")
    print("which is the sharp classical constant t >= D^2/4.")
    xs = np.linspace(1e-3, 6, 2000)
    psi_g = (xs ** 2 - 1) / xs
    def sup_g(r):
        a = xs[xs < r]; b = r - a
        return np.max((a ** 2 - 1) / a + (b ** 2 - 1) / b)
    lo, hi = 1e-3, 6.0
    for _ in range(60):
        mid = 0.5 * (lo + hi)
        if sup_g(mid) < 0: lo = mid
        else: hi = mid
    print(f"   computed c for the Gaussian: {lo:.5f}   (exact 2)")

    print("\nsymmetric stable laws, characteristic function exp(-|u|^alpha)")
    print(f"{'alpha':>7} {'c(alpha)':>10}   meaning: unimodal whenever the support diameter is below c*s")
    for alpha in (2.0, 1.8, 1.5, 1.2, 1.0, 0.8, 0.5):
        try:
            c = c_constant(alpha)
            print(f"{alpha:>7.2f} {c:>10.4f}", flush=True)
        except Exception as e:
            print(f"{alpha:>7.2f} {'failed':>10}  {e}", flush=True)
