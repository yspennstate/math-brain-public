"""Numerical audit of the read-k monotone DNF argument.

Checks, on random read-k monotone DNFs and on star functions of graphs:
 (A) exact product structure: under the spectral law of 1_{A_{i,t}}, T cap (V_t minus i) is uniform
     and independent of the rest (max deviation printed);
 (B) density lemma: nu_i(sparse) <= k_i * max_t Pr[Bin(|V_t|-1,1/2) < |V_t|/beta - 1];
 (C) vacuum bound: Var * Lambda <= (8/ln2) p1 and p1 <= I;
 (D) pi_t lower bound: log2(1/pi_t) <= |V_t| + N_t;
 (E) the Gibbs bound with the term reference and these pi_t: H <= E_P log2(1/Q) <= explicit bound.
"""
import math, sys, numpy as np
from feicore import spectrum, entropy, total_influence, popcounts, polite, wht
from termref import dnf_tt, superset_sum, random_readk, random_regular, star_terms

LN2 = math.log(2)


def binom_tail_lt(m, x):
    """Pr[Bin(m,1/2) < x]"""
    s = 0.0
    for j in range(m + 1):
        if j < x:
            s += math.comb(m, j)
    return s / 2 ** m


def analyse(n, terms, beta=4.0, verbose=False):
    N = 1 << n
    xs = np.arange(N, dtype=np.int64)
    pc = popcounts(n)
    m = len(terms)
    sat = np.zeros((m, N), dtype=bool)
    for t, V in enumerate(terms):
        sat[t] = (xs & V) == V
    nsat = sat.sum(axis=0)
    fval = nsat > 0
    g = np.where(fval, -1.0, 1.0)
    P = spectrum(g)
    H = entropy(P)
    I = total_influence(P, n)
    p0 = float((nsat == 0).mean())
    p1 = float((nsat == 1).mean())
    Var = 4 * p0 * (1 - p0)
    sizes = [bin(V).count('1') for V in terms]
    # u_t, Pr[E^(t)], pi_t
    u = np.array([float((sat[t] & (nsat == 1)).mean()) for t in range(m)])
    Et = np.array([float((nsat - sat[t] == 0).mean()) for t in range(m)])
    pi = u / Et
    Nt = [sum(1 for s in range(m) if s != t and (terms[s] & terms[t])) for t in range(m)]
    worstD = max(math.log2(1 / pi[t]) - (sizes[t] + Nt[t]) for t in range(m))
    Lam = float(-np.log2(1 - pi).sum())
    vac = Var * Lam
    # reference Q over term subsets
    unions = np.zeros(1 << m, dtype=np.int64)
    logq = np.full(1 << m, float(np.log(1 - pi).sum()))
    lr = np.log(pi) - np.log(1 - pi)
    for j in range(m):
        h = 1 << j
        unions[h:2 * h] = unions[:h] | terms[j]
        logq[h:2 * h] = logq[:h] + lr[j]
    W = np.zeros(N)
    np.add.at(W, unions, np.exp(logq - LN2 * pc[unions]))
    Q1 = superset_sum(W, n)
    Q1[0] = 0.0
    eta = Var
    mask = P > 1e-300
    mask[0] = False
    gibbs = P[0] * math.log2(1 / (1 - eta)) + float((P[mask] * (math.log2(1 / eta) + np.log2(1 / Q1[mask]))).sum())
    # density lemma and exact product structure
    worst_density = 0.0
    worst_unif = 0.0
    k = max(sum(1 for V in terms if V >> i & 1) for i in range(n))
    sparse_mass = 0.0   # sum_i w_i Inf_i nu_i(sparse)
    for i in range(n):
        Ti = [t for t, V in enumerate(terms) if V >> i & 1]
        if not Ti:
            continue
        rest = xs[(xs >> i) & 1 == 0]
        up = rest | (1 << i)
        piv = fval[up] & ~fval[rest]          # A_i as a subset of x_{-i} (with bit i = 0)
        # full-length indicator on {0,1}^n with bit i fixed 0 (so spectrum lives on sets not containing i)
        Aind = np.zeros(N)
        Aind[rest] = piv
        # 1_{A_i} as a function on the cube with coordinate i ignored: build on N points with both x_i
        Afull = np.zeros(N)
        Afull[rest] = piv
        Afull[up] = piv
        coef = wht(Afull) / N              # Fourier over all n coords; supported on T not containing i
        delta = float(piv.mean())
        if delta <= 0:
            continue
        nu = coef ** 2 / delta
        # sparse event: for all t in Ti, |T cap (V_t minus i)| < |V_t|/beta - 1
        sp = np.ones(N, dtype=bool)
        for t in Ti:
            Vm = terms[t] & ~(1 << i)
            sp &= pc[xs & Vm] < sizes[t] / beta - 1
        nus = float(nu[sp].sum())
        bound = len(Ti) * max(binom_tail_lt(sizes[t] - 1, sizes[t] / beta - 1) for t in Ti)
        worst_density = max(worst_density, nus / bound if bound > 0 else (0 if nus < 1e-12 else 1e9))
        wi = min(sizes[t] for t in Ti)
        sparse_mass += wi * delta * nus
        # exact product structure for each witness piece
        first = np.full(N, -1)
        for x in rest:
            pass
        for t in Ti:
            # A_{i,t}: pivotal and t is the first witness
            wit_prev = np.zeros(len(rest), dtype=bool)
            for s in Ti:
                if s == t:
                    break
                Vm = terms[s] & ~(1 << i)
                wit_prev |= (rest & Vm) == Vm
            Vm = terms[t] & ~(1 << i)
            wit = (rest & Vm) == Vm
            ait = piv & wit & ~wit_prev
            if not ait.any():
                continue
            F = np.zeros(N)
            F[rest] = ait
            F[up] = ait
            c2 = (wht(F) / N) ** 2
            tot = c2.sum()
            # marginal of T cap Vm must be uniform: group by T & Vm
            key = xs & Vm
            marg = np.bincount(key, weights=c2, minlength=N)[np.unique(key)]
            dev = float(np.max(np.abs(marg / tot - 1.0 / len(marg))))
            worst_unif = max(worst_unif, dev)
    return dict(n=n, m=m, k=k, H=H, I=I, HI=H / I, gibbsI=gibbs / I, vacI=vac / I, p1I=p1 / I,
                vac_vs_p1=vac / ((8 / LN2) * p1) if p1 > 0 else 0, worstD=worstD,
                dens=worst_density, unif=worst_unif, sparseI=sparse_mass / I)


if __name__ == '__main__':
    polite()
    rng = np.random.default_rng(5)
    cases = []
    for (w, s) in [(3, 4), (4, 3)]:
        cases.append((f'tribes w{w} s{s}', w * s, [((1 << w) - 1) << (t * w) for t in range(s)]))
    for (s, d) in [(8, 3), (6, 4), (10, 3)]:
        E = random_regular(s, d, rng)
        cases.append((f'stars s{s} d{d}', len(E), star_terms(s, E)))
    for n, k, wl in [(14, 2, [4] * 7), (14, 3, [3] * 12), (15, 2, [3, 3, 4, 4, 5, 5, 6, 6]),
                     (16, 3, [2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7]), (16, 4, [2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 2, 8]),
                     (14, 5, [2, 2, 2, 3, 3, 4, 5, 6, 7, 2, 3])]:
        for r in range(2):
            cases.append((f'random read-{k}', n, random_readk(n, k, wl, rng)))
    for name, n, terms in cases:
        r = analyse(n, terms)
        print(f"{name:18s} n={r['n']:2d} m={r['m']:2d} k={r['k']} H/I={r['HI']:.3f} gibbs/I={r['gibbsI']:.3f} "
              f"vac/I={r['vacI']:.3f} vac/((8/ln2)p1)={r['vac_vs_p1']:.3f} p1/I={r['p1I']:.3f} "
              f"piD={r['worstD']:+.3f} dens={r['dens']:.3f} unifdev={r['unif']:.1e} sparse/I={r['sparseI']:.3f}",
              flush=True)
