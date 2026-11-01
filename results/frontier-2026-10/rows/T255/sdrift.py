"""T255: the drift of the shaped-attention covariance SDE (Noci et al. 2306.17759, Theorem 4.2) checked against a
Monte Carlo of one layer of the finite network, and its value on the isotropic ray V = s I.
One layer (Eq. 1 with Eq. 9): X' = lam X + gam A X W^V/sqrt n, A = I + Softmax(Y/tau) - 11^T/m, Y = X W^Q W^K^T X^T/n,
tau = tau0 sqrt(n nk). Given X, E[V'] = lam^2 V + gam^2 E[A V A^T], so n E[V' - V] = gam^2 n E[S V + V S^T + S V S^T],
S = A - I. With X W^Q/sqrt n = L G1, X W^K/sqrt n = L G2 (L L^T = V, G1, G2 m x nk iid N(0,1)), Y = L G1 G2^T L^T.
usage: python -X utf8 sdrift.py"""
import numpy as np


def b_paper(V, gam2, tau0):
    m = V.shape[0]
    P = np.eye(m) - np.ones((m, m)) / m
    PVP = P @ V @ P
    xb = V.mean(1)                     # V^{alpha xbar}
    xbxb = V.mean()
    Vbar = np.trace(V) / m
    S1 = lambda a, d, b, w: V[a, b] * (V[d, w] - xb[d] - xb[w] + xbxb)
    S2 = lambda a, d: V[a, a] * (V[d, d] - 2 * xb[d] + 2 * xbxb - Vbar)
    B = np.zeros((m, m))
    for a in range(m):
        for bb in range(m):
            t1 = sum(V[nu, ka] * S1(a, nu, bb, ka) for nu in range(m) for ka in range(m)) / m ** 2
            t2 = sum(V[bb, nu] * S2(a, nu) + V[a, nu] * S2(bb, nu) for nu in range(m)) / (2 * m)
            B[a, bb] = gam2 / tau0 ** 2 * (t1 + t2)
    return B


def b_mc(V, gam2, tau0, n, nk, reps, rng):
    m = V.shape[0]
    L = np.linalg.cholesky(V)
    tau = tau0 * np.sqrt(n * nk)
    acc = np.zeros((m, m)); = np.zeros((m, m))
    for _ in range(reps // 2000):
        G1 = rng.standard_normal((2000, m, nk)); G2 = rng.standard_normal((2000, m, nk))
        Y = L @ G1 @ np.swapaxes(G2, 1, 2) @ L.T
        D = 0
        for sgn in (1.0, -1.0):                # antithetic pair: the first-order (odd) term cancels exactly
            Z = sgn * Y / tau
            Z = Z - Z.max(2, keepdims=True)
            E = np.exp(Z); Sm = E / E.sum(2, keepdims=True)
            S = Sm - 1.0 / m
            D = D + 0.5 * (S @ V + V @ np.swapaxes(S, 1, 2) + S @ V @ np.swapaxes(S, 1, 2))
        acc += D.sum(0); += (D ** 2).sum(0)
    mean = acc / reps; se = np.sqrt(np.maximum(acc2 / reps - mean ** 2, 0) / reps)
    return gam2 * n * mean, gam2 * n * se


rng = np.random.default_rng(1)
gam2, tau0 = 0.5, 1.0
for m in (2, 4):
    for name, V in (("I", np.eye(m)), ("corr0.2", 0.8 * np.eye(m) + 0.2), ("random", None)):
        if V is None:
            A_ = rng.standard_normal((m, m)); V = A_ @ A_.T / m + 0.3 * np.eye(m)
        Bp = b_paper(V, gam2, tau0)
        Bm, se = b_mc(V, gam2, tau0, n=4000, nk=64, reps=200000, rng=rng)
        print("m %d V %-8s paper diag %s off01 %.4f | MC diag %s off01 %.4f (max se %.4f)" % (
            m, name, np.round(np.diag(Bp), 4), Bp[0, 1], np.round(np.diag(Bm), 4), Bm[0, 1], se.max()), flush=True)
    print("  ray check m %d: b(sI)/s^3 at s=1,3: %.5f %.5f ; claimed gam^2 (m-1)/(tau0^2 m^2) = %.5f" % (
        m, b_paper(np.eye(m), gam2, tau0)[0, 0], b_paper(3 * np.eye(m), gam2, tau0)[0, 0] / 27, gam2 * (m - 1) / m ** 2), flush=True)
