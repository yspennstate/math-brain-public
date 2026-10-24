import numpy as np
rng = np.random.default_rng(3)
# X' ~ N(0, s^2 I_m), density <= 1 needs s >= 1/sqrt(2 pi); L = M X' in R^2; R = X'^T A X'
# nu^(eta) = (2pi)^-2 int |E e^{i zeta.L + i eta R}|^2 d^2 zeta, computed exactly for Gaussians
def nuhat(eta, M, A, s):
    m = A.shape[0]
    K = np.eye(m) - 2j * eta * s**2 * A
    Kinv = np.linalg.inv(K)
    detfac = abs(np.linalg.det(K)) ** (-1.0)          # |det K^{-1/2}|^2
    G = M @ Kinv @ M.T                                  # E e^{i zeta.L + i eta R} = det^{-1/2} exp(-(s^2/2) zeta^T G zeta)
    ReG = (G + G.conj().T).real / 2                     # |exp(...)|^2 = exp(-s^2 zeta^T Re(G) zeta)
    return (2*np.pi)**-2 * detfac * np.pi / (s**2 * np.sqrt(np.linalg.det(ReG)))
worst = 0
for trial in range(200):
    m = rng.integers(6, 11); nJ = rng.integers(3, m - 1)
    J = np.arange(nJ); I = np.arange(nJ, m)
    M = np.zeros((2, m)); M[:, :] = rng.standard_normal((2, m)) * rng.random()   # partners anywhere
    A = rng.standard_normal((m, m)) * rng.random() * 2; A = (A + A.T) / 2
    s = 1/np.sqrt(2*np.pi) * (1 + 2 * rng.random())
    MJ = M[:, J]; sv = np.linalg.svd(MJ, compute_uv=False)
    P = MJ.T @ np.linalg.pinv(MJ @ MJ.T) @ MJ
    C = A[np.ix_(I, J)] @ (np.eye(nJ) - P)
    F = np.linalg.norm(C)
    if (np.linalg.norm(C, axis=1)**2).max() > F**2 / 2 or sv[1] < 1e-3: continue
    for eta in [0.5, 1, 2, 5, 10, 30, 100, 300]:
        nh = nuhat(eta, M, A, s)
        b = 2**2.5 * np.pi / (sv[0] * sv[1] * F * eta)
        worst = max(worst, nh / b)
print("max over trials of nu^(eta) / bound:", round(worst, 4))
