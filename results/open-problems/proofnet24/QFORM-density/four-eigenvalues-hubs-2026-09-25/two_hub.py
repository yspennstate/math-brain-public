"""The two-hub bound. If H = {h1, h2}, A_{H,H} = 0 and G = A_{H,R} A_{H,R}^T has det G > 0, then for every b and c
the density of Q = X^T A X + b^T X + c is at most sqrt(2 pi e) det(G)^(-1/4).

Proof being checked: given X_R, Q = V . X_H + (a function of X_R) with V = 2 A_{H,R} X_R + b_H, so the conditional
density is at most 1/max|V_i| <= sqrt(2)/|V|; by Lemma 3.2(b) V has density at most e/(4 sqrt(det G)), and in the
plane E|V|^(-1) <= 2 sqrt(pi M) for any density bounded by M.

Examples: two stars sharing their N leaves, hub rows w1, w2 (unit vectors). They have eigenvalues +-|w1|, +-|w2|
when w1 is orthogonal to w2, no pivot for N > 256, and every off-diagonal block of rank at most two, so the random
sign argument gives no order-three crossing; the bound applies to them for every b. Coordinates are uniform on
[-1/2, 1/2]. Also: hub rows at angle theta, where det G = sin(theta)^2 and the bound grows like |sin theta|^(-1/2).
"""
import math

import numpy as np

rng = np.random.default_rng(20260925)
N = 400
S = 1_000_000
e1 = np.ones(N) / math.sqrt(N)
alt = np.array([(-1.0) ** j for j in range(N)]) / math.sqrt(N)


def build(w1, w2):
    n = N + 2
    A = np.zeros((n, n))
    A[0, 2:] = w1
    A[2:, 0] = w1
    A[1, 2:] = w2
    A[2:, 1] = w2
    return A


def no_pivot(A, eta=1 / 12, zeta=1 / 256):
    d = np.diag(A)
    if np.any(np.abs(d) >= eta):
        return False
    M = np.abs(np.outer(d, d) - A * A)
    np.fill_diagonal(M, 0)
    return M.max() < zeta


def max_cut_rank(A, trials=200):
    best = 0
    for _ in range(trials):
        eps = rng.random(A.shape[0]) < 0.5
        blk = A[np.ix_(eps, ~eps)]
        if blk.size:
            best = max(best, np.linalg.matrix_rank(blk, tol=1e-9))
    return best


def sample_Q(w1, w2, b_h, b_r):
    U = rng.uniform(-0.5, 0.5, size=(S, 2))
    L1 = np.zeros(S)
    L2 = np.zeros(S)
    Lb = np.zeros(S)
    for j in range(N):
        x = rng.uniform(-0.5, 0.5, size=S)
        L1 += w1[j] * x
        L2 += w2[j] * x
        Lb += b_r[j] * x
    return 2 * U[:, 0] * L1 + 2 * U[:, 1] * L2 + U @ b_h + Lb


def max_density(q, bins=4000):
    hist, edges = np.histogram(q, bins=bins)
    return (hist / (q.size * (edges[1] - edges[0]))).max()


ok = True
A = build(e1, alt)
ev = np.sort(np.linalg.eigvalsh(A))
spec = np.allclose(ev[[0, 1, -2, -1]], [-1, -1, 1, 1]) and np.max(np.abs(ev[2:-2])) < 1e-9
npv = no_pivot(A)
rk = max_cut_rank(A)
print(f"overlapping stars: spectrum +-1 twice {spec}; no pivot {npv}; max cut rank over 200 partitions {rk}", flush=True)
ok &= spec and npv and rk <= 2

cases = [
    ("overlapping, w1 perp w2, b = 0", e1, alt, np.zeros(2), np.zeros(N)),
    ("overlapping, w1 perp w2, b_H = (0.3, -0.2)", e1, alt, np.array([0.3, -0.2]), np.zeros(N)),
    ("overlapping, w1 perp w2, b_R = 0.4 w1 + 0.4 w2", e1, alt, np.zeros(2), 0.4 * e1 + 0.4 * alt),
]
for theta in (math.pi / 6, 0.1):
    w2 = math.cos(theta) * e1 + math.sin(theta) * alt
    cases.append((f"angle {theta:.3f} between hub rows, b = 0", e1, w2, np.zeros(2), np.zeros(N)))

for name, w1, w2, b_h, b_r in cases:
    G = np.array([[w1 @ w1, w1 @ w2], [w1 @ w2, w2 @ w2]])
    bound = math.sqrt(2 * math.pi * math.e) * np.linalg.det(G) ** (-0.25)
    d = max_density(sample_Q(w1, w2, b_h, b_r))
    passed = d < bound
    ok &= passed
    print(f"  {name:50s} det G = {np.linalg.det(G):.4f}  max density {d:.4f} < bound {bound:.4f}: {passed}",
          flush=True)
print("ALL PASS" if ok else "FAIL")
