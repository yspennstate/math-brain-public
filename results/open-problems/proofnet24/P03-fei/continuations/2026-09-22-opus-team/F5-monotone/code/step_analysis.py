"""Restriction-step quantities for LTFs.

For a coordinate i: s_S = fhat(S) (S not containing i) is the spectrum of E_i f, d_S = fhat(S+i) the
spectrum of D_i f.  Delta_i H = H(f) - (H(f_+)+H(f_-))/2 = sum_S psi(s_S, d_S) with
psi(s,d) = phi(s^2)+phi(d^2)-(phi((s+d)^2)+phi((s-d)^2))/2.  Inf_i = sum_S d_S^2.
Level-wise bound: Delta_i H <= c_psi Inf_i + sum_k D_k log2(1 + S_k/D_k), D_k, S_k level weights.
"""
import numpy as np
import numba as nb
from ltf_core import ltf_table, spectrum, HI, popcount


@nb.njit(cache=True)
def step_all(c, n):
    """For every coordinate i: (DeltaH, Inf, sumlog, levelbound_logpart)."""
    N = c.shape[0]
    out = np.zeros((n, 4))
    for i in range(n):
        b = 1 << i
        Dk = np.zeros(n + 1)
        Sk = np.zeros(n + 1)
        dH = 0.0
        inf = 0.0
        slog = 0.0
        for S in range(N):
            if S & b:
                continue
            s = c[S]
            d = c[S | b]
            ws = s * s
            wd = d * d
            wp = (s + d) * (s + d)
            wm = (s - d) * (s - d)
            t = 0.0
            if ws > 1e-300:
                t -= ws * np.log2(ws)
            if wd > 1e-300:
                t -= wd * np.log2(wd)
            if wp > 1e-300:
                t += 0.5 * wp * np.log2(wp)
            if wm > 1e-300:
                t += 0.5 * wm * np.log2(wm)
            dH += t
            inf += wd
            k = popcount(S)
            Dk[k] += wd
            Sk[k] += ws
            if wd > 1e-300:
                slog += wd * np.log2(1.0 + ws / wd)
        lvl = 0.0
        for k in range(n + 1):
            if Dk[k] > 1e-300:
                lvl += Dk[k] * np.log2(1.0 + Sk[k] / Dk[k])
        out[i, 0] = dH
        out[i, 1] = inf
        out[i, 2] = slog
        out[i, 3] = lvl
    return out


def analyse(w, theta):
    w = np.asarray(w, np.float64)
    n = len(w)
    f = ltf_table(w, theta)
    c = spectrum(f)
    H, I = HI(c)
    st = step_all(c, n)
    return H, I, st, (1 - c[0]) / 2


def psi_bound_constant():
    """sup_t [psi(t,1) - log2(1+t^2)] over a fine grid (psi is 2-homogeneous)."""
    t = np.concatenate([np.linspace(1e-6, 10, 200001), np.logspace(1, 8, 20001)])
    def ph(w):
        return np.where(w > 0, -w * np.log2(np.where(w > 0, w, 1)), 0.0)
    psi = ph(t * t) + ph(np.ones_like(t)) - 0.5 * (ph((t + 1) ** 2) + ph((t - 1) ** 2))
    g = psi - np.log2(1 + t * t)
    k = np.argmax(g)
    return g[k], t[k], 3 / np.log(2)
