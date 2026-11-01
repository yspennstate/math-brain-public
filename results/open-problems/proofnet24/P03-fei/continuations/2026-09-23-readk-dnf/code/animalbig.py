"""Larger-scale check of the rooted-animal bound (Theorem 2.5) at beta = 8 (the paper's clean-constant choice):
random read-k DNFs with n = 16, k up to 12, graph DNFs (edges of random k-regular graphs, n = 14..16) and
shared-core designs.  For each formula: H <= h(Var) + Var*Lam + sum P L_run (asserted), Kraft sum of the runs,
and the ratio of the realised bound to the theorem's constant 30 + 5.6 log2 k."""
import numpy as np, math
import networkx as nx
from animalref import code_length, h2
from feicore import spectrum, popcounts, entropy, polite
from mincover import random_readk, tt_dnf
from designdnf import design
polite()
rng = np.random.default_rng(2026)
def run(n, terms, beta=8.0, label=""):
    k = int(max(np.bincount(np.concatenate([np.array(V) for V, _ in terms]), minlength=n)))
    masks = [sum(1 << int(v) for v in V) for V, _ in terms]; sizes = [len(V) for V, _ in terms]
    pis = [2.0 ** -w for w in sizes]
    tov = {i: [t for t in range(len(masks)) if masks[t] >> i & 1] for i in range(n)}
    P = spectrum(tt_dnf(n, terms)); pc = popcounts(n)
    H = entropy(P); I = float((P * pc).sum()); Var = 1 - P[0]
    if I <= 0: return
    lam = 1.0 / k; Lam = sum(math.log2(1 + lam * p) for p in pis)
    rel = 0
    for mk in masks: rel |= mk
    EL = 0.0; kraft = 0.0
    nz = np.nonzero(P > 1e-300)[0]
    for S in range(1, 1 << n):
        if S & ~rel: continue
        L, s, W, nu, nv = code_length(S, masks, sizes, pis, lam, k, beta, tov)
        kraft += 2.0 ** -(L + Lam)
        if P[S] > 0: EL += P[S] * L
    bound = h2(Var) + Var * Lam + EL
    assert H <= bound + 1e-9
    print(f"{label:28s} n={n} k={k:2d}: H/I={H/I:5.2f} bound/I={bound/I:6.2f} (theorem {30 + 5.6 * math.log2(k):6.2f}) kraft={kraft:.3f}", flush=True)
for k in (6, 8, 10, 12):
    for rep in range(2):
        run(16, random_readk(16, k, rng, 2, 5), label=f"random read-{k}")
for n, k in ((14, 6), (14, 8), (16, 6), (16, 10)):
    G = nx.random_regular_graph(k, n, seed=int(rng.integers(1e9)))
    run(n, [(np.array([u, v]), np.ones(2, dtype=int)) for u, v in G.edges()], label=f"graph DNF {k}-regular")
for (q, kk, s, p) in [(4, 4, 2, 1), (3, 8, 3, 0), (4, 6, 4, 1)]:
    n, V = design(q, kk, s, p, rng)
    run(n, [(np.array(v), np.ones(len(v), dtype=int)) for v in V], label=f"shared-core q{q} k{kk}")
