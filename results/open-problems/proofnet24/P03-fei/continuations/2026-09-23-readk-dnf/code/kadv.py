"""Adversarial search: how does min_c (term-activation Gibbs bound)/I grow with k on the worst read-k monotone DNFs?
Moves: toggle a variable in a term (respecting read-k), add a term, delete a term.  n = 12, at most 16 terms."""
import math, sys, numpy as np
from feicore import spectrum, entropy, total_influence, polite
from termref import dnf_tt, term_ref_cost
polite()
CS = (1/64, 1/16, 1/4, 1, 4)

def score(n, terms):
    if not terms: return None
    tt = dnf_tt(n, terms)
    if np.all(tt == tt[0]): return None
    P = spectrum(tt); I = total_influence(P, n)
    best = min(term_ref_cost(P, n, terms, c)[0] for c in CS)
    return best / I, entropy(P) / I

def readk_ok(n, terms, k):
    for j in range(n):
        if sum(1 for t in terms if t >> j & 1) > k: return False
    return True

def search(n, k, rng, iters=300):
    terms = []
    while len(terms) < 6:
        w = int(rng.integers(1, 5)); t = 0
        for j in rng.choice(n, size=w, replace=False): t |= 1 << int(j)
        if readk_ok(n, terms + [t], k) and t not in terms: terms.append(t)
    cur = score(n, terms)
    while cur is None:
        terms = terms[:-1]; cur = score(n, terms)
    for it in range(iters):
        cand = list(terms); mv = rng.integers(3)
        if mv == 0 and cand:
            a = int(rng.integers(len(cand))); cand[a] ^= 1 << int(rng.integers(n))
            if cand[a] == 0: continue
        elif mv == 1 and len(cand) < 16:
            w = int(rng.integers(1, 6)); t = 0
            for j in rng.choice(n, size=w, replace=False): t |= 1 << int(j)
            cand.append(t)
        elif mv == 2 and len(cand) > 1:
            cand.pop(int(rng.integers(len(cand))))
        else: continue
        if len(set(cand)) < len(cand) or not readk_ok(n, cand, k): continue
        s = score(n, cand)
        if s is not None and s[0] > cur[0]: terms, cur = cand, s
    return cur, terms

rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 5)
for k in (2, 3, 4, 6, 8):
    best = (0, 0)
    for rep in range(4):
        (g, h), terms = search(12, k, rng)
        if g > best[0]: best = (g, h, len(terms))
    print(f"k={k}: worst min_c Gibbs/I = {best[0]:.3f} (H/I there {best[1]:.3f}, {best[2]} terms)", flush=True)
