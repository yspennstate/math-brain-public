"""Term-indexed reference measures for monotone DNFs.

Q(S) = sum_U q(U) [S subset of V(U)] 2^{-|V(U)|},  q = product over terms with prob pi_t.
Gibbs: H(f) <= E_P log2 1/Q(S).  We report E_P log2(1/Q) / I for the best scalar c in pi_t = min(1/2, c 2^{-|V_t|}).
"""
import sys, time, math, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite


def dnf_tt(n, terms):
    N = 1 << n
    xs = np.arange(N, dtype=np.int64)
    val = np.zeros(N, dtype=bool)
    for m in terms:
        val |= (xs & m) == m
    return np.where(val, -1, 1).astype(np.int8)


def superset_sum(W, n):
    g = W.copy()
    for i in range(n):
        g = g.reshape(-1, 2, 1 << i)
        g[:, 0, :] += g[:, 1, :]
        g = g.reshape(-1)
    return g


def term_ref_cost(P, n, terms, c, split_empty=True):
    m = len(terms)
    N = 1 << n
    sizes = np.array([bin(t).count('1') for t in terms])
    pi = np.minimum(0.5, c * 2.0 ** (-sizes))
    # enumerate U by gray-code style accumulation of union masks
    W = np.zeros(N)
    logq0 = float(np.log(1 - pi).sum())
    lr = np.log(pi) - np.log(1 - pi)
    # iterative enumeration over subsets (m <= ~22)
    unions = np.zeros(1 << m, dtype=np.int64)
    logq = np.full(1 << m, logq0)
    for j in range(m):
        h = 1 << j
        unions[h:2 * h] = unions[:h] | terms[j]
        logq[h:2 * h] = logq[:h] + lr[j]
    pc = popcounts(n)
    wts = np.exp(logq - np.log(2.0) * pc[unions])
    np.add.at(W, unions, wts)
    Q = superset_sum(W, n)
    mask = P > 1e-300
    if split_empty:
        # mixture: (1-eta) delta_empty + eta * Q restricted to nonempty, renormalised
        Qn = Q.copy(); Qn[0] = 0.0
        Qn /= Qn.sum()
        eps = 1.0 - P[0]
        eta = min(max(eps, 1e-300), 1 - 1e-12)
        cost0 = P[0] * math.log2(1 / (1 - eta))
        sel = mask.copy(); sel[0] = False
        cost1 = float((P[sel] * (np.log2(1 / eta) + np.log2(1 / Qn[sel]))).sum())
        return cost0 + cost1, cost1
    return float((P[mask] * np.log2(1 / Q[mask])).sum()), None


def best_cost(P, n, terms):
    best = None
    for c in (0.25, 0.5, 1, 2, 4, 8, 16):
        tot, _ = term_ref_cost(P, n, terms, c)
        if best is None or tot < best[0]:
            best = (tot, c)
    return best


def report(name, n, terms):
    t0 = time.time()
    tt = dnf_tt(n, terms)
    P = spectrum(tt)
    H = entropy(P)
    I = total_influence(P, n)
    tot, c = best_cost(P, n, terms)
    print(f"{name:34s} n={n:2d} m={len(terms):2d} Pr[f]={float((tt==-1).mean()):.3f} H/I={H/I:.3f} "
          f"termref/I={tot/I:.3f} (c={c})  [{time.time()-t0:.1f}s]", flush=True)


def random_regular(s, d, rng):
    for _ in range(10000):
        stubs = np.repeat(np.arange(s), d)
        rng.shuffle(stubs)
        e = stubs.reshape(-1, 2)
        if np.any(e[:, 0] == e[:, 1]):
            continue
        keys = set(tuple(sorted(x)) for x in e)
        if len(keys) == len(e):
            return sorted(keys)
    raise RuntimeError


def star_terms(s, edges):
    terms = []
    for u in range(s):
        m = 0
        for j, (a, b) in enumerate(edges):
            if a == u or b == u:
                m |= 1 << j
        terms.append(m)
    return terms


def random_readk(n, k, widths, rng):
    """random monotone DNF, each variable in at most k terms, term widths from list."""
    load = np.zeros(n, dtype=int)
    terms = []
    for w in widths:
        avail = np.nonzero(load < k)[0]
        if len(avail) < w:
            break
        ch = rng.choice(avail, size=w, replace=False)
        load[ch] += 1
        m = 0
        for j in ch:
            m |= 1 << int(j)
        terms.append(m)
    # remove absorbed terms
    terms = [t for t in terms if not any((u != t and (u & t) == u) for u in terms)]
    return sorted(set(terms))


if __name__ == '__main__':
    polite()
    rng = np.random.default_rng(3)
    # read-once controls: tribes
    for (w, s) in [(2, 6), (3, 5), (4, 4), (5, 3)]:
        terms = [((1 << w) - 1) << (t * w) for t in range(s)]
        report(f'tribes w{w} s{s}', w * s, terms)
    for (s, d) in [(8, 3), (10, 3), (12, 3), (8, 4), (10, 4), (12, 4)]:
        E = random_regular(s, d, rng)
        report(f'stars random-regular s{s} d{d}', len(E), star_terms(s, E))
    for n, k, wl in [(16, 2, [4] * 8), (16, 2, [3] * 10), (18, 2, [4] * 9), (18, 3, [4] * 13), (20, 2, [5] * 8),
                     (20, 3, [5] * 12), (16, 3, [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6])]:
        for rep in range(2):
            terms = random_readk(n, k, wl, rng)
            report(f'random read-{k} widths {wl[0]}..{wl[-1]}', n, terms)
