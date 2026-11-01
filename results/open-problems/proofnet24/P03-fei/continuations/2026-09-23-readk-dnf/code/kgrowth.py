"""Does the term-activation Gibbs bound grow with k?  For families of read-k monotone DNFs with k growing,
report H/I and min over c of the Gibbs bound with pi_t = min(1/2, c 2^{-|V_t|}), c in a wide grid incl. 1/k."""
import math, itertools, numpy as np
from feicore import spectrum, entropy, total_influence, polite
from termref import dnf_tt, term_ref_cost, random_readk
polite()

def bits(ix):
    m = 0
    for j in ix: m |= 1 << int(j)
    return m

def run(name, n, terms):
    tt = dnf_tt(n, terms); P = spectrum(tt); H = entropy(P); I = total_influence(P, n)
    k = max(sum(1 for t in terms if t >> j & 1) for j in range(n))
    best = None
    for c in (1/64, 1/16, 1/8, 1/4, 1/2, 1, 2, 4, 8):
        tot, _ = term_ref_cost(P, n, terms, c)
        if best is None or tot < best[0]: best = (tot, c)
    print(f"{name:28s} n={n:2d} m={len(terms):2d} k={k:2d} Pr[f]={float((tt==-1).mean()):.3f} H/I={H/I:.3f} gibbs/I={best[0]/I:.3f} (c={best[1]:g})", flush=True)

# F1: x0 AND (x1 or ... or xk)
for k in (2, 4, 8, 12, 16):
    run(f"x0&OR_{k}", k + 1, [bits([0, j]) for j in range(1, k + 1)])
# F2: sunflower, core b, k petals of width p
for (b, k, p) in [(4, 2, 2), (4, 4, 2), (4, 6, 2), (6, 4, 2), (8, 4, 2), (6, 6, 2), (4, 8, 2), (3, 6, 2), (3, 4, 3)]:
    n = b + k * p
    if n > 20: continue
    core = list(range(b))
    run(f"sunflower b={b} k={k} p={p}", n, [bits(core + list(range(b + j * p, b + (j + 1) * p))) for j in range(k)])
# F4: vertex stars of the complete r-uniform hypergraph on s vertices (read-r)
for (s, r) in [(6, 2), (7, 2), (6, 3)]:
    E = list(itertools.combinations(range(s), r)); n = len(E)
    if n > 20: continue
    run(f"hyperstars s={s} r={r}", n, [bits([j for j, e in enumerate(E) if u in e]) for u in range(s)])
# F6: at-least-2-of-n (DNF = all pairs), read-(n-1)
for n in (5, 6, 7):
    run(f"thr2 of {n}", n, [bits(pq) for pq in itertools.combinations(range(n), 2)])
# F7: random monotone read-k, widths chosen so that m <= 20
rng = np.random.default_rng(7)
for (n, k, w) in [(12, 2, 3), (12, 4, 3), (12, 6, 4), (14, 6, 5), (12, 8, 5), (16, 5, 4)]:
    for r in range(3):
        terms = random_readk(n, k, [w] * 30, rng)
        if len(terms) > 21: terms = terms[:21]
        run(f"rand n={n} k<={k} w={w}", n, terms)
