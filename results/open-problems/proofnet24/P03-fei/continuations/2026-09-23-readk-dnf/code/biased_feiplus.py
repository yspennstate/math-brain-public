"""Biased FEI+ (O'Donnell-Tan) for read-k DNFs:  H_mu[F^{>=1}] <= C (Inf_mu[F] - Var_mu[F]).
H_mu[F^{>=1}] = sum_{S != empty} Ft(S)^2 log2( prod_{i in S} sigma_i^2 / Ft(S)^2 ),
Ft = mu-biased Fourier coefficients (basis phi_i = (x_i - mu_i)/sigma_i), Inf_mu = sum |S| Ft(S)^2.
Also reports the plain biased entropy ratio for comparison.
"""
import math, numpy as np
from feicore import popcounts, polite
from readk_nonmono import random_nonmono
from termref import random_readk, random_regular, star_terms


def biased_coeffs(F, mu):
    """F: +-1 values on {-1,1}^n (bit i of index = 1 means x_i = -1). mu_i = E x_i.
    Returns Ft(S) for all S (index = mask)."""
    n = len(mu)
    a = F.astype(np.float64).reshape([2] * n)       # axis order: bit n-1 ... bit 0 (C order)
    p = (1 + np.asarray(mu)) / 2                      # Pr[x_i = +1]
    for i in range(n):
        ax = n - 1 - i
        s = math.sqrt(1 - mu[i] ** 2)
        # value at x_i=+1 is index 0 (bit 0), x_i=-1 is index 1
        v0 = np.take(a, 0, axis=ax)
        v1 = np.take(a, 1, axis=ax)
        # E[F] component: p v0 + (1-p) v1 ; phi component: E[F phi_i] = p v0 (1-mu)/s + (1-p) v1 (-1-mu)/s
        c0 = p[i] * v0 + (1 - p[i]) * v1
        c1 = p[i] * v0 * (1 - mu[i]) / s + (1 - p[i]) * v1 * (-1 - mu[i]) / s
        a = np.stack([c0, c1], axis=ax)
    return a.reshape(-1)


def feiplus(n, terms, mu):
    N = 1 << n
    xs = np.arange(N, dtype=np.int64)
    sat = np.zeros(N, dtype=bool)
    for (m, v) in terms:
        sat |= (xs & m) == v
    F = np.where(sat, -1, 1)
    Ft = biased_coeffs(F, mu)
    P = Ft ** 2
    pc = popcounts(n)
    sig2 = 1 - np.asarray(mu) ** 2
    logsig = np.zeros(N)
    for i in range(n):
        logsig += ((xs >> i) & 1) * math.log2(sig2[i])
    mask = (P > 1e-300) & (xs > 0)
    Hplus = float((P[mask] * (logsig[mask] - np.log2(P[mask]))).sum())
    Inf = float((P * pc).sum())
    Var = float(P[1:].sum())
    Hfull = float(-(P[P > 1e-300] * np.log2(P[P > 1e-300])).sum())
    return Hplus, Inf, Var, Hfull


if __name__ == '__main__':
    polite()
    rng = np.random.default_rng(31)
    # sanity: total mass 1
    worst = {}
    for n, k, wl in [(10, 2, [2, 3, 3, 4, 2, 3]), (12, 2, [3] * 8), (12, 3, [2, 3, 3, 4, 4, 2, 3, 5, 2]),
                     (14, 3, [3, 3, 4, 4, 5, 3, 4, 5]), (12, 4, [2, 2, 3, 3, 4, 2, 3, 4, 2, 3])]:
        for r in range(10):
            terms = random_nonmono(n, k, wl, rng, pneg=float(rng.choice([0.0, 0.5])))
            for mode in ('uniform', 'random', 'extreme'):
                if mode == 'uniform':
                    mu = np.zeros(n)
                elif mode == 'random':
                    mu = rng.uniform(-0.95, 0.95, size=n)
                else:
                    mu = rng.choice([-0.995, -0.9, 0.9, 0.995, 0.0], size=n)
                Hp, Inf, Var, Hf = feiplus(n, terms, mu)
                excess = Inf - Var
                ratio = Hp / excess if excess > 1e-12 else (0.0 if Hp < 1e-9 else float('inf'))
                key = (k, mode)
                w = worst.setdefault(key, [0.0, None])
                if ratio > w[0]:
                    w[0] = ratio
                    w[1] = (n, round(Hp, 5), round(excess, 5), round(Var, 4))
    for key in sorted(worst):
        print('read-%d %-8s max H+/(Inf-Var) = %.3f  at %s' % (key[0], key[1], worst[key][0], worst[key][1]), flush=True)
