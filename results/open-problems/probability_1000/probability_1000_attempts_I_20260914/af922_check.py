"""Numerical check of the proof of Aldous-Fill Conjecture 9.22.
With S = D^{1/2} P D^{-1/2}, s = sqrt(pi), N = S - s s^T, A = (N+N^T)/2, B = (N-N^T)/2, M_s = I - sA, C_s = s M_s^{-1/2} B M_s^{-1/2}:
 (1) Ftilde(s) := tr((I - sN)^{-1} (N^T - N)) equals (4/s) * sum over eigenvalue pairs of theta^2/(1+theta^2), theta = |eigs of C_s|;
 (2) Phi(s) := s Ftilde(s) is nondecreasing on (0,1];
 (3) Phi'(1) = tr(Z^2 (P* - P)) with Z = (I - P + Pi)^{-1} - Pi, P* = D^{-1} P^T D.
Random chains including periodic ones."""
import numpy as np, sys
from scipy.linalg import sqrtm
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def chain(n, kind):
    if kind == 0: P = rng.dirichlet(np.ones(n) * 0.3, size=n)
    elif kind == 1:
        P = np.zeros((n, n))
        for i in range(n): P[i, (i + 1) % n] = 1.0        # periodic cycle
        P = 0.9 * P + 0.1 * rng.dirichlet(np.ones(n), size=n) if rng.random() < 0.5 else P
    else:
        perm = rng.permutation(n); P = np.full((n, n), 1e-4)
        for i in range(n): P[i, perm[i]] += rng.uniform(0.5, 5)
        P = P / P.sum(1, keepdims=True)
    ev, V = np.linalg.eig(P.T); k = np.argmin(np.abs(ev - 1)); pi = np.real(V[:, k]); pi = pi / pi.sum()
    return P, pi
worst_mono = np.inf; worst_id = np.inf; worst_deriv = np.inf; cnt = 0
for t in range(int(sys.argv[2]) if len(sys.argv) > 2 else 3000):
    n = rng.integers(2, 7); kind = rng.integers(0, 3)
    P, pi = chain(n, kind)
    if np.any(pi <= 1e-10): continue
    if np.sum(np.abs(np.linalg.eigvals(P) - 1) < 1e-9) != 1: continue   # irreducible check (simple eigenvalue 1)
    d = np.sqrt(pi); S = (d[:, None] * P) / d[None, :]; sh = d
    N = S - np.outer(sh, sh); A = (N + N.T) / 2; B = (N - N.T) / 2
    Pi = np.tile(pi, (n, 1)); Z = np.linalg.inv(np.eye(n) - P + Pi) - Pi; Ps = (pi[None, :] * P.T) / pi[:, None]
    target = np.trace(Z @ Z @ (Ps - P))
    ss = np.linspace(0.02, 1.0, 50)
    Phi = []
    for s in ss:
        R = np.linalg.inv(np.eye(n) - s * N)
        Ft = np.trace(R @ (N.T - N))
        Ms = np.eye(n) - s * A
        Mi = np.linalg.inv(np.real(sqrtm(Ms)))
        C = s * Mi @ B @ Mi
        th = np.abs(np.linalg.eigvals(C)); th = np.sort(th)[::-1]
        # pairs: eigenvalues come as +-i theta, take every other of the sorted magnitudes (zeros at the end)
        pairs = th[0::2][: n // 2]
        Ft2 = (4 / s) * np.sum(pairs ** 2 / (1 + pairs ** 2))
        worst_id = min(worst_id, -abs(Ft - Ft2))
        Phi.append(s * Ft)
    Phi = np.array(Phi)
    worst_mono = min(worst_mono, np.min(np.diff(Phi)))
    # derivative at 1 by finite difference vs target
    h = 1e-5
    R1 = np.linalg.inv(np.eye(n) - N); Rh = np.linalg.inv(np.eye(n) - (1 - h) * N)
    d1 = (np.trace(R1 @ (N.T - N)) * 1 - (1 - h) * np.trace(Rh @ (N.T - N))) / h
    worst_deriv = min(worst_deriv, -abs(d1 - target) / (1 + abs(target)))
    cnt += 1
print("chains:", cnt)
print("max |Ftilde - (4/s) sum g(theta)| :", -worst_id)
print("min increment of Phi(s) over the grid (must be >= 0 up to rounding):", worst_mono)
print("max rel |Phi'(1) - tr Z^2 (P*-P)| :", -worst_deriv)
