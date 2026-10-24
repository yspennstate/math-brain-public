"""Adversarial search over degree-2 PTFs for the per-coordinate localisation quantity of Lemma B,
    Qmax(f) = max_i E_nu ln(N_i / (|T cap U_i| + 1)),  order = influence order,
and for the average localisation constant beta_avg of Lemma A (noise on all predecessors).
For threshold functions Qmax <= L1 = 4.151 is proved (observed <= 0.97).  Usage:
python anneal_q.py N SEED ITERS
"""
import sys, time
import numpy as np
from fei_lib import *

setup_process()


def main(n, seed, iters):
    rng = np.random.default_rng(seed)
    X = coords(n)
    iu = np.triu_indices(n, 1)
    P2 = X[:, iu[0]] * X[:, iu[1]]
    m = iu[0].size

    def score(a, b, th):
        f = sgn(P2 @ a + X @ b - th)
        c = wht(f)
        H, I = HI(c, n)
        if I < 0.05:
            return -1.0, None
        infl = influences(c, n)
        order = list(np.argsort(-infl, kind="stable"))
        Q = lemma3_Q(c, n, order)
        return float(np.nanmax(Q)), (H / I, I)

    a = rng.standard_normal(m) * 1.4 ** (-rng.permutation(m))
    b = rng.standard_normal(n) * 0.5
    th = 0.0
    cur, info = score(a, b, th)
    best, binfo, bp = cur, info, (a.copy(), b.copy(), th)
    log = open("../logs/anneal_q_n%d_s%d.log" % (n, seed), "w")
    for it in range(iters):
        T = 0.08 * (1 - it / iters) + 1e-4
        a2, b2, th2 = a.copy(), b.copy(), th
        mv = rng.integers(0, 4)
        scale = np.abs(a).max() + np.abs(b).max()
        if mv == 0:
            j = rng.integers(0, m); a2[j] = rng.standard_normal() * scale * rng.uniform(0.01, 1.5)
        elif mv == 1:
            j = rng.integers(0, n); b2[j] = rng.standard_normal() * scale * rng.uniform(0.01, 1.5)
        elif mv == 2:
            th2 = th + rng.normal(0, 0.3) * (np.abs(a).sum() + np.abs(b).sum()) / np.sqrt(m)
        else:
            j = rng.integers(0, m); a2[j] = 0.0
        s2, i2 = score(a2, b2, th2)
        if s2 >= cur or rng.random() < np.exp((s2 - cur) / T):
            a, b, th, cur, info = a2, b2, th2, s2, i2
            if cur > best:
                best, binfo, bp = cur, info, (a.copy(), b.copy(), th)
        if it % 100 == 0:
            print("it=%d cur=%.4f best=%.4f  (H/I, I) of best = %s" % (it, cur, best, binfo), file=log, flush=True)
    np.savez("../logs/anneal_q_n%d_s%d.npz" % (n, seed), a=bp[0], b=bp[1], th=bp[2])
    print("FINAL n=%d seed=%d best Qmax=%.5f (H/I, I)=%s   [L1 = %.4f]" % (n, seed, best, binfo, L1), file=log, flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
