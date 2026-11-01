"""Aldous-Fill Conjecture 9.22: trace(Z^2 (P* - P)) >= 0 for every irreducible finite chain (discrete time).
Z = (I - P + Pi)^{-1} - Pi, P* = time reversal, (P*)_{ij} = pi_j P_{ji} / pi_i.
Random search over 3..6-state chains; report the most negative value with its chain. Also Proposition 9.21 as a control (trace Z (P*-P) >= 0 must hold)."""
import numpy as np, sys
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def fundamental(P):
    n = P.shape[0]
    ev, V = np.linalg.eig(P.T)
    k = np.argmin(np.abs(ev - 1)); pi = np.real(V[:, k]); pi = pi / pi.sum()
    Pi = np.tile(pi, (n, 1))
    Z = np.linalg.inv(np.eye(n) - P + Pi) - Pi
    return pi, Z
worst = (np.inf, None); ctrl = np.inf; cnt = 0
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 200000):
    n = rng.integers(3, 7)
    kind = rng.integers(0, 3)
    if kind == 0:
        P = rng.dirichlet(np.ones(n) * rng.uniform(0.1, 2.0), size=n)
    elif kind == 1:   # sparse: cycle plus a few random edges
        P = np.zeros((n, n))
        for i in range(n): P[i, (i + 1) % n] = rng.uniform(0.1, 1)
        for _ in range(rng.integers(1, n + 1)):
            i, j = rng.integers(0, n, 2); P[i, j] += rng.uniform(0, 1)
        P = P / P.sum(1, keepdims=True)
    else:             # near-deterministic permutation plus noise
        perm = rng.permutation(n); P = np.full((n, n), 1e-3)
        for i in range(n): P[i, perm[i]] += rng.uniform(0.5, 5)
        P = P / P.sum(1, keepdims=True)
    try:
        pi, Z = fundamental(P)
    except np.linalg.LinAlgError:
        continue
    if np.any(pi <= 1e-12): continue
    Ps = (pi[None, :] * P.T) / pi[:, None]
    t1 = np.trace(Z @ (Ps - P)); t2 = np.trace(Z @ Z @ (Ps - P))
    cnt += 1
    ctrl = min(ctrl, t1)
    if t2 < worst[0]: worst = (t2, P.copy())
print("chains:", cnt, " control min trace Z(P*-P) =", ctrl, " (must be >= 0)")
print("min trace Z^2(P*-P) =", worst[0])
np.set_printoptions(precision=5, suppress=True)
print(worst[1])
