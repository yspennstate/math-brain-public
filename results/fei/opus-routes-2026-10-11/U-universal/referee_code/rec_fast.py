"""Vectorised version of the composition step of rec.py for symmetric outer gates g applied to k copies of an inner
function h (table on m bits).  Returns H, U, I, G, local ratios of F = g(h, ..., h).  Validated against rec.py."""
import math
import numpy as np
from rlib import Spec, restrict_tables, superset_sum


def xlog2x(p):
    p = np.asarray(p, dtype=np.float64)
    out = np.zeros_like(p)
    m = p > 0
    out[m] = p[m] * np.log2(p[m])
    return out


class Gate:
    def __init__(self, g):
        self.g = np.asarray(g, dtype=np.float64)
        self.k = self.g.size.bit_length() - 1
        ys = np.arange(1 << self.k)
        self.Y = np.stack([1 - 2 * ((ys >> j) & 1) for j in range(self.k)], 0).astype(np.float64)   # (k, 2^k)

    def law(self, mus):
        k = self.k
        mus = np.asarray(mus, dtype=np.float64)
        sig = np.sqrt(np.maximum(0.0, 1 - mus * mus))
        py = np.prod((1 + mus[:, None] * self.Y) / 2, axis=0)
        w = py * self.g
        M = np.zeros((1 << k, 1 << k)); M[0] = 1.0
        ok = np.ones(1 << k, dtype=bool)
        for j in range(k):
            a = (self.Y[j] - mus[j]) / sig[j] if sig[j] > 1e-15 else np.zeros(1 << k)
            idx = np.arange(1 << j)
            M[idx | (1 << j)] = M[idx] * a
            if sig[j] <= 1e-15:
                ok[idx | (1 << j)] = False
        coef = M @ w
        P = np.where(ok, coef * coef, 0.0)
        mu_out = float(w.sum())
        return P, mu_out

    def compose(self, kids):
        """kids: list of (mu, Hq, Uq, Iq, const).  Returns (mu, H, U, I) of the composition (unnormalised)."""
        k = self.k
        mus = [c[0] for c in kids]
        P, mu = self.law(mus)
        pi = superset_sum(P)
        H = -xlog2x(P).sum()
        with np.errstate(divide='ignore', invalid='ignore'):
            U = float(np.where(P > 0, P * np.log2(np.where(P > 0, pi / np.where(P > 0, P, 1), 1)), 0).sum())
        Js = np.arange(1 << k)
        for j, c in enumerate(kids):
            if c[4]:
                continue
            pj = P[((Js >> j) & 1) == 1].sum()
            H += pj * c[1]; U += pj * c[2]
        I = sum(P[((Js >> j) & 1) == 1].sum() * c[3] for j, c in enumerate(kids) if not c[4])
        return mu, float(H), float(U), float(I)


def summ(t):
    t = np.asarray(t, dtype=np.int64)
    mu = float(t.mean())
    if abs(mu) == 1.0:
        return (mu, 0.0, 0.0, 0.0, True)
    sp = Spec.from_tables(t)
    p = sp.p[0].copy(); p0 = p[0]; q = p.copy(); q[0] = 0.0; q /= (1 - p0)
    sq = Spec(q)
    return (mu, float(sq.H()[0]), float(sq.U()[0]), float(sq.I()[0]), False)


def stats_sym(gate, h):
    """F = gate(h, ..., h) for a symmetric gate (all input positions equivalent)."""
    k = gate.k
    base = summ(h)
    mu, H, U, I = gate.compose([base] * k)
    m = int(np.asarray(h).size).bit_length() - 1
    G = 0.0; locs = []; Isum = 0.0
    for v in range(m):
        sp_ = summ(restrict_tables(np.asarray(h), v, 1)); sm_ = summ(restrict_tables(np.asarray(h), v, -1))
        _, Hp, Up, Ip = gate.compose([sp_] + [base] * (k - 1))
        _, Hm, Um, Im = gate.compose([sm_] + [base] * (k - 1))
        inf = I - 0.5 * (Ip + Im); dU = U - 0.5 * (Up + Um)
        G += k * dU; Isum += k * inf
        if inf > 1e-15:
            locs.append(dU / inf)
    if I <= 0:
        return None
    return dict(H_over_I=H / I, U_over_I=U / I, G_over_I=G / I, I=I, I_check=Isum, min_loc=min(locs) if locs else None, max_loc=max(locs) if locs else None)
