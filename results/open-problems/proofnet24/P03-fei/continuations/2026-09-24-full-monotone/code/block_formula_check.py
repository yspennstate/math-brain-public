"""Block (Moebius) version of the cluster formula, checked exactly.

A block is U = V(J) for a connected set J of terms; kappa(U) = sum over connected J with V(J) = U of (-1)^{|J|}.
Claims: (1) Z = sum over families of pairwise disjoint blocks of prod kappa(U) x^U  (multilinear, 0/1 variables);
(2) Zhat(T) = (-1)^{|T|} sum_{families: every block meets T, union contains T} q(V) prod kappa(U) 2^{-|U|}.
Also printed: kappa for the k-cliques inside K_{k+1} (expected (-1)^k k for the full edge set).
"""
import itertools, functools
import numpy as np
print = functools.partial(print, flush=True)
from polymer_check import wht, components


def blocks_of(terms):
    m = len(terms); kap = {}
    for r in range(1, m + 1):
        for J in itertools.combinations(range(m), r):
            if len(components(J, terms)) != 1:
                continue
            U = 0
            for t in J:
                U |= terms[t]
            kap[U] = kap.get(U, 0) + (-1) ** r
    return {U: k for U, k in kap.items() if k != 0}


def families(blocks):
    bl = list(blocks)
    out = [()]
    def rec(start, cur, used):
        for i in range(start, len(bl)):
            if bl[i] & used:
                continue
            nxt = cur + (bl[i],)
            out.append(nxt)
            rec(i + 1, nxt, used | bl[i])
    rec(0, (), 0)
    return out


def check(n, terms):
    N = 1 << n; x = np.arange(N)
    Z = np.ones(N)
    for t in terms:
        Z[(x & t) == t] = 0.0
    Zh = wht(Z)
    kap = blocks_of(terms)
    fams = families(kap)
    # (1) multilinear identity pointwise
    err1 = 0.0
    for xv in range(N):
        s = 0.0
        for F in fams:
            prod = 1.0
            for U in F:
                prod *= kap[U] * (1.0 if (xv & U) == U else 0.0)
            s += prod
        err1 = max(err1, abs(s - Z[xv]))
    def q(A):
        ok = np.ones(N, dtype=bool)
        for t in terms:
            if not (t & A):
                ok &= (x & t) != t
        return ok.mean()
    err2 = 0.0
    for T in range(N):
        s = 0.0
        for F in fams:
            V = 0
            for U in F:
                V |= U
            if (V & T) != T or not all(U & T for U in F):
                continue
            w = q(V)
            for U in F:
                w *= kap[U] * 2.0 ** (-bin(U).count('1'))
            s += w
        s *= (-1) ** bin(T).count('1')
        err2 = max(err2, abs(s - Zh[T]))
    return err1, err2, len(kap), len(fams)


def clique_kappa(k):
    """k-cliques inside K_{k+1}: terms = edge sets; return kappa of the full edge set."""
    V = list(range(k + 1)); E = list(itertools.combinations(V, 2)); idx = {e: i for i, e in enumerate(E)}
    terms = []
    for miss in V:
        vs = [u for u in V if u != miss]
        terms.append(sum(1 << idx[e] for e in itertools.combinations(vs, 2)))
    kap = blocks_of(terms)
    full = (1 << len(E)) - 1
    return kap.get(full, 0), len(kap)


if __name__ == "__main__":
    rng = np.random.default_rng(5)
    for trial in range(10):
        n = int(rng.integers(6, 10)); m = int(rng.integers(3, 7)); w = int(rng.integers(2, 4))
        ts = list(dict.fromkeys(int(sum(1 << int(i) for i in rng.choice(n, size=w, replace=False))) for _ in range(m)))
        e1, e2, nb, nf = check(n, ts)
        print(f"trial {trial}: n={n} m={len(ts)} blocks={nb} families={nf}: identity err {e1:.1e}, Fourier err {e2:.1e}")
    for k in range(2, 7):
        kf, nb = clique_kappa(k)
        print(f"k={k}: kappa(E(K_{k+1})) = {kf} (expected {(-1)**k * k}); distinct blocks {nb}")
