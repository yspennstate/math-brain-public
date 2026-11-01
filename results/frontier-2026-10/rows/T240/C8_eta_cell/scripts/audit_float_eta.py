"""Float sanity audit of the eta-cell chain (not part of the proof): Radau trajectories at the cell's two ends and
its centre, measured in the certified frames against xhat + (eta - eta0) y, as a fraction of the certified r_k.
Usage: python audit_float_eta.py DIR q1 q2 ..."""
import sys, json
sys.path[:0] = ['scripts', '.']
import numpy as np
from scipy.integrate import solve_ivp
import entry_eta as E, entry

d = sys.argv[1]; names = sys.argv[2:]
E.setup('1/2', '1/5000')
tq, nodes, slopes, ys, yslopes = E.build('1600', '0.004')
recs = {}
for n in names:
    for r in map(json.loads, open('%s/%s.jsonl' % (d, n))):
        if 'k' in r: recs[r['k']] = r
K = len(tq) - 1
assert sorted(recs) == list(range(K)), 'pieces do not cover 0..K-1'
frames = [np.array([[float(v) for v in row] for row in entry.frame(entry.jac_f(entry.fl(nodes[k])))[1]]) for k in range(K + 1)]
for eta in (0.4998, 0.5, 0.5002):
    sol = solve_ivp(lambda t, x: E.fe(x, eta), (0, 1600), [1.0, 0, 0], method='Radau', rtol=1e-12, atol=1e-14,
                    dense_output=True)
    worst = 0; kw = 0
    for k in range(K):
        t1 = float(tq[k + 1])
        ref = entry.fl(nodes[k + 1]) + (eta - 0.5) * entry.fl(ys[k + 1])
        ratio = np.linalg.norm(frames[k + 1] @ (sol.sol(t1) - ref)) / recs[k]['r']
        if ratio > worst: worst, kw = ratio, k
    print('eta %.4f: max |z_true| / r_certified = %.3e at node %d (must be < 1)' % (eta, worst, kw + 1))
