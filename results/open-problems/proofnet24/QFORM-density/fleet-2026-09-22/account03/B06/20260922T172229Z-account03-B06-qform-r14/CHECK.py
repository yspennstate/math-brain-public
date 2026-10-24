import math
import numpy as np

rng = np.random.default_rng(20260922)
Lam = np.diag([1.25, -1.75, 2.5])
max_rel = 0.0
max_tail = 0.0
count = 0
for _ in range(50):
    Q, _ = np.linalg.qr(rng.normal(size=(8, 3)))
    R = Q[:, :3]
    A = R @ Lam @ R.T
    for i in range(8):
        for j in range(i + 1, 8):
            H = A[np.ix_([i, j], [i, j])]
            detH = np.linalg.det(H)
            if detH >= -1e-9:
                continue
            K = [k for k in range(8) if k not in (i, j)]
            B = A[np.ix_([i, j], K)]
            D = A[np.ix_(K, K)]
            S = D - B.T @ np.linalg.inv(H) @ B
            ev = np.linalg.eigvalsh(S)
            sigma = ev[np.argmax(np.abs(ev))]
            tail = np.sort(np.abs(ev))[:-1]
            max_tail = max(max_tail, float(np.max(tail)))
            ri, rj = R[i], R[j]
            Delta = np.linalg.det(np.array([[ri @ ri, ri @ rj], [rj @ ri, rj @ rj]]))
            lhs = abs(detH) * abs(sigma)
            rhs = abs(np.linalg.det(Lam)) * Delta
            max_rel = max(max_rel, abs(lhs-rhs) / max(rhs, 1e-14))
            count += 1

print('random_indefinite_pairs', count)
print('max_relative_mass_identity_error', f'{max_rel:.16e}')
print('max_spurious_schur_eigenvalue', f'{max_tail:.16e}')

for m in [4, 16, 64, 256]:
    n = m + 2
    R = np.zeros((n, 3))
    R[0, 0] = 1.0
    R[1, 1] = 1.0
    R[2:, 2] = 1.0 / math.sqrt(m)
    Lam2 = np.diag([1.0, -1.0, 1.0])
    A = R @ Lam2 @ R.T
    H = A[:2, :2]
    K = list(range(2, n))
    B = A[np.ix_([0, 1], K)]
    S = A[np.ix_(K, K)] - B.T @ np.linalg.inv(H) @ B
    sigma = np.linalg.eigvalsh(S)[-1]
    triple = [abs(np.linalg.det(A[np.ix_([0, 1, k], [0, 1, k])])) for k in K]
    print('witness', m, 'detH', np.linalg.det(H), 'sigma', sigma,
          'max_triple_det', max(triple), 'sum_abs_triple_det', sum(triple))

C_nonzero = 16 * math.sqrt(15) * 2**0.25
C_bilinear = 2 * math.sqrt(30)
print('C_nonzero', C_nonzero)
print('C_bilinear', C_bilinear)
