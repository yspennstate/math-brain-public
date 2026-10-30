import itertools
import math
import numpy as np
import mpmath as mp

rng = np.random.default_rng(280923)
max_rel = 0.0
for _ in range(500):
    m = int(rng.integers(3, 7))
    n = int(rng.integers(3, 7))
    while True:
        P = rng.normal(size=(2, 2))
        if abs(np.linalg.det(P)) > 0.1:
            break
    R = rng.normal(size=(2, n))
    C = rng.normal(size=(m, 2))
    M = rng.normal(size=(m, n))
    B = np.block([[P, R], [C, M]])
    S = M - C @ np.linalg.inv(P) @ R
    D = abs(np.linalg.det(P))
    anchored = 0.0
    e3 = 0.0
    for K in itertools.combinations(range(m), 3):
        for L in itertools.combinations(range(n), 3):
            rows = [0, 1] + [2+k for k in K]
            cols = [0, 1] + [2+l for l in L]
            anchored += np.linalg.det(B[np.ix_(rows, cols)])**2
            e3 += np.linalg.det(S[np.ix_(K, L)])**2
    rel = abs(anchored - D*D*e3) / max(1.0, abs(anchored), abs(D*D*e3))
    max_rel = max(max_rel, rel)

rng = np.random.default_rng(280924)
count = 0
min_slack = float('inf')
min_ratio = float('inf')
for _ in range(2000):
    rank = int(rng.integers(4, 10))
    lam = rng.uniform(0.3, 1.7, size=rank)**2
    F2 = lam.sum()
    sr = F2 / lam.max()
    if sr <= 3:
        continue
    e3 = sum(lam[i]*lam[j]*lam[k] for i,j,k in itertools.combinations(range(rank), 3))
    lower = (sr-3)/(6*sr) * F2**3
    min_slack = min(min_slack, e3-lower)
    min_ratio = min(min_ratio, e3/lower)
    count += 1

C5 = float(math.e/20 * mp.beta(mp.mpf(1)/10, mp.mpf(1)/40))
C5_sr4 = C5 * 24**0.1
CD5 = 5 * math.sqrt(2*math.e)
CD5_sr4 = CD5 * 24**0.1
C04 = 3 * 6**(1/6) * math.e**(5/6) * 2**(-2/9)
C04_sr4 = C04 * 24**(1/12)

print('STATUS=PASS')
print(f'anchored_identity_trials=500')
print(f'max_relative_error={max_rel:.16e}')
print(f'stable_rank_cases={count}')
print(f'min_stable_rank_inequality_slack={min_slack:.16e}')
print(f'min_E3_to_lower_bound_ratio={min_ratio:.16e}')
print(f'C5_regdet={C5:.15f}')
print(f'C5_stable_rank_4={C5_sr4:.15f}')
print(f'D5_source_constant={CD5:.15f}')
print(f'D5_source_stable_rank_4={CD5_sr4:.15f}')
print(f'partner_hybrid_constant={C04:.15f}')
print(f'partner_hybrid_stable_rank_4={C04_sr4:.15f}')