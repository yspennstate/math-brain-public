"""Independent finite matrix and group checks of the q-fold cycle formulas."""
import json
import math
from collections import deque
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def run():
    rows = []
    for m in (5, 6, 7, 8, 9, 11, 15, 21):
        for q in (1, 2, 3, 5):
            n = m*q
            p = np.zeros((n, n))
            for i in range(m):
                for a in range(q):
                    for j in ((i-1)%m, (i+1)%m):
                        p[i*q+a, j*q:(j+1)*q] = 1/(2*q)
            actual = np.r_[0., np.linalg.solve(np.eye(n-1)-p[1:, 1:], np.ones(n-1))]
            expected = np.array([0 if v == 0 else (m*q if v//q == 0 else
                                (v//q)*(m-v//q)+m*(q-1)) for v in range(n)])
            hit_error = float(np.max(np.abs(actual-expected)))
            eig_expected = sorted([math.cos(2*math.pi*k/m) for k in range(m)]+[0.]*(m*(q-1)))
            eigen_error = float(np.max(np.abs(np.linalg.eigvalsh(p)-eig_expected)))
            tau0 = (m*m-1)/6 + m*(q-1)
            tau_star = 2*(m*m//4)+2*m*(q-1)
            assert hit_error < 1e-8
            assert eigen_error < 1e-12
            assert abs(float(actual.mean())-tau0) < 1e-8
            assert abs(2*float(actual.max())-tau_star) < 1e-8
            assert abs(float(actual[q])-(n-1)) < 1e-8
            assert np.all(np.count_nonzero(p, axis=1) == 2*q)
            orbit_size = None
            if m in (5, 7, 9) and q in (2, 3, 5):
                perms = [lambda v: ((v//q+1)%m)*q+v%q,
                         lambda v: ((-v//q)%m)*q+v%q]
                # Correct reflection uses -(fiber index), not integer division of -v.
                perms[1] = lambda v: (-(v//q)%m)*q+v%q
                perms.append(lambda v: ((v%q+1)%q if v//q == 0 else v))
                perms.append(lambda v: (1-v if v//q == 0 and v%q in (0,1) else v))
                seen = {(0, q)}
                queue = deque(seen)
                while queue:
                    u, v = queue.popleft()
                    for perm in perms:
                        edge = (perm(u), perm(v))
                        assert p[edge] > 0
                        if edge not in seen:
                            seen.add(edge)
                            queue.append(edge)
                orbit_size = len(seen)
                assert orbit_size == n*2*q
            rows.append(dict(m=m, q=q, n=n, max_hitting_error=hit_error,
                             max_spectrum_error=eigen_error, directed_edge_orbit=orbit_size,
                             tau_star=tau_star, tau0=tau0))
    summary = dict(cases=len(rows), q2_baseline_cases=sum(r['q']==2 for r in rows),
                   new_q3_q5_cases=sum(r['q'] in (3,5) for r in rows),
                   orbit_checks=sum(r['directed_edge_orbit'] is not None for r in rows),
                   max_hitting_error=max(r['max_hitting_error'] for r in rows),
                   max_spectrum_error=max(r['max_spectrum_error'] for r in rows), rows=rows)
    out = ROOT/'measurements'
    out.mkdir(exist_ok=True)
    (out/'P0208.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
    print(json.dumps({k:v for k,v in summary.items() if k!='rows'}))
    return summary

if __name__ == '__main__':
    run()
