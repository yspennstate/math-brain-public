"""Adversarial read-k DNFs for the cover lemma: a shared core B covered k-fold by the cores B_j of
terms t_j = {a_j} u B_j u P_j (a_j and P_j private).  Every cover of a set containing all a_j and
B must use every t_j, so such sets have cover cost ~ k(|P|+..) per element of B.  Measures
E|V(D_beta(S))|/I, E[min cover |V(U)|]/I, the joint-reference bound/I, and H/I."""
import numpy as np, itertools
from feicore import spectrum, popcounts, polite, entropy
from jointref import min_terms_closure, min_superset, h2
from denseunion import dense_union
polite()

def design(q, k, s, p, rng):
    # choose m = q*k/s cores of size s covering each of q core points exactly k times
    m = q * k // s
    for _ in range(2000):
        load = np.zeros(q, dtype=int); cores = []
        ok = True
        for j in range(m):
            cand = np.where(load < k)[0]
            if len(cand) < s: ok = False; break
            w = (k - load[cand]).astype(float); w /= w.sum()
            c = rng.choice(cand, size=s, replace=False, p=w)
            load[c] += 1; cores.append(sorted(c))
        if ok and (load == k).all(): break
    n = q + m * (1 + p)
    terms = []
    nxt = q
    for c in cores:
        V = list(c) + list(range(nxt, nxt + 1 + p)); nxt += 1 + p
        terms.append(V)
    return n, terms

rng = np.random.default_rng(5)
for (q, k, s, p) in [(4, 2, 2, 1), (4, 3, 2, 1), (4, 4, 2, 1), (6, 3, 3, 1), (4, 4, 4, 2), (5, 5, 5, 1), (3, 6, 3, 1), (4, 6, 4, 1), (2, 8, 2, 0), (3, 8, 3, 0)]:
    n, terms = design(q, k, s, p, rng)
    if n > 22: print("skip", q, k, s, p, n); continue
    pc = popcounts(n); xs = np.arange(1 << n)
    val = np.zeros(1 << n, dtype=bool)
    masks = []
    for V in terms:
        mk = sum(1 << v for v in V); masks.append(mk)
        val |= (xs & mk) == mk
    masks = np.array(masks, dtype=np.int64); sizes = np.array([len(V) for V in terms], dtype=np.int64)
    P = spectrum(np.where(val, -1, 1).astype(np.int8))
    H = entropy(P); I = float((P * pc).sum()); Var = 1 - P[0]
    un2, sm2, sp2 = dense_union(masks, sizes, pc, 2, n)
    mt = min_terms_closure(masks, n); reach = mt < (1 << 30)
    msV = min_superset(np.where(reach, pc.astype(float), np.inf), n)
    lam = 1.0 / k
    ms = min_superset(np.where(reach, mt * np.log2(1 / lam) + 2.0 * pc, np.inf), n)
    Np = np.zeros(1 << n)
    for mk in masks: Np += ((xs & mk) == mk)
    logZ = float(np.log2(np.mean((1 + lam) ** Np)))
    nz = np.nonzero(P[1:] > 1e-300)[0] + 1
    bound = h2(Var) + Var * logZ + float((P[nz] * ms[nz]).sum())
    print(f"q={q} k={k} s={s} p={p} n={n} terms={len(terms)}: H/I={H/I:5.2f} bound/I={bound/I:5.2f} "
          f"E|V(D2)|/I={(P*un2).sum()/I:5.2f} sumD2/I={(P*sm2).sum()/I:5.2f} mincover/I={(P[nz]*msV[nz]).sum()/I:5.2f} "
          f"E|S cap B|/I={(P*pc[xs & ((1<<q)-1)]).sum()/I:4.2f}", flush=True)
