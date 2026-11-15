"""Audit the single-slice subset conditions against majorisation objectives."""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
             'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[name] = '1'
import itertools
import json
from pathlib import Path
import numpy as np
from scipy.optimize import linprog


def system(m):
    pairs = list(itertools.combinations_with_replacement(range(m), 2))
    n = len(pairs) * m
    eq, rhs, ub, bound = [], [], [], []
    for e in range(len(pairs)):
        row = np.zeros(n)
        row[e*m:(e+1)*m] = 1
        eq.append(row); rhs.append(1)
    for k in range(m):
        row = np.zeros(n)
        for e, (i, j) in enumerate(pairs):
            row[e*m+k] = 1 if i == j else 2
        eq.append(row); rhs.append(m)
        for mask in range(1, (1 << m)-1):
            row = np.zeros(n)
            for e, (i, j) in enumerate(pairs):
                if (mask >> i) & (mask >> j) & 1:
                    row[e*m+k] = 1 if i == j else 2
            ub.append(row); bound.append(mask.bit_count())
    return pairs, np.array(eq), np.array(rhs), np.array(ub), np.array(bound)


if __name__ == '__main__':
    rng = np.random.default_rng(6601)
    results = []
    for m in range(3, 7):
        pairs, eq, rhs, ub, bound = system(m)
        best = -1.0
        for t in range(100):
            x = np.sort(rng.dirichlet(np.ones(m)))[::-1]
            r = 1 + (t % (m-1))
            objective = np.zeros(len(pairs)*m)
            for e, (i, j) in enumerate(pairs):
                objective[e*m:e*m+r] = x[i]*x[j]*(1 if i == j else 2)
            res = linprog(-objective, A_ub=ub, b_ub=bound,
                          A_eq=eq, b_eq=rhs, bounds=(0, 1),
                          method='highs', options={'threads': 1})
            assert res.success, res.message
            gap = -res.fun - x[:r].sum()
            best = max(best, gap)
            if gap > 1e-8:
                results.append(dict(m=m, trial=t, r=r, x=x.tolist(), gap=gap,
                                    p=res.x.reshape(-1,m).tolist()))
                break
        print(m, best, flush=True)
    Path('data/subset_condition_probe.json').write_text(json.dumps(results, indent=2)+'\n')
