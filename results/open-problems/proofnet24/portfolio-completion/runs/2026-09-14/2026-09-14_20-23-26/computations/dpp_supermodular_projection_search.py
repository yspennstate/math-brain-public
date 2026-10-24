"""Bounded exploratory LP search for a supermodular projection inequality.

This is not a direct test or proof of entropy concavity. All output is numeric.
The seed and full witness are retained if an inequality failure is found.
"""
import itertools
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog


def projection_probabilities(U):
    n, r = U.shape
    p = np.zeros(1 << n)
    for S in itertools.combinations(range(n), r):
        if not S:
            p[0] = 1.
        else:
            p[sum(1 << i for i in S)] = abs(np.linalg.det(U[list(S), :])) ** 2
    return p


def constraints(n):
    rows = []
    for i in range(n):
        for j in range(i + 1, n):
            for S in range(1 << n):
                if S & ((1 << i) | (1 << j)):
                    continue
                row = np.zeros(1 << n)
                row[S] = row[S | (1 << i) | (1 << j)] = -1
                row[S | (1 << i)] = row[S | (1 << j)] = 1
                rows.append(row)
    return np.array(rows)


def run(n=6, rank=2, trials=100, seed=14092026):
    rng = np.random.default_rng(seed)
    Aub = constraints(n)
    bounds = [(0, 0) if S == 0 or S & (S-1) == 0 else (0, 1)
              for S in range(1 << n)]
    best = None
    for trial in range(trials):
        G = rng.integers(-5, 6, (n, rank + 2))
        if np.linalg.matrix_rank(G) < rank + 2:
            continue
        U, _ = np.linalg.qr(G.astype(float))
        W = U[:, :rank]
        u, v = U[:, rank:rank+1], U[:, rank+1:rank+2]
        cost = (projection_probabilities(np.column_stack((W, u, v)))
                - projection_probabilities(np.column_stack((W, u)))
                - projection_probabilities(np.column_stack((W, v)))
                + projection_probabilities(W))
        result = linprog(cost, A_ub=Aub, b_ub=np.zeros(len(Aub)),
                         bounds=bounds, method='highs')
        if not result.success:
            raise RuntimeError(result.message)
        if best is None or result.fun < best['objective']:
            best = {'objective':float(result.fun), 'trial':trial,
                    'integer_basis_input':G.tolist(),
                    'orthonormal_basis':U.tolist(),
                    'f':result.x.tolist(), 'cost':cost.tolist(),
                    'max_constraint_violation':float(np.max(Aub@result.x))}
        if result.fun < -1e-8:
            break
    return {'dimension':n, 'base_rank':rank, 'seed':seed,
            'attempted_trials':trial+1, 'planned_trials':trials,
            'negative_numeric_witness_found':best['objective'] < -1e-8,
            'best':best,
            'interpretation':'Floating-point exploration of a sufficient supermodular lemma; no entropy counterexample or universal proof.'}


if __name__ == '__main__':
    out = run()
    Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k != 'best'}))
    print('best_objective',out['best']['objective'])
