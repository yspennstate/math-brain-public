import math
import numpy as np
from itertools import combinations

C3 = 2*math.pi + 3*math.sqrt(3)
CSTAR = C3 + math.sqrt(C3*C3 + 3*math.pi*math.pi)
assert abs(CSTAR - 24.183038289961516) < 1e-12

# Exact advertised finite-packet constants.
assert abs(4*CSTAR - 96.73215315984606) < 1e-11
assert abs(8*CSTAR - 193.46430631969213) < 1e-11

# Cauchy-Binet / minimum singular-value extraction sanity checks.
rng = np.random.default_rng(20260922)
min_margin = float('inf')
min_cb_margin = float('inf')
for m in range(3, 11):
    N = math.comb(m, 3)
    for _ in range(400):
        G = rng.normal(size=(m, 3))
        U, _ = np.linalg.qr(G, mode='reduced')
        detsq = []
        sminsq = []
        for I in combinations(range(m), 3):
            UI = U[list(I), :]
            d2 = float(np.linalg.det(UI)**2)
            sm = float(np.linalg.svd(UI, compute_uv=False)[-1]**2)
            detsq.append(d2)
            sminsq.append(sm)
            min_margin = min(min_margin, sm-d2)
        cb = sum(detsq)
        min_cb_margin = min(min_cb_margin, cb-1.0)
        assert abs(cb-1.0) < 2e-12
        j = int(np.argmax(detsq))
        assert detsq[j] + 2e-12 >= 1.0/N
        assert sminsq[j] + 2e-12 >= detsq[j]

# Random spectral-packet perturbation checks: selected physical triple
# has the claimed singular gap L*gamma-eta.
min_gap_margin = float('inf')
for m in range(3, 9):
    for _ in range(250):
        U, _ = np.linalg.qr(rng.normal(size=(m,3)), mode='reduced')
        eigs = rng.choice([-1.0, 1.0], 3) * (1.0 + rng.random(3)*2.0)
        L = float(np.min(np.abs(eigs)))
        Is = list(combinations(range(m),3))
        d2s = np.array([np.linalg.det(U[list(I),:])**2 for I in Is])
        I = Is[int(np.argmax(d2s))]
        gamma = float(np.max(d2s))
        # symmetric perturbation normalized to eta = 0.4 L gamma
        R = rng.normal(size=(m,m)); R = (R+R.T)/2
        op = np.linalg.norm(R,2)
        eta = 0.4*L*gamma
        E = np.zeros((m,m)) if op == 0 else R*(eta/op)
        B = U @ np.diag(eigs) @ U.T + E
        M = B[np.ix_(I,I)]
        sm = float(np.linalg.svd(M, compute_uv=False)[-1])
        claimed = L*gamma-eta
        min_gap_margin = min(min_gap_margin, sm-claimed)
        assert sm + 5e-11 >= claimed

print('QFORM_FINITE_TAIL_CHECK_PASS')
print('CSTAR', repr(CSTAR))
print('m4_exact_rank3_bound', repr(4*CSTAR))
print('m4_s4_le_L_over_8_bound', repr(8*CSTAR))
print('min_sminsq_minus_detsq', repr(min_margin))
print('min_cauchy_binet_sum_minus_one', repr(min_cb_margin))
print('min_random_gap_margin', repr(min_gap_margin))
