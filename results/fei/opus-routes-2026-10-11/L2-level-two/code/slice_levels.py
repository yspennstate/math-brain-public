"""Where does the Fourier mass of a derivative sit, measured in units of ln(1/eps)?  (sharpness of the 1/2 threshold)

f = 1 - 2 * 1{#(-1 coords) <= t} on n = N + 1 variables.  D_i f = +-1{|y| = t} on N variables (a Hamming slice), and
W_k(D_i f) = C(N,t)^2 K_k(t; N)^2 / (4^N C(N,k)), K_k Krawtchouk (exact integers, three-term recurrence).  eps = C(N,t) / 2^N.
For each (N, t) report the level law lambda_k = W_k / eps in units c = k / ln(1/eps): its mean, quantiles, and the mass
below c = 0.45, 0.5, 0.55.  Usage: python slice_levels.py OUTJSON
"""
import sys, json, math
from math import comb, log


def kraw_all(N, x):
    K = [1, N - 2 * x]
    for k in range(1, N):
        nxt = ((N - 2 * x) * K[k] - (N - k + 1) * K[k - 1])
        assert nxt % (k + 1) == 0
        K.append(nxt // (k + 1))
    return K


def row(N, t):
    K = kraw_all(N, t)
    four = 4 ** N
    eps_num = comb(N, t)
    # fhat_s(U) = 2^-N K_t(|U|) = 2^-N C(N,t) K_k(t) / C(N,k)  (symmetry C(N,t) K_k(t) = C(N,k) K_t(k)), so
    # W_k = C(N,t)^2 K_k(t)^2 / (4^N C(N,k)) and lambda_k = W_k / eps = C(N,t) K_k(t)^2 / (2^N C(N,k))
    lam = [eps_num * K[k] * K[k] / ((2 ** N) * comb(N, k)) for k in range(N + 1)]
    tot = sum(lam)
    L = N * log(2) - log(eps_num)  # math.log takes big ints; a float quotient overflows at N ~ 2000
    cs = [k / L for k in range(N + 1)]
    mean_c = sum(c * l for c, l in zip(cs, lam))
    def mass_below(c0):
        return sum(l for c, l in zip(cs, lam) if c <= c0)
    def quant(qq):
        s = 0.0
        for c, l in zip(cs, lam):
            s += l
            if s >= qq:
                return c
        return cs[-1]
    return dict(N=N, t=t, rho=t / N, ln_inv_eps=L, total=tot, mean_c=mean_c, q10=quant(0.1), q50=quant(0.5), q90=quant(0.9),
                below045=mass_below(0.45), below050=mass_below(0.5), below055=mass_below(0.55),
                c_min_asymptotic=(0.5 - math.sqrt((t / N) * (1 - t / N))) / (log(2) + (t / N) * log(t / N) + (1 - t / N) * log(1 - t / N)))


def main():
    out = []
    grid = [(N, rho) for N in (200, 800, 2000) for rho in (0.05, 0.2, 0.35, 0.42, 0.46)] + [(4000, 0.2), (4000, 0.35), (8000, 0.2)]
    for N, rho in grid:
        if True:
            t = int(round(rho * N))
            out.append(row(N, t))
            r = out[-1]
            print(f"N={N:5d} rho={r['rho']:.3f} ln(1/eps)={r['ln_inv_eps']:8.2f} sum={r['total']:.6f}  c: mean={r['mean_c']:.3f} q10={r['q10']:.3f} q50={r['q50']:.3f} q90={r['q90']:.3f}  mass(c<=.45)={r['below045']:.3e} (c<=.5)={r['below050']:.3e} (c<=.55)={r['below055']:.3e}", flush=True)
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
