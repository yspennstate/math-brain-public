"""Numerical stress test of the lemmas behind Theorem A (dyadic-scale FEI bound for LTFs).

For an LTF f = sign(w.x - theta) and a class G of coordinates with max|w|/min|w| <= kappa (kappa in {1,2}),
and every i in G with derivative g = D_i f:
  (NS)   Stab^G_{1-c/N}[g] <= kappa (2/sqrt(pi)) c^{-1/2} Inf_i      for 0 < c <= N = |G|
  (LOG)  E_{T ~ g^2/Inf_i} ln(N/(|T cap G|+1)) <= 2 ln B + 2,  B = 4 sqrt(2) kappa / sqrt(pi)
and globally
  (MAIN) H(f) <= H(K) + sum_t E log2 C(n_t, K_t),  H(K) <= (3 + log2 d) I,  sum_t E log2 C <= ((3 + 2 ln B)/ln 2) I.
Prints the worst ratios found (value / bound), which must stay <= 1.
"""
import sys, math, itertools
import numpy as np
import numba as nb
from ltf_core import ltf_table, spectrum, HI, popcount


@nb.njit(cache=True)
def class_stats(c, n, i, gmask, N, cs):
    """For g = D_i f: return partial-noise stabilities at rho = 1 - c/N for c in cs,
    E ln(N/(|T&G|+1)) numerator, and Inf_i."""
    b = 1 << i
    stab = np.zeros(cs.shape[0])
    elog = 0.0
    inf = 0.0
    for T in range(c.shape[0]):
        if T & b:
            continue
        v = c[T | b]
        w = v * v
        if w < 1e-300:
            continue
        k = popcount(T & gmask)
        inf += w
        elog += w * np.log(N / (k + 1.0))
        for q in range(cs.shape[0]):
            stab[q] += w * (1.0 - cs[q] / N) ** k
    return stab, elog, inf


@nb.njit(cache=True)
def multilevel_entropy(c, masks):
    """Entropy (bits) of the multi-level vector K = (|S & G_t|)_t and sum_t E log2 C(n_t, K_t)."""
    d = masks.shape[0]
    # encode K as mixed-radix integer
    sizes = np.zeros(d, np.int64)
    for t in range(d):
        sizes[t] = popcount(masks[t])
    radix = np.ones(d + 1, np.int64)
    for t in range(d):
        radix[t + 1] = radix[t] * (sizes[t] + 1)
    P = np.zeros(radix[d])
    elogC = 0.0
    for S in range(c.shape[0]):
        w = c[S] * c[S]
        if w < 1e-300:
            continue
        code = 0
        lc = 0.0
        for t in range(d):
            kt = popcount(S & masks[t])
            code += kt * radix[t]
            # log2 C(n_t, k_t)
            nt = sizes[t]
            lc += (math.lgamma(nt + 1) - math.lgamma(kt + 1) - math.lgamma(nt - kt + 1)) / math.log(2.0)
        P[code] += w
        elogC += w * lc
    HK = 0.0
    for q in range(P.shape[0]):
        if P[q] > 1e-300:
            HK -= P[q] * np.log2(P[q])
    return HK, elogC


def dyadic_classes(w):
    a = np.abs(np.asarray(w, float))
    nz = np.nonzero(a > 0)[0]
    top = a[nz].max()
    cls = {}
    for j in nz:
        t = int(np.floor(np.log2(top / a[j]) + 1e-12))
        cls.setdefault(t, []).append(j)
    return [sorted(v) for k, v in sorted(cls.items())]


def check(w, theta, cs=np.array([0.25, 0.5, 1.0, 2.0, 4.0, 8.0])):
    w = np.asarray(w, float)
    n = len(w)
    f = ltf_table(w, theta)
    c = spectrum(f)
    H, I = HI(c)
    if I < 1e-14:
        return None
    classes = dyadic_classes(w)
    masks = np.array([sum(1 << j for j in G) for G in classes], dtype=np.int64)
    HK, elogC = multilevel_entropy(c, masks)
    d = len(classes)
    worst_ns = 0.0
    worst_log = 0.0
    for G in classes:
        N = len(G)
        if N < 2:
            continue
        gm = sum(1 << j for j in G)
        a = np.abs(w[G])
        for i in G:
            kappa = math.ceil(abs(w[i]) / a.min() - 1e-12)
            B = 4 * math.sqrt(2) * kappa / math.sqrt(math.pi)
            ok_cs = cs[cs <= N]
            stab, elog, inf = class_stats(c, n, i, gm, float(N), ok_cs.astype(np.float64))
            if inf < 1e-14:
                continue
            for q, cc in enumerate(ok_cs):
                bound = kappa * (2 / math.sqrt(math.pi)) / math.sqrt(cc) * inf
                worst_ns = max(worst_ns, stab[q] / bound)
            worst_log = max(worst_log, (elog / inf) / (2 * math.log(B) + 2))
    kap = 2
    Bm = 4 * math.sqrt(2) * kap / math.sqrt(math.pi)
    main_rhs = (3 + math.log2(d)) * I + ((3 + 2 * math.log(Bm)) / math.log(2)) * I
    return dict(H=H, I=I, HK=HK, elogC=elogC, d=d, ns=worst_ns, lg=worst_log,
                chain=(H <= HK + elogC + 1e-9), hk=HK / ((3 + math.log2(d)) * I),
                elc=elogC / (((3 + 2 * math.log(Bm)) / math.log(2)) * I), main=H / main_rhs)


if __name__ == "__main__":
    rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 3)
    ntr = int(sys.argv[2]) if len(sys.argv) > 2 else 200
    worst = dict(ns=0, lg=0, hk=0, elc=0, main=0)
    arg = {}
    chain_ok = True
    for tr in range(ntr):
        n = int(rng.integers(4, 15))
        kind = tr % 5
        if kind == 0:
            w = rng.uniform(1, 2, n)
        elif kind == 1:
            w = rng.integers(1, 3, n).astype(float)
        elif kind == 2:
            w = 2.0 ** rng.integers(0, 4, n) * rng.uniform(1, 1.3, n)
        elif kind == 3:
            w = np.abs(rng.standard_normal(n)) + 0.05
        else:
            w = np.ones(n)
        s = np.linalg.norm(w)
        theta = float(rng.normal() * s * rng.choice([0.2, 1.0, 2.0])) + 1e-7
        r = check(w, theta)
        if r is None:
            continue
        chain_ok &= r['chain']
        for key in worst:
            if r[key] > worst[key]:
                worst[key] = r[key]
                arg[key] = (np.round(w, 3).tolist(), round(theta, 3), round(r['H'] / r['I'], 4), r['d'])
    print("chain rule H <= H(K)+E log C held on all:", chain_ok)
    for key in worst:
        print("worst %-5s ratio (value/bound) = %.4f   at %s" % (key, worst[key], arg.get(key)))
