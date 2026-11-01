"""Rooted-animal reference measure for read-k DNF formulas.
For nonempty S: dense terms D(S) = {t : |S cap V_t| >= |V_t|/beta}; U_d = minimal subfamily of
D(S) covering S cap V(D(S)); each sparse element i (in no dense term) is covered by a smallest
term t_i; U = U_d u {t_i}.  Components of the overlap graph on U, one root per component.
Code (a sub-probability measure Q on nonempty sets):
  roots R          : product measure, term t in R w.p. lam*pi_t/(1+lam*pi_t), lam = 1/k
  each u in U (BFS): c_u children, prob 1/((c+1)(c+2)); multiset of attachment variables
                     in V_u, 1/C(|V_u|+c-1, c); each child: which of the <=k terms through
                     its attachment variable, 1/k
  S                : |S| = s w.p. 1/(s(s+1)); uniform s-subset of V(U)
L(S) = -log2 of the product.  Checks: sum_S 2^-L(S) <= 1 and H <= h(Var) + sum P(S) L(S),
and compares with the analytic bound."""
import numpy as np
from math import lgamma, log, log2, comb
from collections import deque
from feicore import spectrum, popcounts, polite, entropy
from mincover import random_readk, tt_dnf
polite()
LN2 = log(2)

def log2comb(n, r):
    if r < 0 or r > n: return float('inf')
    return (lgamma(n + 1) - lgamma(r + 1) - lgamma(n - r + 1)) / LN2

def code_length(S, masks, sizes, pis, lam, k, beta, term_of_var):
    m = len(masks)
    popc = lambda x: bin(x).count("1")
    dense = [t for t in range(m) if beta * popc(S & masks[t]) >= sizes[t]]
    Vd = 0
    for t in dense: Vd |= masks[t]
    Sd = S & Vd
    # minimal subcover of Sd by dense terms: greedy removal
    Ud = list(dense)
    changed = True
    while changed:
        changed = False
        for t in list(Ud):
            rest = 0
            for u in Ud:
                if u != t: rest |= masks[u]
            if (Sd & ~rest) == 0:
                Ud.remove(t); changed = True
    # sparse elements
    Us = []
    Wsp = 0
    x = S & ~Vd
    while x:
        i = (x & -x).bit_length() - 1; x &= x - 1
        cand = term_of_var[i]
        t = min(cand, key=lambda t: sizes[t])
        Wsp += sizes[t]
        if t not in Us: Us.append(t)
    U = list(dict.fromkeys(Ud + Us))
    # components
    adj = {u: [v for v in U if v != u and masks[u] & masks[v]] for u in U}
    seen = set(); L = 0.0
    comps = []
    for u in U:
        if u in seen: continue
        comp = []; dq = deque([u]); seen.add(u)
        while dq:
            a = dq.popleft(); comp.append(a)
            for b in adj[a]:
                if b not in seen: seen.add(b); dq.append(b)
        comps.append(comp)
    Ctot = 0
    for comp in comps:
        root = min(comp, key=lambda t: sizes[t])          # cheapest activation
        L += log2(1 / (lam * pis[root]))
        # BFS tree from root
        par = {root: None}; order = [root]; dq = deque([root])
        while dq:
            a = dq.popleft()
            for b in adj[a]:
                if b not in par: par[b] = a; order.append(b); dq.append(b)
        children = {a: [b for b in order if par.get(b) == a] for a in order}
        for a in order:
            c = len(children[a]); Ctot += c
            L += log2((c + 1) * (c + 2))
            if c:
                L += log2comb(sizes[a] + c - 1, c) + c * log2(k)
    VU = 0
    for u in U: VU |= masks[u]
    s = popc(S)
    L += log2(s * (s + 1)) + log2comb(popc(VU), s)
    return L, s, Wsp, len(U), popc(VU)

def h2(v):
    return 0.0 if v <= 0 or v >= 1 else -(v*np.log2(v) + (1-v)*np.log2(1-v))

if __name__ == "__main__":
    rng = np.random.default_rng(21)
    import sys
    beta = float(sys.argv[1]) if len(sys.argv) > 1 else 3.0
    for n in (12, 14):
        pc = popcounts(n)
        for k in (1, 2, 3, 4, 6, 8, 10):
            for rep in range(2):
                terms = random_readk(n, k, rng)
                if not terms: continue
                masks = [sum(1 << int(v) for v in V) for V, _ in terms]
                sizes = [len(V) for V, _ in terms]
                pis = [2.0 ** -w for w in sizes]
                term_of_var = {i: [t for t in range(len(masks)) if masks[t] >> i & 1] for i in range(n)}
                P = spectrum(tt_dnf(n, terms)); H = entropy(P); pcs = pc
                I = float((P * pc).sum()); Var = 1 - P[0]
                if I <= 0: continue
                lam = 1.0 / k
                Lam = sum(log2(1 + lam * p) for p in pis)
                relevant = 0
                for mk in masks: relevant |= mk
                tot = 0.0; kraft = 0.0; EW = 0.0; EL = 0.0
                for S in range(1, 1 << n):
                    if S & ~relevant: continue
                    L, s, W, nu, nv = code_length(S, masks, sizes, pis, lam, k, beta, term_of_var)
                    kraft += 2.0 ** -(L + Lam)
                    if P[S] > 0:
                        EL += P[S] * L; EW += P[S] * W
                bound = h2(Var) + Var * Lam + EL
                print(f"n={n} k={k:2d} beta={beta}: H/I={H/I:5.2f} bound/I={bound/I:6.2f} kraft={kraft:.3f} [Var*Lam/I={Var*Lam/I:4.2f} EL/I={EL/I:6.2f} EW/I={EW/I:5.2f}]", flush=True)
