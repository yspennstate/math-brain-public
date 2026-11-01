"""Explicit per-set charges combined in Theorem A (n <= 20, exact Walsh).

For nonempty S with p_S = Fhat(S)^2:
  cnt(S)  = log2 C(n,|S|)                                    (uniform reference on level |S|)
  rank(S) = |S| log2(e a/(a-1)) + a log2(e) sum_{i in S} ln+(r(i)/|S|)   (F5 Lemma 6, a = 1.2006422748)
  mix(S)  = log2 3 + min(cnt(S), rank(S))                    (mixture reference, the explicit part of Theorem A)
Reported: E_p[charge]/I for each, against H/I, and the exact level-conditional check
  H(S | |S| = d) <= log2 3 + E[min(cnt, rank) | |S| = d]  for every level d (Gibbs with the mixture).
The ordering r is by decreasing influence (ties by index); for the LTF, by decreasing weight.
"""
import math
import numpy as np
from fei_core import (limit_process, spectrum, tribes, majority, recmaj3, bent_plus_flip, numaro_g,
                      and_n, one_point_flip, ltf)

A = 1.2006422748


def charges(F, order=None):
    n, p, sz = spectrum(F)
    N = 1 << n
    idx = np.arange(N, dtype=np.int64)
    infl = np.array([p[(idx >> i) & 1 == 1].sum() for i in range(n)])
    if order is None:
        order = np.argsort(-infl, kind="stable")
    rank = np.empty(n, dtype=np.int64)
    rank[order] = np.arange(1, n + 1)
    mask = (p > 0) & (sz > 0)
    S = idx[mask]
    ps = p[mask]
    ks = sz[mask].astype(np.float64)
    lnplus = np.zeros(len(S))
    for i in range(n):
        has = ((S >> i) & 1) == 1
        lnplus += np.where(has, np.maximum(np.log(rank[i] / ks), 0.0), 0.0)
    rank_c = ks * math.log2(math.e * A / (A - 1)) + A * math.log2(math.e) * lnplus
    lgc = np.array([math.log2(math.comb(n, int(k))) for k in ks])
    mix = math.log2(3) + np.minimum(lgc, rank_c)
    I = float((sz * p).sum())
    H = float(-(p[p > 0] * np.log2(p[p > 0])).sum())
    # level-conditional Gibbs check
    ok = True
    for d in range(1, n + 1):
        sel = ks == d
        if not sel.any():
            continue
        q = ps[sel] / ps[sel].sum()
        Hd = float(-(q * np.log2(q)).sum())
        bound = float((q * mix[sel]).sum())
        if Hd > bound + 1e-9:
            ok = False
    return H / I, float((ps * lgc).sum()) / I, float((ps * rank_c).sum()) / I, float((ps * mix).sum()) / I, ok


if __name__ == "__main__":
    limit_process()
    print(f"{'function':26s} {'H/I':>7s} {'cnt/I':>7s} {'rank/I':>7s} {'mix/I':>7s}  level-Gibbs")
    fams = [("numaro g", numaro_g(), None), ("tribes w2 s8", tribes(2, 8), None), ("tribes w4 s5", tribes(4, 5), None),
            ("recmaj3 depth2", recmaj3(2), None), ("bent+flip m=12", bent_plus_flip(12), None),
            ("bent+flip m=18", bent_plus_flip(18), None), ("AND_16", and_n(16), None),
            ("maj18+flip (F4 6.1)", one_point_flip(18), None), ("majority 19", majority(19), None)]
    w = np.arange(1, 21) ** -0.5
    fams.append(("LTF w=i^-1/2 n=20", ltf(w, 0.0), np.argsort(-w, kind="stable")))
    w2 = 2.0 ** -np.arange(20)
    fams.append(("LTF w=2^-i n=20 (AND/OR)", ltf(w2, 0.3), np.argsort(-w2, kind="stable")))
    for name, F, order in fams:
        hi, c, r, m, ok = charges(F, order)
        print(f"{name:26s} {hi:7.3f} {c:7.3f} {r:7.3f} {m:7.3f}  {'OK' if ok else 'FAIL'}", flush=True)
