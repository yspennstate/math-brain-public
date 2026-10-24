# Non-lazy SRW on the cycle plus a random matching: TV mixing time from vertex 0 vs 3 log_2 n
# (the Lubetzky-Sly / Lubetzky-Peres cutoff location for cubic graphs), plus the worst-case
# lower bound: every cubic graph has t_mix >= (3 log_2 n)(1-o(1)) (Lubetzky-Peres 2016).
import numpy as np, scipy.sparse as sp, time
rng = np.random.default_rng(7)
def cpm(n):
    while True:
        perm = rng.permutation(n)
        rows = list(range(n)) + [(j+1) % n for j in range(n)]; cols = rows[n:] + rows[:n]
        for k in range(0, n, 2):
            a, b = perm[k], perm[k+1]; rows += [a, b]; cols += [b, a]
        A = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n, n))
        if A.max() == 1: return A
for n in [1000, 4000, 16000, 64000, 256000]:
    A = cpm(n); P = (A/3.0).T.tocsr(); dist = np.zeros(n); dist[0] = 1; t = 0; tvs = []
    while True:
        tv = 0.5*np.abs(dist - 1/n).sum(); tvs.append(tv)
        if tv <= 0.25 and t > 0: break
        dist = P @ dist; t += 1
    # window: times where tv crosses 0.9 and 0.1
    t90 = next(i for i, v in enumerate(tvs) if v <= 0.9); 
    d2 = dist.copy(); tt = t
    while 0.5*np.abs(d2 - 1/n).sum() > 0.1: d2 = P @ d2; tt += 1
    print(f"n={n:7d}: SRW t_mix(1/4)={t}  3log2n={3*np.log2(n):.1f}  ratio={t/(3*np.log2(n)):.3f}   TV 0.9->0.1 window: {t90}..{tt} (width {tt-t90}, sqrt(log n)={np.sqrt(np.log(n)):.1f})")
