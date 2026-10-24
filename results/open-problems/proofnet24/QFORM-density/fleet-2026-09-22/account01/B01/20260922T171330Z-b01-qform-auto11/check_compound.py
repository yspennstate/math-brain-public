import itertools
import math
import numpy as np

rng = np.random.default_rng(20260922)
max_err = 0.0
for m in (3, 5, 9):
    for _ in range(50):
        U, _ = np.linalg.qr(rng.normal(size=(m, 2)))
        lam = np.array([
            rng.choice((-1.0, 1.0)) * rng.uniform(0.3, 3.0),
            rng.choice((-1.0, 1.0)) * rng.uniform(0.3, 3.0),
        ])
        H = U @ np.diag(lam) @ U.T
        pairs = list(itertools.combinations(range(m), 2))
        compound_sq = 0.0
        for R in pairs:
            for C in pairs:
                compound_sq += np.linalg.det(H[np.ix_(R, C)]) ** 2
        target = float((lam[0] * lam[1]) ** 2)
        max_err = max(max_err, abs(compound_sq - target))

C_partner = 2 * 3 ** 0.25 * math.sqrt(math.pi * math.e)
C_rank2_inrange = 16 * math.sqrt(30)
threshold = (C_partner / C_rank2_inrange) ** 4

print(f"max_compound_identity_error={max_err:.3e}")
print(f"partner_prefactor={C_partner:.15f}")
print(f"rank2_inrange_prefactor={C_rank2_inrange:.15f}")
print(f"epsilon_crossover={threshold:.15e}")
print("STATUS=PASS" if max_err < 1e-10 else "STATUS=FAIL")
