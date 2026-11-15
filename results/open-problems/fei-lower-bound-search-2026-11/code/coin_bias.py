"""coin_bias.py - a coin gate whose main inputs are uniform bits and whose coins are small functions of bias q.

f = F(x_1..x_m ; h_1..h_k), x_i uniform bits, h_j independent copies of a function h (or of -h) with Pr[h = -1] = q.
With Phi(g) = G_g - c (J_g - 1):   Phi(f) = U_F(1/2,..,1/2 ; q_1..q_k) + sum_j Inf_j Phi(h_j),   U = G - c J + c.
A new lower bound needs Phi(f) + (W(p_f) - c) > 0.

For every bias q = t/16 the best Phi over all functions of at most 4 inputs is taken as Phi(h) (exhaustive), then
the gate is evaluated with all coins at q, at 1 - q, and at every mixed pattern for a few q.
usage: python coin_bias.py LABFILE [WFILE]
"""
import sys

import numpy as np

from rec_hess import het_stats, parts_of


def small_best(c):
    """best Phi, with its G, J and table, for each number of -1 values t/16 over all 4-input functions"""
    tabs = np.arange(1, 65535, dtype=np.int64)
    a = 1.0 - 2.0 * ((tabs[:, None] >> np.arange(16)[None, :]) & 1)
    h = 1
    while h < 16:
        a = a.reshape(len(tabs), -1, 2, h)
        lo, hi = a[:, :, 0, :], a[:, :, 1, :]
        a = np.stack([lo + hi, lo - hi], axis=2).reshape(len(tabs), 16)
        h *= 2
    a /= 16.0
    mean = a[:, 0]
    var = 1 - mean * mean
    w = a * a
    w[:, 0] = 0
    w /= var[:, None]
    with np.errstate(divide="ignore", invalid="ignore"):
        G = -np.where(w > 0, w * np.log2(w), 0.0).sum(axis=1)
    pc = np.array([bin(s).count("1") for s in range(16)])
    J = (w * pc[None, :]).sum(axis=1)
    phi = G - c * (J - 1)
    ones = np.rint((1 - mean) * 8).astype(int)
    out = {}
    for t in range(1, 16):
        sel = np.where(ones == t)[0]
        k = sel[np.argmax(phi[sel])]
        out[t] = (float(phi[k]), float(G[k]), float(J[k]), int(tabs[k]))
    return out


def main():
    parts = open(sys.argv[1], encoding="utf-8").readline().split()
    m = int(parts[0])
    rows, kk = parts_of(m, [ord(ch) - 48 for ch in parts[2]])
    half = np.full(m, 0.5)
    G0, J0, P0, infl0 = het_stats(m, rows, half, np.full(kk, 0.5))
    c = G0 / (J0 - 1)
    print("gate m=%d coins=%d  G %.12f J %.12f c %.12f  coin influence %.6f" % (m, kk, G0, J0, c, infl0[m]))
    W = None
    if len(sys.argv) > 2:
        tab = np.loadtxt(sys.argv[2])
        W = lambda p: float(np.interp(np.log2(p / (1 - p)), tab[:, 0], tab[:, 1]))
    sb = small_best(c)
    print("best Phi of a function of <= 4 inputs by bias:")
    for t in range(1, 16):
        print("  q %2d/16  Phi %+.6f  G %.6f J %.6f  table %04x" % ((t,) + sb[t]))

    def total(pq, phis):
        G, J, pp, infl = het_stats(m, rows, half, pq)
        U = G - c * J + c
        pen = float((infl[m:] * phis).sum())
        D = (W(pp) - c) if W else 0.0
        return U, pen, pp, D, U + pen + D, float(infl[m:].sum())

    print("all coins at the same bias q (Phi of the coin from the table above):")
    for t in range(1, 16):
        q = t / 16.0
        U, pen, pp, D, tot, si = total(np.full(kk, q), np.full(kk, sb[t][0]))
        print("  q %2d/16  U %+.6f  coin infl sum %.6f  penalty %+.6f  Phi(f) %+.6f  p_f %.6f  D %+.6f  total %+.6f"
              % (t, U, si, pen, U + pen, pp, D, tot))
    print("U alone on a fine grid of q (all coins), to see its shape:")
    for q in (0.02, 0.05, 0.1, 0.2, 0.3, 0.4, 0.45, 0.5, 0.55, 0.6, 0.7, 0.8, 0.9, 0.95, 0.98):
        U, pen, pp, D, tot, si = total(np.full(kk, q), np.zeros(kk))
        print("  q %.2f  U %+.6f  U/(q-1/2)^2 %s  coin infl sum %.6f  p_f %.6f" %
              (q, U, ("%+.4f" % (U / (q - 0.5) ** 2)) if q != 0.5 else "-", si, pp))
    print("best mixed pattern (coin j at q or 1 - q) per q:")
    for t in (1, 2, 3, 4, 5, 6, 7):
        q = t / 16.0
        best = None
        for code in range(1 << kk):
            bits = (code >> np.arange(kk)) & 1
            pq = np.where(bits == 1, 1 - q, q)
            phis = np.where(bits == 1, sb[16 - t][0], sb[t][0])
            r = total(pq, phis)
            if best is None or r[4] > best[0]:
                best = (r[4], code, r)
        tot, code, r = best
        print("  q %2d/16  pattern %s  U %+.6f penalty %+.6f Phi(f) %+.6f p_f %.6f D %+.6f total %+.6f"
              % (t, format(code, "0%db" % kk)[::-1], r[0], r[1], r[0] + r[1], r[2], r[3], tot))


if __name__ == "__main__":
    main()
