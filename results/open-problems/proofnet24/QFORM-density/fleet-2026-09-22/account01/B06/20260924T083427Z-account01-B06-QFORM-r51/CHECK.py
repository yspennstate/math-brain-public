import math
import numpy as np

rng = np.random.default_rng(20260924)
max_alllayer = 0.0
max_categorized = 0.0

for m in [0, 1, 2, 5, 10]:
    for _ in range(100):
        K = rng.normal(size=(3, 3))
        K = (K + K.T) / 2
        if abs(K[0, 0]) < 0.1:
            K[0, 0] += 0.3 if K[0, 0] >= 0 else -0.3
        M = rng.normal(size=(3, m))
        a = K[0, 0]
        c = K[1:, 0]
        B = K[1:, 1:] - np.outer(c, c) / a
        if m:
            N = M[1:, :] - np.outer(c, M[0, :]) / a
        else:
            N = np.zeros((2, 0))
        C = np.concatenate([B, N], axis=1)
        Ablock = np.concatenate([K, M], axis=1)

        E = 0.0
        for r in range(1, 3 + m):
            for s in range(r + 1, 3 + m):
                E += np.linalg.det(Ablock[:, [0, r, s]]) ** 2
        rhs = a * a * np.linalg.det(C @ C.T)
        max_alllayer = max(max_alllayer, abs(E-rhs)/max(1.0, abs(E), abs(rhs)))

        # adj(K) by cofactors; valid even if K is singular.
        adj = np.empty((3, 3))
        for ii in range(3):
            for jj in range(3):
                rows = [r for r in range(3) if r != jj]
                cols = [q for q in range(3) if q != ii]
                adj[ii, jj] = ((-1) ** (ii + jj)) * np.linalg.det(K[np.ix_(rows, cols)])
        R = adj @ M
        Sigma = 0.0
        for p in range(m):
            for q in range(p + 1, m):
                Sigma += np.linalg.det(Ablock[:, [0, 3+p, 3+q]]) ** 2
        rhs2 = np.linalg.det(K)**2 + np.sum(R[1]**2) + np.sum(R[2]**2) + Sigma
        max_categorized = max(max_categorized, abs(E-rhs2)/max(1.0, abs(E), abs(rhs2)))

C_grad = 4 * 6**0.75 * (math.pi * math.e)**0.25
C_ns = C_grad * (8/3)**0.25
C_partner_well = 15.0823111681 * 4**0.25

print({
    "max_normalized_alllayer_error": max_alllayer,
    "max_normalized_categorized_error": max_categorized,
    "C_grad": C_grad,
    "C_nearsingular": C_ns,
    "C_partner_well_indefinite": C_partner_well,
})
