"""Numerical checks of the sign-decoupling argument (Lemmas 6.2-6.3, Proposition 6.4).

For symmetric A with |a_ii| <= d, |a_ij| <= a (i != j) and k eigenvalues of modulus >= 1
(orthonormal eigenvectors Phi, n x k), and eps in {+-1}^n with I = {eps=1}, J = {eps=-1}:
  (1) A - D A D = 2 C,  C = P_I A P_J + P_J A P_I            (D = diag(eps))
  (2) 2 Phi^T C Phi = Lambda - Phi^T diag(A) Phi - Q_eps,   Q_eps = sum_{i!=j} eps_i eps_j a_ij phi_i phi_j^T
  (3) E_eps ||Q_eps||_F^2 = sum_{i!=j} a_ij^2 (|phi_i|^2|phi_j|^2 + (phi_i.phi_j)^2) <= 2 a^2 k^2
  (4) s_k(C) = sigma_{ceil(k/2)}(A_IJ) and s_k(C) >= s_k(Phi^T C Phi) >= (1 - d - ||Q_eps||)/2
"""
import numpy as np
rng = np.random.default_rng(20260924)

def frame(A, k):
    w, V = np.linalg.eigh(A)
    idx = np.argsort(-np.abs(w))[:k]
    return w[idx], V[:, idx]

def check(A, k, name, trials=400):
    n = A.shape[0]
    lam, Phi = frame(A, k)
    assert np.min(np.abs(lam)) >= 1 - 1e-9, (name, lam)
    d = np.max(np.abs(np.diag(A)))
    O = A - np.diag(np.diag(A))
    a = np.max(np.abs(O))
    rows = Phi  # row i is phi_i
    nrm2 = np.sum(rows**2, axis=1)
    G = rows @ rows.T
    EQ = np.sum((O**2) * (np.outer(nrm2, nrm2) + G**2))   # diagonal of O is zero
    worst = {"id1": 0.0, "id2": 0.0, "sv": 0.0, "lb": np.inf}
    best = None
    mc = []
    for t in range(trials):
        eps = rng.choice([-1.0, 1.0], size=n)
        D = np.diag(eps)
        I = eps > 0
        C = np.zeros_like(A)
        C[np.ix_(I, ~I)] = A[np.ix_(I, ~I)]
        C[np.ix_(~I, I)] = A[np.ix_(~I, I)]
        worst["id1"] = max(worst["id1"], np.max(np.abs(A - D @ A @ D - 2 * C)))
        Q = Phi.T @ (D @ O @ D) @ Phi
        lhs = 2 * Phi.T @ C @ Phi
        rhs = np.diag(lam) - Phi.T @ np.diag(np.diag(A)) @ Phi - Q
        worst["id2"] = max(worst["id2"], np.max(np.abs(lhs - rhs)))
        qF = np.linalg.norm(Q, "fro")
        mc.append(qF**2)
        sC = np.linalg.svd(C, compute_uv=False)
        M = A[np.ix_(I, ~I)]
        sM = np.linalg.svd(M, compute_uv=False) if M.size else np.zeros(1)
        sMp = np.concatenate([sM, np.zeros(k)])
        m = (k + 1) // 2
        worst["sv"] = max(worst["sv"], abs(sC[k - 1] - sMp[m - 1]))
        sPhi = np.linalg.svd(Phi.T @ C @ Phi, compute_uv=False)[k - 1]
        bound = (1 - d - np.linalg.norm(Q, 2)) / 2
        worst["lb"] = min(worst["lb"], sC[k - 1] - sPhi, sPhi - bound)
        if best is None or qF < best[0]:
            best = (qF, sMp[m - 1])
    print(f"{name:28s} n={n:4d} k={k} d={d:.3f} a={a:.4f} | E||Q||^2 exact={EQ:.4f} "
          f"mc={np.mean(mc):.4f} bound 2a^2k^2={2*a*a*k*k:.4f} | best cut ||Q||_F={best[0]:.3f} "
          f"sigma_{(k+1)//2}={best[1]:.3f} >= {(1-d-np.sqrt(2)*a*k)/2:.3f} | id1={worst['id1']:.1e} "
          f"id2={worst['id2']:.1e} sv={worst['sv']:.1e} lbslack={worst['lb']:.1e}")
    assert worst["id1"] < 1e-12 and worst["id2"] < 1e-9 and worst["sv"] < 1e-9 and worst["lb"] > -1e-9
    assert EQ <= 2 * a * a * k * k + 1e-12
    return EQ

def scaled(A, k):
    lam, _ = frame(A, k)
    return A / np.min(np.abs(lam))

# (a) spread Wigner-type
for n in (60, 200):
    W = rng.standard_normal((n, n)); W = (W + W.T) / np.sqrt(2 * n)
    np.fill_diagonal(W, rng.uniform(-0.05, 0.05, n) * 0)
    for k in (3, 5):
        check(scaled(W, k), k, f"wigner n={n}")
# (b) five stars with spread weights
def stars(nh, m):
    n = nh + nh * m
    A = np.zeros((n, n))
    for h in range(nh):
        leaves = nh + h * m + np.arange(m)
        w = rng.standard_normal(m); w /= np.linalg.norm(w)
        A[h, leaves] = w; A[leaves, h] = w
    return A
check(stars(3, 120), 5, "three stars")
check(stars(3, 120), 3, "three stars")
# (c) rank-five bank-cross example (hub + trigonometric leaves), t = 1
m = 401; th = 2 * np.pi * np.arange(m) / m
l = np.ones(m) / np.sqrt(m); v = np.sqrt(2 / m) * np.cos(2 * th); p = np.sqrt(2 / m) * np.sin(2 * th)
w = np.sqrt(2 / m) * np.cos(th); z = np.sqrt(2 / m) * np.sin(th); e = 1e-3
n = m + 1
def ext(x):
    y = np.zeros(n); y[1:] = x; return y
hvec = np.zeros(n); hvec[0] = 1
L_, V_, P_, W_, Z_ = map(ext, (l, v, p, w, z))
A = (np.outer(hvec, L_) + np.outer(L_, hvec) + e * (np.outer(L_, P_) + np.outer(P_, L_))
     + np.outer(V_, V_) + np.outer(W_, W_) - np.outer(Z_, Z_))
check(A, 5, "rank-five bank cross")
# (d) random low-rank plus small diagonal, entries small
for r in (5, 8):
    n = 300
    U = np.linalg.qr(rng.standard_normal((n, r)))[0]
    S = np.diag(rng.choice([-1, 1], r) * rng.uniform(1, 3, r))
    A = U @ S @ U.T
    A += np.diag(rng.uniform(-0.03, 0.03, n))
    check(scaled(A, 5), 5, f"rank {r} + small diag")
print("ALL DECOUPLING CHECKS PASS")
