import itertools
import math
import numpy as np

SEED = 20260923
TRIALS = 30
N = 7
rng = np.random.default_rng(SEED)

max_rel = 0.0
min_union_slack = float('inf')

for _ in range(TRIALS):
    G = rng.normal(size=(N, 3))
    U = np.linalg.qr(G)[0][:, :3]

    R = np.linalg.qr(rng.normal(size=(3, 3)))[0]
    eig = np.array([1.0 + rng.random(), -(1.0 + rng.random()), 1.0 + rng.random()])
    Lam = R @ np.diag(eig) @ R.T
    A = U @ Lam @ U.T

    triples = list(itertools.combinations(range(N), 3))
    p = np.array([np.linalg.det(U[list(I), :]) ** 2 for I in triples])

    alpha = np.zeros(N)
    for wt, I in zip(p, triples):
        for i in I:
            alpha[i] += wt
    leverage = np.sum(U * U, axis=1)
    denom = max(1e-16, np.max(leverage))
    max_rel = max(max_rel, np.max(np.abs(alpha - leverage)) / denom)

    p_disjoint = 0.0
    for a, I in enumerate(triples):
        SI = set(I)
        for b, J in enumerate(triples):
            if SI.isdisjoint(J):
                p_disjoint += p[a] * p[b]

    ell = np.max(leverage)
    min_union_slack = min(min_union_slack, p_disjoint - (1.0 - 3.0 * ell))

    zsum = 0.0
    for mask in range(1 << N):
        L = [i for i in range(N) if (mask >> i) & 1]
        RR = [i for i in range(N) if not ((mask >> i) & 1)]
        if len(L) >= 3 and len(RR) >= 3:
            M = A[np.ix_(L, RR)]
            s = np.linalg.svd(M, compute_uv=False)
            z = np.prod(s[:3] ** 2) if len(s) >= 3 else 0.0
        else:
            z = 0.0
        zsum += z

    avg_z = zsum / (1 << N)
    target = np.linalg.det(Lam) ** 2 * p_disjoint / 64.0
    if target > 1e-14:
        max_rel = max(max_rel, abs(avg_z - target) / target)

C3 = 3 * 2 ** (4 / 3) * math.e ** (1 / 3)
K3 = 4 * math.pi ** 1.5 * math.e ** 0.5
KD = 2 ** 1.5 * K3
L0 = 6 * math.pi * 2 ** (2 / 3)
C_HYB = (2 / math.pi) * math.sqrt(KD) * (2 * L0) ** 0.25

print(f'trials={TRIALS}')
print(f'max_relative_identity_error={max_rel:.17g}')
print(f'min_union_bound_slack={min_union_slack:.17g}')
print(f'C3={C3:.15f}')
print(f'K3={K3:.15f}')
print(f'KD={KD:.15f}')
print(f'D3_density_base={2*C3:.15f}')
print(f'D3_L1_base={4*math.pi*C3:.15f}')
print(f'partner_hybrid_base={C_HYB:.15f}')
print(f'D3_ge_quarter_density={2*C3*4**(1/6):.15f}')
print(f'D3_ge_quarter_L1={4*math.pi*C3*4**(1/6):.15f}')
assert max_rel < 1e-11
assert min_union_slack >= -1e-12
