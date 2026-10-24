# Independent check of the best laws found by p2_adversary.py: rebuild each law from its saved frame and
# gaps, locate the maximiser of the curved marginal on a finer grid (G = 1024), and re-estimate the density at
# that point by Monte Carlo (8e6 samples, windows 0.02 and 0.01) - a different computation path from the FFT.
import json, sys, math
import numpy as np
from p2_adversary import Evaluator, pos_from_gaps

def check(rec, n=8_000_000, seed=5):
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
    rng = np.random.default_rng(seed)
    X = np.empty((n, m))
    for i in range(m):
        k = rng.integers(0, N, size=n)
        X[:, i] = pos[i][k] + rng.uniform(0, 1.0/N, size=n)
    Y = X @ D[0] + c*(X @ D[1] - b)**2
    mc = [np.mean(np.abs(Y - s_star) < h)/(2*h) for h in (0.02, 0.01)]
    return dict(m=m, F_saved=rec['F'], F_fine=float(acc.max()), mc=mc, s=float(s_star), c=c, b=b,
                pair_bound=rec['pair_bound'], lines=rec['lines'], rhoU=rec['rhoU'])

if __name__ == "__main__":
    with open(sys.argv[1], encoding='utf-8') as f:
        recs = [json.loads(l) for l in f if l.strip()]
    for r in recs:
        print(json.dumps(check(r)), flush=True)
