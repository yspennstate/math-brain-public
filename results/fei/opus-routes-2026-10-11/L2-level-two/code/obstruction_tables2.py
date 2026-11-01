"""Exact tables for O3 (product-reference template on AND_a tensor powers) and O5 (Lemma 1 summed over levels on tribes).

O3: g = AND_a (+-1), p_g(empty) = (1 - 2^(1-a))^2, p_g(S) = 4^(1-a) for S nonempty.  f = product of M = 2^(a-2)
    disjoint copies.  Level generating function L_f(z) = L_g(z)^M.  I(f) = a/2, H(f) = M H(g), eps_i = 2^(1-a).
    Phi(f) = sum_i eps_i log2(1/eps_i) + sum_k W_k log2(I^k / (k! W_k))   (Gibbs bound, Phi >= H).
O5: tribes with s blocks of width w (f = -1 iff some block is all-true).  D_i f has level generating function
    P(z) Q(z)^(s-1),  P = 4^-(w-1) (1+z)^(w-1),  Q = (1 - 2^-w)^2 + 4^-w ((1+z)^w - 1).
    Lemma 1 summed:  S1 = sum_i sum_j psi(d_{j,i}),  psi(x) = x log2(e/x).
    H(tribes) exactly: p(S) depends only on a(S) = number of blocks S meets (S nonempty).
Usage: python obstruction_tables2.py OUTJSON
"""
import sys, json, math
import numpy as np
from math import comb, log2, lgamma, log


def poly_pow(c, M):
    """coefficients of c(z)^M by repeated squaring, with fft convolution and clipping."""
    from scipy.signal import fftconvolve
    res = np.array([1.0])
    base = np.array(c, dtype=float)
    while M:
        if M & 1:
            res = np.clip(fftconvolve(res, base), 0, None)
        M >>= 1
        if M:
            base = np.clip(fftconvolve(base, base), 0, None)
    return res


def ent_terms(W):
    W = np.asarray(W, float)
    m = W > 1e-300
    return W, m


def o3_row(a):
    M = 2 ** (a - 2)
    p0 = (1 - 2.0 ** (1 - a)) ** 2
    q = 4.0 ** (1 - a)
    Lg = np.array([q * comb(a, k) for k in range(a + 1)])
    Lg[0] = p0
    W = poly_pow(Lg, M)
    W = W / W.sum()  # exact total is 1; renormalise fft round-off
    k = np.arange(len(W))
    I = a / 2.0
    eps = 2.0 ** (1 - a)
    first = M * a * eps * log2(1 / eps)
    m = W > 1e-300
    logfact = np.array([lgamma(kk + 1) / log(2) for kk in k])
    second = float(np.sum(W[m] * (k[m] * log2(I) - logfact[m] - np.log2(W[m]))))
    Hg = -p0 * log2(p0) - (2 ** a - 1) * q * log2(q)
    H = M * Hg
    return dict(a=a, M=M, I=I, H_over_I=H / I, Phi_over_I=(first + second) / I, first_over_I=first / I,
                second_over_I=second / I, W0=float(W[0]), mean_level=float((k * W).sum()))


def o5_row(w, s):
    n = w * s
    P = np.array([4.0 ** (-(w - 1)) * comb(w - 1, l) for l in range(w)])
    Q = np.array([4.0 ** (-w) * comb(w, l) for l in range(w + 1)])
    Q[0] = (1 - 2.0 ** (-w)) ** 2
    d = np.convolve(P, poly_pow(Q, s - 1))
    eps = float(d.sum())
    eps_exact = 2.0 ** (-(w - 1)) * (1 - 2.0 ** (-w)) ** (s - 1)
    m = d > 1e-300
    S1 = n * float(np.sum(d[m] * np.log2(math.e / d[m])))
    I = n * eps_exact
    # exact H: p(empty) = (2(1-2^-w)^s - 1)^2 ; for S nonempty with a = a(S) >= 1 blocks:
    # p = 4 (1-2^-w)^(2(s-a)) 4^(-w a), count C(s,a) (2^w-1)^a
    lp_sum = 0.0
    tot = 0.0
    p0 = (2 * (1 - 2.0 ** (-w)) ** s - 1) ** 2
    H = 0.0 if p0 <= 0 else -p0 * log2(p0)
    tot += p0
    for a in range(1, s + 1):
        logcount = (lgamma(s + 1) - lgamma(a + 1) - lgamma(s - a + 1)) / log(2) + a * log2(2 ** w - 1)
        logp = 2 + 2 * (s - a) * log2(1 - 2.0 ** (-w)) - 2 * w * a
        c = 2.0 ** (logcount + logp)
        tot += c
        H += -c * logp
    return dict(w=w, s=s, n=n, eps=eps, eps_check=eps_exact, I=I, H_over_I=H / I, lemma1_sum_over_I=S1 / I,
                log2_inv_eps=log2(1 / eps_exact), parseval=tot, mean_level_Dif=float((np.arange(len(d)) * d).sum() / eps))


def o5b_row(w, s):
    """refined Lemma 1' summed over levels on tribes:  sum_i eps_i [log2(e/eps_i) - D(lambda_i || mu_i)],
    lambda_i(j) = d_{j,i}/eps_i, mu_i(j) = law of |S minus i| under p.  By symmetry P(i in S, |S| = k) = (k/n) W_k, so
    mu_i(j) = (1 - j/n) W_j + ((j+1)/n) W_{j+1},  d_{j,i} = ((j+1)/n) W_{j+1}.
    W(z) = p(empty) + 4 (1-2^-w)^(2s) [ (1 + r((1+z)^w - 1))^s - 1 ],  r = 4^-w / (1-2^-w)^2."""
    n = w * s
    r = 4.0 ** (-w) / (1 - 2.0 ** (-w)) ** 2
    base = np.array([r * comb(w, l) for l in range(w + 1)])
    base[0] = 1.0
    bs = poly_pow(base, s)
    A = 4 * (1 - 2.0 ** (-w)) ** (2 * s)
    W = A * bs
    W[0] = (2 * (1 - 2.0 ** (-w)) ** s - 1) ** 2
    tot = float(W.sum())
    k = np.arange(len(W))
    I_lev = float((k * W).sum())
    Wn = np.append(W, 0.0)
    j = np.arange(len(W))
    d = (j + 1) / n * Wn[1:]
    mu = (1 - j / n) * W + d
    eps = float(d.sum())
    lam = d / eps
    m = lam > 1e-300
    D = float(np.sum(lam[m] * np.log2(lam[m] / mu[m])))
    Hlam = float(-np.sum(lam[m] * np.log2(lam[m])))
    a = mu - d

    def phi_vec(x, y):
        def eta(v):
            out = np.zeros_like(v)
            mm = v > 0
            out[mm] = -v[mm] * np.log2(v[mm])
            return out
        return eta(x) + eta(y) - eta(x + y)
    H_cond_level = float(np.sum(phi_vec(a, d)))  # = H(S_i | |S minus i|), the exact level-only bound on B_i
    h2e = -eps * math.log2(eps) - (1 - eps) * math.log2(1 - eps)
    return dict(w=w, s=s, n=n, parseval=tot, I=I_lev, I_check=n * eps, eps=eps, D_level=D, H_level=Hlam,
                Hcond_level_sum_over_I=n * H_cond_level / I_lev, h2_sum_over_I=n * h2e / I_lev,
                refined_sum_over_I=math.log2(math.e / eps) - D, unrefined_sum_over_I=math.log2(math.e / eps) + Hlam)


def main():
    out = {"O3": [o3_row(a) for a in range(4, 15)]}
    out["O5"] = [o5_row(w, max(1, int(round(2 ** w * math.log(2))))) for w in range(2, 17)]
    out["O5b"] = [o5b_row(w, max(1, int(round(2 ** w * math.log(2))))) for w in range(2, 14)]
    json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), indent=1)
    for r in out["O5b"]:
        print(f"O5b w={r['w']:2d} n={r['n']:6d}  parseval={r['parseval']:.10f}  I={r['I']:.4f} (check {r['I_check']:.4f})  D(lam||mu)={r['D_level']:.4f}  refined/I={r['refined_sum_over_I']:.3f}  sum_i H(S_i||S-i|)/I={r['Hcond_level_sum_over_I']:.3f}  sum h2(eps_i)/I={r['h2_sum_over_I']:.3f}  log2(1/eps)={math.log2(1/r['eps']):.2f}")
    for r in out["O3"]:
        print(f"O3 a={r['a']:2d} M={r['M']:5d}  H/I={r['H_over_I']:.4f}  Phi/I={r['Phi_over_I']:.4f}  (first {r['first_over_I']:.3f}, second {r['second_over_I']:.3f})  W0={r['W0']:.4f}")
    for r in out["O5"]:
        print(f"O5 w={r['w']:2d} s={r['s']:6d} n={r['n']:7d}  I={r['I']:.3f}  H/I={r['H_over_I']:.4f}  Lemma1-sum/I={r['lemma1_sum_over_I']:.3f}  log2(1/eps)={r['log2_inv_eps']:.2f}  parseval={r['parseval']:.12f}  eps rel err={abs(r['eps']/r['eps_check']-1):.1e}")


if __name__ == "__main__":
    main()
