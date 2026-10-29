import sys, json
sys.path[:0] = ['scripts', '.']
import numpy as np
from scipy.integrate import solve_ivp
import entry
tq, nodes, slopes = entry.build(1, 1600, 0.004)
heads = {}
recs = {}
for n in ['p1', 'p2', 'p3b', 'p4', 'p5', 'p6']:
    rows = [json.loads(l) for l in open('run2/%s.jsonl' % n)]
    heads[n] = rows[0]
    for r in rows:
        if 'k' in r: recs[r['k']] = r
names = ['p1', 'p2', 'p3b', 'p4', 'p5', 'p6']
for a, b in zip(names, names[1:]):
    assert heads[a]['t1'] == heads[b]['t0'] and heads[a]['nseg_total'] == heads[b]['nseg_total'] == len(tq) - 1, (a, b)
print('junction times and segment counts agree across pieces; K =', len(tq) - 1)
# independent truth: Radau at tight tolerance (different method from the DOP853 reference)
sol = solve_ivp(entry.ff, (0, 1600), [1.0, 0, 0], method='Radau', rtol=1e-12, atol=1e-14, dense_output=True)
worst = 0; worstd = 0
for k in range(0, len(tq) - 1):
    t1 = float(tq[k + 1])
    Pn, Pinvn = entry.frame(entry.jac_f(entry.fl(nodes[k + 1])))
    z = np.array([[float(v) for v in row] for row in Pinvn]) @ (sol.sol(t1) - entry.fl(nodes[k + 1]))
    ratio = np.linalg.norm(z) / recs[k]['r']
    worst = max(worst, ratio)
    # float defect at the midpoint against the certified d_k
    h = float(tq[k + 1] - tq[k]); s = 0.5
    x0, x1, m0, m1 = [entry.fl(v) for v in (nodes[k], nodes[k + 1], slopes[k], slopes[k + 1])]
    xm = (2*s**3-3*s**2+1)*x0 + (s**3-2*s**2+s)*h*m0 + (-2*s**3+3*s**2)*x1 + (s**3-s**2)*h*m1
    vm = ((6*s**2-6*s)*x0 + (3*s**2-4*s+1)*h*m0 + (-6*s**2+6*s)*x1 + (3*s**2-2*s)*h*m1) / h
    P, Pinv = entry.frame(entry.jac_f(entry.fl(nodes[k])))
    dm = np.linalg.norm(np.array([[float(v) for v in row] for row in Pinv]) @ (vm - entry.ff(0, xm)))
    worstd = max(worstd, dm / recs[k]['d'])
print('max |z_true| / r_certified over all 1069 nodes: %.3e (must be < 1)' % worst)
print('max float midpoint defect / d_certified: %.3e (must be < 1)' % worstd)
