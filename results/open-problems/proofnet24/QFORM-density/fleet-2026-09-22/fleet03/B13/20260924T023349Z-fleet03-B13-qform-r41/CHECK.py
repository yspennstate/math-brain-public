import math
import numpy as np

CT = 759375.0 / 2.0
H2 = 1536.0 * math.e**2
Cstar = 36.0 * CT / H2
W = math.sqrt(2.0 * Cstar)
assert abs(Cstar - 1204.3386411070635) < 1e-9
assert abs(W - 49.07827709093023) < 1e-9
assert abs(W/2.0 - 24.539138545465114) < 1e-9

rng = np.random.default_rng(20260924023349)
for _ in range(5000):
    n = int(rng.integers(5, 35))
    M = rng.normal(size=(n, 2))
    U, _ = np.linalg.qr(M)
    U = U[:, :2]
    c = np.sum(U * U, axis=1)
    K = np.flatnonzero(c <= 1.0/3.0 + 1e-14)
    if len(K) == 0:
        continue
    k = int(rng.choice(K))
    L = [i for i in range(n) if i != k and c[i] <= 1.0/4.0 + 1e-14]
    if len(L) < 2:
        continue
    i, j = [int(x) for x in rng.choice(L, 2, replace=False)]
    I = [r for r in range(n) if r not in (k, i, j)]
    Delta = float(np.linalg.det(U[I].T @ U[I]))
    assert Delta >= 1.0/36.0 - 2e-12

for _ in range(5000):
    t = rng.normal(size=4)
    a = rng.normal(size=4)
    dk = float(rng.choice([-1.0, 1.0]) * (1.0 + rng.random()))
    def G(p, q):
        return dk * (t[p] - t[q])**2 + a[p] + a[q]
    lhs = G(0,1) + G(2,3) - G(0,2) - G(1,3)
    rhs = -2.0 * dk * (t[0]-t[3]) * (t[1]-t[2])
    assert abs(lhs-rhs) <= 1e-10 * (1.0 + abs(lhs) + abs(rhs))

print('QFORM_B13_R41_TWOLINE_CHECK_PASS')
print('Cstar=', repr(Cstar))
print('slope_width_constant=', repr(W))
print('row_distance_constant=', repr(W/2.0))
