"""Exact check of the cluster (polymer) formula for the Fourier coefficients of a monotone DNF.

f = OR_t [V_t subset of x], Z = 1 - f (the indicator of the zero set), q(U) = Pr[no term disjoint from U is satisfied].
Claim: for every T,
    Zhat(T) = (-1)^{|T|} sum_{Gamma} q(V(Gamma)) prod_{gamma in Gamma} (-1)^{|gamma|} 2^{-|V(gamma)|},
the sum over families Gamma of pairwise variable-disjoint connected clusters of terms (connected in the overlap graph),
each cluster meeting T, with V(Gamma) containing T.  (T = empty: only Gamma = empty, Zhat = q.)
Checked against the Walsh transform on random DNFs with overlapping terms.
"""
import itertools, sys, functools
import numpy as np
print = functools.partial(print, flush=True)


def wht(v):
    a = v.astype(np.float64).copy(); n = a.size; h = 1
    while h < n:
        a = a.reshape(-1, 2 * h); x = a[:, :h].copy(); y = a[:, h:].copy()
        a[:, :h] = x + y; a[:, h:] = x - y; a = a.reshape(n); h *= 2
    return a / n


def components(J, terms):
    J = list(J); comps = []; seen = set()
    for t in J:
        if t in seen:
            continue
        stack = [t]; comp = []; seen.add(t)
        while stack:
            u = stack.pop(); comp.append(u)
            for s in J:
                if s not in seen and terms[s] & terms[u]:
                    seen.add(s); stack.append(s)
        comps.append(frozenset(comp))
    return comps


def check(n, terms, rng=None):
    m = len(terms)
    N = 1 << n
    x = np.arange(N)
    Z = np.ones(N)
    for t in terms:
        Z[(x & t) == t] = 0.0
    Zh = wht(Z)
    # q(U) for every union U that can occur: compute on demand
    qcache = {}
    def q(U):
        if U not in qcache:
            rem = [t for t in terms if not (t & U)]
            ok = np.ones(N, dtype=bool)
            for t in rem:
                ok &= (x & t) != t
            qcache[U] = ok.mean()
        return qcache[U]
    # all subsets J of terms with their components
    fams = {}
    for r in range(m + 1):
        for J in itertools.combinations(range(m), r):
            comps = components(J, terms)
            fams[J] = comps
    worst = 0.0
    for T in range(N):
        # regrouped formula: sum over families Gamma of clusters each meeting T, covering T
        # enumerate Gamma as sets J whose every component meets T and whose union covers T
        s = 0.0
        for J, comps in fams.items():
            ok = True; V = 0
            for c in comps:
                Vc = 0
                for t in c:
                    Vc |= terms[t]
                if not (Vc & T):
                    ok = False; break
                V |= Vc
            if not ok or (V & T) != T:
                continue
            w = q(V)
            for c in comps:
                Vc = 0
                for t in c:
                    Vc |= terms[t]
                w *= (-1) ** len(c) * 2.0 ** (-bin(Vc).count('1'))
            s += w
        s *= (-1) ** bin(T).count('1')
        worst = max(worst, abs(s - Zh[T]))
    return worst


def main():
    rng = np.random.default_rng(11)
    for trial in range(12):
        n = int(rng.integers(6, 11)); m = int(rng.integers(3, 7))
        terms = []
        for _ in range(m):
            w = int(rng.integers(2, 5))
            terms.append(int(sum(1 << int(i) for i in rng.choice(n, size=w, replace=False))))
        # drop duplicates
        terms = list(dict.fromkeys(terms))
        err = check(n, terms)
        print(f"trial {trial}: n={n} m={len(terms)} max |formula - WHT| = {err:.2e}")


if __name__ == "__main__":
    main()
