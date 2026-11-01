import itertools
import math
import numpy as np

SEED = 20260923063906
rng = np.random.default_rng(SEED)
min_slack = float("inf")
cases = 0

for m, n, k in [(4,5,3),(5,5,3),(6,4,3),(5,6,2),(6,6,3)]:
    for _ in range(100):
        B = rng.normal(size=(m,n))
        s = np.linalg.svd(B, compute_uv=False)
        if s[k-1] < 1e-12:
            continue
        rows = list(itertools.combinations(range(m), k))
        cols = list(itertools.combinations(range(n), k))
        Z = 0.0
        ar = np.zeros(m)
        ac = np.zeros(n)
        for S in rows:
            for T in cols:
                w = float(np.linalg.det(B[np.ix_(S,T)])**2)
                Z += w
                for i in S:
                    ar[i] += w
                for j in T:
                    ac[j] += w
        ar /= Z
        ac /= Z
        br = k*np.sum(B*B, axis=1)/(s[k-1]**2)
        bc = k*np.sum(B*B, axis=0)/(s[k-1]**2)
        min_slack = min(min_slack, float(np.min(br-ar)), float(np.min(bc-ac)))
        assert np.all(ar <= br + 1e-10)
        assert np.all(ac <= bc + 1e-10)
        cases += 1

print("seed", SEED)
print("cases", cases)
print("min_numerical_slack", repr(min_slack))
print("C_q1", repr(6*math.sqrt(math.e)))
print("selfdual_paid_C_over_L", repr(80*math.sqrt(math.e)))
print("selfdual_star_scale_over_L", repr(3/(40*math.sqrt(6))))
print("q43_paid_C_over_sigma", repr(9*math.sqrt(3*math.e)))
print("q43_star_scale_over_sigma", repr(math.sqrt(2)/3))
print("QFORM_B08_R24_VOLUME_MARGINAL_CHECK_PASS")
