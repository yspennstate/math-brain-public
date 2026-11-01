"""Aldous-Fill Open Problem 4.48: (a) is tau_1 <= tau_0 ?  (b) is tau_2 <= tau_1^(2) ?
Continuous-time finite reversible chains. Random search with exact linear algebra (numpy), bisection for tau_1.
tau_0 = Kemeny constant = sum_j Z_jj ; tau_2 = 1/lambda_2 ; tau_1 = inf{t: dbar(t) <= 1/e}, dbar(t) = max_{ij} TV(P_i(X_t), P_j(X_t));
tau_1^(2) = max_i min{E_i U : U stopping rule with P_i(X_U in .) = pi} = max_{i,j} (E_i T_j - E_pi T_j) = max_{ij} (-Z_ij/pi_j)  (Lovasz-Winkler).
"""
import numpy as np, sys
rng = np.random.default_rng(int(sys.argv[1]) if len(sys.argv) > 1 else 0)

def params(W):
    """W symmetric nonnegative weights (zero diagonal allowed), continuous-time chain with rates q_ij = W_ij (so pi uniform? no: rates q_ij = W_ij / w_i gives pi_i = w_i/w). Use q_ij = W_ij / w_i."""
    n = W.shape[0]; w = W.sum(1)
    if np.any(w <= 0): return None
    Q = W / w[:, None]; np.fill_diagonal(Q, 0); np.fill_diagonal(Q, -Q.sum(1))
    pi = w / w.sum()
    Pi = np.tile(pi, (n, 1))
    Z = np.linalg.inv(Pi - Q) - Pi
    tau0 = np.trace(Z)
    # eigen: symmetrize D^{1/2} (-Q) D^{-1/2}
    d = np.sqrt(pi); S = (d[:, None] * (-Q)) / d[None, :]; S = (S + S.T) / 2
    ev, U = np.linalg.eigh(S)
    lam = np.sort(ev)
    if lam[1] <= 1e-12: return None
    tau2 = 1.0 / lam[1]
    tau12 = np.max(-Z / pi[None, :])
    # tau1 via dbar(t): P_t = D^{-1/2} U e^{-t ev} U^T D^{1/2}
    def dbar(t):
        Pt = (U * np.exp(-t * ev)) @ U.T
        Pt = Pt / d[:, None] * d[None, :]
        m = 0.0
        for i in range(n):
            for j in range(i + 1, n):
                m = max(m, 0.5 * np.abs(Pt[i] - Pt[j]).sum())
        return m
    lo, hi = 0.0, 1.0
    while dbar(hi) > np.exp(-1): hi *= 2
    for _ in range(60):
        mid = (lo + hi) / 2
        if dbar(mid) > np.exp(-1): lo = mid
        else: hi = mid
    tau1 = hi
    return tau0, tau1, tau2, tau12

best_a = (0, None); best_b = (0, None); cnt = 0
for trial in range(int(sys.argv[2]) if len(sys.argv) > 2 else 20000):
    n = rng.integers(3, 7)
    kind = rng.integers(0, 4)
    W = np.zeros((n, n))
    if kind == 0:   # random complete weights, heavy-tailed
        W = np.exp(rng.normal(0, 2.5, (n, n))); W = np.triu(W, 1); W = W + W.T
    elif kind == 1: # random tree / sparse
        for v in range(1, n):
            u = rng.integers(0, v); W[u, v] = W[v, u] = np.exp(rng.normal(0, 2.5))
        for _ in range(rng.integers(0, n)):
            u, v = rng.integers(0, n, 2)
            if u != v: W[u, v] = W[v, u] = np.exp(rng.normal(0, 2.5))
    elif kind == 2: # path with self-loops (loops add holding: implement as diagonal weight -> slows the state)
        for v in range(1, n): W[v-1, v] = W[v, v-1] = np.exp(rng.normal(0, 2.5))
        for v in range(n): W[v, v] = np.exp(rng.normal(0, 3))
    else:           # complete with loops
        W = np.exp(rng.normal(0, 2.5, (n, n))); W = np.triu(W); W = W + W.T - np.diag(np.diag(W))
    r = params(W)
    if r is None: continue
    tau0, tau1, tau2, tau12 = r
    cnt += 1
    ra = tau1 / tau0; rb = tau2 / tau12
    if ra > best_a[0]: best_a = (ra, (n, kind, W.round(4)))
    if rb > best_b[0]: best_b = (rb, (n, kind, W.round(4)))
print("chains tested:", cnt)
print("(a) max tau1/tau0 =", best_a[0]); print(best_a[1])
print("(b) max tau2/tau1^(2) =", best_b[0]); print(best_b[1])
