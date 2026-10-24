"""The one O(k) step left for read-k DNFs: the dense cover. With d_S(i) = #{terms t through i with |S cap V_t| >= |V_t|/beta}
the proof pays beta * sum_{i in S} d_S(i). Measure, per family and k:
  D1 = max_i E_{nu_i} d_S(i)                  (the true per-element count; O(log k) or O(1) would suffice)
  D2 = max_{i,s} ln E_{nu_{i,s}} exp(lam d)   (bounded exponential moment under single pieces -> Jensen gives D1 <= (ln k + D2)/lam)
  R  = E_S[sum_{t dense} |V_t|] / I            (the dense-cover cost the current proof pays)."""
import math, itertools, numpy as np
from feicore import spectrum, total_influence, popcounts, polite, wht
from termref import dnf_tt, random_readk
polite()
BETA = 3.0; LAM = 0.5

def bits(ix):
    m = 0
    for j in ix: m |= 1 << int(j)
    return m

def analyse(name, n, terms):
    N = 1 << n; xs = np.arange(N); pc = popcounts(n)
    tt = dnf_tt(n, terms); f = tt == -1
    P = spectrum(tt.astype(float)); I = total_influence(P, n)
    sizes = [bin(t).count('1') for t in terms]
    fill = [pc[xs & t] for t in terms]                         # |S cap V_t| for every S
    dense = [fill[j] >= sizes[j] / BETA for j in range(len(terms))]
    k = max(sum(1 for t in terms if t >> j & 1) for j in range(n))
    R = float(sum((P * dense[j] * sizes[j]).sum() for j in range(len(terms))) / I)
    D1 = 0.0; D2 = -1e9
    for i in range(n):
        thru = [j for j, t in enumerate(terms) if t >> i & 1]
        if not thru: continue
        rest = xs[(xs >> i) & 1 == 0]; up = rest | (1 << i)
        d = f[up].astype(float) - f[rest].astype(float)
        if not np.any(d): continue
        Sfull = rest | (1 << i)                                 # S = T + i, indexed by T = rest
        dS = np.zeros(len(rest))
        for j in thru: dS += dense[j][Sfull]
        Dg = np.zeros(N); Dg[rest] = d; Dg[up] = d
        nu = (wht(Dg) / N) ** 2; nu = nu / nu.sum(); nuT = nu[rest]
        D1 = max(D1, float((nuT * dS).sum()))
        taken = np.zeros(len(rest), dtype=bool)
        for j in thru:                                          # pieces in index order: least satisfied t minus i
            sat = (up & terms[j]) == terms[j]
            sel = sat & (d != 0) & ~taken; taken |= sat & (d != 0)
            if not sel.any(): continue
            Dl = np.zeros(N); Dl[rest] = d * sel; Dl[up] = d * sel
            nl = (wht(Dl) / N) ** 2; nl = nl / nl.sum()
            D2 = max(D2, math.log(float((nl[rest] * np.exp(LAM * dS)).sum())))
    print(f"{name:30s} n={n:2d} m={len(terms):2d} k={k:2d}  E_nu d (max over i) {D1:6.3f}   max ln E_piece e^(d/2) {D2:6.3f}"
          f"   dense-cover cost/I {R:6.3f}", flush=True)
    return k, D1, D2, R

for k in (2, 4, 8, 12, 16):
    analyse(f"x0 & OR_{k}", k + 1, [bits([0, j]) for j in range(1, k + 1)])
for (b, k, p) in [(4, 4, 1), (6, 6, 1), (4, 8, 1), (8, 8, 1), (6, 10, 1), (4, 4, 2), (6, 6, 2), (4, 8, 2), (3, 6, 2)]:
    n = b + k * p
    if n > 20: continue
    core = list(range(b))
    analyse(f"sunflower b={b} k={k} p={p}", n, [bits(core + list(range(b + j * p, b + (j + 1) * p))) for j in range(k)])
for (s, r) in [(6, 2), (7, 2), (6, 3)]:
    E = list(itertools.combinations(range(s), r)); n = len(E)
    if n > 20: continue
    analyse(f"hyperstars s={s} r={r}", n, [bits([j for j, e in enumerate(E) if u in e]) for u in range(s)])
for n in (5, 6, 7, 8):
    analyse(f"thr2 of {n}", n, [bits(pq) for pq in itertools.combinations(range(n), 2)])
rng = np.random.default_rng(11)
for k in (2, 4, 6, 8, 10):
    for rep in range(3):
        n = 16; widths = list(rng.integers(2, 6, size=40))
        terms = random_readk(n, k, widths, rng)
        if terms: analyse(f"random read-{k} #{rep}", n, terms)
