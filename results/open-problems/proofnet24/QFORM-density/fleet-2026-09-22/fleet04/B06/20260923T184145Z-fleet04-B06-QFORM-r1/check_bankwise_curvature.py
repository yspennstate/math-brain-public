import numpy as np

rng = np.random.default_rng(20260923)
Lam = np.diag([2.3, -1.7, 1.2])

for _ in range(1000):
    R = np.linalg.qr(rng.normal(size=(9, 3)))[0]
    A = R @ Lam @ R.T
    found = None
    for i in range(9):
        for j in range(i + 1, 9):
            P = R[[i, j], :]
            B = P @ Lam @ P.T
            if np.linalg.det(B) < -1e-4:
                found = (i, j, P, B)
                break
        if found:
            break
    if found:
        break

i, j, P, B = found
J = [k for k in range(9) if k not in (i, j)]
C = A[np.ix_([i, j], J)]
AJ = A[np.ix_(J, J)]
Schur = AJ - C.T @ np.linalg.inv(B) @ C
w, V = np.linalg.eigh(Schur)
idx = np.argmax(np.abs(w))
lam = w[idx]
h = V[:, idx]
mu, O = np.linalg.eigh(B)
T2 = O.T @ np.linalg.inv(B) @ C
T = np.vstack([T2, h])

D = -np.linalg.det(B)
tau = np.linalg.det(P @ P.T)
reconstruction = T.T @ np.diag([mu[0], mu[1], lam]) @ T
full_gram = T @ T.T + np.diag([1.0, 1.0, 0.0])

print("pair", i, j)
print("tau", tau)
print("schur_rank_tail", np.sort(np.abs(w))[:-1].max())
print("reconstruction_error", np.max(np.abs(AJ - reconstruction)))
print("coefficient_identity_relative_error",
      abs(D * abs(lam) - abs(np.linalg.det(Lam)) * tau)
      / (abs(np.linalg.det(Lam)) * tau))
print("full_gram_identity_relative_error",
      abs(np.linalg.det(full_gram) - 1 / tau) / (1 / tau))
print("live_gate_bound", 12 * (4 * 1728 * 64 / 61) ** (1 / 3))
