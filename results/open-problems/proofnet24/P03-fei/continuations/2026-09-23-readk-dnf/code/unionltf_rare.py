"""Stress the level-tail step with the paper's parameters (a = 1.44, beta = 5): read-k unions of RARELY-true
threshold functions on larger sets (sizes 5..9, thresholds near the top). Prints every quantity quoted in the paper."""
import math, numpy as np
import unionltf as U
from feicore import polite
polite()

def ltf_rare(R, n, rng):
    xs = np.arange(1 << n)
    bits = ((xs[:, None] >> np.arange(n)[None, :]) & 1) * 2 - 1
    w = np.zeros(n); s = rng.choice([-1, 1], size=len(R)); mag = rng.exponential(size=len(R)) + 0.3
    w[R] = s * mag
    theta = float(mag.sum() * rng.uniform(0.55, 0.95))
    return (bits @ w - theta) > 0, w

def build_big(n, k, rng, mmax=8):
    deg = np.zeros(n, dtype=int); fam = []
    for _ in range(300):
        if len(fam) >= mmax: break
        size = int(rng.integers(5, min(9, n) + 1))
        cand = [j for j in range(n) if deg[j] < k]
        if len(cand) < size: continue
        R = sorted(rng.choice(cand, size=size, replace=False).tolist())
        for j in R: deg[j] += 1
        fam.append(R)
    return fam

U.ltf_on = ltf_rare; U.build = build_big
rng = np.random.default_rng(7)
agg = dict(HI=0.0, path=0.0, rank=0.0, K=0.0, bound=0.0); mingap = 1e9; cnt = 0; kmax = 0
for n in (12, 14):
    for k in (1, 2, 3):
        for rep in range(8 if n == 12 else 4):
            a = U.analyse(n, k, rng)
            if a is None: continue
            cnt += 1; kmax = max(kmax, a['k'])
            for f in agg: agg[f] = max(agg[f], a[f])
            mingap = min(mingap, a['gap'])
print(f"rare family, a={U.A_EXP}, beta={U.BETA}: {cnt} formulas (k <= {kmax}): max H/I {agg['HI']:.3f}, max path ratio "
      f"{agg['path']:.3f}, max piece E F {agg['rank']:.3f}, max K {agg['K']:.4f}, max bound/I {agg['bound']:.2f}, "
      f"min(bound-H) {mingap:.3f}", flush=True)
