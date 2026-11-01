"""Graph DNFs f = OR over edges uv of (x_u and x_v), G k-regular on n vertices (read-k, 2-DNF).
Exact H, I, Var from the truth table; the vacuum term Var*Lambda of the read-k proof, with
Lambda = sum_t log2(1/(1-2^-|V_t|)); p0*mu/I against the path-lemma bound k/4."""
import numpy as np, itertools, sys
import networkx as nx
from feicore import spectrum, entropy, popcounts, polite
polite()
rng = np.random.default_rng(7)

def tt_graph(n, edges):
    xs = np.arange(1 << n)
    val = np.zeros(1 << n, dtype=bool)
    for (u, v) in edges:
        m = (1 << u) | (1 << v)
        val |= (xs & m) == m
    return np.where(val, -1, 1).astype(np.int8), val

rows = []
for n in (12, 14, 16, 18):
    for k in range(1, n):
        if (n * k) % 2: continue
        if k > 10: break
        for rep in range(2):
            G = nx.random_regular_graph(k, n, seed=int(rng.integers(1e9)))
            E = list(G.edges())
            tt, val = tt_graph(n, E)
            P = spectrum(tt)
            pc = popcounts(n)
            H = entropy(P); I = float((P * pc).sum()); V = 1 - P[0]
            p0 = 1 - val.mean()
            mu = len(E) / 4.0
            Lam = len(E) * np.log2(1 / (1 - 0.25))
            J = float((P * pc)[pc >= 2].sum())
            Hp = entropy(P[1:])
            rows.append((n, k, H / I, Hp / J if J > 0 else 0, V * Lam / I, p0 * mu / I, I, p0))
            print(f"n={n:2d} k={k:2d} H/I={H/I:6.3f} H+/J={Hp/J:6.3f} vac/I={V*Lam/I:7.3f} p0mu/I={p0*mu/I:6.3f} I={I:7.3f} p0={p0:.2e}", flush=True)
