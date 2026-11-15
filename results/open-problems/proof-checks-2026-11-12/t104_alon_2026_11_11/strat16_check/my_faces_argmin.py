"""an agent: print the argmin structure on the faces where T ~ 0 (k=5). Usage: python3 my_faces_argmin.py SEED"""
import sys, itertools
import numpy as np
from scipy.optimize import minimize
seed = int(sys.argv[1]); sys.argv = sys.argv[:1] + ['1', '0']
import my_min_search as m
rng = np.random.default_rng(seed); k = 5.0
faces = [(2,3,4,5,7,8,9), (3,4,5,7,9), (0,3,4,7,8,9), (0,4,5,6,9), (6,7,8,9), (1,2,3,5,6,7)]
pairs = list(zip(*m.iu))
for E in faces:
    off = [p for p in range(10) if p not in E]; best = (np.inf, None)
    for s in range(6):
        x0 = np.concatenate([rng.standard_normal(5), 0.4 * rng.standard_normal(6)])
        r = minimize(m.Tval, x0, args=(k,), method='SLSQP', constraints=[
            {'type': 'ineq', 'fun': m.cons}, {'type': 'ineq', 'fun': m.cons_diag},
            {'type': 'eq', 'fun': lambda x, off=off: m.unpack(x)[1][m.iu][off]}], options={'maxiter': 300, 'ftol': 1e-12})
        if r.success and r.fun < best[0]: best = (r.fun, r.x)
    u, A = m.unpack(best[1]); C = np.eye(5) - A
    w = {(int(a), int(b)): round(float(A[a, b]), 4) for a, b in pairs if A[a, b] > 1e-5}
    print('face', [(int(a), int(b)) for a, b in (pairs[p] for p in E)], ' T=%.2e' % best[0])
    print('   positive weights', w, ' diagC', np.round(np.diag(C), 4), ' eig C', np.round(np.linalg.eigvalsh(C), 4), ' u', np.round(u, 4))
