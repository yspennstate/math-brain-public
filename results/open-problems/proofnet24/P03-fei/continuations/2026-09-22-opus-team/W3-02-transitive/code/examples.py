"""Exact spectral bookkeeping for the families used to test (and refute) proof routes:
tribes T_{w,s} = OR_s(AND_w,...), AND_n, and majority Maj_n (all transitive).

For each: H/I; the level bound  N/I := [H(|S|) + E log2 C(n,|S|)]/I  (the symmetric-function route);
E_sb log2(n/|S|); the Shearer window bound  [log2(e/tau) + m]/M  (window A of size m, tau = Pr[S meets A],
M = E[|S cap A| | S meets A]); for tribes also the wreath term X/I = E log2 C(s,J) / I.
Tribes spectrum (composition identity): with p = 2^-w, Pr[J = t] = C(s,t) 4 (1-p)^(2s-t) p^t (t >= 1),
given J the touched blocks are uniform and each block's part is uniform over its 2^w - 1 nonempty subsets.
"""
import math
import numpy as np
from math import comb, log2


def phi(t):
    return -t * log2(t) if t > 0 else 0.0


def tribes(w, s):
    p = 2.0 ** -w
    n = w * s
    c0 = 1 - 2 * (1 - p) ** s                       # mean of the +-1 function (true = -1)
    PJ = [c0 * c0] + [comb(s, t) * 4 * (1 - p) ** (2 * s - t) * p ** t for t in range(1, s + 1)]
    # law of a (block part size), uniform over nonempty subsets
    pa = np.array([0.0] + [comb(w, k) / (2 ** w - 1) for k in range(1, w + 1)])
    Ea = sum(k * pa[k] for k in range(w + 1))
    EJ = sum(t * PJ[t] for t in range(s + 1))
    I = EJ * Ea
    HJ = sum(phi(x) for x in PJ)
    X = sum(PJ[t] * log2(comb(s, t)) for t in range(1, s + 1))
    H = HJ + X + EJ * log2(2 ** w - 1)
    # law of |S|: mixture over J of convolution powers of pa
    size = np.zeros(n + 1); size[0] = PJ[0]
    conv = np.array([1.0])
    for t in range(1, s + 1):
        conv = np.convolve(conv, pa)[: n + 1]
        size[: len(conv)] += PJ[t] * conv
    ks = np.arange(n + 1)
    Hlev = sum(phi(x) for x in size)
    Elog = sum(size[k] * log2(comb(n, k)) for k in range(1, n + 1))
    sb = sum(size[k] * k * log2(n / k) for k in range(1, n + 1)) / I
    tau = EJ / s
    M = Ea
    win = (log2(math.e / tau) + w) / M
    return dict(n=n, mean=c0, HI=H / I, levelI=(Hlev + Elog) / I, sb=sb, window=win, XI=X / I, I=I)


def and_n(n, m):
    # f = -1 iff all -1 ; fhat(S)^2 = 4^(1-n) for S nonempty
    c0 = 1 - 2.0 ** (1 - n)
    H = phi(c0 * c0) + (2 ** n - 1) * phi(4.0 ** (1 - n))
    I = n * 2 ** (n - 1) * 4.0 ** (1 - n)
    tau = (2 ** n - 2 ** (n - m)) * 4.0 ** (1 - n)
    EA = m * I / n
    M = EA / tau
    win = (log2(math.e / tau) + m) / M
    return dict(n=n, m=m, HI=H / I, window=win)


def majority(n):
    mm = (n - 1) // 2
    W = np.zeros(n + 1)
    for k in range(1, n + 1, 2):
        j = (k - 1) // 2
        Mk = 2.0 ** (1 - n) * comb(2 * mm, mm) * comb(mm, j) / comb(2 * mm, 2 * j)
        W[k] = comb(n, k) * Mk * Mk
    I = sum(k * W[k] for k in range(n + 1))
    H = sum(W[k] * (log2(comb(n, k)) - log2(W[k] / comb(n, k))) for k in range(1, n + 1) if W[k] > 0)
    sb = sum(W[k] * k * log2(n / k) for k in range(1, n + 1)) / I
    best = (1e9, None)
    for m in range(1, n + 1):
        # Pr[S meets A] for |A| = m, S uniform given |S| = k
        tau = sum(W[k] * (1 - comb(n - m, k) / comb(n, k)) for k in range(1, n + 1))
        M = (m * I / n) / tau
        win = (log2(math.e / tau) + m) / M
        if win < best[0]:
            best = (win, m)
    return dict(n=n, HI=H / I, sbsum=sum(W), sb=sb, window=best[0], mbest=best[1], I=I)


if __name__ == '__main__':
    print("tribes T_{w,s} (s = round(ln2 * 2^w)): n, mean, H/I, level-bound/I, E_sb log2(n/|S|), window bound, E log2 C(s,J)/I")
    for w in (2, 3, 4, 6, 8, 10, 12, 16, 20):
        s = max(2, round(math.log(2) * 2 ** w))
        r = tribes(w, s)
        print("  w=%2d s=%7d n=%8d mean=%+.3f H/I=%.4f level/I=%.3f Esb=%.3f window=%.3f X/I=%.3f" % (
            w, s, r['n'], r['mean'], r['HI'], r['levelI'], r['sb'], r['window'], r['XI']))
    print("AND_n: H/I and the window bound with |A| = m")
    for n in (10, 20, 40, 80):
        for m in (1, n // 4, n // 2, n):
            r = and_n(n, m)
            print("  n=%3d m=%3d H/I=%.4f window=%.3f" % (n, m, r['HI'], r['window']))
    print("majority: H/I, E_sb log2(n/|S|), best window bound over all window sizes")
    for n in (11, 51, 201, 801, 3201):
        r = majority(n)
        print("  n=%5d H/I=%.4f Esb=%.3f best window=%.3f at m=%d (sum W=%.6f)" % (n, r['HI'], r['sb'], r['window'], r['mbest'], r['sbsum']))
