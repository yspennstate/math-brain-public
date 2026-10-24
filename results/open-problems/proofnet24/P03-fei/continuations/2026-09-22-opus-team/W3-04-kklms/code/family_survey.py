"""Survey of the quantities that separate KKLMS from FEI, on the hard families.

For each function: H/I; the KKLMS Theorem 1.3 charge  K13 = sum |S| log2(|S|+1) Fhat^2 / I = E_mu log2(|S|+1)
(their bound is H <= K (K13 + 1) I); the counting charge CNT = sum Fhat^2 log2 C(n,|S|) / I;
and the tail T(C)/I = mu(lambda >= C) of the per-element log-coefficient lambda(S) = log2(1/Fhat^2)/|S|.
FEI is equivalent to  int_0^inf T(C)/I dC = (H - empty term)/I  being bounded.
Exact Walsh transforms for n <= 20; closed forms for majority and tribes at large n;
Galton-Watson generating functions / sampling for recursive majority and the towers of Numaro's g.
"""
import math
import numpy as np
import mpmath as mp
from fei_core import (limit_process, spectrum, tribes, majority, recmaj3, bent_plus_flip, numaro_g,
                      and_n, one_point_flip, ltf, lam_mu_arrays, tail_T)

CS = [2, 4, 6, 8, 12, 16]


def lgC(a, b):
    return (math.lgamma(a + 1) - math.lgamma(b + 1) - math.lgamma(a - b + 1)) / math.log(2)


def walsh_row(name, F):
    n, p, sz = spectrum(F)
    mask = (p > 0) & (sz > 0)
    I = float((sz * p).sum())
    H = float(-(p[p > 0] * np.log2(p[p > 0])).sum())
    k13 = float((sz[mask] * np.log2(sz[mask] + 1) * p[mask]).sum()) / I
    cnt = float(sum(p[mask][sz[mask] == d].sum() * lgC(n, d) for d in range(1, n + 1))) / I
    lam, mu, _, _, _ = lam_mu_arrays(F)
    tails = tail_T(lam, mu, CS)
    return (name, n, H / I, k13, cnt, tails)


def majority_row(n):
    m = (n - 1) // 2
    mp.mp.dps = 40
    lnc = lambda a, b: mp.loggamma(a + 1) - mp.loggamma(b + 1) - mp.loggamma(a - b + 1)
    base = -2 * m * mp.log(2) + lnc(2 * m, m)
    H = I = k13 = cnt = mp.mpf(0)
    lam_mu = []
    for k in range(1, n + 1, 2):
        j = (k - 1) // 2
        lnM = base + lnc(m, j) - lnc(2 * m, 2 * j)
        Wk = mp.e ** (lnc(n, k) + 2 * lnM)
        l2c = -2 * lnM / mp.log(2)
        H += Wk * l2c
        I += k * Wk
        k13 += k * mp.log(k + 1, 2) * Wk
        cnt += Wk * lnc(n, k) / mp.log(2)
        lam_mu.append((float(l2c / k), float(k * Wk)))
    tails = [sum(w for (l, w) in lam_mu if l >= C) / float(I) for C in CS]
    return (f"majority n={n}", n, float(H / I), float(k13 / I), float(cnt / I), tails)


def tribes_row(w, s):
    """OR of s disjoint ANDs of width w (closed form: |Fhat(S)| = 2 (1-2^-w)^(s-t) 2^(-w t),
    t = number of blocks met by S; given t, |S| = sum of t iid Bin(w,1/2) conditioned >= 1)."""
    n = w * s
    lnq = lambda t: math.log2(4) + 2 * (s - t) * math.log2(1 - 2.0 ** -w) - 2 * w * t
    # size distribution of one met block: Bin(w,1/2) conditioned >= 1
    one = np.array([0.0] + [math.comb(w, a) / (2 ** w - 1) for a in range(1, w + 1)])
    H = I = k13 = cnt = 0.0
    lam_mu = []
    dist = np.array([1.0])
    for t in range(1, s + 1):
        dist = np.convolve(dist, one)
        lw = lgC(s, t) + t * math.log2(2 ** w - 1) + lnq(t)  # log2 of total weight on t-sets
        if lw < -80:
            if t > 3:
                break
            continue
        wt = 2.0 ** lw
        sizes = np.arange(len(dist))
        H += wt * (-lnq(t))
        I += wt * float((sizes * dist).sum())
        k13 += wt * float((sizes * np.log2(sizes + 1) * dist).sum())
        cnt += wt * float(sum(dist[a] * lgC(n, a) for a in range(1, len(dist)) if dist[a] > 0))
        for a in range(1, len(dist)):
            if dist[a] > 0:
                lam_mu.append((-lnq(t) / a, wt * a * dist[a]))
    tails = [sum(x for (l, x) in lam_mu if l >= C) / I for C in CS]
    return (f"tribes w={w} s={s}", n, H / I, k13 / I, cnt / I, tails)


def recmaj_gw_row(depth, samples=200000, rng=None):
    """RecMaj3: spectral sample = Galton-Watson tree, offspring 1 (prob 3/4) or 3 (prob 1/4);
    Fhat^2 = 4^-(internal nodes), |S| = leaves.  Exact H, I; K13 exact from the pgf; tails by sampling."""
    # exact pgf of the leaf count
    P = np.array([0.0, 1.0])
    for _ in range(depth):
        P3 = np.convolve(np.convolve(P, P), P)
        Q = np.zeros(len(P3))
        Q[:len(P)] += 0.75 * P
        Q += 0.25 * P3
        P = Q
    sizes = np.arange(len(P))
    I = float((sizes * P).sum())
    H = 2 * sum(1.5 ** l for l in range(depth))
    k13 = float((sizes * np.log2(sizes + 1) * P).sum()) / I
    n = 3 ** depth
    cnt = float(sum(P[a] * lgC(n, a) for a in range(1, len(P)) if P[a] > 0)) / I
    rng = rng or np.random.default_rng(1)
    z = np.ones(samples, dtype=np.int64)
    internal = np.zeros(samples, dtype=np.int64)
    for _ in range(depth):
        internal += z
        three = rng.binomial(z, 0.25)
        z = z + 2 * three
    lam = 2 * internal / z
    wts = z / z.mean()
    tails = [float((wts * (lam >= C)).mean()) for C in CS]
    return (f"recmaj3 depth={depth}", n, H / I, k13, cnt, tails)


def tower_row(g_table, depth, samples=100000, rng=None):
    """Tower G_k = g(G_{k-1},...) of a balanced g: the spectral sample is a random tree; sample it."""
    rng = rng or np.random.default_rng(2)
    n0, p, sz = spectrum(g_table)
    assert p[0] < 1e-15, "g must be balanced"
    idx = np.nonzero(p > 0)[0]
    probs = p[idx] / p[idx].sum()
    sizes = sz[idx]
    logc = np.log2(1.0 / p[idx])
    Hg = float((p[idx] * logc).sum())
    Ig = float((p[idx] * sizes).sum())

    def sample_tree(k, m):
        # returns (leaves, total log2(1/coef^2)) for m independent spectral samples of G_k
        pick = rng.choice(len(idx), size=m, p=probs)
        lv = sizes[pick].astype(np.int64).copy()
        lc = logc[pick].copy()
        if k == 1:
            return lv, lc
        tot = int(lv.sum())
        sub_l, sub_c = sample_tree(k - 1, tot)
        owner = np.repeat(np.arange(m), lv)
        L = np.bincount(owner, weights=sub_l, minlength=m)
        Cc = np.bincount(owner, weights=sub_c, minlength=m)
        return L.astype(np.int64), lc + Cc

    L, Cc = sample_tree(depth, samples)
    lam = Cc / L
    wts = L / L.mean()
    I = Ig ** depth
    H = Hg * (Ig ** depth - 1) / (Ig - 1)
    k13 = float((wts * np.log2(L + 1)).mean())
    tails = [float((wts * (lam >= C)).mean()) for C in CS]
    return (f"tower of numaro g, depth={depth}", 18 ** depth, H / I, k13, float("nan"), tails)


def fmt(row):
    name, n, hi, k13, cnt, tails = row
    t = " ".join(f"{x:8.2e}" for x in tails)
    return f"{name:34s} {n:>10} {hi:7.3f} {k13:7.3f} {cnt:8.3f} | {t}"


if __name__ == "__main__":
    limit_process()
    print("columns: name, n, H/I, K13 = E_mu log2(|S|+1), CNT = sum Fhat^2 log2 C(n,|S|) / I | mu(lambda >= C) for C =", CS)
    rows = []
    for (name, F) in [("numaro g", numaro_g()), ("tribes w2 s8", tribes(2, 8)), ("tribes w3 s6", tribes(3, 6)),
                      ("tribes w4 s5", tribes(4, 5)), ("recmaj3 depth2", recmaj3(2)),
                      ("bent+flip m=4", bent_plus_flip(4)), ("bent+flip m=12", bent_plus_flip(12)),
                      ("bent+flip m=18", bent_plus_flip(18)), ("AND_16", and_n(16)),
                      ("maj18+flip (F4 6.1)", one_point_flip(18)), ("majority 19", majority(19)),
                      ("LTF w=i^-1/2 n=20", ltf(np.arange(1, 21) ** -0.5, 0.0))]:
        rows.append(walsh_row(name, F))
        print(fmt(rows[-1]), flush=True)
    for n in (101, 1001, 10001, 100001):
        rows.append(majority_row(n))
        print(fmt(rows[-1]), flush=True)
    for (w, s) in ((4, 11), (6, 44), (8, 177), (10, 709), (12, 2839), (14, 11356)):
        rows.append(tribes_row(w, s))
        print(fmt(rows[-1]), flush=True)
    for depth in (2, 4, 6, 8, 10):
        rows.append(recmaj_gw_row(depth))
        print(fmt(rows[-1]), flush=True)
    g = numaro_g()
    for depth in (1, 2, 3, 4):
        rows.append(tower_row(g, depth, samples=60000 if depth < 4 else 20000))
        print(fmt(rows[-1]), flush=True)
