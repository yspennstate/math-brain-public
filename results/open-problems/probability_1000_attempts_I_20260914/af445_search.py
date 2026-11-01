"""Aldous-Fill Open Problem 4.45: is tau_1^(2) of an induced (lumped, stationary-flow) chain at most K tau_1^(2) of the original, for an absolute K? For K = 1?
Continuous-time reversible chains; tau_1^(2) = max_{i,j} (E_i T_j - E_pi T_j) = max_{ij} (-Z_ij / pi_j) (halting-state theorem).
Induced chain on a partition f: hat pi(a) = sum_{i in a} pi_i, rates hat q(a,b) = sum_{i in a, j in b} pi_i q_ij / hat pi(a).
Random search over 3..6-state chains and all partitions (set partitions via restricted growth strings)."""
import numpy as np, sys, itertools
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
def tau12(Q):
    n = Q.shape[0]
    ev, V = np.linalg.eig(Q.T); k = np.argmin(np.abs(ev)); pi = np.real(V[:, k]); pi = pi / pi.sum()
    Pi = np.tile(pi, (n, 1)); Z = np.linalg.inv(Pi - Q) - Pi
    return np.max(-Z / pi[None, :]), pi
def partitions(n):
    def rec(i, cur, m):
        if i == n: yield list(cur); return
        for b in range(m + 1):
            cur.append(b); yield from rec(i + 1, cur, max(m, b + 1)); cur.pop()
    for p in rec(0, [], 0):
        if 1 < max(p) + 1 < n: yield p
best = (0, None)
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 3000):
    n = rng.integers(3, 7)
    W = np.exp(rng.normal(0, 2.0, (n, n))); W = np.triu(W); W = W + W.T - np.diag(np.diag(W))
    mask = rng.random((n, n)) < 0.4; mask = np.triu(mask, 1); W[mask | mask.T] = 0.0   # sparsify
    w = W.sum(1)
    if np.any(w <= 0): continue
    Q = W / w[:, None]; np.fill_diagonal(Q, 0); np.fill_diagonal(Q, -Q.sum(1))
    # connectivity check via eigenvalue zero multiplicity
    if np.sum(np.abs(np.linalg.eigvals(Q)) < 1e-9) != 1: continue
    t_orig, pi = tau12(Q)
    for p in partitions(n):
        m = max(p) + 1
        hatpi = np.zeros(m); Qh = np.zeros((m, m))
        for i in range(n): hatpi[p[i]] += pi[i]
        for i in range(n):
            for j in range(n):
                if i != j and p[i] != p[j]: Qh[p[i], p[j]] += pi[i] * Q[i, j]
        Qh = Qh / hatpi[:, None]; np.fill_diagonal(Qh, -Qh.sum(1))
        if np.sum(np.abs(np.linalg.eigvals(Qh)) < 1e-9) != 1: continue
        t_ind, _ = tau12(Qh)
        r = t_ind / t_orig
        if r > best[0]: best = (r, (n, p, W.round(4), t_orig, t_ind))
print("max tau12(induced)/tau12(original) =", best[0])
print(best[1])
