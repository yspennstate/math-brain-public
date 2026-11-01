"""Non-monotone read-k DNFs: does the term-activation reference still track H?
Terms are (mask, value) pairs: satisfied iff x & mask == value.
Reports H/I, the Gibbs bound with pi_t = min(1/2, u_t / Pr[E^(t)]), max over terms of
log2(1/pi_t) / |V_t|, and p1/I, Var*Lambda/I.
"""
import math, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite, wht
from termref import superset_sum

LN2 = math.log(2)


def random_nonmono(n, k, widths, rng, pneg=0.5):
    load = np.zeros(n, dtype=int)
    terms = []
    for w in widths:
        avail = np.nonzero(load < k)[0]
        if len(avail) < w:
            break
        ch = rng.choice(avail, size=w, replace=False)
        load[ch] += 1
        m = 0
        v = 0
        for j in ch:
            m |= 1 << int(j)
            if rng.random() > pneg:
                v |= 1 << int(j)
        terms.append((m, v))
    return terms


def irredundant(n, terms):
    N = 1 << n
    xs = np.arange(N, dtype=np.int64)
    sat = [((xs & m) == v) for (m, v) in terms]
    keep = list(range(len(terms)))
    changed = True
    while changed:
        changed = False
        for t in list(keep):
            others = np.zeros(N, dtype=bool)
            for s in keep:
                if s != t:
                    others |= sat[s]
            if not np.any(sat[t] & ~others):
                keep.remove(t)
                changed = True
                break
    return [terms[t] for t in keep]


def analyse(n, terms):
    N = 1 << n
    xs = np.arange(N, dtype=np.int64)
    pc = popcounts(n)
    m = len(terms)
    sat = np.array([((xs & mm) == v) for (mm, v) in terms])
    nsat = sat.sum(axis=0)
    g = np.where(nsat > 0, -1.0, 1.0)
    P = spectrum(g)
    H = entropy(P)
    I = total_influence(P, n)
    p0 = float((nsat == 0).mean())
    p1 = float((nsat == 1).mean())
    Var = 4 * p0 * (1 - p0)
    sizes = [bin(mm).count('1') for (mm, v) in terms]
    u = np.array([float((sat[t] & (nsat == 1)).mean()) for t in range(m)])
    Et = np.array([float((nsat - sat[t] == 0).mean()) for t in range(m)])
    pi = np.minimum(0.5, u / Et)
    ratio = max(math.log2(1 / pi[t]) / sizes[t] for t in range(m))
    Lam = float(-np.log2(1 - pi).sum())
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
    return dict(H=H, I=I, HI=H / I, gib=gibbs / I, ratio=ratio, p1I=p1 / I, vacI=Var * Lam / I, m=m)


if __name__ == '__main__':
    polite()
    rng = np.random.default_rng(17)
    worst = {}
    for n, k, wl in [(12, 2, [3] * 8), (12, 3, [3] * 12), (14, 2, [4] * 7), (14, 3, [3, 3, 4, 4, 5, 5, 3, 4, 5, 6]),
                     (14, 4, [2, 3, 3, 4, 4, 5, 2, 3, 4, 5, 6, 3]), (16, 2, [4] * 8), (16, 3, [4] * 12)]:
        for r in range(6):
            terms = irredundant(n, random_nonmono(n, k, wl, rng))
            if len(terms) < 2:
                continue
            a = analyse(n, terms)
            key = f'read-{k} n={n}'
            w = worst.setdefault(key, dict(HI=0, gib=0, ratio=0, p1I=0, vacI=0, cnt=0))
            for kk in ('HI', 'gib', 'ratio', 'p1I', 'vacI'):
                w[kk] = max(w[kk], a[kk])
            w['cnt'] += 1
    for key, w in worst.items():
        print(key, {kk: (round(vv, 3) if isinstance(vv, float) else vv) for kk, vv in w.items()}, flush=True)
