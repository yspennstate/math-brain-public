try:
    import psutil; psutil.Process().nice(psutil.BELOW_NORMAL_PRIORITY_CLASS)
except Exception:
    pass
# Consistency check of Theorem 5.1 (loss-free decoupling at a hub):
# Q = 2 X_h (L_I + L_J + beta) + X_I^T E1 X_I + 2 lam (a.X_I)(b.X_J) + X_J^T E2 X_J + linear,
# uniform laws on [-1/2,1/2]; E1, E2 dense with ||E|| = s (twist INSIDE the blocks, none across).
# The hub is integrated exactly (sinc); the rest by Monte Carlo. Bound: |phi(t)| <= K (2|t|)^{-3/2},
# K = [2 pi (4 pi)^2 2]^{1/2} (|lam| sqrt(det G_I det G_J))^{-1/2}.
import numpy as np
rng = np.random.default_rng(1)
m = 8
H = np.array([[1]])
for _ in range(3):
    H = np.block([[H, H], [H, -H]])
H = H / np.sqrt(m)
wI, aI = H[1], H[2]            # orthonormal, entries +-1/sqrt(8): leverages 1/4 on I
wJ, bJ = H[3], H[5]
lam = 1.0
def dense(s):
    M = rng.standard_normal((m, m)); M = (M + M.T) / 2
    return s * M / np.linalg.norm(M, 2)
bl_I = rng.standard_normal(m) * 0.5; bl_J = rng.standard_normal(m) * 0.5; beta = 0.17
GI = np.array([[wI @ wI, wI @ aI], [aI @ wI, aI @ aI]]); GJ = np.array([[wJ @ wJ, wJ @ bJ], [bJ @ wJ, bJ @ bJ]])
K = np.sqrt(2 * np.pi * (4 * np.pi) ** 2 * 2) / np.sqrt(abs(lam) * np.sqrt(np.linalg.det(GI) * np.linalg.det(GJ)))
ts = np.array([2.0, 4.0, 8.0, 16.0, 32.0, 64.0])
N, chunk = 4_000_000, 500_000
for s in [0.0, 1.0, 3.0]:
    E1, E2 = dense(s), dense(s)
    acc = np.zeros(len(ts), dtype=complex)
    for c in range(N // chunk):
        XI = rng.uniform(-0.5, 0.5, (chunk, m)); XJ = rng.uniform(-0.5, 0.5, (chunk, m))
        L = XI @ wI + XJ @ wJ + beta
        R = np.einsum('ni,ij,nj->n', XI, E1, XI) + np.einsum('ni,ij,nj->n', XJ, E2, XJ) \
            + 2 * lam * (XI @ aI) * (XJ @ bJ) + XI @ bl_I + XJ @ bl_J
        for k, t in enumerate(ts):
            u = t * L                      # hub uniform on [-1/2,1/2]: E e^{i 2 t L x} = sin(tL)/(tL)
            psi = np.sinc(u / np.pi)
            acc[k] += np.sum(psi * np.exp(1j * t * R))
    phi = np.abs(acc / N)
    print(f"twist norm s={s}:", flush=True)
    for t, p in zip(ts, phi):
        print(f"  t={t:5.1f}  |phi|={p:.5f}  t^1.5|phi|={p * t ** 1.5:.3f}  bound={K * (2 * t) ** -1.5:.4f}", flush=True)
print("MC floor ~", 1 / np.sqrt(N), flush=True)
