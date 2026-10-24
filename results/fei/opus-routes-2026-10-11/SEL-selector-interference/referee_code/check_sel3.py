"""Referee check of SEL-3 (bent point-flip family) with exact Walsh integers and 50-digit logarithms.

F_m(z,t) = b(t) if z=+1, b'(t) if z=-1, b quadratic bent on m bits with b(0)=1, b' = b - 2*1_{t=0}.
Checks: the closed forms for H(F_m), H(b), H(b'); delta = Inf_z = 2^-m; cost/delta vs m + 3/ln2;
ratio cost / [h(delta) + min(h(delta), (2/ln2) delta)] -> 1; product over a selector bits (additivity).
"""
import numpy as np
import mpmath as mp
from rlib import wht, popcount_table

mp.mp.dps = 50


def bent(m):
    idx = np.arange(1 << m, dtype=np.int64)
    s = np.zeros(1 << m, dtype=np.int64)
    for k in range(0, m, 2):
        s ^= ((idx >> k) & 1) & ((idx >> (k + 1)) & 1)
    return 1 - 2 * s          # b(0) = 1 at index 0 (all t = 0, i.e. all x = +1)


def H_exact(W, nvars):
    """Entropy of (W/2^n)^2 from exact integers: group equal |W|, 50-digit logs."""
    vals, cnt = np.unique(np.abs(W), return_counts=True)
    tot = mp.mpf(0)
    for v, c in zip(vals, cnt):
        v = int(v)
        if v == 0:
            continue
        p = mp.mpf(v * v) / mp.mpf(4) ** nvars
        tot += int(c) * (-p * mp.log(p, 2))
    return tot


def closed_forms(m):
    eps = mp.mpf(2) ** (-mp.mpf(m) / 2)
    dl = eps ** 2
    L = lambda x: mp.log(x, 2)
    HF = (1 - dl) * (m - (1 - eps) * L(1 - eps) - (1 + eps) * L(1 + eps)) + 2 * m * dl
    Hb = mp.mpf(m)
    Hbp = m - ((1 + eps) * (1 - 2 * eps) ** 2 * L(1 - 2 * eps) + (1 - eps) * (1 + 2 * eps) ** 2 * L(1 + 2 * eps))
    return HF, Hb, Hbp


def main():
    ln2 = mp.log(2)
    print(" m   delta        H(F)err   H(b)err   H(b')err   cost/delta       m+3/ln2        ratio-to-SEL1")
    for m in range(2, 19, 2):
        b = bent(m)
        bp = b.copy(); bp[0] = -bp[0]
        # F(z,t): z is bit 0 (selector, low), t = high bits; index = zi + 2*ti
        F = np.empty(1 << (m + 1), dtype=np.int64)
        F[0::2] = b
        F[1::2] = bp
        WF = wht(F); Wb = wht(b); Wbp = wht(bp)
        HF = H_exact(WF, m + 1); Hb = H_exact(Wb, m); Hbp = H_exact(Wbp, m)
        cHF, cHb, cHbp = closed_forms(m)
        delta = mp.mpf(int(np.sum(b != bp))) / (1 << m)
        cost = HF - (Hb + Hbp) / 2
        hd = -delta * mp.log(delta, 2) - (1 - delta) * mp.log(1 - delta, 2)
        bound = hd + min(hd, 2 / ln2 * delta)
        print("%2d  %.3e  %.1e  %.1e  %.1e  %.12f  %.12f  %.9f" % (
            m, float(delta), float(abs(HF - cHF)), float(abs(Hb - cHb)), float(abs(Hbp - cHbp)),
            float(cost / delta), float(m + 3 / ln2), float(cost / bound)))
    # products over a = 2 selector bits on disjoint data blocks
    print("products (a=2): cost(F x F) vs 2 cost(F), Inf of each selector bit")
    for m in (2, 4, 6, 8):
        b = bent(m); bp = b.copy(); bp[0] = -bp[0]
        F1 = np.empty(1 << (m + 1), dtype=np.int64); F1[0::2] = b; F1[1::2] = bp
        n1 = m + 1
        # product F(z1,z2,t1,t2) = F1(z1,t1) F1(z2,t2); order bits as (z1, z2, t1..., t2...)
        P = np.outer(F1, F1)  # P[i1, i2] with i1 = z1 + 2 t1, i2 = z2 + 2 t2
        z1 = np.arange(1 << n1) & 1; t1 = np.arange(1 << n1) >> 1
        Fp = np.empty(1 << (2 * n1), dtype=np.int64)
        I1, I2 = np.meshgrid(np.arange(1 << n1), np.arange(1 << n1), indexing="ij")
        joint = (z1[I1]) | (z1[I2] << 1) | (t1[I1] << 2) | (t1[I2] << (2 + m))
        Fp[joint.reshape(-1)] = P.reshape(-1)
        WFp = wht(Fp)
        HFp = H_exact(WFp, 2 * n1)
        # branches: for (z1,z2), g = b or b' on each block; avg H = avg over 4 of (H(b_z1) + H(b_z2))
        Hb = H_exact(wht(b), m); Hbp = H_exact(wht(bp), m)
        avgH = Hb + Hbp   # each block contributes (Hb+Hbp)/2, two blocks
        costp = HFp - avgH
        cost1 = H_exact(wht(F1), n1) - (Hb + Hbp) / 2
        # selector influences of the product
        idx = np.arange(1 << (2 * n1))
        inf1 = np.mean(Fp != Fp[idx ^ 1]); inf2 = np.mean(Fp != Fp[idx ^ 2])
        print("m=%d  cost(prod)=%.15f  2*cost(F1)=%.15f  Inf_z1=%.6e Inf_z2=%.6e delta=%.6e" % (
            m, float(costp), float(2 * cost1), inf1, inf2, 2.0 ** -m))


if __name__ == "__main__":
    main()
