"""an agent: NUMERICAL face-by-face minimum of T on the STRAT16 2+5 closure. For every edge set E on 5 vertices
with 4..7 edges, force A_ij = 0 off E (equality constraints) and minimise T = T*/M^2 by SLSQP from several starts.
Reuses Tval/unpack from my_min_search.py (written from RESULT.md (1)). Usage: python3 my_min_faces.py K STARTS SEED"""
import sys, itertools
import numpy as np
from scipy.optimize import minimize
sys.argv, args = sys.argv[:1] + ['1', '0'], sys.argv[1:]
import my_min_search as m
k = float(args[0]); S = int(args[1]); rng = np.random.default_rng(int(args[2]))
pairs = list(zip(*m.iu)); res = []
for ne in range(4, 8):
    for E in itertools.combinations(range(10), ne):
        off = [p for p in range(10) if p not in E]
        best = np.inf; bx = None
        for s in range(S):
            x0 = np.concatenate([rng.standard_normal(5), 0.4 * rng.standard_normal(6)])
            r = minimize(m.Tval, x0, args=(k,), method='SLSQP', constraints=[
                {'type': 'ineq', 'fun': m.cons}, {'type': 'ineq', 'fun': m.cons_diag},
                {'type': 'eq', 'fun': lambda x, off=off: m.unpack(x)[1][m.iu][off]}], options={'maxiter': 300, 'ftol': 1e-12})
            u, A = m.unpack(r.x)
            if r.success and A[m.iu].min() > -1e-7 and np.abs(A[m.iu][off]).max() < 1e-7 and r.fun < best:
                best = r.fun; bx = r.x.copy()
        res.append((best, E, bx))
res.sort(key=lambda r: r[0])
feas = [r for r in res if np.isfinite(r[0])]
print('k=%g faces=%d feasible=%d' % (k, len(res), len(feas)))
for b, E, bx in feas[:8]:
    print('  T=%.6g  edges=%s' % (b, [pairs[p] for p in E]))
    u, A = m.unpack(bx); C = np.eye(5) - A
    w = {(int(a), int(b2)): round(float(A[a, b2]), 4) for a, b2 in pairs if A[a, b2] > 1e-5}
    print('     weights', w, ' diagC', np.round(np.diag(C), 3), ' eigC', np.round(np.linalg.eigvalsh(C), 3), ' u', np.round(u, 3))
