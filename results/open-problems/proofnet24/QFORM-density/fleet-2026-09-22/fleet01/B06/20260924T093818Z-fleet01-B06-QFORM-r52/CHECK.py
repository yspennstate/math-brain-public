import math
import numpy as np

rng = np.random.default_rng(20260924)
min_observed_max_g2 = 1.0
max_p2_relative_error = 0.0

for m in (2, 3, 5, 10):
    for _ in range(500):
        X = rng.normal(size=(3, 3))
        Q, _ = np.linalg.qr(X)
        u = Q[:, 0]
        v = Q[:, 1]
        w = np.cross(u, v)

        g2 = w*w*(1-u*u)
        min_observed_max_g2 = min(min_observed_max_g2, float(np.max(g2)))

        M = rng.normal(size=(3, m))
        lam = float(rng.choice([-1, 1])) * (0.2 + 4.0*rng.random())
        B = np.vstack([v @ M, w @ M])
        delta2 = float(np.linalg.det(B @ B.T))

        K = lam * np.outer(u, u)
        p2 = 0.0
        for i in range(3):
            for p in range(m):
                for q in range(p+1, m):
                    mat = np.column_stack([K[:, i], M[:, p], M[:, q]])
                    p2 += float(np.linalg.det(mat))**2

        rhs = lam**2 * delta2
        rel = abs(p2-rhs) / max(1.0, abs(p2), abs(rhs))
        max_p2_relative_error = max(max_p2_relative_error, rel)

C = (4.0/3.0) * 2.0**(7.0/4.0) * 6.0**0.25 * (math.pi*math.e)**0.25

print('min_observed_max_g2', repr(min_observed_max_g2))
print('theoretical_floor', repr(1.0/6.0))
print('max_p2_relative_error', repr(max_p2_relative_error))
print('C_star', repr(C))
print('PASS_g', min_observed_max_g2 >= 1.0/6.0 - 1e-12)
print('PASS_P2', max_p2_relative_error < 1e-10)
print('PASS_constant', C < 12.0)
