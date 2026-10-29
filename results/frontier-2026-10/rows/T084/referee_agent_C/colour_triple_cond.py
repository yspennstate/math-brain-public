"""Statement S summed at weights lam, q (X, Y independent random-cluster configurations, weight lam^|.| q^k(.)):
good - bad = Z^2 mu(A) mu(B) (mu(v~w | B) - mu(v~w | A)), A = {u !~ v, u !~ w}, B = {u ~ v}. Checked numerically.
python colour_triple_cond.py V m seed cnt"""
import sys, random
from e1_swap import comps

V, m, seed, cnt = map(int, sys.argv[1:5])
rnd = random.Random(seed)
worst = 0.0
neg_q_ge_1 = 0
tested = 0
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    cfg = []
    for mask in range(1 << m):
        k, fd = comps(V, [H[j] for j in range(m) if mask >> j & 1])
        cfg.append((bin(mask).count('1'), k, [fd(x) for x in range(V)]))
    for lam, q in ((1.0, 0.5), (0.7, 0.2), (2.0, 0.9), (1.0, 2.0), (0.5, 3.0)):
        for u, v, w in ((0, 1, 2), (1, 2, 3), (2, 0, 3)):
            wt = [lam ** s * q ** k for s, k, _ in cfg]
            Z = sum(wt)
            A = [i for i, c in enumerate(cfg) if c[2][u] not in (c[2][v], c[2][w])]
            B = [i for i, c in enumerate(cfg) if c[2][u] == c[2][v]]
            vw = lambda i: cfg[i][2][v] == cfg[i][2][w]
            mA, mB = sum(wt[i] for i in A), sum(wt[i] for i in B)
            good = sum(wt[i] for i in A if not vw(i)) * sum(wt[i] for i in B if vw(i))
            bad = sum(wt[i] for i in A if vw(i)) * sum(wt[i] for i in B if not vw(i))
            if mA == 0 or mB == 0:
                continue
            rhs = mA * mB * (sum(wt[i] for i in B if vw(i)) / mB - sum(wt[i] for i in A if vw(i)) / mA)
            worst = max(worst, abs((good - bad) - rhs) / (mA * mB))
            tested += 1
            if q >= 1 and good - bad < -1e-9 * Z * Z:
                neg_q_ge_1 += 1
print('V %d m %d seed %d: %d evaluations, max identity error over mu(A) mu(B) %.2e, negative cases with q >= 1: %d'
      % (V, m, seed, tested, worst, neg_q_ge_1))
