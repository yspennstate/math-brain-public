# Decision-tree complexity versus relative influence for monotone functions.
# For every monotone f on n <= 5 variables (all of them) and for random monotone DNFs on 8-10 variables, compute by
# dynamic programming over subcubes: the least expected depth E*(f) of a decision tree for f (uniform input), the
# least number of leaves s*(f), the least depth D*(f), and the hereditary expected depth
# L(f) = max over restrictions g of f of E*(g). Check:
#   (OSSS)  max_v Inf_v >= Var(F) / E*(f)          [O'Donnell-Saks-Schramm-Servedio, applied to an optimal tree]
#   E*(f) <= log2 s*(f),  E*(f) <= D*(f)
#   H(f) <= (4.6355 + Psi(2 L - 2)) I(f)           [the decision-tree corollary]
import sys, math, itertools, numpy as np
from mono_enum import monotone_masks, walsh

C1 = 2 / math.log(2) + 2 * math.exp(-0.5) / math.log(2)
def Psi(r): return math.log2(math.e * (r + 2 * math.sqrt(max(r, 0.0)) + 2))

def subcube_dp(tt, n):
    """tt: bool array (F, 2^n), bit j of the point index = x_j. Returns dicts of arrays over subcubes (base-3 index,
    digit 2 = free) for the whole cube: E* (min expected depth), leaves, depth, hereditary E*."""
    F = tt.shape[0]; N3 = 3 ** n
    pw3 = [3 ** j for j in range(n)]
    digits = np.array([[(i // pw3[j]) % 3 for j in range(n)] for i in range(N3)])
    stars = (digits == 2).sum(1)
    order = np.argsort(stars, kind='stable')
    const = np.full((F, N3), -1, dtype=np.int8)
    E = np.zeros((F, N3)); Lv = np.ones((F, N3)); D = np.zeros((F, N3)); Eh = np.zeros((F, N3))
    for idx in order:
        d = digits[idx]
        if stars[idx] == 0:
            x = int(sum(int(d[j]) << j for j in range(n)))
            const[:, idx] = tt[:, x].astype(np.int8)
            continue
        js = [j for j in range(n) if d[j] == 2]
        j0 = js[0]
        c0 = const[:, idx - 2 * pw3[j0]]; c1 = const[:, idx - pw3[j0]]
        const[:, idx] = np.where((c0 == c1) & (c0 >= 0), c0, -1)
        nonc = const[:, idx] < 0
        bestE = np.full(F, np.inf); bestL = np.full(F, np.inf); bestD = np.full(F, np.inf); her = np.zeros(F)
        for j in js:
            a = idx - 2 * pw3[j]; b = idx - pw3[j]
            bestE = np.minimum(bestE, 1 + 0.5 * (E[:, a] + E[:, b]))
            bestL = np.minimum(bestL, Lv[:, a] + Lv[:, b])
            bestD = np.minimum(bestD, 1 + np.maximum(D[:, a], D[:, b]))
            her = np.maximum(her, np.maximum(Eh[:, a], Eh[:, b]))
        E[:, idx] = np.where(nonc, bestE, 0.0)
        Lv[:, idx] = np.where(nonc, bestL, 1.0)
        D[:, idx] = np.where(nonc, bestD, 0.0)
        Eh[:, idx] = np.maximum(E[:, idx], her)
    top = N3 - 1
    return E[:, top], Lv[:, top], D[:, top], Eh[:, top]

def spectral(tt, n):
    N = 1 << n
    G = np.where(tt, -1.0, 1.0)
    h = 1
    while h < N:
        G = G.reshape(G.shape[0], N // (2 * h), 2, h)
        a = G[:, :, 0, :].copy(); b = G[:, :, 1, :]
        G[:, :, 0, :] = a + b; G[:, :, 1, :] = a - b
        G = G.reshape(G.shape[0], N); h *= 2
    Fh = G / N; P = Fh * Fh
    x = np.arange(N)
    pc = np.array([bin(t).count('1') for t in range(N)])
    infs = np.stack([P[:, ((x >> v) & 1) == 1].sum(1) for v in range(n)], 1)
    with np.errstate(divide='ignore', invalid='ignore'):
        H = -(np.where(P > 1e-300, P * np.log2(np.where(P > 1e-300, P, 1)), 0)).sum(1)
    I = (P * pc).sum(1)
    q = 1 - tt.mean(1)
    return H, I, infs, q

def report(tt, n, label):
    E, Lv, D, Eh = subcube_dp(tt, n)
    H, I, infs, q = spectral(tt, n)
    nonconst = I > 1e-12
    Var = 4 * q * (1 - q); m = np.minimum(q, 1 - q)
    maxinf = infs.max(1)
    osss = (maxinf * E / Var)[nonconst]
    lg = np.log2(Lv)
    ok1 = (E[nonconst] <= lg[nonconst] + 1e-12).all(); ok2 = (E[nonconst] <= D[nonconst] + 1e-12).all()
    bound = np.array([C1 + Psi(2 * L - 2) for L in Eh[nonconst]])
    ratio = (H[nonconst] / I[nonconst]) / bound
    # also the relative influence actually available versus the OSSS guarantee 2m/E
    rel = (maxinf / m)[nonconst]
    print('%-26s %8d fns | min maxInf*E*/Var %.4f | E*<=log2 s* %s | E*<=D* %s | max (H/I)/bound %.3f | '
          'min max Inf/m %.4f | max E* %.3f, max L %.3f'
          % (label, nonconst.sum(), osss.min(), ok1, ok2, ratio.max(), rel.min(), E[nonconst].max(), Eh[nonconst].max()),
          flush=True)
    return osss.min(), ratio.max()

if __name__ == '__main__':
    worst_osss = 9.0; worst_ratio = 0.0
    for n in range(1, 6):
        masks = monotone_masks(n)
        N = 1 << n
        tt = ((masks[:, None] >> np.arange(N, dtype=np.uint64)[None, :]) & np.uint64(1)).astype(bool)
        a, b = report(tt, n, 'all monotone n=%d' % n)
        worst_osss = min(worst_osss, a); worst_ratio = max(worst_ratio, b)
    rng = np.random.default_rng(7)
    for n in (8, 9, 10):
        N = 1 << n; x = np.arange(N)
        tts = []
        for t in range(60 if n < 10 else 25):
            k = int(rng.integers(1, 4 * n)); w = int(rng.integers(1, 5))
            f = np.zeros(N, dtype=bool)
            for _ in range(k):
                S = rng.choice(n, size=min(w, n), replace=False)
                term = np.ones(N, dtype=bool)
                for v in S: term &= ((x >> int(v)) & 1).astype(bool)
                f |= term
            if f.any() and not f.all(): tts.append(f)
        a, b = report(np.array(tts), n, 'random monotone DNF n=%d' % n)
        worst_osss = min(worst_osss, a); worst_ratio = max(worst_ratio, b)
    print('smallest max_v Inf_v * E*(f) / Var over all cases: %.4f (OSSS says >= 1)' % worst_osss)
    print('largest (H/I) / (4.6355 + Psi(2L-2)): %.4f (the corollary says <= 1)' % worst_ratio)
