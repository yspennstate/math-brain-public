"""Reproduce the GU evidence values for the author's annealed 5-bit function g5 and its compositions.
G(f) = sum_i Delta_i U(f), Delta_i U by direct physical restriction.  Composition f = outer(g5(x^1),...,g5(x^k)) on
disjoint blocks, built by brute force (my own builder)."""
import json, math
import numpy as np
from rlib import Spec, walsh, restrict_tables

g5 = np.array([-1, -1, -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, 1, 1, 1, 1, 1, 1, -1], dtype=np.int64)


def G_stats(f):
    f = np.asarray(f, dtype=np.int64)
    sp = Spec.from_tables(f); n = sp.n
    U = float(sp.U()[0]); H = float(sp.H()[0]); inf = sp.infl()[0]; I = float(inf.sum())
    loc = []
    G = 0.0
    for i in range(n):
        if inf[i] < 1e-15:
            continue
        a = Spec.from_tables(restrict_tables(f, i, 1)); b = Spec.from_tables(restrict_tables(f, i, -1))
        d = U - 0.5 * float(a.U()[0] + b.U()[0])
        G += d; loc.append(d / inf[i])
    return dict(n=n, G_over_I=G / I, U_over_I=U / I, H_over_I=H / I, min_local=min(loc), max_local=max(loc), I=I)


def compose(outer, k, inner, m):
    """f(x^1..x^k) = outer(inner(x^1),...,inner(x^k)); outer indexed with bit j = 1 iff inner(x^j) = -1."""
    n = k * m; N = 1 << n; xs = np.arange(N, dtype=np.int64)
    idx = np.zeros(N, dtype=np.int64)
    for j in range(k):
        blk = (xs >> (j * m)) & ((1 << m) - 1)
        idx |= ((inner[blk] == -1).astype(np.int64) << j)
    return outer[idx]


if __name__ == '__main__':
    maj3 = np.array([1 if bin(x).count('1') < 2 else -1 for x in range(8)], dtype=np.int64)
    and2 = np.array([1, 1, 1, -1], dtype=np.int64)       # -1 iff both inputs are -1
    or3 = np.array([1] + [-1] * 7, dtype=np.int64)
    out = {}
    W = walsh(g5)
    out['g5_walsh_values_over_32'] = sorted(set(int(w) for w in W))
    out['g5'] = G_stats(g5)
    out['maj3 o g5'] = G_stats(compose(maj3, 3, g5, 5))
    out['and2 o g5'] = G_stats(compose(and2, 2, g5, 5))
    out['or3 o g5'] = G_stats(compose(or3, 3, g5, 5))
    print(json.dumps(out, indent=1))
    with open('gu_values_results.json', 'w', encoding='utf-8') as fh:
        json.dump(out, fh, indent=1)
