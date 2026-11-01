"""Cancellation-free versions of the tower recursions (tower_erasure.py, tower_rho0.py).

E(a,b) = phi(a)+phi(b)-phi(a+b) = a log2(1+b/a) + b log2(1+a/b)   (log1p form).
H(g) - (Ht(j,+mu)+Ht(j,-mu))/2 = sum_{U not ni j, a_U != 0} a^2 [F(t) - t^2 log2(1/a^2)]
                                 - sum_{a_U = 0} phi(mu^2 b^2)
                                 + sum_U [ mu^2 b^2 log2(1/b^2) + (1-mu^2) b^2 log1p(-mu^2)/ln 2 ],
with a_U = ghat(U), b_U = ghat(U+j), t = mu b/a, F(t) = [(1+t)^2 ln(1+t) + (1-t)^2 ln(1-t)]/ln 2
= (3t^2 - t^4/6 - t^6/30 - ...)/ln 2 (series used for |t| < 1e-3).
Everything is computed in float64 without subtracting O(1) quantities.  Cross-checked against mpmath at
50 digits on sample points, and against the plain formulas at depth <= 4.
"""
import sys, os, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *

LN2 = np.log(2.0)


def E_stable(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    out = np.zeros(np.broadcast(a, b).shape)
    m = (a > 0) & (b > 0)
    aa, bb = np.broadcast_to(a, out.shape)[m], np.broadcast_to(b, out.shape)[m]
    out[m] = (aa * np.log1p(bb / aa) + bb * np.log1p(aa / bb)) / LN2
    return out


def F_stable(t):
    t = np.asarray(t, float)
    out = np.empty_like(t)
    small = np.abs(t) < 1e-3
    ts = t[small]
    out[small] = (3 * ts ** 2 - ts ** 4 / 6 - ts ** 6 / 30) / LN2
    tl = t[~small]
    with np.errstate(divide="ignore", invalid="ignore"):
        v = ((1 + tl) ** 2 * np.log1p(tl) + np.where(np.abs(tl) < 1, (1 - tl) ** 2 * np.log1p(-tl), 0.0)) / LN2
    out[~small] = v
    return out


def delta_gate_increment(gh, n, j, mu):
    """H(g) - (Ht_g(j,+mu) + Ht_g(j,-mu))/2, stable."""
    S = np.arange(1 << n)
    lo = S[((S >> j) & 1) == 0]
    a = gh[lo]; b = gh[lo | (1 << j)]
    tot = 0.0
    nz = np.abs(a) > 0
    t = mu * b[nz] / a[nz]
    a2 = a[nz] ** 2
    tot += float((a2 * (F_stable(t) - t ** 2 * np.log2(1 / a2))).sum())
    z = (~nz) & (np.abs(b) > 0)
    tot -= float(phi((mu * b[z]) ** 2).sum())
    b2 = b ** 2; bz = b2 > 0
    tot += float((mu * mu * b2[bz] * np.log2(1 / b2[bz]) + (1 - mu * mu) * b2[bz] * np.log1p(-mu * mu) / LN2).sum())
    return tot


def h2_small(x):
    """binary entropy of x (bits), accurate for tiny x."""
    return (-x * np.log(x) - (1 - x) * np.log1p(-x)) / LN2 if x > 0 else 0.0


def run(gtt, n, K):
    gh = wht(np.asarray(gtt, float)[None, :])[0]
    p = gh ** 2
    cq = coord_quantities(gh[None, :], n)
    Inf = cq["Inf"][0]; Bg = cq["B"][0]; Dg = cq["Delta"][0]
    H1 = float(entropy(p)); I1 = float(Inf.sum())
    lvl1 = np.array([gh[1 << j] for j in range(n)])
    assert abs(gh[0]) < 1e-12 and np.allclose(np.abs(lvl1), Inf)
    vals = sorted(set(np.round(Inf, 14)))
    cls = [vals.index(round(x, 14)) for x in Inf]
    S = np.arange(1 << n)
    lows = [S[((S >> j) & 1) == 0] for j in range(n)]

    def Xi(j, c2):
        lo = lows[j]
        return float(E_stable(p[lo], c2 * p[lo | (1 << j)]).sum())

    def key_of(j):
        return tuple(1 if c == cls[j] else 0 for c in range(len(vals)))

    bestB, bestD, Bsum, cnt = {}, {}, {}, {}
    for j in range(n):
        k0 = key_of(j)
        bestB[k0] = min(bestB.get(k0, np.inf), Bg[j] / Inf[j])
        bestD[k0] = min(bestD.get(k0, np.inf), Dg[j] / Inf[j])
        Bsum[k0] = Bsum.get(k0, 0.0) + Bg[j]; cnt[k0] = cnt.get(k0, 0) + 1
    Hk, Ik = H1, I1
    rows = []
    cX, cD = {}, {}
    for depth in range(1, K + 1):
        rows.append(dict(k=depth, H_over_I=Hk / Ik, B_over_I=sum(Bsum.values()) / Ik,
                         exist_B=min(bestB.values()), rho0=min(bestD.values())))
        print(json.dumps(rows[-1])); sys.stdout.flush()
        if depth == K:
            break
        nB, nD, nS, nc = {}, {}, {}, {}
        for key in bestB:
            P = float(np.prod([vals[c] ** key[c] for c in range(len(vals))]))
            for j in range(n):
                ck = (j, key)
                if ck not in cX:
                    cX[ck] = Xi(j, P * P)
                    cD[ck] = (Inf[j] * h2_small(P * P) + delta_gate_increment(gh, n, j, P)) / (Inf[j] * P)
                nk = tuple(key[c] + (1 if c == cls[j] else 0) for c in range(len(vals)))
                nB[nk] = min(nB.get(nk, np.inf), bestB[key] + cX[ck] / (Inf[j] * P))
                nD[nk] = min(nD.get(nk, np.inf), bestD[key] + cD[ck])
                nS[nk] = nS.get(nk, 0.0) + Inf[j] * Bsum[key] + cnt[key] * cX[ck]
                nc[nk] = nc.get(nk, 0) + cnt[key]
        bestB, bestD, Bsum, cnt = nB, nD, nS, nc
        Hk, Ik = H1 + I1 * Hk, I1 * Ik
    return rows


if __name__ == "__main__":
    set_polite()
    # mpmath spot check of the gate increment at a tiny mu on Numaro's g
    from mpmath import mp, mpf, log as mlog
    mp.dps = 50
    g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy"))
    # exact Fourier coefficients are k/2^17 (integers k); recover them exactly for the mp check
    ghat = wht(g[None, :].astype(float))[0]
    kint = np.rint(ghat * 2 ** 18).astype(np.int64)
    assert np.all(np.abs(kint / 2 ** 18 - ghat) < 1e-15)
    j = 9; mu = 1e-9
    S = np.arange(1 << 18); lo = S[((S >> j) & 1) == 0]
    A = [mpf(int(x)) / 2 ** 18 for x in kint[lo]]; Bv = [mpf(int(x)) / 2 ** 18 for x in kint[lo | (1 << j)]]
    def ph(x):
        return -x * mlog(x, 2) if x > 0 else mpf(0)
    m = mpf(mu)
    ex = mpf(0)
    for a, b in zip(A, Bv):
        ex += ph(a * a) + ph(b * b) - (ph((a + m * b) ** 2) + ph((a - m * b) ** 2)) / 2 - ph((1 - m * m) * b * b)
    st = delta_gate_increment(ghat, 18, j, mu)
    print("gate increment at mu=1e-9, j=9: mpmath", float(ex), " stable float", st)
    rows = run(g, 18, 10)
    json.dump(rows, open(os.path.join(HERE, "..", "logs", "tower_stable.json"), "w"), indent=1)
