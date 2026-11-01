"""Audit of the linear-in-k version for arbitrary (non-monotone, possibly redundant) read-k DNFs.

pi_t = 2^{-|V_t|}.  Checks:
 (V1) path lemma:  p0 * mu <= (1/2) * sum_j Inf_j * kappa_j,  kappa_j = sum_{t contains j} 2^{pos-1}... we check two
      forms: the crude  p0*mu <= (k/4) I  and the refined  p0*mu <= (1/2) max_j sum_{t ni j} 1/|V_t| * I ... (random order)
 (V2) density lemma for non-monotone pieces (exact uniformity + ratio),
 (V3) Gibbs bound with pi_t = 2^{-|V_t|} vs H and vs the proved constant 2.886 + 10.78 k.
"""
import math, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite, wht
from termref import superset_sum
from readk_nonmono import random_nonmono

LN2 = math.log(2)


def binom_tail_lt(m, x):
    return sum(math.comb(m, j) for j in range(m + 1) if j < x) / 2 ** m


def analyse(n, terms, beta=3.0):
    N = 1 << n
    xs = np.arange(N, dtype=np.int64)
    pc = popcounts(n)
    m = len(terms)
    sat = np.array([((xs & mm) == v) for (mm, v) in terms])
    nsat = sat.sum(axis=0)
    fval = nsat > 0
    g = np.where(fval, -1.0, 1.0)
    P = spectrum(g)
    H = entropy(P)
    I = total_influence(P, n)
    p0 = float((~fval).mean())
    Var = 4 * p0 * (1 - p0)
    sizes = np.array([bin(mm).count('1') for (mm, v) in terms])
    mu = float((2.0 ** -sizes).sum())
    k = max(sum(1 for (mm, v) in terms if mm >> j & 1) for j in range(n))
    kap = max((sum(1.0 / sizes[t] for t in range(m) if terms[t][0] >> j & 1) for j in range(n)), default=0)
    path_crude = p0 * mu / (k / 4 * I)
    path_ref = p0 * mu / (0.5 * kap * I)
    # Gibbs with pi = 2^{-|V_t|}
    pi = 2.0 ** -sizes
    unions = np.zeros(1 << m, dtype=np.int64)
    logq = np.full(1 << m, float(np.log(1 - pi).sum()))
    lr = np.log(pi) - np.log(1 - pi)
    for j in range(m):
        h = 1 << j
        unions[h:2 * h] = unions[:h] | terms[j][0]
        logq[h:2 * h] = logq[:h] + lr[j]
    W = np.zeros(N)
    np.add.at(W, unions, np.exp(logq - LN2 * pc[unions]))
    Q1 = superset_sum(W, n)
    Q1[0] = 0.0
    mask = P > 1e-300
    mask[0] = False
    gibbs = P[0] * math.log2(1 / (1 - Var)) + float((P[mask] * (math.log2(1 / Var) + np.log2(1 / Q1[mask]))).sum())
    # density lemma (non-monotone pieces)
    worst_dens = 0.0
    worst_unif = 0.0
    for i in range(n):
        Ti = [t for t in range(m) if terms[t][0] >> i & 1]
        if not Ti:
            continue
        rest = xs[(xs >> i) & 1 == 0]
        up = rest | (1 << i)
        d = fval[up].astype(float) - fval[rest].astype(float)   # D_i g in {-1,0,1}
        if not np.any(d):
            continue
        Dfull = np.zeros(N)
        Dfull[rest] = d
        Dfull[up] = d
        coef = wht(Dfull) / N
        delta = float(np.abs(d).mean())
        nu = coef ** 2 / delta
        sp = np.ones(N, dtype=bool)
        for t in Ti:
            Vm = terms[t][0] & ~(1 << i)
            sp &= pc[xs & Vm] < sizes[t] / beta - 1
        nus = float(nu[sp].sum())
        bound = len(Ti) * max(binom_tail_lt(sizes[t] - 1, sizes[t] / beta - 1) for t in Ti)
        if bound > 0:
            worst_dens = max(worst_dens, nus / bound)
        elif nus > 1e-12:
            worst_dens = max(worst_dens, 1e9)
        # uniformity of each first-witness piece
        prev = np.zeros(len(rest), dtype=bool)
        for t in Ti:
            mm, v = terms[t]
            Vm = mm & ~(1 << i)
            wit = (rest & Vm) == (v & Vm)
            piece = (d != 0) & wit & ~prev
            prev |= wit
            if not piece.any():
                continue
            F = np.zeros(N)
            F[rest] = d * piece
            F[up] = d * piece
            c2 = (wht(F) / N) ** 2
            key = xs & Vm
            u = np.unique(key)
            marg = np.bincount(key, weights=c2, minlength=N)[u]
            worst_unif = max(worst_unif, float(np.max(np.abs(marg / c2.sum() - 1.0 / len(u)))))
    return dict(k=k, HI=H / I, gibI=gibbs / I, bound=2.886 + 10.78 * k, path_crude=path_crude,
                path_ref=path_ref, dens=worst_dens, unif=worst_unif, m=m)


if __name__ == '__main__':
    polite()
    rng = np.random.default_rng(23)
    worst = {}
    configs = [(10, 2, [2, 2, 3, 3, 3, 4]), (12, 2, [3] * 8), (12, 3, [2, 3, 3, 4, 4, 2, 3, 5, 2]),
               (14, 2, [4] * 7), (14, 3, [3, 3, 4, 4, 5, 5, 3, 4, 5, 6]), (14, 4, [2, 3, 3, 4, 4, 5, 2, 3, 4, 5, 6, 3]),
               (16, 3, [4] * 12), (12, 5, [2, 2, 2, 3, 3, 3, 4, 4, 2, 3, 2, 5])]
    for n, k, wl in configs:
        for r in range(8):
            for pneg in (0.0, 0.3, 0.5):
                terms = random_nonmono(n, k, wl, rng, pneg=pneg)   # NOT made irredundant on purpose
                if len(terms) < 1:
                    continue
                a = analyse(n, terms)
                key = f'n={n} k<={k}'
                w = worst.setdefault(key, dict(HI=0, gibI=0, path_crude=0, path_ref=0, dens=0, unif=0, cnt=0))
                for kk in ('HI', 'gibI', 'path_crude', 'path_ref', 'dens', 'unif'):
                    w[kk] = max(w[kk], a[kk])
                w['cnt'] += 1
    for key, w in worst.items():
        print(key, {kk: (round(float(vv), 4) if isinstance(vv, (float, np.floating)) else vv) for kk, vv in w.items()},
              flush=True)
