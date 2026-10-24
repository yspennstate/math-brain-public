"""Level-entropy constant kappa_lev = sup R(eps, m) over admissible (eps, m), in bits:
    R(eps, m) = h(eps)/(eps m) + h(1/m),   eps = 1 - fhat(0)^2 = 4p(1-p),  m = I/eps >= 1,
    edge isoperimetry: I >= 2 p log2(1/p)  (p = min(Pr[f=1], Pr[f=-1]) <= 1/2),  i.e.  m >= log2(1/p) / (2(1-p)).
H(|S|) = h(eps) + eps H(|S| given S nonempty) <= h(eps) + eps m h(1/m)  (geometric maximises entropy at given mean),
so H(|S|) <= kappa_lev I for every Boolean function.  For fixed eps, dR/dm = -(h(eps)/eps + log2(m-1))/m^2, so the
maximum over m >= m_min is at m* = max(m_min, 1 + 2^(-h(eps)/eps)).  Evaluated with mpmath on a fine grid of p,
followed by a Lipschitz-safe refinement (reported both).
"""
from mpmath import mp, mpf, log, sqrt, nstr

mp.dps = 30


def h(x):
    x = mpf(x)
    if x <= 0 or x >= 1:
        return mpf(0)
    return -(x * log(x, 2) + (1 - x) * log(1 - x, 2))


def R_at_p(p):
    p = mpf(p)
    eps = 4 * p * (1 - p)
    mmin = max(mpf(1), log(1 / p, 2) / (2 * (1 - p)))
    m_star = max(mmin, 1 + mpf(2) ** (-h(eps) / eps))
    return h(eps) / (eps * m_star) + h(1 / m_star), eps, m_star


if __name__ == "__main__":
    best = (mpf(0), None)
    # p = 2^-x, x in (1, 60]
    N = 20000
    for i in range(1, N + 1):
        x = 1 + mpf(59) * i / N
        p = mpf(2) ** (-x)
        r, eps, m = R_at_p(p)
        if r > best[0]:
            best = (r, (x, eps, m))
    r, (x, eps, m) = best
    print("kappa_lev (grid over p = 2^-x, 20000 points, x in (1,60]) = %s at x = %s (p = %s), eps = %s, m* = %s"
          % (nstr(r, 12), nstr(x, 8), nstr(mpf(2) ** (-x), 8), nstr(eps, 8), nstr(m, 8)))
    # refine around the maximiser
    lo, hi = x - mpf(59) / N * 2, x + mpf(59) / N * 2
    for it in range(60):
        a = lo + (hi - lo) / 3; b = hi - (hi - lo) / 3
        if R_at_p(mpf(2) ** (-a))[0] < R_at_p(mpf(2) ** (-b))[0]:
            lo = a
        else:
            hi = b
    print("refined maximum %s at x = %s" % (nstr(R_at_p(mpf(2) ** (-lo))[0], 15), nstr(lo, 12)))
    # tail behaviour and p close to 1/2
    for x in [1.0001, 1.5, 2, 3, 4, 5, 6, 6.5, 7, 8, 10, 20, 40, 60]:
        r, eps, m = R_at_p(mpf(2) ** (-mpf(x)))
        print("x=%6.3f p=%.3e R=%s m*=%s" % (x, float(mpf(2) ** (-mpf(x))), nstr(r, 10), nstr(m, 8)))
