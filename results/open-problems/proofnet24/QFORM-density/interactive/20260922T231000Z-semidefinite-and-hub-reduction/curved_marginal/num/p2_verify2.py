# Second check of the laws found by p2_adversary.py, for larger m.
# For each saved law: (1) rebuild the density of (U, V) on a finer grid (G = 1024, spacing 0.025), locate the
# maximiser of the curved marginal at the saved (c, b); (2) re-estimate the density there by Monte Carlo, in
# chunks (4e6 samples, windows 0.02 and 0.01); (3) compute the largest density of a linear form
# cos(t) U + sin(t) V over 360 directions t, integrating the grid density along the level lines (p2_lines.py),
# the full comparison the search itself made only on 9 slopes.
import json, sys, math
import numpy as np
from p2_adversary import Evaluator, pos_from_gaps
from p2_lines import line_max as line_max_interp

def mc_density(D, pos, N, c, b, s_star, n=4_000_000, chunk=500_000, seed=5):
    rng = np.random.default_rng(seed)
    m = D.shape[1]
    hits = {0.02: 0, 0.01: 0}
    done = 0
    while done < n:
        k = min(chunk, n - done)
        X = np.empty((k, m))
        for i in range(m):
            idx = rng.integers(0, N, size=k)
            X[:, i] = pos[i][idx] + rng.uniform(0, 1.0/N, size=k)
        Y = X @ D[0] + c*(X @ D[1] - b)**2
        for h in hits:
            hits[h] += int(np.sum(np.abs(Y - s_star) < h))
        done += k
    return [hits[h]/n/(2*h) for h in (0.02, 0.01)]

def check(rec):
    D = np.array(rec['frame']); gaps = np.array(rec['gaps']); N = rec['N']; m = D.shape[1]
    pos = pos_from_gaps(gaps, N)
    ev = Evaluator(D, N, 1024, 0.025, cs=[], nb=1)
    rho = ev.density(pos)
    d = ev.delta; G = ev.G
    ug = ev.x0u + d*np.arange(G); vg = ev.x0v + d*np.arange(G)
    c, b = rec['arg']
    acc = np.zeros(G)
    for j in range(G):
        acc += np.interp(ug - c*(vg[j]-b)**2, ug, rho[j], left=0, right=0)
    acc *= d
    s_star = ug[np.argmax(acc)]
    mc = mc_density(D, pos, N, c, b, s_star)
    line_max, line_dir = line_max_interp(rho, ev.x0u, d, ndir=360, x0v=ev.x0v)
    return dict(m=m, iters=rec['iters'], F_saved=rec['F'], F_fine=float(acc.max()), mc=mc, s=float(s_star),
                c=c, b=b, lines_saved=rec['lines'], line_max_360=line_max, line_dir=line_dir,
                ratio=float(acc.max())/line_max, pair_bound=rec['pair_bound'], mass=float(rho.sum()*d*d))

if __name__ == "__main__":
    try:
        import psutil
        psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
    except Exception:
        pass
    with open(sys.argv[1], encoding='utf-8') as f:
        recs = [json.loads(l) for l in f if l.strip()]
    for r in recs:
        print(json.dumps(check(r)), flush=True)
