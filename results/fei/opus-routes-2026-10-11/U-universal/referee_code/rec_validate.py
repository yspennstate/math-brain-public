"""Validate rec.py against brute force on compositions small enough to tabulate (n <= 15)."""
import json
import numpy as np
from rec import var, table, gate, root_stats, AND2, OR2, MAJ3, andk, ork
from gu_values import G_stats, g5, compose

rng = np.random.default_rng(77)
out = {}

# known cases
G5 = table(g5)
r = root_stats(gate(MAJ3, [G5, G5, G5], symmetric=True)); b = G_stats(compose(np.array(MAJ3), 3, g5, 5))
out['maj3_g5'] = dict(rec_G_over_I=r['G_over_I'], brute=b['G_over_I'], rec_H_over_I=r['H_over_I'], brute_H=b['H_over_I'], I_consistency=r['I'] - r['I_from_infl'])
r = root_stats(gate(AND2, [G5, G5], symmetric=True)); b = G_stats(compose(np.array(AND2), 2, g5, 5))
out['and2_g5'] = dict(rec_G_over_I=r['G_over_I'], brute=b['G_over_I'])


# random trees: brute force by building the truth table recursively
def build_random(depth):
    """returns (node, table_fn) where table_fn maps an assignment array (N, nvars) of +-1 to values."""
    if depth == 0 or rng.random() < 0.25:
        if rng.random() < 0.5:
            return var(), 1, (lambda X: X[:, 0])
        m = int(rng.integers(2, 4)); t = rng.choice([-1, 1], size=1 << m)
        while abs(t.sum()) == len(t):
            t = rng.choice([-1, 1], size=1 << m)
        def tf(X, t=t, m=m):
            idx = np.zeros(X.shape[0], dtype=np.int64)
            for i in range(m):
                idx |= ((X[:, i] == -1).astype(np.int64) << i)
            return t[idx]
        return table(t), m, tf
    k = int(rng.integers(2, 4)); g = rng.choice([-1, 1], size=1 << k)
    kids = [build_random(depth - 1) for _ in range(k)]
    nv = sum(c[1] for c in kids)
    def tf(X, kids=kids, g=g, k=k):
        idx = np.zeros(X.shape[0], dtype=np.int64); off = 0
        for j, (nd, m, f) in enumerate(kids):
            v = f(X[:, off:off + m]); off += m
            idx |= ((v == -1).astype(np.int64) << j)
        return g[idx]
    return gate(g, [c[0] for c in kids]), nv, tf


errs = []
for trial in range(40):
    node, nv, tf = build_random(2)
    if nv > 13 or nv < 2:
        continue
    N = 1 << nv; xs = np.arange(N)
    X = np.stack([1 - 2 * ((xs >> i) & 1) for i in range(nv)], 1)
    t = tf(X).astype(np.int64)
    if abs(t.sum()) == N:
        continue
    r = root_stats(node); b = G_stats(t)
    errs.append(dict(nv=nv, dG=abs(r['G_over_I'] - b['G_over_I']), dH=abs(r['H_over_I'] - b['H_over_I']), dU=abs(r['U_over_I'] - b['U_over_I']), dminloc=abs(r['min_local_U'] - b['min_local'])))
out['random_trees'] = dict(count=len(errs), max_dG=max(e['dG'] for e in errs), max_dH=max(e['dH'] for e in errs), max_dU=max(e['dU'] for e in errs), max_dminloc=max(e['dminloc'] for e in errs))
print(json.dumps(out, indent=1))
with open('rec_validate_results.json', 'w', encoding='utf-8') as fh:
    json.dump(out, fh, indent=1)
