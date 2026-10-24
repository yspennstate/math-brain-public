"""The level law of a Hamming slice converges to an arcsine law (the proof of the slice statement in NOTES section 4).

g = 1{|y| = t} on N bits, lambda_k = W_k(g) / E g.  lambda_k = w(k) p_t(k)^2 with w = Binomial(N, 1/2) and p_t the t-th
orthonormal Krawtchouk polynomial, so the moments of lambda are diagonal entries of powers of the Krawtchouk Jacobi matrix
(b = N/2, a_n^2 = n (N - n + 1) / 4).  Claim: for t / N -> rho the law of k / N converges to the arcsine law on
[1/2 - sqrt(rho(1-rho)), 1/2 + sqrt(rho(1-rho))], whose central moments are E (X - 1/2)^{2r} = C(2r, r) (rho(1-rho)/4)^r.

Checks, each by two independent paths:
  A. central moments r = 1..4 exactly (Fractions): direct Krawtchouk sum against walks on the integer matrix
     T (T[n][n+1] = 1, T[n+1][n] = (n+1)(N-n), zero diagonal), which is similar to 2(J - N/2); then the limit.
  B. mass at levels k <= c ln(1/eps): exact (slice_levels.row) against the arcsine law at the finite-N point c ln(1/eps)/N
     and at the limit point c (ln 2 - H_e(rho)).
  C. c_min(rho) = (1/2 - sqrt(rho(1-rho))) / (ln 2 - H_e(rho)) on a grid: >= 1/2 everywhere and -> 1/2 at rho = 1/2.
Usage: python slice_limit.py OUTJSON
"""
import os, sys, json, math
from fractions import Fraction
from math import comb, log, sqrt, asin, pi
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import slice_levels as SL


def moments_kraw(N, t, rmax):
    K = SL.kraw_all(N, t)
    den = (2 ** N) * comb(N, t)
    out = []
    for r in range(1, rmax + 1):
        # lambda_k = C(N,t) K_k(t)^2 / (2^N C(N,k)); central moment of k - N/2 (times 2^{2r}: (2k - N)^{2r})
        s = Fraction(0)
        for k in range(N + 1):
            s += Fraction(comb(N, t) * K[k] * K[k] * (2 * k - N) ** (2 * r), (2 ** N) * comb(N, k))
        out.append(s)  # = E (2k - N)^{2r}
    return out


def moments_walk(N, t, rmax):
    """E (2k - N)^{2r} = e_t^T T^{2r} e_t, T tridiagonal integer, similar to 2(J - N/2)."""
    out = []
    for r in range(1, rmax + 1):
        m = 2 * r
        v = {t: 1}
        for _ in range(m):
            nv = {}
            for n, x in v.items():
                if n + 1 <= N:  # e_n -> column n of T: T[n+1][n] = (n+1)(N-n)
                    nv[n + 1] = nv.get(n + 1, 0) + (n + 1) * (N - n) * x
                if n - 1 >= 0:  # T[n-1][n] = 1
                    nv[n - 1] = nv.get(n - 1, 0) + x
            v = nv
        out.append(Fraction(v.get(t, 0)))
    return out


def arcsine_cdf(x, rho):
    s = sqrt(rho * (1 - rho))
    lo, hi = 0.5 - s, 0.5 + s
    if x <= lo:
        return 0.0
    if x >= hi:
        return 1.0
    return (2 / pi) * asin(sqrt((x - lo) / (hi - lo)))


def He(r):
    return -(r * log(r) + (1 - r) * log(1 - r))


def c_min(rho):
    return (0.5 - sqrt(rho * (1 - rho))) / (log(2) - He(rho))


def main():
    out = dict(A=[], B=[], C=[])
    # A: moments
    for (N, t) in ((200, 40), (800, 160), (2000, 400), (800, 280), (2000, 700)):
        mk, mw = moments_kraw(N, t, 4), moments_walk(N, t, 4)
        rho = t / N
        for r in range(4):
            lim = comb(2 * (r + 1), r + 1) * (rho * (1 - rho) / 4) ** (r + 1)
            val = float(mk[r]) / (2 * N) ** (2 * (r + 1))  # E (k/N - 1/2)^{2r}
            out["A"].append(dict(N=N, t=t, r=r + 1, kraw_equals_walk=(mk[r] == mw[r]), central_moment=val, arcsine_limit=lim,
                                 ratio=val / lim))
            print(f"A N={N:5d} t={t:4d} r={r+1}  kraw==walk {mk[r] == mw[r]}  E(k/N-1/2)^{2*(r+1)} = {val:.6e}  arcsine {lim:.6e}  ratio {val/lim:.5f}")
    for (N, t) in ((10 ** 5, 2 * 10 ** 4), (10 ** 6, 2 * 10 ** 5)):
        mw = moments_walk(N, t, 4)
        rho = t / N
        for r in range(4):
            lim = comb(2 * (r + 1), r + 1) * (rho * (1 - rho) / 4) ** (r + 1)
            val = float(mw[r]) / (2 * N) ** (2 * (r + 1))
            out["A"].append(dict(N=N, t=t, r=r + 1, kraw_equals_walk=None, central_moment=val, arcsine_limit=lim, ratio=val / lim))
            print(f"A N={N:7d} t={t:6d} r={r+1}  walk only  ratio {val/lim:.7f}")
    # B: masses below c ln(1/eps)
    for (N, rho) in ((200, 0.2), (800, 0.2), (2000, 0.2), (4000, 0.2), (8000, 0.2), (2000, 0.35), (4000, 0.35), (2000, 0.05)):
        t = int(round(rho * N))
        R = SL.row(N, t)
        L = R["ln_inv_eps"]
        for c0, key in ((0.5, "below050"), (0.55, "below055")):
            fin = arcsine_cdf(c0 * L / N, t / N)
            lim = arcsine_cdf(c0 * (log(2) - He(t / N)), t / N)
            out["B"].append(dict(N=N, t=t, c=c0, exact=R[key], arcsine_at_finite_N=fin, arcsine_limit=lim))
            print(f"B N={N:5d} rho={t/N:.3f} c<={c0}: exact {R[key]:.4e}  arcsine(c L/N) {fin:.4e}  limit {lim:.4e}")
    # C: c_min on a grid
    grid = [k / 1000 for k in range(1, 500)]
    vals = [c_min(r) for r in grid]
    out["C"] = dict(min_over_grid=min(vals), argmin=grid[vals.index(min(vals))], at=[(r, c_min(r)) for r in (0.05, 0.2, 0.35, 0.45, 0.49, 0.499)])
    print("C min c_min on grid", min(vals), "at rho", grid[vals.index(min(vals))], [(r, round(c_min(r), 6)) for r in (0.05, 0.2, 0.35, 0.45, 0.49, 0.499)])
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
