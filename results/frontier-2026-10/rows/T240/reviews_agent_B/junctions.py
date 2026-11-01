# agent B review of T240 C8: rebuild the reference here and recompute the segments either side of every piece
# junction (and the first, and the trap row), comparing d, mu, R, r with the lead's logs.
import sys, json
sys.path[:0] = ['scripts', '.']
from fractions import Fraction as F
import entry_eta as E, entry
E.setup('1/2', '1/5000')
tq, nodes, slopes, ys, yslopes = E.build('1600', '0.004')
print('nodes', len(tq) - 1, flush=True)
logs = {}
for n in ['q1', 'q2', 'q3', 'q4', 'q5', 'q6b', 'q6c', 'q6d']:
    rows = [json.loads(l) for l in open('logs/%s.jsonl' % n)]
    logs[n] = rows
    for k in sorted({rows[1]['k'], [r for r in rows if 'k' in r][-1]['k']}):
        row = [r for r in rows if r.get('k') == k][0]
        # the radius entering segment k: r_in for the first row, else the previous row's r (a float; recompute with it)
        prev = [r for r in rows if r.get('k') == k - 1]
        r0 = F(rows[0]['r_in']) if not prev else F(prev[0]['r'])
        P, Pinv = entry.frame(entry.jac_f(entry.fl(nodes[k])))
        res = E.segment(nodes[k], nodes[k + 1], slopes[k], slopes[k + 1], ys[k], ys[k + 1], yslopes[k], yslopes[k + 1],
                        tq[k + 1] - tq[k], P, Pinv, r0, 6)
        same = (abs(float(tq[k]) - row['t']) == 0, float(res['d']) == row['d'], float(res['mu']) == row['mu'], float(res['R']) == row['R'])
        print(n, k, 't,d,mu,R identical:', same, ' d %.6e vs %.6e' % (float(res['d']), row['d']), flush=True)
