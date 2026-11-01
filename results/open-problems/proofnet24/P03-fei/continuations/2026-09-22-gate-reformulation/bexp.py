"""Erasure entropy of the spectral sample: B(f) = sum_i H(S_i | S_{-i}).

Why it matters.  The record's erasure reduction gives Delta_i = B_i + JS(q_+,q_-) with JS <= (2/ln2) Inf_i, so
    rho_0(f) = min_i Delta_i/Inf_i  <=  (sum_i Delta_i)/I(f)  <=  B(f)/I(f) + 2/ln2 ,
and a uniform bound rho_0 <= K gives FEI with constant K.  Since B <= H (erasure entropy <= entropy),

    C_FEI - 2/ln2  <=  sup B/I  <=  C_FEI ,

so measuring sup B/I sandwiches the conjecture's own constant.  This module computes B, B_i, Inf_i, Delta_i, H, I
exactly from the spectrum, exhaustively for small n and by hill climbing above that.
"""
import numpy as np, math, sys, itertools
LN2 = math.log(2.0)

def fwht(a):
    """in-place-ish Walsh-Hadamard; a shape (..., 2^n) -> sum_x a(x) chi_S(x)"""
    a = np.array(a, dtype=np.float64, copy=True)
    N = a.shape[-1]; h = 1
    while h < N:
        a = a.reshape(*a.shape[:-1], N // (2 * h), 2, h)
        x = a[..., 0, :].copy(); y = a[..., 1, :].copy()
        a[..., 0, :] = x + y; a[..., 1, :] = x - y
        a = a.reshape(*a.shape[:-3], N)
        h *= 2
    return a

def spectrum(vals, n):
    """vals: (..., 2^n) of +-1 -> mu(S) = fhat(S)^2 and fhat"""
    fh = fwht(vals) / (1 << n)
    return fh, fh * fh

def _h2(v):
    v = np.clip(v, 0.0, 1.0)
    with np.errstate(divide="ignore", invalid="ignore"):
        return np.where((v > 0) & (v < 1), -v * np.log2(np.maximum(v, 1e-300)) - (1 - v) * np.log2(np.maximum(1 - v, 1e-300)), 0.0)

def stats(vals, n):
    """vals (B, 2^n) of +-1.  returns dict of arrays over the batch."""
    vals = np.atleast_2d(np.asarray(vals, float))
    fh, mu = spectrum(vals, n)
    N = 1 << n
    with np.errstate(divide="ignore", invalid="ignore"):
        H = -np.where(mu > 1e-300, mu * np.log2(np.maximum(mu, 1e-300)), 0.0).sum(axis=1)
    sizes = np.array([bin(s).count("1") for s in range(N)], float)
    I = (mu * sizes).sum(axis=1)
    Bi = np.zeros((vals.shape[0], n)); Infi = np.zeros((vals.shape[0], n)); Di = np.zeros((vals.shape[0], n))
    for i in range(n):
        lo = np.array([s for s in range(N) if not (s >> i) & 1])
        hi = lo | (1 << i)
        a = fh[:, lo]; b = fh[:, hi]
        A = a * a; Bb = b * b
        m = A + Bb
        with np.errstate(divide="ignore", invalid="ignore"):
            beta = np.where(m > 1e-300, Bb / np.maximum(m, 1e-300), 0.0)
        Bi[:, i] = (m * _h2(beta)).sum(axis=1)
        Infi[:, i] = Bb.sum(axis=1)
        # Delta_i = sum_T m [ h(beta) + 1 - h((1+u)/2) ],  u = 2ab/m
        with np.errstate(divide="ignore", invalid="ignore"):
            u = np.where(m > 1e-300, 2 * a * b / np.maximum(m, 1e-300), 0.0)
        Di[:, i] = (m * (_h2(beta) + 1.0 - _h2((1.0 + u) * 0.5))).sum(axis=1)
    B = Bi.sum(axis=1)
    rel = Infi > 1e-12
    with np.errstate(divide="ignore", invalid="ignore"):
        rho = np.where(rel, Di / np.maximum(Infi, 1e-300), np.inf).min(axis=1)
    return dict(H=H, I=I, B=B, Bi=Bi, Infi=Infi, Di=Di, rho0=rho,
                BI=np.where(I > 1e-12, B / np.maximum(I, 1e-300), 0.0),
                HI=np.where(I > 1e-12, H / np.maximum(I, 1e-300), 0.0),
                maxBiInf=np.where(rel, Bi / np.maximum(Infi, 1e-300), 0.0).max(axis=1))

def all_functions(n):
    N = 1 << n
    idx = np.arange(1 << N, dtype=np.uint64)[:, None]
    return 1.0 - 2.0 * ((idx >> np.arange(N, dtype=np.uint64)[None, :]) & 1).astype(np.float64)

def bent_plus_flip(m):
    """f on n = m+1 variables: a bent function on m variables (m even, inner product), flipped at one point
    that has x_{new} = true.  Predicts B_i/Inf_i ~ m for the new coordinate."""
    assert m % 2 == 0
    M = 1 << m
    xs = np.arange(M)
    half = m // 2
    u = xs & ((1 << half) - 1); v = xs >> half
    ip = np.array([bin(int(a) & int(b)).count("1") & 1 for a, b in zip(u, v)])
    g = 1.0 - 2.0 * ip                              # bent: inner product function
    f = np.concatenate([g, g.copy()])               # new variable is the top bit; f independent of it
    f[M] = -f[M]                                    # flip one point with x_new = 1 (index M -> top bit set)
    return f, m + 1

if __name__ == "__main__":
    what = sys.argv[1] if len(sys.argv) > 1 else "small"
    if what == "small":
        for n in (2, 3, 4):
            V = all_functions(n)
            keep = np.abs(V.sum(axis=1)) < (1 << n)      # non-constant
            s = stats(V[keep], n)
            ok = s["I"] > 1e-9
            print("n=%d  %d non-constant:  max B/I = %.6f   max H/I = %.6f   max_i B_i/Inf_i = %.6f   max rho0 = %.6f"
                  % (n, keep.sum(), s["BI"][ok].max(), s["HI"][ok].max(), s["maxBiInf"][ok].max(), s["rho0"][ok].max()))
            j = int(np.argmax(np.where(ok, s["BI"], -1)))
            print("    argmax B/I: tt=%d  B=%.5f I=%.5f H=%.5f" % (int(((1 - V[keep][j]) / 2 * (1 << np.arange(1 << n))).sum()), s["B"][j], s["I"][j], s["H"][j]))
    elif what == "bent":
        print("bent-on-m plus one flip:  the new coordinate's B_i/Inf_i against m")
        for m in (2, 4, 6, 8, 10, 12):
            f, n = bent_plus_flip(m)
            s = stats(f[None, :], n)
            i = n - 1
            print("  m=%2d n=%2d   Inf_i=%.3e  B_i=%.3e  B_i/Inf_i=%.4f   (m=%d)   B/I=%.4f  H/I=%.4f  rho0=%.4f"
                  % (m, n, s["Infi"][0, i], s["Bi"][0, i], s["Bi"][0, i] / s["Infi"][0, i], m, s["BI"][0], s["HI"][0], s["rho0"][0]))
