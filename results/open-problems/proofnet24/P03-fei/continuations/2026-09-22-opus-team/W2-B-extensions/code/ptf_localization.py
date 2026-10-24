"""Does the localisation property hold for degree-2 PTFs?  For the influence order (the order that
coincides with the weight order for threshold functions) and for every coordinate i with N >= 2
predecessors-plus-one, with P = all predecessors of i and eta in {0.25, 0.5, 1}:

  beta_pw  = max_x Pr[D_i f(y) != 0 | x] * sqrt(eta N)          (pointwise, what Theorem 1 uses)
  beta_avg = E[|D_i f(x)| Pr[D_i f(y) != 0 | x]] / Inf_i * sqrt(eta N)   (average, what Lemma A needs)
  Q_max    = max_i E_nu ln(N_i / (|T cap U_i| + 1))                 (what Lemma B bounds)

For threshold functions beta_pw <= 2/sqrt(pi) E-Erdos factor (<= 1.13 for large N).  We report the
maxima over the family, and the same numbers for random LTFs as a reference.
"""
import sys, time
import numpy as np
from fei_lib import *

setup_process()


def loc_stats(f, n):
    c = wht(f)
    H, I = HI(c, n)
    infl = influences(c, n)
    order = list(np.argsort(-infl, kind="stable"))
    Q = lemma3_Q(c, n, order)
    bpw, bavg = 0.0, 0.0
    worst_pw = None
    for pos, i in enumerate(order):
        if infl[i] < 1e-12 or pos == 0:
            continue
        N = pos + 1
        pred = [1 << int(u) for u in order[:pos]]
        for eta in (0.25, 0.5, 1.0):
            Pw, h = pointwise_exit(f, n, i, pred, eta)
            s = np.sqrt(eta * N)
            v = float(Pw.max()) * s
            if v > bpw:
                bpw, worst_pw = v, (int(i), N, eta, float(Pw.max()))
            bavg = max(bavg, float((h * Pw).sum() / h.sum()) * s)
    return dict(HI=H / I, Qmax=float(np.nanmax(Q)), bpw=bpw, bavg=bavg, worst=worst_pw)


def main():
    rng = np.random.default_rng(99)
    out = open("../logs/ptf_localization.log", "w")
    for n in (10, 12, 14):
        X = coords(n)
        iu = np.triu_indices(n, 1)
        P2 = X[:, iu[0]] * X[:, iu[1]]
        fams = []
        for rep in range(4):
            w = np.abs(rng.standard_normal(n)) * 1.4 ** (-rng.permutation(n)) * rng.choice([-1, 1], size=n)
            fams.append(("LTF", sgn(X @ w - rng.normal(0, 0.5) * np.sqrt((w ** 2).sum()))))
        for rep in range(4):
            a = rng.standard_normal(iu[0].size)
            b = rng.standard_normal(n) * rng.choice([0.0, 1.0, 3.0])
            th = rng.normal(0, 1) * np.sqrt((a ** 2).sum() + (b ** 2).sum())
            fams.append(("dense2", sgn(P2 @ a + X @ b - th)))
        for rep in range(4):
            a = rng.standard_normal(iu[0].size) * 1.5 ** (-rng.permutation(iu[0].size))
            b = rng.standard_normal(n) * 1.5 ** (-rng.permutation(n))
            fams.append(("geom2", sgn(P2 @ a + X @ b - rng.normal(0, 0.2))))
        for rep in range(4):
            # x_0 * (sum over a set K) + small linear form: the example where a subcube stays in D_0
            K = rng.choice(np.arange(1, n), size=n // 2, replace=False)
            J = [j for j in range(1, n) if j not in K]
            lin = np.zeros(n); lin[J] = rng.standard_normal(len(J))
            fams.append(("x0*sumK+L", sgn(X[:, 0] * X[:, K].sum(1) + X @ lin + 0.01)))
        # annealed Phi maximiser at n = 12 if present
        try:
            z = np.load("../logs/anneal_phi_n12_s11.npz")
            if n == 12:
                fams.append(("anneal-phi-best", sgn(P2 @ z["a"] + X @ z["b"] - float(z["th"]))))
        except Exception:
            pass
        for name, f in fams:
            if np.all(f == f[0]):
                continue
            t0 = time.time()
            r = loc_stats(f, n)
            print("n=%2d %-16s H/I=%.3f  Qmax=%.3f  beta_pw=%.3f  beta_avg=%.3f  worst(i,N,eta,P)=%s  (%.1fs)"
                  % (n, name, r["HI"], r["Qmax"], r["bpw"], r["bavg"], r["worst"], time.time() - t0), file=out, flush=True)
    out.close()


if __name__ == "__main__":
    main()
