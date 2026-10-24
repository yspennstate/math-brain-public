"""The single hub with a hub diagonal in the spread regime: Q = a X_h^2 + 2 X_h L + lambda V^2 + 2 eps L P. Given X', Q is
a quadratic in X_h, and P(|Q - y| <= delta | X') is the hub measure of the set where a x^2 + 2 x L lies in
[y - delta - R, y + delta - R], R = lambda V^2 + 2 eps L P: with D_pm = L^2 + a (y pm delta - R), that set is
x + L/a in +-[sqrt(D_-)_+/|a|, sqrt(D_+)_+/|a|] (for a > 0; for a < 0 the roles of D_+ and D_- swap), and its measure is
read off the hub distribution function exactly. Same light laws, frames and hubs as small_eps_dim.py."""
import sys, importlib
import numpy as np
import small_eps as se

def peak_diag(a, eps, hubkind, w, v, p, lam=1.0, nsamp=1_000_000, B=100_000):
    xs, Fs = se.hub_cdf(hubkind, eps)
    delta = 0.002
    ys = np.concatenate([np.linspace(-1.5, 1.5, 121), np.linspace(-0.1, 0.1, 101)])
    acc = np.zeros_like(ys); done = 0
    F = lambda z: np.interp(z, xs, Fs)
    while done < nsamp:
        X = se.light("comb", (B, len(w)))
        L, V, P = X @ w, X @ v, X @ p
        R = lam * V * V + 2 * eps * L * P
        c = -L / a
        for j, y in enumerate(ys):
            Dp = L * L + a * (y + delta - R); Dm = L * L + a * (y - delta - R)
            hi = np.sqrt(np.maximum(np.maximum(Dp, Dm), 0.0)) / abs(a)
            lo = np.sqrt(np.maximum(np.minimum(Dp, Dm), 0.0)) / abs(a)
            m = (F(c + hi) - F(c + lo)) + (F(c - lo) - F(c - hi))
            acc[j] += m.sum()
        done += B
    dens = acc / done / (2 * delta)
    return float(dens.max())

def frame(m):
    importlib.reload(se)
    while True:
        w, v, p = se.frames("random", m)
        if np.max(w ** 2 + v ** 2) <= 0.5:
            return w, v, p

if __name__ == "__main__":
    ms = [int(x) for x in sys.argv[1].split(",")] if len(sys.argv) > 1 else [8, 32, 128]
    for m in ms:
        w, v, p = frame(m)
        for a in (0.5, -0.5):
            row = []
            for hubkind in ("rough", "unif"):
                importlib.reload(se)
                row.append("%s hub %.3f" % (hubkind, peak_diag(a, 0.01, hubkind, w, v, p)))
            print("m=%4d  max|w_i| %.2f  a=%+.1f  eps=0.01  %s" % (m, np.max(np.abs(w)), a, "   ".join(row)), flush=True)
