"""E0066: sweep of periodic-orbit feasibility over random base vectors y (uses qbo_periodic_lp.py).

For m = 3: every cyclic order of the permutation vectors of y, periods 2..6, interior and boundary y.
For m = 4: all 23 two-cycles and sampled 3- and 4-cycles.
Records, per (m, kind, period): how many (y, cyclic order) pairs are realisable by some QBO, and how many by a
QBO that is not a coordinate permutation operator.
"""
import numpy as np, itertools, time
import qbo_periodic_lp as L

rng = np.random.default_rng(11)


def run(m, y, periods, max_cycles):
    base = L.polytope_constraints(m)
    pv = L.perm_vectors(y)
    n = len(pv)
    out = {}
    for p in periods:
        if p > n:
            continue
        others = list(range(1, n))
        import math
        total = math.perm(len(others), p - 1)
        if total <= max_cycles:
            seqs = itertools.permutations(others, p - 1)
        else:
            seqs = [tuple(rng.permutation(others)[:p - 1]) for _ in range(max_cycles)]
        tried = feas = nonperm = 0
        for rest in seqs:
            cycle = [pv[0]] + [pv[i] for i in rest]
            tried += 1
            P = L.feasible(m, cycle, base)
            if P is None:
                continue
            err, mf = L.verify(P, cycle, n_maj=100)
            if err > 1e-6 or mf > 0:
                print('   !! LP solution failed direct check', m, p, err, mf)
                continue
            feas += 1
            if not L.is_permutation_operator(P):
                nonperm += 1
        out[p] = (tried, feas, nonperm)
    return out


def rand_y(m, boundary=False):
    while True:
        y = rng.random(m)
        if boundary:
            y[-1] = 0.0
        y = y / y.sum()
        y = np.sort(y)[::-1]
        d = np.diff(y)
        if np.all(np.abs(d[:m - 1 - (1 if boundary else 0)]) > 0.03) and (boundary or y.min() > 0.03):
            return y


if __name__ == '__main__':
    t0 = time.time()
    tot = {}
    for m, kinds in ((3, ('interior', 'boundary')), (4, ('interior', 'boundary'))):
        for kind in kinds:
            n_y = 12 if m == 3 else 5
            periods = range(2, 7) if m == 3 else (2, 3, 4)
            maxc = 10 ** 6 if m == 3 else 60
            for r in range(n_y):
                y = rand_y(m, boundary=(kind == 'boundary'))
                res = run(m, y, periods, maxc)
                for p, (tried, feas, nonperm) in res.items():
                    key = (m, kind, p)
                    a = tot.setdefault(key, [0, 0, 0, 0])
                    a[0] += 1; a[1] += tried; a[2] += feas; a[3] += nonperm
                print('m=%d %s y=%s ->' % (m, kind, np.round(y, 3)), {p: v for p, v in res.items()}, '%.0fs' % (time.time() - t0), flush=True)
    print('=== totals: (m, kind, period): [#y, cyclic orders tried, realisable by a QBO, realisable by a NON-permutation QBO]')
    for k in sorted(tot):
        print(k, tot[k])
