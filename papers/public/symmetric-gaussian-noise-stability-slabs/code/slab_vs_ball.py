"""Joint exceedances of the slab and the ball at equal Gaussian measure 1 - eps, in R^n.

J_slab = P(|X_1| > t, |Y_1| > t) with 2 Phibar(t) = eps, J_ball = P(|X| > r, |Y| > r) with P(chi^2_n > r^2) = eps,
X, Y standard Gaussian in R^n with correlation rho. Prints both, their ratio, the ratio divided by
t^{(n-1)(1-rho)/(1+rho)} (Theorem 1.1 says it is bounded below), and the explicit bounds of Lemmas 3.1 and 3.2 so that
L_slab <= J_slab and J_ball <= U_ball can be read off. Usage: python slab_vs_ball.py
"""
import math
import numpy as np
from scipy import integrate, optimize, special, stats


def phibar(x):
    return 0.5 * special.erfc(x / math.sqrt(2))


def chi2_sf(n, q):
    return special.gammaincc(n / 2, q / 2)


def j_slab(t, rho):
    s = math.sqrt(1 - rho * rho)
    f = lambda x: stats.norm.pdf(x) * (phibar((t - rho * x) / s) + phibar((t + rho * x) / s))
    scale = stats.norm.pdf(t)
    val, _ = integrate.quad(lambda x: f(x) / scale, t, t + 40, limit=400, epsabs=0, epsrel=1e-12)
    return 2 * val * scale


def j_ball(r, rho, n):
    # condition on R = |X| > r; |Y|^2 / (1 - rho^2) is noncentral chi^2_n with noncentrality rho^2 R^2 / (1 - rho^2)
    v = 1 - rho * rho
    dens = lambda R: stats.chi.pdf(R, n)
    g = lambda R: dens(R) * stats.ncx2.sf(r * r / v, n, rho * rho * R * R / v)
    scale = dens(r)
    val, _ = integrate.quad(lambda R: g(R) / scale, r, r + 40, limit=400, epsabs=0, epsrel=1e-12)
    return val * scale


def lower_slab(t, rho):
    """Lemma 3.1: J_slab >= 2 P(|D_1| <= 1/t) P(S_1 > 2t + 1/t), S_1 ~ N(0, 2(1+rho)), D_1 ~ N(0, 2(1-rho))."""
    sd, ss = math.sqrt(2 * (1 - rho)), math.sqrt(2 * (1 + rho))
    return 2 * (1 - 2 * phibar(1 / (t * sd))) * phibar((2 * t + 1 / t) / ss)


def upper_ball(r, rho, n):
    """Lemma 3.2: P(|D| > 2r) + P(|v|^2 > g r^2) + E P(|S|^2 > s^2), with g = 4/(1+rho) and
    s^2 = 4 r^2 - |v|^2 + 2 sqrt(4 - g) r |w|; w ~ N(0, 2(1-rho)), v ~ N(0, 2(1-rho) I_{n-1}) independent."""
    sig2 = 2 * (1 - rho)
    g = 4 / (1 + rho)
    p1 = chi2_sf(n, 4 * r * r / sig2)
    p2 = chi2_sf(n - 1, g * r * r / sig2)
    c = math.sqrt(4 - g) * r

    def inner(q, w):  # q = |v|^2
        s2 = 4 * r * r - q + 2 * c * abs(w)
        return chi2_sf(n, s2 / (2 * (1 + rho)))

    # integrate over w (normal) and q = |v|^2 = sig2 * chi^2_{n-1}, restricted to q <= g r^2
    wq = lambda w: stats.norm.pdf(w, scale=math.sqrt(sig2))
    qd = lambda q: stats.chi2.pdf(q / sig2, n - 1) / sig2
    base = chi2_sf(n, 4 * r * r / (2 * (1 + rho)))
    f = lambda q, w: wq(w) * qd(q) * inner(q, w) / base
    val, _ = integrate.dblquad(f, 0, 60 * math.sqrt(sig2), 0, g * r * r, epsabs=0, epsrel=1e-8)
    return p1 + p2 + 2 * val * base   # factor 2: w ranges over both signs


def main():
    print("n rho eps t r J_slab J_ball ratio ratio/t^e L_slab/J_slab J_ball/U_ball")
    for n in (2, 3):
        for rho in (0.1, 0.5, 0.9):
            e = (n - 1) * (1 - rho) / (1 + rho)
            for k in (2, 4, 8, 16, 32):
                eps = 10.0 ** (-k)
                t = optimize.brentq(lambda x: 2 * phibar(x) - eps, 0, 40)
                r = optimize.brentq(lambda x: chi2_sf(n, x * x) - eps, 0, 40)
                js, jb = j_slab(t, rho), j_ball(r, rho, n)
                ls, ub = lower_slab(t, rho), upper_ball(r, rho, n)
                print(f"{n} {rho} 1e-{k} {t:.4f} {r:.4f} {js:.4e} {jb:.4e} {js / jb:.4f} {js / jb / t ** e:.4f} "
                      f"{ls / js:.4f} {jb / ub:.4f}")


if __name__ == "__main__":
    main()
