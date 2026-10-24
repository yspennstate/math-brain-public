"""Restriction drop Delta_w and rho_0 = min_w Delta_w/Inf_w along a balanced monotone self-composition tower.

For G_k = g(G_{k-1},...,G_{k-1}) with g balanced and monotone, a leaf w in outer block j, c = Inf_w(G_{k-1})
(= level-1 coefficient of G_{k-1} at w), restricting w makes input j of the outer g biased with mean +-c, and
  Delta_w(G_k) = Inf_j(g) Delta_w(G_{k-1}) + Inf_j(g) h2(c^2) + H(g) - (Ht_g(j,+c) + Ht_g(j,-c))/2,
where Ht_g(j, mu) is the spectral entropy of g in the product basis with input j of mean mu (others uniform).
(Derivation in the report: composition identity with one biased input; the It_l, l != j, average back to
Inf_l(g) over the two signs.)  Checked by brute force on a small g at k = 2, then run on Numaro's g."""
import sys, os, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from feilib import *

set_polite()


def biased_one_entropy(gh, n, j, mu):
    """Ht of g with input j biased to mean mu: coefficients Ghat(U)+mu Ghat(U+j) (j not in U), sqrt(1-mu^2)Ghat(U) (j in U)."""
    S = np.arange(1 << n)
    lo = S[((S >> j) & 1) == 0]; hi = lo | (1 << j)
    a = gh[lo] + mu * gh[hi]
    b = np.sqrt(1 - mu * mu) * gh[hi]
    return float(phi(a * a).sum() + phi(b * b).sum())


def tower(gtt, n, K, verbose=True):
    gh = wht(gtt[None, :].astype(np.float64))[0]
    p = gh ** 2
    cq = coord_quantities(gh[None, :], n)
    Inf = cq["Inf"][0]; Dg = cq["Delta"][0]
    Hg = float(entropy(p))
    lvl1 = np.array([gh[1 << j] for j in range(n)])
    assert abs(gh[0]) < 1e-12 and np.allclose(np.abs(lvl1), Inf)
    # classes of coordinates by |level-1 coefficient| (so P depends on counts per class)
    vals = sorted(set(np.round(Inf, 14)))
    cls = [vals.index(round(x, 14)) for x in Inf]
    best = {}
    for j in range(n):
        key = tuple(1 if c == cls[j] else 0 for c in range(len(vals)))
        best[key] = min(best.get(key, np.inf), Dg[j] / Inf[j])
    cache = {}
    out = [min(best.values())]
    if verbose:
        print(json.dumps(dict(k=1, rho0=out[-1])))
    for depth in range(2, K + 1):
        nb = {}
        for key, r in best.items():
            P = float(np.prod([vals[c] ** key[c] for c in range(len(vals))]))
            for j in range(n):
                ck = (j, key)
                if ck not in cache:
                    ht = 0.5 * (biased_one_entropy(gh, n, j, P) + biased_one_entropy(gh, n, j, -P))
                    cache[ck] = (Inf[j] * float(h2(P * P)) + Hg - ht) / (Inf[j] * P)
                nk = tuple(key[c] + (1 if c == cls[j] else 0) for c in range(len(vals)))
                nb[nk] = min(nb.get(nk, np.inf), r + cache[ck])
        best = nb
        out.append(min(best.values()))
        if verbose:
            print(json.dumps(dict(k=depth, rho0=out[-1]))); sys.stdout.flush()
    return out


if __name__ == "__main__":
    from check_composition import compose
    # brute-force check on the small balanced monotone g of check_tower_small.py
    gs = np.array([1, 1, 1, -1, 1, 1, -1, -1, 1, -1, 1, -1, 1, -1, -1, -1], dtype=np.int8)
    pred = tower(gs, 4, 2, verbose=False)
    tt2, n2, offs, sizes = compose(gs, 4, [(gs, 4)] * 4)
    c2 = coord_quantities(wht(tt2[None, :].astype(float)), n2)
    brute = float((c2["Delta"][0] / c2["Inf"][0]).min())
    print("small g check, k=2: recursion rho0 =", pred[-1], " brute force rho0 =", brute)
    g = np.load(os.path.join(HERE, "..", "..", "inputs", "numaro18_pm1_table.npy"))
    res = tower(g, 18, 7)
    json.dump(res, open(os.path.join(HERE, "..", "logs", "tower_rho0.json"), "w"))
