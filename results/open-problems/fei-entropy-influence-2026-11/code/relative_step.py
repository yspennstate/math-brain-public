"""Numerical check of the relative step bound and of the short-term lemma (FLOW 12(v), items 1 and 2).

(A) For every Boolean f and coordinate i with Inf_i > 0:
        E_i + J_i <= Inf_i * (C0 + log2(1 + Var(f) / Inf_i)),   C0 = 1/ln2 + 2.61 + 2/ln2 = 6.94
    (E_i = H(1[i in U] | U - i), J_i = Jensen-Shannon divergence of the spectra of the two restrictions at x_i).
(B) If t is a term (a conjunction of k literals, any signs) with t <= f and f is not constant, then some variable v
    of t has Inf_v >= 2 P[f = 0] / (2^k - 1).
(C) Hence H <= (w + 7.94) I for every DNF of width w, monotone or not.

Functions: +-1 valued truth tables, -1 = true; bit j of the index is x_j.
Usage: python relative_step.py [seed]
"""
import sys
import numpy as np
from rand_restrict_identity import wht, ent

C0 = 1 / np.log(2) + 2.61 + 2 / np.log(2)


def steps(f, n):
    """list of (Inf_i, E_i, J_i)."""
    mu = wht(f) ** 2
    idx = np.arange(1 << n)
    out = []
    for i in range(n):
        lo = idx[(idx >> i) & 1 == 0]
        p, q = mu[lo], mu[lo | (1 << i)]
        nu = p + q
        e = ent(np.concatenate((p, q))) - ent(nu)
        j = ent(nu) - 0.5 * ent(wht(f[lo]) ** 2) - 0.5 * ent(wht(f[lo | (1 << i)]) ** 2)
        out.append((float(q.sum()), e, j))
    return out, mu


def rand_dnf(n, w, terms, rng, monotone=False):
    idx = np.arange(1 << n)
    val = np.zeros(idx.size, dtype=bool)
    tl = []
    for _ in range(terms):
        k = int(rng.integers(1, w + 1))
        vs = rng.choice(n, size=k, replace=False)
        sg = np.ones(k, dtype=int) if monotone else rng.integers(0, 2, size=k)
        sat = np.ones(idx.size, dtype=bool)
        for v, s in zip(vs, sg):
            sat &= ((idx >> int(v)) & 1) == int(s)
        val |= sat
        tl.append([int(v) for v in vs])
    return np.where(val, -1.0, 1.0), tl


def check(f, n, terms=None, w=None):
    st, mu = steps(f, n)
    var = 1.0 - mu[0]
    if var < 1e-12:
        return None
    worst_a = 0.0
    for inf, e, j in st:
        if inf > 1e-15:
            worst_a = max(worst_a, (e + j) / (inf * (C0 + np.log2(1 + var / inf))))
    res = {"A": worst_a}
    tot_i = sum(s[0] for s in st)
    h = ent(mu)
    res["HI"] = h / tot_i
    if terms is not None:
        q0 = float((f > 0).mean())                  # P[f = 0] (false)
        worst_b = np.inf
        for t in terms:
            k = len(t)
            worst_b = min(worst_b, max(st[v][0] for v in t) / (2 * q0 / (2 ** k - 1)))
        res["B"] = worst_b                           # must be >= 1
        res["C"] = h / ((w + 7.94) * tot_i)          # must be <= 1
    return res


def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    rng = np.random.default_rng(seed)
    wa = 0.0
    for n in (4, 6, 8, 10):
        for _ in range(40):
            p = rng.choice([0.5, 0.2, 0.05, 0.01])
            f = np.where(rng.random(1 << n) < p, -1.0, 1.0)
            r = check(f, n)
            if r:
                wa = max(wa, r["A"])
    print(f"random functions (4 biases, n = 4..10, 160 functions): max of (E+J)/bound = {wa:.4f}  (must be <= 1)")
    for mono in (False, True):
        wa, wb, wc, whi, cnt = 0.0, np.inf, 0.0, 0.0, 0
        for n in (6, 8, 10, 12):
            for w in (1, 2, 3, 4):
                for terms in (1, 2, 4, 8, 16, 40):
                    for _ in range(4):
                        f, tl = rand_dnf(n, w, terms, rng, monotone=mono)
                        r = check(f, n, tl, w)
                        if r:
                            cnt += 1
                            wa, wb, wc = max(wa, r["A"]), min(wb, r["B"]), max(wc, r["C"])
                            whi = max(whi, r["HI"])
        print(f"random DNFs monotone={mono} ({cnt} nonconstant): max (E+J)/bound = {wa:.4f}; "
              f"min over terms of maxInf/(2q/(2^k-1)) = {wb:.4f} (must be >= 1); "
              f"max H/((w+7.94) I) = {wc:.4f}; max H/I = {whi:.4f}", flush=True)


if __name__ == "__main__":
    main()
